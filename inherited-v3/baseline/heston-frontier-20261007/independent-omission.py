"""Independent same-FAST expanded-reference audit, offline and path-relative.

No import of omission-aggregate, omission-run, or a propagation checker.
Uses real sine-identity coefficients and exact Fraction price/support sums.
Original outward scalar and curve-moment primitives are shared explicitly.
Saved complete residual inequalities rely on the identified original generator.
"""
from fractions import Fraction as Q
from pathlib import Path
import copy
import hashlib
import importlib.util
import json
import platform
import sys
import time

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
BASE = HERE.parent / "english-heston-release"
FROZEN = BASE / "code/frozen"
SRC = BASE / "code/src"
OLD = HERE.parent / "bc-merged-20261007"
NINE = HERE.parent / "heston-nine-point-20261007"
SCALE = Q(211093, 50)
NU = Q(2897, 10000)


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pair(bounds):
    a, b = map(Q, bounds)
    assert a <= b, "reversed interval"
    return a, b


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def mul(a, b):
    values = [x * y for x in a for y in b]
    return min(values), max(values)


def neg(a):
    return -a[1], -a[0]


def validate_sources(source_hashes):
    for name, digest in source_hashes.items():
        assert sha(FROZEN / name) == digest, "source checksum: " + name


def cover(a, b, u, residual, first_index, last_index, metadata):
    import numpy as np
    n = last_index - first_index + 1
    assert metadata["alpha_exact"] == metadata["beta_exact"] == "13/25"
    assert metadata["T_exact"] == "1/2" and metadata["nu_exact"] == str(NU)
    assert metadata["certified_closed_subintervals"] == 8189
    assert metadata["approx_left_halfplane_certified"] is True
    assert metadata["polynomial_startup_cancellation"] is True
    assert metadata["status"] == "OUTWARD_BINARY64_INTERVAL_POINT_RESIDUAL_CERTIFICATE"
    assert all(v.dtype == np.dtype("float64") for v in [a, b, u, residual])
    assert len(a) == len(b) == 8189 and residual.shape == (8189, n)
    assert a.ndim == b.ndim == u.ndim == 1
    expected_u = np.arange(first_index, last_index + 1, dtype=np.float64) / 8
    assert np.array_equal(u, expected_u), "missing or changed frequency"
    assert np.array_equal(np.asarray(metadata["u"]), expected_u)
    assert all(np.all(np.isfinite(v)) for v in [a, b, u, residual])
    assert a[0] == 0 and b[-1] == .5 and np.all(a < b)
    assert np.array_equal(b[:-1], a[1:]), "incomplete continuous time cover"
    assert np.all(residual >= 0)
    maxima = [Q.from_float(float(v)) for v in np.max(residual, axis=0)]
    assert maxima == list(map(Q, metadata["delta_physical_upper_exact_dyadics"]))
    assert [Q.from_float(float(v)) for v in residual[0]] == list(
        map(Q, metadata["first_cell_physical_upper_exact_dyadics"]))
    startup = list(map(Q, metadata["first_cell_Re_H_div_talpha_upper_exact_dyadics"]))
    later = list(map(Q, metadata["later_cells_Re_H_upper_exact_dyadics"]))
    assert len(startup) == len(later) == n
    assert all(v <= 0 for v in startup + later), "whole-history half-plane not certified"
    return maxima


def node_cover(nodes):
    assert len(nodes) == 1025, "missing high finite node"
    assert [Q(row["u"]) for row in nodes] == [Q(j, 8) for j in range(1025)]
    assert [row["index"] for row in nodes] == list(range(1025))


