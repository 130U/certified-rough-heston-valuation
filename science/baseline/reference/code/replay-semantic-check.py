"""Compare regenerated arithmetic records with released frozen mathematical values."""
from pathlib import Path
import argparse,json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
FROZEN=HERE/'frozen'

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--work',type=Path,default=ROOT/'out'/'aggregate')
    parser.add_argument('--output',type=Path,default=ROOT/'out'/'replay-semantic-check.json')
    args=parser.parse_args();work=args.work.resolve();outroot=(ROOT/'out').resolve()
    if work!=outroot and outroot not in work.parents:raise ValueError('work must be within out/')
    if outroot not in args.output.resolve().parents:raise ValueError('output must be within out/')
    price_fields=['rows','node_error_cover','aggregation_price_vector',
        'D_type_exponent_error_mass_upper_enclosure','true_tail_whole_curve_coefficient_lower']
    names=['f8-price-point052-u64.json','f8-price-point06-u64.json','f8-price-betap9-u64-.json']
    for name in names:
        old=json.loads((FROZEN/name).read_text(encoding='utf-8'))
        new=json.loads((work/name).read_text(encoding='utf-8'))
        for field in price_fields:assert old[field]==new[field],(name,field)
    name='finite-candidate-calibration-result.json'
    old=json.loads((FROZEN/name).read_text(encoding='utf-8'))
    new=json.loads((work/name).read_text(encoding='utf-8'))
    fields=['global_finite_minimum_objective_enclosure','strict_unique_finite_minimizer',
        'strict_winner_objective_gap_lower','objective_uniform_perturbation_strict_robustness_radius']
    for field in fields:assert old[field]==new[field],field
    for a,b in zip(old['candidates'],new['candidates']):
        for field in ['alpha','H','bounds','true_objective_gap_enclosure']:assert a[field]==b[field]
    for a,b in zip(old['actual_Pade_numeric_output_reference_oracle']['candidates'],
                   new['actual_Pade_numeric_output_reference_oracle']['candidates']):
        assert a==b
    application=json.loads((work/'finance-usecase-calculations.json').read_text(encoding='utf-8'))
    assert application['true_unique_winner']==application['actual_pade_unique_winner']=='13/25'
    result={'status':'PASS_REPLAY_NUMERICAL_VALUES_IDENTICAL',
        'price_certificates_compared':3,'price_rows':36,
        'compared_price_fields':price_fields,'finite_objective_fields':fields,
        'actual_Pade_candidate_objective_and_error_vectors_identical':True,
        'application_winner_alpha':'13/25',
        'spread_error_upper_exact':application['vertical_call_spread']['actual_spread_error_upper_using_price_box']['exact'],
        'scope':'Saved residual/exponent/tail inputs replayed through price and objective aggregation; metadata identities differ under documented public relocation.'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
