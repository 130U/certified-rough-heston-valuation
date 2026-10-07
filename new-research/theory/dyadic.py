"""Exact outward-rounded dyadic interval certificate; Python standard library only.

This is a sign certificate, not a solution-error or option-price certificate.
All arithmetic endpoints are integers with the common denominator 2**100.
The finite frequency cover is checked using Cramer's rule only after the raw
matrix determinant is excluded from zero.  No binary64 value enters a test.
"""
from fractions import Fraction as F
from math import isqrt

BITS=100
S=1<<BITS

def ceildiv(a,b): return -((-a)//b)

class I:
    __slots__=('lo','hi')
    def __init__(self,x=0,hi=None,raw=False):
        if raw: self.lo,self.hi=x,hi
        else:
            x=F(x); self.lo=(x.numerator*S)//x.denominator
            self.hi=ceildiv(x.numerator*S,x.denominator)
    def __add__(a,b):
        b=iv(b);return I(a.lo+b.lo,a.hi+b.hi,True)
    __radd__=__add__
    def __neg__(a):return I(-a.hi,-a.lo,True)
    def __sub__(a,b):return a+-iv(b)
    def __rsub__(a,b):return iv(b)+-a
    def __mul__(a,b):
        b=iv(b);v=[a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi]
        return I(min(v)//S,ceildiv(max(v),S),True)
    __rmul__=__mul__
    def recip(a):
        assert a.lo>0 or a.hi<0,(a.lo,a.hi)
        return I((S*S)//a.hi,ceildiv(S*S,a.lo),True)
    def __truediv__(a,b):return a*iv(b).recip()
    def __rtruediv__(a,b):return iv(b)*a.recip()
    def __pow__(a,n):
        assert isinstance(n,int) and n>=0
        result=I(1)
        while n:
            if n&1:result=result*a
            a=a*a;n//=2
        return result
    def square(a):
        lo=0 if a.lo<=0<=a.hi else min(a.lo*a.lo,a.hi*a.hi)
        return I(lo//S,ceildiv(max(a.lo*a.lo,a.hi*a.hi),S),True)
    def sqrt(a):
        assert a.lo>=0
        lo=isqrt(a.lo*S);hi=isqrt(a.hi*S)
        if hi*hi<a.hi*S:hi+=1
        return I(lo,hi,True)
    def bounds(a):return [str(F(a.lo,S)),str(F(a.hi,S))]

def iv(x):return x if isinstance(x,I) else I(x)

class C:
    __slots__=('re','im')
    def __init__(self,re=0,im=0):self.re,self.im=iv(re),iv(im)
    def __add__(a,b):
        b=cv(b);return C(a.re+b.re,a.im+b.im)
    __radd__=__add__
    def __neg__(a):return C(-a.re,-a.im)
    def __sub__(a,b):return a+-cv(b)
    def __rsub__(a,b):return cv(b)+-a
    def __mul__(a,b):
        b=cv(b);return C(a.re*b.re-a.im*b.im,a.re*b.im+a.im*b.re)
    __rmul__=__mul__
    def conj(a):return C(a.re,-a.im)
    def norm2(a):return a.re.square()+a.im.square()
    def recip(a):
        n=a.norm2();assert n.lo>0
        return C(a.re/n,-a.im/n)
    def __truediv__(a,b):return a*cv(b).recip()
    def __rtruediv__(a,b):return cv(b)*a.recip()
    def __pow__(a,n):
        result=C(1)
        while n:
            if n&1:result=result*a
            a=a*a;n//=2
        return result
    def sqrt_positive_real(a):
        # Our discriminant has strictly positive real part; this fixes the branch.
        assert a.re.lo>0
        r=((a.norm2().sqrt()+a.re)/2).sqrt()
        return C(r,a.im/(2*r))

def cv(x):return x if isinstance(x,C) else C(x)

def log_unit(x):
    # x lies in [1,2].  atanh z, z in [0,1/3]; N=100 with an explicit tail.
    z=(x-1)/(x+1);assert z.lo>=0 and z.hi<S
    z2=z.square();term=z;total=I(0)
    for k in range(100):total+=term/F(2*k+1);term=term*z2
    tail=2*term/(201*(1-z2))
    return 2*total+I(0,tail.hi,True)

LOG2=log_unit(I(2))
def log_pos(x):
    x=iv(x);assert x.lo>0
    k=0
    while x.lo< S:x=x*2;k-=1
    while x.hi>2*S:x=x/2;k+=1
    return log_unit(x)+k*LOG2

def atan_recip(q):
    z=I(F(1,q));z2=z.square();term=z;total=I(0)
    for k in range(100):
        total=total+((-1)**k)*term/F(2*k+1);term=term*z2
    # First omitted term is positive because 100 is even.
    bound=term/201
    return total+I(0,bound.hi,True)

PI=16*atan_recip(5)-4*atan_recip(239)

def exp_positive(x):
    # x>0; scaling to [0,1], positive Taylor and geometric tail, then squaring.
    assert x.lo>=0
    k=0
    while x.hi>S:x=x/2;k+=1
    total=I(1);term=I(1)
    for n in range(1,101):term=term*x/n;total+=term
    nextterm=term*x/101
    tail=nextterm/(1-x/102)
    result=total+I(0,tail.hi,True)
    for _ in range(k):result=result.square()
    return result

B=[F(1,6),F(-1,30),F(1,42),F(-1,30),F(5,66),F(-691,2730),
   F(7,6),F(-3617,510),F(43867,798),F(-174611,330),F(854513,138)]

def gamma_positive(q):
    q=F(q);assert q>0
    shift=max(0,ceildiv((20-q).numerator,(20-q).denominator))
    z=I(q+shift)
    lg=(z-F(1,2))*log_pos(z)-z+log_pos(2*PI)/2
    for k in range(1,11):lg+=B[k-1]/(2*k*(2*k-1)*z**(2*k-1))
    # Positive real log-Gamma remainder after B20: [0, B22/(22*21*z**21)].
    tail=B[10]/(22*21*z**21);lg+=I(0,tail.hi,True)
    value=exp_positive(lg)
    for j in range(shift):value=value/(q+j)
    return value

