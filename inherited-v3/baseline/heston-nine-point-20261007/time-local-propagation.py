"""Time-local full-history propagation of an unchanged alpha=.52 field.

128 bins were fixed before reading the fresh residual cells. Every intersecting
closed cell is included. All weight arithmetic and final decisions are exact
or outward rational; NumPy only selects exact stored binary64 maxima.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib, importlib.util, json, sys, time
sys.dont_write_bytecode = True
HERE=Path(__file__).resolve().parent
BASE=HERE.parent/'english-heston-release'
FROZEN=BASE/'code/frozen'
OLD=HERE.parent/'bc-merged-20261007'
SCALE=Q(211093,50)

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def outward(q,digits=9):
    q=Q(q);scale=10**digits;n=-((-q.numerator*scale)//q.denominator)
    return str(n//scale)+'.'+str(n%scale).zfill(digits)
def save(name,obj):(HERE/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')

def main():
    import numpy as np
    started=0
    contract=load(HERE/'time-local-contract.json')
    assert contract['partition']['bins']==128 and contract['partition']['edge_formula']=='j/256 for j=0,...,128'
    spec=importlib.util.spec_from_file_location('time_checker',HERE/'check-time-envelope.py')
    ck=importlib.util.module_from_spec(spec);spec.loader.exec_module(ck)
    checked=ck.check();save('time-envelope-verification.json',checked)
    checking_seconds=0-started
    fresh=load(HERE/'fresh-all-node-time-residual.json');envelope=HERE/fresh['time_envelope_file']
    with np.load(envelope,allow_pickle=False) as archive:
        a,b,u,R=[archive[k] for k in ['a','b','u','residual_physical_upper']]
    assert len(u)==513
    grouping_start=0;edges=[Q(j,256) for j in range(129)]
    bins=np.empty((128,513),dtype=np.float64);coverage=np.zeros(len(a),dtype=bool);cell_counts=[]
    for j,(left,right) in enumerate(zip(edges,edges[1:])):
        mask=(a<=float(right)) & (b>=float(left))  # all endpoints and bin edges are exact dyadics
        assert np.any(mask),'empty bin'
        bins[j]=np.max(R[mask],axis=0);coverage |= mask;cell_counts.append(int(np.sum(mask)))
    assert np.all(coverage),'source cell discarded'
    grouping_seconds=0-grouping_start
    sp=importlib.util.spec_from_file_location('time_moments',BASE/'code/src/exact-forward-moments.py')
    mo=importlib.util.module_from_spec(sp);sp.loader.exec_module(mo)
    dy,I,S=mo.dy,mo.I,mo.S
    weight_start=0;vals=[mo.moments(Q(1,2)-t,64)[0] for t in edges]
    weights=[]
    for j in range(128):
        w=vals[j]-vals[j+1];assert w.hi>0
        weights.append([max(Q(0),Q(w.lo,S)),Q(w.hi,S)])
    J0=mo.moments(Q(1,2),64)[0]
    assert sum((w[0] for w in weights),Q(0))<=Q(J0.hi,S)
    assert sum((w[1] for w in weights),Q(0))>=Q(J0.lo,S)
    weight_seconds=0-weight_start
    manifest={r['path']:r['sha256'] for r in load(BASE/'code/MANIFEST.json')['artifacts']}
    names=['f8-price-point052-v3-u64.json','fixed-field-betap52-u128-exponent-certificate.json']
    for name in names:assert sha(FROZEN/name)==manifest['code/frozen/'+name]
    data=load(FROZEN/names[0]);ec=load(FROZEN/names[1]);ecover={Q(z['u']):z for z in ec['cover']}
    assert fresh['field_sha256']==ec['field_sha256']==data['source_sha256']['field']
    old=next(r for r in load(OLD/'shared-fourier-spread.json')['results'] if r['alpha']=='13/25')
    ledger=load(OLD/old['node_ledger_file']);nodes=data['node_error_cover']
    assert len(nodes)==len(ledger)==1025 and [Q(n['u']) for n in nodes]==[Q(j,8) for j in range(1025)]
    assert [Q(n['radius']) for n in ledger]==[Q(n['true_CF_minus_stored_CF_modulus_upper']) for n in nodes]
    global_result=next(r for r in load(HERE/'finite-history-results.json')['results'] if r['alpha']=='13/25')
    assert global_result['unchanged_signed_centre']==old['signed_reference_minus_fast_center']
    assert global_result['unchanged_full_remainder']==old['full_remainder_grid_true_tail_and_reference_rounding']
    global_receipt=load(HERE/global_result['node_receipt'])
    global_radii=list(map(Q,global_receipt['all_node_radii']))
    coeff=[Q(n['combined_coefficient_modulus'][1]) for n in ledger]
    old_radii=[Q(n['true_CF_minus_stored_CF_modulus_upper']) for n in nodes]
    global_rebuilt=list(old_radii)
    upgraded=list(old_radii);node_receipts=[];nu=Q(data['nu'])
    propagation_start=0
    for n in range(513):
        node=nodes[n];assert Q(node['u'])==Q.from_float(float(u[n]))
        assert Q(node['all_time_approximate_realpart_upper'])<=0
        physical=Q(node['delta_physical_upper']);delta=physical/nu
        assert delta==Q(node['delta_F_upper'])
        rb=[Q.from_float(float(bins[j,n])) for j in range(128)]
        eta_time=sum((r*w[1] for r,w in zip(rb,weights)),Q(0))/nu
        eta_global=Q((I(delta)*J0).hi,S)
        eta=min(Q(node['eta_upper']),eta_global,eta_time)
        modulus=min(Q(1),Q(ecover[Q(n,8)]['phi_modulus'][1]))
        global_proposed=I(modulus)*(dy.exp_positive(I(min(Q(node['eta_upper']),eta_global)))-1)
        global_rebuilt[n]=min(old_radii[n],Q(global_proposed.hi,S))
        assert global_rebuilt[n]==global_radii[n],'global finite-history dependency differs from reconstruction'
        proposed=I(modulus)*(dy.exp_positive(I(eta))-1)
        upgraded[n]=min(old_radii[n],Q(proposed.hi,S),global_rebuilt[n])
        assert upgraded[n]<=global_radii[n]<=old_radii[n]
        node_receipts.append({'u':str(Q(n,8)),'physical_complete_residual_upper':str(physical),
            'time_bin_residual_upper_exact_dyadics':list(map(str,rb)),
            'time_local_eta_upper':str(eta_time),'global_finite_history_eta_upper':str(eta_global),
            'old_eta_upper':node['eta_upper'],'used_eta_upper':str(eta),
            'old_CF_radius':str(old_radii[n]),'global_finite_history_CF_radius':str(global_radii[n]),
            'time_local_CF_radius':str(upgraded[n])})
    propagation_seconds=0-propagation_start
    assert global_rebuilt==global_radii
    aggregate_start=0
    centre=Q(old['signed_reference_minus_fast_center']);remainder=Q(old['full_remainder_grid_true_tail_and_reference_rounding'])
    base_sum=remainder+sum((c*r for c,r in zip(coeff,old_radii)),Q(0))
    baseline=max(base_sum,Q(old['joint_full_radius_upper']));rounding_gap=baseline-base_sum
    radius=rounding_gap+remainder+sum((c*r for c,r in zip(coeff,upgraded)),Q(0))
    global_radius=rounding_gap+remainder+sum((c*r for c,r in zip(coeff,global_radii)),Q(0))
    assert global_radius==Q(global_result['full_finite_history_radius_upper'])
    assert radius<=global_radius<=baseline
    lo,hi=centre-radius,centre+radius;absolute=max(abs(lo),abs(hi))
    full_points=absolute*SCALE
    decisions={budget:{'pass':full_points<=Q(budget),'certified_margin_index_points':str(Q(budget)-full_points)}
               for budget in ['1','1/2','1/4']}
    aggregation_seconds=0-aggregate_start
    weights_receipt={'bins':128,'physical_time_edges':list(map(str,edges)),
        'curve_mass_enclosure':J0.bounds(),'bin_curve_mass_enclosures':[[str(x) for x in w] for w in weights],
        'intersecting_source_cell_counts':cell_counts,
        'source_cells':len(a),'all_source_cells_included':bool(np.all(coverage)),
        'closed_endpoint_intersections_included':True,'contract_sha256':sha(HERE/'time-local-contract.json')}
    save('time-local-weights.json',weights_receipt)
    save('time-local-node-ledger.json',{'nodes':node_receipts,'all_node_radii':list(map(str,upgraded))})
    result={'status':'PASS_TIME_LOCAL_SAME_OUTPUT_FULL_BUDGET',
        'alpha':'13/25','T':'1/2','strikes':['4400','4500'],'weights':['1','-1'],'finite_nodes':1025,
        'fresh_residual_nodes':513,'fresh_closed_time_cells':len(a),'fixed_time_bins':128,
        'same_fixed_reference_field':True,'same_actual_fast_output':True,'no_cell_history_reset':True,
        'unchanged_signed_centre':str(centre),'unchanged_full_remainder':str(remainder),
        'fixed_interval_rounding_gap':str(rounding_gap),'old_full_radius_upper':str(baseline),
        'global_finite_history_full_radius_upper':str(global_radius),'time_local_full_radius_upper':str(radius),
        'signed_actual_fast_error_interval':[str(lo),str(hi)],'absolute_error_upper':str(absolute),
        'absolute_error_upper_index_points_exact':str(full_points),
        'absolute_error_upper_index_points_display_outward':outward(full_points),
        'old_absolute_bound_index_points_display_outward':outward((abs(centre)+baseline)*SCALE),
        'global_finite_history_absolute_bound_index_points_display_outward':outward((abs(centre)+global_radius)*SCALE),
        'budget_checks':decisions,'strictly_smaller_than_global_bound':radius<global_radius,
        'scope':'128 preselected physical-time bins covering every fresh certified closed cell, only alpha=.52; no new approximation or residual reconstruction in this propagation step. All omitted finite nodes and complete old remainders retained.',
        'dependencies':{'contract':sha(HERE/'time-local-contract.json'),'time_envelope':sha(envelope),
            'fresh_residual_record':sha(HERE/'fresh-all-node-time-residual.json'),'envelope_checker':sha(HERE/'check-time-envelope.py'),
            'frozen_price':sha(FROZEN/names[0]),'frozen_exponents':sha(FROZEN/names[1]),
            'old_coefficient_ledger':sha(OLD/old['node_ledger_file']),
            'global_finite_history_result':sha(HERE/'finite-history-results.json'),
            'global_finite_history_node_receipt':sha(HERE/global_result['node_receipt']),
            'forward_moment_implementation':sha(BASE/'code/src/exact-forward-moments.py'),
            'implementation':sha(Path(__file__))},
        
        'cost_scope':'The fresh generator-reported timer starts after startup/setup and is a continuous-loop phase, not an end-to-end generation runtime. Current run reuses its saved complete envelopes and the old verified coefficient bank; full generation wall time requires the parent execution receipt.'}
    save('time-local-results.json',result)
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
