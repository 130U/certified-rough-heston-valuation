"""Independent cell/bin ledger and full financial readback.

Does not import time-local-propagation.py or check-time-envelope.py.
Shares the original exact forward-moment and dyadic exponential primitives,
whose identities and limited independence are explicitly reported.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json
import platform
import sys
import time

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
BASE = HERE.parent / "english-heston-release"
OLD = HERE.parent / "bc-merged-20261007"
FROZEN = BASE / "code/frozen"
SCALE = Q(211093, 50)


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_cover(a, b, u, bounds, expected_maxima, expected_cells):
    import numpy as np
    assert all(v.dtype == np.dtype("float64") for v in (a, b, u, bounds))
    assert a.ndim == b.ndim == u.ndim == 1
    assert len(a) == len(b) == expected_cells
    assert bounds.shape == (expected_cells, 513)
    assert np.array_equal(u, np.arange(513, dtype=np.float64) / 8)
    assert all(np.all(np.isfinite(v)) for v in (a, b, u, bounds))
    assert a[0] == 0 and b[-1] == .5
    assert np.all(a < b)
    assert np.array_equal(b[:-1], a[1:])
    assert np.all(bounds >= 0)
    maxima = [str(Q.from_float(float(v))) for v in np.max(bounds, axis=0)]
    assert maxima == expected_maxima


def group_bins(a, b, bounds, edges):
    import numpy as np
    assert edges == [Q(j, 256) for j in range(129)]
    grouped = []
    all_selected = np.zeros(len(a), dtype=bool)
    counts = []
    for left, right in zip(edges, edges[1:]):
        selected = (a <= float(right)) & (b >= float(left))
        assert np.any(selected)
        all_selected |= selected
        counts.append(int(np.sum(selected)))
        grouped.append([Q.from_float(float(v)) for v in np.max(bounds[selected], axis=0)])
    assert np.all(all_selected)
    assert len(grouped) == 128
    return grouped, counts


def validate_weights(weights, expected_weights, full_mass, baseline_v0):
    assert len(weights) == len(expected_weights) == 128
    for supplied, expected in zip(weights, expected_weights):
        low, high = map(Q, supplied)
        e_low, e_high = expected
        assert Q(0) < low <= e_low <= e_high <= high
        assert high >= baseline_v0 / 256
    assert sum((Q(w[0]) for w in weights), Q(0)) <= Q(full_mass[1])
    assert sum((Q(w[1]) for w in weights), Q(0)) >= Q(full_mass[0])


def rejects(negatives, name, function):
    try:
        function()
    except (AssertionError, IndexError) as error:
        negatives.append({"name": name, "status": "PASS_REJECTED", "reason": str(error)})
    else:
        raise AssertionError("damaged data accepted: " + name)


def menu_certificate(label, coefficients, old_radii, new_radii, centre, remainder, baseline):
    """Unit-count optimality witness for the supplied once-only 513-action menu."""
    gains = [(coefficients[j] * (old_radii[j] - new_radii[j]), j) for j in range(513)]
    assert all(gain >= 0 for gain, j in gains)
    gains.sort(key=lambda item: (-item[0], item[1]))
    ranks = {j: rank for rank, (gain, j) in enumerate(gains, 1)}
    actions = [
        {"index": j, "u": str(Q(j, 8)), "rank": ranks[j],
         "coefficient_modulus_upper": str(coefficients[j]),
         "old_CF_radius": str(old_radii[j]), "new_CF_radius": str(new_radii[j]),
         "certified_radius_decrement": str(coefficients[j] * (old_radii[j] - new_radii[j]))}
        for j in range(513)
    ]
    radius = baseline
    trace = []
    for count, (gain, j) in enumerate(gains, 1):
        previous = radius
        radius -= gain
        passed = (abs(centre) + radius) * SCALE <= 1
        trace.append({"step": count, "index": j, "u": str(Q(j, 8)),
                      "decrement": str(gain), "radius_upper": str(radius),
                      "absolute_bound_index_points_exact": str((abs(centre) + radius) * SCALE),
                      "budget_pass": passed})
        if passed:
            assert (abs(centre) + previous) * SCALE > 1
            return {
                "label": label,
                "minimum_unit_upgrade_count": count,
                "new_radius_precomputation_count": 513,
                "baseline_radius_upper": str(baseline),
                "unchanged_signed_centre": str(centre), "unchanged_full_remainder": str(remainder),
                "budget_index_points": "1",
                "last_failed_prefix_count": count - 1,
                "last_failed_full_signed_interval": [str(centre - previous), str(centre + previous)],
                "last_failed_absolute_bound_index_points_exact": str((abs(centre) + previous) * SCALE),
                "first_pass_full_signed_interval": [str(centre - radius), str(centre + radius)],
                "first_pass_absolute_bound_index_points_exact": str((abs(centre) + radius) * SCALE),
                "all_513_available_action_decrements": actions,
                "complete_ranked_action_indices": [j for gain, j in gains],
                "prefix_trace_through_first_pass": trace,
                "scope": "Exact minimum unit count for this supplied once-only menu after all 513 new radii are known. Fixed signed centre and full remainder; no runtime or residual-generation optimality."
            }
    raise AssertionError("expected supplied time-local menu to certify one-point budget")


def main():
    import numpy as np
    started = 0
    contract = load(HERE / "time-local-contract.json")
    assert contract["partition"]["bins"] == 128
    assert contract["partition"]["edge_formula"] == "j/256 for j=0,...,128"
    fresh = load(HERE / "fresh-all-node-time-residual.json")
    assert fresh["alpha_exact"] == fresh["beta_exact"] == "13/25"
    assert fresh["T_exact"] == "1/2" and fresh["nu_exact"] == "2897/10000"
    assert fresh["approx_left_halfplane_certified"] is True
    envelope = HERE / fresh["time_envelope_file"]
    assert sha(envelope) == fresh["time_envelope_sha256"]
    generated = HERE / "continuous-residual-with-time.py"
    assert sha(generated) == fresh["source_sha256"]
    assert sha(FROZEN / "fixed-field-betap52-u128.npz") == fresh["field_sha256"]
    frozen_residual = load(FROZEN / "field-residual-certificate-point052-v3-u64.json")
    for key in ["delta_physical_upper_exact_dyadics",
                "first_cell_physical_upper_exact_dyadics",
                "first_cell_Re_H_div_talpha_upper_exact_dyadics",
                "later_cells_Re_H_upper_exact_dyadics"]:
        assert fresh[key] == frozen_residual[key]
    with np.load(envelope, allow_pickle=False) as archive:
        assert set(archive.files) == {"a", "b", "u", "residual_physical_upper"}
        a, b, u, bounds = [archive[name] for name in
                           ("a", "b", "u", "residual_physical_upper")]
    expected_maxima = frozen_residual["delta_physical_upper_exact_dyadics"]
    validate_cover(a, b, u, bounds, expected_maxima, fresh["certified_closed_subintervals"])
    assert [str(Q.from_float(float(v))) for v in bounds[0]] == fresh[
        "first_cell_physical_upper_exact_dyadics"]
    weights_data = load(HERE / "time-local-weights.json")
    node_data = load(HERE / "time-local-node-ledger.json")
    result = load(HERE / "time-local-results.json")
    edges = list(map(Q, weights_data["physical_time_edges"]))
    grouped, counts = group_bins(a, b, bounds, edges)
    assert counts == weights_data["intersecting_source_cell_counts"]
    assert weights_data["source_cells"] == len(a)
    assert weights_data["all_source_cells_included"] is True
    assert weights_data["contract_sha256"] == sha(HERE / "time-local-contract.json")
    for key, path in {
        "contract": HERE / "time-local-contract.json",
        "time_envelope": envelope,
        "fresh_residual_record": HERE / "fresh-all-node-time-residual.json",
        "frozen_price": FROZEN / "f8-price-point052-v3-u64.json",
        "frozen_exponents": FROZEN / "fixed-field-betap52-u128-exponent-certificate.json",
        "forward_moment_implementation": BASE / "code/src/exact-forward-moments.py",
        "implementation": HERE / "time-local-propagation.py",
    }.items():
        assert result["dependencies"][key] == sha(path)
    assert result["alpha"] == "13/25" and result["T"] == "1/2"
    assert result["strikes"] == ["4400", "4500"] and result["weights"] == ["1", "-1"]
    assert set(result["budget_checks"]) == {"1", "1/2", "1/4"}
    bin_seconds = 0 - started

    moment_start = 0
    module_path = BASE / "code/src/exact-forward-moments.py"
    spec = importlib.util.spec_from_file_location("independent_original_moments", module_path)
    mo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mo)
    dy, I, S = mo.dy, mo.I, mo.S
    assert mo.V0 == Q(131, 5000) and mo.THETA == Q(721, 10000)
    assert mo.ALPHA0 == Q(2643, 5000) and mo.LAMBDA == Q(5037, 10000)
    moments = [mo.moments(Q(1, 2) - edge, 64)[0] for edge in edges]
    expected_weights = []
    for left, right in zip(moments, moments[1:]):
        diff = left - right
        expected_weights.append([max(Q(0), Q(diff.lo, S)), Q(diff.hi, S)])
    full_mass = mo.moments(Q(1, 2), 64)[0]
    assert weights_data["curve_mass_enclosure"] == full_mass.bounds()
    validate_weights(weights_data["bin_curve_mass_enclosures"], expected_weights,
                     full_mass.bounds(), mo.V0)
    moment_seconds = 0 - moment_start

    manifest = {r["path"]: r["sha256"] for r in load(BASE / "code/MANIFEST.json")["artifacts"]}
    for name in ["f8-price-point052-v3-u64.json",
                 "fixed-field-betap52-u128-exponent-certificate.json",
                 "field-residual-certificate-point052-v3-u64.json",
                 "fixed-field-betap52-u128.npz"]:
        assert sha(FROZEN / name) == manifest["code/frozen/" + name]
    source = load(FROZEN / "f8-price-point052-v3-u64.json")
    exponents = load(FROZEN / "fixed-field-betap52-u128-exponent-certificate.json")
    exponent_by_u = {Q(n["u"]): n for n in exponents["cover"]}
    old = next(r for r in load(OLD / "shared-fourier-spread.json")["results"]
               if r["alpha"] == "13/25")
    old_ledger = load(OLD / old["node_ledger_file"])
    nodes = source["node_error_cover"]
    assert len(nodes) == len(old_ledger) == 1025
    old_radii = [Q(n["true_CF_minus_stored_CF_modulus_upper"]) for n in nodes]
    coefficients = [Q(n["combined_coefficient_modulus"][1]) for n in old_ledger]
    assert [Q(n["radius"]) for n in old_ledger] == old_radii
    assert [Q(n["u"]) for n in nodes] == [Q(j, 8) for j in range(1025)]
    assert len(node_data["nodes"]) == 513
    global_result = next(r for r in load(HERE / "finite-history-results.json")["results"]
                         if r["alpha"] == "13/25")
    global_radii = list(map(Q, load(HERE / global_result["node_receipt"])["all_node_radii"]))
    new_radii = list(map(Q, node_data["all_node_radii"]))
    assert len(new_radii) == len(global_radii) == 1025
    nu = Q(source["nu"])
    weighted_checks = []
    for j, row in enumerate(node_data["nodes"]):
        assert Q(row["u"]) == Q(j, 8)
        residual_bins = [grouped[bj][j] for bj in range(128)]
        assert list(map(Q, row["time_bin_residual_upper_exact_dyadics"])) == residual_bins
        eta_upper = sum((r * w[1] for r, w in zip(residual_bins, expected_weights)), Q(0)) / nu
        stored_eta = Q(row["time_local_eta_upper"])
        assert stored_eta >= eta_upper
        physical = Q(nodes[j]["delta_physical_upper"])
        assert physical == Q(row["physical_complete_residual_upper"])
        delta_f = physical / nu
        assert delta_f == Q(nodes[j]["delta_F_upper"])
        assert Q(nodes[j]["all_time_approximate_realpart_upper"]) <= 0
        global_eta = Q((I(delta_f) * full_mass).hi, S)
        assert global_eta == Q(row["global_finite_history_eta_upper"])
        old_eta = Q(nodes[j]["eta_upper"])
        assert old_eta == Q(row["old_eta_upper"])
        eta = min(old_eta, global_eta, stored_eta)
        assert eta == Q(row["used_eta_upper"])
        modulus = min(Q(1), Q(exponent_by_u[Q(j, 8)]["phi_modulus"][1]))
        independent_global = I(modulus) * (
            dy.exp_positive(I(min(old_eta, global_eta))) - 1)
        assert global_radii[j] == min(old_radii[j], Q(independent_global.hi, S))
        proposed = I(modulus) * (dy.exp_positive(I(eta)) - 1)
        radius = min(old_radii[j], global_radii[j], Q(proposed.hi, S))
        assert radius == new_radii[j] == Q(row["time_local_CF_radius"])
        assert Q(row["old_CF_radius"]) == old_radii[j]
        assert Q(row["global_finite_history_CF_radius"]) == global_radii[j]
        weighted_checks.append(stored_eta == eta_upper)
    assert all(new_radii[j] == old_radii[j] for j in range(513, 1025))
    assert all(global_radii[j] == old_radii[j] for j in range(513, 1025))
    centre = Q(old["signed_reference_minus_fast_center"])
    remainder = Q(old["full_remainder_grid_true_tail_and_reference_rounding"])
    direct = remainder + sum((c * r for c, r in zip(coefficients, old_radii)), Q(0))
    baseline = max(direct, Q(old["joint_full_radius_upper"]))
    gap = baseline - direct
    assert gap >= 0
    radius = gap + remainder + sum((c * r for c, r in zip(coefficients, new_radii)), Q(0))
    global_radius = gap + remainder + sum((c * r for c, r in zip(coefficients, global_radii)), Q(0))
    assert centre == Q(result["unchanged_signed_centre"])
    assert remainder == Q(result["unchanged_full_remainder"])
    assert gap == Q(result["fixed_interval_rounding_gap"])
    assert baseline == Q(result["old_full_radius_upper"])
    assert global_radius == Q(result["global_finite_history_full_radius_upper"])
    assert global_radius == Q(global_result["full_finite_history_radius_upper"])
    assert radius == Q(result["time_local_full_radius_upper"]) <= global_radius <= baseline
    assert list(map(Q, result["signed_actual_fast_error_interval"])) == [centre - radius, centre + radius]
    absolute = abs(centre) + radius
    assert Q(result["absolute_error_upper"]) == absolute
    points = absolute * SCALE
    assert Q(result["absolute_error_upper_index_points_exact"]) == points
    displayed = Q(result["absolute_error_upper_index_points_display_outward"])
    assert points <= displayed < points + Q(1, 10**9)
    for target, decision in result["budget_checks"].items():
        assert decision["pass"] == (points <= Q(target))
        assert Q(decision["certified_margin_index_points"]) == Q(target) - points
    pass
    menu_started = 0
    time_menu = menu_certificate("shared_Fourier_time_local", coefficients, old_radii, new_radii,
                                 centre, remainder, baseline)
    rows = [next(row for row in source["rows"] if Q(row["K"]) == strike)
            for strike in [Q(4400), Q(4500)]]
    root_m = [I(Q(row["m"])).sqrt() for row in rows]
    marginal_coefficients = []
    for j in range(1025):
        frequency = Q(j, 8)
        factor = Q(source["h"]) * (2 if j == 0 else 1 / (frequency**2 + Q(1, 4))) / dy.PI
        marginal_coefficients.append(max(
            Q((factor * (root_m[0] + root_m[1])).hi, S), coefficients[j]))
    marginal_baseline = remainder + sum(
        (a_m * radius for a_m, radius in zip(marginal_coefficients, old_radii)), Q(0))
    marginal_time_menu = menu_certificate(
        "same_centre_signed_marginal_time_local", marginal_coefficients, old_radii, new_radii,
        centre, remainder, marginal_baseline)
    menu_seconds = 0 - menu_started

    negatives = []
    damaged_b = b.copy()
    damaged_b[len(b) // 2] = np.nextafter(damaged_b[len(b) // 2], -np.inf)
    rejects(negatives, "badcell_time_gap", lambda: validate_cover(
        a, damaged_b, u, bounds, expected_maxima, len(a)))
    rejects(negatives, "remove_startup_cell", lambda: validate_cover(
        a[1:], b[1:], u, bounds[1:], expected_maxima, len(a)))
    rejects(negatives, "removebin", lambda: validate_weights(
        weights_data["bin_curve_mass_enclosures"][:-1], expected_weights, full_mass.bounds(), mo.V0))
    wrong_weights = [[str(Q(low) - mo.V0 / 256), str(Q(high) - mo.V0 / 256)]
                     for low, high in weights_data["bin_curve_mass_enclosures"]]
    rejects(negatives, "omitstartup_weight_mass", lambda: validate_weights(
        wrong_weights, expected_weights, full_mass.bounds(), mo.V0))
    constant_curve_identity = {"V0": "1", "R_physical": "1", "nu": "1", "T": "1/2",
                               "correct_eta0_bound": "1/2", "eta0_if_startup_omitted": "0"}
    files = ["time-local-contract.json", "fresh-all-node-time-residual.json",
             fresh["time_envelope_file"], "time-local-weights.json", "time-local-node-ledger.json",
             "time-local-results.json", "finite-history-results.json", "theory-research.md",
             global_result["node_receipt"]]
    payload = {
        "status": "PASS_INDEPENDENT_TIME_LOCAL_POSITIVE_WEIGHT_AND_FULL_BUDGET_CHECK",
        "command": "python heston-nine-point-20261007/independent-time-local.py",
        "python_version": platform.python_version(),
        "script_sha256": sha(Path(__file__)),
        "input_sha256": {name: sha(HERE / name) for name in files},
        "shared_primitive_sha256": {str(module_path.relative_to(BASE)): sha(module_path),
                                    "code/src/interval-pade-certificate.py":
                                        sha(BASE / "code/src/interval-pade-certificate.py")},
        "counts": {"frequencies": 513, "closed_cells": len(a), "bins": 128,
                   "all_finite_nodes": 1025, "positive_weights": 128,
                   "weighted_eta_checked": 513, "weighted_eta_exact_equal": sum(weighted_checks)},
        "all_closed_intersecting_cells_included": True,
        "positive_startup_mass_included": True,
        "same_output_same_centre_same_complete_remainder": True,
        "old_global_time_three_way_eta_min_verified": True,
        "all_new_CF_radii_independently_recomputed_using_shared_primitives": True,
        "signed_error_interval": list(map(str, [centre - radius, centre + radius])),
        "absolute_error_index_points_exact": str(points),
        "absolute_error_index_points_outward": result["absolute_error_upper_index_points_display_outward"],
        "budget_decisions": result["budget_checks"],
        "fixed_precomputed_time_local_menu": time_menu,
        "fixed_precomputed_time_local_signed_marginal_menu": marginal_time_menu,
        "menu_cost_caveat": "All 513 eligible radii are accounted for before fixed-menu ranking. This is an action-count result for an already available menu; it is not a measured execution-cost or general runtime-optimality claim.",
        "negative_controls": negatives,
        "analytic_startup_counterexample": constant_curve_identity,
        
        "limits": ['No import of math-agent propagation or time-envelope checker.', 'Original forward-moment and exponential interval primitives are shared.', 'Continuous residual inequalities depend on the identified unchanged generator mathematics.', 'This validates saved continuous-cell envelope coverage and propagation, not an independent transcendental residual implementation.', 'Only alpha=13/25, T=1/2, original fixed field and original actual Padé outputs.']
    }
    output = HERE / "independent-time-local.json"
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": payload["status"], "counts": payload["counts"],
                      "absolute_error_index_points_outward":
                          payload["absolute_error_index_points_outward"],
                      "fixed_time_menu": {k: v for k, v in time_menu.items() if k not in [
                          "all_513_available_action_decrements", "complete_ranked_action_indices",
                          "prefix_trace_through_first_pass"]},
                      "fixed_time_signed_marginal_menu": {k: v for k, v in marginal_time_menu.items() if k not in [
                          "all_513_available_action_decrements", "complete_ranked_action_indices",
                          "prefix_trace_through_first_pass"]},
                      "result_sha256": sha(output)}, indent=2))


if __name__ == "__main__":
    main()
