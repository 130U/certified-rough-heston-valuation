# Certified Joint Pricing Errors in Rough Heston

## Abstract

We certify the error of a specified rough-Heston pricing implementation while retaining the Fourier perturbations shared by multiple strikes. A finite-history propagation theorem connects a continuously enclosed complex Riccati residual to the derivative-based pricing exponent. Its positive weights preserve the full Caputo history and the physical time scale. The resulting transform disks, analytic-strip quadrature, true-frequency tails and outward arithmetic produce a joint set containing model prices minus the actual frozen output, with its signed reference-centre shift retained. The rational production approximation and the independently certified reference follow separate proof chains. In a fixed twelve-strike experiment, finite-history propagation reduces a complete spread bound from 1.397613 to 0.378599 index points without changing the output or residual envelope. A matched quarter-year comparison gives 0.233318843 points jointly and 0.252393939 through signed marginal bounds: only the joint method certifies the 0.25-point budget. Refining omitted frequencies and changing the reference centre are reported separately from geometric improvement. A prespecified nearby five-point grid separates all ten candidate pairs jointly, versus seven marginally. Actual returned-reference and centre-corrected outputs test applicability. Deterministic operation counts distinguish output generation, certification, verification and reuse across portfolios. Failed decisions and unresolved intervals are retained. All guarantees concern the specified mathematical model and implementation, rather than market fit or realized trading loss.

**Keywords:** rough Heston; continuous residual; finite history; actual output; joint pricing error; deterministic certification.

## 1. Research question and contribution

Can a complete, verifiable bound on a numerical pricing output retain enough shared structure to change a financial certification decision? At one model parameter and maturity, every strike uses the same Fourier transform values. Independently widening each price loses the fact that the perturbation at each frequency is one common complex number. We construct the price-error set from those common variables, rather than infer dependence from observed covariance.

Our object is explicit. Let \(c^*\) denote mathematical model prices, \(c^{\rm fast}\) the stored production output, and \(\bar c\) an independent reference centre. The complete inclusion has the form

\[
c^*-c^{\rm fast}=d+\operatorname{Re}(A\delta)+r,
\qquad d=\bar c-c^{\rm fast}.
\tag{I1}
\]

Each component of \(\delta\) is a rigorously enclosed common Fourier error. The remainder \(r\) retains quadrature, finite omitted nodes, infinite tails and arithmetic. A reference refinement changes \(d\) and its certified uncertainty together. Neither the reference price nor the fast output is identified with the exact model price.

### 1.1. Three contributions, with their dependencies

The principal analytical contribution is the connection from a dissipative complex Riccati residual to the Heston exponent through a finite-history kernel. Theorem 3.3 states this result near the beginning of the paper. The initial curve term and the physical factor \(\nu^{-1}\) remain explicit. Existing Caputo convexity and positive-resolvent results supply the comparison mechanism; the model-specific pricing-functional composition, certified history weights and complete output budget are the contribution developed here.

The second contribution is a complete implementation-level financial certificate. Shared transform disks are translated to the actual output and evaluated in portfolio and finite-objective directions. The quarter-year matched comparison isolates a certification decision changed by the joint structure. The unified ablation distinguishes propagation, time-local envelopes, omitted-frequency certification and recentering. Support functions, convexity and sorting a fully known unit-cost menu are established tools, rather than separate novelty claims.

The third contribution is a checkable structural domain for the specified Gatheral--Radoicic rational construction, together with an independently generated reference certificate. The all-frequency result has explicit restrictions on correlation, fractional order and mean reversion. The numerical references do not derive their residual certificates from the algebraic sign proof. A nearby-parameter protocol and output controls probe the method's transfer and its appropriate workload.

| Proof chain | Inputs and conclusion | Role in the price certificate |
|---|---|---|
| Rational construction | Endpoint matching, raw determinant and numerator signs; well-defined Padé output and left-half-plane structure | Defines and checks the specified production formula on its stated domain |
| Independent reference | Fixed field, full continuous residual, dissipation, finite-history exponent and complete Fourier error | Certifies the reference transform and model-price inclusion |
| Output translation | Stored fast values and independently enclosed reference centre | Converts the reference inclusion into error of the actual output |

The chains share the mathematical model. A successful Padé sign certificate does not by itself certify its pricing error. Conversely, the independent-reference residual route does not require the Padé trajectory to serve as its reference field.

### 1.2. Related work and the precise evidence distinction

Gatheral--Radoicic [GR2019, GR2023v1] construct two-end rational approximations. Jeng--Kilicman [JK2020, JK2021] analyse global Padé approximations and public SPX data. The formula and endpoint-matching method used here are theirs. Our structural statement concerns the raw matching system throughout its explicitly certified domain.

Abi Jaber--El Euch [AbiJaberElEuch2018v1] supply the Volterra model and affine transform. Li--Liu [LiLiu2018] establish Caputo convexity through regularization; Kopteva [Kopteva2021v2] propagates a time-dependent residual with a positive fractional inverse. Simon [SimonCM2015] supplies Mittag--Leffler positivity, and Trefethen--Weideman [TrefethenWeideman2014] supplies strip trapezoidal analysis. We state the exact regularity bridge consumed here and attribute these mechanisms.

Ben Hammouda et al. [BenHammouda2026v1, Section 3.2] develop error-controlled multilevel rough-Heston quadrature. In their practical tolerance procedure, unavailable constants are replaced by numerical error indicators, and tolerance attainment is assessed numerically rather than certified a posteriori. Their useful algorithmic error-control objective differs from our complete deterministic enclosure of a stored output, including tails and arithmetic. This distinction is specific to the cited version and procedure; it is not a claim that all other rough-Heston methods lack rigorous analysis.

Boyarchenko--de Innocentis--Levendorskii [BL2025v1] address reliable pricing, numerical bias and incorrect calibration. Their modified Adams method is a relevant numerical comparison. Their Conformal Bootstrap is explicitly an ad-hoc principle, and is not treated here as a deterministic interval guarantee. Hager--Kreher [HK2026v1] develop analytic expansions in the Hurst parameter and local convergence results; those results address a different approximation object. Bayer--Breneis [BBWeak2023v1, BBSimulation2023v1] control Markovian kernel approximations and investigate low-dimensional simulation. Comparisons therefore state the model, output and guarantee being compared.

This bounded literature comparison supports the particular contribution claimed above. It does not establish priority over every unpublished or contemporaneous method. The classical Heston original-chain analysis is preserved as a separate extension, with its own probability objects and incomplete annual monetary certificate; it is not a main contribution of this rough-Heston paper.
