"""Full-budget same-FAST certificate with an expanded nonzero reference.

High-node disks move their centres: old true-minus-zero radii are translated
by |psi| before any minimum is taken. Interval primitives are explicitly shared.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib,importlib.util,json,sys,time
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;BASE=HERE.parent/'english-heston-release';FROZEN=BASE/'code/frozen'
OLD=HERE.parent/'bc-merged-20261007';NINE=HERE.parent/'heston-nine-point-20261007';SCALE=Q(211093,50)
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):(HERE/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def upward(q,digits=9):
    q=Q(q);s=10**digits;n=-((-q.numerator*s)//q.denominator)
    return str(n//s)+'.'+str(n%s).zfill(digits)
def main():
    import numpy as np
    begin=0;contract=load(HERE/'omission-contract.json')
    for name,digest in contract['source_sha256'].items():assert sha(FROZEN/name)==digest
    frozen_manifest={z['path']:z['sha256'] for z in load(BASE/'code/MANIFEST.json')['artifacts']}
    primitive_names=['exponent-field-certificate.py','exact-forward-moments.py','interval-pade-certificate.py']
    for name in primitive_names:assert sha(BASE/'code/src'/name)==frozen_manifest['code/src/'+name]
    p=BASE/'code/src/exponent-field-certificate.py';sp=importlib.util.spec_from_file_location('omission_component',p)
    cp=importlib.util.module_from_spec(sp);sp.loader.exec_module(cp);mo=cp.mo;dy=mo.dy;I,S,C=mo.I,mo.S,mo.dy.C
    def box(bounds):
        a,b=map(Q,bounds);assert a<=b
        return I(I(a).lo,I(b).hi,True)
    data=load(FROZEN/'f8-price-point052-v3-u64.json');ec=load(FROZEN/'fixed-field-betap52-u128-exponent-certificate.json')
    raw=load(HERE/'omission-residual-high.json');assert raw['approx_left_halfplane_certified']
    assert ec['source_sha256']==sha(p)
    assert raw['field_sha256']==ec['field_sha256']==data['source_sha256']['field']
    old=next(z for z in load(OLD/'shared-fourier-spread.json')['results'] if z['alpha']=='13/25')
    oldcoef=load(OLD/old['node_ledger_file']);low=load(NINE/'time-local-node-ledger.json');lowresult=load(NINE/'time-local-results.json')
    assert lowresult['unchanged_signed_centre']==old['signed_reference_minus_fast_center']
    assert lowresult['dependencies']['frozen_exponents']==sha(FROZEN/'fixed-field-betap52-u128-exponent-certificate.json')
    assert [Q(z['u']) for z in ec['cover']]==[Q(j,8) for j in range(1025)]
    assert [Q(z['u']) for z in data['node_error_cover']]==[Q(j,8) for j in range(1025)]
    rows=[next(z for z in data['rows'] if z['K']==k) for k in ['4400','4500']]
    fast={z['row_id']:Q(z['normalized_call_exact_dyadic']) for c in load(FROZEN/'frozen-pade-numeric-output.json')['cover'] if Q(c['alpha'])==Q(13,25) for z in c['rows']}
    reference_start=0;reference_rows=[];reference_coefficients=[[],[]]
    for rindex,row in enumerate(rows):
        phase0=mo.log_endpoint(Q(row['m']));pref=I(Q(row['m'])).sqrt()/dy.PI
        sums={512:I(0),1024:I(0)};integral=I(0)
        for j,z in enumerate(ec['cover']):
            u=Q(z['u']);phase=-u*phase0
            rotation=C(cp.trig(phase,True),cp.trig(phase))
            phi=C(box(z['phi_re']),box(z['phi_im']))
            integral+=(2*phi.re if j==0 else (rotation*phi).re/(u*u+Q(1,4)))
            coeff=rotation*C(-Q(data['h'])*pref*(2 if j==0 else 1/(u*u+Q(1,4))))
            reference_coefficients[rindex].append(coeff)
            if j in sums:sums[j]=1-Q(data['h'])*pref*integral
        assert sums[512].bounds()==row['stored_field_price'],'old reference assembly mismatch'
        interval=list(map(Q,sums[1024].bounds()));mid=sum(interval,Q(0))/2;rounding=(interval[1]-interval[0])/2
        reference_rows.append({'row_id':row['row_id'],'K':row['K'],'m':row['m'],'old_reference_interval':row['stored_field_price'],
            'new_reference_interval':list(map(str,interval)),'new_reference_midpoint':str(mid),'new_reference_rounding_radius':str(rounding),
            'unchanged_actual_fast':str(fast[row['row_id']]),'signed_new_reference_minus_fast':str(mid-fast[row['row_id']]),
            'unchanged_grid_strip_budget_upper':row['budgets']['grid'][1],
            'unchanged_true_infinite_tail_beyond128_upper':row['budgets']['true_discrete_tail'][1]})
    reference_seconds=0-reference_start
    centre=Q(reference_rows[0]['signed_new_reference_minus_fast'])-Q(reference_rows[1]['signed_new_reference_minus_fast'])
    remainder=sum((Q(r[k]) for r in reference_rows for k in ['new_reference_rounding_radius','unchanged_grid_strip_budget_upper','unchanged_true_infinite_tail_beyond128_upper']),Q(0))
    oldcentre=Q(old['signed_reference_minus_fast_center']);oldinterval=list(map(Q,lowresult['signed_actual_fast_error_interval']))
    oldfloor=abs(oldcentre)+Q(old['full_remainder_grid_true_tail_and_reference_rounding'])+sum((Q(oldcoef[j]['combined_coefficient_modulus'][1])*Q(data['node_error_cover'][j]['true_CF_minus_stored_CF_modulus_upper']) for j in range(513,1025)),Q(0))
    coeff=[];margcoeff=[]
    for j in range(1025):
        joint=(reference_coefficients[0][j]-reference_coefficients[1][j]).norm2().sqrt()
        assert joint.bounds()==oldcoef[j]['combined_coefficient_modulus']
        coeff.append(Q(joint.hi,S))
        margcoeff.append(Q((reference_coefficients[0][j].norm2().sqrt()+reference_coefficients[1][j].norm2().sqrt()).hi,S))
    with np.load(HERE/raw['time_envelope_file'],allow_pickle=False) as bank:
        a,b,u,R=[bank[k] for k in ['a','b','u','residual_physical_upper']]
    assert len(u)==512 and R.shape==(8189,512)
    edges=[Q(j,256) for j in range(129)];J0=mo.moments(Q(1,2),64)[0]
    masses=[mo.moments(Q(1,2)-t,64)[0] for t in edges]
    weights=[Q((masses[j]-masses[j+1]).hi,S) for j in range(128)]
    assert all(w>0 for w in weights)
    bins=[];coverage=np.zeros(len(a),dtype=bool)
    for left,right in zip(edges,edges[1:]):
        mask=(a<=float(right))&(b>=float(left));assert np.any(mask)
        coverage|=mask;bins.append(np.max(R[mask],axis=0))
    assert np.all(coverage)
    nu=Q(raw['nu_exact']);globalr=list(map(Q,low['all_node_radii']));timer=list(globalr)
    nodeledger=[];propagation_start=0
    for j in range(1025):
        ep=ec['cover'][j];oldradius=Q(data['node_error_cover'][j]['true_CF_minus_stored_CF_modulus_upper'])
        record={'index':j,'u':str(Q(j,8)),'psi_re':ep['phi_re'],'psi_im':ep['phi_im'],'psi_modulus':ep['phi_modulus'],
            'joint_coefficient_modulus_upper':str(coeff[j]),'marginal_sum_coefficient_modulus_upper':str(margcoeff[j]),
            'old_CF_radius_centre':('same_nonzero_psi' if j<=512 else 'zero'), 'old_CF_radius':str(oldradius)}
        if j<=512:
            record['radius_source']='unchanged separately verified same-reference time-local low-node radius'
        else:
            k=j-513;physical=Q(raw['delta_physical_upper_exact_dyadics'][k]);delta=physical/nu
            assert Q(raw['first_cell_Re_H_div_talpha_upper_exact_dyadics'][k])<=0
            assert Q(raw['later_cells_Re_H_upper_exact_dyadics'][k])<=0
            eta_global=Q((I(delta)*J0).hi,S)
            eta_time=sum((Q.from_float(float(bins[t][k]))*weights[t] for t in range(128)),Q(0))/nu
            eta=min(eta_global,eta_time);modulus=Q(ep['phi_modulus'][1]);factor=min(Q(1),modulus)
            safe_translated=oldradius+modulus
            proposed_global=Q((I(factor)*(dy.exp_positive(I(eta_global))-1)).hi,S)
            proposed_time=Q((I(factor)*(dy.exp_positive(I(eta))-1)).hi,S)
            globalr[j]=min(safe_translated,proposed_global);timer[j]=min(safe_translated,proposed_time,globalr[j])
            record.update({'radius_source':'new complete high-node residual with physical/nu and certified whole-history half-plane',
                'physical_residual_upper':str(physical),'normalized_delta_F_upper':str(delta),'eta_global_upper':str(eta_global),
                'eta_time_local_upper':str(eta_time),'used_time_local_eta_upper':str(eta),
                'safe_old_disk_translated_to_new_psi_radius':str(safe_translated),'new_disk_embedded_in_old_zero_disk':modulus+timer[j]<=oldradius,
                'first_cell_Re_H_div_talpha_upper':raw['first_cell_Re_H_div_talpha_upper_exact_dyadics'][k],
                'later_cells_Re_H_upper':raw['later_cells_Re_H_upper_exact_dyadics'][k],
                'time_bin_physical_residual_upper':list(map(lambda x:str(Q.from_float(float(x[k]))),bins))})
        record.update({'global_CF_radius_new_psi':str(globalr[j]),'time_local_CF_radius_new_psi':str(timer[j])});nodeledger.append(record)
    propagation_seconds=0-propagation_start;scenarios=[]
    for name,radii in [('global-complete-history',globalr),('128-preselected-closed-time-bins',timer)]:
        radius=remainder+sum((c*r for c,r in zip(coeff,radii)),Q(0));marginalradius=remainder+sum((c*r for c,r in zip(margcoeff,radii)),Q(0))
        interval=[centre-radius,centre+radius];marginalinterval=[centre-marginalradius,centre+marginalradius]
        intersection=[max(interval[0],oldinterval[0]),min(interval[1],oldinterval[1])];assert intersection[0]<=intersection[1]
        absolute=max(map(abs,interval));intersection_abs=max(map(abs,intersection))
        scenarios.append({'scenario':name,'new_signed_centre':str(centre),'joint_radius_upper':str(radius),
            'joint_actual_fast_error_interval':list(map(str,interval)),'joint_absolute_bound_index_points_exact':str(absolute*SCALE),
            'joint_absolute_bound_index_points_outward':upward(absolute*SCALE),
            'same_new_disk_signed_marginal_error_interval':list(map(str,marginalinterval)),
            'same_new_disk_signed_marginal_absolute_bound_index_points_outward':upward(max(map(abs,marginalinterval))*SCALE),
            'legal_old_new_complete_interval_intersection':list(map(str,intersection)),
            'intersection_absolute_bound_index_points_exact':str(intersection_abs*SCALE),
            'intersection_absolute_bound_index_points_outward':upward(intersection_abs*SCALE),
            'old_new_intersection_strictly_improves_new':intersection!=interval,
            'all_high_disks_embedded_in_old_zero_disks':all(Q(ec['cover'][j]['phi_modulus'][1])+radii[j]<=Q(data['node_error_cover'][j]['true_CF_minus_stored_CF_modulus_upper']) for j in range(513,1025)),
            'propagation_scope':'Low nodes retain prior time-local radii in both scenarios; scenario name describes only newly certified high nodes.',
            'budget_decisions':{v:{'new_joint_pass':absolute*SCALE<=Q(v),'intersection_pass':intersection_abs*SCALE<=Q(v)} for v in contract['budgets_index_points']}})
    save('omission-node-ledger.json',{'field_sha256':raw['field_sha256'],'reference_nonzero_nodes':1025,'nodes':nodeledger,
        'time_weights_upper':list(map(str,weights)),'time_edges':list(map(str,edges)),'global_all_node_radii':list(map(str,globalr)),
        'time_local_all_node_radii':list(map(str,timer))})
    files=[HERE/'omission-contract.json',HERE/'omission-propagation-contract.json',HERE/'omission-residual-high.json',HERE/raw['time_envelope_file'],
        HERE/'omission-full-execution.json',NINE/'time-local-results.json',NINE/'time-local-node-ledger.json',OLD/old['node_ledger_file']]
    result={'status':'PASS_EXPANDED_REFERENCE_SAME_ACTUAL_FAST_OUTPUT_FULL_BUDGET','alpha':'13/25','T':'1/2',
        'reference_rows':reference_rows,'old_signed_centre':str(oldcentre),'new_signed_centre':str(centre),
        'signed_reference_centre_correction':str(centre-oldcentre),'centre_correction_index_points_exact':str((centre-oldcentre)*SCALE),
        'old_reference_irreducible_floor_given_zero_low_errors_index_points_outward':upward(oldfloor*SCALE),
        'prior_time_local_complete_error_interval':list(map(str,oldinterval)),
        'prior_time_local_absolute_bound_index_points_outward':lowresult['absolute_error_upper_index_points_display_outward'],
        'new_full_remainder_grid_true_infinite_tail_and_reference_rounding':str(remainder),
        'high_nodes_fresh_certified':512,'closed_time_cells_each':8189,'same_actual_fast_output':True,'same_reference_centre':False,
        'scenarios':scenarios,'contract_sha256':sha(HERE/'omission-contract.json'),
        'dependency_sha256':{str(p.relative_to(HERE.parent)).replace('\\','/'):sha(p) for p in files},
        'source_sha256':sha(Path(__file__)),'interval_primitives_shared':True,'continuous_derivative_generator_shared':True,
        'shared_primitive_sha256':{name:sha(BASE/'code/src'/name) for name in primitive_names},
        
        
        'claim_boundary':'One old fixed field, alpha=.52,T=.5 and one 4400-4500 spread. Proof-conditional numerical certification of unchanged actual fast output; no observed true bias/profitability or minimum-runtime claim.'}
    save('omission-results.json',result)
    print(json.dumps({k:result[k] for k in ['status', 'old_reference_irreducible_floor_given_zero_low_errors_index_points_outward', 'centre_correction_index_points_exact', 'prior_time_local_absolute_bound_index_points_outward', 'scenarios']},indent=2))
if __name__=='__main__':main()
