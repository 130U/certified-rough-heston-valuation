"""Check exact receipt arithmetic and mode-box aggregation without field regeneration."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import time
import sys

HERE = Path(__file__).resolve().parent
started = 0
read = lambda name: json.loads((HERE / name).read_text(encoding="utf-8-sig"))
sha = lambda name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
provenance = read("provenance.json")
names = ["field-result.json", "field-cell-integrals.json", "field-independent-readback.json"]
before = {name: sha(name) for name in names}
for name in names:
    assert before[name] == provenance["files"][name]["portable_sha256"]
r = read(names[0])
c = read(names[1])
independent = read(names[2])
assert r["cell_integrals_sha256"] == sha(names[1])
assert r["candidate_sha256"] == c["candidate_sha256"] == independent["candidate_sha256"] == provenance["not_shipped"]["field-candidate"]["sha256"]
assert r["source_sha256"] == c["source_sha256"] == provenance["source_identities"]["field-generator"]
assert c["normalization"] == "exp(-9/200)/2; original centers already contain endpoint weights"
assert c["fixed_state_shape"] == {"m": 0, "y": "0", "D": "0", "v": "9/200"}
assert len(c["cells"]) == 8

def absolute_lower(lo, hi):
    assert lo <= hi
    return F(0) if lo <= 0 <= hi else min(abs(lo), abs(hi))

box_lower = F(0)
for i, cell in enumerate(c["cells"]):
    assert cell["cell"] == i
    assert cell["physical_time"] == [str(F(i, 96)), str(F(i + 1, 96))]
    assert len(cell["mode_integrals"]) == 385
    sum_lo = sum_hi = F(0)
    for k, mode in enumerate(cell["mode_integrals"]):
        assert mode["k"] == k
        rl, ru = map(F, mode["real"])
        il, iu = map(F, mode["imag"])
        assert rl <= ru and il <= iu
        sum_lo += rl
        sum_hi += ru
    theta_lo, theta_hi = map(F, cell["theta0_integral"])
    assert theta_lo <= theta_hi
    assert not (theta_hi < sum_lo or theta_lo > sum_hi)
    assert F(cell["theta0_absolute_lower"]) == absolute_lower(theta_lo, theta_hi)
    box_lower += absolute_lower(sum_lo, sum_hi)

theta_lower = sum((F(cell["theta0_absolute_lower"]) for cell in c["cells"]), F(0))
parseval_lower = sum((F(cell["parseval_norm_lower"]) for cell in c["cells"]), F(0))
assert theta_lower == F(r["arithmetic_theta0_lower"])
assert parseval_lower == F(r["arithmetic_parseval_lower"])
geometry = F(r["geometric_upper"])
L0 = theta_lower - geometry
L1 = parseval_lower - geometry
L = max(L0, L1)
assert L0 == F(r["theta0_whole_lower"])
assert L1 == F(r["parseval_whole_lower"])
assert L == F(r["whole_lower"])
assert L > F(1, 1000)
assert box_lower - geometry >= F("0.003407444052031154")
scaled = F(2399, 1200) * L
assert scaled == F(r["same_weight_positive_payment_lower"])
assert scaled < F(r["original_conversion_balance"])
for key in ("theta0_whole_lower", "parseval_whole_lower", "whole_lower", "same_weight_positive_payment_lower"):
    lo, hi = map(F, r[key + "_outward18"])
    assert lo <= F(r[key]) <= hi
assert r["status"] == "FAIL_SELECTED_INTEGRATED_PDE_CONTRACT_ONLY"
assert r["uniform_integrated_contract_failed"] is True
assert r["same_weight_positive_payment_exceeds_balance"] is False
assert independent["status"] == "INDEPENDENT_NECESSARY_SCREEN_VERIFIED"
assert independent["checked_mode_cells"] == 3080
assert independent["checked_time_pieces"] == 64
assert independent["precision_bits"] == 384
assert independent["theta0_lower_outward18"] == r["theta0_whole_lower_outward18"]
assert independent["sufficient_conversion_upper"] is None
assert independent["actual_bias_lower_bound"] is None
assert before == {name: sha(name) for name in names}
result = {
    "status": "PASS_EXACT_FIELD_RECEIPT_AND_MODE_BOX_AGGREGATION",
    "scope": "Exact saved integral arithmetic. The archived 384-bit direct integration is not rerun; the coefficient bank is not shipped.",
    "inputs": before,
    "mode_cells": 3080, "original_time_pieces": 64,
    "whole_lower_exact": str(L),
    "independent_mode_box_whole_lower_exact": str(box_lower - geometry),
    "verified_display_lower": "0.003407444052031154",
    "selected_PDE_allocation_rejected": True,
    "complete_balance_rejected_by_this_lower_bound": False,
    "actual_bias_lower_bound": None,
    "field_candidate_calls": 0, "expm_calls": 0, "price_calls": 0,
    "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    
}
if "--write" in sys.argv:
    (HERE / "field-validation.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
