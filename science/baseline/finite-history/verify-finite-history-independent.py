"""Independent finite-history arithmetic, coefficient, policy and menu audit.

Does not import finite-history.py. It reconstructs eta from physical residual
and nu, and uses a real trigonometric identity for the spread coefficients.
The upstream theorem and scalar interval primitives remain explicit dependencies.
"""
from fractions import Fraction as Q
from pathlib import Path
import copy,hashlib,importlib.util,json,sys,time
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;BASE=HERE.parent/'reference';OLD=HERE.parent/'continuous'
FROZEN=BASE/'code'/'frozen';SCALE=Q(211093,50)
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check_price_contract(record,data,pade):
    rows=[next(r for r in data['rows'] if r['K']==k) for k in ['4400','4500']]
    fast={r['row_id']:Q(r['normalized_call_exact_dyadic']) for c in pade['cover'] if Q(c['alpha'])==Q(record['alpha']) for r in c['rows']}
    centers=[sum(map(Q,r['stored_field_price']))/2 for r in rows]
    d=(centers[0]-fast[rows[0]['row_id']])-(centers[1]-fast[rows[1]['row_id']])
    R=sum((Q(r['budgets'][key][1]) for r in rows for key in ['grid','true_discrete_tail']),Q(0))
    R+=sum((Q(r['stored_field_price'][1])-Q(r['stored_field_price'][0]) for r in rows),Q(0))/2
    assert d==Q(record['unchanged_signed_centre']),'signed centre was altered'
    assert R==Q(record['unchanged_full_remainder']),'tail, grid or arithmetic was omitted'
    return rows,d,R