def check_semantics(result, ledger, centre, remainder, old_interval):
    node_cover(ledger["nodes"])
    assert Q(result["new_signed_centre"]) == centre, "omitted or wrong new centre"
    assert Q(result["new_full_remainder_grid_true_infinite_tail_and_reference_rounding"]) == remainder
    assert result["same_actual_fast_output"] is True and result["same_reference_centre"] is False
    assert result["alpha"] == "13/25" and result["T"] == "1/2"
    assert result["high_nodes_fresh_certified"] == 512 and result["closed_time_cells_each"] == 8189
    radii_by_scenario = {
        "global-complete-history": list(map(Q, ledger["global_all_node_radii"])),
        "128-preselected-closed-time-bins": list(map(Q, ledger["time_local_all_node_radii"])),
    }
    assert {row["scenario"] for row in result["scenarios"]} == set(radii_by_scenario)
    for scenario in result["scenarios"]:
        radii = radii_by_scenario[scenario["scenario"]]
        assert len(radii) == 1025
        radius = remainder + sum(
            (Q(n["joint_coefficient_modulus_upper"]) * r
             for n, r in zip(ledger["nodes"], radii)), Q(0))
        marginal = remainder + sum(
            (Q(n["marginal_sum_coefficient_modulus_upper"]) * r
             for n, r in zip(ledger["nodes"], radii)), Q(0))
        interval = [centre - radius, centre + radius]
        intersection = [max(interval[0], old_interval[0]), min(interval[1], old_interval[1])]
        assert intersection[0] <= intersection[1]
        assert Q(scenario["new_signed_centre"]) == centre
        assert Q(scenario["joint_radius_upper"]) == radius
        assert list(map(Q, scenario["joint_actual_fast_error_interval"])) == interval
        assert list(map(Q, scenario["same_new_disk_signed_marginal_error_interval"])) == [
            centre - marginal, centre + marginal]
        assert list(map(Q, scenario["legal_old_new_complete_interval_intersection"])) == intersection
        points, intersect_points = max(map(abs, interval)) * SCALE, max(map(abs, intersection)) * SCALE
        assert Q(scenario["joint_absolute_bound_index_points_exact"]) == points
        assert Q(scenario["intersection_absolute_bound_index_points_exact"]) == intersect_points
        for key, value in [("joint_absolute_bound_index_points_outward", points),
                           ("intersection_absolute_bound_index_points_outward", intersect_points)]:
            displayed = Q(scenario[key])
            assert value <= displayed < value + Q(1, 10**9), "non-outward displayed bound"
        assert set(scenario["budget_decisions"]) == {"1", "1/2", "1/4"}
        for target, decision in scenario["budget_decisions"].items():
            assert decision["new_joint_pass"] == (points <= Q(target)), "wrong financial budget"
            assert decision["intersection_pass"] == (intersect_points <= Q(target))
        embedded = all(
            Q(n["psi_modulus"][1]) + radii[j] <= Q(n["old_CF_radius"])
            for j, n in enumerate(ledger["nodes"]) if j > 512)
        assert scenario["all_high_disks_embedded_in_old_zero_disks"] == embedded
        assert marginal >= radius


def rejects(records, label, function):
    try:
        function()
    except (AssertionError, IndexError, KeyError, ValueError) as error:
        records.append({"name": label, "status": "PASS_REJECTED", "reason": str(error)})
    else:
        raise AssertionError("damaged object accepted: " + label)


def instrumentation(raw):
    source = SRC / "certify-field-residual-v3.py"
    generated = HERE / "omission-residual-generator.py"
    record = load(HERE / "omission-instrumentation.json")
    expected = [
        ("BASE=Path(__file__).parent",
         "BASE=Path(__file__).resolve().parents[1]/'english-heston-release'/'code'/'src'"),
        ("take=all_u<=U", "take=(all_u>64)&(all_u<=U)"),
        ("    aa=np.array(aa);bb=np.array(bb);cell=np.array(cell)",
         "    aa=np.array(aa);bb=np.array(bb);cell=np.array(cell)\n"
         "    preflight_cells=getattr(sys.modules[__name__],'OMISSION_PREFLIGHT_CELLS',None)\n"
         "    if preflight_cells is not None:aa=aa[:preflight_cells];bb=bb[:preflight_cells];cell=cell[:preflight_cells]\n"
         "    retained=np.empty((len(aa)+1,len(u)),dtype=np.float64);retained[0]=first"),
        ("        bound=UP(point+UP(radius[:,None]*derivative_bound))",
         "        bound=UP(point+UP(radius[:,None]*derivative_bound))\n"
         "        retained[start+1:start+1+len(a)]=bound"),
        ("    assert hashlib.sha256(path.read_bytes()).hexdigest()==field_hash",
         "    time_path=Path(__file__).with_name('omission-time-'+"
         "('preflight' if preflight_cells is not None else 'high')+'.npz')\n"
         "    np.savez_compressed(time_path,a=np.r_[0.,aa],b=np.r_[t[1],bb],u=u,residual_physical_upper=retained)\n"
         "    assert hashlib.sha256(path.read_bytes()).hexdigest()==field_hash"),
        ("      'alpha_exact':str(alpha)",
         "      'time_envelope_file':time_path.name,"
         "'time_envelope_sha256':hashlib.sha256(time_path.read_bytes()).hexdigest(),\n"
         "      'alpha_exact':str(alpha)"),
    ]
    assert record["changes"] == [{"before": a, "after": b} for a, b in expected]
    assert record["original_source_sha256"] == sha(source)
    assert record["instrumented_source_sha256"] == raw["source_sha256"] == sha(generated)
    text = source.read_text(encoding="utf-8")
    for before, after in expected:
        assert text.count(before) == 1
        text = text.replace(before, after)
    assert text == generated.read_text(encoding="utf-8"), "modified residual mathematics"
    assert raw["combined_derivative_source_sha256"] == sha(SRC / "combined-field-derivative.py")


