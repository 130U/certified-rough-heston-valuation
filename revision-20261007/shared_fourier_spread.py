"""Same-center full-budget shared Fourier certificate from released real inputs.

Integer dyadic interval primitives are reused, while support aggregation is new.
It consumes saved node certificates, not fresh continuous residual generation.
"""
from __future__ import annotations
from fractions import Fraction as Q
from pathlib import Path
import argparse, hashlib, importlib.util, json, sys, time
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
from audit_paths import release_root
RELEASE=release_root(HERE)
FROZEN=RELEASE/'code'/'frozen'
SRC=RELEASE/'code'/'src'

def load(name): return json.loads((FROZEN/name).read_text(encoding='utf-8'))
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def qbounds(x): return list(map(Q,x))
def display(q): return format(float(q),'.15g')

def validate_cover(data):
    rows=data['node_error_cover'];h=Q(data['h']);cutoff=Q(data['grid_cutoff'])
    assert len(rows)==int(cutoff/h)+1,'missing finite frequency node'
    assert [Q(r['u']) for r in rows]==[i*h for i in range(len(rows))],'frequency order or coverage'
    assert all(Q(r['true_CF_minus_stored_CF_modulus_upper'])>=0 for r in rows),'negative disk radius'
    assert all(set(r['budgets']) >= {'grid','true_discrete_tail','all_finite_node_errors'} for r in data['rows']),'incomplete budget'
    for r in data['rows']:
        for k in ['grid','true_discrete_tail','all_finite_node_errors']:
            lo,hi=qbounds(r['budgets'][k]);assert 0<=lo<=hi,'invalid positive budget'
        lo,hi=qbounds(r['stored_field_price']);assert lo<=hi,'reversed reference interval'
        lo,hi=qbounds(r['true_normalized_price']);assert lo<=hi,'reversed true-price interval'

