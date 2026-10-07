"""Same-model, same-task, same-tolerance controls without host/clock metadata.

Every arbitrary output is compared to one shared complete strict reference;
neither modern empirical refinement nor a changed centre is a free guarantee.
Twenty-eight tasks aggregate the same point certificate without regeneration.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse,hashlib,importlib.util,json,sys
HERE=Path(__file__).resolve().parent;SDK=HERE/'sdk';sys.dont_write_bytecode=True
F=Q(211093,50)
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,o):p.write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def module(name,f):
    sp=importlib.util.spec_from_file_location(name,SDK/f);m=importlib.util.module_from_spec(sp);sys.modules[name]=m;sp.loader.exec_module(m);return m
def main():
    p=argparse.ArgumentParser();p.add_argument('--N',type=int,required=True);p.add_argument('--local128',action='store_true');args=p.parse_args()
    location=HERE/'local128' if args.local128 else HERE/('N'+str(args.N));suffix='-local128' if args.local128 else ''
    record=load(location/'candidate-13_25.json');modern=load(HERE/'modern-adams-outputs.json');ctrl=record['correction_control']
    reference=Q(ctrl['direct_reference_spread']);jr=Q(ctrl['direct_reference_and_corrected_joint_bound_points']);mr=Q(ctrl['direct_reference_and_corrected_marginal_bound_points'])
    rows=[{'method':'Frozen Padé output','complete_joint_bound_points':ctrl['uncorrected_fast_joint_complete_bound_points'],
          'complete_marginal_bound_points':ctrl['uncorrected_fast_marginal_complete_bound_points'],
          'additional_output_workload':{'Fourier_nodes':record['workload']['actual_fast_fourier_nodes'],'Jacobi_nodes_per_frequency':256}},
          {'method':'Direct strict reference returned as binary64','complete_joint_bound_points':ctrl['actual_binary64_reference_joint_bound_points'],'complete_marginal_bound_points':ctrl['actual_binary64_reference_marginal_bound_points'],
          'additional_output_workload':'reference already generated and fully charged below'},
          {'method':'Frozen Padé + binary64 stored correction and binary64 addition','complete_joint_bound_points':ctrl['actual_binary64_corrected_fast_joint_bound_points'],'complete_marginal_bound_points':ctrl['actual_binary64_corrected_fast_marginal_bound_points'],
          'additional_output_workload':{'binary64_additions_per_price':1},'algebraic_identity':'Ideal exact correction equals the rational centre; stored correction and addition rounding are explicitly charged.'}]
    for item in modern['rows']:
        if 'exact_stored_call_outputs' not in item:
            rows.append({'method':'BL modified-Adams core N='+str(item['N']),'status':item['status']});continue
        outputs=list(map(Q,item['exact_stored_call_outputs']));spread=outputs[7]-outputs[8];shift=abs(reference-spread)*F
        rows.append({'method':'BL modified-Adams core N='+str(item['N']),
            'complete_joint_bound_points':str(shift+jr),'complete_marginal_bound_points':str(shift+mr),
            'absolute_reference_translation_points':str(shift),'additional_output_workload':item['workload']})
    for r in rows:
        if 'complete_joint_bound_points' in r:
            r['joint_quarter_point_pass']=Q(r['complete_joint_bound_points'])<=Q(1,4)
            r['marginal_quarter_point_pass']=Q(r['complete_marginal_bound_points'])<=Q(1,4)
    # Freeze only mathematical portfolio content, excluding historical run info.
    pp=HERE/'portfolio-28.json'
    if not pp.exists():
        source=HERE.parent/'baseline/finite-history/portfolio-contract.json'
        old=load(source);save(pp,{'directions':old['directions'],'strikes':old['strikes'],
            'D':'1','F':'211093/50','position_scale':'exact original weights; one point multiplier',
            'source_contract_sha256':sha(source)})
    comp=module('control_component','exponent-field-certificate.py');I,S,C=comp.I,comp.S,comp.C
    def iv(b):
        lo,hi=map(Q,b);return I((lo.numerator*S)//lo.denominator,-((-hi.numerator*S)//hi.denominator),True)
    def norm(c):return Q(c.norm2().sqrt().hi,S)
    portfolios=[];price=record['price_rows']
    for d in load(pp)['directions']:
        weights=list(map(Q,d['weights']));shift=sum((w*Q(r['centre_correction']) for w,r in zip(weights,price)),Q(0));joint=Q(0);marginal=Q(0)
        for node in record['node_ledger']:
            z=C(0);per=Q(0)
            for w,c in zip(weights,node['coefficients']):
                cc=C(iv(c['re']),iv(c['im']));z+=cc*w;per+=abs(w)*norm(cc)
            epsilon=Q(node['epsilon_upper']);joint+=epsilon*norm(z);marginal+=epsilon*per
        rem=sum((abs(w)*sum((Q(r[k]) for k in ['strip_remainder','true_infinite_tail_remainder','reference_arithmetic_remainder']),Q(0)) for w,r in zip(weights,price)),Q(0))
        j=(abs(shift)+joint+rem)*F;m=(abs(shift)+marginal+rem)*F
        portfolios.append({'id':d['id'],'weights':d['weights'],'frozen_fast_joint_bound_points':str(j),'frozen_fast_marginal_bound_points':str(m),
             'direct_reference_joint_bound_points':str((joint+rem)*F),'same_radius_comparison':True,
             'joint_quarter_point_pass':j<=Q(1,4),'marginal_quarter_point_pass':m<=Q(1,4)})
    assert len(portfolios)==28
    save(HERE/('workload-controls-N'+str(args.N)+suffix+'.json'),{'status':'EXECUTED_SAME_MODEL_SAME_TASK_SAME_QUARTER_POINT_GUARANTEE_COMPARISON',
       'T':'1/2','alpha':'13/25','strikes':['4400','4500'],'index_point_tolerance':'1/4','methods':rows,
       'shared_complete_certificate_generation':record['workload'],
       'certificate_verification_workload':{'field_and_source_identity_checks':'all identified inputs','closed_cell_envelopes_read':record['workload']['continuous_residual_node_cell_entries'],
            'strict_exponents_reconstructed':513,'true_CF_node_envelopes_reconstructed':1025,'twelve_price_coefficients_reconstructed':12300},
       'all_28_portfolios':portfolios,
       'amortization':{'additional_continuous_residual_entries_for_28_portfolios':0,'joint_disk_support_terms':28*1025,
          'marginal_disk_support_terms':28*1025,'one_candidate_certificate_bank_reused_by_prices_and_portfolios':True},
       'empirical_modern_refinement_difference_points':modern['empirical_512_1024_spread_refinement_difference_points'],
       'important_boundary':'Saved bank reuse and typed work counts; generation and reading cover separate obligations.',
       'use_case':'Offline audit of frozen production outputs, external-library verification, and repeated tasks sharing one candidate certificate. For a fresh one-off price after the reference is available, direct reference output is the simpler certified choice.'})
    print('PASS same-guarantee output controls and 28 shared-bank tasks',flush=True)
if __name__=='__main__':main()