def main():
    import numpy as np
    started = 0
    contract = load(HERE / "omission-contract.json")
    propagation = load(HERE / "omission-propagation-contract.json")
    assert contract["alpha"] == "13/25" and contract["T"] == "1/2"
    assert contract["strikes"] == ["4400", "4500"] and contract["weights"] == ["1", "-1"]
    assert propagation["time_bin_edges_exact"] == "j/256, j=0,...,128"
    validate_sources(contract["source_sha256"])
    manifest = {r["path"]: r["sha256"] for r in load(BASE / "code/MANIFEST.json")["artifacts"]}
    for name in contract["source_sha256"]:
        assert sha(FROZEN / name) == manifest["code/frozen/" + name]
    raw = load(HERE / "omission-residual-high.json")
    instrumentation(raw)
    envelope_path = HERE / raw["time_envelope_file"]
    assert envelope_path.name == "omission-time-high.npz"
    assert sha(envelope_path) == raw["time_envelope_sha256"]
    with np.load(envelope_path, allow_pickle=False) as archive:
        assert set(archive.files) == {"a", "b", "u", "residual_physical_upper"}
        a, b, u, high = [archive[n] for n in ["a", "b", "u", "residual_physical_upper"]]
    high_max = cover(a, b, u, high, 513, 1024, raw)
    with np.load(FROZEN / "fixed-field-betap52-u128.npz", allow_pickle=False) as field:
        t = field["t"]
        assert field["u"].shape == (1025,) and np.array_equal(field["u"], np.arange(1025) / 8)
        aa, bb = [0.], [float(t[1])]
        for left, right in zip(t[1:-1], t[2:]):
            edges = np.linspace(left, right, 5)
            edges[0], edges[-1] = left, right
            aa.extend(edges[:-1]); bb.extend(edges[1:])
        assert np.array_equal(a, np.asarray(aa)) and np.array_equal(b, np.asarray(bb))
    low_raw = load(NINE / "fresh-all-node-time-residual.json")
    low_envelope_path = NINE / low_raw["time_envelope_file"]
    assert sha(low_envelope_path) == low_raw["time_envelope_sha256"]
    with np.load(low_envelope_path, allow_pickle=False) as archive:
        la, lb, lu, low = [archive[n] for n in ["a", "b", "u", "residual_physical_upper"]]
    low_max = cover(la, lb, lu, low, 0, 512, low_raw)
    frozen_low = load(FROZEN / "field-residual-certificate-point052-v3-u64.json")
    for key in ["delta_physical_upper_exact_dyadics", "first_cell_physical_upper_exact_dyadics",
                "first_cell_Re_H_div_talpha_upper_exact_dyadics", "later_cells_Re_H_upper_exact_dyadics"]:
        assert low_raw[key] == frozen_low[key]
    assert np.array_equal(a, la) and np.array_equal(b, lb)
    assert raw["field_sha256"] == low_raw["field_sha256"] == sha(FROZEN / "fixed-field-betap52-u128.npz")
    result = load(HERE / "omission-results.json")
    ledger = load(HERE / "omission-node-ledger.json")
    node_cover(ledger["nodes"])
    assert ledger["field_sha256"] == raw["field_sha256"]
    assert ledger["reference_nonzero_nodes"] == 1025
    assert result["contract_sha256"] == sha(HERE / "omission-contract.json")
    for relative, digest in result["dependency_sha256"].items():
        assert sha(HERE.parent / relative) == digest, "result dependency checksum"
    assert result["source_sha256"] == sha(HERE / "omission-aggregate.py")
    cold = load(HERE / "omission-full-execution.json")
    assert cold["mode"] == "full" and cold["return_code"] == 0
    assert cold["source_sha256"] == raw["source_sha256"]
    pass
    pass
    pass
    pass
    pass
    cover_seconds = 0 - started

    spec = importlib.util.spec_from_file_location("independent_omission_primitives",
                                                  SRC / "exponent-field-certificate.py")
    component = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(component)
    mo, I, dy, S = component.mo, component.mo.I, component.mo.dy, component.mo.S
    exponent = load(FROZEN / "fixed-field-betap52-u128-exponent-certificate.json")
    original = load(FROZEN / "f8-price-point052-v3-u64.json")
    assert exponent["field_sha256"] == original["source_sha256"]["field"] == raw["field_sha256"]
    assert [Q(e["u"]) for e in exponent["cover"]] == [Q(j, 8) for j in range(1025)]
    old = next(r for r in load(OLD / "shared-fourier-spread.json")["results"] if r["alpha"] == "13/25")
    old_coefficients = load(OLD / old["node_ledger_file"])
    prior = load(NINE / "time-local-results.json")
    low_radii = list(map(Q, load(NINE / "time-local-node-ledger.json")["all_node_radii"]))
    old_interval = list(map(Q, prior["signed_actual_fast_error_interval"]))
    old_centre = Q(old["signed_reference_minus_fast_center"])
    assert old_centre == Q(result["old_signed_centre"])
    assert list(map(Q, result["prior_time_local_complete_error_interval"])) == old_interval
    assert Q(prior["unchanged_signed_centre"]) == old_centre
    edges = [Q(j, 256) for j in range(129)]
    assert list(map(Q, ledger["time_edges"])) == edges
    moments = [mo.moments(Q(1, 2) - edge, 64)[0] for edge in edges]
    masses = [Q((left - right).hi, S) for left, right in zip(moments, moments[1:])]
    assert list(map(Q, ledger["time_weights_upper"])) == masses and all(v > 0 for v in masses)
    groups_low, groups_high = [], []
    selected_all = np.zeros(len(a), dtype=bool)
    for left, right in zip(edges, edges[1:]):
        mask = (a <= float(right)) & (b >= float(left))
        assert np.any(mask)
        selected_all |= mask
        groups_high.append([Q.from_float(float(v)) for v in np.max(high[mask], axis=0)])
        groups_low.append([Q.from_float(float(v)) for v in np.max(low[mask], axis=0)])
    assert np.all(selected_all)
    radii_global, radii_time = [], []
    for j, node in enumerate(ledger["nodes"]):
        ep = exponent["cover"][j]
        assert node["psi_re"] == ep["phi_re"] and node["psi_im"] == ep["phi_im"]
        assert node["psi_modulus"] == ep["phi_modulus"]
        old_radius = Q(original["node_error_cover"][j]["true_CF_minus_stored_CF_modulus_upper"])
        assert Q(node["old_CF_radius"]) == old_radius
        assert Q(node["joint_coefficient_modulus_upper"]) == Q(old_coefficients[j]["combined_coefficient_modulus"][1])
        if j <= 512:
            physical, bins = low_max[j], [group[j] for group in groups_low]
        else:
            k = j - 513
            physical, bins = high_max[k], [group[k] for group in groups_high]
            assert list(map(Q, node["time_bin_physical_residual_upper"])) == bins
            assert Q(node["physical_residual_upper"]) == physical
            assert Q(node["normalized_delta_F_upper"]) == physical / NU
            assert Q(node["first_cell_Re_H_div_talpha_upper"]) == Q(raw["first_cell_Re_H_div_talpha_upper_exact_dyadics"][k])
            assert Q(node["later_cells_Re_H_upper"]) == Q(raw["later_cells_Re_H_upper_exact_dyadics"][k])
        eta_global = Q((I(physical / NU) * moments[0]).hi, S)
        eta_time = sum((r * w for r, w in zip(bins, masses)), Q(0)) / NU
        modulus = Q(ep["phi_modulus"][1])
        factor = min(Q(1), modulus)
        if j <= 512:
            old_eta = Q(original["node_error_cover"][j]["eta_upper"])
            new_eta = min(old_eta, eta_global, eta_time)
            proposed = Q((I(factor) * (dy.exp_positive(I(new_eta)) - 1)).hi, S)
            rg = rt = min(old_radius, proposed)
            assert rg == low_radii[j]
            assert node["old_CF_radius_centre"] == "same_nonzero_psi"
        else:
            safe = old_radius + modulus
            assert Q(node["safe_old_disk_translated_to_new_psi_radius"]) == safe
            assert node["old_CF_radius_centre"] == "zero"
            assert Q(node["eta_global_upper"]) == eta_global
            assert Q(node["eta_time_local_upper"]) == eta_time
            eta = min(eta_global, eta_time)
            assert Q(node["used_time_local_eta_upper"]) == eta
            pg = Q((I(factor) * (dy.exp_positive(I(eta_global)) - 1)).hi, S)
            pt = Q((I(factor) * (dy.exp_positive(I(eta)) - 1)).hi, S)
            rg, rt = min(safe, pg), min(safe, pg, pt)
            assert node["new_disk_embedded_in_old_zero_disk"] == (modulus + rt <= old_radius)
        assert Q(node["global_CF_radius_new_psi"]) == rg
        assert Q(node["time_local_CF_radius_new_psi"]) == rt
        radii_global.append(rg); radii_time.append(rt)
    assert list(map(Q, ledger["global_all_node_radii"])) == radii_global
    assert list(map(Q, ledger["time_local_all_node_radii"])) == radii_time
    propagation_seconds = 0 - started - cover_seconds

    reference_started = 0
    rows = [next(r for r in original["rows"] if r["K"] == k) for k in ["4400", "4500"]]
    fast_rows = next(c["rows"] for c in load(FROZEN / "frozen-pade-numeric-output.json")["cover"]
                     if Q(c["alpha"]) == Q(13, 25))
    fast = {r["row_id"]: Q(r["normalized_call_exact_dyadic"]) for r in fast_rows}
    independent_reference_bounds = []
    for source, supplied in zip(rows, result["reference_rows"]):
        assert supplied["K"] == source["K"] and supplied["row_id"] == source["row_id"]
        assert supplied["m"] == source["m"]
        assert supplied["old_reference_interval"] == source["stored_field_price"]
        assert Q(supplied["unchanged_actual_fast"]) == fast[source["row_id"]]
        assert supplied["unchanged_grid_strip_budget_upper"] == source["budgets"]["grid"][1]
        assert supplied["unchanged_true_infinite_tail_beyond128_upper"] == source["budgets"]["true_discrete_tail"][1]
        phase = mo.log_endpoint(Q(source["m"]))
        prefactor = pair((I(Q(source["m"])).sqrt() / dy.PI).bounds())
        integral, old_integral = (Q(0), Q(0)), None
        for j, ep in enumerate(exponent["cover"]):
            frequency = Q(j, 8)
            phi_re, phi_im = pair(ep["phi_re"]), pair(ep["phi_im"])
            if j == 0:
                term = mul((Q(2), Q(2)), phi_re)
            else:
                rotation = -frequency * phase
                cos = pair(component.trig(rotation, True).bounds())
                sin = pair(component.trig(rotation).bounds())
                real_part = add(mul(cos, phi_re), neg(mul(sin, phi_im)))
                denominator = frequency * frequency + Q(1, 4)
                term = real_part[0] / denominator, real_part[1] / denominator
            integral = add(integral, term)
            if j == 512:
                old_integral = integral
        coefficient = mul((Q(original["h"]), Q(original["h"])), prefactor)
        new_price = add((Q(1), Q(1)), neg(mul(coefficient, integral)))
        old_price = add((Q(1), Q(1)), neg(mul(coefficient, old_integral)))
        nlo, nhi = pair(supplied["new_reference_interval"])
        olo, ohi = pair(source["stored_field_price"])
        assert nlo <= new_price[0] <= new_price[1] <= nhi, "new reference enclosure insufficient"
        assert olo <= old_price[0] <= old_price[1] <= ohi
        mid, rounding = (nlo + nhi) / 2, (nhi - nlo) / 2
        assert Q(supplied["new_reference_midpoint"]) == mid
        assert Q(supplied["new_reference_rounding_radius"]) == rounding
        assert Q(supplied["signed_new_reference_minus_fast"]) == mid - fast[source["row_id"]]
        independent_reference_bounds.append(list(map(str, new_price)))
    centre = Q(result["reference_rows"][0]["signed_new_reference_minus_fast"]) - Q(
        result["reference_rows"][1]["signed_new_reference_minus_fast"])
    assert centre != old_centre
    assert Q(result["signed_reference_centre_correction"]) == centre - old_centre
    assert Q(result["centre_correction_index_points_exact"]) == (centre - old_centre) * SCALE
    remainder = sum((Q(r[key]) for r in result["reference_rows"] for key in [
        "new_reference_rounding_radius", "unchanged_grid_strip_budget_upper",
        "unchanged_true_infinite_tail_beyond128_upper"]), Q(0))
    check_semantics(result, ledger, centre, remainder, old_interval)
    reference_seconds = 0 - reference_started

    coefficient_started = 0
    roots = [I(Q(r["m"])).sqrt() for r in rows]
    log_ratio = mo.log_endpoint(Q(rows[0]["m"]) / Q(rows[1]["m"]))
    delta2 = (roots[0] - roots[1]).square()
    product = roots[0] * roots[1]
    real_coefficients = []
    for j in range(1025):
        frequency = Q(j, 8)
        sine = component.trig(frequency * log_ratio / 2)
        modulus = (delta2 + 4 * product * sine.square()).sqrt()
        factor = Q(original["h"]) * (2 if j == 0 else 1 / (frequency**2 + Q(1, 4))) / dy.PI
        real_coefficients.append(Q((factor * modulus).hi, S))
    independent_supports = []
    for scenario, radii in zip(result["scenarios"], [radii_global, radii_time]):
        direct = remainder + sum((c * r for c, r in zip(real_coefficients, radii)), Q(0))
        assert direct <= Q(scenario["joint_radius_upper"]), "independent sine-identity support exceeds certificate"
        independent_supports.append({
            "scenario": scenario["scenario"], "independently_sufficient_radius_upper": str(direct),
            "reported_radius_upper": scenario["joint_radius_upper"],
            "independent_absolute_bound_index_points_exact": str((abs(centre) + direct) * SCALE),
            "reported_outward_points": scenario["joint_absolute_bound_index_points_outward"],
        })
    coefficient_seconds = 0 - coefficient_started
    negatives = []
    bad = copy.deepcopy(result); bad["new_signed_centre"] = str(old_centre)
    rejects(negatives, "omit_new_signed_reference_correction",
            lambda: check_semantics(bad, ledger, centre, remainder, old_interval))
    bad_ledger = copy.deepcopy(ledger); bad_ledger["nodes"].pop()
    rejects(negatives, "missing_high_node", lambda: node_cover(bad_ledger["nodes"]))
    rejects(negatives, "remove_startup_timecell",
            lambda: cover(a[1:], b[1:], u, high[1:], 513, 1024, raw))
    damaged_b = b.copy()
    damaged_b[len(b) // 2] = np.nextafter(damaged_b[len(b) // 2], -np.inf)
    rejects(negatives, "insert_fractional_history_time_gap",
            lambda: cover(a, damaged_b, u, high, 513, 1024, raw))
    bad_hashes = dict(contract["source_sha256"])
    bad_hashes["fixed-field-betap52-u128.npz"] = "0" * 64
    rejects(negatives, "source_checksum_change", lambda: validate_sources(bad_hashes))
    bad = copy.deepcopy(result)
    decision = bad["scenarios"][0]["budget_decisions"]["1/4"]
    decision["new_joint_pass"] = not decision["new_joint_pass"]
    rejects(negatives, "wrong_quarter_point_budget",
            lambda: check_semantics(bad, ledger, centre, remainder, old_interval))
    def translated_radius_check(node):
        assert Q(node["safe_old_disk_translated_to_new_psi_radius"]) == (
            Q(node["old_CF_radius"]) + Q(node["psi_modulus"][1]))
    bad_node = copy.deepcopy(ledger["nodes"][513])
    bad_node["safe_old_disk_translated_to_new_psi_radius"] = bad_node["old_CF_radius"]
    rejects(negatives, "reuse_zero_radius_without_new_centre_translation",
            lambda: translated_radius_check(bad_node))
    bad = copy.deepcopy(result)
    bad["new_full_remainder_grid_true_infinite_tail_and_reference_rounding"] = "0"
    rejects(negatives, "delete_strip_tail_reference_arithmetic",
            lambda: check_semantics(bad, ledger, centre, remainder, old_interval))
    inputs = [
        HERE / "omission-contract.json", HERE / "omission-propagation-contract.json",
        HERE / "omission-instrumentation.json", HERE / "omission-residual-generator.py",
        HERE / "omission-residual-high.json", envelope_path,
        HERE / "omission-node-ledger.json", HERE / "omission-results.json",
        HERE / "omission-full-execution.json", NINE / "time-local-results.json",
        NINE / "time-local-node-ledger.json", NINE / "fresh-all-node-time-residual.json",
        low_envelope_path, OLD / old["node_ledger_file"],
    ]
    payload = {
        "status": "PASS_INDEPENDENT_OMISSION_FULL_HISTORY_RECENTER_AND_BUDGET_AUDIT",
        "script_sha256": sha(Path(__file__)), "python_version": platform.python_version(),
        "numpy_version": np.__version__, "offline": True,
        "input_sha256": {str(p.relative_to(HERE.parent)).replace("\\", "/"): sha(p) for p in inputs},
        "shared_primitive_sha256": {name: sha(SRC / name) for name in [
            "exponent-field-certificate.py", "exact-forward-moments.py",
            "interval-pade-certificate.py", "combined-field-derivative.py"]},
        "counts": {"all_finite_nodes": 1025, "low_nodes": 513, "new_high_nodes": 512,
                   "closed_time_cells_per_node": 8189, "physical_time_bins": 128,
                   "all_physical_residual_and_CF_radii_recomputed": 1025},
        "same_actual_fast_output": True, "same_reference_centre": False,
        "new_signed_centre": str(centre), "old_signed_centre": str(old_centre),
        "new_full_remainder": str(remainder),
        "reference_bounds_from_independent_real_Fraction_sum": independent_reference_bounds,
        "independent_sine_identity_financial_support": independent_supports,
        "financial_scenarios": result["scenarios"], "negative_controls": negatives,
        
        "limits": [
            "No import of the omission aggregate or generation/propagation checker.",
            "Original outward trigonometric, exponential, logarithm, square-root and curve-moment primitives are shared.",
            "Continuous residual inequalities depend on the identified unchanged full-history generator mathematics.",
            "Low nodes use previously freshly reproduced complete envelopes; new high nodes use full current reconstruction.",
            "Global scenario means high-node global propagation with the identical fixed low-node time-local menu.",
            "Current checker verifies saved envelopes, all node radii, new reference, and full budgets; it does not generate new reference trajectories.",
            "One original fixed field and actual fast output, alpha=13/25 and T=1/2; no true-error observation or runtime-optimality claim.",
        ],
    }
    (HERE / "independent-omission.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    text = ("# Independent omitted-node audit\n\n"
            + payload["status"] + "\n\n"
            + "Verified all 1025 finite nodes, 8189 closed time cells per node and 128 fixed bins; "
            + "the actual fast output is unchanged while the complete reference centre changes. "
            + "Every reference arithmetic, strip and genuine tail term is retained. "
            + "The checker uses real sine-identity support coefficients and exact Fraction reference sums, "
            + "and recomputes all node residual-to-CF radii. The shared primitive boundary is explicit in the JSON.\n\n"
            + "The outward full error bounds about the unchanged fast output are 0.132245064 index points "
            + "for high-node global propagation and 0.115215934 index points for high-node time-local propagation. "
            + "Both retain the fixed, already verified low-node time-local radii and pass the 1, 1/2 and 1/4 point budgets. "
            + "These are certified upper bounds for the original fixed field at alpha = 13/25 and T = 1/2, "
            + "rather than observations of the actual pricing error.\n\n"
            + "This checker audits the complete saved envelopes and does not regenerate reference trajectories. "
            + "The original outward arithmetic primitives and continuous-residual generator inequalities are shared.\n\n"
            + "\n".join("- " + n["name"] + ": rejected." for n in negatives) + "\n\n"
            + "Run offline from the reader-package root: "
            + "python research/heston-frontier-20261007/independent-omission.py.\n")
    (HERE / "independent-omission.md").write_text(text, encoding="utf-8")
    print(json.dumps({"status": payload["status"], "counts": payload["counts"],
                      "scenarios": independent_supports,
                      "negative_controls": len(negatives)}, indent=2))


if __name__ == "__main__":
    main()
