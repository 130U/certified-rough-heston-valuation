"""Independent exact cover and perturbation reader; no machine metadata."""
from fractions import Fraction as Q
from pathlib import Path
import argparse, gzip, hashlib, json

HERE=Path(__file__).resolve().parent
def load(name):
    p=HERE/name
    return json.loads(gzip.decompress(p.read_bytes())) if name.endswith('.gz') else json.loads(p.read_text(encoding='utf-8'))
def sha(name):return hashlib.sha256((HERE/name).read_bytes()).hexdigest()

# Norm majorants independently expressed as exact (value, derivative) pairs.
def add(*xs):return tuple(sum(x[j] for x in xs) for j in (0,1))
def mul(x,y):return x[0]*y[0],x[1]*y[0]+x[0]*y[1]
def scale(x,c):return x[0]*c,x[1]*c
def powr(x,n):
    return (x[0]**n,n*x[0]**(n-1)*x[1]) if n else (Q(1),Q(0))
def derivative_bounds():
    b=(Q(1,2),Q(0)); p=(Q(2,3),Q(0)); v=(Q(1,3),Q(0))
    m=(Q(3,2),Q(0)); zeta=(Q(2,3),Q(0))
    sb=(Q(3,4),Q(1)); ai=(Q(8,5),Q(384,125)); r=(Q(1),Q(11,5))
    db=scale(sb,Q(1,2)); cb=mul(zeta,add((Q(1,8),Q(0)),scale(powr(sb,2),Q(1,2))))
    vv=mul(p,mul(r,ai))
    ww=add(mul(mul(m,mul(p,v)),mul(r,powr(ai,2))),
           scale(mul(powr(p,2),mul(powr(r,2),powr(ai,3))),Q(1,2)))
    delta=add(mul(powr(b,2),ww),scale(mul(b,mul(r,vv)),2),
              mul(db,mul(r,ww)),mul(db,powr(vv,2)),powr(r,3))
    f1=add(mul(powr(b,2),vv),mul(b,mul(db,ww)),mul(b,powr(r,2)),
           mul(db,mul(r,vv)),mul(cb,mul(r,ww)),mul(cb,powr(vv,2)))
    f2=add(mul(powr(b,2),r),mul(b,mul(db,vv)),mul(b,mul(cb,ww)),
           mul(powr(db,2),ww),mul(db,powr(r,2)),mul(cb,mul(r,vv)))
    f3=add(powr(b,3),scale(mul(b,mul(db,r)),2),
           mul(b,mul(cb,vv)),mul(powr(db,2),vv),mul(cb,powr(r,2)))
    pp=add(mul(db,delta),mul(b,f1))
    bb=[mul(fj,delta) for fj in (f1,f2,f3)]
    dd=[mul(b,powr(delta,2)),
        add(mul(db,powr(delta,2)),scale(mul(b,bb[0]),2)),
        add(mul(r,mul(f3,delta)),mul(pp,f1),mul(b,mul(delta,f2))),
        add(mul(r,mul(f3,f1)),mul(pp,f2),mul(b,mul(delta,f3))),
        add(mul(r,mul(f3,f2)),mul(pp,f3)),mul(r,powr(f3,2))]
    return [q[1] for q in bb],[q[1] for q in dd]

def original_geometry(rows):
    leaves=set()
    bm=[None]*3; dm=[None]*6; area=Q(0)
    for row in rows:
        al,ar=map(Q,row['alpha']);el,er=map(Q,row['eta'])
        assert Q(13,25)<=al<ar<=Q(3,5) and 0<=el<er<=1
        key=(al,ar,el,er);assert key not in leaves;leaves.add(key)
        area+=(ar-al)*(er-el)
        for dst,values in ((bm,row['B_lower']),(dm,row['negative_D_lower'])):
            for j,s in enumerate(values):
                x=Q(s);assert x>0
                dst[j]=x if dst[j] is None else min(dst[j],x)
    nodes=0
    def walk(al,ar,el,er,depth=0):
        nonlocal nodes
        nodes+=1;key=(al,ar,el,er)
        if key in leaves:leaves.remove(key);return
        assert depth<28
        if (ar-al)/Q(19,50)>=er-el:
            mid=(al+ar)/2;walk(al,mid,el,er,depth+1);walk(mid,ar,el,er,depth+1)
        else:
            mid=(el+er)/2;walk(al,ar,el,mid,depth+1);walk(al,ar,mid,er,depth+1)
    walk(Q(13,25),Q(3,5),Q(0),Q(1))
    assert not leaves and area==Q(2,25) and nodes==2*len(rows)-1
    return bm,dm,nodes

