"""Continuous-alpha/all-frequency exact dyadic interval sign certificate.

Reuses the frozen 100-bit standard-library interval arithmetic without editing
it.  Every sign decision uses integer endpoints; clocks are progress only.
"""
from pathlib import Path
from fractions import Fraction as F
import importlib.util, hashlib, json, time, math, argparse

HERE=Path(__file__).parent
LIB=HERE/'interval-pade-certificate.py'
spec=importlib.util.spec_from_file_location('pade_interval_base',LIB)
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
I,C,S=base.I,base.C,base.S
RHO=F(-1489,2000)
_gamma_cache={}
_alpha_cache={}

def box(l,r):return I(I(l).lo,I(r).hi,True)
def gamma_point(q):
    q=F(q)
    if q not in _gamma_cache:_gamma_cache[q]=base.gamma_positive(q)
    return _gamma_cache[q]

def gamma_inc(l,r):
    # All arguments >= 1.52. Gamma is increasing for x>=3/2:
    # psi'(x)>0, psi(3/2)=2-gamma-2log2>2-.58-1.4>0.
    assert l>=F(3,2)
    return I(gamma_point(l).lo,gamma_point(r).hi,True)

def trig(x,cosine=False):
    # Taylor/Lagrange remainder: derivative modulus <= 1, all real arguments.
    total=I(0);x2=x.square()
    term=I(1) if cosine else x
    for k in range(32):
        total+=((-1)**k)*term
        n=2*k+(0 if cosine else 1)
        term=term*x2/((n+1)*(n+2))
    degree=64 if cosine else 65
    m=I(0,x.hi,True)
    tail=m**degree/math.factorial(degree)
    return total+I(-tail.hi,tail.hi,True)

def alpha_constants(l,r):
    key=(l,r)
    if key in _alpha_cache:return _alpha_cache[key]
    # Monotone scalar ratios retain Gamma dependence exactly at endpoints:
    # p decreases, v increases; d(log m)/da=2(psi(1+2a)-psi(1+a))>0;
    # d(log zeta)/da=2psi(1+2a)+psi(1+a)-3psi(1+3a)<0.
    # Thus no broad interval evaluation of oscillating Taylor terms or of
    # independently boxed Gamma factors enters the continuous-alpha cover.
    def endpoint(a):
        g1=gamma_point(1+a);g2=gamma_point(1+2*a);g3=gamma_point(1+3*a)
        angle=base.PI*a
        return (trig(angle)/angle,-trig(angle,True),g2/g1.square(),g2*g1/g3)
    pl,vl,ml,zl=endpoint(l);pr,vr,mr,zr=endpoint(r)
    p=I(pr.lo,pl.hi,True);v=I(vl.lo,vr.hi,True)
    m=I(ml.lo,mr.hi,True);zeta=I(zr.lo,zl.hi,True)
    out=(p,v,m,zeta)
    _alpha_cache[key]=out
    return out

def raw_values(al,ar,el,er):
    p,v,m,zeta=alpha_constants(al,ar)
    eta=box(el,er)
    h=(eta.square()+(1-eta).square()/4).sqrt()
    sigma=-RHO/2
    Sb=C(sigma*(1-eta)/h,2*sigma*eta/h)
    # |Sb|^2=rho^2 exactly; preserve positive discriminant real part.
    A=C(1-RHO*RHO+2*Sb.re.square(),2*Sb.re*Sb.im).sqrt_positive_real()
    R=1/(A+Sb)
    b=F(1,2)
    db=Sb/(2*m)
    cb=C(zeta)*(C(F(1,8))-Sb*Sb/(2*m))
    V=C(p)*R/A
    W=C(m*p*v)*R/(A*A)+C(p.square())*R*R/(2*A**3)
    Delta=b*b*W+2*b*R*V-db*R*W-db*V*V-R**3
    F1=b*b*V+b*db*W-b*R*R+db*R*V+cb*R*W+cb*V*V
    F2=-b*b*R+b*db*V+b*cb*W+db*db*W+db*R*R+cb*R*V
    F3=-b**3+2*b*db*R-b*cb*V-db*db*V+cb*R*R
    Fs=[F1,F2,F3]
    B=[(fj*Delta.conj()).re for fj in Fs]
    pp=db*Delta-b*F1
    D=[-b*Delta.norm2(),db.re*Delta.norm2()-2*b*B[0],
       (-R*F3*Delta.conj()+pp*F1.conj()-b*Delta*F2.conj()).re,
       (-R*F3*F1.conj()+pp*F2.conj()-b*Delta*F3.conj()).re,
       (-R*F3*F2.conj()+pp*F3.conj()).re,-R.re*F3.norm2()]
    return B,D,Delta,R

