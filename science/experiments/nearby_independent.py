"""Separate reconstruction of complete nearby-grid certificates.

Does not import or call the primary candidate generator. Shared rigorous
gamma/moment/trig/interval primitives are explicitly disclosed. This reader
checks every closed-cell envelope and recomputes every stored-field exponent,
true-CF node bound, coefficient, radius, objective support and pair decision.
It does not claim a separately implemented interval proof of every residual
derivative; the executed residual producer's source is bound by provenance.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse,copy,hashlib,importlib.util,json,sys
import numpy as np
HERE=Path(__file__).resolve().parent;SDK=HERE/'sdk';sys.dont_write_bytecode=True
F=Q(211093,50);H=Q(1,8);NU=Q(2897,10000);T=Q(1,2);STRIP=Q(9,20)
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,o):p.write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8')
def module(name,f):
    sp=importlib.util.spec_from_file_location(name,SDK/f);m=importlib.util.module_from_spec(sp);sys.modules[name]=m;sp.loader.exec_module(m);return m
def exact(v):return Q.from_float(float(v))
def guard(record,folder):
    a=record['alpha'];label=a.replace('/','_');field=folder/('field-'+label+'.npz');residual=folder/('residual-'+label+'.json');ex=folder/('exponents-'+label+'.json')
    assert record['T']=='1/2' and record['contract_sha256']==sha(HERE/'nearby-contract-execution.json')
    assert record['quotes_sha256']==sha(SDK/'normalized-quote-bands.json')
    for key,p in [('field_sha256',field),('residual_sha256',residual),('exponents_sha256',ex),('bank_sha256',field.with_name(field.stem+'-residual-cells.npz'))]:assert record[key]==sha(p)
    assert [Q(r['u']) for r in record['node_ledger']]==[j*H for j in range(1025)]
    assert len(record['price_rows'])==12 and [r['row_id'] for r in record['price_rows']]==list(range(1,13))
    for r in record['price_rows']:
        assert Q(r['true_infinite_tail_remainder'])>0
        assert Q(r['actual_fast_output'])+Q(r['centre_correction'])==Q(r['strict_reference_centre'])==Q(r['fast_plus_signed_correction'])
    assert record['status']=='COMPLETE_POINT_CANDIDATE_AND_REAL_QUOTE_OBJECTIVE_CERTIFICATE'
    return field,residual,ex

def verify(record,folder):
    field,rp,ep=guard(record,folder);raw=load(rp);n=record['N'];alpha=Q(record['alpha'])
    assert raw['source_sha256']==sha(SDK/'certify-field-residual.py')
    assert raw['combined_derivative_source_sha256']==sha(SDK/'combined-field-derivative.py')
    assert Q(raw['alpha_exact'])==alpha==Q(raw['beta_exact'])
    data={k:v for k,v in np.load(field).items()};t,u,lg=data['t'],data['u'],data['LG']
    assert t.shape==(n+1,) and u.shape==(513,) and lg.shape==(n+1,513)
    assert t[0]==0 and t[-1]==.5 and np.all(np.diff(t)>0) and np.all(lg[0]==0)
    assert np.array_equal(u,np.arange(513)/8)
    assert all(np.all(np.isfinite(z)) for z in data.values())
    bank={k:v for k,v in np.load(field.with_name(field.stem+'-residual-cells.npz')).items()}
    aa=[0.];bb=[t[1]]
    for j in range(1,n):
        edges=np.linspace(t[j],t[j+1],3);edges[0]=t[j];edges[-1]=t[j+1]
        assert np.all(np.diff(edges)>0);aa.extend(edges[:-1]);bb.extend(edges[1:])
    assert np.array_equal(bank['a'],aa) and np.array_equal(bank['b'],bb)
    assert np.array_equal(bank['a'][1:],bank['b'][:-1]) and bank['b'][-1]==.5
    assert bank['bound'].shape==(2*n-1,513) and bank['re_upper'].shape==bank['bound'].shape
    assert np.all(np.isfinite(bank['bound'])) and np.all(bank['bound']>=0)
    deltas=list(map(Q,raw['delta_physical_upper_exact_dyadics']))
    assert list(map(exact,np.max(bank['bound'],axis=0)))==deltas
    assert list(map(exact,bank['bound'][0]))==list(map(Q,raw['first_cell_physical_upper_exact_dyadics']))
    assert np.all(bank['re_upper'][1:]<=0)
    assert all(Q(x)<=0 for x in raw['first_cell_Re_H_div_talpha_upper_exact_dyadics'])
    assert list(map(exact,np.max(bank['re_upper'][1:],axis=0)))==list(map(Q,raw['later_cells_Re_H_upper_exact_dyadics']))
    # Independently rebuild the analytic startup residual using the identified
    # rigorous producer primitives; all later closed bounds above are read.
    residual=module('ind_near_res','certify-field-residual.py')
    nu,c,d,B=residual.startup_coefficients(alpha,alpha,u,data['A1'],data['A2'])
    startup=residual.first_cell(t[1],lg[1],B,data['A1'],data['A2'],nu,c,d,alpha,alpha)
    assert list(map(exact,startup))==list(map(Q,raw['first_cell_physical_upper_exact_dyadics']))
    component=module('ind_near_component','exponent-field-certificate.py');mo,dy,I,S,C=component.mo,component.mo.dy,component.I,component.S,component.C
    direct=module('ind_near_tail','direct-tail-certificate.py');direct.T=T
    def iv(bounds):
        lo,hi=map(Q,bounds);assert lo<=hi;return I((lo.numerator*S)//lo.denominator,-((-hi.numerator*S)//hi.denominator),True)
    def upper(x):return Q(x.hi,S)
    def norm(c):return c.norm2().sqrt()
    def abs_i(x):return I(0 if x.lo<=0<=x.hi else min(abs(x.lo),abs(x.hi)),max(abs(x.lo),abs(x.hi)),True)
    j0=mo.moments(T,64)[0];wp=[mo.power_field_moment(k*alpha,T,64) for k in [1,2]]
    weights=mo.linear_field_weights(list(map(exact,t)),T,64);exdata=load(ep)
    assert exdata['weights']==[w.bounds() for w in weights]
    assert exdata['J0']==j0.bounds() and exdata['power_moments']==[w.bounds() for w in wp]
    exponent_rows=exdata['rows'];assert [Q(r['u']) for r in exponent_rows]==[j*H for j in range(513)]
    phis=[];mods=[]
    for j in range(513):
        u=j*H;ex=C(-(u*u+Q(1,4))/2)*j0
        for k in range(2):
            v=data['A'+str(k+1)][j];ex+=C(exact(v.real),exact(v.imag))*wp[k]/NU
        for k,w in enumerate(weights):
            v=lg[k,j];ex+=C(exact(v.real),exact(v.imag))*w/NU
        r=exponent_rows[j];assert ex.re.bounds()==r['exponent_re'] and ex.im.bounds()==r['exponent_im']
        mag=mo.signed_exp(ex.re);phi=C(mag*component.trig(ex.im,True),mag*component.trig(ex.im))
        assert phi.re.bounds()==r['phi_re'] and phi.im.bounds()==r['phi_im'] and mag.bounds()==r['phi_modulus']
        phis.append(phi);mods.append(mag)
    quotes=[r for r in load(SDK/'normalized-quote-bands.json')['rows'] if Q(r['T_decimal_input'])==T]
    ms=[Q(r['moneyness_fraction']) for r in quotes];pref=[I(m).sqrt()/dy.PI for m in ms];logs=[mo.log_endpoint(m) for m in ms]
    den=(Q(1,2)-STRIP)*(dy.exp_positive(2*dy.PI*STRIP/H)-1)
    strips=[upper(I(m).sqrt()*mo.signed_exp(STRIP*abs_i(k))/den) for m,k in zip(ms,logs)]
    td=direct.time_data(alpha,64);rate=Q(direct.tail_rate(Q(128),alpha,td).lo,S)
    assert str(rate)==record['tail_rate_lower'] and rate>0
    assert record['time_q_bin_edges']==list(map(str,td[0])) and record['time_q_bin_masses']==[v.bounds() for v in td[2]]
    tails=[upper(p*mo.signed_exp(I(-rate*128))/(rate*128**2)) for p in pref]
    refs=[I(1) for _ in range(12)];radius=[Q(0)]*12;coeffs=[];epsilons=[]
    for j,r in enumerate(record['node_ledger']):
        u=j*H;tm,te=direct.envelope_node(u,alpha,td);tb=Q(tm.hi,S)
        assert str(tb)==r['true_CF_modulus_upper'] and te.bounds()==r['comparison_exponent']
        if j<=512:
            mag=mods[j];eta=upper(I(deltas[j]/NU)*j0);cap=I(min(S,mag.lo),min(S,mag.hi),True)
            epsilon=min(upper(cap*(dy.exp_positive(I(eta))-1)),upper(I(tb)+mag));phi=phis[j]
        else:epsilon=tb;eta=Q(0);phi=C(0)
        assert str(epsilon)==r['epsilon_upper'] and str(eta)==r['eta_upper'];epsilons.append(epsilon)
        cs=[]
        for i in range(12):
            if j==0:cc=C(-2*H*pref[i])
            else:
                phase=-u*logs[i];cc=C(component.trig(phase,True),component.trig(phase))*(-H*pref[i]/(u*u+Q(1,4)))
            assert cc.re.bounds()==r['coefficients'][i]['re'] and cc.im.bounds()==r['coefficients'][i]['im']
            refs[i]+=(cc*phi).re;radius[i]+=epsilon*upper(norm(cc));cs.append(cc)
        coeffs.append(cs)
    centres=[Q(v.lo+v.hi,2*S) for v in refs];rounding=[Q(v.hi-v.lo,2*S) for v in refs]
    remainder=[strips[i]+tails[i]+rounding[i] for i in range(12)];complete=[radius[i]+remainder[i] for i in range(12)]
    incompat=[]
    for i,r in enumerate(record['price_rows']):
        assert Q(r['strict_reference_centre'])==centres[i] and Q(r['complete_reference_radius'])==complete[i]
        assert Q(r['strip_remainder'])==strips[i] and Q(r['true_infinite_tail_remainder'])==tails[i] and Q(r['reference_arithmetic_remainder'])==rounding[i]
        bounds=[max(Q(0),centres[i]-complete[i]),min(Q(1),centres[i]+complete[i])]
        assert bounds==list(map(Q,r['true_price_interval']))
        actual=Q(r['actual_fast_output']);correction=centres[i]-actual
        ra=exact(float(centres[i]));delta=exact(float(correction));ca=exact(float(actual)+float(delta))
        assert ra==Q(r['actual_reference_output_binary64']) and delta==Q(r['actual_signed_correction_binary64']) and ca==Q(r['actual_corrected_fast_output_binary64'])
        assert Q(r['correction_storage_rounding_exact'])==delta-correction and Q(r['correction_addition_rounding_exact'])==ca-actual-delta
        assert Q(r['actual_reference_complete_bound'])==abs(ra-centres[i])+complete[i]
        assert Q(r['actual_corrected_fast_complete_bound'])==abs(ca-centres[i])+complete[i]
        if bounds[1]<Q(quotes[i]['normalized_bid']['lower_fraction']) or bounds[0]>Q(quotes[i]['normalized_ask']['upper_fraction']):incompat.append(i+1)
    assert incompat==record['bid_ask_incompatible_rows']
    targets=[(Q(r['price_mid_target']['lower_fraction']),Q(r['price_mid_target']['upper_fraction'])) for r in quotes]
    z=[centres[i]-(a+b)/2 for i,(a,b) in enumerate(targets)];mq=[(b-a)/2 for a,b in targets]
    a=[v/12 for v in z];jc=sum((v*v for v in z),Q(0))/24;rr=[complete[i]+mq[i] for i in range(12)]
    h_m=sum((abs(a[i])*rr[i] for i in range(12)),Q(0));h_j=sum((abs(a[i])*(remainder[i]+mq[i]) for i in range(12)),Q(0))
    for eps,cs in zip(epsilons,coeffs):
        vector=C(0)
        for i in range(12):vector+=cs[i]*a[i]
        h_j+=eps*upper(norm(vector))
    qrest=sum((v*v for v in rr),Q(0))/24;bl=Q(0);bu=Q(0)
    for v,r in zip(z,rr):
        lo,hi=v-r,v+r;bl+=Q(0) if lo<=0<=hi else min(lo*lo,hi*hi);bu+=max(lo*lo,hi*hi)
    bl/=24;bu/=24;marg=[max(bl,jc-h_m,Q(0)),min(bu,jc+h_m+qrest)];joint=[max(marg[0],jc-h_j,Q(0)),min(marg[1],jc+h_j+qrest)]
    obj=record['objective'];assert list(map(Q,obj['joint_interval']))==joint and list(map(Q,obj['marginal_interval']))==marg
    assert Q(obj['reference_J'])==jc and Q(obj['joint_linear_support'])==h_j and Q(obj['marginal_linear_support'])==h_m and Q(obj['quadratic_remainder'])==qrest
    cs=record['correction_control'];jr=sum((eps*upper(norm(c[7]-c[8])) for eps,c in zip(epsilons,coeffs)),Q(0));mr=sum((eps*upper(norm(c[7])+norm(c[8])) for eps,c in zip(epsilons,coeffs)),Q(0));rem=remainder[7]+remainder[8]
    returned=[Q(r['actual_fast_output']) for r in record['price_rows']];shift=(centres[7]-centres[8])-(returned[7]-returned[8])
    assert Q(cs['uncorrected_fast_joint_complete_bound_points'])==(abs(shift)+jr+rem)*F
    assert Q(cs['direct_reference_and_corrected_joint_bound_points'])==(jr+rem)*F
    assert Q(cs['uncorrected_fast_marginal_complete_bound_points'])==(abs(shift)+mr+rem)*F
    for label,fieldname in [('reference','actual_reference_output_binary64'),('corrected_fast','actual_corrected_fast_output_binary64')]:
        output=[Q(r[fieldname]) for r in record['price_rows']];roundshift=abs(output[7]-output[8]-(centres[7]-centres[8]))
        assert Q(cs['actual_binary64_'+label+'_joint_bound_points'])==(roundshift+jr+rem)*F
        assert Q(cs['actual_binary64_'+label+'_marginal_bound_points'])==(roundshift+mr+rem)*F
    return {'alpha':str(alpha),'N':n,'closed_residual_entries':bank['bound'].size,'strict_exponents_rebuilt':513,
       'all_true_CF_nodes_and_12_coefficients_rebuilt':1025,'joint_objective':list(map(str,joint)),
       'marginal_objective':list(map(str,marg)),'incompatible_rows':incompat,'status':'PASS'}

def main():
    p=argparse.ArgumentParser();p.add_argument('--N',type=int,required=True);p.add_argument('--alpha');a=p.parse_args();folder=HERE/('N'+str(a.N));reports=[]
    if a.alpha:
        record=load(folder/('candidate-'+a.alpha.replace('/','_')+'.json'));report=verify(record,folder)
        save(folder/('point-independent-'+a.alpha.replace('/','_')+'.json'),{'status':'PASS_COMPLETE_POINT_RECONSTRUCTION','record':report,'candidate_sha256':sha(folder/('candidate-'+a.alpha.replace('/','_')+'.json')),'executed_reader_sha256':sha(Path(__file__))})
        print('PASS complete independent point',a.alpha,'N',a.N,flush=True);return
    summary=load(folder/'nearby-results.json')
    records=[load(folder/('candidate-'+s.replace('/','_')+'.json')) for s in summary['grid']]
    for r in records:
        cache=folder/('point-independent-'+r['alpha'].replace('/','_')+'.json');cp=folder/('candidate-'+r['alpha'].replace('/','_')+'.json')
        if cache.exists():
            stored=load(cache);assert stored['executed_reader_sha256']==sha(Path(__file__)) and stored['candidate_sha256']==sha(cp);reports.append(stored['record'])
        else:
            report=verify(r,folder);reports.append(report)
            save(cache,{'status':'PASS_COMPLETE_POINT_RECONSTRUCTION','record':report,'candidate_sha256':sha(cp),'executed_reader_sha256':sha(Path(__file__))})
        print('PASS independent complete point',r['alpha'],'N',a.N,flush=True)
    for line in summary['pairs']:
        aa=summary['grid'].index(line['alpha_a']);bb=summary['grid'].index(line['alpha_b'])
        for mode in ['joint','marginal']:
            lo,hi=map(Q,reports[aa][mode+'_objective']);l2,h2=map(Q,reports[bb][mode+'_objective']);expected=[str(lo-h2),str(hi-l2)]
            assert expected==line[mode]['a_minus_b_interval']
            decision='A_STRICTLY_SMALLER' if hi<l2 else 'B_STRICTLY_SMALLER' if h2<lo else 'UNRESOLVED'
            assert decision==line[mode]['decision']
    controls=[];r=records[0]
    for name,mutate in [
        ('drop_finite_tail_node',lambda v:v['node_ledger'].pop()),
        ('erase_true_infinite_tail',lambda v:v['price_rows'][0].update(true_infinite_tail_remainder='0')),
        ('alter_quote_identity',lambda v:v.update(quotes_sha256='0'*64)),
        ('alter_field_identity',lambda v:v.update(field_sha256='0'*64)),
        ('ignore_signed_translation',lambda v:v['price_rows'][0].update(centre_correction='0')),
        ('mislabel_diagnostic_as_certificate',lambda v:v.update(status='FLOAT_DIAGNOSTIC'))]:
        bad=copy.deepcopy(r);mutate(bad)
        try:guard(bad,folder)
        except (AssertionError,ValueError,KeyError):controls.append({'control':name,'rejected':True})
        else:raise AssertionError('negative control accepted: '+name)
    save(folder/'nearby-independent.json',{'status':'PASS_SEPARATE_ALL_NODE_AND_ALL_CELL_RECONSTRUCTION',
       'executed_reader_sha256':sha(Path(__file__)),'candidate_records':reports,'pair_decisions_checked':10,
       'negative_controls':controls,'source_sharing_boundary':'independent assembly and finite-set logic; shares identified rigorous moment, trig, tail and startup primitives; does not independently rederive all later residual derivatives',
       'candidate_sha256':summary['candidate_sha256']})
    print('PASS all pairs and six negative controls',flush=True)
if __name__=='__main__':main()
