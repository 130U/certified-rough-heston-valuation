"""Separate rational readback of the reference secondary audit.

No producer import, no recomputation claim for the original continuous bank.
Frozen evidence and original certified scalar primitives are inherited.
"""
from pathlib import Path
from fractions import Fraction
import copy,hashlib,importlib.util,json,sys,csv
import numpy as np
sys.dont_write_bytecode=True
from audit_layout import HERE as A,BASE as B,EXP as E,resolve
Q=Fraction;F=Q(211093,50)
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def src(n):return read(B/n)
def exp(n):return read(E/n)
def value(x):return Q(x)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def sumq(xs):return sum((value(x) for x in xs),Q())
def quarter(data):
 original=src('frontier/transfer-supplement-results.json');local=src('frontier/transfer-time-local-results.json');ledger=src('frontier/transfer-time-local-nodes.json')['nodes']
 assert len(ledger)==1025 and original['omitted_finite_nodes']==0
 j=sumq(x['joint_node_support_exact'] for x in ledger);m=sumq(x['signed_marginal_node_support_exact'] for x in ledger)
 c=value(original['signed_centre_exact']);r={k:value(original[n]) for k,n in [('strip','true_strip_upper'),('true_infinite_tail','true_infinite_tail_upper'),('reference_arithmetic','reference_arithmetic_radius')]};rest=sum(r.values(),Q())
 expected={'signed_reference_minus_actual_fast':(c,c),'absolute_centre_charge':(abs(c),abs(c)),'used_reference_node_support':(j,m),'finite_zero_node_support':(Q(),Q()),'complete_radius':(j+rest,m+rest),'absolute_error_upper':(abs(c)+j+rest,abs(c)+m+rest)}
 expected.update({k:(v,v) for k,v in r.items()});assert len(data['rows'])==len(expected)
 for x in data['rows']:
  a,b=expected[x['component']];assert value(x['joint_normalized_exact'])==a and value(x['marginal_normalized_exact'])==b;assert value(x['joint_index_points_exact'])==F*a and value(x['marginal_index_points_exact'])==F*b
 assert value(data['total_support_difference_points'])==(m-j)*F
 assert data['joint_pass']==(F*(abs(c)+j+rest)<=Q(1,4)) and data['marginal_pass']==(F*(abs(c)+m+rest)<=Q(1,4))
 assert F*(abs(c)+j+rest)==value(local['joint_absolute_bound_index_points_exact'])
 assert F*(abs(c)+m+rest)==value(local['signed_marginal_absolute_bound_index_points_exact'])