def check(al,ar,el,er):
    B,D,Delta,R=raw_values(al,ar,el,er)
    if any(z.lo<=0 for z in B):return None,'raw cone B'
    if any(z.hi>=0 for z in D):return None,'raw halfplane D'
    return dict(alpha=[str(al),str(ar)],eta=[str(el),str(er)],
         B_lower=[str(F(z.lo,S)) for z in B],negative_D_lower=[str(F(-z.hi,S)) for z in D],
         delta_norm2_lower=str(F(Delta.norm2().lo,S)),R_real_lower=str(F(R.re.lo,S))),None

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--max-depth',type=int,default=28)
    parser.add_argument('--max-cells',type=int,default=200000)
    parser.add_argument('--alpha-top',type=F,default=F(9,10))
    args=parser.parse_args();start=time.monotonic()
    bands=[(F(13,25),F(3,5)),(F(3,5),F(3,4)),(F(3,4),args.alpha_top)]
    bands=[(l,min(r,args.alpha_top)) for l,r in bands if l<args.alpha_top]
    todo=[(l,r,F(0),F(1),0,0) for l,r in reversed(bands)]
    accepted=[];unresolved=[];failures={};count=0
    while todo:
        al,ar,el,er,ad,ed=todo.pop();count+=1
        try:result,why=check(al,ar,el,er)
        except (AssertionError,ZeroDivisionError):result,why=None,'intermediate enclosure'
        if result is not None:accepted.append(result)
        elif ad+ed>=args.max_depth or count>=args.max_cells:
            unresolved.append(dict(alpha=[str(al),str(ar)],eta=[str(el),str(er)],reason=why,depth=ad+ed))
            if count>=args.max_cells:
                unresolved.extend(dict(alpha=[str(t[0]),str(t[1])],eta=[str(t[2]),str(t[3])],reason='cell budget',depth=t[4]+t[5]) for t in todo)
                todo=[]
        else:
            failures[why]=failures.get(why,0)+1
            # Normalize alpha width by total range before choosing a dimension.
            if (ar-al)/(args.alpha_top-F(13,25)) >= er-el:
                mid=(al+ar)/2
                todo.extend([(mid,ar,el,er,ad+1,ed),(al,mid,el,er,ad+1,ed)])
            else:
                mid=(el+er)/2
                todo.extend([(al,ar,mid,er,ad,ed+1),(al,ar,el,mid,ad,ed+1)])
        if count%2000==0:
            print('checked',count,'accepted',len(accepted),'pending',len(todo),'unresolved',len(unresolved),'seconds',round(time.monotonic()-start,2),flush=True)
    # A rational area check and pairwise-disjoint dyadic split tree establish
    # exact cover; no floating-point mesh or endpoint limit is involved.
    area=sum((F(r['alpha'][1])-F(r['alpha'][0]))*(F(r['eta'][1])-F(r['eta'][0])) for r in accepted)
    unresolved_area=sum((F(r['alpha'][1])-F(r['alpha'][0]))*(F(r['eta'][1])-F(r['eta'][0])) for r in unresolved)
    assert area+unresolved_area==args.alpha_top-F(13,25)
    data=dict(status='EXACT_DYADIC_INTERVAL_FULL_COVER' if not unresolved else 'EXACT_PARTIAL_COVER_NOT_FULL_CERTIFICATE',bits=base.BITS,
        parameters=dict(alpha=['13/25',str(args.alpha_top)],rho=str(RHO),kappa='0',eta=['0','1'],frequency='all u>=0, with u=infinity limit included'),
        cells=len(accepted),checked=count,unresolved=len(unresolved),seconds=time.monotonic()-start,split_reasons=failures,
        exact_accepted_area=str(area),exact_unresolved_area=str(unresolved_area),
        library_sha256=hashlib.sha256(LIB.read_bytes()).hexdigest(),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        pi_enclosure=base.PI.bounds(),
        B_uniform_lower=[str(min(F(r['B_lower'][j]) for r in accepted)) for j in range(3)] if accepted else [],
        negative_D_uniform_lower=[str(min(F(r['negative_D_lower'][j]) for r in accepted)) for j in range(6)] if accepted else [],
        gamma_point_enclosures={str(k):v.bounds() for k,v in sorted(_gamma_cache.items())},
        cover=accepted,unresolved_cover=unresolved)
    out=HERE/'compact-halfplane-certificate.json'
    out.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(data['status'],len(accepted),'accepted',len(unresolved),'unresolved','seconds',round(time.monotonic()-start,2),flush=True)
    print('B lower',data['B_uniform_lower'],flush=True)
    print('negative D lower',data['negative_D_uniform_lower'],flush=True)

if __name__=='__main__':main()
