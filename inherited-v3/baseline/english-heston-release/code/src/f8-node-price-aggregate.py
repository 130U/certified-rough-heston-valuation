"""Exact F8 prices for first-maturity twelve-strike normalized IV experiment.

Missing continuous residual input is a hard failure. Stored-field exponents
alone are never true-CF certificates. All proof decisions are rational/100-bit
outward dyadic arithmetic. Omitted high-frequency approximate nodes are zero,
but their TRUE discrete tail is charged through F6/F7, never defaulted to zero.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, importlib.util, json, sys, time

BASE=Path(__file__).resolve().parent
H=F(1,8); STRIP=F(9,20); NU=F(2897,10000)
RHO=F(-1489,2000); S0=F(1489,4000); T=F(1,2)


def fraction(value):
    if not isinstance(value,str):
        raise TypeError("certificate endpoints must be exact rational strings")
    return F(value)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_interval(record,I,S):
    if len(record)!=2:raise ValueError("interval must contain two endpoints")
    lo,hi=map(fraction,record)
    if lo>hi:raise ValueError("reversed interval")
    return I((lo.numerator*S)//lo.denominator,-((-hi.numerator*S)//hi.denominator),True)


def absolute(x,I):
    lower=0 if x.lo<=0<=x.hi else min(abs(x.lo),abs(x.hi))
    return I(lower,max(abs(x.lo),abs(x.hi)),True)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exponents",type=Path,default=BASE/"fixed-field-betap52-exponent-certificate.json")
    parser.add_argument("--residual",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--exponent-error-proof",type=Path,required=True,
                        help="independently established D-type positive-kernel error identity")
    parser.add_argument("--solver-cutoff",type=str,
                        help="explicit optional shorter node cover; omitted true tail is still charged")
    parser.add_argument("--grid-cutoff",type=str,
                        help="explicit hybrid finite grid cutoff; later approximate CF nodes are zero and charged")
    parser.add_argument("--true-cf-envelope",type=Path,
                        help="completed point-alpha true CF comparison envelope with actual proof files")
    parser.add_argument("--omit-failed-nodes",action="store_true",
                        help="explicitly replace unusable residual nodes by zero CF and charge the true envelope")
    args=parser.parse_args()
    # Do not create an output before every mandatory evidence source exists.
    for path in (args.exponents,args.residual,args.exponent_error_proof):
        if not path.is_file():raise FileNotFoundError(f"mandatory certificate missing: {path}")
    exponent_bytes=args.exponents.read_bytes();residual_bytes=args.residual.read_bytes()
    exponents=json.loads(exponent_bytes);residual=json.loads(residual_bytes)
    if exponents["status"]!="EXACT_STORED_FIELD_EXPONENT_COMPONENT_NOT_TRUE_CF_CERTIFICATE":
        raise ValueError("unexpected field exponent certificate status")
    if residual["status"]!="EXACT_CONTINUOUS_RESIDUAL_CERTIFICATE":
        raise ValueError("pointwise/grid residual diagnostics are not accepted")
    required=["field_sha256","T","nu","rho","kappa","alpha_lower","alpha_upper",
              "frequency_step","cover","residual_definition","proof_evidence"]
    for key in required:
        if key not in residual:raise ValueError(f"mandatory residual evidence missing: {key}")
    if residual["residual_definition"]!="D_C_t_alpha_Hhat_minus_nu_F":
        raise ValueError("physical Caputo residual definition must be explicit")
    if not residual["proof_evidence"]:raise ValueError("continuous-time residual proof evidence required")
    if residual["field_sha256"]!=exponents["field_sha256"]:
        raise ValueError("residual/exponent field hashes differ")
    field=args.exponents.parent/exponents["field"]
    if not field.is_file() or digest(field)!=exponents["field_sha256"]:
        raise ValueError("current frozen field differs from exponent source hash")
    if fraction(residual["T"])!=T or fraction(exponents["T"])!=T:
        raise ValueError("this contract is first maturity T=1/2 only")
    if fraction(residual["nu"])!=NU or fraction(exponents["nu"])!=NU:
        raise ValueError("nu differs from frozen profile")
    if fraction(residual["rho"])!=RHO or fraction(residual["kappa"])!=0:
        raise ValueError("rho/kappa differs from frozen profile")
    if fraction(residual["frequency_step"])!=H:
        raise ValueError("frequency step differs from exact h=1/8")
    alpha_l,alpha_u=map(fraction,[residual["alpha_lower"],residual["alpha_upper"]])
    if not F(".52")<=alpha_l<=alpha_u<=F(".9"):
        raise ValueError("parameter scope outside frozen first-maturity profile")
    component_spec=importlib.util.spec_from_file_location("field_component",BASE/"exponent-field-certificate.py")
    if exponents.get("source_sha256")!=digest(BASE/"exponent-field-certificate.py"):
        raise ValueError("exponent certificate source hash differs from the executed source available here")
    component=importlib.util.module_from_spec(component_spec);component_spec.loader.exec_module(component)
    mo=component.mo;dy=mo.dy;I,S,C=mo.I,mo.S,dy.C
    if (mo.ALPHA0,mo.LAMBDA,mo.V0,mo.THETA)!=(F(".5286"),F(".5037"),F(".0262"),F(".0721")):
        raise ValueError("forward curve differs from the frozen profile")
    if exponents["bits"]!=dy.BITS or dy.BITS!=100:
        raise ValueError("unexpected source arithmetic precision")
    ef={fraction(row["u"]):row for row in exponents["cover"]}
    if len(ef)!=len(exponents["cover"]):raise ValueError("duplicate exponent nodes")
    certs=sorted(residual["cover"],key=lambda row:fraction(row["u"]))
    if args.solver_cutoff is not None:
        chosen=F(args.solver_cutoff)
        if chosen<=0 or (chosen/H).denominator!=1:
            raise ValueError("solver cutoff must be a positive multiple of 1/8")
        certs=[row for row in certs if fraction(row["u"])<=chosen]
    if len(certs)<2:raise ValueError("positive cutoff and zero node both required")
    cutoff=H*(len(certs)-1)
    solver_cutoff=cutoff
    node_rows={fraction(row["u"]):row for row in certs}
    if len(node_rows)!=len(certs):raise ValueError("duplicate residual nodes")
    if sorted(node_rows)!=[i*H for i in range(len(certs))]:
        raise ValueError("residual node cover must start at zero and have no gaps")
    direct_bytes=None;direct_source_hashes={};direct_nodes=None;direct_tail_rate=None
    if args.true_cf_envelope is not None:
        direct_bytes=args.true_cf_envelope.read_bytes();direct=json.loads(direct_bytes)
        if direct.get("status")!="EXACT_TRUE_CF_COMPARISON_ENVELOPE_WITH_MODEL_ASSUMPTIONS" or direct.get("bits")!=100:
            raise ValueError("unexpected true-CF envelope status/precision")
        if direct.get("source_sha256")!=digest(BASE/"direct-tail-certificate.py"):
            raise ValueError("true-CF envelope source differs from available executed source")
        for key in ["model_proof","kernel_proof","tail_proof"]:
            proof=BASE/direct[key]
            if not proof.is_file():raise FileNotFoundError(f"true-CF proof missing: {proof}")
            direct_source_hashes[key]=digest(proof)
        matches=[r for r in direct["cover"] if fraction(r["alpha"])==alpha_l==alpha_u]
        if len(matches)!=1:raise ValueError("true-CF envelope does not cover this exact point alpha")
        dr=matches[0]
        for key,value in [("T",T),("rho",RHO),("nu",NU)]:
            if fraction(dr[key])!=value:raise ValueError("true-CF envelope fixed profile differs")
        direct_nodes={fraction(r["u"]):fraction(r["CF_modulus_upper"]) for r in dr["frequency_nodes"]}
        if len(direct_nodes)!=len(dr["frequency_nodes"]) or any(not 0<=v<=1 for v in direct_nodes.values()):
            raise ValueError("invalid/duplicate true-CF node bounds")
        if args.grid_cutoff is not None:cutoff=F(args.grid_cutoff)
        if cutoff<=0 or (cutoff/H).denominator!=1 or cutoff<solver_cutoff:
            raise ValueError("hybrid cutoff must be a grid node at or beyond used residual cover")
        rates=[r for r in dr["tails"] if F(r["V"])==cutoff]
        if len(rates)!=1:raise ValueError("no completed uniform true-tail rate at hybrid cutoff")
        direct_tail_rate=fraction(rates[0]["c_lower"])
        if direct_tail_rate<=0:raise ValueError("positive tail rate required")
        if any(i*H not in direct_nodes for i in range(int(cutoff/H)+1)):
            raise ValueError("true-CF envelope lacks a hybrid finite node")
    elif args.grid_cutoff is not None or args.omit_failed_nodes:
        raise ValueError("hybrid/failed-node omission requires explicit true-CF envelope")
    # On x in [1,2], psi=digamma is increasing, psi(1)=-EulerGamma,
    # psi(2)=1-EulerGamma and 0<EulerGamma<1, so |psi|<1. Thus
    # Gamma(x)>=Gamma(mid)*exp(-radius). Point domains have radius zero.
    alpha_mid=(alpha_l+alpha_u)/2;radius=(alpha_u-alpha_l)/2
    gamma2_lower=(mo.gamma_cached(2-alpha_mid)*mo.signed_exp(I(-radius))).lo
    if gamma2_lower<=0:raise ValueError("positive uniform Gamma lower bound failed")
    mass_bound=mo.THETA*mo.power(T,1-alpha_u)/(NU*I(gamma2_lower,gamma2_lower,True))
    # Whole-curve D-type tail (linearization proof, (20)). Eliminate the
    # T^alpha scale BEFORE bounding:
    # c_J(u)=b_rho^2 J0(T) u/[4(1+ b_rho nu u T^alpha/(2 Gamma(1+alpha)))].
    # T<1, so T^alpha <= T^alpha_lower. Digamma bound supplies a uniform
    # Gamma denominator LOWER bound; endpoint minima alone are not valid.
    gamma1_lower=(mo.gamma_cached(1+alpha_mid)*mo.signed_exp(I(-radius))).lo
    if gamma1_lower<=0:raise ValueError("positive uniform Gamma(1+alpha) lower failed")
    b_rho=I(2*(1-RHO*RHO)).sqrt()
    J0=mo.moments(T,terms=64)[0]
    if J0.lo<=0:raise ValueError("positive frozen forward-curve mass failed")
    z_over_gamma_per_u=b_rho*NU*mo.power(T,alpha_l)/(2*I(gamma1_lower,gamma1_lower,True))
    def decay_coefficient(u):
        coefficient=I(2*(1-RHO*RHO))*J0*u/(4*(1+z_over_gamma_per_u*u))
        if coefficient.lo<=0:raise ValueError("positive whole-curve decay coefficient failed")
        return F(coefficient.lo,S)
    eps_sum=I(0);eps_used=I(0);eps_omitted=I(0);phis=[];node_report=[]
    for index in range(int(cutoff/H)+1):
        u=index*H;row=node_rows.get(u)
        if row is None:
            if direct_nodes is None:raise ValueError("omitted node has no true-CF envelope")
            epsilon=I(direct_nodes[u]);phi=C(I(0),I(0))
            node_weight=F(2) if index==0 else 1/(u*u+F(1,4))
            eps_sum+=node_weight*epsilon;eps_omitted+=node_weight*epsilon;phis.append((u,phi))
            node_report.append({"u":str(u),"approximate_CF":"zero, deliberately omitted",
                "true_CF_minus_stored_CF_modulus_upper":str(F(epsilon.hi,S)),"error_source":"true-CF comparison envelope"})
            continue
        if u not in ef:raise ValueError("used residual node lacks a stored exponent")
        er=ef[u]
        phi=C(load_interval(er["phi_re"],I,S),load_interval(er["phi_im"],I,S))
        modulus=load_interval(er["phi_modulus"],I,S)
        if modulus.lo<0:raise ValueError("negative field exponential modulus")
        if "delta_physical_upper" in row:
            delta_phys=fraction(row["delta_physical_upper"]);delta=delta_phys/NU
            if "delta_F_upper" in row and fraction(row["delta_F_upper"])<delta:
                raise ValueError("normalized residual understates physical residual/nu")
        elif "delta_F_upper" in row:
            delta=fraction(row["delta_F_upper"]);delta_phys=NU*delta
        else:
            raise ValueError("every used node needs a continuous physical/normalized residual bound")
        if delta<0:raise ValueError("negative residual upper bound")
        halfplane_values=[]
        if "approx_halfplane_upper" in row:halfplane_values.append(fraction(row["approx_halfplane_upper"]))
        if "approx_halfplane_upper_bounds" in row:
            if not isinstance(row["approx_halfplane_upper_bounds"],list) or not row["approx_halfplane_upper_bounds"]:
                raise ValueError("nonempty exact list of independent all-time real-part bounds required")
            halfplane_values.extend(map(fraction,row["approx_halfplane_upper_bounds"]))
        halfplane_upper=min(halfplane_values) if halfplane_values else None
        if halfplane_upper is not None and halfplane_upper<2*S0:
            hp_proof=BASE/"complex-dissipativity.md"
            if not hp_proof.is_file():raise FileNotFoundError("mandatory halfplane error proof missing")
            direct_source_hashes["halfplane_error_proof"]=digest(hp_proof)
            stability=S0-max(F(0),halfplane_upper)/2
            computed_E=I(delta)/stability
            error_branch="certified all-time approximate real-part bound, linear delta/(s0-max(0,epsilon_R)/2)"
        elif delta<S0*S0/2:
            computed_E=2*I(delta)/(S0+(I(S0*S0-2*delta)).sqrt())
            error_branch="strict quadratic R1 barrier"
        elif args.omit_failed_nodes:
            epsilon=I(direct_nodes[u]);phi=C(I(0),I(0))
            node_weight=F(2) if index==0 else 1/(u*u+F(1,4))
            eps_sum+=node_weight*epsilon;eps_omitted+=node_weight*epsilon;phis.append((u,phi))
            node_report.append({"u":str(u),"delta_F_upper":str(delta),
                "approximate_CF":"zero, deliberately omitted after failed residual barrier",
                "true_CF_minus_stored_CF_modulus_upper":str(F(epsilon.hi,S)),"error_source":"true-CF comparison envelope"})
            continue
        else:raise ValueError("residual fails R1 and has no certified approximate-halfplane branch")
        supplied_E=fraction(row["E_delta_upper"]) if "E_delta_upper" in row else F(computed_E.hi,S)
        if supplied_E<F(computed_E.hi,S):
            raise ValueError("supplied E upper does not contain the exact R1 upper endpoint")
        # D-type identity: Ltrue-Lbar=nu^-1 integral q(T-t)(Htrue-Hhat),
        # q=(I^(1-alpha)xi)' >=0. No R3 field-factor or extra residual term.
        eta_interval=mass_bound*computed_E
        eta=F(eta_interval.hi,S)
        minimum_modulus=I(min(S,modulus.lo),min(S,modulus.hi),True)
        epsilon=minimum_modulus*(dy.exp_positive(I(eta))-1)
        # Optional exact true-CF envelope is another independent, always safe
        # cap: |true-stored| <= B_true + |stored|, not a solver claim.
        if direct_nodes is not None:true_modulus=I(direct_nodes[u])
        elif u==0: true_modulus=I(1)
        else:
            c=decay_coefficient(u)
            true_modulus=mo.signed_exp(I(-c*u))
        epsilon=I(0,min(epsilon.hi,(true_modulus+modulus).hi),True)
        node_weight=F(2) if index==0 else 1/(u*u+F(1,4))
        eps_sum+=node_weight*epsilon
        eps_used+=node_weight*epsilon
        phis.append((u,phi))
        node_report.append({"u":str(u),"delta_physical_upper":str(delta_phys),
            "delta_F_upper":str(delta),"E_computed_interval":computed_E.bounds(),
            "E_supplied_upper":str(supplied_E),"eta_upper":str(eta),
            "state_error_branch":error_branch,
            "all_time_approximate_realpart_upper":str(halfplane_upper) if halfplane_upper is not None else None,
            "true_CF_minus_stored_CF_modulus_upper":str(F(epsilon.hi,S))})
    # F7 tail of the TRUE grid: approximate coefficients after cutoff are zero.
    c=direct_tail_rate if direct_tail_rate is not None else decay_coefficient(cutoff)
    tail_integral=mo.signed_exp(I(-c*cutoff))/(c*cutoff*cutoff)
    strip_denominator=(F(1,2)-STRIP)*(dy.exp_positive(2*dy.PI*STRIP/H)-1)
    quotes_bytes=(BASE/"normalized-quote-bands.json").read_bytes()
    quotes=json.loads(quotes_bytes)
    selected=[row for row in quotes["rows"] if F(row["T_decimal_input"])==T]
    if [row["row_id"] for row in selected]!=list(range(1,13)):
        raise ValueError("frozen first-maturity quote row order changed")
    rows=[];start=0
    for quote in selected:
        m=fraction(quote["moneyness_fraction"])
        k=mo.log_endpoint(m);prefactor=I(m).sqrt()/dy.PI
        integral=2*phis[0][1].re
        for u,phi in phis[1:]:
            phase=-u*k
            phase_c=C(component.trig(phase,True),component.trig(phase))
            integral+=(phase_c*phi).re/(u*u+F(1,4))
        approximation=1-H*prefactor*integral
        grid=I(m).sqrt()*mo.signed_exp(STRIP*absolute(k,I))/strip_denominator
        tail=prefactor*tail_integral
        nodes=H*prefactor*eps_sum
        used_nodes=H*prefactor*eps_used;omitted_nodes=H*prefactor*eps_omitted
        total=grid+tail+nodes
        true_price=approximation+I(-total.hi,total.hi,True)
        # Proven true-martingale call bounds, not data-dependent clipping.
        intrinsic=max(F(0),1-m)
        true_price=I(max(I(intrinsic).lo,true_price.lo),min(S,true_price.hi),True)
        if true_price.lo>true_price.hi:raise ValueError("model price interval contradicts arbitrage bounds")
        rows.append({"row_id":quote["row_id"],"T":"1/2","K":quote["K_decimal_input"],
            "m":str(m),"stored_field_price":approximation.bounds(),
            "true_normalized_price":true_price.bounds(),
            "budgets":{"grid":grid.bounds(),"true_discrete_tail":tail.bounds(),
                "all_finite_node_errors":nodes.bounds(),
                "continuous_residual_nodes":used_nodes.bounds(),
                "true_CF_omitted_finite_nodes":omitted_nodes.bounds(),
                "dyadic_arithmetic":"contained in displayed outward endpoints; no binary64 error omitted"}})
    result={"status":"EXACT_F8_T05_PRICE_ENCLOSURES_WITH_SUPPLIED_CONTINUOUS_RESIDUAL_CERTIFICATE",
        "contract_id":"SPX-IV-normalized-alpha-profile-12-T05-v1",
        "scope":"first maturity T=0.5, twelve strikes only; no remaining-maturity or unrestricted-calibration result",
        "model_probabilistic_foundation":"model-admissibility.md",
        "price_certificate":"F8/R1/R4, D-type positive-kernel exponent error, whole-curve true tail, plus mandatory externally certified continuous residual input",
        "alpha_lower":str(alpha_l),"alpha_upper":str(alpha_u),"T":"1/2","nu":str(NU),"rho":str(RHO),"kappa":"0",
        "h":str(H),"strip_a":str(STRIP),"solver_cutoff":str(solver_cutoff),"grid_cutoff":str(cutoff),
        "omitted_approximate_CF_nodes":"zero; true discrete tail charged, never error zero",
        "source_sha256":{"exponents":hashlib.sha256(exponent_bytes).hexdigest(),
            "residual":hashlib.sha256(residual_bytes).hexdigest(),"field":exponents["field_sha256"],
            "quotes":hashlib.sha256(quotes_bytes).hexdigest(),
            "aggregator":digest(Path(__file__)),
            "D_type_error_identity_proof":digest(args.exponent_error_proof)},
        "true_CF_comparison_input_sha256":hashlib.sha256(direct_bytes).hexdigest() if direct_bytes is not None else None,
        "additional_proof_sha256":direct_source_hashes,
        "finite_sum_object":"hybrid: stored exponents only at usable certified residual nodes; approximate CF exactly zero at every deliberately omitted finite node",
        "D_type_exponent_error_mass_upper_enclosure":mass_bound.bounds(),
        "true_tail_whole_curve_coefficient_lower":str(c),
        "tail_parameter_bounds":{
            "actual_used_tail":"direct true-Riccati real-part comparison and positive-kernel partition" if direct_tail_rate is not None else "whole-curve auxiliary Laplace/Cauchy-Schwarz bound",
            "tail_proof_equation":"direct-real-tail.md (19)-(25)" if direct_tail_rate is not None else "fractional-exponent-linearization.md (20), algebraically canceled scale",
            "actual_uniform_decay_coefficient_lower":str(c)},
        "fallback_whole_curve_parameter_bounds":{"used_for_this_result":direct_tail_rate is None,
            "z_over_Gamma_per_u":z_over_gamma_per_u.bounds(),"J0_T":J0.bounds(),
            "Gamma_1_plus_alpha_uniform_lower":str(F(gamma1_lower,S)),
            "proof_equation":"fractional-exponent-linearization.md (20), auxiliary Laplace/Cauchy-Schwarz fallback"},
        "rows":rows,"node_error_cover":node_report,
        "aggregation_price_vector":[{"lower":row["true_normalized_price"][0],"upper":row["true_normalized_price"][1]} for row in rows],
        "input_residual_proof_evidence":residual["proof_evidence"],
        "residual_proof_validated_by_this_aggregator":False,
        "no_global_calibration_classification_from_this_single_price_cover":True}
    # Catch a field changed during aggregation; no output survives a mismatch.
    if digest(field)!=exponents["field_sha256"]:
        raise ValueError("field changed while aggregating")
    args.output.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":result["status"],"scope":result["scope"],"alpha":[str(alpha_l),str(alpha_u)],
          "solver_cutoff":result["solver_cutoff"],"grid_cutoff":result["grid_cutoff"],
          "rows":len(rows)},indent=2))


if __name__=="__main__":main()
