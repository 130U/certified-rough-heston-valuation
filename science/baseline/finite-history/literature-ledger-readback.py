"""Independent rational ledger and fixed-menu readback; no certificate generator import.

This checks accounting and optimal unit action count. It does not regenerate the
continuous residual or establish exponential/moment interval primitives.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import platform
import sys
import time

HERE = Path(__file__).resolve().parent
OLD = HERE.parent / "continuous"
BASE = HERE.parent / "reference"
SCALE = Q(211093, 50)


def load(p):
    return json.loads(p.read_text(encoding="utf-8"))


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    started = 0
    data = load(HERE / "finite-history-results.json")
    old_data = load(OLD / "shared-fourier-spread.json")
    old_by_alpha = {r["alpha"]: r for r in old_data["results"]}
    assert sha(HERE / "finite-history.py") == data["implementation_sha256"]
    assert sha(HERE / "experiment-contract.json") == data["contract_sha256"]
    input_files = {p.name: p for p in (BASE / "code/frozen").glob("*.json")}
    input_files.update({p.name: p for p in OLD.glob("shared-fourier-nodes-*.json")})
    for name, expected in data["input_sha256"].items():
        assert sha(input_files[name]) == expected, name
    mass_hi = Q(data["finite_history_forward_mass_enclosure"][1])
    records = []
    for row in data["results"]:
        old = old_by_alpha[row["alpha"]]
        source = load(BASE / "code/frozen" / old["source"])
        ledger = load(OLD / old["node_ledger_file"])
        nodes = source["node_error_cover"]
        receipt = load(HERE / row["node_receipt"])
        new = list(map(Q, receipt["all_node_radii"]))
        assert len(nodes) == len(ledger) == len(new) == 1025
        assert [Q(n["u"]) for n in nodes] == [Q(j, 8) for j in range(1025)]
        assert [Q(n["u"]) for n in ledger] == [Q(j, 8) for j in range(1025)]
        radii = [Q(n["true_CF_minus_stored_CF_modulus_upper"]) for n in nodes]
        coefficients = [Q(n["combined_coefficient_modulus"][1]) for n in ledger]
        assert all(Q(n["radius"]) == r for n, r in zip(ledger, radii))
        centre = Q(old["signed_reference_minus_fast_center"])
        remainder = Q(old["full_remainder_grid_true_tail_and_reference_rounding"])
        assert centre == Q(row["unchanged_signed_centre"])
        assert remainder == Q(row["unchanged_full_remainder"])
        direct = remainder + sum((a * r for a, r in zip(coefficients, radii)), Q(0))
        initial = max(direct, Q(old["joint_full_radius_upper"]))
        rounding_gap = initial - direct
        assert rounding_gap >= 0
        assert initial == Q(row["baseline_radius_upper"])
        assert all(Q(0) <= b <= a for a, b in zip(radii, new))
        eligible = {j for j, n in enumerate(nodes) if "delta_physical_upper" in n}
        assert len(eligible) == len(receipt["nodes"]) == row["eligible_nodes"] == 513
        remain = set(eligible)
        running = initial
        first_pass = 0 if (abs(centre) + running) * SCALE <= 1 else None
        primary_steps = row["primary_stopping_step"]
        assert primary_steps is not None
        for i, rec in enumerate(receipt["nodes"]):
            j = rec["index"]
            assert j == max(remain, key=lambda k: (coefficients[k] * radii[k], -k))
            remain.remove(j)
            assert Q(rec["u"]) == Q(j, 8)
            delta_f = Q(nodes[j]["delta_physical_upper"]) / Q(source["nu"])
            assert delta_f == Q(nodes[j]["delta_F_upper"]) == Q(rec["delta_F"])
            assert Q(nodes[j]["all_time_approximate_realpart_upper"]) <= 0
            assert Q(rec["finite_history_eta_upper"]) >= delta_f * mass_hi
            assert Q(rec["used_eta_upper"]) == min(
                Q(rec["finite_history_eta_upper"]), Q(rec["old_eta_upper"]))
            assert Q(rec["old_CF_radius"]) == radii[j]
            assert Q(rec["new_CF_radius"]) == new[j]
            running -= coefficients[j] * (radii[j] - new[j])
            assert running >= 0
            passed = (abs(centre) + running) * SCALE <= 1
            if first_pass is None and passed:
                first_pass = i + 1
            if i < primary_steps:
                tr = row["primary_trace"][i]
                assert Q(tr["radius_upper"]) == running
                assert list(map(Q, tr["signed_interval"])) == [centre - running, centre + running]
                assert Q(tr["absolute_error_upper"]) == abs(centre) + running
                assert tr["primary_budget_pass"] == passed
        assert not remain
        assert primary_steps == first_pass
        assert all(new[j] == radii[j] for j in set(range(1025)) - eligible)
        final = rounding_gap + remainder + sum((a * r for a, r in zip(coefficients, new)), Q(0))
        assert final == running == Q(row["full_finite_history_radius_upper"])
        assert list(map(Q, row["full_signed_interval"])) == [centre - final, centre + final]
        assert Q(row["full_absolute_error_upper"]) == abs(centre) + final
        pass
        records.append({
            "alpha": row["alpha"],
            "all_finite_nodes_accounted": 1025,
            "upgraded_nodes": 513,
            "primary_stopping_count": primary_steps,
            "full_bound_index_points": float((abs(centre) + final) * SCALE),
            "same_centre_same_remainder": True,
            "rounding_gap_retained": True,
            "exact_prefix_and_final_interval_match": True,
        })
        if row["alpha"] == "13/25":
            target = Q(1) / SCALE - abs(centre)
            gains = [(coefficients[j] * (radii[j] - new[j]), j) for j in eligible]
            gains.sort(key=lambda item: (-item[0], item[1]))
            running_opt = initial
            optimal = None
            first_opt = None
            last_fail = None
            opt_data = load(HERE / "optimal-upgrade-menu.json")["joint"]
            for count, (gain, j) in enumerate(gains, 1):
                if optimal is not None:
                    break
                before = running_opt
                running_opt -= gain
                trace = opt_data["trace"][count - 1]
                assert trace["index"] == j
                assert Q(trace["gain"]) == gain
                assert Q(trace["radius"]) == running_opt
                assert trace["pass"] == (running_opt <= target)
                if running_opt <= target:
                    optimal = count
                    first_opt = running_opt
                    last_fail = before
            assert optimal == opt_data["minimum_upgrades"] == 82
            assert Q(opt_data["threshold_radius"]) == target
            assert Q(opt_data["certified_radius"]) == first_opt <= target
            assert Q(opt_data["last_failed_radius"]) == last_fail > target
            records[-1]["fixed_menu_unit_count_optimum"] = optimal
            records[-1]["top81_exact_failure_top82_exact_pass"] = True
    payload = {
        "status": "PASS_INDEPENDENT_RATIONAL_LEDGER_AND_UNIT_MENU_READBACK",
        "command": "python finite-history/literature-ledger-readback.py",
        "python_version": platform.python_version(),
        "script_sha256": sha(Path(__file__)),
        "input_sha256": {name: sha(HERE / name) for name in [
            "finite-history-results.json", "optimal-upgrade-menu.json"]},
        "records": records,
        "limits": [
            "No import of finite-history.py or its supporting interval primitives.",
            "Saved moment and CF-radius certificates are inputs, not independently established here.",
            "The 82 optimum counts supplied unit upgrades after all 513 new radii are known.",
            "All-radius generation and original continuous-residual costs remain in total work.",
            "This audit does not accept or regenerate newly retained time-envelope files."
        ],
        
    }
    out = HERE / "literature-ledger-readback.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": payload["status"], "records": records,
                      "result_sha256": sha(out)}, indent=2))


if __name__ == "__main__":
    main()
