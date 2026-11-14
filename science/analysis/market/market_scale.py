"""Market scale and netting accounts derived from the saved banks.

The quote table, the certified distance between model and quotes, and the stored node supports are exact
rational readings of saved records. Netting ratios, band shares and the width scan evaluate the support
formula of Theorem 5.1 in binary64 from the stored node radii.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import cmath
import csv
import hashlib
import json
import math
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
F = Q(211093, 50)
STEP = Q(1, 8)
STRIKES = [3700 + 100 * i for i in range(12)]
BANDS = [(0, 16), (16, 32), (32, 64), (64, 96), (96, 129)]
WIDTHS = [5, 10, 25, 50, 100, 200, 400]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def dec(value, places=6):
    return f'{float(value):.{places}f}'


def upper(value, places=9):
    """Decimal display of a nonnegative rational bound, rounded upward."""
    scaled = value * 10 ** places
    digits = -((-scaled.numerator) // scaled.denominator)
    return f'{digits // 10 ** places}.{digits % 10 ** places:0{places}d}'


def payoff_modulus(weights, moneyness, u):
    """|sum_i w_i sqrt(m_i) exp(-i u k_i)| and the gross sum of |w_i| sqrt(m_i)."""
    total, gross = 0j, 0.0
    for w, m in zip(weights, moneyness):
        if w:
            c = w * math.sqrt(m)
            total += c * cmath.exp(-1j * u * math.log(m))
            gross += abs(c)
    return abs(total), gross


def node_supports(weights, moneyness, radii):
    """Joint and leg-by-leg node supports in index points for stored radii on the grid u_n = n/8."""
    joint = marginal = 0.0
    for n, radius in enumerate(radii):
        u = n * float(STEP)
        modulus, gross = payoff_modulus(weights, moneyness, u)
        scale = float(STEP) / math.pi * (0.5 if n == 0 else 1.0) * radius / (u * u + 0.25)
        joint += scale * modulus
        marginal += scale * gross
    return joint * float(F), marginal * float(F)


def build(science):
    paths = {
        'quotes': science/'experiments/sdk/normalized-quote-bands.json',
        'usecase': science/'baseline/reference/code/frozen/finance-usecase-calculations.json',
        'quarter_nodes': science/'baseline/frontier/transfer-time-local-nodes.json',
        'quarter_coefficients': science/'baseline/frontier/transfer-coefficients.json',
        'half_year_nodes': science/'baseline/finite-history/finite-history-nodes-alpha-13_25.json',
        'half_year_directions': science/'baseline/finite-history/portfolio-results-finite-history.json',
        'thresholds': science/'analysis/audit/portfolio-exact-thresholds.csv',
    }
    quotes = load(paths['quotes'])
    assert quotes['source_commit'] == '860049da2b7486fe8aa509061eff23cc28c2ef89'
    rows = []
    for r in quotes['rows']:
        bid = Q(r['normalized_bid']['lower_fraction']) * F
        ask = Q(r['normalized_ask']['upper_fraction']) * F
        mid = Q(r['price_mid_target']['lower_fraction']) * F
        rows.append({'strike': int(r['K_decimal_input']), 'bid_iv': r['bid_iv_decimal_input'],
                     'ask_iv': r['ask_iv_decimal_input'], 'bid_points': dec(bid, 2), 'ask_points': dec(ask, 2),
                     'mid_points': dec(mid, 2), 'width_points': dec(ask - bid, 2),
                     'bid_points_exact': str(bid), 'ask_points_exact': str(ask)})
    assert [r['strike'] for r in rows] == STRIKES
    by_strike = {r['strike']: r for r in rows}
    lo, hi = by_strike[4400], by_strike[4500]
    spread = {'legs': [4400, 4500],
              'mid_points': dec(Q(lo['bid_points_exact']) / 2 + Q(lo['ask_points_exact']) / 2
                                - Q(hi['bid_points_exact']) / 2 - Q(hi['ask_points_exact']) / 2, 3),
              'width_from_legs_points': dec(Q(lo['ask_points_exact']) - Q(lo['bid_points_exact'])
                                            + Q(hi['ask_points_exact']) - Q(hi['bid_points_exact']), 3)}

    usecase = load(paths['usecase'])
    assert usecase['contract']['sample_date'] == '2021-06-18'
    misfit = []
    for case in usecase['quote_validation_cases']:
        gap = Q(case['true_price']['lower_exact']) - Q(case['normalized_ask']['upper_exact'])
        assert gap > 0
        misfit.append({'strike': case['K'], 'model_price_lower_points': dec(Q(case['true_price']['lower_exact']) * F, 3),
                       'ask_points': dec(Q(case['normalized_ask']['upper_exact']) * F, 3),
                       'model_above_ask_points_lower': dec(gap * F, 3), 'model_above_ask_points_exact': str(gap * F)})

    quarter = load(paths['quarter_nodes'])
    coefficients = load(paths['quarter_coefficients'])
    m_lo, m_hi = [float(Q(x)) for x in coefficients['moneynesses']]
    delta = math.log(m_hi / m_lo)
    deviation = 0.0
    for row in coefficients['rows']:
        u = float(Q(row['u']))
        stored = float(Q(row['joint_modulus_upper'])) / float(Q(row['signed_marginal_modulus_upper']))
        formula = math.sqrt(math.tanh(delta / 4) ** 2 + math.sin(u * delta / 2) ** 2 / math.cosh(delta / 4) ** 2)
        deviation = max(deviation, abs(stored - formula))
    assert deviation < 1e-12
    joint_total = sum(Q(n['joint_node_support_exact']) for n in quarter['nodes']) * F
    marginal_total = sum(Q(n['signed_marginal_node_support_exact']) for n in quarter['nodes']) * F
    bands = []
    for low, high in BANDS:
        chosen = [n for n in quarter['nodes'] if low <= Q(n['u']) < high]
        joint = sum(Q(n['joint_node_support_exact']) for n in chosen) * F
        marginal = sum(Q(n['signed_marginal_node_support_exact']) for n in chosen) * F
        bands.append({'u_from': low, 'u_below': high, 'nodes': len(chosen), 'joint_points': dec(joint),
                      'leg_by_leg_points': dec(marginal), 'ratio': dec(joint / marginal, 3),
                      'share_of_leg_by_leg': dec(marginal / marginal_total, 3)})
    assert sum(b['nodes'] for b in bands) == 1025
    quarter_radii = [float(Q(n['time_CF_radius_upper'])) for n in quarter['nodes']]
    scan = []
    for width in WIDTHS:
        moneyness = [4400 / float(F), (4400 + width) / float(F)]
        joint, marginal = node_supports([1, -1], moneyness, quarter_radii)
        d = math.log(moneyness[1] / moneyness[0])
        scan.append({'width_points': width, 'nyquist_frequency': dec(math.pi / d, 1), 'joint_node_points': dec(joint),
                     'leg_by_leg_node_points': dec(marginal), 'ratio': dec(joint / marginal, 3)})
    check = next(s for s in scan if s['width_points'] == 100)
    assert abs(float(check['joint_node_points']) - float(joint_total)) < 1e-6
    assert abs(float(check['leg_by_leg_node_points']) - float(marginal_total)) < 1e-6

    radii = [float(Q(x)) for x in load(paths['half_year_nodes'])['all_node_radii']]
    assert len(radii) == 1025
    thresholds, spread_ladder = {}, []
    with paths['thresholds'].open(encoding='utf-8', newline='') as handle:
        for r in csv.DictReader(handle):
            if r['configuration_id'] == 'H1' and r['alpha'] == '13/25':
                thresholds[r['direction_id'], r['method']] = Q(r['exact_threshold_points'])
            if r['alpha'] == '13/25' and r['direction_id'] == 'adjacent-spread-4400-4500':
                spread_ladder.append({'configuration_id': r['configuration_id'], 'method': r['method'],
                                      'bound_points_upper_9dp': upper(Q(r['exact_threshold_points']))})
    moneyness = [k / float(F) for k in STRIKES]
    directions, families, signed = [], {}, {}
    for r in load(paths['half_year_directions'])['records']:
        if r['alpha'] != '13/25':
            continue
        signed[r['direction_id']] = Q(r['signed_center']) * F
        weights = [float(Q(x)) for x in r['weights']]
        account = r['radius_account']
        stored = (Q(account['certified_reference_nodes']) + Q(account['omitted_finite_nodes'])) * F
        joint, marginal = node_supports(weights, moneyness, radii)
        assert abs(joint - float(stored)) < 1e-9, r['direction_id']
        loads = [w * math.sqrt(m) for w, m in zip(weights, moneyness)]
        herfindahl = math.sqrt(sum(c * c for c in loads)) / sum(abs(c) for c in loads)
        centre = abs(Q(r['signed_center'])) * F
        row = {'direction_id': r['direction_id'], 'kind': r['kind'], 'joint_node_points': dec(stored),
               'leg_by_leg_node_points': dec(marginal), 'node_netting_ratio': dec(joint / marginal, 3),
               'herfindahl_root': dec(herfindahl, 3), 'absolute_centre_points': dec(centre),
               'complete_joint_points': dec(thresholds[r['direction_id'], 'joint']),
               'complete_leg_by_leg_points': dec(thresholds[r['direction_id'], 'marginal'])}
        directions.append(row)
        families.setdefault(r['kind'], []).append(row)
    assert len(directions) == 28
    steps = [signed[f'adjacent-spread-{a}-{a + 100}'] for a in STRIKES[:-1]]
    offsets = [-sum(steps[:i], Q(0)) for i in range(12)]
    first = signed['positive-basket-all'] - sum(offsets, Q(0)) / 12
    centres = [first + x for x in offsets]
    assert centres[0] - centres[3] == signed['wide-spread-3700-4000']
    assert sum(centres[:6], Q(0)) / 6 == signed['positive-basket-first-half']
    strike_centres = [{'strike': k, 'reference_minus_stored_points': dec(c, 3)} for k, c in zip(STRIKES, centres)]
    summary = []
    for kind, members in families.items():
        ratios = [float(x['node_netting_ratio']) for x in members]
        complete = [float(x['complete_joint_points']) / float(x['complete_leg_by_leg_points']) for x in members]
        summary.append({'kind': kind, 'count': len(members), 'node_ratio_min': dec(min(ratios), 3),
                        'node_ratio_mean': dec(sum(ratios) / len(ratios), 3), 'node_ratio_max': dec(max(ratios), 3),
                        'herfindahl_root_mean': dec(sum(float(x['herfindahl_root']) for x in members) / len(members), 3),
                        'absolute_centre_mean_points': dec(sum(float(x['absolute_centre_points']) for x in members) / len(members), 3),
                        'complete_ratio_mean': dec(sum(complete) / len(complete), 3)})
    return {
        'status': 'PASS_MARKET_SCALE_AND_NETTING_ACCOUNTS',
        'scope': 'Exact readings of saved quote, price and node records; binary64 evaluation of the Theorem 5.1 support formula from stored radii for ratios, band shares and the width scan.',
        'contract': {'sample_date': '2021-06-18', 'maturity_years': '1/2', 'index_level': '4221.86', 'discount': '1',
                     'contract_multiplier_usd_per_point': 100},
        'input_sha256': {str(p.relative_to(science).as_posix()): sha(p) for p in paths.values()},
        'executed_script_sha256': sha(Path(__file__)),
        'quotes': rows,
        'call_spread_4400_4500': spread,
        'certified_model_above_ask': misfit,
        'quarter_year_spread': {'log_strike_gap': dec(delta, 9), 'nyquist_frequency': dec(math.pi / delta, 2),
                                'formula_max_deviation_from_stored_ratio': f'{deviation:.3e}',
                                'joint_node_points': dec(joint_total), 'leg_by_leg_node_points': dec(marginal_total),
                                'ratio': dec(joint_total / marginal_total, 3), 'bands': bands, 'width_scan': scan},
        'six_month_spread_4400_4500_bounds': spread_ladder,
        'six_month_strike_centres': strike_centres,
        'six_month_directions': directions,
        'six_month_families': summary,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', default=str(HERE.parents[1]), help='Path of the science directory')
    parser.add_argument('--check', action='store_true', help='Compare with the saved record without writing')
    args = parser.parse_args()
    result = build(Path(args.baseline).resolve())
    target = HERE/'market-scale.json'
    if args.check:
        assert load(target) == result, 'saved market-scale record differs from the saved banks'
    else:
        target.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(result['status'], len(result['quotes']), 'quotes;', len(result['six_month_directions']), 'directions')


if __name__ == '__main__':
    main()
