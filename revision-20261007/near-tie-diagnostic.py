"""R10: a synthetic two-candidate tie using the released pricing objects.

The target is the exact midpoint of the frozen .52/.60 fast outputs at
the original twelve strikes. Existing complete true-price intervals are
reused, not regenerated. All objectives and decisions use Fraction.
"""
from __future__ import annotations

import hashlib
import json
import platform
import sys
import time
from datetime import datetime, timezone
from decimal import Decimal, localcontext, ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction as F
from pathlib import Path

sys.dont_write_bytecode = True
from audit_paths import release_root, evidence_directory

HERE = Path(__file__).resolve().parent
RELEASE = release_root(HERE)
EVIDENCE = evidence_directory(HERE)
FROZEN = RELEASE / "code" / "frozen"
PIN = "6a5134197db60c765ca3aea4f6cdeb2bafbb6617"
ALPHAS = [F(13, 25), F(3, 5)]
PRICE_FILES = ["f8-price-point052-v3-u64.json", "f8-price-point06-v3-u64.json"]
BUDGET_KEYS = ["grid", "true_discrete_tail", "all_finite_node_errors"]
PRICE_STATUS = "EXACT_F8_T05_PRICE_ENCLOSURES_WITH_SUPPLIED_CONTINUOUS_RESIDUAL_CERTIFICATE"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def decimal(q, places=15, upper=True):
    with localcontext() as ctx:
        ctx.prec = 160
        value = Decimal(q.numerator) / Decimal(q.denominator)
        return str(value.quantize(Decimal(1).scaleb(-places),
                                 rounding=ROUND_CEILING if upper else ROUND_FLOOR))


def square_bounds(lower, upper):
    assert lower <= upper
    return (F(0) if lower <= 0 <= upper else min(lower * lower, upper * upper),
            max(lower * lower, upper * upper))


def objective(prices, targets):
    assert len(prices) == len(targets) == 12
    row_bounds = [square_bounds(pl - mu, pu - ml)
                  for (pl, pu), (ml, mu) in zip(prices, targets)]
    denominator = 2 * len(targets)
    lower = sum((v[0] for v in row_bounds), F(0)) / denominator
    upper = sum((v[1] for v in row_bounds), F(0)) / denominator
    return {"lower": str(lower), "upper": str(upper),
            "lower_decimal_outward": decimal(lower, upper=False),
            "upper_decimal_outward": decimal(upper),
            "row_squared_residual_bounds": [[str(l), str(u)] for l, u in row_bounds]}


def decision(objectives):
    bounds = {alpha: (F(value["lower"]), F(value["upper"]))
              for alpha, value in objectives.items()}
    best = min(bounds, key=lambda alpha: bounds[alpha][1])
    least_upper = bounds[best][1]
    candidates = [alpha for alpha, (lower, _) in bounds.items() if lower <= least_upper]
    margin = min(lower for alpha, (lower, _) in bounds.items() if alpha != best) - least_upper
    overlap_lower = max(v[0] for v in bounds.values())
    overlap_upper = min(v[1] for v in bounds.values())
    separated = margin > 0
    return {"status": "CERTIFIED_UNIQUE" if separated else "UNSEPARATED",
            "strict_unique_minimizer": best if separated else None,
            "retained_candidates": candidates,
            "strict_winner_margin_lower": str(margin),
            "least_objective_upper": str(least_upper),
            "objective_intervals_overlap": overlap_lower <= overlap_upper,
            "intersection": [str(overlap_lower), str(overlap_upper)]
                if overlap_lower <= overlap_upper else None}


def file_record(path):
    return {"path": path.relative_to(RELEASE).as_posix(),
            "bytes": path.stat().st_size, "sha256": sha(path),
            "public_source": f"https://github.com/130U/certified-rough-heston-valuation/blob/{PIN}/"
                             + path.relative_to(RELEASE).as_posix()}


