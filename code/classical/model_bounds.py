"""Exact outward model bounds only. No LP, fitting, or price solver."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import hashlib,json,time

ROOT=Path(__file__).resolve().parent
BITS=160; SCALE=1<<BITS; H=F(1,768); D=F(27,200); XI2=F(529,10000)
FREEZE_SHA='4fb9c383d752bbd89bbf58bdb9b6b5225a4c1d07baab308202fd4d554c0b3635'
def dn(x): return F((x.numerator*SCALE)//x.denominator,SCALE)
def up(x): return -dn(-x)
def sqrtbox(x):
    assert x>=0
    n=isqrt((x.numerator*SCALE*SCALE)//x.denominator)
    lo=F(n,SCALE); hi=lo if lo*lo==x else lo+F(1,SCALE)
    assert lo*lo<=x<=hi*hi
    return lo,hi
def expbox(x):
    if x<0:
        l,u=expbox(-x);return dn(1/u),up(1/l)
    k=0;y=x
    while y>F(1,8): y/=2;k+=1
    term=F(1);s=term
    for n in range(1,41):term=term*y/n;s+=term
    nxt=term*y/41
    lo=dn(s);hi=up(s+nxt/(1-y/42))
    for _ in range(k):lo=dn(lo*lo);hi=up(hi*hi)
    return lo,hi
def cadd(a,b):return a[0]+b[0],a[1]+b[1]
def cscale(a,x):return a[0]*x,a[1]*x
def cmul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def norm(a):return sqrtbox(a[0]*a[0]+a[1]*a[1])[1]
def lap(t,eta,c,d,v):
    lo=hi=t;sl=su=F(0);guards=True
    for n in range(767):
        assert lo>=0 and hi<=eta/(2*c) # f monotone on the entire enclosure
        sl=dn(sl+lo);su=up(su+hi)
        lo=dn(eta*lo-c*lo*lo);hi=up(eta*hi-c*hi*hi)
        assert lo>=0
    al=d*H*sl+v*lo;au=d*H*su+v*hi
    return expbox(-au)[0],expbox(-al)[1],{'t767':[lo,hi],'sum':[sl,su],'guard':guards}
def make_P():
    lower=[F(0)]+[F(r-1,100) for r in range(1,101)]+[F(1)]
    upper=[F(0)]+[F(r,100) for r in range(1,101)]+[None]
    ts=[F(1),F(4),F(16),F(64),F(256),F(191,192)**2/(2*F(49,625))/H]
    rows=[];rhs=[];names=[];records=[]
    def add(a,b,name):rows.append(a);rhs.append(b);names.append(name)
    for t in ts:
        a=[expbox(-t*u)[0] if u is not None else F(0) for u in upper]
        for name,eta,c,d,v in [('ref',F(191,192),F(49,625)*H/2,F(3,50),F(3,100)),('point',F(255,256),XI2*H/2,D,F(9,200))]:
            ll,uu,rec=lap(t,eta,c,d,v);add(a,uu,f'upper_{name}_{t}')
            records.append({'name':name,'t':t,'L':[ll,uu],**rec})
        a=[-expbox(-t*l)[1] for l in lower]
        b=-expbox(-t*F(7,150))[0]
        add(a,b,f'lower_Jensen_{t}')
    add(lower,F(7,150),'mean_point')
    add([expbox(4*l)[0] for l in lower],F(5,4),'exp4_point')
    add([F(1)]*102,F(1),'mass_upper');add([F(-1)]*102,F(-1),'mass_lower')
    return lower,upper,rows,rhs,names,records
def envelope(p,w,lower,upper):
    q=(p,F(w));g=cscale(cadd(cmul(q,q),cscale(q,-1)),F(1,2))
    L=cadd(cscale(q,F(-253,2000)),(F(-3),F(0)));c=XI2/2
    b1=g;b2=cscale(cmul(L,g),F(1,2))
    b3=cscale(cadd(cmul(cmul(L,L),g),cscale(cmul(g,g),2*c)),F(1,6))
    # Re P(s)<=0 for the whole step; exact rational barrier check.
    assert b1[0]+max(b2[0],F(0))*H+max(b3[0],F(0))*H*H<0
    assert p*(p-1)/2-F(279,800)*w*w<0
    rr=[cadd(cmul(L,b3),cscale(cmul(b1,b2),2*c)),cscale(cadd(cscale(cmul(b1,b3),2),cmul(b2,b2)),c),cscale(cmul(b2,b3),2*c),cscale(cmul(b3,b3),c)]
    mods=[norm(x) for x in rr]
    eb=up(sum((mods[k-3]*H**(k+1)/F(k+1) for k in range(3,7)),F(0)))
    ea=up(D*sum((mods[k-3]*H**(k+2)/F((k+1)*(k+2)) for k in range(3,7)),F(0)))
    bc=cadd(cadd(cscale(b1,H),cscale(b2,H*H)),cscale(b3,H**3))
    da=cscale(cadd(cadd(cscale(b1,H*H/2),cscale(b2,H**3/3)),cscale(b3,H**4/4)),-D)
    db=cadd(cscale(g,H),cscale(bc,-1))
    bplus=min(F(0),bc[0]+eb);lam=max(H*g[0],bplus);m=2-lam
    ap=up(norm(da)+ea);bp=up(norm(db)+eb)
    al=up(D*norm(g)*H*H/2);bl=up((norm(L)+XI2*norm(g)*H)*norm(g)*H*H/2)
    aa=min(ap,al);bb=min(bp,bl);assert m>0 and aa>=0 and bb>0
    peak=1/m-aa/bb
    hs=[];branches=[]
    pref=expbox(2*p*F(1,100)*H)[1]
    for l,u in zip(lower,upper):
        candidates=[l]
        if u is not None:candidates.append(u)
        if peak>=l and (u is None or peak<=u):candidates.append(peak)
        val=max(up((aa+bb*x)*expbox(-m*x)[1]) for x in candidates)
        split=up(pref*val*val);coarse=up(4*expbox(2*p*F(1,100)*H-4*l)[1])
        hs.append(min(split,coarse));branches.append('split' if split<=coarse else 'coarse')
    # First entry is the atom, whose u=l=0; infinite last-band limit=0.
    return hs,{'p':p,'w':w,'g':g,'L':L,'b1':b1,'b2':b2,'b3':b3,'r':rr,'E_B':eb,'E_A':ea,'bc':bc,'delta_a_center':da,'delta_b_center':db,'A_pol':ap,'B_pol':bp,'A_loc':al,'B_loc':bl,'A':aa,'B':bb,'m':m,'peak':peak,'branches':branches,'projection_exact_zero':True,'barriers':True}


def encode(x):
    if isinstance(x,F):return f'{x.numerator}/{x.denominator}'
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x
