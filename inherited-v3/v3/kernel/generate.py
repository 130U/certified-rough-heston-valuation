"""Strict finite-history resolvent weights and unchanged-output full prices."""
import argparse
from fractions import Fraction as Q
from common import HERE, baseline, identities, load, save, sha, module, interval

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--baseline");args=parser.parse_args()
    base=baseline(args.baseline);contract=identities(base);sdk=base/"experiments/sdk"
    mo=module("kernel_moments",sdk/"exact-forward-moments.py")
    direct=module("kernel_q",sdk/"direct-tail-certificate.py")
    I,S,C=mo.I,mo.S,mo.dy.C
    alpha,T,nu,sigma=map(Q,(contract["alpha"],contract["T"],contract["nu"],contract["sigma"]))
    lam=nu*sigma;M=contract["outer_resolvent_terms"];inner=contract["inner_curve_terms"]
    assert lam==Q(contract["physical_lambda"]) and sigma>=0
    assert (mo.ALPHA0,mo.LAMBDA,mo.V0,mo.THETA)==tuple(map(Q,[contract["curve"][k] for k in ["alpha0","lambda_xi","V0","theta"]]))
    source=load(base/"experiments/local128/candidate-13_25.json")
    envelopes=load(base/"experiments/local128/weights-and-envelopes.json")["records"]
    original=load(base/"experiments/N2048/candidate-13_25.json")
    residual=load(base/"experiments/N2048/residual-13_25.json")
    exponents=load(base/"experiments/N2048/exponents-13_25.json")["rows"]
    assert source["status"]=="DESCRIPTIVE_LOCAL128_OUTPUT_CONTROL_NOT_NEARBY_GRID_OBJECTIVE_RESULT"
    assert len(source["node_ledger"])==1025 and len(envelopes)==128
    assert residual["approx_left_halfplane_certified"]
    assert all(Q(x)<=0 for x in residual["first_cell_Re_H_div_talpha_upper_exact_dyadics"])
    assert all(Q(x)<=0 for x in residual["later_cells_Re_H_upper_exact_dyadics"])
    def upper(x): return Q(x.hi,S)
    def norm(x): return upper(x.norm2().sqrt())
    def cumulative(t):
        t=Q(t)
        if t==0:return I(0),I(0)
        curve=mo.moments(t,inner)[0]
        if lam==0:return curve,I(0)
        total=I(0)
        for n in range(M):
            beta=n*alpha
            primitive=mo.power_field_moment(beta,t,inner)/mo.gamma_cached(1+beta)
            total+=((-lam)**n)*primitive
        x=lam*mo.power(t,alpha);assert 0<=x.lo and x.hi<S
        tail=mo.THETA*I(t)*(x**M)/(1-x)
        return total+I(-tail.hi,tail.hi,True),tail
    edges=[Q(k,256) for k in range(129)]
    values=[cumulative(t) for t in edges]
    cumulative_rows=[{"t":str(t),"W_resolvent":w.bounds(),"absolute_series_tail":r.bounds()} for t,(w,r) in zip(edges,values)]
    weights=[]
    for k,e in enumerate(envelopes):
        a,b=Q(e["left"]),Q(e["right"]);assert (a,b)==(edges[k],edges[k+1])
        curve=interval(I,S,e["strict_weight"])
        raw=values[128-k][0]-values[127-k][0]
        # Both positivity and domination follow analytically from q>=0, k>=0.
        w=I(max(0,raw.lo),min(raw.hi,curve.hi),True)
        assert 0<=w.lo<=w.hi
        weights.append({"left":str(a),"right":str(b),"curve_weight":curve.bounds(),
                        "raw_resolvent_weight":raw.bounds(),"resolvent_weight":w.bounds()})
    save(HERE/"weights.json",{"status":"STRICT_FULL_RESOLVENT_CUMULATIVE_AND_128_CELL_WEIGHTS",
         "contract_sha256":sha(HERE/"contract.json"),"source_weight_sha256":sha(base/"experiments/local128/weights-and-envelopes.json"),
         "formula":"W_lambda(t)=sum_n (-lambda)^n integral_0^t (xi*g_(n alpha))(s) ds",
         "outer_terms":M,"inner_terms":inner,"cumulative":cumulative_rows,"cells":weights,
         "sigma_zero_control":{"physical_lambda":"0","kernel":"curve",
                               "weights":[w["curve_weight"] for w in weights]},
         "sharing":"V2 exact-forward-moment integration and identified dyadic/Gamma/log/exp primitives; new resolvent summation and explicit outer tail"})
    J0=mo.moments(T,inner)[0]
    A=interval(I,S,direct.cumulative_q(T,alpha,inner).bounds())
    globalR=list(map(Q,residual["delta_physical_upper_exact_dyadics"]))
    modes=["global_state","global_curve","local_curve","local_resolvent"]
    prices=source["price_rows"];pointscale=Q(contract["price_task"]["index_point_scale"])
    remainders=[sum((Q(r[k]) for k in ["strip_remainder","true_infinite_tail_remainder","reference_arithmetic_remainder"]),Q(0)) for r in prices]
    radii={m:[Q(0)]*12 for m in modes};spread={m:{"joint":Q(0),"marginal":Q(0)} for m in modes};nodes=[]
    eps_used={m:[] for m in modes}
    for j,old in enumerate(source["node_ledger"]):
        u=Q(old["u"]);assert u==Q(j,8)
        coefficients=[C(interval(I,S,v["re"]),interval(I,S,v["im"])) for v in old["coefficients"]]
        if j<=512:
            eta_curve=sum((Q(e["physical_residual_envelope"][j])*Q(w["curve_weight"][1])/nu for e,w in zip(envelopes,weights)),Q(0))
            eta_lo=sum((Q(e["physical_residual_envelope"][j])*Q(w["resolvent_weight"][0])/nu for e,w in zip(envelopes,weights)),Q(0))
            eta_hi=sum((Q(e["physical_residual_envelope"][j])*Q(w["resolvent_weight"][1])/nu for e,w in zip(envelopes,weights)),Q(0))
            etas={"global_state":upper(I(globalR[j]/(nu*nu*sigma))*A),
                  "global_curve":upper(I(globalR[j]/nu)*J0),
                  "local_curve":eta_curve,"local_resolvent":eta_hi}
            assert etas["global_curve"]==Q(original["node_ledger"][j]["eta_upper"])
            assert eta_curve==Q(old["eta_upper"]) and 0<=eta_lo<=eta_hi<=eta_curve
            mag=interval(I,S,exponents[j]["phi_modulus"])
            cap=I(min(S,mag.lo),min(S,mag.hi),True)
            triangle=upper(I(Q(old["true_CF_modulus_upper"]))+mag)
            eps={m:min(upper(cap*(mo.dy.exp_positive(I(eta))-1)),triangle) for m,eta in etas.items()}
            assert eps["local_curve"]==Q(old["epsilon_upper"]) and eps["global_curve"]==Q(original["node_ledger"][j]["epsilon_upper"])
            assert eps["local_resolvent"]<=eps["local_curve"]
        else:
            etas={m:Q(0) for m in modes};eps={m:Q(old["epsilon_upper"]) for m in modes}
            eta_lo=eta_hi=Q(0)
            assert old==original["node_ledger"][j]
        nodes.append({"u":str(u),"eta_resolvent_enclosure":[str(eta_lo),str(eta_hi)],
                     "eta_upper":{m:str(v) for m,v in etas.items()},"epsilon_upper":{m:str(v) for m,v in eps.items()}})
        for m in modes:
            eps_used[m].append(eps[m])
            for i in range(12):radii[m][i]+=eps[m]*norm(coefficients[i])
            spread[m]["joint"]+=eps[m]*norm(coefficients[7]-coefficients[8])
            spread[m]["marginal"]+=eps[m]*(norm(coefficients[7])+norm(coefficients[8]))
    centre=Q(source["correction_control"]["direct_reference_spread"])
    fast=Q(source["correction_control"]["actual_frozen_fast_spread"])
    shift=centre-fast;rem=remainders[7]+remainders[8]
    ledger={}
    for m in modes:
        s=spread[m];r=s["joint"]+rem;mar=s["marginal"]+rem
        total=(abs(shift)+r)*pointscale;mt=(abs(shift)+mar)*pointscale
        interval_error=[(shift-r)*pointscale,(shift+r)*pointscale]
        actuals={}
        for label,column in [("reference","actual_reference_output_binary64"),("corrected_fast","actual_corrected_fast_output_binary64")]:
            returned=Q(prices[7][column])-Q(prices[8][column]);rs=abs(returned-centre)
            actuals[label]={"joint_bound_points":str((rs+r)*pointscale),"marginal_bound_points":str((rs+mar)*pointscale)}
        ledger[m]={"frozen_fast_joint_bound_points":str(total),"frozen_fast_marginal_bound_points":str(mt),
                   "signed_error_interval_points":list(map(str,interval_error)),
                   "signed_centre_points":str(shift*pointscale),"disk_joint_radius_points":str(s["joint"]*pointscale),
                   "finite_omitted_joint_radius_points":str(sum((eps_used[m][j]*norm(C(interval(I,S,source["node_ledger"][j]["coefficients"][7]["re"]),interval(I,S,source["node_ledger"][j]["coefficients"][7]["im"]))-C(interval(I,S,source["node_ledger"][j]["coefficients"][8]["re"]),interval(I,S,source["node_ledger"][j]["coefficients"][8]["im"]))) for j in range(513,1025)),Q(0))*pointscale),
                   "remainder_points":str(rem*pointscale),"actual_outputs":actuals,
                   "budget_decisions":{b:total<=Q(b) for b in contract["price_task"]["budgets"]},
                   "price_rows":[{"row_id":old["row_id"],"same_strict_reference_centre":old["strict_reference_centre"],
                         "same_actual_fast_output":old["actual_fast_output"],"complete_reference_radius":str(radii[m][i]+remainders[i]),
                         "frozen_fast_absolute_error_upper":str(abs(Q(old["centre_correction"]))+radii[m][i]+remainders[i])} for i,old in enumerate(prices)]}
    out={"status":"COMPLETE_SAME_OUTPUT_RESOLVENT_VS_CURVE_FULL_1025_NODE_COMPARISON",
         "contract_sha256":sha(HERE/"contract.json"),"weights_sha256":sha(HERE/"weights.json"),
         "executed_source_sha256":sha(HERE/"generate.py"),"loader_sha256":sha(HERE/"common.py"),
         "parameters":{k:contract[k] for k in ["alpha","T","nu","sigma","physical_lambda"]},
         "modes":ledger,"node_ledger":nodes,
         "work":{"new_residual_entries":0,"closed_source_entries_reused":513*4095,
                 "used_reference_frequencies":513,"omitted_finite_frequencies":512,"full_grid_frequencies":1025,
                 "propagation_bins":128,"resolvent_weighted_residual_terms":128*513,
                 "outer_series_terms":M,"inner_curve_series_terms":inner,"all_price_rows":12},
         "scope":"Rigorous bound on the full residual-envelope functional; no lower bound on true error, observed-error reduction, changed reference, or market claim.",
         "independent_reader_boundary":"New separate replay is required before independent-pass status."}
    save(HERE/"results.json",out)
    print({"status":out["status"],"frozen_fast_joint_points":{m:float(Q(ledger[m]["frozen_fast_joint_bound_points"])) for m in modes}})
if __name__=="__main__":main()