def main():
    started = time.perf_counter()
    utc_started = datetime.now(timezone.utc).isoformat()
    manifest_path = RELEASE / "code" / "MANIFEST.json"
    manifest = read(manifest_path)
    manifest_entries = {entry["path"]: entry for entry in manifest["artifacts"]}
    provenance_path = RELEASE / "code" / "PROVENANCE.json"
    provenance = read(provenance_path)
    original_records = {entry["public_path"]: entry for entry in provenance["records"]}
    names = ["frozen-pade-numeric-output.json", "normalized-quote-bands.json",
             "calibration-contract-finite-T05.json", *PRICE_FILES]
    for name in names:
        path = FROZEN / name
        key = "code/frozen/" + name
        expected = manifest_entries[key]
        assert sha(path) == expected["sha256"], "source SHA differs: " + name
        assert path.stat().st_size == expected["bytes"], "source length differs: " + name
        assert original_records[key]["public_sha256"] == expected["sha256"]
    pade = read(FROZEN / names[0])
    quotes = read(FROZEN / names[1])
    contract = read(FROZEN / names[2])
    quote_sha = sha(FROZEN / names[1])
    quote_original_sha = original_records["code/frozen/" + names[1]]["original_sha256"]
    contract_original_sha = original_records["code/frozen/" + names[2]]["original_sha256"]
    assert pade["status"] == "FROZEN_PADE_NUMERIC_OUTPUT_EXACT_DYADICS_NOT_TRUE_PRICE_CERTIFICATE"
    assert pade["quotes_sha256"] == quote_original_sha
    assert pade["contract_sha256"] == contract_original_sha
    assert contract["selected_row_ids"] == list(range(1, 13))
    assert set(ALPHAS) <= {F(v) for v in contract["candidate_alpha_exact"]}
    selected_quotes = [next(r for r in quotes["rows"] if r["row_id"] == i)
                       for i in range(1, 13)]
    assert [F(r["K_decimal_input"]) for r in selected_quotes] == [F(k) for k in range(3700, 4801, 100)]
    assert all(F(r["T_decimal_input"]) == F(1, 2) for r in selected_quotes)
    fast = {}
    for alpha in ALPHAS:
        item = next(c for c in pade["cover"] if F(c["alpha"]) == alpha)
        assert [r["row_id"] for r in item["rows"]] == list(range(1, 13))
        values = [F(r["normalized_call_exact_dyadic"]) for r in item["rows"]]
        assert all(v.denominator & (v.denominator - 1) == 0 for v in values)
        fast[alpha] = values
    targets = [(a + b) / 2 for a, b in zip(fast[ALPHAS[0]], fast[ALPHAS[1]])]
    # This exact row-by-row identity is the constructive tie, not a floating-point test.
    residual_identity = [fast[ALPHAS[0]][i] - targets[i] ==
                         -(fast[ALPHAS[1]][i] - targets[i]) for i in range(12)]
    assert all(residual_identity)
    prices = {}
    complete_budget_rows = {}
    for alpha, filename in zip(ALPHAS, PRICE_FILES):
        payload = read(FROZEN / filename)
        assert payload["status"] == PRICE_STATUS
        assert F(payload["alpha_lower"]) == F(payload["alpha_upper"]) == alpha
        assert payload["source_sha256"]["quotes"] == quote_original_sha
        assert payload.get("input_residual_proof_evidence") and payload.get("price_certificate")
        for key, value in [("T", F(1, 2)), ("nu", F(2897, 10000)),
                           ("rho", F(-1489, 2000)), ("kappa", F(0))]:
            assert F(payload[key]) == value
        assert [r["row_id"] for r in payload["rows"]] == list(range(1, 13))
        assert [F(r["K"]) for r in payload["rows"]] == [F(k) for k in range(3700, 4801, 100)]
        prices[alpha] = []
        complete_budget_rows[str(alpha)] = []
        for row in payload["rows"]:
            lower, upper = map(F, row["true_normalized_price"])
            ref_lower, ref_upper = map(F, row["stored_field_price"])
            assert 0 <= lower <= upper <= 1 and ref_lower <= ref_upper
            assert all(0 <= F(row["budgets"][k][0]) <= F(row["budgets"][k][1])
                       for k in BUDGET_KEYS)
            budget = sum((F(row["budgets"][k][1]) for k in BUDGET_KEYS), F(0))
            # Confirms that the consumed price interval includes every released budget,
            # with finite-node residual/omission pieces not charged a second time.
            assert lower == ref_lower - budget and upper == ref_upper + budget
            prices[alpha].append((lower, upper))
            complete_budget_rows[str(alpha)].append({
                "row_id": row["row_id"], "K": row["K"],
                "stored_field_price": row["stored_field_price"],
                "true_normalized_price": row["true_normalized_price"],
                "complete_component_upper": {k: row["budgets"][k][1] for k in BUDGET_KEYS},
                "sum_complete_component_upper": str(budget),
                "interval_reconstruction_exact": True})
    synthetic_targets = [(v, v) for v in targets]
    fast_objectives = {str(alpha): objective([(v, v) for v in fast[alpha]], synthetic_targets)
                       for alpha in ALPHAS}
    fast_value = F(fast_objectives[str(ALPHAS[0])]["lower"])
    assert all(F(v["lower"]) == F(v["upper"]) == fast_value for v in fast_objectives.values())
    true_objectives = {str(alpha): objective(prices[alpha], synthetic_targets) for alpha in ALPHAS}
    synthetic_decision = decision(true_objectives)
    assert synthetic_decision["status"] == "UNSEPARATED"
    assert synthetic_decision["objective_intervals_overlap"]
    assert synthetic_decision["retained_candidates"] == list(map(str, ALPHAS))
    # A substantive control retains actual released quote-midpoint uncertainty.
    real_targets = [(F(r["price_mid_target"]["lower_fraction"]),
                     F(r["price_mid_target"]["upper_fraction"])) for r in selected_quotes]
    real_true = {str(alpha): objective(prices[alpha], real_targets) for alpha in ALPHAS}
    real_fast = {str(alpha): objective([(v, v) for v in fast[alpha]], real_targets) for alpha in ALPHAS}
    real_decision = decision(real_true)
    assert real_decision["status"] == "CERTIFIED_UNIQUE"
    assert real_decision["strict_unique_minimizer"] == str(ALPHAS[0])
    assert decision(real_fast)["strict_unique_minimizer"] == str(ALPHAS[0])
    intervals = {alpha: f"[{value['lower_decimal_outward']}, {value['upper_decimal_outward']}]"
                 for alpha, value in true_objectives.items()}
    value_lower, value_upper = decimal(fast_value, upper=False), decimal(fast_value)
    zh = (
        "为检验候选无法分离时的实际输出，我们保留原十二个执行价3700—4800、半年期限及其余模型输入，"
        "仅取\\(\\alpha=.52,.60\\)，并构造合成目标价\\(m_i=(c_i^{\\rm fast,.52}+c_i^{\\rm fast,.60})/2\\)。"
        "原冻结快速输出按精确二进有理数解释，因此两个快速二次目标\\(J=(1/24)\\sum_i(c_i-m_i)^2\\)"
        f"逐行严格相等，其共同值位于[{value_lower}, {value_upper}]。"
        f"沿用包含连续残差、指数求值、求积、全部有限节点与真实无限尾的价格证书，模型目标区间分别为{intervals['13/25']}和{intervals['3/5']}，"
        "二者重叠。严格候选判定返回\\(\\{.52,.60\\}\\)及`UNSEPARATED`，不认证唯一胜者。"
        "以原SPX隐含波动率所定义的报价目标中点区间为对照时，同一两候选及价格证书仍严格选择\\(\\alpha=.52\\)。"
        "这个诊断是合成报价压力测试；其结论不表示市场出现平局，也不涉及连续参数加密或其余参数重新拟合。"
        "计算使用完整价格区间，复用上游证书而未重新生成它们；精确目标、逐行恒等式、输入字节身份及运行记录见`near-tie-diagnostic.json`。\n")
    en = (
        "To test an unresolved candidate decision with actual pricing outputs, we retain the original twelve strikes, 3700--4800, "
        "the six-month maturity, and the other model inputs, but restrict the candidate set to \\(\\alpha=.52,.60\\). "
        "We construct synthetic target prices \\(m_i=(c_i^{\\rm fast,.52}+c_i^{\\rm fast,.60})/2\\). "
        "Interpreting the frozen fast outputs as exact dyadics makes their quadratic objectives "
        f"\\(J=(1/24)\\sum_i(c_i-m_i)^2\\) exactly equal, row by row; the common value lies in [{value_lower}, {value_upper}]. "
        f"Using the existing complete price certificates gives model-objective intervals {intervals['13/25']} and {intervals['3/5']}, "
        "which overlap. The decision returns \\(\\{.52,.60\\}\\) with status `UNSEPARATED`, withholding a unique-winner certificate. "
        "As a control, the original SPX-IV-defined quote-midpoint intervals and the same two candidates and price certificates still certify \\(\\alpha=.52\\). "
        "This is a synthetic-quote stress test, not an observed market tie, a denser continuous-parameter experiment, or a refit of other parameters. "
        "The complete price intervals retain continuous-residual, exponent, quadrature, finite-node, and true infinite-tail errors. "
        "Upstream certificates are reused rather than regenerated; exact targets, row identities, source byte identities, and execution records appear in `near-tie-diagnostic.json`.\n")
    paragraph_paths = []
    for lang, paragraph in [("zh", zh), ("en", en)]:
        path = EVIDENCE / f"near-tie-paragraph-{lang}.md"
        path.write_text(paragraph, encoding="utf-8")
        paragraph_paths.append(path)
    runtime_platform = platform.platform()
    out = {
        "status": "PASS_SYNTHETIC_TWO_CANDIDATE_NEAR_TIE_DIAGNOSTIC",
        "diagnostic": "R10 constructive synthetic-target tie, with complete model-price uncertainty",
        "baseline_commit": PIN,
        "authoring_date": "2026-10-07",
        "scope": "Synthetic target prices only; original 12 strikes, T=1/2, fixed forward curve and other parameters; candidates .52/.60 only.",
        "not_a_market_observation": True,
        "no_continuous_parameter_or_refitting_claim": True,
        "arithmetic": "Python standard-library Fraction; all objective comparisons exact; displayed decimals rounded outward",
        "objective_definition": "J=(1/(2*12))*sum_i(c_i-m_i)^2",
        "source_manifest": file_record(manifest_path),
        "source_provenance": file_record(provenance_path),
        "historical_to_public_inputs": {
            "quotes_original_sha256": quote_original_sha,
            "quotes_public_sha256": quote_sha,
            "contract_original_sha256": contract_original_sha,
            "contract_public_sha256": sha(FROZEN / names[2]),
            "declared_changes": {name: original_records["code/frozen/" + name]["changes"]
                                 for name in names[1:3]},
            "note": "Historical embedded digests are checked against the release provenance original digests; public bytes are checked separately against the release manifest. Selected quote rows retain their exact values."},
        "sources": [file_record(FROZEN / name) for name in names],
        "method_reference": file_record(RELEASE / "code/src/calibration-interval-aggregate.py"),
        "frozen_algorithm": pade["algorithm"],
        "frozen_algorithm_runtime_versions": pade["runtime_versions"],
        "synthetic_quotes": [{"row_id": i + 1, "K": str(3700 + 100 * i),
                              "target_exact": str(v),
                              "fast52_exact": str(fast[ALPHAS[0]][i]),
                              "fast60_exact": str(fast[ALPHAS[1]][i]),
                              "opposite_signed_residuals_exact": residual_identity[i]}
                             for i, v in enumerate(targets)],
        "synthetic_fast_objectives": fast_objectives,
        "synthetic_fast_objective_difference_exact": "0",
        "synthetic_model_objectives": true_objectives,
        "synthetic_model_decision": synthetic_decision,
        "complete_price_budget_readback": complete_budget_rows,
        "original_real_quote_control": {"quote_midpoint_uncertainty_retained": True,
                                        "model_objectives": real_true, "fast_objectives": real_fast,
                                        "model_decision": real_decision, "fast_decision": decision(real_fast)},
        "upstream_continuous_residual_and_price_component_proofs_regenerated": False,
        "execution": {"utc_started": utc_started,
                      "utc_completed": datetime.now(timezone.utc).isoformat(),
                      "python_version": platform.python_version(),
                      "python_executable": sys.executable,
                      "platform": runtime_platform,
                      "source_sha256": sha(Path(__file__)),
                      "source_bytes": Path(__file__).stat().st_size,
                      "path_helper_sha256": sha(HERE / "audit_paths.py"),
                      "path_helper_bytes": (HERE / "audit_paths.py").stat().st_size,
                      "command_argv": [sys.executable, "-B", str(Path(__file__).resolve()), *sys.argv[1:]],
                      "wall_seconds": time.perf_counter() - started, "exit_status": 0},
    }
    result_path = EVIDENCE / "near-tie-diagnostic.json"
    result_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    generated = [Path(__file__), HERE / "audit_paths.py", result_path, *paragraph_paths]
    receipt = {"status": "GENERATED_ARTIFACT_BYTE_RECEIPT", "baseline_commit": PIN,
               "execution": out["execution"],
               "artifacts": [{"path": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}
                             for path in generated]}
    receipt_path = EVIDENCE / "near-tie-diagnostic-receipt.json"
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": out["status"], "synthetic_equal_fast_objective": str(fast_value),
                      "synthetic_model_objectives": {a: {k: v[k] for k in ["lower_decimal_outward", "upper_decimal_outward"]}
                                                     for a, v in true_objectives.items()},
                      "synthetic_model_decision": synthetic_decision,
                      "real_quote_control_decision": real_decision,
                      "wall_seconds": out["execution"]["wall_seconds"],
                      "receipt": receipt_path.name, "result_sha256": sha(result_path)}, indent=2))


if __name__ == "__main__":
    main()
