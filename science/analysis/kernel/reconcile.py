"""Exact read-only reconciliation of matched kernel inputs and baseline displays."""
import argparse
from fractions import Fraction as Q
from common import HERE, baseline, identities, load, save, sha

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--baseline');args=parser.parse_args()
    base=baseline(args.baseline);identities(base)
    original=load(base/'experiments/N2048/candidate-13_25.json')
    local=load(base/'experiments/local128/candidate-13_25.json')
    result=load(HERE/'results.json')
    fields=['actual_fast_output','strict_reference_centre','centre_correction',
            'actual_reference_output_binary64','actual_corrected_fast_output_binary64',
            'strip_remainder','true_infinite_tail_remainder','reference_arithmetic_remainder']
    assert len(original['price_rows'])==len(local['price_rows'])==12
    assert all(a[k]==b[k] for a,b in zip(original['price_rows'],local['price_rows']) for k in fields)
    assert len(original['node_ledger'])==len(local['node_ledger'])==1025
    assert all(a['coefficients']==b['coefficients'] for a,b in zip(original['node_ledger'],local['node_ledger']))
    for mode,source in [('global_curve',original),('local_curve',local)]:
        current=result['modes'][mode]
        assert Q(current['frozen_fast_joint_bound_points'])==Q(source['correction_control']['uncorrected_fast_joint_complete_bound_points'])
        for a,b in zip(current['price_rows'],source['price_rows']):
            assert Q(a['complete_reference_radius'])==Q(b['complete_reference_radius'])
            assert Q(a['frozen_fast_absolute_error_upper'])==Q(b['frozen_fast_absolute_error_upper'])
    for k in ['signed_centre_points','finite_omitted_joint_radius_points','remainder_points']:
        assert len({result['modes'][m][k] for m in result['modes']})==1
    modes=result['modes'];v=modes['local_resolvent']
    floor=abs(Q(v['signed_centre_points']))+Q(v['finite_omitted_joint_radius_points'])+Q(v['remainder_points'])
    lower=Q((floor.numerator*10**9)//floor.denominator,10**9)
    assert lower<floor and lower>Q(1,4)
    global_bound=Q(modes['global_curve']['frozen_fast_joint_bound_points'])
    scaled=global_bound*10**9
    ceiling=(scaled.numerator+scaled.denominator-1)//scaled.denominator
    assert ceiling==428570987
    save(HERE/'matched-input-audit.json',{
        'status':'PASS_EXACT_SAME_INPUTS_AND_BASELINE_ENDPOINT_RECONCILIATION',
        'script_sha256':sha(HERE/'reconcile.py'),'results_sha256':sha(HERE/'results.json'),
        'source_N2048_sha256':sha(base/'experiments/N2048/candidate-13_25.json'),
        'source_local128_sha256':sha(base/'experiments/local128/candidate-13_25.json'),
        'same_price_input_fields':fields,'all_price_rows':12,'all_frequency_coefficients':1025,
        'same_four_mode_fields':['signed_centre_points','finite_omitted_joint_radius_points','remainder_points'],
        'global_and_local_curve_full_price_endpoints_exactly_match_saved_baseline':True,
        'global_curve_bound_exact':str(global_bound),'global_curve_upward_nine_decimal':'0.428570987',
        'fixed_formula_floor_exact':str(floor),'fixed_formula_floor_downward_nine_decimal':'0.352626733',
        'floor_strictly_above_downward_endpoint_and_quarter_budget':True})
    print('PASS_EXACT_SAME_INPUTS_AND_BASELINE_ENDPOINT_RECONCILIATION')

if __name__=='__main__':main()
