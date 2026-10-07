"""Standalone Cramer-matrix sign replay and complete continuous splice check."""
from fractions import Fraction as F
from pathlib import Path
import argparse, gzip, hashlib, importlib.util, json, math
import dyadic as base
HERE=Path(__file__).resolve().parent
I,C,S=base.I,base.C,base.S
_gamma={};_alpha={}

def load(name):return json.loads(gzip.decompress((HERE/name).read_bytes()))
def sha(name):return hashlib.sha256((HERE/name).read_bytes()).hexdigest()
def gamma(q):
    if q not in _gamma:_gamma[q]=base.gamma_positive(q)
    return _gamma[q]
def trig(x,cosine=False):
    total=I(0);term=I(1) if cosine else x;xs=x.square()
    for k in range(32):
        total+=(-1)**k*term
        n=2*k+(0 if cosine else 1)
        term=term*xs/((n+1)*(n+2))
    degree=64 if cosine else 65
    tail=I(0,x.hi,True)**degree/math.factorial(degree)
    return total+I(-tail.hi,tail.hi,True)
def scalars(al,ar):
    key=al,ar
    if key not in _alpha:
        def point(a):
            g1,g2,g3=gamma(1+a),gamma(1+2*a),gamma(1+3*a)
            x=base.PI*a
            return trig(x)/x,-trig(x,True),g2/g1.square(),g2*g1/g3
        pl,vl,ml,zl=point(al);pr,vr,mr,zr=point(ar)
        _alpha[key]=I(pr.lo,pl.hi,True),I(vl.lo,vr.hi,True),I(ml.lo,mr.hi,True),I(zr.lo,zl.hi,True)
    return _alpha[key]
