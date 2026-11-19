"""Add actual returned binary64 controls to already proved centre/radius ledgers.

This deterministic algebraic augmentation does not change fields, residuals,
strict reference exponents, Fourier radii, quotes, objectives, or grid design.
It charges stored correction and final addition rounding explicitly.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse,json
HERE=Path(__file__).resolve().parent;F=Q(211093,50)
def exact(x):return Q.from_float(float(x))
def main():
    p=argparse.ArgumentParser();p.add_argument('--N',type=int,required=True);a=p.parse_args()
    for path in (HERE/('N'+str(a.N))).glob('candidate-*.json'):
        obj=json.loads(path.read_text(encoding='utf-8'))
        for r in obj['price_rows']:
            centre=Q(r['strict_reference_centre']);fast=Q(r['actual_fast_output']);correction=centre-fast
            ref=exact(float(centre));delta=exact(float(correction));returned=exact(float(fast)+float(delta));radius=Q(r['complete_reference_radius'])
            r.update(actual_reference_output_binary64=str(ref),actual_signed_correction_binary64=str(delta),
               actual_corrected_fast_output_binary64=str(returned),reference_output_rounding_exact=str(ref-centre),
               correction_storage_rounding_exact=str(delta-correction),correction_addition_rounding_exact=str(returned-fast-delta),
               actual_reference_complete_bound=str(abs(ref-centre)+radius),actual_corrected_fast_complete_bound=str(abs(returned-centre)+radius))
        rows=obj['price_rows'];cs=obj['correction_control'];ideal=Q(cs['direct_reference_spread'])
        for name,key in [('reference','actual_reference_output_binary64'),('corrected_fast','actual_corrected_fast_output_binary64')]:
            returned=Q(rows[7][key])-Q(rows[8][key]);shift=abs(returned-ideal)*F
            cs['actual_binary64_'+name+'_spread']=str(returned)
            cs['actual_binary64_'+name+'_joint_bound_points']=str(shift+Q(cs['direct_reference_and_corrected_joint_bound_points']))
            cs['actual_binary64_'+name+'_marginal_bound_points']=str(shift+Q(cs['direct_reference_and_corrected_marginal_bound_points']))
        cs['qualification']='Ideal rational reference and exact corrected prices are algebraically equal. Actual binary64 reference/correction/addition are separately stored and their exact translation from the ideal centre is fully charged.'
        path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('PASS exact binary64 storage and addition rounding augmentation')
if __name__=='__main__':main()
