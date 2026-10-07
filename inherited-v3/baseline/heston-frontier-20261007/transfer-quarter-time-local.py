"""One frozen 128-bin quarter propagation; same full128 centre and remainder."""
from pathlib import Path
from fractions import Fraction as Q
import hashlib, importlib.util, json, sys, time
import numpy as np
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('timequarter_paths',HERE/'independent-transfer.py');ap=importlib.util.module_from_spec(sp);sp.loader.exec_module(ap)
BASE,OUT=ap.BASE,ap.OUT;OLD=HERE.parent/'heston-nine-point-20261007'
T,NU,DF=Q(1,4),Q(2897,10000),Q(211093,50)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def save(name,x):(OUT/name).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def main():
    sys.stdout.reconfigure(encoding='utf-8');started=0
    contract=load(OUT/'transfer-time-local-contract.json');assert contract['bins']==128 and contract['bin_edge_formula']=='j/512 for j=0,...,128'
    global_result=load(OUT/'transfer-supplement-results.json');ledger=load(OUT/'transfer-supplement-node-ledger.json');ec=load(OUT/'transfer-supplement-exponents.json')
    assert global_result['T']=='1/4' and global_result['alpha']=='13/25' and global_result['used_nodes']==1025
    lowrecord=load(OLD/'fresh-all-node-time-residual.json');highrecord=load(OUT/'omission-residual-high.json')
    lowpath=OLD/lowrecord['time_envelope_file'];highpath=OUT/highrecord['time_envelope_file']
    assert sha(lowpath)==lowrecord['time_envelope_sha256'] and sha(highpath)==highrecord['time_envelope_sha256']
    assert lowrecord['field_sha256']==highrecord['field_sha256']==global_result['field_sha256']
    arrays=[]
    for path,record,indices in [(lowpath,lowrecord,range(513)),(highpath,highrecord,range(513,1025))]:
        with np.load(path) as ar:a,b,u,R=[ar[k] for k in ['a','b','u','residual_physical_upper']]
        assert a[0]==0 and b[-1]==.5 and np.all(a<b) and np.array_equal(a[1:],b[:-1]) and np.all(R>=0)
        assert R.shape==(8189,len(indices)) and np.array_equal(u,np.array(list(indices),dtype=np.float64)/8)
        assert [str(Q.from_float(float(v))) for v in np.max(R,axis=0)]==record['delta_physical_upper_exact_dyadics']
        arrays.append((a,b,R))
    edges=[Q(j,512) for j in range(129)]; grouped=[];counts=[]
    for a,b,R in arrays:
        selected_all=np.zeros(len(a),dtype=bool);bins=[];ct=[]
        for left,right in zip(edges,edges[1:]):
            mask=(a<=float(right))&(b>=float(left));assert np.any(mask);selected_all|=mask
            bins.append(np.max(R[mask],axis=0));ct.append(int(np.sum(mask)))
        assert np.array_equal(selected_all,(a<=float(T))&(b>=0));grouped.append(np.array(bins));counts.append(ct)
    bins=np.concatenate(grouped,axis=1);assert bins.shape==(128,1025)
    mo=ap.module('quartertime_moments','exact-forward-moments.py');I,S,dy=mo.I,mo.S,mo.dy
    values=[mo.moments(T-e,64)[0] for e in edges];weights=[]
    for v,w in zip(values,values[1:]):
        d=v-w;assert d.lo>0;weights.append([Q(d.lo,S),Q(d.hi,S)])
    nodes=[];joint=Q(0);marginal=Q(0)
    for j,(row,er) in enumerate(zip(ledger['rows'],ec['cover'])):
        rs=[Q.from_float(float(x)) for x in bins[:,j]];eta_time=sum((r*w[1] for r,w in zip(rs,weights)),Q(0))/NU
        eta=min(Q(row['eta_used_upper']),eta_time);mod=min(Q(1),Q(er['phi_modulus'][1]))
        new=I(mod)*(dy.exp_positive(I(eta))-1);radius=min(Q(row['CF_radius_upper']),Q(new.hi,S))
        jc=radius*Q(row['joint_coefficient_upper']);mc=radius*Q(row['signed_marginal_coefficient_upper']);joint+=jc;marginal+=mc
        nodes.append({'u':row['u'],'eta_time_exact_sum_upper':str(eta_time),'eta_used_upper':str(eta),'global_CF_radius_upper':row['CF_radius_upper'],
                      'time_CF_radius_upper':str(radius),'joint_node_support_exact':str(jc),'signed_marginal_node_support_exact':str(mc)})
    centre=Q(global_result['signed_centre_exact']);rem=Q(global_result['full_remainder_exact']);radius=joint+rem;mrad=marginal+rem
    bound=DF*(abs(centre)+radius);mbound=DF*(abs(centre)+mrad)
    save('transfer-time-local-weights.json',{'T':str(T),'bins':128,'edges':list(map(str,edges)),'weights':[[str(a),str(b)] for a,b in weights],
               'source_closed_cell_counts_per_bin':counts,'positive_weights':True})
    save('transfer-time-local-nodes.json',{'T':str(T),'nodes':nodes})
    sources=[OUT/'transfer-time-local-contract.json',OUT/'transfer-supplement-results.json',OUT/'transfer-supplement-node-ledger.json',OUT/'transfer-supplement-exponents.json',
             lowpath,highpath,OLD/'fresh-all-node-time-residual.json',OUT/'omission-residual-high.json',BASE/'code/src/exact-forward-moments.py']
    result={'status':'COMPLETE_QUARTER_FULL128_TIME_LOCAL_SAME_CENTRE_ACCOUNT','T':str(T),'alpha':'13/25','bins':128,'used_nodes':1025,
        'contract_sha256':sha(OUT/'transfer-time-local-contract.json'),'source_sha256':sha(Path(__file__)),'input_sha256':{p.name:sha(p) for p in sources},
        'component_sha256':{name:sha(OUT/name) for name in ['transfer-time-local-weights.json','transfer-time-local-nodes.json']},
        'unchanged_signed_centre_exact':str(centre),'unchanged_full_remainder_exact':str(rem),'joint_node_support_exact':str(joint),'signed_marginal_node_support_exact':str(marginal),
        'joint_full_radius_exact':str(radius),'signed_marginal_full_radius_exact':str(mrad),'joint_true_minus_actual_fast_interval_exact':[str(centre-radius),str(centre+radius)],
        'joint_absolute_bound_index_points_exact':str(bound),'signed_marginal_absolute_bound_index_points_exact':str(mbound),
        'display_joint_bound_upper_9dp':str(Q(-((-bound.numerator*10**9)//bound.denominator),10**9)),
        'budget_decisions':[{'budget_index_points':str(b),'joint_status':'CERTIFIED' if bound<=b else 'NOT_CERTIFIED',
             'signed_marginal_status':'CERTIFIED' if mbound<=b else 'NOT_CERTIFIED'} for b in [Q(1,4),Q(1,2),Q(1),Q(2)]],
        
        'scope':'Single separately frozen descriptive exploration after global quarter results are known. Same actual fast output/full128 reference/centre/strip/infinite tail/arithmetic; exact128-bin positive full-history weights. No further variants.',
        'cost_scope':'This replay charges the new quarter grouping, moment weights, time-local propagation and full aggregation only. Continuous residual generation and full quarter reference computation are separately recorded upstream costs.'}
    save('transfer-time-local-results.json',result);print('COMPLETE quarter full128 128-bin', float(bound), 'signed marginal', float(mbound), flush=True)
if __name__=='__main__':main()