def paircheck(data):
 lookup={}
 for n in [1024,2048]:
  old=exp(f'N{n}/nearby-results.json')
  for a in old['grid']:lookup[n,a]=exp(f'N{n}/candidate-'+a.replace('/','_')+'.json')
 expected=[]
 for n in [1024,2048]:
  grid=list(exp(f'N{n}/nearby-results.json')['grid'])
  for ia,a in enumerate(grid):
   for b in grid[ia+1:]:
    for mode in ['joint','marginal']:
     x=list(map(value,lookup[n,a]['objective'][mode+'_interval']));y=list(map(value,lookup[n,b]['objective'][mode+'_interval']));lo,hi=x[0]-y[1],x[1]-y[0];decision='A_STRICTLY_SMALLER' if hi<0 else 'B_STRICTLY_SMALLER' if lo>0 else 'UNRESOLVED'
     expected.append({'level':n,'alpha_a':a,'alpha_b':b,'mode':mode,'a_minus_b_interval_exact':list(map(str,[lo,hi])),'decision':decision})
 assert data['pairs']==expected and len(expected)==40
 assert data['unresolved']==[{k:r[k] for k in ['level','alpha_a','alpha_b','mode']} for r in expected if r['decision']=='UNRESOLVED']
 a=lookup[2048,'13/25'];b=lookup[2048,'21/40'];aa=a['objective'];bb=b['objective'];nearest=data['nearest_pair'];gap=value(bb['joint_interval'][0])-value(aa['joint_interval'][1])
 assert value(nearest['strict_gap_exact'])==gap and gap>0
 assert value(nearest['lower_B_exact'])==value(bb['joint_interval'][0]) and value(nearest['upper_A_exact'])==value(aa['joint_interval'][1])
 parts={r['component']:r for r in nearest['parts']};assert value(parts['reference_midpoint_objective_difference']['signed_gap_contribution'])==value(bb['reference_J'])-value(aa['reference_J'])
 assert value(parts['candidate_a_quadratic_remainder']['signed_gap_contribution'])==-value(aa['quadratic_remainder'])
 quotes=[r for r in exp('sdk/normalized-quote-bands.json')['rows'] if value(r['T_decimal_input'])==Q(1,2)]
 remainder={};nodegroups={}
 specification=importlib.util.spec_from_file_location('reader_strict_original',E/'sdk/exponent-field-certificate.py');primitive=importlib.util.module_from_spec(specification);sys.modules[specification.name]=primitive;specification.loader.exec_module(primitive);I,C,S=primitive.I,primitive.C,primitive.S
 def interval(bounds):
  lo,hi=map(value,bounds);return I(lo.numerator*S//lo.denominator,-((-hi.numerator*S)//hi.denominator),True)
 for lab,cand in [('a',a),('b',b)]:
  rem={k:Q() for k in ['strip','true_infinite_tail','reference_arithmetic','midpoint_conversion_arithmetic']};weights=[]
  for p,q in zip(cand['price_rows'],quotes):
   lo,hi=value(q['price_mid_target']['lower_fraction']),value(q['price_mid_target']['upper_fraction']);signed_weight=(value(p['strict_reference_centre'])-(lo+hi)/2)/12;weights.append(signed_weight);weight=abs(signed_weight)
   rem['strip']+=weight*value(p['strip_remainder']);rem['true_infinite_tail']+=weight*value(p['true_infinite_tail_remainder']);rem['reference_arithmetic']+=weight*value(p['reference_arithmetic_remainder']);rem['midpoint_conversion_arithmetic']+=weight*(hi-lo)/2
  remainder[lab]=rem
  groups={'used_node_support':Q(),'finite_zero_support':Q()}
  for frequency in cand['node_ledger']:
   combined=C(0)
   for coefficient,weight in zip(frequency['coefficients'],weights):combined+=C(interval(coefficient['re']),interval(coefficient['im']))*weight
   contribution=Q(combined.norm2().sqrt().hi,S)*value(frequency['epsilon_upper'])
   groups['finite_zero_support' if value(frequency['u'])>64 else 'used_node_support']+=contribution
  nodegroups[lab]=groups
 for key in remainder['a']:
  rr=parts[key+'_both_candidates'];assert value(rr['candidate_a_support'])==remainder['a'][key] and value(rr['candidate_b_support'])==remainder['b'][key];assert value(rr['signed_gap_contribution'])==-remainder['a'][key]-remainder['b'][key]
 for key in ['used_node_support','finite_zero_support']:
  rr=parts[key+'_both_candidates'];assert value(rr['candidate_a_support'])==nodegroups['a'][key] and value(rr['candidate_b_support'])==nodegroups['b'][key];assert value(rr['signed_gap_contribution'])==-value(rr['candidate_a_support'])-value(rr['candidate_b_support'])
 for lab,cand in [('a',a),('b',b)]:
  total=sum(remainder[lab].values(),Q())+sumq(parts[key+'_both_candidates']['candidate_'+lab+'_support'] for key in ['used_node_support','finite_zero_support']);assert total==value(cand['objective']['joint_linear_support'])
 adjustment=value(bb['joint_interval'][0])-(value(bb['reference_J'])-value(bb['joint_linear_support']))+(value(aa['reference_J'])+value(aa['joint_linear_support'])+value(aa['quadratic_remainder'])-value(aa['joint_interval'][1]))
 assert value(parts['box_intersection_endpoint_adjustment']['signed_gap_contribution'])==adjustment
 assert sumq(x['signed_gap_contribution'] for x in nearest['parts'])==gap
def countcheck(data):
 thresholds=[]
 for file,cid in [('portfolio-results.json','H0'),('portfolio-results-finite-history.json','H1')]:
  for r in src('finite-history/'+file)['records']:
   for key,method in [('best_signed_marginal','marginal'),('shared_Fourier','joint')]:thresholds.append({'configuration_id':cid,'T':'1/2','alpha':r['alpha'],'direction_id':r['direction_id'],'method':method,'exact_threshold_points':r['absolute_error_bounds_index_points'][key]})
 for n,cid,tail in [(1024,'N1',''),(2048,'N2',''),(2048,'N2L','-local128')]:
  for r in exp(f'workload-controls-N{n}{tail}.json')['all_28_portfolios']:
   for method in ['joint','marginal']:thresholds.append({'configuration_id':cid,'T':'1/2','alpha':'13/25','direction_id':r['id'],'method':method,'exact_threshold_points':r['frozen_fast_'+method+'_bound_points']})
 assert thresholds==data['threshold_rows'] and len(thresholds)==504
 curves={}
 for r in thresholds:curves.setdefault((r['configuration_id'],r['alpha'],r['method']),[]).append(value(r['exact_threshold_points']))
 assert all(len(v)==28 for v in curves.values());expected=[]
 for k,v in sorted(curves.items()):
  for b in sorted(set(v)|{Q(),Q(1,4),Q(1,2),Q(1),Q(2)}):expected.append({'configuration_id':k[0],'alpha':k[1],'method':k[2],'exact_budget_points':str(b),'passed_count':len([x for x in v if not x>b]),'directions':28})
 assert expected==data['counts']
 with (A/'portfolio-exact-thresholds.csv').open(newline='',encoding='utf-8') as f:assert list(csv.DictReader(f))==thresholds
 with (A/'portfolio-budget-counts.csv').open(newline='',encoding='utf-8') as f:assert list(csv.DictReader(f))==[{k:str(v) for k,v in r.items()} for r in expected]
def configcheck(data):
 initial=exp('nearby-contract.json');assert value(data['common']['nu'])==Q(2897,10000) and data['common']['strict_bits']==100
 assert data['common']['finite_grid_nodes']==1025 and data['common']['actual_fast_fourier_nodes']==352
 for alpha,record in data['old_fields'].items():
  with np.load(resolve(record['field_source'])) as z:
   t=[Q.from_float(float(v)) for v in z['t']];assert len(t)-1==record['stored_time_cells'];assert len(z['u'])==record['stored_frequency_nodes'];assert sum(x<Q(1,4) for x in t)==record['quarter_restricted_time_cells'];assert (Q(1,4) in t)==record['quarter_endpoint_is_original_knot']
 for r in data['configurations']:
  assert value(r['nu'])==Q(2897,10000) and r['reference_nonzero_nodes']==8*int(r['reference_cutoff'])+1 and r['finite_zero_nodes']==1025-r['reference_nonzero_nodes']
  if r['configuration_id'] in ['N1','N2','N2L']:assert r['closed_subcells_per_nonstartup_cell']==initial['closed_subcells_per_nonstartup_cell']==2
  else:assert r['closed_subcells_per_nonstartup_cell']==4
  if r['configuration_id'] in ['H3','H4','Q1','Q2']:assert r['finite_zero_nodes']==0
def centrecheck(data):
 old=src('finite-history/time-local-results.json');expanded=src('frontier/omission-results.json');values={}
 values['H2']=(value(old['unchanged_signed_centre'])*F,value(old['time_local_full_radius_upper'])*F)
 for cid,r in zip(['H3','H4'],expanded['scenarios']):values[cid]=(value(r['new_signed_centre'])*F,value(r['joint_radius_upper'])*F)
 actual=[r['unchanged_actual_fast'] for r in expanded['reference_rows']]
 for path,cid in [('N2048/candidate-13_25.json','N2'),('local128/candidate-13_25.json','N2L')]:
  d=exp(path);p=d['price_rows'];shift=(value(p[7]['centre_correction'])-value(p[8]['centre_correction']))*F;bound=value(d['correction_control']['uncorrected_fast_joint_complete_bound_points']);values[cid]=(shift,bound-abs(shift));assert [p[7]['actual_fast_output'],p[8]['actual_fast_output']]==actual
 for row in data['rows']:
  c,r=values[row['configuration_id']];assert value(row['signed_centre_points'])==c and value(row['absolute_centre_points'])==abs(c);assert value(row['complete_radius_points'])==r and value(row['complete_bound_points'])==abs(c)+r;assert row['actual_fast_exact_normalized']==actual
 for r in data['transitions']:
  a,b=values[r['before']],values[r['after']];assert value(r['absolute_centre_charge_change_points'])==abs(b[0])-abs(a[0]);assert value(r['complete_radius_change_points'])==b[1]-a[1];assert value(r['complete_bound_change_points'])==abs(b[0])+b[1]-abs(a[0])-a[1];assert r['same_reference_centre']==(a[0]==b[0])
 for r in data['BL_reference_floor_shares']:
  cid=r['configuration_id'];n=1024 if cid=='N1' else 2048;d=exp(f'workload-controls-N{n}'+('-local128' if cid=='N2L' else '')+'.json');method=next(m for m in d['methods'] if m['method']==r['method']);bound=value(method['complete_joint_bound_points']);shift=value(method['absolute_reference_translation_points']);floor=bound-shift;ref=value(d['methods'][1]['complete_joint_bound_points']);assert value(r['ideal_reference_certificate_floor_points'])==floor and value(r['BL_translation_points'])==shift and value(r['BL_complete_bound_points'])==bound and value(r['returned_reference_complete_bound_points'])==ref;assert value(r['ideal_floor_fraction_of_BL_bound'])==floor/bound and value(r['returned_reference_fraction_of_BL_bound'])==ref/bound
def matrixcheck(data):
 for r in data['obligations']:
  text=resolve(r['source']).read_text(encoding='utf-8');assert digest(resolve(r['source']))==r['source_sha256'];assert all(x in text for x in r['source_anchors'])
 for r in data['flag_source_identities']:assert digest(resolve(r['source']))==r['sha256']
 run=(B/'finite-history/run_evidence.py').read_text(encoding='utf-8');assert "if a.full:run('all-211241-structural-signs'" in run and "if a.regenerate_continuous:run('fresh-all-513-time-residuals'" in run
 frontier=(B/'frontier/run_frontier.py').read_text(encoding='utf-8');assert 'if a.regenerate_full:' in frontier
 row=next(r for r in data['flag_semantics'] if r['entry']=='reproduce.py --full');assert row['newly_executes']=='default plus all211241 original structural sign leaves' and 'continuous derivative generation' in row['does_not_execute']
 ci=next(r for r in data['flag_semantics'] if r['entry']=='publication CI source.yml');assert ci['newly_executes']=='publication source identities'
def main():
 identities=read(A/'source-identities.json');assert len(identities['sources'])==identities['source_objects']
 for name,r in identities['sources'].items():p=resolve(name);assert p.stat().st_size==r['evidence_bytes'] and digest(p)==r['sha256']
 checks=[('quarter-exact-ledger.json',quarter),('nearby-pair-resolution.json',paircheck),('portfolio-budget-counts.json',countcheck),('configuration-registry.json',configcheck),('frozen-output-centre-account.json',centrecheck),('proof-obligation-matrix.json',matrixcheck)]
 for file,fn in checks:fn(read(A/file))
 controls=[]
 def reject(name,file,fn,mutate):
  bad=copy.deepcopy(read(A/file));mutate(bad)
  try:fn(bad)
  except (AssertionError,KeyError,ValueError):controls.append({'control':name,'rejected':True})
  else:raise AssertionError('corrupted account accepted '+name)
 reject('manufacture_quarter_finite_omission',checks[0][0],quarter,lambda d:next(r for r in d['rows'] if r['component']=='finite_zero_node_support').update(joint_normalized_exact='1/100000'))
 reject('erase_paid_reference_arithmetic',checks[0][0],quarter,lambda d:next(r for r in d['rows'] if r['component']=='reference_arithmetic').update(joint_normalized_exact='0'))
 reject('delete_nearby_quadratic_gap_charge',checks[1][0],paircheck,lambda d:next(r for r in d['nearest_pair']['parts'] if r['component']=='candidate_a_quadratic_remainder').update(signed_gap_contribution='0'))
 reject('claim_unresolved_pair_as_separated',checks[1][0],paircheck,lambda d:d['pairs'][0].update(decision='A_STRICTLY_SMALLER'))
 reject('lose_endpoint_equality_at_budget',checks[2][0],countcheck,lambda d:d['counts'][1].update(passed_count=d['counts'][1]['passed_count']-1))
 reject('relabel_new_bank_as_four_subcells',checks[3][0],configcheck,lambda d:next(r for r in d['configurations'] if r['configuration_id']=='N2').update(closed_subcells_per_nonstartup_cell=4))
 reject('ignore_new_reference_centre_payment',checks[4][0],centrecheck,lambda d:next(r for r in d['transitions'] if r['before']=='H2').update(absolute_centre_charge_change_points='0'))
 reject('erase_BL_reference_floor',checks[4][0],centrecheck,lambda d:d['BL_reference_floor_shares'][0].update(ideal_reference_certificate_floor_points='0'))
 reject('misstate_full_as_continuous_generation',checks[5][0],matrixcheck,lambda d:next(r for r in d['flag_semantics'] if r['entry']=='reproduce.py --full').update(newly_executes='all fresh continuous derivatives'))
 receipt={'status':'PASS_INDEPENDENT_SECONDARY_SAVED_EVIDENCE_AUDIT','reader_sha256':digest(Path(__file__)),'source_identity_manifest_sha256':digest(A/'source-identities.json'),'derived_objects':[{'path':name,'sha256':digest(A/name)} for name,fn in checks],'work_counts':{'original_quarter_finite_support_nodes':1025,'nearby_pair_mode_decisions':40,'portfolio_complete_threshold_endpoints':504,'original_configurations':11,'deliberate_corruptions_rejected':len(controls)},'negative_controls':controls,'scope':'Separate exact secondary derivations from frozen reference evidence. Original continuous-bank derivative validity and strict elementary/moment libraries remain inherited; no new full original pipeline replay is claimed. Used/finite nearby linear supports and coordinate remainders are independently reassembled with the disclosed strict arithmetic primitive, which is not a separately implemented transcendental library.'}
 (A/'independent-audit.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8');print('PASS independent reference secondary audit',len(controls),'meaningful corruption controls')
if __name__=='__main__':main()
