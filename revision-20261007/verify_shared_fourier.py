"""Check the shared spread with a second coefficient assembly.

The calculator multiplies complex phase boxes. This checker uses
|sqrt(m1)e^-iu log(m1)-sqrt(m2)e^-iu log(m2)|^2
=(sqrt(m1)-sqrt(m2))^2+4sqrt(m1m2)sin^2(u log(m1/m2)/2).
Elementary interval primitives remain shared, and that boundary is explicit.
"""
from fractions import Fraction as Q
from pathlib import Path
import copy,importlib.util,json,sys,time
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
from audit_paths import release_root
FROZEN=release_root(HERE)/'code'/'frozen'
SRC=FROZEN.parent/'src'
def price_semantics(result,data,pade):
    alpha=Q(result['alpha'])
    rows=[next(r for r in data['rows'] if r['K']==k) for k in ['4400','4500']]
    fast={r['row_id']:Q(r['normalized_call_exact_dyadic']) for c in pade['cover'] if Q(c['alpha'])==alpha for r in c['rows']}
    refs=[sum(map(Q,r['stored_field_price']))/2 for r in rows]
    arith=sum((Q(r['stored_field_price'][1])-Q(r['stored_field_price'][0]) for r in rows),Q(0))/2
    remainder=arith+sum((Q(r['budgets'][key][1]) for r in rows for key in ['grid','true_discrete_tail']),Q(0))
    center=(refs[0]-fast[rows[0]['row_id']])-(refs[1]-fast[rows[1]['row_id']])
    assert center==Q(result['signed_reference_minus_fast_center']),'signed reference-fast shift'
    assert remainder==Q(result['full_remainder_grid_true_tail_and_reference_rounding']),'full remainder including tail and arithmetic'
    J=Q(result['joint_full_radius_upper'])
    assert list(map(Q,result['joint_signed_actual_fast_error_interval']))==[center-J,center+J],'actual-output signed interval'
    assert Q(result['joint_actual_fast_absolute_error_upper'])==max(abs(center-J),abs(center+J)),'actual-output absolute upper bound'
    independent_marginal=[Q(rows[0]['true_normalized_price'][0])-fast[rows[0]['row_id']]-Q(rows[1]['true_normalized_price'][1])+fast[rows[1]['row_id']],
                          Q(rows[0]['true_normalized_price'][1])-fast[rows[0]['row_id']]-Q(rows[1]['true_normalized_price'][0])+fast[rows[1]['row_id']]]
    assert independent_marginal==list(map(Q,result['best_signed_marginal_actual_fast_error_interval'])),'best signed marginal source intervals'
    return rows,remainder
def main():
    started=time.perf_counter()
    sp=importlib.util.spec_from_file_location('independent_coeff',SRC/'exponent-field-certificate.py')
    comp=importlib.util.module_from_spec(sp);sp.loader.exec_module(comp);mo=comp.mo;I,S=mo.I,mo.S
    source=json.loads((HERE/'shared-fourier-spread.json').read_text());records=[]
    pade=json.loads((FROZEN/'frozen-pade-numeric-output.json').read_text());negative=[]
    for result in source['results']:
        data=json.loads((FROZEN/result['source']).read_text());rows,remainder=price_semantics(result,data,pade)
        roots=[I(Q(r['m'])).sqrt() for r in rows];logratio=mo.log_endpoint(Q(rows[0]['m'])/Q(rows[1]['m']))
        diff2=(roots[0]-roots[1]).square();prod=roots[0]*roots[1];total=I(0)
        for index,node in enumerate(data['node_error_cover']):
            u=Q(node['u']);epsilon=Q(node['true_CF_minus_stored_CF_modulus_upper'])
            stable=(diff2+4*prod*comp.trig(u*logratio/2).square()).sqrt()
            factor=Q(data['h'])*(2 if index==0 else 1/(u*u+Q(1,4)))/mo.dy.PI
            total+=factor*stable*epsilon
        certified_upper=Q(total.hi,S)+remainder;claimed=Q(result['joint_full_radius_upper'])
        assert certified_upper<=claimed,('independent coefficient upper exceeds claimed full radius',result['alpha'],str(certified_upper-claimed))
        records.append({'alpha':result['alpha'],'nodes':len(data['node_error_cover']),
                        'independent_node_support_interval':total.bounds(),
                        'independently_sufficient_full_radius_upper':str(certified_upper),
                        'reported_full_radius_upper':str(claimed),'reported_upper_independently_confirmed':True})
        changed=copy.deepcopy(result);changed['signed_reference_minus_fast_center']='0'
        rejected=False
        try:price_semantics(changed,data,pade)
        except AssertionError:rejected=True
        assert rejected;negative.append({'alpha':result['alpha'],'omitted_signed_reference_fast_shift_rejected':True})
    decisions=json.loads((HERE/'spread-decisions.json').read_text())
    scale=Q(decisions['DF'])
    for row in decisions['results']:
        bounds={k:Q(v) for k,v in row['error_bounds_normalized_exact'].items()}
        for decision in row['decisions']:
            budget=Q(decision['budget_index_points'])
            assert all(decision['results'][key]==('CERTIFIED_AT_BUDGET' if value*scale<=budget else 'NOT_CERTIFIED_AT_BUDGET') for key,value in bounds.items()),'incorrect budget decision'
    output={'status':'PASS_SECOND_COEFFICIENT_ASSEMBLY_SHARED_FOURIER_VERIFICATION','records':records,'signed_shift_negative_controls':negative,
            'signed_price_transformation_remainder_and_budget_decisions_exactly_checked':True,
            'wall_seconds':time.perf_counter()-started,
            'scope':'New stable real trigonometric coefficient identity; no import of the shared-Fourier calculator. Upstream saved radii and elementary scalar enclosure library are reused.'}
    (HERE/'shared-fourier-independent-verification.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(output,indent=2))
if __name__=='__main__':main()
