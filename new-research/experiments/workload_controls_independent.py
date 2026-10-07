"""Separate rational read-back of same-guarantee and 28-task comparisons."""
from pathlib import Path
from fractions import Fraction as Q
import argparse,hashlib,importlib.util,json,sys
HERE=Path(__file__).resolve().parent;SDK=HERE/'sdk';F=Q(211093,50);sys.dont_write_bytecode=True
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser();p.add_argument('--N',type=int,required=True);p.add_argument('--local128',action='store_true');args=p.parse_args()
    location=HERE/'local128' if args.local128 else HERE/('N'+str(args.N));suffix='-local128' if args.local128 else ''
    bank=load(location/'candidate-13_25.json');controls=load(HERE/('workload-controls-N'+str(args.N)+suffix+'.json'));modern=load(HERE/'modern-adams-outputs.json')
    cs=bank['correction_control'];methods=controls['methods']
    assert methods[0]['complete_joint_bound_points']==cs['uncorrected_fast_joint_complete_bound_points']
    assert methods[1]['complete_joint_bound_points']==cs['actual_binary64_reference_joint_bound_points']
    assert methods[2]['complete_joint_bound_points']==cs['actual_binary64_corrected_fast_joint_bound_points']
    ref=Q(cs['direct_reference_spread']);jr=Q(cs['direct_reference_and_corrected_joint_bound_points']);mr=Q(cs['direct_reference_and_corrected_marginal_bound_points'])
    for r,m in zip(methods[3:],modern['rows']):
        output=list(map(Q,m['exact_stored_call_outputs']));delta=abs(output[7]-output[8]-ref)*F
        assert Q(r['complete_joint_bound_points'])==delta+jr and Q(r['complete_marginal_bound_points'])==delta+mr
        assert r['additional_output_workload']==m['workload']
    for r in methods:
        assert r['joint_quarter_point_pass']==(Q(r['complete_joint_bound_points'])<=Q(1,4))
        assert r['marginal_quarter_point_pass']==(Q(r['complete_marginal_bound_points'])<=Q(1,4))
    spec=importlib.util.spec_from_file_location('ind_controls_components',SDK/'exponent-field-certificate.py');comp=importlib.util.module_from_spec(spec);spec.loader.exec_module(comp);I,S,C=comp.I,comp.S,comp.C
    def iv(v):
        lo,hi=map(Q,v);return I((lo.numerator*S)//lo.denominator,-((-hi.numerator*S)//hi.denominator),True)
    def norm(c):return Q(c.norm2().sqrt().hi,S)
    prices=bank['price_rows'];coefs=[]
    for node in bank['node_ledger']:coefs.append([C(iv(c['re']),iv(c['im'])) for c in node['coefficients']])
    for rec in controls['all_28_portfolios']:
        ws=list(map(Q,rec['weights']));shift=sum((w*Q(r['centre_correction']) for w,r in zip(ws,prices)),Q(0));joint=Q(0);marg=Q(0)
        for node,cs in zip(bank['node_ledger'],coefs):
            z=C(0);h=Q(0)
            for w,c in zip(ws,cs):z+=c*w;h+=abs(w)*norm(c)
            eps=Q(node['epsilon_upper']);joint+=eps*norm(z);marg+=eps*h
        rem=sum((abs(w)*sum((Q(r[k]) for k in ['strip_remainder','true_infinite_tail_remainder','reference_arithmetic_remainder']),Q(0)) for w,r in zip(ws,prices)),Q(0))
        j=(abs(shift)+joint+rem)*F;m=(abs(shift)+marg+rem)*F
        assert Q(rec['frozen_fast_joint_bound_points'])==j and Q(rec['frozen_fast_marginal_bound_points'])==m
        assert Q(rec['direct_reference_joint_bound_points'])==(joint+rem)*F
        assert rec['joint_quarter_point_pass']==(j<=Q(1,4)) and rec['marginal_quarter_point_pass']==(m<=Q(1,4))
    assert controls['amortization']['additional_continuous_residual_entries_for_28_portfolios']==0
    assert controls['amortization']['joint_disk_support_terms']==28*1025
    out={'status':'PASS_SEPARATE_SAME_GUARANTEE_AND_28_TASK_READBACK','N':args.N,
      'methods_checked':5,'same_index_point_tolerance':'1/4','portfolio_aggregations_reconstructed':28,
      'new_continuous_residual_entries_for_portfolios':0,'controls_sha256':sha(HERE/('workload-controls-N'+str(args.N)+suffix+'.json')),
      'reader_sha256':sha(Path(__file__)),'rounding_paid':'actual binary64 reference, stored correction and final addition checked by nearby_independent; ideal rational translation is separately identified'}
    (HERE/('workload-controls-independent-N'+str(args.N)+suffix+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('PASS independent five-method and 28-task comparison',flush=True)
if __name__=='__main__':main()
