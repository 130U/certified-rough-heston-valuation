"""Default saved-bank audit; no repeated expensive continuous reconstruction.

Every delivered closed cell is checked for coverage and consistency. The
derivative enclosure is trusted through the recorded original generator and
transparent instrumentation, not proved again merely by inspecting its array.
Startup is additionally reassembled directly with shared rigorous primitives.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib,importlib.util,json,sys,time
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;BASE=HERE.parent/'english-heston-release';FROZEN=BASE/'code/frozen'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def exact(v):return Q.from_float(float(v))
def check_bank(raw,a,b,u,R):
    import numpy as np
    assert raw['status']=='OUTWARD_BINARY64_INTERVAL_POINT_RESIDUAL_CERTIFICATE'
    assert raw['alpha_exact']==raw['beta_exact']=='13/25' and Q(raw['T_exact'])==Q(1,2)
    assert Q(raw['nu_exact'])==Q(2897,10000)
    assert raw['split']==4 and raw['certified_closed_subintervals']==8189
    assert len(u)==512 and np.array_equal(u,np.arange(513,1025)/8)
    assert R.shape==(8189,512) and len(a)==len(b)==8189
    assert np.all(np.isfinite(R)) and np.all(R>=0)
    assert a[0]==0 and b[-1]==.5 and np.all(a<b) and np.array_equal(b[:-1],a[1:])
    assert [exact(v) for v in R[0]]==list(map(Q,raw['first_cell_physical_upper_exact_dyadics']))
    assert [exact(v) for v in np.max(R,axis=0)]==list(map(Q,raw['delta_physical_upper_exact_dyadics']))
    assert len(raw['u'])==512 and [exact(v) for v in raw['u']]==list(map(exact,u))
    assert len(raw['first_cell_Re_H_div_talpha_upper_exact_dyadics'])==len(raw['later_cells_Re_H_upper_exact_dyadics'])==512
    assert raw['approx_left_halfplane_certified'] is True
    assert all(Q(z)<=0 for z in raw['first_cell_Re_H_div_talpha_upper_exact_dyadics'])
    assert all(Q(z)<=0 for z in raw['later_cells_Re_H_upper_exact_dyadics'])
def main():
    import numpy as np
    started=time.perf_counter();contract=load(HERE/'omission-contract.json')
    for name,digest in contract['source_sha256'].items():assert sha(FROZEN/name)==digest
    frozen_manifest={z['path']:z['sha256'] for z in load(BASE/'code/MANIFEST.json')['artifacts']}
    for name in ['certify-field-residual-v3.py','combined-field-derivative.py','exact-forward-moments.py','interval-pade-certificate.py']:
        assert sha(BASE/'code/src'/name)==frozen_manifest['code/src/'+name]
    raw=load(HERE/'omission-residual-high.json');path=HERE/raw['time_envelope_file']
    assert sha(path)==raw['time_envelope_sha256'];assert raw['field_sha256']==sha(FROZEN/raw['field_file'])
    instrumentation=load(HERE/'omission-instrumentation.json')
    original=BASE/'code/src/certify-field-residual-v3.py';instrumented=HERE/'omission-residual-generator.py'
    assert sha(original)==instrumentation['original_source_sha256']
    text=original.read_text(encoding='utf-8')
    for change in instrumentation['changes']:
        assert text.count(change['before'])==1;text=text.replace(change['before'],change['after'])
    assert text==instrumented.read_text(encoding='utf-8')
    assert sha(instrumented)==instrumentation['instrumented_source_sha256']==raw['source_sha256']
    assert sha(BASE/'code/src/combined-field-derivative.py')==raw['combined_derivative_source_sha256']
    receipt=load(HERE/'omission-full-execution.json');assert receipt['return_code']==0
    assert receipt['source_sha256']==sha(instrumented) and receipt['peak_working_set_bytes']<=1073741824
    assert all(v=='1' for v in receipt['thread_environment'].values())
    with np.load(path,allow_pickle=False) as bank:a,b,u,R=[bank[k] for k in ['a','b','u','residual_physical_upper']]
    check_bank(raw,a,b,u,R)
    with np.load(FROZEN/raw['field_file'],allow_pickle=False) as field:t,fu,A1,A2,LG=[field[k] for k in ['t','u','A1','A2','LG']]
    assert np.all(LG[0]==0) and len(t)==2049 and LG.shape==(2049,1025)
    expected_a=[0.];expected_b=[t[1]]
    for j in range(1,len(t)-1):
        edges=np.linspace(t[j],t[j+1],5);edges[0]=t[j];edges[-1]=t[j+1]
        expected_a.extend(edges[:-1]);expected_b.extend(edges[1:])
    assert np.array_equal(a,expected_a) and np.array_equal(b,expected_b)
    assert np.array_equal(u,fu[513:]);bank_seconds=time.perf_counter()-started
    sp=importlib.util.spec_from_file_location('omission_direct_startup',BASE/'code/src/exact-forward-moments.py')
    mo=importlib.util.module_from_spec(sp);sp.loader.exec_module(mo);I,C,S=mo.I,mo.dy.C,mo.S
    alpha=Q(13,25);nu=Q(2897,10000);rho=Q(-1489,2000);t1=exact(t[1])
    exponents=set([alpha,2*alpha,Q(1)]+[k*alpha for k in range(1,7)]+[alpha+1,2*alpha+1,3*alpha+1,4*alpha+1,2*alpha+2])
    powers={p:mo.power(t1,p) for p in exponents};direct=[];within_first=[]
    for index in range(513,1025):
        uj=exact(fu[index]);c=-(uj*uj+Q(1,4))/2;d=C(rho/2,rho*uj)
        def complex_exact(z):return C(exact(z.real),exact(z.imag))
        A=complex_exact(A1[index]);B=complex_exact(A2[index]);L=complex_exact(LG[1,index])
        H=[(alpha,C(nu*c)/C(mo.gamma_cached(1+alpha))),
           (2*alpha,A*C(mo.gamma_cached(1+alpha)/mo.gamma_cached(1+2*alpha))),
           (3*alpha,B*C(mo.gamma_cached(1+2*alpha)/mo.gamma_cached(1+3*alpha))),
           (alpha+1,L/C(t1*mo.gamma_cached(2+alpha)))]
        terms={}
        def add(p,z):terms[p]=terms.get(p,C(0))+z
        add(alpha,A);add(2*alpha,B);add(Q(1),L/C(t1))
        for p,z in H:add(p,-nu*d*z)
        for p,z in H:
            for q,w in H:add(p+q,-nu*z*w/2)
        bound=I(0)
        for p,z in terms.items():bound+=z.norm2().sqrt()*powers[p]
        value=Q(bound.hi,S);direct.append(str(value));k=index-513
        within_first.append(value<=Q(raw['first_cell_physical_upper_exact_dyadics'][k]))
        assert value<=Q(raw['delta_physical_upper_exact_dyadics'][k]),'independent startup exceeds complete bound'
    negative={}
    import copy
    mutations={'nu_missing':lambda z:z.pop('nu_exact'),'halfplane_false':lambda z:z.update(approx_left_halfplane_certified=False),
               'delta_zero':lambda z:z['delta_physical_upper_exact_dyadics'].__setitem__(0,'0')}
    for name,mutate in mutations.items():
        z=copy.deepcopy(raw);mutate(z)
        try:check_bank(z,a,b,u,R);negative[name]=False
        except (AssertionError,KeyError):negative[name]=True
    for name,args in [('high_node_deleted',(raw,a,b,u[:-1],R[:,:-1])),('closed_cell_deleted',(raw,a[:-1],b[:-1],u,R[:-1])),
                      ('startup_discarded',(raw,a[1:],b[1:],u,R[1:]))]:
        try:check_bank(*args);negative[name]=False
        except (AssertionError,KeyError):negative[name]=True
    assert all(negative.values())
    result={'status':'PASS_ALL_SAVED_HIGH_NODE_CELLS_AND_DIRECT_STARTUP_AUDIT','nodes':512,'closed_cells':8189,
        'all_4192768_nonnegative_residual_entries_checked':True,'exact_source_partition_checked':True,
        'all_complete_residual_maxima_checked':True,'all_startup_and_later_halfplane_upper_bounds_nonpositive':True,
        'direct_caputo_startup_upper_bounds':direct,'direct_startup_within_saved_first_cell_count':sum(within_first),
        'direct_startup_within_saved_complete_residual_count':512,'negative_controls_rejected':negative,
        'contract_sha256':sha(HERE/'omission-contract.json'),'residual_record_sha256':sha(HERE/'omission-residual-high.json'),
        'matrix_sha256':sha(path),'source_sha256':sha(Path(__file__)),
        'costs_seconds':{'saved_bank_read_and_full_consistency':bank_seconds,'default_saved_evidence_audit_total':time.perf_counter()-started},
        'trust_boundary':'Saved all-cell coverage and maxima consistency are complete inspections, not independent recalculation of every derivative enclosure. Original residual mathematics and interval Gamma/power primitives are shared; direct startup assembly is separate. Optional fresh full reconstruction costs are recorded separately.'}
    (HERE/'omission-verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='direct_caputo_startup_upper_bounds'},indent=2))
if __name__=='__main__':main()
