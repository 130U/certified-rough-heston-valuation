"""Outward IEEE-binary64 interval certificate for a fixed fractional PI field.

No libm log/exp/power is trusted: each uses finite series and explicit tails.
Dot products are NumPy diagnostics plus the proved gamma_(2n) error enclosure.
Every saved field component is interpreted as its exact binary dyadic value.
This first implementation certifies a point alpha and the specified fixed
frequency nodes; it does not certify all alpha values or continuous frequency.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import importlib.util, argparse, hashlib, json, math, sys, time
import numpy as np

BASE=Path(__file__).resolve().parents[1]/'reference'/'code'/'src'
spec=importlib.util.spec_from_file_location('dyadic',BASE/'interval-pade-certificate.py')
D=importlib.util.module_from_spec(spec);spec.loader.exec_module(D)
spec_c=importlib.util.spec_from_file_location('combined',BASE/'combined-field-derivative.py')
C=importlib.util.module_from_spec(spec_c);spec_c.loader.exec_module(C)
COMBINED_SOURCE_HASH=hashlib.sha256((BASE/'combined-field-derivative.py').read_bytes()).hexdigest()
DN=lambda x:np.nextafter(x,-np.inf)
UP=lambda x:np.nextafter(x,np.inf)
ZERO=np.float64(0.)

def pair(x):return x if isinstance(x,tuple) else (np.asarray(x),np.asarray(x))
def add(a,b):a,b=pair(a),pair(b);return DN(a[0]+b[0]),UP(a[1]+b[1])
def neg(a):a=pair(a);return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    a,b=pair(a),pair(b)
    vals=[a[j]*b[k] for j in range(2) for k in range(2)]
    return DN(np.minimum.reduce(vals)),UP(np.maximum.reduce(vals))
def div(a,b):
    b=pair(b);assert np.all((b[0]>0)|(b[1]<0))
    return mul(a,(DN(1/b[1]),UP(1/b[0])))
def square(a):
    a=pair(a);lo=np.where((a[0]<=0)&(a[1]>=0),0.,np.minimum(a[0]**2,a[1]**2))
    return np.maximum(0.,DN(lo)),UP(np.maximum(a[0]**2,a[1]**2))
def maximum_abs(a):a=pair(a);return UP(np.maximum(abs(a[0]),abs(a[1])))
def rational(q):
    q=F(q);x=float(q)
    return (np.float64(np.nextafter(x,-np.inf) if F.from_float(x)>q else x),
            np.float64(np.nextafter(x,np.inf) if F.from_float(x)<q else x))
@lru_cache(maxsize=None)
def gamma(q):
    a=D.gamma_positive(F(q));return rational(F(a.lo,D.S))[0],rational(F(a.hi,D.S))[1]
LOG2=(rational(F(D.LOG2.lo,D.S))[0],rational(F(D.LOG2.hi,D.S))[1])

def log_bounds(x):
    x=np.asarray(x);assert np.all(x>0)
    m,e=np.frexp(x);m=m*2;e=e-1 # exact scaling of normal binary64 values
    z=div(sub(m,1),add(m,1));z2=square(z);term=z;total=pair(np.zeros_like(x))
    for k in range(22):total=add(total,div(term,2*k+1));term=mul(term,z2)
    # tail <= 2*z^45/[45*(1-z^2)] after 22 terms; z>=0.
    tail=div(mul(2,term),mul(45,sub(1,z2)))
    return add(add(mul(2,total),(np.zeros_like(x),tail[1])),mul(e,LOG2))

def exp_bounds(x):
    x=pair(x)
    mid=(x[0]+x[1])/2
    k=np.floor(mid/float(F(D.LOG2.lo,D.S))).astype(np.int64)
    r=sub(x,mul(k,LOG2));assert np.all(maximum_abs(r)<1)
    # Horner degree24, |remainder| <= 3/25! for |r|<1; e<3.
    value=pair(np.full_like(mid,1./math.factorial(24)))
    # The constants 1/n! themselves require outward conversion.
    value=pair(np.zeros_like(mid));value=add(value,rational(F(1,math.factorial(24))))
    for n in range(23,-1,-1):value=add(mul(value,r),rational(F(1,math.factorial(n))))
    tail=rational(F(3,math.factorial(25)))[1]
    value=add(value,(-tail,tail))
    return DN(np.ldexp(value[0],k)),UP(np.ldexp(value[1],k))

def power(x,p):
    x=pair(x);p=pair(p)
    assert np.all(x[0]>=0)
    if p[0]>0:
        lower=np.where(x[0]==0,0.,1.);upper=np.where(x[1]==0,0.,1.)
        take=x[0]>0
        if np.any(take):
            q=mul(log_bounds(x[0][take] if np.ndim(x[0]) else x[0]),p)
            lower=np.asarray(lower);lower[take]=exp_bounds(q)[0]
        take=x[1]>0
        if np.any(take):
            q=mul(log_bounds(x[1][take] if np.ndim(x[1]) else x[1]),p)
            upper=np.asarray(upper);upper[take]=exp_bounds(q)[1]
        return lower,upper
    assert np.all(x[0]>0)
    logs=(log_bounds(x[0])[0],log_bounds(x[1])[1])
    return exp_bounds(mul(logs,p))

def cp(z):return (pair(np.asarray(z).real),pair(np.asarray(z).imag))
def cadd(a,b):return add(a[0],b[0]),add(a[1],b[1])
def cneg(a):return neg(a[0]),neg(a[1])
def csub(a,b):return cadd(a,cneg(b))
def cmul(a,b):return sub(mul(a[0],b[0]),mul(a[1],b[1])),add(mul(a[0],b[1]),mul(a[1],b[0]))
def cscale(a,b):return mul(a[0],b),mul(a[1],b)
def cabs(a):
    r,i=maximum_abs(a[0]),maximum_abs(a[1]);return UP(np.sqrt(UP(UP(r*r)+UP(i*i))))

def dot_interval(weights,values):
    """Enclose a real interval matrix times exact stored dyadic real matrix.

    For n products and any parenthesization: gamma_(2n) sum|w*v| plus underflow
    budget, with epsilon=2^-53. A conservative norm product replaces sum|w*v|.
    Center/radius formation is itself enclosed before the floating dot.
    """
    lo,hi=weights;n=lo.shape[1]
    center=(lo+hi)/2
    radius=UP(np.maximum(abs(center-lo),abs(hi-center)))
    out=center@values
    eps=2.**-53;g=rational(F(2*n,2**53-2*n))[1]
    # Bound each dot's rounding without trusting a second dot's arithmetic.
    l1center=UP(np.sum(abs(center),axis=1)/DN(1-g))
    l1radius=UP(np.sum(radius,axis=1)/DN(1-g))
    vmax=UP(np.max(abs(values),axis=0))
    rad=UP(UP(l1radius[:,None]*vmax[None,:])+UP(g*l1center[:,None]*vmax[None,:]))
    rad=UP(rad+np.nextafter(0.,1.)*(2*n+2))
    assert np.all(np.isfinite(out)) and np.all(np.isfinite(rad))
    return DN(out-rad),UP(out+rad)

def volterra_weights(q,t,alpha,derivative=False):
    """Exact positive kernel weights enclosed by directed arithmetic.

    Kernel order alpha.  Each t interval is truncated at q.  Small h/tau uses
    an eight-term positive binomial series; tail <= z^8/(1-z), since all
    coefficients (1-alpha)_k/k! are <=1 for alpha in (0,1).
    """
    q=np.asarray(q);left=t[:-1][None,:];right=t[1:][None,:]
    stop=np.minimum(q[:,None],right);active=stop>left
    tau=sub(q[:,None],left);h=sub(stop,left)
    # Avoid invalid inactive entries while preserving exact zero outputs.
    tau=(np.where(active,tau[0],1.),np.where(active,tau[1],1.))
    h=(np.where(active,h[0],1.),np.where(active,h[1],1.))
    z=div(h,tau);small=active&(z[1]<.01)
    # These arrays are mutated below: endpoint arrays must not alias.
    wl=(np.zeros_like(stop),np.zeros_like(stop))
    wr=(np.zeros_like(stop),np.zeros_like(stop))
    pa=rational(alpha);ga=gamma(alpha)
    if np.any(small):
        zs=(z[0][small],z[1][small]);ts=(tau[0][small],tau[1][small]);hs=(h[0][small],h[1][small])
        coef=pair(np.ones(np.count_nonzero(small)));sr=pair(np.zeros_like(coef[0]));sl=pair(np.zeros_like(coef[0]))
        for k in range(8):
            sr=add(sr,div(coef,k+2));sl=add(sl,div(coef,(k+1)*(k+2)))
            coef=mul(mul(coef,zs),div(sub(k+1,pa),k+1))
        tail=div(power(zs,8),sub(1,zs))
        sr=add(sr,(np.zeros_like(tail[1]),tail[1]));sl=add(sl,(np.zeros_like(tail[1]),tail[1]))
        factor=div(mul(power(ts,sub(pa,1)),hs),ga)
        for result,v in [(wr,mul(factor,sr)),(wl,mul(factor,sl))]:result[0][small]=v[0];result[1][small]=v[1]
    big=active&~small
    if np.any(big):
        ta=(tau[0][big],tau[1][big]);hh=(h[0][big],h[1][big])
        direct_end=sub(np.broadcast_to(q[:,None],stop.shape)[big],stop[big])
        at_query=(stop[big]==np.broadcast_to(q[:,None],stop.shape)[big])
        end=(np.where(at_query,0.,direct_end[0]),np.where(at_query,0.,direct_end[1]))
        end=(np.maximum(end[0],0.),np.maximum(end[1],0.))
        i0=div(sub(power(ta,pa),power(end,pa)),pa)
        i1=div(sub(power(ta,add(pa,1)),power(end,add(pa,1))),add(pa,1))
        rr=div(sub(mul(ta,i0),i1),hh);ll=sub(i0,rr)
        rr=div(rr,ga);ll=div(ll,ga)
        # The final truncated interval has a closed positive formula.
        last=at_query
        if np.any(last):
            last_h=(hh[0][last],hh[1][last])
            last_r=div(power(last_h,pa),mul(mul(pa,add(pa,1)),ga))
            rr[0][last]=last_r[0];rr[1][last]=last_r[1]
            last_l=mul(last_r,pa);ll[0][last]=last_l[0];ll[1][last]=last_l[1]
        for result,v in [(wr,rr),(wl,ll)]:result[0][big]=np.maximum(v[0],0.);result[1][big]=v[1]
    # Partial interval: convert wr to the stored complete-right-end coefficient.
    exact_width=sub(t[1:],t[:-1])
    ratio=div(h,(np.broadcast_to(exact_width[0],stop.shape),np.broadcast_to(exact_width[1],stop.shape)))
    ratio=(np.where(active,ratio[0],0.),np.where(active,ratio[1],0.))
    rr=mul(wr,ratio);ll=add(wl,mul(wr,sub(1,ratio)))
    if derivative:return add(wl,wr)
    return ll,rr

def linear_integral(q,t,LG,alpha):
    wl,wr=volterra_weights(q,t,alpha)
    return (add(dot_interval(wl,LG[:-1].real),dot_interval(wr,LG[1:].real)),
            add(dot_interval(wl,LG[:-1].imag),dot_interval(wr,LG[1:].imag)))

def derivative_interval(a,b,t,LG,alpha):
    # Old completed intervals have weights decreasing in q; the active current
    # interval weight increases.  This sign follows because alpha-1<0.
    wa=volterra_weights(a,t,alpha,True);wb=volterra_weights(b,t,alpha,True)
    left=t[:-1][None,:];right=t[1:][None,:]
    old=right<=a[:,None]
    low=np.where(old,wb[0],wa[0]);high=np.where(old,wa[1],wb[1])
    slopes=(LG[1:]-LG[:-1])/np.diff(t)[:,None]
    # These floating slopes are not exact: divide original exact dyadic
    # differences with directed rounding, and pass midpoint/radius separately.
    h=sub(t[1:],t[:-1])
    dr=sub(LG[1:].real,LG[:-1].real);di=sub(LG[1:].imag,LG[:-1].imag)
    sr=div(dr,(h[0][:,None],h[1][:,None]));si=div(di,(h[0][:,None],h[1][:,None]))
    def apply(s):
        mid=(s[0]+s[1])/2;rad=UP(np.maximum(abs(mid-s[0]),abs(s[1]-mid)))
        result=dot_interval((low,high),mid)
        extra=UP(UP(np.sum(high,axis=1)/DN(1-rational(F(2*len(t),2**53-2*len(t)))[1]))[:,None]*UP(np.max(rad,axis=0))[None,:])
        return DN(result[0]-extra),UP(result[1]+extra)
    return (apply(sr),apply(si)),(low,high)

def startup_coefficients(alpha,beta,u,A1,A2):
    nu=rational(F(2897,10000));rho=rational(F(-1489,2000))
    c=pair(-(u*u+.25)/2) # u is a dyadic multiple of 1/8, c is exact here
    d=(div(rho,2),mul(rho,u))
    B1=(div(mul(nu,c),gamma(1+alpha)),pair(np.zeros_like(u)))
    B2=cscale(cp(A1),div(gamma(1+beta),gamma(1+alpha+beta)))
    B3=cscale(cp(A2),div(gamma(1+2*beta),gamma(1+alpha+2*beta)))
    return nu,c,d,[B1,B2,B3]

def H0(t,B,alpha,beta,derivative=False):
    result=(pair(np.zeros((len(t),len(B[0][0][0])))),pair(np.zeros((len(t),len(B[0][0][0])))))
    for j,coef in enumerate(B):
        p=alpha+j*beta
        factor=power(pair(np.asarray(t)),rational(p-1 if derivative else p))
        if derivative:factor=mul(factor,rational(p))
        result=cadd(result,cscale(coef,(factor[0][:,None],factor[1][:,None])))
    return result

def residual_polynomial(B,A1,A2,nu,d,alpha,beta):
    assert alpha==beta
    # Constant nu*c cancels exactly; collect equal generalized powers before
    # any evaluation, including the two startup terms of the field.
    terms={}
    def term(p,z):terms[p]=cadd(terms.get(p,cp(np.zeros_like(A1))),z)
    term(alpha,cp(A1));term(2*alpha,cp(A2))
    for j,z in enumerate(B):term((j+1)*alpha,cneg(cscale(cmul(d,z),nu)))
    for j,z in enumerate(B):
        for k,w in enumerate(B):term((j+k+2)*alpha,cneg(cscale(cmul(z,w),div(nu,2))))
    return terms

def polynomial(t,terms,derivative=False):
    shape=(len(t[0]) if isinstance(t,tuple) else len(t),len(next(iter(terms.values()))[0][0]))
    out=(pair(np.zeros(shape)),pair(np.zeros(shape)))
    for p,z in terms.items():
        factor=power(t,rational(p-1 if derivative else p))
        if derivative:factor=mul(factor,rational(p))
        out=cadd(out,cscale(z,(factor[0][:,None],factor[1][:,None])))
    return out

def first_cell(t1,LG1,B,A1,A2,nu,c,d,alpha,beta):
    assert alpha==beta
    # Expand the residual in exact generalized powers, then bound each term.
    terms={}
    def term(p,z):terms[p]=cadd(terms.get(p,cp(np.zeros_like(LG1))),z)
    term(beta,cp(A1));term(2*beta,cp(A2));term(F(1),cscale(cp(LG1),div(1,t1)))
    HL=cscale(cp(LG1),div(1,mul(t1,gamma(2+alpha))))
    HH=[(alpha+j*beta,z) for j,z in enumerate(B)]+[(alpha+1,HL)]
    for p,z in HH:term(p,cneg(cscale(cmul(d,z),nu)))
    for p,z in HH:
        for q,w in HH:term(p+q,cneg(cscale(cmul(z,w),div(nu,2))))
    bound=np.zeros_like(LG1.real)
    for p,z in terms.items():bound=UP(bound+UP(cabs(z)*power(np.asarray([t1]),rational(p))[1][0]))
    return bound

def certify(path,alpha,U,split,block):
    field_hash=hashlib.sha256(path.read_bytes()).hexdigest()
    source_hash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    saved=np.load(path);t=saved['t'];all_u=saved['u'];take=(all_u>64)&(all_u<=U)
    u=all_u[take];A1=saved['A1'][take];A2=saved['A2'][take];LG=saved['LG'][:,take]
    assert t[0]==0. and t[-1]==.5 and np.all(np.diff(t)>0)
    assert np.all(LG[0]==0) and np.array_equal(all_u,np.arange(len(all_u))/8)
    assert all(np.all(np.isfinite(v)) for v in [t,all_u,A1,A2,LG])
    meta=json.loads(path.with_suffix('.json').read_text(encoding='utf-8'));beta=F(meta['beta_exact_decimal'])
    assert alpha==beta,'First version is a point certificate only.'
    assert np.finfo(float).nmant==52 and np.finfo(float).iexp==11
    nu,c,d,B=startup_coefficients(alpha,beta,u,A1,A2)
    Rpoly=residual_polynomial(B,A1,A2,nu,d,alpha,beta)
    combined_source=C.source_intervals(sys.modules[__name__],t,LG,A1,A2,beta)
    maximum=first_cell(t[1],LG[1],B,A1,A2,nu,c,d,alpha,beta)
    first=maximum.copy();peak=np.zeros_like(u);started=0
    first_HL=cscale(cp(LG[1]),div(1,mul(t[1],gamma(2+alpha))))
    first_re_bracket=B[0][0][1].copy()
    for p,z in [(beta,B[1]),(2*beta,B[2]),(F(1),first_HL)]:
        first_re_bracket=UP(first_re_bracket+UP(np.maximum(z[0][1],0.)*power(np.asarray([t[1]]),rational(p))[1][0]))
    max_Re_Hbox=np.full_like(u,-np.inf)
    # Subdivision endpoints are saved dyadics; subintervals form an exact cover.
    aa=[];bb=[];cell=[]
    for j in range(1,len(t)-1):
        edges=np.linspace(t[j],t[j+1],split+1);edges[0]=t[j];edges[-1]=t[j+1]
        aa.extend(edges[:-1]);bb.extend(edges[1:]);cell.extend([j]*split)
    aa=np.array(aa);bb=np.array(bb);cell=np.array(cell)
    preflight_cells=getattr(sys.modules[__name__],'OMISSION_PREFLIGHT_CELLS',None)
    if preflight_cells is not None:aa=aa[:preflight_cells];bb=bb[:preflight_cells];cell=cell[:preflight_cells]
    retained=np.empty((len(aa)+1,len(u)),dtype=np.float64);retained[0]=first
    for start in range(0,len(aa),block):
        a=aa[start:start+block];b=bb[start:start+block];j=cell[start:start+block]
        m=(a+b)/2;radius=UP(np.maximum(abs(m-a),abs(b-m)))
        J=linear_integral(m,t,LG,alpha);HM=H0(m,B,alpha,beta);HH=cadd(HM,J)
        # Exact affine remainder at the point, with outward dyadic ratio.
        ratio=div(sub(m,t[j]),sub(t[j+1],t[j]))
        L=cadd(cp(LG[j]),cscale(cp(LG[j+1]-LG[j]),(ratio[0][:,None],ratio[1][:,None])))
        # Account for the rounded coefficient subtraction above.
        L=(add(pair(LG[j].real),mul(sub(LG[j+1].real,LG[j].real),(ratio[0][:,None],ratio[1][:,None]))),
           add(pair(LG[j].imag),mul(sub(LG[j+1].imag,LG[j].imag),(ratio[0][:,None],ratio[1][:,None]))))
        # r=P_r+L-nu*(d+H0)*J-nu*J^2/2, with startup cancellation retained.
        rm=csub(cadd(polynomial(m,Rpoly),L),cscale(cadd(cmul(cadd(d,HM),J),cscale(cmul(J,J),rational(F(1,2)))),nu))
        point=cabs(rm)
        JP,Wprime=derivative_interval(a,b,t,LG,alpha)
        # Startup derivative enclosures use t in the full closed interval.
        HP=(pair(np.zeros_like(point)),pair(np.zeros_like(point)))
        GP=(div(sub(LG[j+1].real,LG[j].real),sub(t[j+1],t[j])[:,None] if False else (sub(t[j+1],t[j])[0][:,None],sub(t[j+1],t[j])[1][:,None])),
            div(sub(LG[j+1].imag,LG[j].imag),(sub(t[j+1],t[j])[0][:,None],sub(t[j+1],t[j])[1][:,None])))
        for k,z in enumerate(B):
            p=alpha+k*beta;pw=mul(power((a,b),rational(p-1)),rational(p))
            HP=cadd(HP,cscale(z,(pw[0][:,None],pw[1][:,None])))
        HP=cadd(HP,JP)
        LP=GP
        # Hhat throughout the subinterval is enclosed by the mean value theorem.
        span=(neg(mul((radius[:,None],radius[:,None]),maximum_abs(HP[0])))[0],mul((radius[:,None],radius[:,None]),maximum_abs(HP[0]))[1])
        spani=(neg(mul((radius[:,None],radius[:,None]),maximum_abs(HP[1])))[0],mul((radius[:,None],radius[:,None]),maximum_abs(HP[1]))[1])
        Hbox=(add(HH[0],span),add(HH[1],spani))
        # Preserve the same polynomial cancellation in r'.
        H0box=H0((a,b)[0],B,alpha,beta) if False else None
        H0prime=(pair(np.zeros_like(point)),pair(np.zeros_like(point)))
        H0whole=(pair(np.zeros_like(point)),pair(np.zeros_like(point)))
        for k,z in enumerate(B):
            p=alpha+k*beta;pw=power((a,b),rational(p));pd=mul(power((a,b),rational(p-1)),rational(p))
            H0whole=cadd(H0whole,cscale(z,(pw[0][:,None],pw[1][:,None])))
            H0prime=cadd(H0prime,cscale(z,(pd[0][:,None],pd[1][:,None])))
        Jbox=(add(J[0],(-UP(radius[:,None]*maximum_abs(JP[0])),UP(radius[:,None]*maximum_abs(JP[0])))),
              add(J[1],(-UP(radius[:,None]*maximum_abs(JP[1])),UP(radius[:,None]*maximum_abs(JP[1])))))
        RP=csub(cadd(polynomial((a,b),Rpoly,True),LP),cscale(cadd(cmul(cadd(d,cadd(H0whole,Jbox)),JP),cmul(H0prime,Jbox)),nu))
        # The unexpanded formula is better after the startup phase.  Both are
        # strict enclosures of the same derivative; taking the smaller scalar
        # modulus upper bound is therefore legitimate, not a heuristic switch.
        GPfull=LP
        for p,z in [(beta,cp(A1)),(2*beta,cp(A2))]:
            pw=mul(power((a,b),rational(p-1)),rational(p))
            GPfull=cadd(GPfull,cscale(z,(pw[0][:,None],pw[1][:,None])))
        RPdirect=csub(GPfull,cscale(cmul(cadd(d,Hbox),HP),nu))
        HPcombined=C.enclosure(sys.modules[__name__],a,b,t,LG,A1,A2,nu,c,alpha,beta,combined_source,Wprime)
        span_re=UP(radius[:,None]*maximum_abs(HPcombined[0]));span_im=UP(radius[:,None]*maximum_abs(HPcombined[1]))
        Hboxcombined=(add(HH[0],(-span_re,span_re)),add(HH[1],(-span_im,span_im)))
        RPcombined=csub(GPfull,cscale(cmul(cadd(d,Hboxcombined),HPcombined),nu))
        derivative_bound=np.minimum(np.minimum(cabs(RP),cabs(RPdirect)),cabs(RPcombined))
        # Each Hbox is a valid enclosure. Intersect real upper bounds only.
        real_upper=np.minimum(Hbox[0][1],Hboxcombined[0][1])
        max_Re_Hbox=np.maximum(max_Re_Hbox,np.max(real_upper,axis=0))
        bound=UP(point+UP(radius[:,None]*derivative_bound))
        retained[start+1:start+1+len(a)]=bound
        local=np.max(bound,axis=0);changed=local>maximum
        maximum[changed]=local[changed];peak[changed]=m[np.argmax(bound,axis=0)][changed]
        if start%(block*16)==0:print('certified intervals',start+len(a),'of',len(aa),'seconds',round(0-started,1),flush=True)
    time_path=Path(__file__).with_name('omission-time-'+('preflight' if preflight_cells is not None else 'high')+'.npz')
    np.savez_compressed(time_path,a=np.r_[0.,aa],b=np.r_[t[1],bb],u=u,residual_physical_upper=retained)
    assert hashlib.sha256(path.read_bytes()).hexdigest()==field_hash
    assert hashlib.sha256(Path(__file__).read_bytes()).hexdigest()==source_hash
    assert hashlib.sha256((BASE/'combined-field-derivative.py').read_bytes()).hexdigest()==COMBINED_SOURCE_HASH
    return {'status':'OUTWARD_BINARY64_INTERVAL_POINT_RESIDUAL_CERTIFICATE',
      'time_envelope_file':time_path.name,'time_envelope_sha256':hashlib.sha256(time_path.read_bytes()).hexdigest(),
      'alpha_exact':str(alpha),'beta_exact':str(beta),'T_exact':'1/2','frequency_scope':'fixed dyadic nodes only',
      'u':u.tolist(),'nu_exact':'2897/10000','field_file':path.name,'field_sha256':field_hash,
      'split':split,'certified_closed_subintervals':len(aa)+1,'first_cell_method':'finite generalized-power residual expansion',
      'residual_definition':'physical Gbar-nu*F(Hhat), Hhat=I^alpha Gbar',
      'delta_physical_upper_exact_dyadics':[str(F.from_float(float(v))) for v in maximum],
      'delta_F_upper_convenience':(maximum/(2897/10000)).tolist(),
      'first_cell_physical_upper_exact_dyadics':[str(F.from_float(float(v))) for v in first],
      'largest_bound_time':peak.tolist(),
      'source_sha256':source_hash,'polynomial_startup_cancellation':True,
      'combined_derivative_source_sha256':COMBINED_SOURCE_HASH,
      'first_cell_Re_H_div_talpha_upper_exact_dyadics':[str(F.from_float(float(v))) for v in first_re_bracket],
      'later_cells_Re_H_upper_exact_dyadics':[str(F.from_float(float(v))) for v in max_Re_Hbox],
      'approx_left_halfplane_certified':bool(np.all(first_re_bracket<=0)&np.all(max_Re_Hbox<=0))}

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    p=argparse.ArgumentParser();p.add_argument('--field',default='fixed-field-betap52.npz')
    p.add_argument('--alpha',default='.52');p.add_argument('--U',type=float,default=20)
    p.add_argument('--split',type=int,default=4);p.add_argument('--block',type=int,default=32)
    p.add_argument('--output',default='field-residual-certificate.json');a=p.parse_args()
    out=certify(BASE/a.field,F(a.alpha),a.U,a.split,a.block)
    (BASE/a.output).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    for v in [0,1,3,5,10,20]:
        if v in out['u']:j=out['u'].index(v);print('u',v,'deltaF upper',out['delta_F_upper_convenience'][j],flush=True)

if __name__=='__main__':main()
