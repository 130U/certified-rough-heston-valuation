"""Separate strict double-series replay and full-bank financial reconstruction."""
import argparse, copy
from fractions import Fraction as Q
import numpy as np
from common import HERE, baseline, identities, load, save, sha, module, interval, exact

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--baseline");args=parser.parse_args()
    base=baseline(args.baseline);contract=identities(base)
    result=load(HERE/"results.json");weights=load(HERE/"weights.json");protocol=load(HERE/"reader-protocol.json")
    source=load(base/"experiments/local128/candidate-13_25.json")
    global_source=load(base/"experiments/N2048/candidate-13_25.json")
    source_weights=load(base/"experiments/local128/weights-and-envelopes.json")["records"]
    residual=load(base/"experiments/N2048/residual-13_25.json")
    point=load(base/"experiments/N2048/point-independent-13_25.json")
    assert point["status"]=="PASS_COMPLETE_POINT_RECONSTRUCTION"
    assert point["candidate_sha256"]==sha(base/"experiments/N2048/candidate-13_25.json")
    alpha,T,nu,sigma=map(Q,(contract["alpha"],contract["T"],contract["nu"],contract["sigma"]))
    lam=nu*sigma;curve=contract["curve"]
    alpha0,lxi,v0,theta=map(Q,[curve[k] for k in ["alpha0","lambda_xi","V0","theta"]])
    scale=Q(contract["price_task"]["index_point_scale"])
    oldprices=source["price_rows"]
    rem=sum((Q(oldprices[i][k]) for i in [7,8] for k in ["strip_remainder","true_infinite_tail_remainder","reference_arithmetic_remainder"]),Q(0))
    shift=Q(source["correction_control"]["direct_reference_spread"])-Q(source["correction_control"]["actual_frozen_fast_spread"])
    def guard(r,w):
        assert r["status"]=="COMPLETE_SAME_OUTPUT_RESOLVENT_VS_CURVE_FULL_1025_NODE_COMPARISON"
        assert r["parameters"]=={k:contract[k] for k in ["alpha","T","nu","sigma","physical_lambda"]}
        assert Q(r["parameters"]["sigma"])>=0 and Q(r["parameters"]["physical_lambda"])==Q(r["parameters"]["nu"])*Q(r["parameters"]["sigma"])
        assert r["contract_sha256"]==w["contract_sha256"]==sha(HERE/"contract.json")
        assert [Q(z["u"]) for z in r["node_ledger"]]==[Q(j,8) for j in range(1025)]
        assert len(w["cells"])==128
        for j,c in enumerate(w["cells"]):assert [Q(c["left"]),Q(c["right"])]==[Q(j,256),Q(j+1,256)]
        zero=w["sigma_zero_control"]
        assert zero["physical_lambda"]=="0" and zero["kernel"]=="curve"
        assert zero["weights"]==[c["curve_weight"] for c in w["cells"]]
        for mode,value in r["modes"].items():
            assert Q(value["remainder_points"])==rem*scale>0 and Q(value["signed_centre_points"])==shift*scale
            assert len(value["price_rows"])==12
            for old,new in zip(oldprices,value["price_rows"]):
                assert old["strict_reference_centre"]==new["same_strict_reference_centre"]
                assert old["actual_fast_output"]==new["same_actual_fast_output"]
        for node in r["node_ledger"][:513]:
            lo,hi=map(Q,node["eta_resolvent_enclosure"])
            assert 0<=lo<=Q(node["eta_upper"]["local_resolvent"])==hi
    guard(result,weights)
    assert result["weights_sha256"]==sha(HERE/"weights.json") and result["executed_source_sha256"]==sha(HERE/"generate.py")
    assert result["loader_sha256"]==sha(HERE/"common.py")
    # Direct double series: no producer function or power_field_moment imported.
    dy=module("ind_kernel_dyadic",base/"experiments/sdk/interval-pade-certificate.py");I,S,C=dy.I,dy.S,dy.C
    gamma_cache={}
    def gamma(q):
        q=Q(q)
        if q not in gamma_cache:gamma_cache[q]=dy.gamma_positive(q)
        return gamma_cache[q]
    def signed_exp(x):
        if x.lo>=0:return dy.exp_positive(x)
        if x.hi<=0:return dy.exp_positive(-x).recip()
        return I(dy.exp_positive(I(-x.lo,-x.lo,True)).recip().lo,dy.exp_positive(I(x.hi,x.hi,True)).hi,True)
    def power(t,beta):
        t,beta=Q(t),Q(beta)
        if t==0:return I(0)
        if beta==1:return I(t)
        k=0;q=t
        while q<1:q*=2;k-=1
        while q>2:q/=2;k+=1
        return signed_exp(beta*(dy.log_unit(I(q))+k*dy.LOG2))
    def W(t,damping):
        t=Q(t)
        if not t:return I(0)
        damping=Q(damping);inner=protocol["independent_inner_terms"];N=protocol["independent_outer_terms"]
        w=lxi*power(t,alpha0);assert w.hi<S
        inner_tail=(w**inner)/(1-w)
        total=I(0)
        for n in range(1 if damping==0 else N):
            beta=n*alpha;t_power=power(t,1+beta)
            term=I(1);ml=I(0)
            for m in range(inner):
                assert 2+beta+m*alpha0>=2
                ml+=term/gamma(2+beta+m*alpha0);term=-term*w
            ml+=I(-inner_tail.hi,inner_tail.hi,True)
            total+=((-damping)**n)*(theta*t_power/gamma(2+beta)+(v0-theta)*t_power*ml)
        if damping:
            x=damping*power(t,alpha);assert 0<=x.lo and x.hi<S
            tail=theta*I(t)*(x**N)/(1-x);total+=I(-tail.hi,tail.hi,True)
        return total
    values=[W(Q(k,256),lam) for k in range(129)]
    # Exercise zero damping explicitly. The analytical identity K_0=xi is
    # exact; two strict implementations must give compatible cumulative
    # enclosures. No reciprocal damping occurs in either calculation.
    mo_zero=module("ind_zero_curve",base/"experiments/sdk/exact-forward-moments.py")
    zero_values=[W(Q(k,256),Q(0)) for k in range(129)]
    for k,z in enumerate(zero_values):
        original_curve=interval(I,S,mo_zero.moments(Q(k,256),64)[0].bounds())
        assert max(z.lo,original_curve.lo)<=min(z.hi,original_curve.hi)
    for k,cell in enumerate(weights["cells"]):
        raw=zero_values[128-k]-zero_values[127-k]
        original=interval(I,S,cell["curve_weight"])
        assert max(raw.lo,original.lo)<=min(raw.hi,original.hi)
    independent_weights=[]
    for k,w in enumerate(weights["cells"]):
        raw=values[128-k]-values[127-k];curve_iv=interval(I,S,w["curve_weight"])
        bounded=I(max(0,raw.lo),min(raw.hi,curve_iv.hi),True)
        assert 0<=bounded.lo<=bounded.hi
        independent_weights.append(bounded)
    # Every source entry is read; binary64 values are exact dyadics, so these
    # comparisons against dyadic j/256 edges implement exact endpoint ordering.
    bank=np.load(base/"experiments/N2048/field-13_25-residual-cells.npz")
    assert bank["bound"].shape==(4095,513)
    assert bank["a"][0]==0 and bank["b"][-1]==.5 and np.array_equal(bank["a"][1:],bank["b"][:-1])
    assert np.all(np.isfinite(bank["bound"])) and np.all(bank["bound"]>=0)
    assert np.all(bank["re_upper"][1:]<=0)
    assert all(Q(x)<=0 for x in residual["first_cell_Re_H_div_talpha_upper_exact_dyadics"])
    assert list(map(exact,np.max(bank["bound"],axis=0)))==list(map(Q,residual["delta_physical_upper_exact_dyadics"]))
    envelopes=[]
    for k,saved in enumerate(source_weights):
        a,b=Q(k,256),Q(k+1,256)
        indices=np.flatnonzero((bank["a"]<=float(b))&(bank["b"]>=float(a)))
        assert len(indices)==saved["overlapping_closed_cell_count"]
        assert int(indices[0])==saved["first_closed_source_index"] and int(indices[-1])==saved["last_closed_source_index"]
        maxima=list(map(exact,np.max(bank["bound"][indices],axis=0)))
        assert maxima==list(map(Q,saved["physical_residual_envelope"]));envelopes.append(maxima)
    exponents=load(base/"experiments/N2048/exponents-13_25.json")["rows"]
    def up(x):return Q(x.hi,S)
    def norm(x):return up(x.norm2().sqrt())
    shared_q=module("ind_shared_global_q",base/"experiments/sdk/direct-tail-certificate.py")
    A=interval(I,S,shared_q.cumulative_q(T,alpha,64).bounds())
    maximum_R=list(map(Q,residual["delta_physical_upper_exact_dyadics"]))
    eta_replays=[];independent_eps=[];min_checks=0
    for j,node in enumerate(result["node_ledger"]):
        old=source["node_ledger"][j]
        if j<513:
            lo=sum((r[j]*Q(w.lo,S)/nu for r,w in zip(envelopes,independent_weights)),Q(0))
            hi=sum((r[j]*Q(w.hi,S)/nu for r,w in zip(envelopes,independent_weights)),Q(0))
            recorded_lo,recorded_hi=map(Q,node["eta_resolvent_enclosure"])
            assert recorded_lo<=lo<=hi<=recorded_hi
            mag=interval(I,S,exponents[j]["phi_modulus"]);cap=I(min(S,mag.lo),min(S,mag.hi),True)
            triangle=up(I(Q(old["true_CF_modulus_upper"]))+mag)
            epsilon=min(up(cap*(dy.exp_positive(I(hi))-1)),triangle)
            assert epsilon<=Q(node["epsilon_upper"]["local_resolvent"])
            eta_state=up(I(maximum_R[j]/(nu*nu*sigma))*A)
            assert Q(node["eta_upper"]["global_state"])==eta_state
            assert Q(node["epsilon_upper"]["global_state"])==min(up(cap*(dy.exp_positive(I(eta_state))-1)),triangle)
            assert node["eta_upper"]["local_curve"]==old["eta_upper"] and node["epsilon_upper"]["local_curve"]==old["epsilon_upper"]
            assert node["eta_upper"]["global_curve"]==global_source["node_ledger"][j]["eta_upper"]
            assert node["epsilon_upper"]["global_curve"]==global_source["node_ledger"][j]["epsilon_upper"]
            assert Q(node["epsilon_upper"]["local_resolvent"])<=Q(node["epsilon_upper"]["local_curve"])
            for mode,eta in node["eta_upper"].items():
                assert Q(node["epsilon_upper"][mode])==min(up(cap*(dy.exp_positive(I(Q(eta)))-1)),triangle)
            min_checks+=1
            eta_replays.append([str(lo),str(hi)]);independent_eps.append(epsilon)
        else:
            epsilon=Q(old["epsilon_upper"])
            assert all(Q(v)==epsilon for v in node["epsilon_upper"].values())
            assert all(Q(v)==0 for v in node["eta_upper"].values());independent_eps.append(epsilon)
    # Reassemble all 12 prices, signed interval, both supports, and actual returns.
    coefficients=[[C(interval(I,S,z["re"]),interval(I,S,z["im"])) for z in old["coefficients"]] for old in source["node_ledger"]]
    remainder=[sum((Q(r[k]) for k in ["strip_remainder","true_infinite_tail_remainder","reference_arithmetic_remainder"]),Q(0)) for r in oldprices]
    for mode,value in result["modes"].items():
        eps=[Q(n["epsilon_upper"][mode]) for n in result["node_ledger"]]
        jr=sum((e*norm(c[7]-c[8]) for e,c in zip(eps,coefficients)),Q(0))
        mr=sum((e*(norm(c[7])+norm(c[8])) for e,c in zip(eps,coefficients)),Q(0))
        radius=jr+rem;mar=mr+rem
        assert Q(value["disk_joint_radius_points"])==jr*scale
        assert list(map(Q,value["signed_error_interval_points"]))==[(shift-radius)*scale,(shift+radius)*scale]
        assert Q(value["frozen_fast_joint_bound_points"])==(abs(shift)+radius)*scale
        assert Q(value["frozen_fast_marginal_bound_points"])==(abs(shift)+mar)*scale
        for b,decision in value["budget_decisions"].items():assert decision==((abs(shift)+radius)*scale<=Q(b))
        for label,column in [("reference","actual_reference_output_binary64"),("corrected_fast","actual_corrected_fast_output_binary64")]:
            returned=Q(oldprices[7][column])-Q(oldprices[8][column]);offset=abs(returned-Q(source["correction_control"]["direct_reference_spread"]))
            assert Q(value["actual_outputs"][label]["joint_bound_points"])==(offset+radius)*scale
            assert Q(value["actual_outputs"][label]["marginal_bound_points"])==(offset+mar)*scale
        for i,p in enumerate(value["price_rows"]):
            rad=sum((e*norm(c[i]) for e,c in zip(eps,coefficients)),Q(0))+remainder[i]
            assert Q(p["complete_reference_radius"])==rad
            assert Q(p["frozen_fast_absolute_error_upper"])==abs(Q(oldprices[i]["centre_correction"]))+rad
    controls=[]
    for name in protocol["controls"]:
        r,w=copy.deepcopy(result),copy.deepcopy(weights)
        if name=="negative_sigma":r["parameters"]["sigma"]="-1"
        elif name=="wrong_nu_scale":r["parameters"]["nu"]="1"
        elif name=="missing_initial_closed_cell":w["cells"][0]["left"]="1/256"
        elif name=="omitted_finite_node_removed":r["node_ledger"].pop()
        elif name=="erased_true_infinite_tail":r["modes"]["local_resolvent"]["remainder_points"]="0"
        elif name=="altered_signed_centre":r["modes"]["local_resolvent"]["signed_centre_points"]="0"
        elif name=="understated_resolvent_eta":r["node_ledger"][1]["eta_upper"]["local_resolvent"]="0"
        elif name=="sigma_zero_not_curve":w["sigma_zero_control"]["weights"][0]=["0","0"]
        else:raise AssertionError("unknown negative control")
        try:guard(r,w)
        except AssertionError:controls.append({"control":name,"rejected":True})
        else:raise AssertionError("corruption accepted: "+name)
    report={"status":"PASS_SEPARATE_STRICT_RESOLVENT_REPLAY_AND_FULL_PRICE_READBACK",
        "contract_sha256":sha(HERE/"contract.json"),"reader_protocol_sha256":sha(HERE/"reader-protocol.json"),
        "reader_sha256":sha(HERE/"independent.py"),"results_sha256":sha(HERE/"results.json"),
        "independent_outer_terms":protocol["independent_outer_terms"],"independent_inner_terms":protocol["independent_inner_terms"],
        "complete_bank_entries_read":int(bank["bound"].size),"bin_maximum_vectors_checked":128,
        "independent_resolvent_eta_enclosures":eta_replays,"full_frequency_nodes":1025,"all_price_rows":12,
        "complete_transform_radius_minima_checked":min_checks,"loader_sha256":sha(HERE/"common.py"),
        "same_output_centres_remainders":True,"sigma_zero_control":"zero damping is exactly the curve kernel; no reciprocal damping required",
        "zero_sigma_cumulative_enclosures_replayed":129,"zero_sigma_cell_enclosures_compared":128,
        "negative_controls":controls,
        "sharing_boundary":"Independent direct double Gamma-series and certificate assembly; shares identified reference Gamma/log/exp and dyadic coefficient arithmetic. Inherits reference residual proof and reference exponents, rather than independently rederiving every residual derivative."}
    save(HERE/"independent.json",report)
    print({"status":report["status"],"full_nodes":1025,"prices":12,"negative_controls_rejected":len(controls)})
if __name__=="__main__":main()
