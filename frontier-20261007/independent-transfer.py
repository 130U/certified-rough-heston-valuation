"""Independent complete quarter-maturity readback; never imports transfer-pricing.

--full also recomputes all three exact restricted-field components and actual
fast outputs. Original moment, trig, tail comparison and 100-bit arithmetic
primitives are shared, not independently reimplemented mathematical libraries.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse, copy, hashlib, importlib.util, json, platform, sys, time
import numpy as np
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
helper=HERE/'audit_paths.py'
if not helper.is_file():helper=HERE.parent/'bc-merged-20261007/audit_paths.py'
sp=importlib.util.spec_from_file_location('ind_transfer_paths',helper)
ap=importlib.util.module_from_spec(sp);sp.loader.exec_module(ap)
BASE,OUT=ap.release_root(HERE),ap.evidence_directory(HERE)
SRC,FROZEN=BASE/'code/src',BASE/'code/frozen'
T,NU,H,V,STRIP,DF=Q(1,4),Q(2897,10000),Q(1,8),Q(128),Q(9,20),Q(211093,50)
M=[Q(4400)/DF,Q(4500)/DF]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def module(name,file):
    sp=importlib.util.spec_from_file_location(name,SRC/file)
    obj=importlib.util.module_from_spec(sp);sp.loader.exec_module(obj);return obj
def validate_profile(e,alpha):
    assert e['status']=='EXACT_CONTINUOUS_RESIDUAL_CERTIFICATE'
    assert Q(e['T'])>=T and Q(e['alpha_lower'])==Q(e['alpha_upper'])==alpha
    assert Q(e['nu'])==NU and Q(e['rho'])==Q(-1489,2000) and Q(e['kappa'])==0
    assert Q(e['frequency_step'])==H and e['residual_definition']=='D_C_t_alpha_Hhat_minus_nu_F'
    assert e['proof_evidence'] and [Q(r['u']) for r in e['cover']]==[j*H for j in range(513)]
    assert all(Q(r['delta_physical_upper'])>=0 and Q(r['approx_halfplane_upper'])<=0 for r in e['cover'])
def verify_terminal_account(summary,expected):
    for key,value in expected.items():assert summary[key]==value,(key,'financial account mismatch')
def reject_tests(summary,expected,envelope,ledger):
    tests=[]
    def rejected(name,fn):
        try:fn()
        except (AssertionError,ValueError,KeyError):tests.append({'name':name,'status':'PASS_REJECTED'})
        else:raise AssertionError('damaged input accepted: '+name)
    bad=copy.deepcopy(envelope);bad['T']='1/2'
    rejected('half-year-tail-is-not-new-quarter-tail',lambda: require_quarter(bad))
    dropped=[x['u'] for x in ledger['rows'][:-1]]
    rejected('missing-omitted-finite-node',lambda: require_nodes(dropped))
    badcentre=copy.deepcopy(summary);badcentre['signed_centre_exact']='0'
    rejected('actual-recomputed-centre-replaced-by-zero',lambda: verify_terminal_account(badcentre,expected))
    badtail=copy.deepcopy(summary);badtail['remainder']['true_infinite_tail_upper']='0'
    rejected('actual-infinite-tail-dropped',lambda: verify_terminal_account(badtail,expected))
    badbudget=copy.deepcopy(summary);badbudget['budget_decisions'][0]['joint_status']='CERTIFIED'
    rejected('quarter-budget-failure-replaced-with-success',lambda: verify_terminal_account(badbudget,expected))
    return tests
def require_quarter(x):assert Q(x['T'])==T
def require_nodes(nodes):assert list(map(Q,nodes))==[j*H for j in range(1025)]
def require_equal(a,b):assert a==b

def main():
    sys.stdout.reconfigure(encoding='utf-8');p=argparse.ArgumentParser(description=__doc__);p.add_argument('--full',action='store_true');args=p.parse_args()
    started=time.perf_counter();checks=[];inputs={}
    result=load(OUT/'transfer-results.json');contract=load(OUT/'transfer-contract.json');preflight=load(OUT/'transfer-preflight.json')
    assert result['status']=='COMPLETE_SECOND_MATURITY_PRICING_CERTIFICATE_WITH_REUSED_UPSTREAM_CONTINUOUS_RESIDUAL'
    assert result['T']=='1/4' and result['source_horizon']=='1/2' and result['bits']==100
    assert result['contract_sha256']==preflight['contract_sha256']==sha(OUT/'transfer-contract.json')
    assert contract['maturity_exact']=='1/4' and contract['candidate_alpha_exact']==['13/25','3/5','9/10']
    for name,expected in result['component_sha256'].items():
        assert sha(OUT/name)==expected;inputs[name]=expected
    manifest=load(BASE/'code/MANIFEST.json');trusted={r['path']:r['sha256'] for r in manifest['artifacts']}
    inputs['upstream-MANIFEST.json']=sha(BASE/'code/MANIFEST.json')
    for rec in preflight['records']:
        for name in (rec['field'],rec['residual'],str(Path(rec['field']).with_suffix('.json'))):
            f=FROZEN/name;assert sha(f)==trusted['code/frozen/'+name];inputs[name]=sha(f)
    for name,expected in result['input_sha256'].items():
        if name in ['transfer-contract.json','transfer-preflight.json']:path=OUT/name
        elif name.endswith('.npz') or name.startswith('residual-node-certificate-'):path=FROZEN/name
        elif name=='rough-heston.md':path=BASE/'manuscript'/name
        elif name=='theory-research.md':path=HERE.parent/'heston-nine-point-20261007'/name
        else:path=SRC/name
        assert sha(path)==expected,(name,'identity');inputs[name]=expected
    comp=module('ind_quarter_component','exponent-field-certificate.py');mo,I,S,C=comp.mo,comp.I,comp.S,comp.C;dy=mo.dy
    direct=module('ind_quarter_tail','direct-tail-certificate.py');direct.T=T
    assert direct.S==S and dy.BITS==100
    def iv(bounds):
        a,b=map(Q,bounds);assert a<=b
        return I((a.numerator*S)//a.denominator,-((-b.numerator*S)//b.denominator),True)
    def hi(i):return Q(i.hi,S)
    def absiv(i):return I(0 if i.lo<=0<=i.hi else min(abs(i.lo),abs(i.hi)),max(abs(i.lo),abs(i.hi)),True)
    J0=mo.moments(T,64)[0];logs=[mo.log_endpoint(m) for m in M];pref=[I(m).sqrt()/dy.PI for m in M]
    sd=(Q(1,2)-STRIP)*(dy.exp_positive(2*dy.PI*STRIP/H)-1)
    strip=[I(m).sqrt()*mo.signed_exp(STRIP*absiv(k))/sd for m,k in zip(M,logs)]
    stored_coeff=load(OUT/'transfer-coefficients.json');coefficients=[]
    for j in range(1025):
        u=j*H;cs=[]
        for prefactor,log in zip(pref,logs):
            if j==0:cs.append(C(-2*H*prefactor))
            else:
                ang=-u*log;cs.append(C(comp.trig(ang,True),comp.trig(ang))*(-H*prefactor/(u*u+Q(1,4))))
        record=stored_coeff['rows'][j]
        assert record['u']==str(u)
        for c,stored in zip(cs,record['call_coefficients']):assert c.re.bounds()==stored['re'] and c.im.bounds()==stored['im']
        a=hi((cs[0]-cs[1]).norm2().sqrt());b=hi(cs[0].norm2().sqrt()+cs[1].norm2().sqrt())
        assert str(a)==record['joint_modulus_upper'] and str(b)==record['signed_marginal_modulus_upper']
        coefficients.append((cs,a,b))
    assert stored_coeff['call_strip_remainders']==[i.bounds() for i in strip]
    fast=load(OUT/'transfer-fast-output.json');require_quarter(fast)
    fast_replayed=0
    if args.full:
        pricing=module('ind_quarter_fast','price-profile-diagnostic.py');u,w=pricing.fourier_grid(8)
        for row in fast['rows']:
            ex=pricing.pade_exponent(float(Q(row['alpha'])),u,T=float(T),order=256)
            calls=pricing.prices(np.exp(ex),u,w,[float(m) for m in M])
            assert row['normalized_call_exact_stored_binary64']==[str(Q.from_float(float(v))) for v in calls]
            fast_replayed+=1
    row_results=[];exponents_replayed=0
    for rec,actual,summary in zip(preflight['records'],fast['rows'],result['rows']):
        alpha=Q(rec['alpha']);label=str(alpha).replace('/','_');field=FROZEN/rec['field'];residual=load(FROZEN/rec['residual']);validate_profile(residual,alpha)
        assert residual['field_sha256']==sha(field)==rec['field_sha256']
        ep=load(OUT/('transfer-exponents-alpha-'+label+'.json'));require_quarter(ep)
        assert ep['field_sha256']==sha(field) and ep['contract_sha256']==result['contract_sha256']
        assert ep['component_source_sha256']==sha(SRC/'exponent-field-certificate.py')
        assert ep['nodes']==513 and [Q(r['u']) for r in ep['cover']]==[j*H for j in range(513)]
        with np.load(field) as archive:raw={k:archive[k] for k in archive.files}
        times=[Q.from_float(float(x)) for x in raw['t']];left=rec['terminal_cell_index']
        r=(T-times[left])/(times[left+1]-times[left]);assert times[left]<T<times[left+1]
        assert str(r)==ep['terminal_interpolation_exact_fraction']==rec['terminal_interpolation_fraction']
        trimmed=times[:left+1]+[T];assert ep['time_nodes']==list(map(str,trimmed))
        if args.full:
            weights=mo.linear_field_weights(trimmed,T,64);assert ep['linear_forward_weights']==[w.bounds() for w in weights]
            beta=Q(load(field.with_suffix('.json'))['beta_exact_decimal']);w1=mo.power_field_moment(beta,T,64);w2=mo.power_field_moment(2*beta,T,64)
            assert ep['J0']==J0.bounds() and ep['power_moments']==[w1.bounds(),w2.bounds()]
            for j in range(513):
                u=j*H;a1=complex(raw['A1'][j]);a2=complex(raw['A2'][j]);eq=lambda x:Q.from_float(float(x))
                ex=C(-(u*u+Q(1,4))/2)*J0+C(eq(a1.real),eq(a1.imag))*w1/NU+C(eq(a2.real),eq(a2.imag))*w2/NU
                for k,w in enumerate(weights[:-1]):
                    z=complex(raw['LG'][k,j]);ex+=C(eq(z.real),eq(z.imag))*w/NU
                lz,rz=complex(raw['LG'][left,j]),complex(raw['LG'][left+1,j])
                tr=C(eq(lz.real)+r*(eq(rz.real)-eq(lz.real)),eq(lz.imag)+r*(eq(rz.imag)-eq(lz.imag)))
                ex+=tr*weights[-1]/NU;magnitude=mo.signed_exp(ex.re);phi=C(magnitude*comp.trig(ex.im,True),magnitude*comp.trig(ex.im))
                saved=ep['cover'][j]
                assert saved['exponent_re']==ex.re.bounds() and saved['exponent_im']==ex.im.bounds()
                assert saved['phi_re']==phi.re.bounds() and saved['phi_im']==phi.im.bounds() and saved['phi_modulus']==magnitude.bounds()
                exponents_replayed+=1
            print('full exact exponent replay',alpha,flush=True)
        envelope=load(OUT/('transfer-tail-alpha-'+label+'.json'));require_quarter(envelope)
        assert envelope['alpha']==str(alpha) and envelope['original_source_sha256']==sha(SRC/'direct-tail-certificate.py')
        require_nodes([x['u'] for x in envelope['rows']])
        td=direct.time_data(alpha,64);assert envelope['q_bin_edges']==list(map(str,td[0]))
        assert envelope['q_bin_masses']==[v.bounds() for v in td[2]] and all(v.lo>=0 for v in td[2])
        rate=direct.tail_rate(V,alpha,td);assert rate.lo>0 and rate.bounds()==envelope['tail_rate_interval']
        cl=Q(rate.lo,direct.S);assert str(cl)==envelope['tail_rate_lower']
        tail_integral=mo.signed_exp(I(-cl*V))/(cl*V*V);tails=[p*tail_integral for p in pref]
        assert envelope['call_infinite_tail_remainders']==[v.bounds() for v in tails]
        true_bounds=[]
        for j in range(1025):
            bound,ex=direct.envelope_node(j*H,alpha,td);true_bounds.append(Q(bound.hi,direct.S))
            assert str(true_bounds[-1])==envelope['rows'][j]['true_CF_modulus_upper'] and ex.bounds()==envelope['rows'][j]['comparison_exponent_interval']
        ledger=load(OUT/('transfer-node-ledger-alpha-'+label+'.json'));require_nodes([x['u'] for x in ledger['rows']])
        calls=[I(1),I(1)];joint=Q(0);marginal=Q(0);used=Q(0);omitted=Q(0)
        old_mass=mo.THETA*mo.power(T,1-alpha)/(NU*mo.gamma_cached(2-alpha))
        for j,(cs,a,b) in enumerate(coefficients):
            saved=ledger['rows'][j]
            if j<513:
                ee=ep['cover'][j];mod=iv(ee['phi_modulus']);phi=C(iv(ee['phi_re']),iv(ee['phi_im']));delta=Q(residual['cover'][j]['delta_physical_upper'])/NU
                oldeta=hi(old_mass*(I(delta)/Q(1489,4000)));neweta=hi(I(delta)*J0);eta=min(oldeta,neweta)
                residual_bound=hi(I(min(S,mod.lo),min(S,mod.hi),True)*(dy.exp_positive(I(eta))-1));triangle=hi(I(true_bounds[j])+mod)
                eps=min(residual_bound,triangle)
                assert saved['eta_old_uniform_upper']==str(oldeta) and saved['eta_finite_history_upper']==str(neweta)
                assert saved['eta_used_upper']==str(eta) and saved['residual_radius_upper']==str(residual_bound) and saved['triangle_radius_upper']==str(triangle)
                for k,c in enumerate(cs):calls[k]+=(c*phi).re
            else:eps=true_bounds[j];assert saved['reference_CF']=='exact zero'
            assert saved['CF_radius_upper']==str(eps)
            jcon,mcon=a*eps,b*eps
            assert saved['joint_node_contribution_exact']==str(jcon) and saved['signed_marginal_node_contribution_exact']==str(mcon)
            joint+=jcon;marginal+=mcon
            if j<513:used+=jcon
            else:omitted+=jcon
        mids=[Q(x.lo+x.hi,2*S) for x in calls];arith=sum((Q(x.hi-x.lo,2*S) for x in calls),Q(0))
        act=list(map(Q,actual['normalized_call_exact_stored_binary64']));centre=mids[0]-mids[1]-act[0]+act[1]
        remainder=sum((hi(x) for x in strip+tails),Q(0))+arith;radius=joint+remainder;mradius=marginal+remainder
        bound=DF*(abs(centre)+radius);mbound=DF*(abs(centre)+mradius)
        assert summary['alpha']==str(alpha) and summary['reference_normalized_call_intervals']==[x.bounds() for x in calls]
        for key,value in [('signed_centre_exact',centre),('joint_used_node_support_exact',used),('joint_omitted_node_support_exact',omitted),
                          ('joint_all_node_support_exact',joint),('signed_marginal_all_node_support_exact',marginal),('joint_full_radius_exact',radius),
                          ('signed_marginal_full_radius_exact',mradius),('joint_absolute_bound_index_points_exact',bound),('signed_marginal_absolute_bound_index_points_exact',mbound)]:
            assert Q(summary[key])==value,(alpha,key)
        assert summary['remainder']=={'true_strip_upper':str(sum((hi(x) for x in strip),Q(0))),
             'true_infinite_tail_upper':str(sum((hi(x) for x in tails),Q(0))),'reference_arithmetic_radius':str(arith),'sum_exact':str(remainder)}
        assert summary['joint_true_minus_actual_fast_interval_exact']==[str(centre-radius),str(centre+radius)]
        assert summary['signed_marginal_true_minus_actual_fast_interval_exact']==[str(centre-mradius),str(centre+mradius)]
        expected=[{'budget_index_points':str(b),'joint_status':'CERTIFIED' if bound<=b else 'NOT_CERTIFIED',
             'signed_marginal_status':'CERTIFIED' if mbound<=b else 'NOT_CERTIFIED'} for b in [Q(1,4),Q(1,2),Q(1),Q(2)]]
        assert summary['budget_decisions']==expected
        terminal_expected={'signed_centre_exact':str(centre),'joint_full_radius_exact':str(radius),
             'signed_marginal_full_radius_exact':str(mradius),'remainder':{'true_strip_upper':str(sum((hi(x) for x in strip),Q(0))),
             'true_infinite_tail_upper':str(sum((hi(x) for x in tails),Q(0))),'reference_arithmetic_radius':str(arith),'sum_exact':str(remainder)},
             'joint_absolute_bound_index_points_exact':str(bound),'signed_marginal_absolute_bound_index_points_exact':str(mbound),
             'budget_decisions':expected}
        verify_terminal_account(summary,terminal_expected)
        row_results.append({'alpha':str(alpha),'nodes_checked':1025,'joint_absolute_bound_index_points_exact':str(bound),
                            'signed_marginal_absolute_bound_index_points_exact':str(mbound),'budget_decisions':expected})
    inputs['transfer-results.json']=sha(OUT/'transfer-results.json');inputs['transfer-contract.json']=sha(OUT/'transfer-contract.json')
    receipt={'status':'PASS_INDEPENDENT_COMPLETE_QUARTER_TRANSFER_READBACK','mode':'FULL_SOURCE_COMPONENT_AND_FAST_REPLAY' if args.full else 'IDENTITY_CHECKED_COMPONENT_FINANCIAL_REPLAY',
         'source_sha256':sha(Path(__file__)),'python_version':platform.python_version(),'numpy_version':np.__version__,
         'input_sha256':inputs,'full_exact_field_nodes_replayed':exponents_replayed,'actual_fast_candidates_replayed':fast_replayed,
         'all_true_CF_envelope_nodes_replayed':3075,'all_complete_financial_nodes_replayed':3075,
         'negative_controls':reject_tests(summary,terminal_expected,envelope,ledger),'rows':row_results,'wall_seconds':time.perf_counter()-started,
         'independence':'Does not import transfer-pricing or its aggregation. Shares original rigorous moments, trig, true-tail comparison and dyadic primitives, and reruns the original fast implementation only in --full. Frozen residual validity is inherited from upstream continuous certificates; this reader does not regenerate those certificates.'}
    (OUT/'independent-transfer.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('PASS independent quarter transfer',receipt['mode'],'seconds',receipt['wall_seconds'],flush=True)
if __name__=='__main__':main()
