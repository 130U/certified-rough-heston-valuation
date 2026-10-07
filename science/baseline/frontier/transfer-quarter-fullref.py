"""Optional fixed-alpha complete T=1/4 full-reference128 certificate.

No modification of original all-three transfer results or actual outputs.
"""
from pathlib import Path
from fractions import Fraction as Q
import hashlib, importlib.util, json, platform, sys, time
import numpy as np
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
helper=HERE/'audit_paths.py'
if not helper.is_file():helper=HERE.parent/'continuous/audit_paths.py'
sp=importlib.util.spec_from_file_location('q128_paths',helper);ap=importlib.util.module_from_spec(sp);sp.loader.exec_module(ap)
BASE,OUT=ap.release_root(HERE),ap.evidence_directory(HERE)
SRC,FROZEN=BASE/'code/src',BASE/'code/frozen'
T,A,NU,H,V,STRIP,DF=Q(1,4),Q(13,25),Q(2897,10000),Q(1,8),Q(128),Q(9,20),Q(211093,50)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def save(name,x):
    path=OUT/name;path.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8');return path
def module(name,file):
    sp=importlib.util.spec_from_file_location(name,SRC/file);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def main():
    sys.stdout.reconfigure(encoding='utf-8');started=0;costs={};source_sha=sha(Path(__file__))
    contract_path=OUT/'transfer-supplement-contract.json';contract=load(contract_path);assert contract['T_exact']=='1/4' and contract['nodes']==1025
    field=FROZEN/'fixed-field-betap52-u128.npz';assert sha(field)==contract['field_sha256']
    meta=load(field.with_suffix('.json'));assert meta['nu_exact']==str(NU) and meta['rho_exact']=='-1489/2000' and meta['kappa_exact']=='0'
    highpath=OUT/'omission-residual-high.json';high=load(highpath);assert high['field_sha256']==sha(field)
    assert high['status']=='OUTWARD_BINARY64_INTERVAL_POINT_RESIDUAL_CERTIFICATE' and high['T_exact']=='1/2'
    assert Q(high['alpha_exact'])==Q(high['beta_exact'])==A and Q(high['nu_exact'])==NU
    assert list(map(Q,high['u']))==[j*H for j in range(513,1025)] and high['certified_closed_subintervals']==8189
    assert high['approx_left_halfplane_certified'] and high['polynomial_startup_cancellation']
    assert all(Q(x)<=0 for x in high['first_cell_Re_H_div_talpha_upper_exact_dyadics']+high['later_cells_Re_H_upper_exact_dyadics'])
    assert sha(OUT/high['time_envelope_file'])==high['time_envelope_sha256']
    assert sha(OUT/'omission-residual-generator.py')==high['source_sha256']
    lowpath=FROZEN/'residual-node-certificate-point052-u64.json';low=load(lowpath)
    assert low['field_sha256']==sha(field) and low['status']=='EXACT_CONTINUOUS_RESIDUAL_CERTIFICATE'
    assert [Q(x['u']) for x in low['cover']]==[j*H for j in range(513)]
    assert all(Q(x['approx_halfplane_upper'])<=0 for x in low['cover'])
    delta_phys=[Q(x['delta_physical_upper']) for x in low['cover']]+list(map(Q,high['delta_physical_upper_exact_dyadics']))
    assert len(delta_phys)==1025 and all(x>=0 for x in delta_phys)
    comp=module('supplement_exactfield','exponent-field-certificate.py');mo,I,S,C=comp.mo,comp.I,comp.S,comp.C;dy=mo.dy
    direct=module('supplement_truetail','direct-tail-certificate.py');direct.T=T
    def hi(x):return Q(x.hi,S)
    def absiv(x):return I(0 if x.lo<=0<=x.hi else min(abs(x.lo),abs(x.hi)),max(abs(x.lo),abs(x.hi)),True)
    def eq(x):return Q.from_float(float(x))
    with np.load(field) as ar:data={k:ar[k] for k in ar.files}
    times=[eq(x) for x in data['t']];left=max(i for i,t in enumerate(times) if t<T);r=(T-times[left])/(times[left+1]-times[left])
    trimmed=times[:left+1]+[T];one=0;weights=mo.linear_field_weights(trimmed,T,64)
    J0=mo.moments(T,64)[0];w1=mo.power_field_moment(A,T,64);w2=mo.power_field_moment(2*A,T,64)
    pass
    one=0;exponent_rows=[];phis=[];moduli=[]
    for j in range(1025):
        u=j*H;a1=complex(data['A1'][j]);a2=complex(data['A2'][j])
        ex=C(-(u*u+Q(1,4))/2)*J0+C(eq(a1.real),eq(a1.imag))*w1/NU+C(eq(a2.real),eq(a2.imag))*w2/NU
        for k,w in enumerate(weights[:-1]):
            z=complex(data['LG'][k,j]);ex+=C(eq(z.real),eq(z.imag))*w/NU
        zl,zr=complex(data['LG'][left,j]),complex(data['LG'][left+1,j])
        terminal=C(eq(zl.real)+r*(eq(zr.real)-eq(zl.real)),eq(zl.imag)+r*(eq(zr.imag)-eq(zl.imag)))
        ex+=terminal*weights[-1]/NU;mod=mo.signed_exp(ex.re);phi=C(mod*comp.trig(ex.im,True),mod*comp.trig(ex.im))
        phis.append(phi);moduli.append(mod);exponent_rows.append({'u':str(u),'exponent_re':ex.re.bounds(),'exponent_im':ex.im.bounds(),
                  'phi_re':phi.re.bounds(),'phi_im':phi.im.bounds(),'phi_modulus':mod.bounds()})
        if j and j%256==0:print('new-quarter full128 reference',j,round(0-one,2),flush=True)
    pass
    ep=save('transfer-supplement-exponents.json',{'status':'EXACT_QUARTER_FULL128_FIELD_COMPONENT_NOT_TRUE_CF_CERTIFICATE',
          'T':str(T),'alpha':str(A),'field_sha256':sha(field),'bits':100,'contract_sha256':sha(contract_path),
          'source_sha256':source_sha,'terminal_cell_index':left,'terminal_interpolation_fraction':str(r),
          'time_nodes':list(map(str,trimmed)),'linear_forward_weights':[x.bounds() for x in weights],
          'J0':J0.bounds(),'power_moments':[w1.bounds(),w2.bounds()],'cover':exponent_rows})
    one=0;td=direct.time_data(A,64);tailrate=direct.tail_rate(V,A,td);assert tailrate.lo>0
    true=[]
    for j in range(1025):b,ex=direct.envelope_node(j*H,A,td);true.append(Q(b.hi,direct.S))
    cl=Q(tailrate.lo,direct.S);tailint=mo.signed_exp(I(-cl*V))/(cl*V*V)
    m=[Q(4400)/DF,Q(4500)/DF];pref=[I(x).sqrt()/dy.PI for x in m];logs=[mo.log_endpoint(x) for x in m]
    grid_den=(Q(1,2)-STRIP)*(dy.exp_positive(2*dy.PI*STRIP/H)-1)
    strips=[I(x).sqrt()*mo.signed_exp(STRIP*absiv(k))/grid_den for x,k in zip(m,logs)];tails=[p*tailint for p in pref]
    pass
    one=0;oldmass=mo.THETA*mo.power(T,1-A)/(NU*mo.gamma_cached(2-A));calls=[I(1),I(1)];joint=Q(0);marginal=Q(0);ledger=[]
    for j,(mod,phi) in enumerate(zip(moduli,phis)):
        u=j*H;delta=delta_phys[j]/NU;oldeta=hi(oldmass*(I(delta)/Q(1489,4000)));neweta=hi(I(delta)*J0);eta=min(oldeta,neweta)
        residual_bound=hi(I(min(S,mod.lo),min(S,mod.hi),True)*(dy.exp_positive(I(eta))-1));tri=hi(I(true[j])+mod);eps=min(residual_bound,tri)
        cs=[]
        for p,k in zip(pref,logs):
            if j==0:cs.append(C(-2*H*p))
            else:
                ang=-u*k;cs.append(C(comp.trig(ang,True),comp.trig(ang))*(-H*p/(u*u+Q(1,4))))
        for k,c in enumerate(cs):calls[k]+=(c*phi).re
        cj=hi((cs[0]-cs[1]).norm2().sqrt());cm=hi(cs[0].norm2().sqrt()+cs[1].norm2().sqrt())
        joint+=eps*cj;marginal+=eps*cm
        ledger.append({'u':str(u),'delta_physical_upper':str(delta_phys[j]),'eta_old_uniform_upper':str(oldeta),'eta_finite_history_upper':str(neweta),
            'eta_used_upper':str(eta),'reference_modulus_upper':str(hi(mod)),'true_CF_modulus_upper':str(true[j]),
            'residual_radius_upper':str(residual_bound),'triangle_radius_upper':str(tri),'CF_radius_upper':str(eps),
            'joint_coefficient_upper':str(cj),'signed_marginal_coefficient_upper':str(cm),
            'joint_node_support_exact':str(eps*cj),'signed_marginal_node_support_exact':str(eps*cm)})
    lp=save('transfer-supplement-node-ledger.json',{'T':str(T),'alpha':str(A),'used_nodes':1025,'rows':ledger})
    actual=load(OUT/'transfer-fast-output.json')['rows'][0];assert Q(actual['alpha'])==A
    fastcalls=list(map(Q,actual['normalized_call_exact_stored_binary64']));mids=[Q(x.lo+x.hi,2*S) for x in calls]
    centre=mids[0]-mids[1]-fastcalls[0]+fastcalls[1];arith=sum((Q(x.hi-x.lo,2*S) for x in calls),Q(0))
    strip=sum((hi(x) for x in strips),Q(0));tail=sum((hi(x) for x in tails),Q(0));rem=strip+tail+arith
    radius=joint+rem;mrad=marginal+rem;bound=DF*(abs(centre)+radius);mbound=DF*(abs(centre)+mrad)
    pass
    input_paths=[contract_path,OUT/'transfer-contract.json',OUT/'transfer-fast-output.json',OUT/'transfer-results.json',field,field.with_suffix('.json'),lowpath,highpath,
                 OUT/'omission-residual-generator.py',SRC/'exponent-field-certificate.py',SRC/'exact-forward-moments.py',SRC/'direct-tail-certificate.py',OUT/high['time_envelope_file']]
    result={'status':'COMPLETE_QUARTER_SUPPLEMENT_FULL_REFERENCE128_SAME_ACTUAL_FAST_OUTPUT','T':str(T),'alpha':str(A),'bits':100,
        'used_nodes':1025,'omitted_finite_nodes':0,'true_infinite_tail_cutoff':'128','field_sha256':sha(field),'contract_sha256':sha(contract_path),
        'source_sha256':source_sha,'input_sha256':{p.name:sha(p) for p in input_paths},'component_sha256':{ep.name:sha(ep),lp.name:sha(lp)},
        'actual_fast_normalized_calls':list(map(str,fastcalls)),'reference_normalized_call_intervals':[x.bounds() for x in calls],
        'signed_centre_exact':str(centre),'reference_arithmetic_radius':str(arith),'true_strip_upper':str(strip),'true_infinite_tail_upper':str(tail),
        'new_quarter_tail_rate_lower':str(cl),'full_remainder_exact':str(rem),'joint_node_support_exact':str(joint),'signed_marginal_node_support_exact':str(marginal),
        'joint_full_radius_exact':str(radius),'signed_marginal_full_radius_exact':str(mrad),
        'joint_true_minus_actual_fast_interval_exact':[str(centre-radius),str(centre+radius)],
        'joint_absolute_bound_index_points_exact':str(bound),'signed_marginal_absolute_bound_index_points_exact':str(mbound),
        'display_joint_bound_upper_9dp':str(Q(-((-bound.numerator*10**9)//bound.denominator),10**9)),
        'budget_decisions':[{'budget_index_points':str(b),'joint_status':'CERTIFIED' if bound<=b else 'NOT_CERTIFIED',
                 'signed_marginal_status':'CERTIFIED' if mbound<=b else 'NOT_CERTIFIED'} for b in [Q(1,4),Q(1,2),Q(1),Q(2)]],
        'python_version':platform.python_version(),'numpy_version':np.__version__,
        'scope':'Prespecified optional quarter pricing transfer supplement; new reference at previously omitted nodes and a newly recomputed centre. The actual new-quarter fast outputs are unchanged. This is not a calibration or a theorem that old/new CF discs are nested.',
        'cost_scope':'Reused original field and all full-half-year continuous residual work are upstream costs; this measured supplementary wall charges all1025 quarter exponents, new tails, coefficients and complete aggregation. Original all-three pricing transfer results remain separately reported.'}
    assert sha(Path(__file__))==source_sha;save('transfer-supplement-results.json',result)
    print('COMPLETE supplementary quarter full128', float(bound), 'marginal', float(mbound), flush=True)
if __name__=='__main__':main()
