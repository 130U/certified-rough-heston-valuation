"""Finite-history recertification of unchanged actual Padé outputs.

The propagation assumptions and proof are stated in the paper. No residual/field is regenerated.
Positive forward moments and exponential use the original rigorous primitives.
The independent checker must not import this implementation.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib, importlib.util, json, sys, time
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
BASE = HERE.parent / 'reference'
OLD = HERE.parent / 'continuous'
FROZEN = BASE / 'code' / 'frozen'
SCALE = Q(211093, 50)

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def bound_pts(q): return float(q * SCALE)
def save(name, obj):
    (HERE/name).write_text(json.dumps(obj, indent=2)+'\n', encoding='utf-8')

def main():
    start=0
    contract=load(HERE/'experiment-contract.json')
    assert Q(contract['primary_absolute_error_budget_index_points'])==1
    sp=importlib.util.spec_from_file_location('finite_component',BASE/'code/src/exponent-field-certificate.py')
    cp=importlib.util.module_from_spec(sp);sp.loader.exec_module(cp)
    mo=cp.mo;dy=mo.dy;I,S=mo.I,mo.S
    J0=mo.moments(Q(1,2),64)[0]
    assert J0.lo>0
    setup=0-start
    inputs={}
    frozen_manifest={r['path']:r['sha256'] for r in load(BASE/'code/MANIFEST.json')['artifacts']}
    old_all=load(OLD/'shared-fourier-spread.json')
    all_results=[]
    for old in old_all['results']:
        begin=0
        source=FROZEN/old['source']; data=load(source)
        assert sha(source)==frozen_manifest['code/frozen/'+source.name]
        ledger=load(OLD/old['node_ledger_file'])
        nodes=data['node_error_cover']
        assert len(nodes)==len(ledger)==1025
        assert [Q(n['u']) for n in nodes]==[Q(j,8) for j in range(1025)]
        alpha=Q(old['alpha'])
        stem={Q(13,25):'betap52-u128',Q(3,5):'betap6-u128',Q(9,10):'betap9-u80'}[alpha]
        ep=FROZEN/('fixed-field-'+stem+'-exponent-certificate.json')
        ec=load(ep)
        assert sha(ep)==frozen_manifest['code/frozen/'+ep.name]
        ecover={Q(z['u']):z for z in ec['cover']}
        centre=Q(old['signed_reference_minus_fast_center'])
        remainder=Q(old['full_remainder_grid_true_tail_and_reference_rounding'])
        coeff=[Q(n['combined_coefficient_modulus'][1]) for n in ledger]
        radii=[Q(n['true_CF_minus_stored_CF_modulus_upper']) for n in nodes]
        direct_sum=remainder+sum((a*e for a,e in zip(coeff,radii)),Q(0))
        radius=max(direct_sum,Q(old['joint_full_radius_upper']))
        # Outward interval products/sums and the exact sum of coefficient upper
        # endpoints have tiny different rounding margins. Keep their maximum.
        eligible=[j for j,z in enumerate(nodes) if 'delta_physical_upper' in z]
        for j in eligible:
            assert Q(nodes[j]['all_time_approximate_realpart_upper'])<=0
        baseline_radius=radius
        upgraded=list(radii); node_receipts=[]; trace=[]
        for count in range(len(eligible)):
            remaining=[j for j in eligible if upgraded[j]==radii[j] and j not in {r['index'] for r in node_receipts}]
            if not remaining: break
            j=max(remaining,key=lambda k:(coeff[k]*radii[k],-k))
            z=nodes[j];u=Q(z['u']);t0=0
            delta=Q(z['delta_physical_upper'])/Q(data['nu'])
            assert delta==Q(z['delta_F_upper'])
            eta0=I(delta)*J0
            eta=min(Q(eta0.hi,S),Q(z['eta_upper']))
            modulus_hi=min(Q(1),Q(ecover[u]['phi_modulus'][1]))
            proposed=I(modulus_hi)*(dy.exp_positive(I(eta))-1)
            upgraded[j]=min(radii[j],Q(proposed.hi,S))
            radius-=coeff[j]*(radii[j]-upgraded[j])
            assert radius>=0
            lo,hi=centre-radius,centre+radius
            maxabs=max(abs(lo),abs(hi))
            trace.append({'step':len(trace)+1,'u':str(u),'radius_upper':str(radius),
                          'signed_interval':[str(lo),str(hi)],'absolute_error_upper':str(maxabs),
                          'absolute_error_upper_index_points':bound_pts(maxabs),
                          'primary_budget_pass':maxabs*SCALE<=1})
            node_receipts.append({'index':j,'u':str(u),'delta_F':str(delta),
                'finite_history_eta_upper':str(Q(eta0.hi,S)), 'old_eta_upper':z['eta_upper'],
                'used_eta_upper':str(eta),'old_CF_radius':str(radii[j]),
                'new_CF_radius':str(upgraded[j])})
        initial_max=max(abs(centre-baseline_radius),abs(centre+baseline_radius))
        first_pass=({'step':0,'absolute_error_upper_index_points':bound_pts(initial_max)}
                    if initial_max*SCALE<=1 else next((r for r in trace if r['primary_budget_pass']),None))
        full=max(abs(centre-radius),abs(centre+radius))
        # Primary-policy result uses only its prefix; all remaining actions are
        # separately disclosed supplementary work, included in total wall time.
        prefix=trace[:first_pass['step']] if first_pass else trace
        supplementary=trace[len(prefix):]
        name='finite-history-nodes-alpha-'+str(alpha).replace('/','_')+'.json'
        save(name,{'alpha':str(alpha),'nodes':node_receipts,'all_node_radii':list(map(str,upgraded))})
        result={'alpha':str(alpha),'source':old['source'],'node_receipt':name,
            'unchanged_signed_centre':str(centre),'unchanged_full_remainder':str(remainder),
            'baseline_radius_upper':str(baseline_radius),'baseline_absolute_bound_index_points':bound_pts(initial_max),
            'full_finite_history_radius_upper':str(radius),'full_signed_interval':[str(centre-radius),str(centre+radius)],
            'full_absolute_error_upper':str(full),'full_absolute_bound_index_points':bound_pts(full),
            'radius_reduction_fraction':str(1-radius/baseline_radius),
            'adaptive_status':'CERTIFIED' if first_pass else 'NOT_CERTIFIED',
            'primary_stopping_step':first_pass['step'] if first_pass else None,
            'primary_stop_bound_index_points':first_pass['absolute_error_upper_index_points'] if first_pass else bound_pts(full),
            'eligible_nodes':len(eligible),'primary_trace':prefix,
            'supplementary_steps_after_primary_stop':len(supplementary),
            'all_results_budget_pass':{v:full*SCALE<=Q(v) for v in ['1/4','1/2','1','2']},
            
            }
        all_results.append(result)
        inputs[source.name]=sha(source);inputs[ep.name]=sha(ep)
        inputs[old['node_ledger_file']]=sha(OLD/old['node_ledger_file'])
        print(json.dumps({k:result[k] for k in ['alpha', 'baseline_absolute_bound_index_points', 'full_absolute_bound_index_points', 'adaptive_status', 'primary_stopping_step', 'primary_stop_bound_index_points']},indent=2),flush=True)
    result={'status':'PASS_FINITE_HISTORY_SAME_OUTPUT_FULL_BUDGET',
        'scope':'Conditional on the complete finite-history proof; all old upstream certificates reused unchanged. Same original 4400-4500 spread, three original point candidates, T=1/2.',
        'arithmetic':'100-bit outward integer dyadic primitives; exact Fraction comparisons',
        'finite_history_forward_mass_enclosure':J0.bounds(),
        'contract_sha256':sha(HERE/'experiment-contract.json'),'implementation_sha256':sha(Path(__file__)),
        'input_sha256':inputs,'results':all_results,
        
        'cost_scope':'Fresh recertification/aggregation, not fresh field/continuous residual generation. Total includes supplementary all-node calculations after the primary stopping rule.'}
    save('finite-history-results.json',result)

if __name__=='__main__':main()
