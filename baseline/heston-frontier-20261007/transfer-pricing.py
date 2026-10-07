"""Complete second-maturity pricing transfer, with exact stored-output target.

The continuous full-history field is restricted, never restarted. Shared
upstream rigorous arithmetic is identified; the original half-year tail
numbers are not used. This is pricing transfer, not market calibration.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse, hashlib, importlib.util, json, platform, sys, time
import numpy as np

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent

def paths():
    helper = HERE / 'audit_paths.py'
    if not helper.is_file(): helper = HERE.parent / 'bc-merged-20261007/audit_paths.py'
    sp = importlib.util.spec_from_file_location('transfer_paths', helper)
    p = importlib.util.module_from_spec(sp); sp.loader.exec_module(p)
    return p.release_root(HERE), p.evidence_directory(HERE)

BASE, OUT = paths()
SRC, FROZEN = BASE/'code/src', BASE/'code/frozen'
T, NU, H, V, STRIP = Q(1,4), Q(2897,10000), Q(1,8), Q(128), Q(9,20)
SCALE = Q(211093,50)
M = [Q(4400)/SCALE, Q(4500)/SCALE]

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def save(name, obj):
    target=OUT/name
    target.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    return target
def module(name, file):
    sp=importlib.util.spec_from_file_location(name,SRC/file)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def exact(x): return Q.from_float(float(x))

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reuse-components',action='store_true',help='Reuse identity-checked new-quarter exponent components only')
    args=parser.parse_args()
    started=0; costs={}; script_hash=sha(Path(__file__))
    contract=load(OUT/'transfer-contract.json'); preflight=load(OUT/'transfer-preflight.json')
    contract_hash=sha(OUT/'transfer-contract.json')
    assert preflight['contract_sha256']==contract_hash
    assert preflight['status']=='PASS_TRANSFER_PREFLIGHT_BEFORE_NEW_VALUES'
    input_hashes={'transfer-contract.json':contract_hash,'transfer-preflight.json':sha(OUT/'transfer-preflight.json')}
    for oldpath, expected in preflight['source_sha256'].items():
        name=Path(oldpath).name
        if name=='rough-heston.md': path=BASE/'manuscript'/name
        elif name=='theory-research.md': path=HERE.parent/'heston-nine-point-20261007'/name
        else:path=SRC/name
        assert sha(path)==expected,(name,'source drift');input_hashes[name]=expected
    start=0
    comp=module('transfer_field','exponent-field-certificate.py')
    mo,dy,I,S,C=comp.mo,comp.mo.dy,comp.I,comp.S,comp.C
    direct=module('transfer_tail','direct-tail-certificate.py');direct.T=T
    fast=module('transfer_fast','price-profile-diagnostic.py')
    pass
    assert dy.BITS==100 and direct.T==T
    def interval(bounds):
        lo,hi=map(Q,bounds);assert lo<=hi
        return I((lo.numerator*S)//lo.denominator,-((-hi.numerator*S)//hi.denominator),True)
    def upper(x): return Q(x.hi,S)
    def lower(x): return Q(x.lo,S)
    def abs_i(x):return I(0 if x.lo<=0<=x.hi else min(abs(x.lo),abs(x.hi)),max(abs(x.lo),abs(x.hi)),True)
    def norm(c):return c.norm2().sqrt()
    start=0;fast_rows=[]
    uf,wf=fast.fourier_grid(8)
    for rec in preflight['records']:
        alpha=Q(rec['alpha']); one=0
        exponent=fast.pade_exponent(float(alpha),uf,T=float(T),order=256)
        outputs=fast.prices(np.exp(exponent),uf,wf,[float(v) for v in M])
        assert np.all(np.isfinite(outputs))
        fast_rows.append({'alpha':str(alpha),'T':str(T),'normalized_call_exact_stored_binary64':[str(exact(p)) for p in outputs],
                          'normalized_spread_exact':str(exact(outputs[0])-exact(outputs[1]))})
        print('frozen actual fast output',alpha,flush=True)
    fp=save('transfer-fast-output.json',{'status':'ACTUAL_SECOND_MATURITY_PADÉ_OUTPUT_FROZEN_AS_EXACT_DYADICS',
         'T':str(T),'contract_sha256':contract_hash,'source_sha256':sha(SRC/'price-profile-diagnostic.py'),
         'fourier_legendre_order':8,'time_jacobi_order':256,'fourier_quadrature_nodes':len(uf),'rows':fast_rows,
         'scope':'Finite returned binary64 outputs are exact pricing targets. No claim that these outputs are certified by their internal quadrature.'})
    pass
    # Coefficients and strip contribution are computed once at the new contract.
    start=0; coefficient_rows=[]; pref=[I(m).sqrt()/dy.PI for m in M]; logs=[mo.log_endpoint(m) for m in M]
    grid_den=(Q(1,2)-STRIP)*(dy.exp_positive(2*dy.PI*STRIP/H)-1)
    grid=[I(m).sqrt()*mo.signed_exp(STRIP*abs_i(k))/grid_den for m,k in zip(M,logs)]
    for n in range(1025):
        u=n*H;coeff=[]
        for p,k in zip(pref,logs):
            if n==0:coeff.append(C(-2*H*p))
            else:
                phase=-u*k
                coeff.append(C(comp.trig(phase,True),comp.trig(phase))*(-H*p/(u*u+Q(1,4))))
        coefficient_rows.append({'u':str(u),'call_coefficients':[{'re':c.re.bounds(),'im':c.im.bounds()} for c in coeff],
             'joint_modulus_upper':str(upper(norm(coeff[0]-coeff[1]))),
             'signed_marginal_modulus_upper':str(upper(norm(coeff[0])+norm(coeff[1])))})
    cp=save('transfer-coefficients.json',{'T':str(T),'h':str(H),'moneynesses':list(map(str,M)),
         'strip_halfwidth':str(STRIP),'call_strip_remainders':[x.bounds() for x in grid],'rows':coefficient_rows})
    pass
    results=[];component_paths=[fp,cp]
    J0=mo.moments(T,64)[0]
    for rec, actual in zip(preflight['records'],fast_rows):
        alpha=Q(rec['alpha']);label=str(alpha).replace('/','_');field=FROZEN/rec['field']; residual_path=FROZEN/rec['residual']
        assert sha(field)==rec['field_sha256'];input_hashes[field.name]=sha(field);input_hashes[residual_path.name]=sha(residual_path)
        residual=load(residual_path);assert residual['field_sha256']==sha(field)
        assert residual['status']=='EXACT_CONTINUOUS_RESIDUAL_CERTIFICATE' and Q(residual['T'])==Q(1,2)
        assert Q(residual['alpha_lower'])==Q(residual['alpha_upper'])==alpha
        residual_rows=residual['cover'];assert [Q(x['u']) for x in residual_rows]==[n*H for n in range(513)]
        assert all(Q(x['approx_halfplane_upper'])<=0 for x in residual_rows)
        start=0; td=direct.time_data(alpha,64);rate=direct.tail_rate(V,alpha,td)
        assert rate.lo>0
        tailrows=[]
        for n in range(1025):
            b,ex=direct.envelope_node(n*H,alpha,td)
            tailrows.append({'u':str(n*H),'true_CF_modulus_upper':str(Q(b.hi,direct.S)),
                             'comparison_exponent_interval':ex.bounds()})
        c=Q(rate.lo,direct.S);tailintegral=mo.signed_exp(I(-c*V))/(c*V*V)
        tails=[p*tailintegral for p in pref]
        tp=save('transfer-tail-alpha-'+label+'.json',{'status':'NEW_QUARTER_TRUE_CF_AND_INFINITE_TAIL',
             'alpha':str(alpha),'T':str(T),'V':str(V),'terms':64,'bits':100,
             'original_source_sha256':sha(SRC/'direct-tail-certificate.py'),'contract_sha256':contract_hash,
             'q_bin_edges':list(map(str,td[0])),'q_bin_masses':[x.bounds() for x in td[2]],
             'tail_rate_interval':rate.bounds(),'tail_rate_lower':str(c),'call_infinite_tail_remainders':[x.bounds() for x in tails],
             'rows':tailrows,'startup_term':'V0*g_(1-alpha) included by cumulative_q; no omission of fractional startup mass'})
        costs['new_tail_alpha_'+label+'_seconds']=0-start;component_paths.append(tp)
        start=0;ep=OUT/('transfer-exponents-alpha-'+label+'.json')
        if args.reuse_components and ep.is_file():
            stored=load(ep);assert stored['contract_sha256']==contract_hash and stored['field_sha256']==sha(field)
            assert stored['T']=='1/4' and stored['component_source_sha256']==sha(SRC/'exponent-field-certificate.py')
            exponent_rows=stored['cover']
        else:
            with np.load(field) as ar:data={k:ar[k] for k in ar.files}
            fulltimes=[exact(x) for x in data['t']];left=rec['terminal_cell_index']
            assert fulltimes[left]<T<fulltimes[left+1]
            ratio=(T-fulltimes[left])/(fulltimes[left+1]-fulltimes[left])
            assert str(ratio)==rec['terminal_interpolation_fraction']
            times=fulltimes[:left+1]+[T];weights=mo.linear_field_weights(times,T,64)
            assert len(weights)==rec['retained_time_nodes_with_new_terminal']
            beta=Q(load(field.with_suffix('.json'))['beta_exact_decimal'])
            w1,w2=mo.power_field_moment(beta,T,64),mo.power_field_moment(2*beta,T,64)
            exponent_rows=[]
            for n in range(513):
                u=n*H;a1=complex(data['A1'][n]);a2=complex(data['A2'][n])
                ex=C(-(u*u+Q(1,4))/2)*J0+C(exact(a1.real),exact(a1.imag))*w1/NU+C(exact(a2.real),exact(a2.imag))*w2/NU
                for k,w in enumerate(weights[:-1]):
                    z=complex(data['LG'][k,n]);ex+=C(exact(z.real),exact(z.imag))*w/NU
                zl,zr=complex(data['LG'][left,n]),complex(data['LG'][left+1,n])
                terminal=C(exact(zl.real)+ratio*(exact(zr.real)-exact(zl.real)),exact(zl.imag)+ratio*(exact(zr.imag)-exact(zl.imag)))
                ex+=terminal*weights[-1]/NU
                magnitude=mo.signed_exp(ex.re);phi=C(magnitude*comp.trig(ex.im,True),magnitude*comp.trig(ex.im))
                exponent_rows.append({'u':str(u),'exponent_re':ex.re.bounds(),'exponent_im':ex.im.bounds(),
                        'phi_re':phi.re.bounds(),'phi_im':phi.im.bounds(),'phi_modulus':magnitude.bounds()})
                if n and n%128==0:print('quarter exact reference',alpha,n,'seconds',round(0-start,2),flush=True)
            save(ep.name,{'status':'EXACT_STORED_QUARTER_FIELD_COMPONENT_NOT_TRUE_CF_CERTIFICATE',
                'alpha':str(alpha),'beta':str(beta),'T':str(T),'nu':str(NU),'bits':100,'nodes':513,
                'field':field.name,'field_sha256':sha(field),'contract_sha256':contract_hash,
                'component_source_sha256':sha(SRC/'exponent-field-certificate.py'),
                'terminal_interpolation_exact_fraction':str(ratio),'terminal_original_cell':list(map(str,fulltimes[left:left+2])),
                'time_nodes':list(map(str,times)),'linear_forward_weights':[w.bounds() for w in weights],
                'J0':J0.bounds(),'power_moments':[w1.bounds(),w2.bounds()],
                'scope':'Exact physical-time restriction of unchanged full-history field. No Caputo restart at the new terminal point.',
                'cover':exponent_rows})
        costs['new_reference_alpha_'+label+'_seconds']=0-start;component_paths.append(ep)
        assert [Q(r['u']) for r in exponent_rows]==[n*H for n in range(513)]
        start=0;node_ledger=[];reference=[I(1),I(1)];joint=Q(0);marginal=Q(0);used=Q(0);omitted=Q(0)
        mass_bound=mo.THETA*mo.power(T,1-alpha)/(NU*mo.gamma_cached(2-alpha))
        for n in range(1025):
            coeff=coefficient_rows[n]
            if n<=512:
                er=exponent_rows[n];rr=residual_rows[n]
                phi=C(interval(er['phi_re']),interval(er['phi_im']));mod=interval(er['phi_modulus'])
                delta=Q(rr['delta_physical_upper'])/NU
                old_eta=upper(mass_bound*(I(delta)/Q(1489,4000)));history_eta=upper(I(delta)*J0);eta=min(old_eta,history_eta)
                minmod=I(min(S,mod.lo),min(S,mod.hi),True)
                from_residual=upper(minmod*(dy.exp_positive(I(eta))-1))
                triangle=upper(I(Q(tailrows[n]['true_CF_modulus_upper']))+mod)
                epsilon=min(from_residual,triangle)
                for k in range(2):
                    cc=coeff['call_coefficients'][k]
                    reference[k]+=(C(interval(cc['re']),interval(cc['im']))*phi).re
                extra={'delta_physical_upper':rr['delta_physical_upper'],'delta_F_upper':str(delta),
                    'eta_old_uniform_upper':str(old_eta),'eta_finite_history_upper':str(history_eta),'eta_used_upper':str(eta),
                    'residual_radius_upper':str(from_residual),'triangle_radius_upper':str(triangle)}
            else:
                epsilon=Q(tailrows[n]['true_CF_modulus_upper']);extra={'reference_CF':'exact zero','radius_source':'new-quarter true CF envelope'}
            j=epsilon*Q(coeff['joint_modulus_upper']);m=epsilon*Q(coeff['signed_marginal_modulus_upper'])
            joint+=j;marginal+=m
            if n<=512:used+=j
            else:omitted+=j
            node_ledger.append({'u':str(n*H),'CF_radius_upper':str(epsilon),'joint_node_contribution_exact':str(j),
                                'signed_marginal_node_contribution_exact':str(m),**extra})
        reference_mid=[Q(x.lo+x.hi,2*S) for x in reference]
        arithmetic=sum((Q(x.hi-x.lo,2*S) for x in reference),Q(0))
        actualcalls=list(map(Q,actual['normalized_call_exact_stored_binary64']))
        centre=(reference_mid[0]-reference_mid[1])-(actualcalls[0]-actualcalls[1])
        strip=sum(map(upper,grid),Q(0));tail=sum(map(upper,tails),Q(0));remainder=strip+tail+arithmetic
        radius=joint+remainder;mradius=marginal+remainder;bound=(abs(centre)+radius)*SCALE;mbound=(abs(centre)+mradius)*SCALE
        lp=save('transfer-node-ledger-alpha-'+label+'.json',{'alpha':str(alpha),'T':str(T),'rows':node_ledger});component_paths.append(lp)
        result={'alpha':str(alpha),'T':str(T),'reference_used_cutoff':'64','finite_true_grid_cutoff':'128',
            'actual_fast_normalized_calls':list(map(str,actualcalls)),'reference_normalized_call_intervals':[x.bounds() for x in reference],
            'reference_normalized_call_midpoints':list(map(str,reference_mid)),'signed_centre_exact':str(centre),
            'remainder':{'true_strip_upper':str(strip),'true_infinite_tail_upper':str(tail),'reference_arithmetic_radius':str(arithmetic),'sum_exact':str(remainder)},
            'joint_used_node_support_exact':str(used),'joint_omitted_node_support_exact':str(omitted),'joint_all_node_support_exact':str(joint),
            'signed_marginal_all_node_support_exact':str(marginal),'joint_full_radius_exact':str(radius),'signed_marginal_full_radius_exact':str(mradius),
            'joint_true_minus_actual_fast_interval_exact':[str(centre-radius),str(centre+radius)],
            'signed_marginal_true_minus_actual_fast_interval_exact':[str(centre-mradius),str(centre+mradius)],
            'joint_absolute_bound_index_points_exact':str(bound),'signed_marginal_absolute_bound_index_points_exact':str(mbound),
            'display_joint_absolute_bound_index_points_upper_9dp':str(Q(-((-bound.numerator*10**9)//bound.denominator),10**9)),
            'budget_decisions':[{'budget_index_points':str(b),'joint_status':'CERTIFIED' if bound<=b else 'NOT_CERTIFIED',
                                 'signed_marginal_status':'CERTIFIED' if mbound<=b else 'NOT_CERTIFIED'} for b in [Q(1,4),Q(1,2),Q(1),Q(2)]]}
        results.append(result);costs['full_aggregate_alpha_'+label+'_seconds']=0-start
        print('COMPLETE T=1/4',alpha,'joint points upper',float(bound),'marginal',float(mbound),flush=True)
    assert sha(Path(__file__))==script_hash
    output={'status':'COMPLETE_SECOND_MATURITY_PRICING_CERTIFICATE_WITH_REUSED_UPSTREAM_CONTINUOUS_RESIDUAL',
        'T':str(T),'source_horizon':'1/2','contract_sha256':contract_hash,'script_sha256':script_hash,
        'python_version':platform.python_version(),'numpy_version':np.__version__,'bits':100,
        'scope':'Pricing transfer only. Frozen three candidates, original physical curve and normalized 4400-4500 spread. No market observations or calibration inference.',
        'proof_scope':'Original admissible model and martingale/affine law hold at every finite T. Full-history residual/halfplane restriction is valid. New T-dependent reference integral, true envelope, omitted frequencies and infinite tail are all recomputed.',
        'input_sha256':input_hashes,'component_sha256':{p.name:sha(p) for p in component_paths},'rows':results,
        
        'cost_scope':'New pricing transfer costs only. The reused half-year field construction and continuous residual generation are sunk upstream work, not claimed free and not included in this replay wall time. New tail and all three actual fast outputs are charged. --reuse-components explicitly identifies component reuse.'}
    path=save('transfer-results.json',output)
    print('PASS COMPLETE TRANSFER', path.name, flush=True)

if __name__=='__main__':main()