def main():
    started=0;sp=importlib.util.spec_from_file_location('checker_elementary',BASE/'code/src/exponent-field-certificate.py')
    cp=importlib.util.module_from_spec(sp);sp.loader.exec_module(cp);mo=cp.mo;I,S=mo.I,mo.S
    J0=mo.moments(Q(1,2),64)[0];pade=load(FROZEN/'frozen-pade-numeric-output.json')
    result=load(HERE/'finite-history-results.json');records=[];negative=[];menu=None
    manifest={r['path']:r['sha256'] for r in load(BASE/'code/MANIFEST.json')['artifacts']}
    tracked=[HERE/'finite-history-results.json',HERE/'experiment-contract.json',FROZEN/'frozen-pade-numeric-output.json']
    assert result['contract_sha256']==sha(HERE/'experiment-contract.json')
    assert sha(FROZEN/'frozen-pade-numeric-output.json')==manifest['code/frozen/frozen-pade-numeric-output.json']
    assert list(map(Q,result['finite_history_forward_mass_enclosure']))==list(map(Q,J0.bounds()))
    for rec in result['results']:
        alpha=Q(rec['alpha']);source=FROZEN/rec['source'];data=load(source);rows,center,R=check_price_contract(rec,data,pade)
        assert sha(source)==manifest['code/frozen/'+source.name]==result['input_sha256'][source.name]
        tracked.append(source)
        stem={Q(13,25):'betap52-u128',Q(3,5):'betap6-u128',Q(9,10):'betap9-u80'}[alpha]
        exponent_file=FROZEN/('fixed-field-'+stem+'-exponent-certificate.json');exponents=load(exponent_file)
        assert sha(exponent_file)==manifest['code/frozen/'+exponent_file.name]==result['input_sha256'][exponent_file.name]
        tracked.append(exponent_file)
        ep={Q(r['u']):r for r in exponents['cover']}
        receipt_file=HERE/rec['node_receipt'];receipt=load(receipt_file);reported=list(map(Q,receipt['all_node_radii']));tracked.append(receipt_file)
        assert len(reported)==1025,'finite node deleted'
        old=list(map(lambda n:Q(n['true_CF_minus_stored_CF_modulus_upper']),data['node_error_cover']))
        assert [Q(n['u']) for n in data['node_error_cover']]==[Q(j,8) for j in range(1025)]
        expected=list(old);byindex={n['index']:n for n in receipt['nodes']}
        assert set(byindex)==set(range(513)) and len(receipt['nodes'])==513,'eligible receipt node deleted'
        radius_reconstruction_started=0
        for j in range(513):
            node=data['node_error_cover'][j];assert Q(node['all_time_approximate_realpart_upper'])<=0
            delta=Q(node['delta_physical_upper'])/Q(data['nu']);assert delta==Q(node['delta_F_upper'])
            eta=I(delta)*J0;used=min(Q(eta.hi,S),Q(node['eta_upper']))
            phi=min(Q(1),Q(ep[Q(node['u'])]['phi_modulus'][1]));epsilon=I(phi)*(mo.dy.exp_positive(I(used))-1)
            expected[j]=min(old[j],Q(epsilon.hi,S))
            nr=byindex[j]
            assert Q(nr['delta_F'])==delta,'physical-to-normalized nu factor omitted'
            assert Q(nr['finite_history_eta_upper'])==Q(eta.hi,S) and Q(nr['used_eta_upper'])==used
            assert Q(nr['new_CF_radius'])==expected[j] and Q(nr['old_CF_radius'])==old[j]
        radius_reconstruction_seconds=0-radius_reconstruction_started
        assert expected==reported,'new radius vector does not match independent reconstruction'
        old_all=load(OLD/'shared-fourier-spread.json');original=next(r for r in old_all['results'] if Q(r['alpha'])==alpha)
        ledger_file=OLD/original['node_ledger_file'];ledger=load(ledger_file);a=[Q(n['combined_coefficient_modulus'][1]) for n in ledger]
        assert sha(ledger_file)==result['input_sha256'][ledger_file.name];tracked.append(ledger_file)
        b=[I(Q(r['m'])).sqrt() for r in rows];logratio=mo.log_endpoint(Q(rows[0]['m'])/Q(rows[1]['m']))
        stable_sum=I(0);marginal_coeff=[]
        for j in range(1025):
            u=Q(j,8);factor=Q(data['h'])*(2 if j==0 else 1/(u*u+Q(1,4)))/mo.dy.PI
            stable=((b[0]-b[1]).square()+4*b[0]*b[1]*cp.trig(u*logratio/2).square()).sqrt()
            stable_sum+=factor*stable*expected[j]
            marginal_coeff.append(max(Q((factor*(b[0]+b[1])).hi,S),a[j]))
        assert Q(stable_sum.hi,S)+R<=Q(rec['full_finite_history_radius_upper']),'alternative coefficient assembly cannot confirm full upper'
        radius=max(Q(original['joint_full_radius_upper']),R+sum((ai*ei for ai,ei in zip(a,old)),Q(0)))
        assert radius==Q(rec['baseline_radius_upper'])
        unprocessed=set(range(513));steps=[]
        for nr in receipt['nodes']:
            j=max(unprocessed,key=lambda k:(a[k]*old[k],-k));assert j==nr['index'],'policy chose wrong largest current contribution'
            radius-=a[j]*(old[j]-expected[j]);unprocessed.remove(j)
            steps.append({'radius':radius,'absolute':max(abs(center-radius),abs(center+radius))})
        assert radius==Q(rec['full_finite_history_radius_upper'])
        assert list(map(Q,rec['full_signed_interval']))==[center-radius,center+radius]
        assert Q(rec['full_absolute_error_upper'])==steps[-1]['absolute']
        prefix=rec['primary_trace']
        for j,tr in enumerate(prefix):
            assert Q(tr['radius_upper'])==steps[j]['radius'] and Q(tr['absolute_error_upper'])==steps[j]['absolute']
            assert tr['primary_budget_pass']==(steps[j]['absolute']*SCALE<=1)
        if alpha==Q(13,25):
            assert len(prefix)==82 and not prefix[-2]['primary_budget_pass'] and prefix[-1]['primary_budget_pass']
            threshold=Q(1)/SCALE-abs(center)
            menu_started=0
            def optimal_menu(label,coeff,baseline):
                gains=[(coeff[j]*(old[j]-expected[j]),j) for j in range(513)]
                ordered=sorted(gains,key=lambda x:(-x[0],x[1]));r=baseline;trace=[]
                if r<=threshold:return {'label':label,'minimum_upgrades':0,'baseline_radius':str(baseline),'trace':[]}
                for count,(gain,j) in enumerate(ordered,1):
                    r-=gain;trace.append({'step':count,'index':j,'u':str(Q(j,8)),'gain':str(gain),
                                        'radius':str(r),'absolute_error_upper':str(abs(center)+r),'pass':r<=threshold})
                    if r<=threshold:
                        return {'label':label,'minimum_upgrades':count,'baseline_radius':str(baseline),'threshold_radius':str(threshold),
                                'last_failed_radius':str(baseline if count==1 else Q(trace[-2]['radius'])),'certified_radius':str(r),'trace':trace}
                return {'label':label,'minimum_upgrades':None,'status':'NOT_CERTIFIED_EVEN_FULL_MENU','baseline_radius':str(baseline),'trace':trace}
            joint_start=Q(rec['baseline_radius_upper'])
            marginal_start=R+sum((ci*oi for ci,oi in zip(marginal_coeff,old)),Q(0))
            menu={'alpha':str(alpha),'joint':optimal_menu('shared_Fourier',a,joint_start),
                  'best_signed_marginal':optimal_menu('same_center_marginal',marginal_coeff,marginal_start),
                  'new_radii_precomputed_all_eligible_nodes':513,
                  'optimization_scope':'Exact minimum count for a fixed once-only upgrade menu with unit action counts, fixed signed centre and complete unchanged remainder. Not runtime-optimal and not a minimum number of residual-generation calls.',
                  'cost_caveat':'All new radii must already be computed to rank certified gains; complete node precomputation cost cannot be omitted.'}
            pass
            pass
        records.append({'alpha':str(alpha),'independently_reconstructed_radii':1025,'eligible_nodes':513,
                        
                        'old_policy_receipts_and_primary_trace_exactly_match':True,
                        'alternative_coefficient_full_upper_confirmed':True,'full_signed_endpoints_exactly_match':True})
        for name,changed_record,changed_data,changed_receipt in [
            ('zero_centre',dict(rec,unchanged_signed_centre='0'),data,None),
            ('remove_true_tail',rec,copy.deepcopy(data),None),
            ('delete_node',rec,data,dict(receipt,all_node_radii=receipt['all_node_radii'][:-1])),
            ('omit_nu',rec,data,copy.deepcopy(receipt))]:
            rejected=False
            if name=='remove_true_tail':changed_data['rows'][7]['budgets']['true_discrete_tail']=['0','0']
            if name=='omit_nu':changed_receipt['nodes'][0]['delta_F']=data['node_error_cover'][changed_receipt['nodes'][0]['index']]['delta_physical_upper']
            try:
                if changed_receipt is None:check_price_contract(changed_record,changed_data,pade)
                elif name=='delete_node':assert len(changed_receipt['all_node_radii'])==1025,'finite node deleted'
                else:
                    n=changed_receipt['nodes'][0];assert Q(n['delta_F'])==Q(data['node_error_cover'][n['index']]['delta_physical_upper'])/Q(data['nu']),'nu factor omitted'
            except AssertionError:rejected=True
            assert rejected;negative.append({'alpha':str(alpha),'corruption':name,'rejected':True})
    output={'status':'PASS_INDEPENDENT_FINITE_HISTORY_ARITHMETIC_AND_POLICY_AUDIT','records':records,'negative_controls':negative,
            'finite_history_theorem_still_external_proof_obligation':True,'shared_dependencies':'Original exact moment/exponential/trigonometric/interval primitives and saved upstream field/residual certificates; no import of finite-history.py',
            'input_sha256':{p.name:sha(p) for p in tracked},'implementation_sha256':sha(Path(__file__))}
    (HERE/'finite-history-independent-verification.json').write_text(json.dumps(output,indent=2)+'\n')
    pass
    (HERE/'optimal-upgrade-menu.json').write_text(json.dumps(menu,indent=2)+'\n')
    print(json.dumps({'status':output['status'],
                      'minimum_joint_upgrades':menu['joint']['minimum_upgrades'],
                      'minimum_same_center_marginal_upgrades':menu['best_signed_marginal']['minimum_upgrades']},indent=2))
if __name__=='__main__':main()
