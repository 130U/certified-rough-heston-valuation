"""Recreate only the small exact model bounds; no optimization or pricing."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import time
import sys
import model_bounds as bounds

HERE = Path(__file__).resolve().parent
started = time.perf_counter()
source = HERE / "terminal767-input.json"
before = hashlib.sha256(source.read_bytes()).hexdigest()
data = json.loads(source.read_text())
lower, upper, A, b, names, records = bounds.make_P()
profiles, details = [], []
for p, omega in [(F(-1, 48), 64)] + [(F(-1, 4), -w) for w in range(8, 121, 16)]:
    profile, detail = bounds.envelope(p, omega, lower, upper)
    profiles.append(profile)
    details.append(detail)
regenerated = bounds.encode({
    "freeze_sha256": bounds.FREEZE_SHA,
    "bands": {"lower": lower, "upper": upper},
    "P_A": A, "P_b": b, "P_names": names,
    "Laplace_records": records, "profiles": profiles, "details": details,
})
assert regenerated == data, "Exact outward regeneration does not match the archive."
assert bounds.envelope(F(-1, 48), -64, lower, upper)[0] == profiles[0]
assert hashlib.sha256(source.read_bytes()).hexdigest() == before
result = {
    "status": "PASS_EXACT_MODEL_BOUND_REGENERATION",
    "probability_rows": len(A), "bands": len(lower),
    "effective_profiles": len(profiles), "profile_band_entries": len(profiles) * len(lower),
    "Laplace_recursions": len(records), "steps_per_recursion": 767,
    "outward_precision_bits": bounds.BITS,
    "matches_every_saved_field": True,
    "LP_calls": 0, "price_calls": 0, "field_candidate_calls": 0,
    "input_sha256": before,
    "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "elapsed_seconds": time.perf_counter() - started,
    "scope": "Probability and one-step profile bounds only; no candidate search or payoff pricing.",
}
if "--write" in sys.argv:
    (HERE / "input-validation.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