def det(matrix):
    a,b,c=matrix[0];d,e,f=matrix[1];g,h,i=matrix[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
def cramer_signs(row,rl,rr):
    al,ar=map(F,row['alpha']);el,er=map(F,row['eta'])
    p,v,m,zeta=scalars(al,ar)
    eta=I(I(el).lo,I(er).hi,True);rho=I(I(rl).lo,I(rr).hi,True)
    h=(eta.square()+(1-eta).square()/4).sqrt()
    sb=C((-rho/2)*(1-eta)/h,(-rho)*eta/h)
    a=C(1-rho.square()+2*sb.re.square(),2*sb.re*sb.im).sqrt_positive_real()
    r=1/(a+sb);b1=C(F(-1,2));b2=sb/(2*m)
    b3=C(zeta)*(C(F(1,8))-sb*sb/(2*m))
    g0=-r;g1=C(p)*r/a
    g2=C(m*p*v)*r/(a*a)+C(p.square())*r*r/(2*a**3)
    matrix=[[g0,g1,g2],[b1,-g0,-g1],[b2,b1,-g0]]
    rhs=[b1,-b2,-b3];delta=det(matrix);numerators=[]
    for column in range(3):
        replaced=[r[:] for r in matrix]
        for k in range(3):replaced[k][column]=rhs[k]
        numerators.append(det(replaced))
    bb=[(fj*delta.conj()).re for fj in numerators]
    q=[delta]+numerators
    pp=[C(0),b1*delta,b2*delta+b1*numerators[0],g0*numerators[2]]
    coeff=[I(0) for _ in range(7)]
    for j in range(1,4):
        for k in range(4):coeff[j+k]+=(pp[j]*q[k].conj()).re
    return [F(z.lo,S) for z in bb],[F(-z.hi,S) for z in coeff[1:]]

def keys(row):return (*map(F,row['alpha']),*map(F,row['eta']))
def partition(root,leaf_keys,limit):
    remaining=set(leaf_keys);assert len(remaining)==len(leaf_keys)
    count=0
    def walk(al,ar,el,er,depth):
        nonlocal count
        count+=1;k=al,ar,el,er
        if k in remaining:remaining.remove(k);return
        assert depth<limit
        if (ar-al)/F(2,25)>=er-el:
            mid=(al+ar)/2
            walk(al,mid,el,er,depth+1);walk(mid,ar,el,er,depth+1)
        else:
            mid=(el+er)/2
            walk(al,ar,el,mid,depth+1);walk(al,ar,mid,er,depth+1)
    walk(*root,0);assert not remaining
    return count

def run(sample=None):
    direct=load('rho-direct.json.gz');prior=load('rho-cover.json.gz')
    legacy=load('legacy-compact-cover.json.gz')
    assert direct['status']=='PASS_CONTINUOUS_RHO_DIRECT_SUPPLEMENT'
    assert direct['prior_attempt_sha256']==sha('rho-cover.json.gz')
    assert direct['protocol_sha256']==sha('rho-direct-protocol.json')
    rl,rr=map(F,direct['parameters']['rho'])
    assert (rl,rr)==(F(-744501,1000000),F(-744499,1000000))
    # The independent fallback reader covers all upstream signs and derivative constants.
    spec=importlib.util.spec_from_file_location('independent_persistence',HERE/'rho-check.py')
    reader=importlib.util.module_from_spec(spec);spec.loader.exec_module(reader)
    persistence=reader.run()
    assert persistence['status']=='PASS_INDEPENDENT_EXACT_CONTINUOUS_RHO_PERSISTENCE'
    lb,ld=reader.derivative_bounds()
    accepted_by_old={};unresolved_by_old={}
    retained_ids=set()
    for row in prior['retained']:
        j=row['upstream_leaf'];assert j not in retained_ids;retained_ids.add(j)
        old=legacy['cover'][j]
        assert list(map(F,row['B_extended_lower']))==[F(q)-(rr-rl)/2*l for q,l in zip(old['B_lower'],lb)]
        assert list(map(F,row['negative_D_extended_lower']))==[F(q)-(rr-rl)/2*l for q,l in zip(old['negative_D_lower'],ld)]
        assert min(map(F,row['B_extended_lower']+row['negative_D_extended_lower']))>0
    for row in prior['refined']:
        assert min(map(F,row['B_extended_lower']+row['negative_D_extended_lower']))>0
        assert list(map(F,row['B_extended_lower']))==[F(q)-(rr-rl)/2*l for q,l in zip(row['B_lower'],lb)]
        assert list(map(F,row['negative_D_extended_lower']))==[F(q)-(rr-rl)/2*l for q,l in zip(row['negative_D_lower'],ld)]
        accepted_by_old.setdefault(row['upstream_leaf'],[]).append(keys(row))
    direct_by_unresolved={}
    for row in direct['accepted']:
        assert min(map(F,row['B_lower']+row['negative_D_lower']))>0
        direct_by_unresolved.setdefault(row['source_unresolved_leaf'],[]).append(keys(row))
    nodes=0
    for j,row in enumerate(prior['unresolved']):
        leaves=direct_by_unresolved.pop(j)
        nodes+=partition(keys(row),leaves,18)
        unresolved_by_old.setdefault(row['upstream_leaf'],[]).append(keys(row))
    assert not direct_by_unresolved
    for j,old in enumerate(legacy['cover']):
        if j in retained_ids:
            assert j not in accepted_by_old and j not in unresolved_by_old
        else:
            leaves=accepted_by_old.pop(j,[])+unresolved_by_old.pop(j,[])
            nodes+=partition(keys(old),leaves,18)
    assert not accepted_by_old and not unresolved_by_old
    assert F(prior['exact_accepted_area'])+F(direct['exact_accepted_area'])==F(2,25)
    assert direct['unresolved_leaf_count']==0 and F(direct['exact_unresolved_area'])==0
    rows=direct['accepted'] if sample is None else direct['accepted'][:sample]
    replay_b=[None]*3;replay_d=[None]*6
    for row in rows:
        b,d=cramer_signs(row,rl,rr)
        assert min(b+d)>0,(row['source_unresolved_leaf'],b,d)
        for minima,values in ((replay_b,b),(replay_d,d)):
            for k,value in enumerate(values):minima[k]=value if minima[k] is None else min(value,minima[k])
    return dict(status='PASS_INDEPENDENT_CONTINUOUS_RHO_DIRECT_SPLICE' if sample is None else 'PASS_SAMPLE_ONLY_NOT_COMPLETE',
                full_original_leaf_count=len(legacy['cover']),retained_perturbation_leaf_count=len(prior['retained'])+len(prior['refined']),
                direct_leaf_count=len(direct['accepted']),direct_cramer_replays=len(rows),
                exact_total_alpha_eta_area='2/25',rho=list(map(str,(rl,rr))),splice_tree_nodes=nodes,
                independent_cramer_B_uniform_lower=list(map(str,replay_b)),
                independent_cramer_negative_D_uniform_lower=list(map(str,replay_d)),
                shared_dependencies='Only the original dyadic primitives and upstream saved baseline signs are shared; the supplement signs are replayed through independently assembled Cramer matrices and polynomial convolution.',
                source_sha256=sha('rho-direct-check.py'),
                inputs_sha256={name:sha(name) for name in ['rho-direct.json.gz','rho-cover.json.gz','legacy-compact-cover.json.gz','rho-direct-protocol.json']})

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--sample',type=int);args=ap.parse_args()
    result=run(args.sample)
    target='rho-direct-independent.json' if args.sample is None else 'rho-direct-sample.json'
    (HERE/target).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('inputs_sha256','independent_cramer_B_uniform_lower','independent_cramer_negative_D_uniform_lower')}))
