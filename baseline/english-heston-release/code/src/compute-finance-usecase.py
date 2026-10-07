"""Exact read-back of the sealed finite calibration case; no pricing rerun."""
from pathlib import Path
from fractions import Fraction as Q
import hashlib
import json

HERE = Path(__file__).resolve().parent
BASE = HERE
NAMES = ["finite-candidate-calibration-result.json", "normalized-quote-bands.json",
         "frozen-pade-numeric-output.json", "f8-price-point052-v3-u64.json",
         "f8-price-point06-v3-u64.json", "f8-price-betap9-u64-v3.json"]
DATA = {name: json.loads((BASE / name).read_text(encoding="utf-8")) for name in NAMES}

def dec(q, digits=15, upper=False):
    q = Q(q)
    scale = 10 ** digits
    scaled = q * scale
    z = -((-scaled.numerator) // scaled.denominator) if upper else scaled.numerator // scaled.denominator
    sign = "-" if z < 0 else ""
    z = abs(z)
    return sign + str(z // scale) + "." + str(z % scale).zfill(digits)

def interval(lo, hi):
    return {"lower_exact": str(Q(lo)), "upper_exact": str(Q(hi)),
            "lower_decimal_outward": dec(lo), "upper_decimal_outward": dec(hi, upper=True)}

def exact(q):
    return {"exact": str(Q(q)), "lower_decimal_outward": dec(q),
            "upper_decimal_outward": dec(q, upper=True)}

result = DATA[NAMES[0]]
quotes = DATA[NAMES[1]]
numeric = DATA[NAMES[2]]
gap = Q(result["strict_winner_objective_gap_lower"])
radius = Q(result["objective_uniform_perturbation_strict_robustness_radius"])
assert gap > 0 and radius == gap / 2
assert result["strict_unique_finite_minimizer"] == "13/25"

objective_rows = []
algorithm = result["actual_frozen_pade_algorithm"] if "actual_frozen_pade_algorithm" in result else None
if algorithm is None:
    for key, value in result.items():
        if isinstance(value, dict) and "candidates" in value:
            algorithm = value
            break
assert algorithm is not None
alg_by_alpha = {r["alpha"]: r for r in algorithm["candidates"]}
for item in result["candidates"]:
    ab = alg_by_alpha[item["alpha"]]["algorithm_objective_bounds"]
    objective_rows.append({"alpha": item["alpha"], "H": item["H"],
                           "true_J": interval(item["bounds"]["mid_lower"], item["bounds"]["mid_upper"]),
                           "actual_pade_J": interval(ab["mid_lower"], ab["mid_upper"]),
                           "excluded_quote_rows": item["bounds"]["compatibility_box_excluded_by_rows"]})
winner_alg = alg_by_alpha["13/25"]["algorithm_objective_bounds"]
algorithm_gap = min(Q(row["algorithm_objective_bounds"]["mid_lower"])
                    for a, row in alg_by_alpha.items() if a != "13/25") - Q(winner_alg["mid_upper"])
assert algorithm_gap > 0

quote_by_id = {r["row_id"]: r for r in quotes["rows"]}
price_by_id = {r["row_id"]: r for r in DATA[NAMES[3]]["rows"]}
stored_by_id = {r["row_id"]: r for r in numeric["cover"][0]["rows"]}
cases = []
for row_id in [8, 9]:
    quote, price = quote_by_id[row_id], price_by_id[row_id]
    plo, phi = map(Q, price["true_normalized_price"])
    bid = quote["normalized_bid"]
    ask = quote["normalized_ask"]
    alo, ahi = Q(ask["lower_fraction"]), Q(ask["upper_fraction"])
    cash = Q(stored_by_id[row_id]["normalized_call_exact_dyadic"])
    error = max(abs(cash - plo), abs(cash - phi))
    assert plo > ahi
    recorded_error = Q(alg_by_alpha["13/25"]["actual_numeric_normalized_price_error_upper"][row_id - 1])
    assert error == recorded_error
    cases.append({"row_id": row_id, "K": quote["K_decimal_input"],
                  "bid_iv": quote["bid_iv_decimal_input"], "ask_iv": quote["ask_iv_decimal_input"],
                  "normalized_bid": interval(bid["lower_fraction"], bid["upper_fraction"]),
                  "normalized_ask": interval(alo, ahi),
                  "true_price": interval(plo, phi), "actual_pade_output": exact(cash),
                  "actual_output_error_upper": exact(error),
                  "true_price_above_ask_gap_lower": exact(plo - ahi),
                  "normalized_quote_band_width": interval(alo - Q(bid["upper_fraction"]),
                                                          ahi - Q(bid["lower_fraction"])),
                  "actual_pade_above_ask": interval(cash - ahi, cash - alo)})

p8lo, p8hi = map(Q, price_by_id[8]["true_normalized_price"])
p9lo, p9hi = map(Q, price_by_id[9]["true_normalized_price"])
spread_lo, spread_hi = p8lo - p9hi, p8hi - p9lo
spread_p = Q(stored_by_id[8]["normalized_call_exact_dyadic"]) - Q(stored_by_id[9]["normalized_call_exact_dyadic"])
e8 = Q(cases[0]["actual_output_error_upper"]["exact"])
e9 = Q(cases[1]["actual_output_error_upper"]["exact"])
spread_error = max(abs(spread_p - spread_lo), abs(spread_p - spread_hi))
assert 0 < spread_lo < spread_hi < Q(100) / Q("4221.86")
assert spread_error <= e8 + e9

out = {
    "status": "PASS_EXACT_FINITE_CASE_READBACK_AND_DERIVED_LINEAR_SPREAD_BOUND",
    "contract": {"sample_date": "2021-06-18", "T": "1/2", "D": "1", "F": "4221.86",
                 "unit": "C/(D F), exact-decimal-IV-defined zero-carry normalized call contract",
                 "candidate_alpha": ["13/25", "3/5", "9/10"], "fixed_curve_alpha": "0.5286",
                 "fixed_rho": "-0.7445", "fixed_nu": "0.2897", "Riccati_lambda": "0"},
    "source_sha256": {name: hashlib.sha256((BASE / name).read_bytes()).hexdigest() for name in NAMES},
    "objectives": objective_rows,
    "true_unique_winner": "13/25", "actual_pade_unique_winner": "13/25",
    "true_objective_gap_lower": exact(gap),
    "actual_pade_objective_gap_lower": exact(algorithm_gap),
    "uniform_objective_perturbation_strict_radius": exact(radius),
    "robustness_condition": "2 delta_J + epsilon_alg < true_objective_gap_lower",
    "quote_validation_cases": cases,
    "vertical_call_spread": {
        "weights": {"K4400": "1", "K4500": "-1"},
        "true_normalized_spread": interval(spread_lo, spread_hi),
        "actual_pade_normalized_spread": exact(spread_p),
        "actual_spread_error_upper_using_price_box": exact(spread_error),
        "component_triangle_error_upper": exact(e8 + e9),
        "payoff_cap_normalized": exact(Q(100) / Q("4221.86")),
        "source_of_bound": "linear interval arithmetic and standard triangle inequality; no new model or independence assumption"},
    "proof_dependency": "read-back arithmetic conditional on the sealed true-price certificates, whose continuous residual, affine exponent, Fourier strip and tail proofs are in the existing proof package",
}
(HERE / "finance-usecase-calculations.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({"status": out["status"], "true_gap": out["true_objective_gap_lower"],
                  "robustness_radius": out["uniform_objective_perturbation_strict_radius"],
                  "cases": cases, "vertical_call_spread": out["vertical_call_spread"]}, ensure_ascii=False, indent=2))