def run():
    source=load('legacy-compact-cover.json.gz'); receipt=load('rho-fallback.json')
    assert sha('legacy-compact-cover.json.gz')==receipt['upstream_sha256']
    assert sha('rho-protocol.json')==receipt['protocol_sha256']
    assert sha('rho-cover.json.gz')==receipt['primary_attempt_sha256']
    bm,dm,nodes=original_geometry(source['cover'])
    assert bm==list(map(Q,source['B_uniform_lower']))
    assert dm==list(map(Q,source['negative_D_uniform_lower']))
    lb,ld=derivative_bounds()
    assert lb==list(map(Q,receipt['B_rho_lipschitz']))
    assert ld==list(map(Q,receipt['D_rho_lipschitz']))
    h=min([Q(1,1000000)]+[m/(2*l) for m,l in zip(bm+dm,lb+ld)])
    assert h>0 and Q(receipt['rho_half_width'])==h
    expectedb=[m-h*l for m,l in zip(bm,lb)]
    expectedd=[m-h*l for m,l in zip(dm,ld)]
    assert min(expectedb+expectedd)>0
    assert expectedb==list(map(Q,receipt['B_uniform_extended_lower']))
    assert expectedd==list(map(Q,receipt['negative_D_uniform_extended_lower']))
    assert list(map(Q,receipt['rho_interval']))==[Q(-1489,2000)-h,Q(-1489,2000)+h]
    assert Q(receipt['interval_width'])==2*h
    attempt=load('rho-cover.json.gz')
    assert attempt['status']=='UNRESOLVED_CONTINUOUS_RHO_EXTENSION'
    assert Q(attempt['exact_accepted_area'])+Q(attempt['exact_unresolved_area'])==Q(2,25)
    assert Q(attempt['exact_unresolved_area'])>0
    assert Q(receipt['primary_unresolved_area'])==Q(attempt['exact_unresolved_area'])
    assert attempt['refined_evaluations']==150001
    dh=Q(1); exponent=0
    while dh>h:dh/=2;exponent+=1
    assert exponent==receipt['readable_dyadic_exponent']==41
    assert dh==Q(receipt['readable_dyadic_half_width'])
    assert list(map(Q,receipt['readable_dyadic_interval']))==[Q(-1489,2000)-dh,Q(-1489,2000)+dh]
    # Actual corruptions exercise the mathematical checks, not only hashes.
    def scalar_receipt_check(candidate):
        assert candidate['kappa']=='0'
        assert Q(candidate['rho_half_width'])==h>0
        assert candidate['primary_attempt_status']==attempt['status']
    corruptions=[]
    for name,updates in [
        ('larger_half_width',dict(rho_half_width='1/1000000')),
        ('zero_width',dict(rho_half_width='0')),
        ('partial_primary_as_full_domain',dict(primary_attempt_status='PASS_CONTINUOUS_RHO_ALPHA_ALL_FREQUENCY')),
        ('wrong_damping_parameter',dict(kappa='1'))]:
        candidate=dict(receipt);candidate.update(updates)
        corruptions.append((name,lambda candidate=candidate:scalar_receipt_check(candidate)))
    corruptions.append(('missing_initial_low_frequency_boundary',lambda:original_geometry(source['cover'][1:])))
    negative={}
    for name,check in corruptions:
        try:check()
        except AssertionError:negative[name]='REJECTED'
        else:raise AssertionError('accepted negative control '+name)
    return dict(status='PASS_INDEPENDENT_EXACT_CONTINUOUS_RHO_PERSISTENCE',
                original_closed_leaf_count=len(source['cover']),partition_tree_nodes=nodes,
                exact_area='2/25',rho_half_width=str(h),rho_interval=receipt['rho_interval'],
                readable_dyadic_half_width=str(dh),readable_dyadic_exponent=exponent,
                independent_derivative_majorants=True,all_original_sign_records_checked=True,
                primary_unresolved_retained=True,negative_controls=negative,
                independence_limit='Checks every saved upstream sign and full continuous cover, and independently assembles all derivative majorants and perturbation bounds. Does not regenerate every original raw interval-polynomial evaluation.',
                input_sha256={name:sha(name) for name in ['legacy-compact-cover.json.gz','rho-fallback.json','rho-cover.json.gz','rho-protocol.json']},
                checker_sha256=sha('rho-check.py'))

if __name__=='__main__':
    result=run()
    (HERE/'rho-independent.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('input_sha256','negative_controls')}))
