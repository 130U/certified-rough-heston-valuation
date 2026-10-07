"""Independent full128 quarter readback, without importing its producer.

Default validates the entire high-frequency continuous-cell ledger, freshly
replays all1025 CF/tail/financial terms; --full also replays1025 exact exponent
components. Shares only the identified upstream arithmetic and comparison.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse, copy, hashlib, importlib.util, json, platform, sys, time
import numpy as np
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('shared_independent_path_helpers',HERE/'independent-transfer.py')
other=importlib.util.module_from_spec(sp);sp.loader.exec_module(other)
BASE,OUT,SRC,FROZEN=other.BASE,other.OUT,other.SRC,other.FROZEN
T,A,NU,H,V,STRIP,DF=Q(1,4),Q(13,25),Q(2897,10000),Q(1,8),Q(128),Q(9,20),Q(211093,50)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def validate_high_cells(a,b,u,values,maxima):
    assert a.dtype==b.dtype==u.dtype==values.dtype==np.dtype('float64')
    assert a.shape==b.shape==(8189,) and u.shape==(512,) and values.shape==(8189,512)
    assert all(np.all(np.isfinite(x)) for x in (a,b,u,values)) and np.all(values>=0)
    assert a[0]==0 and b[-1]==.5 and np.all(a<b) and np.array_equal(a[1:],b[:-1])
    assert np.array_equal(u,np.arange(513,1025,dtype=np.float64)/8)
    assert [str(Q.from_float(float(v))) for v in np.max(values,axis=0)]==maxima
def check_account(saved,expected):
    for key,value in expected.items():assert saved[key]==value,(key,'incomplete full-reference financial account')
def check_time_local(global_result,global_ledger,exponents,mo,I,S,dy):
    """Separate searchsorted closed-cell grouping and exact upper-endpoint sum."""
    started=time.perf_counter();saved=load(OUT/'transfer-time-local-results.json');contract=load(OUT/'transfer-time-local-contract.json')
    assert saved['status']=='COMPLETE_QUARTER_FULL128_TIME_LOCAL_SAME_CENTRE_ACCOUNT' and saved['T']=='1/4' and saved['alpha']=='13/25'
    assert contract['bins']==128 and contract['bin_edge_formula']=='j/512 for j=0,...,128'
    assert saved['contract_sha256']==sha(OUT/'transfer-time-local-contract.json') and saved['source_sha256']==sha(HERE/'transfer-quarter-time-local.py')
    old=HERE.parent/'heston-nine-point-20261007';hashes={}
    for name,expected_hash in saved['input_sha256'].items():
        if name in ['time-residual-alpha-13_25.npz','fresh-all-node-time-residual.json']:path=old/name
        elif name=='exact-forward-moments.py':path=SRC/name
        else:path=OUT/name
        assert sha(path)==expected_hash;hashes[name]=expected_hash
    for name,expected_hash in saved['component_sha256'].items():assert sha(OUT/name)==expected_hash;hashes[name]=expected_hash
    records=[load(old/'fresh-all-node-time-residual.json'),load(OUT/'omission-residual-high.json')]
    paths=[old/records[0]['time_envelope_file'],OUT/records[1]['time_envelope_file']]
    groups=[];counts=[];covered_counts=[]
    edges=[Q(j,512) for j in range(129)]
    for path,record,first,nodes in zip(paths,records,[0,513],[513,512]):
        assert record['field_sha256']==global_result['field_sha256'] and record['T_exact']=='1/2' and record['alpha_exact']=='13/25'
        assert record['approx_left_halfplane_certified'] and record['polynomial_startup_cancellation']
        assert all(Q(v)<=0 for v in record['first_cell_Re_H_div_talpha_upper_exact_dyadics']+record['later_cells_Re_H_upper_exact_dyadics'])
        assert sha(path)==record['time_envelope_sha256']
        with np.load(path) as ar:a,b,u,R=[ar[k] for k in ['a','b','u','residual_physical_upper']]
        assert a.shape==b.shape==(8189,) and u.shape==(nodes,) and R.shape==(8189,nodes)
        assert all(x.dtype==np.dtype('float64') and np.all(np.isfinite(x)) for x in [a,b,u,R]) and np.all(R>=0)
        assert a[0]==0 and b[-1]==.5 and np.all(a<b) and np.array_equal(a[1:],b[:-1])
        assert np.array_equal(u,np.arange(first,first+nodes,dtype=np.float64)/8)
        assert [str(Q.from_float(float(x))) for x in np.max(R,axis=0)]==record['delta_physical_upper_exact_dyadics']
        rows=[];ct=[];covered=np.zeros(8189,dtype=bool)
        for left,right in zip(edges,edges[1:]):
            start=int(np.searchsorted(b,float(left),side='left'));stop=int(np.searchsorted(a,float(right),side='right'))
            assert 0<=start<stop<=8189 and np.all(b[start:stop]>=float(left)) and np.all(a[start:stop]<=float(right))
            assert start==0 or b[start-1]<float(left)
            assert stop==8189 or a[stop]>float(right)
            rows.append([Q.from_float(float(x)) for x in np.max(R[start:stop],axis=0)]);ct.append(stop-start);covered[start:stop]=True
        assert np.array_equal(covered,(a<=float(T))&(b>=0));covered_counts.append(int(np.sum(covered)));groups.append(rows);counts.append(ct)
    values=[mo.moments(T-edge,64)[0] for edge in edges];weights=[]
    for a,b in zip(values,values[1:]):d=a-b;assert d.lo>0;weights.append([Q(d.lo,S),Q(d.hi,S)])
    supplied=load(OUT/'transfer-time-local-weights.json');assert supplied['edges']==list(map(str,edges)) and supplied['source_closed_cell_counts_per_bin']==counts
    def validate_weights(ws):assert ws==[[str(a),str(b)] for a,b in weights]
    validate_weights(supplied['weights'])
    node_records=load(OUT/'transfer-time-local-nodes.json')['nodes'];assert len(node_records)==1025
    joint=Q(0);marginal=Q(0)
    for j,(old_row,ex,row) in enumerate(zip(global_ledger['rows'],exponents['cover'],node_records)):
        bounds=[groups[0][k][j] if j<513 else groups[1][k][j-513] for k in range(128)]
        eta_time=sum((r*weight[1] for r,weight in zip(bounds,weights)),Q(0))/NU;eta=min(Q(old_row['eta_used_upper']),eta_time)
        modulus=min(Q(1),Q(ex['phi_modulus'][1]));proposal=I(modulus)*(dy.exp_positive(I(eta))-1)
        radius=min(Q(old_row['CF_radius_upper']),Q(proposal.hi,S));jc=radius*Q(old_row['joint_coefficient_upper']);mc=radius*Q(old_row['signed_marginal_coefficient_upper'])
        assert row=={'u':old_row['u'],'eta_time_exact_sum_upper':str(eta_time),'eta_used_upper':str(eta),'global_CF_radius_upper':old_row['CF_radius_upper'],
                     'time_CF_radius_upper':str(radius),'joint_node_support_exact':str(jc),'signed_marginal_node_support_exact':str(mc)}
        joint+=jc;marginal+=mc
    centre=Q(global_result['signed_centre_exact']);remainder=Q(global_result['full_remainder_exact']);radius=joint+remainder;mrad=marginal+remainder
    bound=DF*(abs(centre)+radius);mbound=DF*(abs(centre)+mrad)
    expected={'unchanged_signed_centre_exact':str(centre),'unchanged_full_remainder_exact':str(remainder),'joint_node_support_exact':str(joint),
         'signed_marginal_node_support_exact':str(marginal),'joint_full_radius_exact':str(radius),'signed_marginal_full_radius_exact':str(mrad),
         'joint_true_minus_actual_fast_interval_exact':[str(centre-radius),str(centre+radius)],'joint_absolute_bound_index_points_exact':str(bound),
         'signed_marginal_absolute_bound_index_points_exact':str(mbound),
         'budget_decisions':[{'budget_index_points':str(b),'joint_status':'CERTIFIED' if bound<=b else 'NOT_CERTIFIED',
         'signed_marginal_status':'CERTIFIED' if mbound<=b else 'NOT_CERTIFIED'} for b in [Q(1,4),Q(1,2),Q(1),Q(2)]]}
    check_account(saved,expected)
    negatives=[]
    for name,fn in [('quarter-bin-weight-removed',lambda:validate_weights(supplied['weights'][:-1])),
                     ('time-local-centre-replaced-by-zero',lambda:check_account({**saved,'unchanged_signed_centre_exact':'0'},expected))]:
        try:fn()
        except AssertionError:negatives.append({'name':name,'status':'PASS_REJECTED'})
        else:raise AssertionError('invalid time-local quarter data accepted')
    hashes['transfer-time-local-results.json']=sha(OUT/'transfer-time-local-results.json')
    return {'status':'PASS_INDEPENDENT_QUARTER_FULL128_128_BIN_COMPLETE_ACCOUNT','bins':128,'nodes':1025,
       'all_positive_weight_intervals_checked':128,'closed_source_cells_intersecting_quarter_per_file':covered_counts,
       'all_intersecting_closed_cell_bin_maxima_checked':128*1025,'joint_absolute_bound_index_points_exact':str(bound),
       'signed_marginal_absolute_bound_index_points_exact':str(mbound),'budget_decisions':expected['budget_decisions'],
       'input_sha256':hashes,'negative_controls':negatives,'wall_seconds':time.perf_counter()-started,
       'independence':'Independent searchsorted closed-intersection spans rather than producer masks. Independent exactFraction sums of freshly recomputed positive weight upper endpoints. Same rigorously enclosed quarter reference and full remainders were independently replayed earlier in this invocation.'}
def main():
    sys.stdout.reconfigure(encoding='utf-8');p=argparse.ArgumentParser(description=__doc__);p.add_argument('--full',action='store_true');args=p.parse_args()
    started=time.perf_counter();result=load(OUT/'transfer-supplement-results.json');contract=load(OUT/'transfer-supplement-contract.json');inputs={}
    assert result['status']=='COMPLETE_QUARTER_SUPPLEMENT_FULL_REFERENCE128_SAME_ACTUAL_FAST_OUTPUT'
    assert result['T']=='1/4' and result['alpha']=='13/25' and result['used_nodes']==1025 and result['omitted_finite_nodes']==0
    assert contract['T_exact']==result['T'] and contract['nodes']==1025 and result['contract_sha256']==sha(OUT/'transfer-supplement-contract.json')
    for name,expected in result['input_sha256'].items():
        if name.startswith('fixed-field-') or name.startswith('residual-node-'):path=FROZEN/name
        elif name in ['exponent-field-certificate.py','exact-forward-moments.py','direct-tail-certificate.py']:path=SRC/name
        elif name.endswith('.py') and (HERE/name).is_file():path=HERE/name
        else:path=OUT/name
        assert sha(path)==expected,(name,'input identity');inputs[name]=expected
    for name,expected in result['component_sha256'].items():assert sha(OUT/name)==expected;inputs[name]=expected
    field=FROZEN/'fixed-field-betap52-u128.npz';manifest=load(BASE/'code/MANIFEST.json');trust={x['path']:x['sha256'] for x in manifest['artifacts']}
    lowpath=FROZEN/'residual-node-certificate-point052-v3-u64.json';low=load(lowpath);other.validate_profile(low,A)
    assert sha(field)==trust['code/frozen/'+field.name] and sha(lowpath)==trust['code/frozen/'+lowpath.name]
    high=load(OUT/'omission-residual-high.json');assert high['status']=='OUTWARD_BINARY64_INTERVAL_POINT_RESIDUAL_CERTIFICATE'
    assert high['field_sha256']==result['field_sha256']==low['field_sha256']==sha(field)
    assert high['T_exact']=='1/2' and high['alpha_exact']==high['beta_exact']=='13/25' and Q(high['nu_exact'])==NU
    assert high['approx_left_halfplane_certified'] and high['polynomial_startup_cancellation'] and high['certified_closed_subintervals']==8189
    assert list(map(Q,high['u']))==[j*H for j in range(513,1025)]
    assert all(Q(v)<=0 for v in high['first_cell_Re_H_div_talpha_upper_exact_dyadics']+high['later_cells_Re_H_upper_exact_dyadics'])
    assert sha(OUT/high['time_envelope_file'])==high['time_envelope_sha256']
    with np.load(OUT/high['time_envelope_file']) as ar:a,b,raw_u,values=[ar[k] for k in ['a','b','u','residual_physical_upper']]
    validate_high_cells(a,b,raw_u,values,high['delta_physical_upper_exact_dyadics'])
    delta_phys=[Q(x['delta_physical_upper']) for x in low['cover']]+list(map(Q,high['delta_physical_upper_exact_dyadics']))
    comp=other.module('ind_full128_component','exponent-field-certificate.py');mo,I,S,C=comp.mo,comp.I,comp.S,comp.C;dy=mo.dy
    direct=other.module('ind_full128_tail','direct-tail-certificate.py');direct.T=T
    def hi(x):return Q(x.hi,S)
    def iv(bound):
        lo,up=map(Q,bound);assert lo<=up
        return I((lo.numerator*S)//lo.denominator,-((-up.numerator*S)//up.denominator),True)
    def eq(x):return Q.from_float(float(x))
    def absiv(x):return I(0 if x.lo<=0<=x.hi else min(abs(x.lo),abs(x.hi)),max(abs(x.lo),abs(x.hi)),True)
    ep=load(OUT/'transfer-supplement-exponents.json');assert ep['field_sha256']==sha(field) and ep['T']=='1/4' and ep['bits']==100
    assert [Q(x['u']) for x in ep['cover']]==[j*H for j in range(1025)]
    with np.load(field) as ar:data={k:ar[k] for k in ar.files}
    times=[eq(x) for x in data['t']];left=max(i for i,t in enumerate(times) if t<T);r=(T-times[left])/(times[left+1]-times[left])
    trimmed=times[:left+1]+[T];assert ep['terminal_cell_index']==left and ep['terminal_interpolation_fraction']==str(r) and ep['time_nodes']==list(map(str,trimmed))
    J0=mo.moments(T,64)[0];count=0
    if args.full:
        weights=mo.linear_field_weights(trimmed,T,64);w1=mo.power_field_moment(A,T,64);w2=mo.power_field_moment(2*A,T,64)
        assert ep['linear_forward_weights']==[x.bounds() for x in weights] and ep['J0']==J0.bounds() and ep['power_moments']==[w1.bounds(),w2.bounds()]
        for j,saved in enumerate(ep['cover']):
            u=j*H;a1,a2=complex(data['A1'][j]),complex(data['A2'][j])
            ex=C(-(u*u+Q(1,4))/2)*J0+C(eq(a1.real),eq(a1.imag))*w1/NU+C(eq(a2.real),eq(a2.imag))*w2/NU
            for k,w in enumerate(weights[:-1]):
                z=complex(data['LG'][k,j]);ex+=C(eq(z.real),eq(z.imag))*w/NU
            zl,zr=complex(data['LG'][left,j]),complex(data['LG'][left+1,j])
            terminal=C(eq(zl.real)+r*(eq(zr.real)-eq(zl.real)),eq(zl.imag)+r*(eq(zr.imag)-eq(zl.imag)))
            ex+=terminal*weights[-1]/NU;mag=mo.signed_exp(ex.re);ph=C(mag*comp.trig(ex.im,True),mag*comp.trig(ex.im))
            assert saved['exponent_re']==ex.re.bounds() and saved['exponent_im']==ex.im.bounds() and saved['phi_modulus']==mag.bounds()
            assert saved['phi_re']==ph.re.bounds() and saved['phi_im']==ph.im.bounds();count+=1
            if j and j%256==0:print('independent quarter full128 exponent',j,flush=True)
    td=direct.time_data(A,64);rate=direct.tail_rate(V,A,td);assert rate.lo>0;cl=Q(rate.lo,direct.S)
    tailintegral=mo.signed_exp(I(-cl*V))/(cl*V*V);m=[Q(4400)/DF,Q(4500)/DF];pref=[I(x).sqrt()/dy.PI for x in m];logs=[mo.log_endpoint(x) for x in m]
    grid_den=(Q(1,2)-STRIP)*(dy.exp_positive(2*dy.PI*STRIP/H)-1)
    grid=[I(x).sqrt()*mo.signed_exp(STRIP*absiv(k))/grid_den for x,k in zip(m,logs)];tails=[p*tailintegral for p in pref]
    oldmass=mo.THETA*mo.power(T,1-A)/(NU*mo.gamma_cached(2-A));calls=[I(1),I(1)];joint=Q(0);marginal=Q(0)
    ledger=load(OUT/'transfer-supplement-node-ledger.json');assert len(ledger['rows'])==1025
    for j,(row,er) in enumerate(zip(ledger['rows'],ep['cover'])):
        u=j*H;assert Q(row['u'])==u;mod=iv(er['phi_modulus']);phi=C(iv(er['phi_re']),iv(er['phi_im']));btrue,ex=direct.envelope_node(u,A,td);true=Q(btrue.hi,direct.S)
        delta=delta_phys[j]/NU;oldeta=hi(oldmass*(I(delta)/Q(1489,4000)));neweta=hi(I(delta)*J0);eta=min(oldeta,neweta)
        residual_bound=hi(I(min(S,mod.lo),min(S,mod.hi),True)*(dy.exp_positive(I(eta))-1));tri=hi(I(true)+mod);eps=min(residual_bound,tri)
        for key,value in [('delta_physical_upper',delta_phys[j]),('eta_old_uniform_upper',oldeta),('eta_finite_history_upper',neweta),
                          ('eta_used_upper',eta),('true_CF_modulus_upper',true),('residual_radius_upper',residual_bound),('triangle_radius_upper',tri),('CF_radius_upper',eps)]:assert Q(row[key])==value
        coeff=[]
        for p,k in zip(pref,logs):
            if j==0:coeff.append(C(-2*H*p))
            else:
                ang=-u*k;coeff.append(C(comp.trig(ang,True),comp.trig(ang))*(-H*p/(u*u+Q(1,4))))
        for k,c in enumerate(coeff):calls[k]+=(c*phi).re
        cj=hi((coeff[0]-coeff[1]).norm2().sqrt());cm=hi(coeff[0].norm2().sqrt()+coeff[1].norm2().sqrt());jc=eps*cj;mc=eps*cm
        assert Q(row['joint_coefficient_upper'])==cj and Q(row['signed_marginal_coefficient_upper'])==cm
        assert Q(row['joint_node_support_exact'])==jc and Q(row['signed_marginal_node_support_exact'])==mc;joint+=jc;marginal+=mc
    actual=load(OUT/'transfer-fast-output.json')['rows'][0];assert actual['alpha']=='13/25' and actual['T']=='1/4'
    fastcalls=list(map(Q,actual['normalized_call_exact_stored_binary64']));mids=[Q(x.lo+x.hi,2*S) for x in calls]
    centre=mids[0]-mids[1]-fastcalls[0]+fastcalls[1];arith=sum((Q(x.hi-x.lo,2*S) for x in calls),Q(0));strip=sum(map(hi,grid),Q(0));tail=sum(map(hi,tails),Q(0));rem=arith+strip+tail
    radius=joint+rem;mrad=marginal+rem;bound=DF*(abs(centre)+radius);mbound=DF*(abs(centre)+mrad)
    expected={'reference_normalized_call_intervals':[x.bounds() for x in calls],'signed_centre_exact':str(centre),'reference_arithmetic_radius':str(arith),
       'true_strip_upper':str(strip),'true_infinite_tail_upper':str(tail),'new_quarter_tail_rate_lower':str(cl),'full_remainder_exact':str(rem),
       'joint_node_support_exact':str(joint),'signed_marginal_node_support_exact':str(marginal),'joint_full_radius_exact':str(radius),'signed_marginal_full_radius_exact':str(mrad),
       'joint_true_minus_actual_fast_interval_exact':[str(centre-radius),str(centre+radius)],
       'joint_absolute_bound_index_points_exact':str(bound),'signed_marginal_absolute_bound_index_points_exact':str(mbound),
       'budget_decisions':[{'budget_index_points':str(b),'joint_status':'CERTIFIED' if bound<=b else 'NOT_CERTIFIED',
       'signed_marginal_status':'CERTIFIED' if mbound<=b else 'NOT_CERTIFIED'} for b in [Q(1,4),Q(1,2),Q(1),Q(2)]]}
    check_account(result,expected)
    negative=[]
    def reject(name,fn):
        try:fn()
        except (AssertionError,ValueError,IndexError):negative.append({'name':name,'status':'PASS_REJECTED'})
        else:raise AssertionError('invalid supplemental account accepted: '+name)
    reject('closed-high-frequency-cell-missing',lambda:validate_high_cells(a[:-1],b[:-1],raw_u,values[:-1],high['delta_physical_upper_exact_dyadics']))
    changed=copy.deepcopy(result);changed['signed_centre_exact']=load(OUT/'transfer-results.json')['rows'][0]['signed_centre_exact']
    reject('old-used64-centre-reused-after-nonzero-reference',lambda:check_account(changed,expected))
    changedtail=copy.deepcopy(result);changedtail['true_infinite_tail_upper']='0'
    reject('infinite-tail-dropped-after-full-finite-reference',lambda:check_account(changedtail,expected))
    time_check=check_time_local(result,ledger,ep,mo,I,S,dy)
    receipt={'status':'PASS_INDEPENDENT_QUARTER_FULL_REFERENCE128_COMPLETE_ACCOUNT','mode':'FULL_SOURCE_COMPONENT_REPLAY' if args.full else 'IDENTITY_CHECKED_COMPONENT_REPLAY',
       'source_sha256':sha(Path(__file__)),'input_sha256':inputs,'producer_result_sha256':sha(OUT/'transfer-supplement-results.json'),
       'continuous_closed_cells_verified':8189,'high_frequency_nodes_verified':512,'closed_cell_node_pairs_verified':8189*512,
       'exact_exponents_replayed':count,'true_CF_and_financial_nodes_replayed':1025,'negative_controls':negative,
       'joint_absolute_bound_index_points_exact':str(bound),'signed_marginal_absolute_bound_index_points_exact':str(mbound),'budget_decisions':expected['budget_decisions'],
       'time_local_verification':time_check,'wall_seconds':time.perf_counter()-started,'python_version':platform.python_version(),'numpy_version':np.__version__,
       'independence':'No producer import. Uses independently written exponent and financial loops, shared original rigorous moment/trig/tail/dyadic primitives and only path/profile helpers from independent-transfer.py. Checks the complete new upstream cell ledger but does not regenerate its Caputo residual calculation. Original new-quarter actual fast output was separately fully replayed by independent-transfer.py --full.'}
    (OUT/'independent-transfer-supplement.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('PASS independent complete quarter full128',float(bound),'seconds',receipt['wall_seconds'],flush=True)
if __name__=='__main__':main()
