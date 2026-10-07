"""Deterministic secondary audit of the frozen reference evidence; no host telemetry.

This audit reassembles already certified accounts. It neither regenerates a
Caputo residual bank nor converts a diagnostic into a new certificate.
"""
from pathlib import Path
from fractions import Fraction as Q
import csv,hashlib,importlib.util,json,sys
import numpy as np
sys.dont_write_bytecode=True
from audit_layout import HERE,PACKET as ROOT,BASE,EXP,canonical
FROZEN=BASE/'reference/code/frozen';NINE=BASE/'finite-history';FRONT=BASE/'frontier'
F=Q(211093,50);SOURCES={}
def source(p):
 key=canonical(p);SOURCES[key]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'evidence_bytes':p.stat().st_size};return key
def load(p):source(p);return json.loads(p.read_text(encoding='utf-8'))
def save(name,x):
 def conv(v):
  if isinstance(v,Q):return str(v)
  if isinstance(v,list):return [conv(i) for i in v]
  if isinstance(v,dict):return {k:conv(i) for k,i in v.items()}
  return v
 (HERE/name).write_text(json.dumps(conv(x),indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def qsum(xs):return sum(map(Q,xs),Q(0))
def dec(x):return f'{float(Q(x)):.9f}'
def md(name,text): (HERE/name).write_text(text.rstrip()+'\n',encoding='utf-8')
def shape(p):
 source(p)
 with np.load(p) as z:return {k:list(v.shape) for k,v in z.items()}
def configs():
 low=NINE/'time-residual-alpha-13_25.npz';high=FRONT/'omission-time-high.npz'
 shapes={'old_low':shape(low),'old_high':shape(high)}
 fields={}
 for a,label,upper in [('13/25','52',128),('3/5','6',128),('9/10','9',80)]:
  p=FROZEN/('fixed-field-betap'+label+'-u'+str(upper)+'.npz');source(p)
  with np.load(p) as z:
   ts=[Q.from_float(float(v)) for v in z['t']]
   nt=len(ts)-1;ni=sum(v<Q(1,4) for v in ts)
   fields[a]={'field_source':canonical(p),'field_sha256':SOURCES[canonical(p)]['sha256'],'stored_time_cells':nt,'stored_frequency_nodes':len(z['u']),'stored_field_cutoff':upper,'quarter_restricted_time_cells':ni,'quarter_endpoint_is_original_knot':Q(1,4) in ts}
 common={'nu':'2897/10000','rho':'-1489/2000','Riccati_kappa':'0','frequency_step':'1/8','finite_grid_cutoff':'128','finite_grid_nodes':1025,'strict_bits':100,'moment_series_terms':64,'tail_time_bins':64,'strip_halfwidth':'9/20','actual_fast_fourier_cutoff':'200','actual_fast_fourier_nodes':352,'actual_fast_Gauss_order':8,'actual_fast_Jacobi_order':256}
 out=[]
 def row(cid,T,alphas,ref,sub,bins,nt,origin,bank,bound='not_one_common_value'):
  out.append(dict(common,configuration_id=cid,T=T,alphas=alphas,reference_cutoff=str(ref),reference_nonzero_nodes=int(ref*8+1),finite_zero_nodes=int((128-ref)*8),closed_subcells_per_nonstartup_cell=sub,history_bins=bins,reference_time_cells=nt,field_origin=origin,residual_bank=bank,reported_joint_bound_points=bound))
 row('H0','1/2',['13/25','3/5','9/10'],64,4,0,{'13/25':2048,'3/5':2048,'9/10':1024},'old stored field; old uniform propagation','released global continuous certificate')
 row('H1','1/2',['13/25','3/5','9/10'],64,4,1,{'13/25':2048,'3/5':2048,'9/10':1024},'same old field; finite-horizon global propagation','same global continuous certificate')
 row('H2','1/2',['13/25'],64,4,128,2048,'same old field; low-node local propagation','old_low: 8189 x 513 closed entries','0.367258782')
 row('H3','1/2',['13/25'],128,4,'low128; high1',2048,'same old field; reference centre expanded to 128','old_low + old_high: 8189 x 1025','0.132245064')
 row('H4','1/2',['13/25'],128,4,128,2048,'same old field; reference centre expanded to 128','old_low + old_high: 8189 x 1025','0.115215934')
 row('Q0','1/4',['13/25','3/5','9/10'],64,4,1,{a:d['quarter_restricted_time_cells'] for a,d in fields.items()},'new quarter fast output; restricted old field','reused larger-horizon global certificate')
 row('Q1','1/4',['13/25'],128,4,1,fields['13/25']['quarter_restricted_time_cells'],'new quarter fast output; restricted old field; expanded reference','old low global + old high global','0.351318692')
 row('Q2','1/4',['13/25'],128,4,128,fields['13/25']['quarter_restricted_time_cells'],'same Q1 field/output/centre; all intersecting closed cells from zero','old_low + old_high; weighted over [0,1/4]','0.233318843')
 contract=load(EXP/'nearby-contract.json')
 for n,cid in [(1024,'N1'),(2048,'N2')]:
  row(cid,'1/2',contract['candidate_alpha_exact'],64,2,1,n,'independently regenerated field at every alpha','fresh '+str(2*n-1)+' x 513 per alpha','0.590239296' if n==1024 else '0.428570987')
  for a in contract['candidate_alpha_exact']:
   p=EXP/f'N{n}'/('field-'+a.replace('/','_')+'.npz');sh=shape(p);assert sh['t']==[n+1] and sh['u']==[513]
   shape(EXP/f'N{n}'/('field-'+a.replace('/','_')+'-residual-cells.npz'))
 row('N2L','1/2',['13/25'],64,2,128,2048,'same independently regenerated N2 field/output/centre','N2 closed bank reused; zero new residual entries','0.394999331')
 save('configuration-registry.json',{'status':'SOURCE_IDENTITIES_AND_MATHEMATICAL_SHAPES_FIXED','common':common,'old_fields':fields,'bank_shapes':shapes,'configurations':out,'BL_core_solver_levels':[512,1024],'BL_guarantee_source':'N1,N2 or N2L complete reference account; BL nominal history is not a separate residual certificate','definition':'N_t counts physical-time source cells; Nu is explicitly the number of frequency nodes, not the model parameter nu. history_bins=0 means old uniform-state bound, 1 global finite-horizon envelope. Quarter restrictions keep history from zero.'})
 return out,fields
def quarter():
 s=load(FRONT/'transfer-supplement-results.json');l=load(FRONT/'transfer-time-local-results.json');nodes=load(FRONT/'transfer-time-local-nodes.json')['nodes']
 j=qsum(r['joint_node_support_exact'] for r in nodes);m=qsum(r['signed_marginal_node_support_exact'] for r in nodes)
 assert j==Q(l['joint_node_support_exact']) and m==Q(l['signed_marginal_node_support_exact'])
 center=Q(l['unchanged_signed_centre_exact']);strip=Q(s['true_strip_upper']);tail=Q(s['true_infinite_tail_upper']);arith=Q(s['reference_arithmetic_radius']);rem=strip+tail+arith
 assert rem==Q(s['full_remainder_exact'])==Q(l['unchanged_full_remainder_exact']);assert s['omitted_finite_nodes']==0
 rows=[]
 for name,vj,vm in [('signed_reference_minus_actual_fast',center,center),('absolute_centre_charge',abs(center),abs(center)),('used_reference_node_support',j,m),('finite_zero_node_support',Q(0),Q(0)),('strip',strip,strip),('true_infinite_tail',tail,tail),('reference_arithmetic',arith,arith),('complete_radius',j+rem,m+rem),('absolute_error_upper',abs(center)+j+rem,abs(center)+m+rem)]:
  rows.append({'component':name,'joint_normalized_exact':vj,'marginal_normalized_exact':vm,'joint_index_points_exact':vj*F,'marginal_index_points_exact':vm*F})
 assert rows[-1]['joint_index_points_exact']==Q(l['joint_absolute_bound_index_points_exact']) and rows[-1]['marginal_index_points_exact']==Q(l['signed_marginal_absolute_bound_index_points_exact'])
 save('quarter-exact-ledger.json',{'configuration_id':'Q2','status':'PASS_EXACT_REASSEMBLY_OF_ALL1025_TERMS','F':F,'rows':rows,'same_output_field_centre_radii_and_remainders':True,'only_difference':'1025-node support aggregated after versus before combining the two strike coefficients','total_support_difference_points':(m-j)*F,'budget_points':'1/4','joint_pass':rows[-1]['joint_index_points_exact']<=Q(1,4),'marginal_pass':rows[-1]['marginal_index_points_exact']<=Q(1,4)})
 return rows
def objective_gap():
 contract=load(EXP/'nearby-contract.json');qdata=load(EXP/'sdk/normalized-quote-bands.json');quotes=[q for q in qdata['rows'] if Q(q['T_decimal_input'])==Q(1,2)]
 pairs=[]
 for n in [1024,2048]:
  d=load(EXP/f'N{n}/nearby-results.json')
  for p in d['pairs']:
   a=load(EXP/f'N{n}'/('candidate-'+p['alpha_a'].replace('/','_')+'.json'))
   b=load(EXP/f'N{n}'/('candidate-'+p['alpha_b'].replace('/','_')+'.json'))
   for mode in ['joint','marginal']:
    ai=list(map(Q,a['objective'][mode+'_interval']));bi=list(map(Q,b['objective'][mode+'_interval']));interval=[ai[0]-bi[1],ai[1]-bi[0]]
    decision='A_STRICTLY_SMALLER' if interval[1]<0 else 'B_STRICTLY_SMALLER' if interval[0]>0 else 'UNRESOLVED'
    assert list(map(Q,p[mode]['a_minus_b_interval']))==interval and p[mode]['decision']==decision
    pairs.append({'level':n,'alpha_a':p['alpha_a'],'alpha_b':p['alpha_b'],'mode':mode,'a_minus_b_interval_exact':interval,'decision':decision})
 a=load(EXP/'N2048/candidate-13_25.json');b=load(EXP/'N2048/candidate-21_40.json')
 # Shared disclosed outward arithmetic; independently reassemble used/zero support.
 sp=importlib.util.spec_from_file_location('audit_strict',EXP/'sdk/exponent-field-certificate.py');comp=importlib.util.module_from_spec(sp);sys.modules['audit_strict']=comp;sp.loader.exec_module(comp);source(EXP/'sdk/exponent-field-certificate.py')
 I,C,S=comp.I,comp.C,comp.S
 def iv(x):
  lo,hi=map(Q,x);return I((lo.numerator*S)//lo.denominator,-((-hi.numerator*S)//hi.denominator),True)
 def parts(candidate):
  prices=candidate['price_rows'];centres=[Q(p['strict_reference_centre']) for p in prices];mq=[];aa=[]
  for i,q in enumerate(quotes):
   lo,hi=Q(q['price_mid_target']['lower_fraction']),Q(q['price_mid_target']['upper_fraction']);mq.append((hi-lo)/2);aa.append((centres[i]-(hi+lo)/2)/12)
  parts={k:Q(0) for k in ['used_node_support','finite_zero_support','strip','true_infinite_tail','reference_arithmetic','midpoint_conversion_arithmetic']}
  for w,p,s in zip(aa,prices,mq):
   parts['strip']+=abs(w)*Q(p['strip_remainder']);parts['true_infinite_tail']+=abs(w)*Q(p['true_infinite_tail_remainder']);parts['reference_arithmetic']+=abs(w)*Q(p['reference_arithmetic_remainder']);parts['midpoint_conversion_arithmetic']+=abs(w)*s
  for row in candidate['node_ledger']:
   cc=[C(iv(c['re']),iv(c['im'])) for c in row['coefficients']];combined=sum((c*w for c,w in zip(cc,aa)),C(0));support=Q(combined.norm2().sqrt().hi,S)*Q(row['epsilon_upper']);parts['used_node_support' if Q(row['u'])<=64 else 'finite_zero_support']+=support
  assert sum(parts.values(),Q(0))==Q(candidate['objective']['joint_linear_support'])
  return parts
 pa,pb=parts(a),parts(b);oa,ob=a['objective'],b['objective'];upperA=Q(oa['joint_interval'][1]);lowerB=Q(ob['joint_interval'][0]);gap=lowerB-upperA
 rows=[{'component':'reference_midpoint_objective_difference','signed_gap_contribution':Q(ob['reference_J'])-Q(oa['reference_J'])}]
 for k in pa:rows.append({'component':k+'_both_candidates','signed_gap_contribution':-pa[k]-pb[k],'candidate_a_support':pa[k],'candidate_b_support':pb[k]})
 rows.append({'component':'candidate_a_quadratic_remainder','signed_gap_contribution':-Q(oa['quadratic_remainder'])})
 rows.append({'component':'box_intersection_endpoint_adjustment','signed_gap_contribution':lowerB-(Q(ob['reference_J'])-Q(ob['joint_linear_support']))+(Q(oa['reference_J'])+Q(oa['joint_linear_support'])+Q(oa['quadratic_remainder'])-upperA)})
 assert qsum(r['signed_gap_contribution'] for r in rows)==gap and gap>0
 save('nearby-pair-resolution.json',{'status':'PASS_ALL40_PAIR_DECISIONS_REASSEMBLED','pairs':pairs,'unresolved':[{k:r[k] for k in ['level','alpha_a','alpha_b','mode']} for r in pairs if r['decision']=='UNRESOLVED'],'nearest_pair':{'level':2048,'alpha_a':'13/25','alpha_b':'21/40','lower_B_exact':lowerB,'upper_A_exact':upperA,'strict_gap_exact':gap,'parts':rows,'interpretation':'Finite-grid fixed original price-midpoint loss only. Conversion arithmetic is not market bid/ask uncertainty; every candidate retains a separate bid/ask incompatibility check.'}})
 return rows,gap
def thresholds():
 rows=[]
 for filename,cid in [('portfolio-results.json','H0'),('portfolio-results-finite-history.json','H1')]:
  d=load(NINE/filename)
  for r in d['records']:
   for key,method in [('best_signed_marginal','marginal'),('shared_Fourier','joint')]:
    rows.append({'configuration_id':cid,'T':'1/2','alpha':r['alpha'],'direction_id':r['direction_id'],'method':method,'exact_threshold_points':r['absolute_error_bounds_index_points'][key]})
 for filename,cid in [('workload-controls-N1024.json','N1'),('workload-controls-N2048.json','N2'),('workload-controls-N2048-local128.json','N2L')]:
  d=load(EXP/filename)
  for r in d['all_28_portfolios']:
   for method in ['joint','marginal']:
    rows.append({'configuration_id':cid,'T':'1/2','alpha':'13/25','direction_id':r['id'],'method':method,'exact_threshold_points':r['frozen_fast_'+method+'_bound_points']})
 series={}
 for r in rows:
  key=(r['configuration_id'],r['alpha'],r['method']);series.setdefault(key,[]).append(Q(r['exact_threshold_points']))
 assert len(rows)==504 and all(len(v)==28 for v in series.values())
 counts=[]
 for key,vs in sorted(series.items()):
  budgets=sorted(set(vs)|{Q(0),Q(1,4),Q(1,2),Q(1),Q(2)})
  for budget in budgets:counts.append({'configuration_id':key[0],'alpha':key[1],'method':key[2],'exact_budget_points':str(budget),'passed_count':sum(v<=budget for v in vs),'directions':28})
 for name,records in [('portfolio-exact-thresholds.csv',rows),('portfolio-budget-counts.csv',counts)]:
  with (HERE/name).open('w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,fieldnames=list(records[0]));w.writeheader();w.writerows(records)
 save('portfolio-budget-counts.json',{'status':'PASS_EXACT_ENDPOINT_CDF','inclusion_rule':'A complete upper endpoint B is certified at tolerance tau iff B<=tau. Floating coordinates are used only for rendering. Every curve has the same 28 fixed directions; between-bank curves are descriptive, within-bank joint/marginal comparisons have identical radii. No 28-direction quarter bank is manufactured.','threshold_rows':rows,'counts':counts})
 return series,counts
def centres():
 omission=load(FRONT/'omission-results.json');old=load(NINE/'time-local-results.json');globalR=load(NINE/'finite-history-results.json');nodeold=load(NINE/'time-local-node-ledger.json');ledger=load(FRONT/'omission-node-ledger.json');price=load(FROZEN/'f8-price-point052-u64.json')
 # The actual target stays fixed. Every reference movement pays its new centre.
 rows=[]
 for cid,centre,radius in [('H2',Q(old['unchanged_signed_centre']),Q(old['time_local_full_radius_upper']))]:
  rows.append({'configuration_id':cid,'signed_centre_points':centre*F,'absolute_centre_points':abs(centre)*F,'complete_radius_points':radius*F,'complete_bound_points':(abs(centre)+radius)*F,'actual_fast_exact_normalized':[r['unchanged_actual_fast'] for r in omission['reference_rows']]})
 for cid,r in zip(['H3','H4'],omission['scenarios']):
  c=Q(r['new_signed_centre']);rad=Q(r['joint_radius_upper']);bound=Q(r['joint_absolute_bound_index_points_exact']);assert (abs(c)+rad)*F==bound
  rows.append({'configuration_id':cid,'signed_centre_points':c*F,'absolute_centre_points':abs(c)*F,'complete_radius_points':rad*F,'complete_bound_points':bound,'actual_fast_exact_normalized':[r['unchanged_actual_fast'] for r in omission['reference_rows']]})
 for filename,cid in [('N2048/candidate-13_25.json','N2'),('local128/candidate-13_25.json','N2L')]:
  d=load(EXP/filename);p=d['price_rows'];c=Q(p[7]['centre_correction'])-Q(p[8]['centre_correction']);bound=Q(d['correction_control']['uncorrected_fast_joint_complete_bound_points']);radius=bound/F-abs(c)
  assert [p[7]['actual_fast_output'],p[8]['actual_fast_output']]==rows[0]['actual_fast_exact_normalized']
  rows.append({'configuration_id':cid,'signed_centre_points':c*F,'absolute_centre_points':abs(c)*F,'complete_radius_points':radius*F,'complete_bound_points':bound,'actual_fast_exact_normalized':[p[7]['actual_fast_output'],p[8]['actual_fast_output']]})
 changes=[]
 for before,after in [('H2','H3'),('H3','H4'),('N2','N2L'),('H4','N2L')]:
  a=next(r for r in rows if r['configuration_id']==before);b=next(r for r in rows if r['configuration_id']==after)
  dc=Q(b['absolute_centre_points'])-Q(a['absolute_centre_points']);dr=Q(b['complete_radius_points'])-Q(a['complete_radius_points']);db=Q(b['complete_bound_points'])-Q(a['complete_bound_points']);assert dc+dr==db
  changes.append({'before':before,'after':after,'absolute_centre_charge_change_points':dc,'complete_radius_change_points':dr,'complete_bound_change_points':db,'same_actual_fast':True,'same_reference_centre':a['signed_centre_points']==b['signed_centre_points'],'interpretation':'Cross-bank descriptive identity' if before=='H4' else 'Exact frozen-target centre/radius accounting'})
 floor=[]
 for filename,cid in [('workload-controls-N1024.json','N1'),('workload-controls-N2048.json','N2'),('workload-controls-N2048-local128.json','N2L')]:
  d=load(EXP/filename);reference=Q(d['methods'][1]['complete_joint_bound_points'])
  # Strict ideal radius is obtained from independently validated candidate ledger.
  candidate=load(EXP/('local128/candidate-13_25.json' if cid=='N2L' else f'N{1024 if cid=="N1" else 2048}/candidate-13_25.json'))
  ideal=Q(candidate['correction_control']['direct_reference_and_corrected_joint_bound_points'])
  for m in d['methods'][3:]:
   total=Q(m['complete_joint_bound_points']);translation=Q(m['absolute_reference_translation_points']);assert ideal+translation==total
   floor.append({'configuration_id':cid,'method':m['method'],'ideal_reference_certificate_floor_points':ideal,'returned_reference_complete_bound_points':reference,'BL_translation_points':translation,'BL_complete_bound_points':total,'ideal_floor_fraction_of_BL_bound':ideal/total,'returned_reference_fraction_of_BL_bound':reference/total,'boundary':'Dominance of the common certificate floor does not establish intrinsic BL accuracy or algorithm speed.'})
 save('frozen-output-centre-account.json',{'status':'PASS_EXACT_TARGET_PRESERVATION_AND_CENTRE_PAYMENT','rows':rows,'transitions':changes,'BL_reference_floor_shares':floor})
 return rows,changes,floor
def main():
 conf,fields=configs();qr=quarter();gaprows,gap=objective_gap();series,counts=thresholds();cr,change,floor=centres()
 save('source-identities.json',{'status':'FROZEN_FOR_SECONDARY_AUDIT','sources':SOURCES,'source_objects':len(SOURCES),'total_evidence_bytes':sum(v['evidence_bytes'] for v in SOURCES.values()),'boundary':'Exact saved-evidence secondary audit; no new residual or exponent proof generated by this script.'})
 print('PASS deterministic reference saved-evidence audit',len(SOURCES),'source objects; exact nearest-pair gap',f'{float(gap):.12e}')
if __name__=='__main__':main()
