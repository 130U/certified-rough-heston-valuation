"""Aggregate caller-certified model prices into conditional profile conclusions.

This program does not certify the price solver.  Its result is conditional on
the input's continuous-box and point true-price enclosures.  All calculations
and comparisons below are exact rational arithmetic.

Input schema: {"status":"CERTIFIED_PRICE_ENCLOSURES", "price_certificate":
"path or evidence identifier", "boxes":[{"alpha_lower":"0.52",
"alpha_upper":"0.53", "prices":[{"lower":"integer/integer",
"upper":"integer/integer"}, ...48 rows]}], "witnesses":[{"alpha":"0.5286",
"prices":[...48 rows]}], "near_optimal_tolerance":"0"}.
Boxes must cover [0.52,0.9] contiguously. Overlap at their endpoints is allowed.
Use the row order of normalized-quote-bands.json. No floats are accepted.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse
import hashlib
import json

BASE = Path(__file__).resolve().parent
ALPHA_L, ALPHA_U, ALPHA_C = F("0.52"), F("0.9"), F("0.6")


def rational(value):
    if not isinstance(value, str):
        raise TypeError("all numerical input bounds must be exact rational strings")
    return F(value)


def show(value):
    return f"{value.numerator}/{value.denominator}"


def source_interval(record):
    return F(record["lower_fraction"]), F(record["upper_fraction"])


def price_intervals(records, count):
    if len(records) != count:
        raise ValueError("price-vector row count differs from frozen quote contract")
    values = [(rational(row["lower"]), rational(row["upper"])) for row in records]
    if any(lo > hi for lo, hi in values):
        raise ValueError("reversed model price interval")
    return values


def square_bounds(lo, hi):
    lower = F(0) if lo <= 0 <= hi else min(lo*lo, hi*hi)
    return lower, max(lo*lo, hi*hi)


def objective_bounds(prices, quotes):
    mid_l, mid_u, band_l, band_u = F(0), F(0), F(0), F(0)
    eliminated_by_rows, certified_inside = [], True
    for index, ((pl,pu), (bl,bu,al,au,ml,mu)) in enumerate(zip(prices,quotes),1):
        lower, upper = square_bounds(pl-mu, pu-ml)
        mid_l += lower
        mid_u += upper
        assert bu <= al
        band_l += max(bl-pu, pl-au, 0)**2
        band_u += max(bu-pl, pu-al, 0)**2
        if pu < bl or pl > au:
            eliminated_by_rows.append(index)
        if pl < bu or pu > al:
            certified_inside = False
    factor = F(1,2*len(quotes))
    return {"mid_lower":mid_l*factor,"mid_upper":mid_u*factor,
            "band_lower":band_l*factor,"band_upper":band_u*factor,
            "compatibility_box_excluded_by_rows":eliminated_by_rows,
            "point_quote_compatibility_sufficient":certified_inside}


def serial_bounds(result):
    return {key: show(value) if isinstance(value,F) else value for key,value in result.items()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--contract",type=Path,default=BASE/"calibration-contract.json")
    args = parser.parse_args()
    source_bytes = (BASE / "normalized-quote-bands.json").read_bytes()
    source = json.loads(source_bytes)
    contract=json.loads(args.contract.read_text(encoding="utf-8"))
    selected=contract.get("selected_row_ids",list(range(1,49)))
    if len(set(selected))!=len(selected) or not selected:
        raise ValueError("contract row selection must be explicit, unique and nonempty")
    source_rows={row["row_id"]:row for row in source["rows"]}
    quotes = []
    for identifier in selected:
        row=source_rows[identifier]
        bl,bu = source_interval(row["normalized_bid"])
        al,au = source_interval(row["normalized_ask"])
        ml,mu = source_interval(row["price_mid_target"])
        quotes.append((bl,bu,al,au,ml,mu))
    payload_bytes = args.input.read_bytes()
    payload = json.loads(payload_bytes)
    if payload.get("status") != "CERTIFIED_PRICE_ENCLOSURES" or not payload.get("price_certificate"):
        raise ValueError("explicit external true-price certificate evidence is required")
    tolerance = rational(payload.get("near_optimal_tolerance", "0"))
    assert tolerance >= 0
    boxes = sorted(payload["boxes"],key=lambda box:rational(box["alpha_lower"]))
    if not boxes or not payload["witnesses"]:
        raise ValueError("both continuous-domain boxes and point witnesses are required")
    previous = ALPHA_L
    box_results = []
    for box in boxes:
        left,right = rational(box["alpha_lower"]),rational(box["alpha_upper"])
        if left != previous or not left < right <= ALPHA_U:
            raise ValueError("boxes must give one contiguous exact cover of the frozen alpha domain")
        previous = right
        bounds = objective_bounds(price_intervals(box["prices"],len(quotes)),quotes)
        box_results.append((left,right,bounds))
    if previous != ALPHA_U:
        raise ValueError("continuous alpha cover does not end at 0.9")
    witness_results = []
    for witness in payload["witnesses"]:
        alpha = rational(witness["alpha"])
        if not ALPHA_L <= alpha <= ALPHA_U:
            raise ValueError("witness outside the frozen domain")
        bounds = objective_bounds(price_intervals(witness["prices"],len(quotes)),quotes)
        witness_results.append((alpha,bounds))
    best = min(witness_results,key=lambda entry:entry[1]["mid_upper"])
    upper = best[1]["mid_upper"]
    lower = min(bounds["mid_lower"] for _,_,bounds in box_results)
    if lower > upper:
        raise ValueError("inconsistent model-price enclosures: global objective lower exceeds witness upper")
    retained = [(left,right) for left,right,bounds in box_results if bounds["mid_lower"] <= upper+tolerance]
    smooth_lower = min(bounds["mid_lower"] for left,right,bounds in box_results if right >= ALPHA_C)
    possible_compatible = [(left,right) for left,right,bounds in box_results
                           if not bounds["compatibility_box_excluded_by_rows"]]
    result = {
        "status":"CONDITIONAL_CALIBRATION_INTERVAL_AGGREGATION",
        "condition":"caller price certificate establishes each input enclosure for the true model, continuously over every box",
        "price_certificate":payload["price_certificate"],
        "contract_id":contract["contract_id"],
        "selected_row_ids":selected,
        "contract_sha256":hashlib.sha256(args.contract.read_bytes()).hexdigest(),
        "quotes_sha256":hashlib.sha256(source_bytes).hexdigest(),
        "price_input_sha256":hashlib.sha256(payload_bytes).hexdigest(),
        "global_minimum_objective_enclosure":{"lower":show(lower),"upper":show(upper)},
        "best_certified_witness":{"alpha":show(best[0]),"bounds":serial_bounds(best[1])},
        "near_optimal_tolerance":show(tolerance),
        "all_true_near_optimal_alpha_outer_boxes":[[show(left),show(right)] for left,right in retained],
        "all_true_near_optimal_H_outer_boxes":[[show(left-F(1,2)),show(right-F(1,2))] for left,right in retained],
        "smooth_class_alpha_ge_0.6_lower_bound":show(smooth_lower),
        "smooth_class_excluded_for_true_near_optimal_set":smooth_lower > upper+tolerance,
        "exact_quote_compatibility_outer_boxes":[[show(left),show(right)] for left,right in possible_compatible],
        "boxes":[{"alpha":[show(left),show(right)],"bounds":serial_bounds(bounds)} for left,right,bounds in box_results],
        "witnesses":[{"alpha":show(alpha),"bounds":serial_bounds(bounds)} for alpha,bounds in witness_results],
        "no_parameter_distance_or_unique_identification_claim":True,
        "solver_certificate_validated_by_this_script":False,
    }
    args.output.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":result["status"],"global_minimum_objective_enclosure":result["global_minimum_objective_enclosure"],
          "retained_box_count":len(retained),"smooth_class_excluded":result["smooth_class_excluded_for_true_near_optimal_set"]},indent=2))


if __name__ == "__main__":
    main()