def main():
    started=time.perf_counter()
    spec=importlib.util.spec_from_file_location('component',SRC/'exponent-field-certificate.py')
    comp=importlib.util.module_from_spec(spec);spec.loader.exec_module(comp)
    mo=comp.mo;dy=mo.dy;I,C,S=mo.I,dy.C,mo.S
    pade=load('frozen-pade-numeric-output.json')
    manifest=load('../MANIFEST.json')
    entries={r['path']:r for r in manifest['artifacts']}
    names=['frozen-pade-numeric-output.json','direct-tail-certificate.json',
           'f8-price-point052-v3-u64.json','f8-price-point06-v3-u64.json','f8-price-betap9-u64-v3.json']
    for name in names:
        assert sha(FROZEN/name)==entries['code/frozen/'+name]['sha256'],'source byte identity'
    results=[]
    for name in names[-3:]:
        data=load(name);validate_cover(data)
        alpha=Q(data['alpha_lower']);assert alpha==Q(data['alpha_upper'])
        rows=[next(r for r in data['rows'] if r['K']==k) for k in ['4400','4500']]
        fast={r['row_id']:Q(r['normalized_call_exact_dyadic']) for c in pade['cover'] if Q(c['alpha'])==alpha for r in c['rows']}
        refs=[];arith=[];d=[];marginal_errors=[]
        for row in rows:
            rl,ru=qbounds(row['stored_field_price']);refs.append((rl+ru)/2);arith.append((ru-rl)/2)
            d.append(refs[-1]-fast[row['row_id']])
            tl,tu=qbounds(row['true_normalized_price']);marginal_errors.append((tl-fast[row['row_id']],tu-fast[row['row_id']]))
        signed_center=d[0]-d[1]
        remainder=sum((Q(r['budgets'][k][1]) for r in rows for k in ['grid','true_discrete_tail']),Q(0))+sum(arith,Q(0))
        phases=[mo.log_endpoint(Q(r['m'])) for r in rows]
        prefs=[I(Q(r['m'])).sqrt()/dy.PI for r in rows]
        joint=I(0);marginal=I(0);node_ledger=[]
        for j,node in enumerate(data['node_error_cover']):
            u=Q(node['u']);radius=Q(node['true_CF_minus_stored_CF_modulus_upper'])
            coeff=[]
            for pref,k in zip(prefs,phases):
                phase=-u*k;z=C(comp.trig(phase,True),comp.trig(phase))
                factor=-Q(data['h'])*pref*(2 if j==0 else 1/(u*u+Q(1,4)))
                coeff.append(z*C(factor))
            norm=(coeff[0]-coeff[1]).norm2().sqrt()
            term=norm*radius;joint+=term
            mterm=(coeff[0].norm2().sqrt()+coeff[1].norm2().sqrt())*radius;marginal+=mterm
            node_ledger.append({'u':str(u),'radius':str(radius),'combined_coefficient_modulus':norm.bounds(),
                                'joint_node_support':term.bounds(),'sum_marginal_node_support':mterm.bounds()})
        J=Q(joint.hi,S)+remainder
        B=Q(marginal.hi,S)+remainder
        best_signed=[marginal_errors[0][0]-marginal_errors[1][1],marginal_errors[0][1]-marginal_errors[1][0]]
        joint_interval=[signed_center-J,signed_center+J]
        assert joint_interval[0]>=best_signed[0] and joint_interval[1]<=best_signed[1],'joint does not nest in best signed marginal intervals'
        assert J<B,'no strict support improvement'
        mj=max(abs(v) for v in best_signed);jj=max(abs(v) for v in joint_interval)
        scale=Q(211093,50) # frozen normalization: discounted forward DF=4221.86
        record={'alpha':str(alpha),'source':name,'strikes':['4400','4500'],'weights':['1','-1'],
                'shared_finite_nodes':len(node_ledger),'reference_centers_exact':list(map(str,refs)),
                'signed_reference_minus_fast_center':str(signed_center),
                'reference_rounding_radius':str(sum(arith,Q(0))),
                'full_remainder_grid_true_tail_and_reference_rounding':str(remainder),
                'joint_node_support_interval':joint.bounds(),'marginal_node_support_interval':marginal.bounds(),
                'joint_full_radius_upper':str(J),'same_outer_set_marginal_full_radius_upper':str(B),
                'joint_signed_actual_fast_error_interval':list(map(str,joint_interval)),
                'best_signed_marginal_actual_fast_error_interval':list(map(str,best_signed)),
                'joint_actual_fast_absolute_error_upper':str(jj),'best_signed_marginal_absolute_error_upper':str(mj),
                'absolute_error_reduction_fraction':str(1-jj/mj),
                'display':{'signed_center':display(signed_center),'full_remainder':display(remainder),
                           'joint_radius':display(J),'marginal_radius':display(B),
                           'joint_signed_interval':list(map(display,joint_interval)),
                           'best_signed_marginal_interval':list(map(display,best_signed)),
                           'joint_actual_fast_absolute_error_upper':display(jj),
                           'best_signed_marginal_absolute_error_upper':display(mj),
                           'reduction_percent':display(100*(1-jj/mj)),
                           'joint_actual_fast_bound_index_points':display(jj*scale),
                           'best_signed_marginal_bound_index_points':display(mj*scale),
                           'joint_support_width_index_points':display(2*J*scale)},
                'node_ledger_file':'shared-fourier-nodes-alpha-'+str(alpha).replace('/','_')+'.json'}
        (HERE/record['node_ledger_file']).write_text(json.dumps(node_ledger,indent=2)+'\n',encoding='utf-8')
        results.append(record)
        print(json.dumps({'alpha':str(alpha),'display':record['display']},indent=2),flush=True)
    result={'status':'PASS_SAME_CENTER_FULL_BUDGET_SHARED_FOURIER_CERTIFICATE','arithmetic':'100-bit outward integer dyadic intervals; exact Fraction comparisons',
            'scope':'Frozen first-maturity rough Heston actual Padé output, same reference, all finite node errors, complete grid and true infinite-tail budgets. No new upstream residual generation.',
            'source_sha256':{name:sha(FROZEN/name) for name in names},
            'implementation_sha256':sha(Path(__file__)),
            'dependency_sha256':{name:sha(SRC/name) for name in ['exponent-field-certificate.py','exact-forward-moments.py','interval-pade-certificate.py']},
            'same_center':True,'omitted_finite_nodes_counted_once':True,'clipping':False,'results':results,
            'wall_seconds':time.perf_counter()-started}
    (HERE/'shared-fourier-spread.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    return result

if __name__=='__main__':main()
