"""Certified moments of the frozen forward curve; integer interval arithmetic.

This is an integration component, not a complete price certificate.  The field
coefficients supplied to it are exact dyadic numbers, with no solver claim.
The curve and its time exponent are frozen independently of candidate alpha.
"""
from fractions import Fraction as F
import importlib.util, json
from pathlib import Path

spec=importlib.util.spec_from_file_location('dyadic',Path(__file__).with_name('interval-pade-certificate.py'))
dy=importlib.util.module_from_spec(spec);spec.loader.exec_module(dy)
I,S=dy.I,dy.S
ALPHA0=F(2643,5000); LAMBDA=F(5037,10000)
V0=F(131,5000); THETA=F(721,10000)

def signed_exp(x):
    if x.lo>=0:return dy.exp_positive(x)
    if x.hi<=0:return dy.exp_positive(-x).recip()
    a=dy.exp_positive(I(-x.lo,-x.lo,True)).recip()
    b=dy.exp_positive(I(x.hi,x.hi,True))
    return I(a.lo,b.hi,True)

def log_endpoint(q):
    # Exact rational scaling puts q in [1,2]; outward rounding cannot force an
    # infinite rescale loop for an interval that straddles a power of two.
    q=F(q); assert q>0
    k=0
    while q<1:q*=2;k-=1
    while q>2:q/=2;k+=1
    return dy.log_unit(I(q))+k*dy.LOG2

def power(q,a):
    q=F(q);a=F(a)
    if q==0:
        assert a>0
        return I(0)
    return signed_exp(a*log_endpoint(q))

def moments(z,terms=48):
    """Intervals for integral_0^z xi(s)ds and integral_0^z s xi(s)ds.

    Alternating series is evaluated with an absolute geometric remainder.
    Gamma(x) is increasing for x>=2 (log-convexity and Gamma(1)=Gamma(2)=1).
    Here lambda*z**alpha0<1, so both denominator ratios are <=1.
    """
    z=F(z);assert 0<=z<=2
    if z==0:return I(0),I(0)
    zi=I(z);w=LAMBDA*power(z,ALPHA0);assert w.hi<S
    term=I(1);e2=I(0);e3=I(0)
    for n in range(terms):
        e2+=term/gamma_cached(2+n*ALPHA0)
        e3+=term/gamma_cached(3+n*ALPHA0)
        term=-term*w
    # |term|<=w**terms; denominator Gamma>=1.  Symmetric tail is rigorous.
    tail=(w**terms)/(1-w)
    rem=I(-tail.hi,tail.hi,True)
    e2+=rem;e3+=rem
    j0=THETA*zi+(V0-THETA)*zi*e2
    j1=THETA*zi.square()/2+(V0-THETA)*zi.square()*(e2-e3)
    return j0,j1

GAMMA_CACHE={}
def gamma_cached(q):
    q=F(q)
    if q not in GAMMA_CACHE:GAMMA_CACHE[q]=dy.gamma_positive(q)
    return GAMMA_CACHE[q]

def linear_field_weights(nodes,T,terms=48):
    """Nonnegative weights for integral_0^T xi(T-t)*linear_field(t)dt.

    Each input node is an exact rational.  Returned coefficient intervals
    contain the exact integration weights.  No time quadrature is used.
    """
    nodes=list(map(F,nodes));T=F(T)
    assert nodes[0]==0 and nodes[-1]==T
    assert all(a<b for a,b in zip(nodes,nodes[1:]))
    vals=[moments(T-t,terms) for t in nodes]
    weights=[I(0) for _ in nodes]
    for j,(left,right) in enumerate(zip(nodes,nodes[1:])):
        A=T-right;B=T-left;h=right-left
        J0=vals[j][0]-vals[j+1][0];J1=vals[j][1]-vals[j+1][1]
        wl=(J1-A*J0)/h;wr=(B*J0-J1)/h
        # Positivity follows from xi>=V0>0 and hat bases >=0.  Intersection
        # with this proved condition tightens rounding width, never guesses.
        wl=I(max(0,wl.lo),wl.hi,True);wr=I(max(0,wr.lo),wr.hi,True)
        assert wl.hi>=0 and wr.hi>=0
        weights[j]+=wl;weights[j+1]+=wr
    return weights

def power_field_moment(beta,T,terms=64):
    """Exact integral xi(T-t)*t**beta, with the same explicit ML remainder."""
    beta=F(beta);T=F(T);assert beta>=0 and 0<T<=2
    w=LAMBDA*power(T,ALPHA0);assert w.hi<S
    term=I(1);ml=I(0)
    for n in range(terms):
        ml+=term/gamma_cached(beta+2+n*ALPHA0)
        term=-term*w
    tail=w**terms/(1-w);ml+=I(-tail.hi,tail.hi,True)
    p=power(T,beta+1)
    return THETA*p/(beta+1)+(V0-THETA)*gamma_cached(beta+1)*p*ml
