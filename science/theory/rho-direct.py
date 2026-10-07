"""Direct three-dimensional interval supplement with frozen mathematical budget."""
from pathlib import Path
from fractions import Fraction as F
import gzip, hashlib, importlib.util, json
import dyadic as base

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('rho_prior',HERE/'rho-cover.py')
prior=importlib.util.module_from_spec(spec);spec.loader.exec_module(prior)
I,C,S=base.I,base.C,base.S

def raw_values(al,ar,el,er,rl,rr):
    p,v,m,zeta=prior.alpha_constants(al,ar)
    eta=I(I(el).lo,I(er).hi,True)
    rho=I(I(rl).lo,I(rr).hi,True)
    h=(eta.square()+(1-eta).square()/4).sqrt()
    sigma=-rho/2
    sb=C(sigma*(1-eta)/h,2*sigma*eta/h)
    a=C(1-rho.square()+2*sb.re.square(),2*sb.re*sb.im).sqrt_positive_real()
    r=1/(a+sb)
    b,db=F(1,2),sb/(2*m)
    cb=C(zeta)*(C(F(1,8))-sb*sb/(2*m))
    vv=C(p)*r/a
    ww=C(m*p*v)*r/(a*a)+C(p.square())*r*r/(2*a**3)
    delta=b*b*ww+2*b*r*vv-db*r*ww-db*vv*vv-r**3
    f1=b*b*vv+b*db*ww-b*r*r+db*r*vv+cb*r*ww+cb*vv*vv
    f2=-b*b*r+b*db*vv+b*cb*ww+db*db*ww+db*r*r+cb*r*vv
    f3=-b**3+2*b*db*r-b*cb*vv-db*db*vv+cb*r*r
    bb=[(fj*delta.conj()).re for fj in (f1,f2,f3)]
    pp=db*delta-b*f1
    dd=[-b*delta.norm2(),db.re*delta.norm2()-2*b*bb[0],
        (-r*f3*delta.conj()+pp*f1.conj()-b*delta*f2.conj()).re,
        (-r*f3*f1.conj()+pp*f2.conj()-b*delta*f3.conj()).re,
        (-r*f3*f2.conj()+pp*f3.conj()).re,-r.re*f3.norm2()]
    return bb,dd

def main():
    protocol=json.loads((HERE/'rho-direct-protocol.json').read_text(encoding='utf-8'))
    old=json.loads(gzip.decompress((HERE/'rho-cover.json.gz').read_bytes()))
    rl,rr=map(F,protocol['rho'])
    todo=[(*map(F,r['alpha']),*map(F,r['eta']),0,j)
          for j,r in enumerate(old['unresolved'])]
    accepted=[];unresolved=[];count=0
    while todo and count<protocol['maximum_direct_evaluations']:
        al,ar,el,er,depth,parent=todo.pop();count+=1
        try:
            bb,dd=raw_values(al,ar,el,er,rl,rr)
            good=all(q.lo>0 for q in bb) and all(q.hi<0 for q in dd)
        except (AssertionError,ZeroDivisionError):
            good=False
        if good:
            accepted.append(dict(alpha=list(map(str,(al,ar))),eta=list(map(str,(el,er))),
                                 source_unresolved_leaf=parent,
                                 B_lower=[str(F(q.lo,S)) for q in bb],
                                 negative_D_lower=[str(F(-q.hi,S)) for q in dd]))
        elif depth>=protocol['maximum_additional_depth']:
            unresolved.append(dict(alpha=list(map(str,(al,ar))),eta=list(map(str,(el,er))),
                                   source_unresolved_leaf=parent,additional_depth=depth))
        elif (ar-al)/F(2,25)>=er-el:
            mid=(al+ar)/2
            todo.extend([(al,mid,el,er,depth+1,parent),(mid,ar,el,er,depth+1,parent)])
        else:
            mid=(el+er)/2
            todo.extend([(al,ar,el,mid,depth+1,parent),(al,ar,mid,er,depth+1,parent)])
        if count%2000==0:
            print(json.dumps(dict(direct_evaluations=count,accepted=len(accepted),pending=len(todo),unresolved=len(unresolved))),flush=True)
    unresolved.extend(dict(alpha=list(map(str,(al,ar))),eta=list(map(str,(el,er))),
                           source_unresolved_leaf=parent,additional_depth=depth)
                      for al,ar,el,er,depth,parent in todo)
    area=lambda r:(F(r['alpha'][1])-F(r['alpha'][0]))*(F(r['eta'][1])-F(r['eta'][0]))
    accepted_area=sum(map(area,accepted));unresolved_area=sum(map(area,unresolved))
    assert accepted_area+unresolved_area==F(old['exact_unresolved_area'])
    result=dict(status='PASS_CONTINUOUS_RHO_DIRECT_SUPPLEMENT' if not unresolved else 'UNRESOLVED_DIRECT_SUPPLEMENT',
                parameters={k:protocol[k] for k in ('alpha','rho','kappa','eta')},
                design_class=protocol['design_class'],initial_unresolved_leaf_count=len(old['unresolved']),
                direct_evaluations=count,accepted_leaf_count=len(accepted),unresolved_leaf_count=len(unresolved),
                exact_accepted_area=str(accepted_area),exact_unresolved_area=str(unresolved_area),
                B_uniform_lower=[str(min(F(r['B_lower'][j]) for r in accepted)) for j in range(3)] if accepted else [],
                negative_D_uniform_lower=[str(min(F(r['negative_D_lower'][j]) for r in accepted)) for j in range(6)] if accepted else [],
                prior_attempt_sha256=hashlib.sha256((HERE/'rho-cover.json.gz').read_bytes()).hexdigest(),
                protocol_sha256=hashlib.sha256((HERE/'rho-direct-protocol.json').read_bytes()).hexdigest(),
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                accepted=accepted,unresolved=unresolved)
    (HERE/'rho-direct.json.gz').write_bytes(gzip.compress(json.dumps(result,separators=(',',':')).encode('utf-8'),compresslevel=9,mtime=0))
    print(json.dumps({k:v for k,v in result.items() if k not in ('accepted','unresolved')}),flush=True)
    if unresolved:raise SystemExit(1)

if __name__=='__main__':main()
