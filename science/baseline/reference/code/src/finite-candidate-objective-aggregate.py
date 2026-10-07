"""Exact objective intervals over a frozen finite alpha candidate contract.

Every required candidate needs a completed true-price certificate. A pair
contract is distinct from the three-candidate contract and from a continuous
profile. No floating-point objective comparison or default missing candidate.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, importlib.util, json, sys

BASE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("continuous_aggregate",BASE/"calibration-interval-aggregate.py")
maths=importlib.util.module_from_spec(spec);spec.loader.exec_module(maths)

def digest(blob):return hashlib.sha256(blob).hexdigest()
def rational(v):
    if not isinstance(v,str):raise TypeError("exact rational string required")
    return F(v)
def show(v):return str(v)

def analyze(candidates,quotes,tolerance=F(0)):
    """Pure finite-set algebra, conditional on the supplied true-price bounds."""
    if tolerance<0 or not candidates:raise ValueError("nonnegative tolerance and candidates required")
    results={alpha:maths.objective_bounds(prices,quotes) for alpha,prices in candidates.items()}
    lower=min(r["mid_lower"] for r in results.values())
    best=min(results,key=lambda a:results[a]["mid_upper"])
    upper=results[best]["mid_upper"]
    if lower>upper:raise ValueError("inconsistent objective enclosures")
    retained=[a for a,r in results.items() if r["mid_lower"]<=upper+tolerance]
    inner=[a for a,r in results.items() if r["mid_upper"]-lower<=tolerance]
    competitors=[r["mid_lower"] for a,r in results.items() if a!=best]
    margin=min(competitors)-upper if competitors else None
    unique=best if margin is not None and margin>0 else None
    smooth=[r["mid_lower"] for a,r in results.items() if a>=F(3,5)]
    smooth_lower=min(smooth) if smooth else None
    compatible=[a for a,r in results.items() if not r["compatibility_box_excluded_by_rows"]]
    inside=[a for a,r in results.items() if r["point_quote_compatibility_sufficient"]]
    return {"results":results,"global_lower":lower,"global_upper":upper,
        "best_witness":best,"near_optimal_outer":retained,"near_optimal_inner":inner,
        "strict_unique_minimizer":unique,"strict_winner_margin_lower":margin,
        "smooth_lower":smooth_lower,
        "smooth_near_optimal_class_excluded":smooth_lower is not None and smooth_lower>upper+tolerance,
        "compatible_outer":compatible,"compatible_inner":inside}

def main():
    sys.stdout.reconfigure(encoding="utf8")
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract",type=Path,default=BASE/"calibration-contract-finite-T05.json")
    parser.add_argument("--prices",type=Path,nargs="+",required=True)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--near-optimal-tolerance",default="0")
    parser.add_argument("--pade-output",type=Path,
        help="frozen exact dyadic outputs of the specified self-written numerical Pade workflow; never true-price input")
    args=parser.parse_args()
    cb=args.contract.read_bytes();contract=json.loads(cb)
    required=[rational(a) for a in contract["candidate_alpha_exact"]]
    profile=[rational(a) for a in contract["profile_parameters"]["vary"]["alpha_finite_candidates"]]
    if required!=profile or len(set(required))!=len(required) or len(required)<2:
        raise ValueError("contract finite candidate definitions differ")
    if not all(F(13,25)<=a<=F(9,10) for a in required):
        raise ValueError("candidate outside frozen admissible model range")
    selected=contract["selected_row_ids"]
    if selected!=list(range(1,13)):raise ValueError("this implementation requires the frozen twelve T=.5 rows")
    qb=(BASE/"normalized-quote-bands.json").read_bytes();source=json.loads(qb)
    quoted={r["row_id"]:r for r in source["rows"]}
    quotes=[]
    for identifier in selected:
        row=quoted[identifier]
        if F(row["T_decimal_input"])!=F(1,2):raise ValueError("quote maturity differs")
        intervals=[maths.source_interval(row[k]) for k in ["normalized_bid","normalized_ask","price_mid_target"]]
        quotes.append(tuple(v for interval in intervals for v in interval))
    candidates={};evidence={}
    for path in args.prices:
        blob=path.read_bytes();payload=json.loads(blob)
        if payload.get("status")!="EXACT_F8_T05_PRICE_ENCLOSURES_WITH_SUPPLIED_CONTINUOUS_RESIDUAL_CERTIFICATE":
            raise ValueError("a completed F8 true-price certificate is required for every candidate")
        if not payload.get("price_certificate") or not payload.get("input_residual_proof_evidence"):
            raise ValueError("price proof evidence is missing")
        if payload["source_sha256"]["quotes"]!=digest(qb):
            raise ValueError("price input used different frozen quotes")
        alpha=rational(payload["alpha_lower"])
        if alpha!=rational(payload["alpha_upper"]):
            raise ValueError("finite candidate input must certify its exact point alpha")
        if alpha not in required or alpha in candidates:
            raise ValueError("unexpected or duplicate candidate")
        for key,value in [("T",F(1,2)),("nu",F(2897,10000)),("rho",F(-1489,2000)),("kappa",F(0))]:
            if rational(payload[key])!=value:raise ValueError("price input fixed profile differs")
        if [row["row_id"] for row in payload["rows"]]!=selected:
            raise ValueError("price certificate row ordering differs")
        prices=[tuple(map(rational,row["true_normalized_price"])) for row in payload["rows"]]
        if len(prices)!=len(quotes) or any(pl>pu or pl<0 or pu>1 for pl,pu in prices):
            raise ValueError("invalid normalized true-price intervals")
        candidates[alpha]=prices
        evidence[alpha]={"path":path.name,"sha256":digest(blob),"price_certificate":payload["price_certificate"],
            "component_source_sha256":payload["source_sha256"]}
    if set(candidates)!=set(required):
        missing=sorted(set(required)-set(candidates))
        raise ValueError("required candidate price certificate missing: "+",".join(map(str,missing)))
    candidates={a:candidates[a] for a in required}
    tolerance=rational(args.near_optimal_tolerance);r=analyze(candidates,quotes,tolerance)
    oracle=None
    if args.pade_output is not None:
        pb=args.pade_output.read_bytes();pade=json.loads(pb)
        if pade.get("status")!="FROZEN_PADE_NUMERIC_OUTPUT_EXACT_DYADICS_NOT_TRUE_PRICE_CERTIFICATE":
            raise ValueError("algorithm output needs explicit non-true-price frozen status")
        if pade.get("contract_sha256")!=digest(cb) or pade.get("quotes_sha256")!=digest(qb):
            raise ValueError("algorithm output contract/quotes differ")
        if not pade.get("runtime_versions") or not pade.get("algorithm"):
            raise ValueError("frozen numerical algorithm and runtime versions must be identified")
        executed=Path(pade["executed_source_path"])
        if not executed.is_absolute():executed=args.pade_output.parent/executed
        if not executed.is_file() or pade.get("executed_source_sha256")!=digest(executed.read_bytes()):
            raise ValueError("frozen algorithm executed source unavailable or changed")
        for name,sha in pade.get("component_sources_sha256",{}).items():
            path=args.pade_output.parent/name
            if not path.is_file() or digest(path.read_bytes())!=sha:
                raise ValueError("frozen numeric algorithm component source unavailable or changed")
        outputs={}
        for item in pade["cover"]:
            alpha=rational(item["alpha"])
            if alpha in outputs or alpha not in required:raise ValueError("unexpected/duplicate algorithm candidate")
            if [row["row_id"] for row in item["rows"]]!=selected:raise ValueError("algorithm row order differs")
            exact=[]
            for row in item["rows"]:
                value=rational(row["normalized_call_exact_dyadic"])
                if value.denominator & (value.denominator-1):
                    raise ValueError("binary64 algorithm output must be its exact dyadic value")
                exact.append(value)
            outputs[alpha]=exact
        if set(outputs)!=set(required):raise ValueError("all required frozen algorithm candidates needed")
        algbounds={a:maths.objective_bounds([(v,v) for v in outputs[a]],quotes) for a in required}
        algbest=min(required,key=lambda a:algbounds[a]["mid_upper"])
        algcompetitors=[algbounds[a]["mid_lower"] for a in required if a!=algbest]
        algmargin=min(algcompetitors)-algbounds[algbest]["mid_upper"]
        algwinner=algbest if algmargin>0 else None
        oracle={"status":"TRUE_PRICE_INTERVAL_REFERENCE_ORACLE_FOR_ACTUAL_NUMERIC_OUTPUTS",
            "algorithm_output_sha256":digest(pb),"algorithm":pade["algorithm"],
            "executed_source_sha256":pade["executed_source_sha256"],
            "component_sources_sha256":pade.get("component_sources_sha256",{}),
            "runtime_versions":pade["runtime_versions"],
            "quote_target":"exact BS bid/ask PRICE midpoint; its rigorous enclosure remains in the objective",
            "algorithm_objective_evaluation":"exact Fraction interval arithmetic; quote-mid uncertainty is enclosed, not silently replaced by a dyadic target",
            "certified_algorithm_finite_argmin":show(algwinner) if algwinner is not None else None,
            "algorithm_finite_winner_gap_lower":show(algmargin),
            "actual_algorithm_and_true_model_finite_argmin_same_certified":
                algwinner is not None and algwinner==r["strict_unique_minimizer"],
            "candidates":[{"alpha":show(a),"algorithm_objective_bounds":maths.serial_bounds(algbounds[a]),
                "actual_numeric_normalized_price_error_upper":[
                    show(max(abs(v-lo),abs(v-hi))) for v,(lo,hi) in zip(outputs[a],candidates[a])],
                "frozen_normalized_calls_exact_dyadics":[show(v) for v in outputs[a]]} for a in required],
            "guarantee":"each error bound encloses every error of this actual output versus the true model, including all solver, Fourier quadrature, truncation and floating arithmetic effects",
            "not_certified":"continuous Pade Fourier integral, other algorithms/grids, other parameter candidates, continuous alpha argmin, unrestricted market identification"}
        if algwinner is not None:
            oracle["selected_candidate_true_objective_regret_upper"]=show(
                r["results"][algwinner]["mid_upper"]-r["global_lower"])
    out={"status":"EXACT_FINITE_CANDIDATE_OBJECTIVE_AGGREGATION_WITH_SUPPLIED_TRUE_PRICE_CERTIFICATES",
        "scope":"only the explicitly frozen finite alpha candidates and twelve normalized T=.5 quote-defined prices",
        "contract_id":contract["contract_id"],"contract_sha256":digest(cb),"quotes_sha256":digest(qb),
        "source_sha256":digest(Path(__file__).read_bytes()),"selected_row_ids":selected,
        "finite_candidate_alpha":[show(a) for a in required],
        "finite_candidate_H":[show(a-F(1,2)) for a in required],
        "near_optimal_tolerance":show(tolerance),
        "global_finite_minimum_objective_enclosure":{"lower":show(r["global_lower"]),"upper":show(r["global_upper"])},
        "best_certified_witness":show(r["best_witness"]),
        "all_true_epsilon_near_optimal_finite_candidates_outer":[show(a) for a in r["near_optimal_outer"]],
        "certified_epsilon_near_optimal_finite_candidates_inner":[show(a) for a in r["near_optimal_inner"]],
        "strict_unique_finite_minimizer":show(r["strict_unique_minimizer"]) if r["strict_unique_minimizer"] is not None else None,
        "strict_winner_objective_gap_lower":show(r["strict_winner_margin_lower"]) if r["strict_winner_margin_lower"] is not None else None,
        "objective_uniform_perturbation_strict_robustness_radius":
            show(r["strict_winner_margin_lower"]/2) if r["strict_unique_minimizer"] is not None else None,
        "perturbation_guarantee":"if a positive winner margin m is certified, any uniformly perturbed objective with sup error delta_J<m/2 has the same finite minimizer; epsilon-algorithm also needs 2delta_J+epsilon<m",
        "smooth_finite_class_alpha_ge_0.6_objective_lower":show(r["smooth_lower"]) if r["smooth_lower"] is not None else None,
        "smooth_finite_class_excluded_from_true_near_optimal_set":r["smooth_near_optimal_class_excluded"],
        "exact_quote_compatible_finite_candidates_outer":[show(a) for a in r["compatible_outer"]],
        "certified_exact_quote_compatible_finite_candidates_inner":[show(a) for a in r["compatible_inner"]],
        "candidates":[{"alpha":show(a),"H":show(a-F(1,2)),"bounds":maths.serial_bounds(r["results"][a]),
            "true_objective_gap_enclosure":{"lower":show(max(F(0),r["results"][a]["mid_lower"]-r["global_upper"])),
                "upper":show(r["results"][a]["mid_upper"]-r["global_lower"])},
            "evidence":evidence[a]} for a in required],
        "true_price_component_proofs_revalidated_by_this_objective_script":False,
        "actual_Pade_numeric_output_reference_oracle":oracle,
        "no_continuous_argmin_or_unrestricted_identification_claim":True}
    args.output.write_text(json.dumps(out,indent=2)+"\n",encoding="utf8")
    print(json.dumps({k:out[k] for k in ["status","finite_candidate_alpha",
        "global_finite_minimum_objective_enclosure","strict_unique_finite_minimizer"]},indent=2))

if __name__=="__main__":main()
