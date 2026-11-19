"""Generate every point candidate's continuous proof and complete price ledger.

Clock and host information are deliberately never collected. All uncertainty
decisions use exact rational arithmetic and disclosed outward primitives.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse,hashlib,importlib.util,json,sys
import numpy as np
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;SDK=HERE/'sdk'
T=Q(1,2);NU=Q(2897,10000);H=Q(1,8);V=Q(128);F=Q(211093,50);STRIP=Q(9,20)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,obj):p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def module(name,file):
    sp=importlib.util.spec_from_file_location(name,SDK/file);m=importlib.util.module_from_spec(sp);sys.modules[name]=m;sp.loader.exec_module(m);return m
def exact(x):return Q.from_float(float(x))
def freeze_field(alpha,n,U,path):
    field=module('nearby_field','field-residual-diagnostic.py');u=np.arange(U*8+1)/8
    x,y,hh,ff,ll,co=field.solve(float(alpha),u,n,.5,True)
    c,d,b1,b2,b3,a1,a2=co;t=x/field.NU**(1/float(alpha));t[0]=0.;t[-1]=.5
    A1=field.NU**2*a1;A2=field.NU**3*a2;LG=field.NU*ll
    assert np.all(np.diff(t)>0) and np.all(LG[0]==0)
    np.savez_compressed(path,t=t,u=u,A1=A1,A2=A2,LG=LG)
    save(path.with_suffix('.json'),{'status':'EXACT_STORED_DYADIC_FIELD',
       'beta_exact_decimal':str(alpha),'T':'1/2','sha256':sha(path),
       'n':n,'frequency_upper':U,'definition':'Gbar=nu*c+A1*t^alpha+A2*t^(2alpha)+LGlin; Hhat=I^alpha Gbar'})
    return {'t':t,'u':u,'A1':A1,'A2':A2,'LG':LG}

def generate(alpha,n,pilot=False):
    label=str(alpha).replace('/','_');folder=HERE/('pilot' if pilot else 'N'+str(n));folder.mkdir(exist_ok=True)
    p=folder/('field-'+label+'.npz');U=2 if pilot else 64
    if p.exists():
        data={k:a for k,a in np.load(p).items()};assert sha(p)==load(p.with_suffix('.json'))['sha256']
    else:data=freeze_field(alpha,n,U,p)
    res=module('nearby_res','certify-field-residual.py')
    rp=folder/('residual-'+label+'.json')
    if rp.exists():raw=load(rp);assert raw['field_sha256']==sha(p) and raw['source_sha256']==sha(SDK/'certify-field-residual.py')
    else:raw=res.certify(p,alpha,U,2,32);save(rp,raw)
    assert raw['approx_left_halfplane_certified'], 'approximate field must have complete half-plane evidence'
    assert raw['certified_closed_subintervals']==1+2*(n-1)
    bank=p.with_name(p.stem+'-residual-cells.npz');assert sha(bank)==raw['bank_sha256']
    if pilot:
        save(folder/'pilot-result.json',{'status':'PASS_PATH_AND_FULL_COVER_ONLY_NOT_SCIENTIFIC_RESULT',
             'alpha':str(alpha),'n':n,'frequency_nodes':U*8+1,'closed_cells':1+2*(n-1),
             'field_sha256':sha(p),'residual_sha256':sha(rp),'bank_sha256':sha(bank)})
        print('PASS pilot cover and arithmetic path',flush=True);return
    comp=module('nearby_comp','exponent-field-certificate.py');mo,dy,I,S,C=comp.mo,comp.mo.dy,comp.I,comp.S,comp.C
    direct=module('nearby_direct','direct-tail-certificate.py');direct.T=T
    fast=module('nearby_fast','price-profile-diagnostic.py')
    def interval(b):
        lo,hi=map(Q,b);assert lo<=hi;return I((lo.numerator*S)//lo.denominator,-((-hi.numerator*S)//hi.denominator),True)
    def upper(x):return Q(x.hi,S)
    def abs_i(x):return I(0 if x.lo<=0<=x.hi else min(abs(x.lo),abs(x.hi)),max(abs(x.lo),abs(x.hi)),True)
    def norm(z):return z.norm2().sqrt()
    quotes=[r for r in load(SDK/'normalized-quote-bands.json')['rows'] if Q(r['T_decimal_input'])==T]
    assert [r['row_id'] for r in quotes]==list(range(1,13))
    M=list(map(lambda r:Q(r['moneyness_fraction']),quotes));pref=[I(m).sqrt()/dy.PI for m in M];logs=[mo.log_endpoint(m) for m in M]
    den=(Q(1,2)-STRIP)*(dy.exp_positive(2*dy.PI*STRIP/H)-1)
    strips=[upper(I(m).sqrt()*mo.signed_exp(STRIP*abs_i(k))/den) for m,k in zip(M,logs)]
    uf,wf=fast.fourier_grid(8);fe=fast.pade_exponent(float(alpha),uf,.5,256)
    returned=list(map(exact,fast.prices(np.exp(fe),uf,wf,list(map(float,M)))))
    times=list(map(exact,data['t']));weights=mo.linear_field_weights(times,T,64)
    j0=mo.moments(T,64)[0];w1=mo.power_field_moment(alpha,T,64);w2=mo.power_field_moment(2*alpha,T,64)
    ep=folder/('exponents-'+label+'.json')
    if ep.exists():
        exponents=load(ep)['rows'];assert load(ep)['field_sha256']==sha(p)
    else:
        exponents=[]
        for j in range(513):
            u=j*H;a1,a2=data['A1'][j],data['A2'][j]
            ex=C(-(u*u+Q(1,4))/2)*j0+C(exact(a1.real),exact(a1.imag))*w1/NU+C(exact(a2.real),exact(a2.imag))*w2/NU
            for k,w in enumerate(weights):
                z=data['LG'][k,j];ex+=C(exact(z.real),exact(z.imag))*w/NU
            mag=mo.signed_exp(ex.re);phi=C(mag*comp.trig(ex.im,True),mag*comp.trig(ex.im))
            exponents.append({'u':str(u),'exponent_re':ex.re.bounds(),'exponent_im':ex.im.bounds(),
                'phi_re':phi.re.bounds(),'phi_im':phi.im.bounds(),'phi_modulus':mag.bounds()})
        save(ep,{'status':'STRICT_REFERENCE_COMPONENT_NOT_TRUE_CF_CERTIFICATE','alpha':str(alpha),
           'field_sha256':sha(p),'bits':100,'weights':[w.bounds() for w in weights],
           'J0':j0.bounds(),'power_moments':[w1.bounds(),w2.bounds()],'rows':exponents})
    td=direct.time_data(alpha,64);tr=direct.tail_rate(V,alpha,td);cl=Q(tr.lo,S);assert cl>0
    tails=[upper(z*mo.signed_exp(I(-cl*V))/(cl*V*V)) for z in pref]
    refs=[I(1) for _ in M];radii=[Q(0) for _ in M];nodes=[];coeffs=[]
    deltas=list(map(Q,raw['delta_physical_upper_exact_dyadics']))
    for j in range(1025):
        u=j*H;true_mod,tex=direct.envelope_node(u,alpha,td);bound=upper(true_mod)
        if j<=512:
            er=exponents[j];phi=C(interval(er['phi_re']),interval(er['phi_im']));mag=interval(er['phi_modulus'])
            eta=upper(I(deltas[j]/NU)*j0);cap=I(min(S,mag.lo),min(S,mag.hi),True)
            eps=min(upper(cap*(dy.exp_positive(I(eta))-1)),upper(I(bound)+mag))
        else:phi=C(0);eta=Q(0);eps=bound
        cs=[]
        for i in range(12):
            if j==0:c=C(-2*H*pref[i])
            else:
                phase=-u*logs[i];c=C(comp.trig(phase,True),comp.trig(phase))*(-H*pref[i]/(u*u+Q(1,4)))
            refs[i]+=(c*phi).re;radii[i]+=eps*upper(norm(c));cs.append(c)
        coeffs.append(cs)
        nodes.append({'u':str(u),'true_CF_modulus_upper':str(bound),'comparison_exponent':tex.bounds(),
            'eta_upper':str(eta),'epsilon_upper':str(eps),
            'coefficients':[{'re':c.re.bounds(),'im':c.im.bounds()} for c in cs]})
    centres=[Q(z.lo+z.hi,2*S) for z in refs]
    arithmetic=[Q(z.hi-z.lo,2*S) for z in refs]
    remainders=[strips[i]+tails[i]+arithmetic[i] for i in range(12)]
    full=[radii[i]+remainders[i] for i in range(12)]
    targets=[(Q(r['price_mid_target']['lower_fraction']),Q(r['price_mid_target']['upper_fraction'])) for r in quotes]
    mt=[(a+b)/2 for a,b in targets];mq=[(b-a)/2 for a,b in targets];z=[centres[i]-mt[i] for i in range(12)]
    a=[v/12 for v in z];jc=sum((v*v for v in z),Q(0))/24
    rr=[full[i]+mq[i] for i in range(12)]
    hm=sum((abs(a[i])*rr[i] for i in range(12)),Q(0));hj=sum((abs(a[i])*(remainders[i]+mq[i]) for i in range(12)),Q(0))
    for j,cs in enumerate(coeffs):
        v=C(0)
        for i in range(12):v+=cs[i]*a[i]
        hj+=Q(nodes[j]['epsilon_upper'])*upper(norm(v))
    quadratic=sum((v*v for v in rr),Q(0))/24
    boxlower=Q(0);boxupper=Q(0)
    for v,r in zip(z,rr):
        lo,hi=v-r,v+r;boxlower+=0 if lo<=0<=hi else min(lo*lo,hi*hi);boxupper+=max(lo*lo,hi*hi)
    boxlower/=24;boxupper/=24
    jm=(max(boxlower,jc-hm,Q(0)),min(boxupper,jc+hm+quadratic))
    jj=(max(jm[0],jc-hj,Q(0)),min(jm[1],jc+hj+quadratic))
    incompat=[];inside=True;price_rows=[]
    for i,r in enumerate(quotes):
        lo,hi=max(Q(0),centres[i]-full[i]),min(Q(1),centres[i]+full[i])
        bid=Q(r['normalized_bid']['lower_fraction']);ask=Q(r['normalized_ask']['upper_fraction'])
        if hi<bid or lo>ask:incompat.append(r['row_id'])
        if lo<Q(r['normalized_bid']['upper_fraction']) or hi>Q(r['normalized_ask']['lower_fraction']):inside=False
        correction=centres[i]-returned[i]
        reference_actual=exact(float(centres[i]));correction_actual=exact(float(correction))
        corrected_actual=exact(float(returned[i])+float(correction_actual))
        price_rows.append({'row_id':r['row_id'],'K':r['K_decimal_input'],'actual_fast_output':str(returned[i]),
            'strict_reference_centre':str(centres[i]),'centre_correction':str(correction),
            'fast_plus_signed_correction':str(returned[i]+correction),
            'actual_reference_output_binary64':str(reference_actual),
            'actual_signed_correction_binary64':str(correction_actual),
            'actual_corrected_fast_output_binary64':str(corrected_actual),
            'reference_output_rounding_exact':str(reference_actual-centres[i]),
            'correction_storage_rounding_exact':str(correction_actual-correction),
            'correction_addition_rounding_exact':str(corrected_actual-returned[i]-correction_actual),
            'actual_reference_complete_bound':str(abs(reference_actual-centres[i])+full[i]),
            'actual_corrected_fast_complete_bound':str(abs(corrected_actual-centres[i])+full[i]),
            'complete_reference_radius':str(full[i]),'frozen_fast_absolute_error_upper':str(abs(correction)+full[i]),
            'true_price_interval':[str(lo),str(hi)],'strip_remainder':str(strips[i]),
            'true_infinite_tail_remainder':str(tails[i]),'reference_arithmetic_remainder':str(arithmetic[i])})
    # Same full certificate and same tolerance; only the actual output centre changes.
    w=[Q(0)]*12;w[7]=1;w[8]=-1
    js=Q(0);ms=Q(0)
    for j,cs in enumerate(coeffs):
        delta=cs[7]-cs[8];eps=Q(nodes[j]['epsilon_upper'])
        js+=eps*upper(norm(delta));ms+=eps*upper(norm(cs[7])+norm(cs[8]))
    rem=remainders[7]+remainders[8];sc=(centres[7]-centres[8])-(returned[7]-returned[8])
    ra=[Q(r['actual_reference_output_binary64']) for r in price_rows]
    ca=[Q(r['actual_corrected_fast_output_binary64']) for r in price_rows]
    reference_shift=abs((ra[7]-ra[8])-(centres[7]-centres[8]))
    corrected_shift=abs((ca[7]-ca[8])-(centres[7]-centres[8]))
    correction_control={'spread_strikes':['4400','4500'],'index_point_budget':'1/4',
       'actual_frozen_fast_spread':str(returned[7]-returned[8]),'direct_reference_spread':str(centres[7]-centres[8]),
       'fast_plus_correction_spread':str(returned[7]-returned[8]+sc),
       'signed_correction_points':str(sc*F),
       'uncorrected_fast_joint_complete_bound_points':str((abs(sc)+js+rem)*F),
       'uncorrected_fast_marginal_complete_bound_points':str((abs(sc)+ms+rem)*F),
       'direct_reference_and_corrected_joint_bound_points':str((js+rem)*F),
       'direct_reference_and_corrected_marginal_bound_points':str((ms+rem)*F),
       'actual_binary64_reference_spread':str(ra[7]-ra[8]),
       'actual_binary64_corrected_fast_spread':str(ca[7]-ca[8]),
       'actual_binary64_reference_joint_bound_points':str((reference_shift+js+rem)*F),
       'actual_binary64_corrected_fast_joint_bound_points':str((corrected_shift+js+rem)*F),
       'actual_binary64_reference_marginal_bound_points':str((reference_shift+ms+rem)*F),
       'actual_binary64_corrected_fast_marginal_bound_points':str((corrected_shift+ms+rem)*F),
       'qualification':'Ideal rational reference and exact corrected prices are algebraically equal. Actual binary64 reference/correction/addition are separately stored and their exact translation from the ideal centre is fully charged.'}
    out={'status':'COMPLETE_POINT_CANDIDATE_AND_REAL_QUOTE_OBJECTIVE_CERTIFICATE',
       'alpha':str(alpha),'N':n,'T':'1/2','contract_sha256':sha(HERE/'nearby-contract-execution.json'),
       'field_sha256':sha(p),'residual_sha256':sha(rp),'bank_sha256':sha(bank),
       'exponents_sha256':sha(ep),'quotes_sha256':sha(SDK/'normalized-quote-bands.json'),
       'tail_rate_lower':str(cl),'time_q_bin_edges':list(map(str,td[0])),'time_q_bin_masses':[v.bounds() for v in td[2]],
       'price_rows':price_rows,'node_ledger':nodes,
       'objective':{'reference_J':str(jc),'joint_linear_support':str(hj),'marginal_linear_support':str(hm),
          'quadratic_remainder':str(quadratic),'joint_interval':list(map(str,jj)),'marginal_interval':list(map(str,jm))},
       'bid_ask_incompatible_rows':incompat,'inside_all_quote_bands':inside,
       'correction_control':correction_control,
       'workload':{'actual_fast_fourier_nodes':len(uf),'fast_Jacobi_nodes_per_frequency':256,
         'reference_frequency_nodes':513,'full_finite_grid_nodes':1025,'reference_time_nodes':n+1,
         'continuous_closed_cells':1+2*(n-1),'continuous_residual_node_cell_entries':513*(1+2*(n-1)),
         'strict_reference_exponents':513,'strict_true_CF_node_envelopes':1025,
         'full_price_coefficient_assemblies':12*1025,'joint_objective_disk_support_terms':1025,
         'spread_joint_disk_support_terms':1025,'inherited_candidate_residuals_reused':0,
         'true_infinite_tail_comparisons':1,'forward_curve_moment_series_terms':64,
         'one_task_amortization':'same candidate certificate supports all 12 prices and 28 fixed portfolio aggregations without extra residual generation'}}
    save(folder/('candidate-'+label+'.json'),out)
    print('PASS complete candidate',alpha,'N',n,'objective joint',list(map(float,jj)),'incompatible rows',incompat,flush=True)

def aggregate(n):
    folder=HERE/('N'+str(n));contract=load(HERE/'nearby-contract-execution.json');grid=contract['candidate_alpha_exact']
    rows=[load(folder/('candidate-'+a.replace('/','_')+'.json')) for a in grid]
    for r in rows:assert r['status']=='COMPLETE_POINT_CANDIDATE_AND_REAL_QUOTE_OBJECTIVE_CERTIFICATE'
    pairs=[]
    for i in range(5):
        for j in range(i+1,5):
            line={'alpha_a':grid[i],'alpha_b':grid[j],'adjacent':j==i+1}
            for mode in ['joint','marginal']:
                al,au=map(Q,rows[i]['objective'][mode+'_interval']);bl,bu=map(Q,rows[j]['objective'][mode+'_interval'])
                line[mode]={'a_minus_b_interval':[str(al-bu),str(au-bl)],
                   'decision':'A_STRICTLY_SMALLER' if au<bl else 'B_STRICTLY_SMALLER' if bu<al else 'UNRESOLVED'}
            pairs.append(line)
    upgrade=any(r['adjacent'] and r['joint']['decision']=='UNRESOLVED' for r in pairs)
    save(folder/'nearby-results.json',{'status':'COMPLETE_FINITE_NEARBY_GRID_ONLY_NOT_MARKET_IDENTIFICATION',
       'N':n,'grid':grid,'pairs':pairs,'prespecified_second_layer_required':n==1024 and upgrade,
       'candidate_objectives':[{'alpha':r['alpha'],'objective':r['objective'],'incompatible_rows':r['bid_ask_incompatible_rows'],
            'correction_control':r['correction_control'],'workload':r['workload']} for r in rows],
       'candidate_sha256':{a:sha(folder/('candidate-'+a.replace('/','_')+'.json')) for a in grid},
       'conclusion_boundary':'Separation is among five declared point candidates for the original 12-row experiment only. No continuous optimizer, calibrated market model, or cross-alpha error dependence is asserted.'})
    print('PASS all ten pair decisions','second layer required',n==1024 and upgrade,flush=True)

def main():
    sys.stdout.reconfigure(encoding='utf-8');p=argparse.ArgumentParser();p.add_argument('--pilot',action='store_true');p.add_argument('--N',type=int,default=1024);p.add_argument('--alpha');p.add_argument('--aggregate-only',action='store_true');a=p.parse_args()
    if a.pilot:generate(Q(13,25),64,True);return
    assert a.N in [1024,2048]
    if not a.aggregate_only:
        grid=[a.alpha] if a.alpha else load(HERE/'nearby-contract-execution.json')['candidate_alpha_exact']
        for alpha in grid:generate(Q(alpha),a.N)
    if not a.alpha:aggregate(a.N)
if __name__=='__main__':main()
