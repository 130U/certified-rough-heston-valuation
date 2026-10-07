# Technical evidence appendix

We use twelve quotes at the mathematical maturity \(T=1/2\) from the public SPX sample representing ordinary market conditions. Strikes range from 3700 to 4800 in steps of 100. The original CSV is identified by commit 860049da2b7486fe8aa509061eff23cc28c2ef89 in the WoonJeng data repository. The market bid and ask implied-volatility columns and the authors' model-output columns are identified separately. Market quotes define the objective; the error analysis in this paper supplies the model-price intervals.

The experiment uses normalised call prices with \(D=1,F=4221.86\). Decimal IV and maturity values in the CSV are treated as exact rational inputs. Standard Black–Scholes conversion of the bid and ask IVs gives \(B_i,A_i\). The target is the price midpoint \(M_i=(B_i+A_i)/2\), rather than the Black–Scholes price obtained from the reported midpoint IV. These inputs jointly define the normalised quote setting below.

Fix \(\rho=-.7445,\nu=.2897,\lambda_R=\kappa=0\) and the entire forward variance function
\[
\xi_*(t)=.0721+(.0262-.0721)
E_{.5286}(-.5037t^{.5286}).
\tag{8.1}
\]
The curve exponent .5286 and curve parameter .5037 remain fixed. Changing \(\alpha\) neither recomputes the curve nor assigns .5037 to Riccati mean reversion. These values are the published rounded fitted parameters in [JK2021] and define a candidate comparison with the other inputs fixed.

The candidate set is
\[
\Theta_{\rm finite}=\{13/25,3/5,9/10\},\qquad
H=\alpha-\tfrac12\in\{.02,.1,.4\}.
\tag{8.2}
\]
This is a conditional objective profile with all other parameters and the complete curve held fixed. The threshold \(H_c=.1\) distinguishes the lower- and higher-H candidates in this comparison. All three satisfy \(H<.5\), so the classification is within the roughness candidates rather than between rough and classical Heston models. All assertions in this section concern the complete three-element set (8.2).

The model prices \(c_i(\alpha)=C_i(\alpha)/(DF)\) arise from the admissible nonnegative Volterra variance model and its exact affine transform. The model and kernel assumptions of AbiJaberElEuch2018v1 are verified individually in this paper; admissibility is established at the probability-model level. Define
\[
J(\alpha)=\frac1{24}\sum_{i=1}^{12}
 [c_i(\alpha)-M_i]^2,\qquad
J_{\rm band}(\alpha)=\frac1{24}\sum_{i=1}^{12}
 \operatorname{dist}(c_i(\alpha),[B_i,A_i])^2.
\tag{8.3}
\]
Thus the normalised price RMS is \(\sqrt{2J}\), rather than \(\sqrt{J/6}\). The same normalisation applies to the objective intervals, finite-candidate gap, and stability constants.

| α | H | Rigorous model J interval | Rigorous model-price RMS interval | Rigorous implemented Padé J interval |
|---|---|---|---|---|
| 0.52 | 0.02 | [0.0000000068962, 0.0000001833669] | [0.00011744, 0.00060559] | [0.0000000708602, 0.0000000708603] |
| 0.60 | 0.10 | [0.0000004535720, 0.0000006021720] | [0.00095244, 0.00109743] | [0.0000006127366, 0.0000006127367] |
| 0.90 | 0.40 | [0.0000082343900, 0.0000083484458] | [0.00405817, 0.00408619] | [0.0000081393603, 0.0000081393604] |

All displayed endpoints are decimal outward roundings of rational bounds; the decisions use the untruncated exact rational endpoints. The unique minimiser of the model objective is α=0.52, H=0.02. A strict lower bound on the gap between its objective and those of its competitors is 0.0000002702052. The implemented Padé output has the same unique finite-set minimiser, as certified by strict interval separation.

For ε=0, the outer set of exact optimal candidates is \(\{13/25\}\). The specified higher-H candidates with α≥.6 are strictly separated from this optimum.

| α | Rigorous model J_band interval | Rows strictly excluding quote consistency | All-row quote consistency certified |
|---|---|---|---|
| 0.52 | [0.0000000005732, 0.0000000877280] | [8, 9] | No |
| 0.60 | [0.0000003444775, 0.0000004648236] | [5, 6, 7, 8, 9, 10, 11] | No |
| 0.90 | [0.0000076345237, 0.0000077422463] | [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] | No |

Least-squares ordering and quote consistency are determined separately from objective intervals and rowwise price intervals. The following tables report the prices supporting these two model-validation results.

#### α=0.52, H=0.02

| K | Rigorous quote-midpoint interval | Rigorous normalised model-price interval | Implemented Padé dyadic output (displayed value) | Total model-price error bound for this output |
|---|---|---|---|---|
| 3700 | [0.13916863, 0.13916864] | [0.13882872, 0.13937153] | 0.13910887 | 0.00028016 |
| 3800 | [0.11921230, 0.11921231] | [0.11858902, 0.11913912] | 0.11888921 | 0.00030019 |
| 3900 | [0.09981335, 0.09981336] | [0.09909480, 0.09965209] | 0.09943278 | 0.00033799 |
| 4000 | [0.08123198, 0.08123199] | [0.08055552, 0.08111992] | 0.08092667 | 0.00037115 |
| 4100 | [0.06371452, 0.06371453] | [0.06322696, 0.06379836] | 0.06361496 | 0.00038801 |
| 4200 | [0.04759685, 0.04759686] | [0.04740368, 0.04798201] | 0.04781654 | 0.00041287 |
| 4300 | [0.03333802, 0.03333803] | [0.03349166, 0.03407684] | 0.03393723 | 0.00044558 |
| 4400 | [0.02173166, 0.02173167] | [0.02200137, 0.02259332] | 0.02244498 | 0.00044361 |
| 4500 | [0.01316937, 0.01316938] | [0.01332823, 0.01392686] | 0.01373568 | 0.00040746 |
| 4600 | [0.00760335, 0.00760336] | [0.00746696, 0.00807221] | 0.00785225 | 0.00038529 |
| 4700 | [0.00434644, 0.00434645] | [0.00393703, 0.00454881] | 0.00430503 | 0.00036801 |
| 4800 | [0.00253419, 0.00253420] | [0.00199815, 0.00261641] | 0.00232396 | 0.00032582 |

#### α=0.60, H=0.10

| K | Rigorous quote-midpoint interval | Rigorous normalised model-price interval | Implemented Padé dyadic output (displayed value) | Total model-price error bound for this output |
|---|---|---|---|---|
| 3700 | [0.13916863, 0.13916864] | [0.13908096, 0.13925890] | 0.13914793 | 0.00011096 |
| 3800 | [0.11921230, 0.11921231] | [0.11900101, 0.11918134] | 0.11908020 | 0.00010114 |
| 3900 | [0.09981335, 0.09981336] | [0.09970355, 0.09988623] | 0.09981101 | 0.00010746 |
| 4000 | [0.08123198, 0.08123199] | [0.08138513, 0.08157015] | 0.08152385 | 0.00013873 |
| 4100 | [0.06371452, 0.06371453] | [0.06429081, 0.06447812] | 0.06445106 | 0.00016025 |
| 4200 | [0.04759685, 0.04759686] | [0.04869874, 0.04888832] | 0.04888577 | 0.00018704 |
| 4300 | [0.03333802, 0.03333803] | [0.03496352, 0.03515534] | 0.03518748 | 0.00022397 |
| 4400 | [0.02173166, 0.02173167] | [0.02351737, 0.02371142] | 0.02375739 | 0.00024002 |
| 4500 | [0.01316937, 0.01316938] | [0.01471126, 0.01490749] | 0.01493438 | 0.00022313 |
| 4600 | [0.00760335, 0.00760336] | [0.00857862, 0.00877702] | 0.00878309 | 0.00020447 |
| 4700 | [0.00434644, 0.00434645] | [0.00474038, 0.00494092] | 0.00492883 | 0.00018845 |
| 4800 | [0.00253419, 0.00253420] | [0.00255071, 0.00275338] | 0.00270300 | 0.00015230 |

#### α=0.90, H=0.40

| K | Rigorous quote-midpoint interval | Rigorous normalised model-price interval | Implemented Padé dyadic output (displayed value) | Total model-price error bound for this output |
|---|---|---|---|---|
| 3700 | [0.13916863, 0.13916864] | [0.13880016, 0.13883098] | 0.13876501 | 0.00006596 |
| 3800 | [0.11921230, 0.11921231] | [0.11929811, 0.11932934] | 0.11923074 | 0.00009859 |
| 3900 | [0.09981335, 0.09981336] | [0.10073709, 0.10076873] | 0.10063802 | 0.00013071 |
| 4000 | [0.08123198, 0.08123199] | [0.08327826, 0.08331031] | 0.08315433 | 0.00015597 |
| 4100 | [0.06371452, 0.06371453] | [0.06710772, 0.06714016] | 0.06696694 | 0.00017321 |
| 4200 | [0.04759685, 0.04759686] | [0.05242401, 0.05245684] | 0.05228161 | 0.00017523 |
| 4300 | [0.03333802, 0.03333803] | [0.03943228, 0.03946550] | 0.03931664 | 0.00014886 |
| 4400 | [0.02173166, 0.02173167] | [0.02834450, 0.02837811] | 0.02828552 | 0.00009258 |
| 4500 | [0.01316937, 0.01316938] | [0.01934300, 0.01937699] | 0.01935637 | 0.00002061 |
| 4600 | [0.00760335, 0.00760336] | [0.01249183, 0.01252619] | 0.01257890 | 0.00008707 |
| 4700 | [0.00434644, 0.00434645] | [0.00765389, 0.00768862] | 0.00780424 | 0.00015035 |
| 4800 | [0.00253419, 0.00253420] | [0.00449079, 0.00452590] | 0.00467714 | 0.00018635 |

The implemented Padé procedure is the selected six-condition GR [3/3] approximation. It uses a 256-point Jacobi rule for the derivative-based exponent and an eighth-order composite Gauss–Legendre rule for Fourier inversion with a fixed truncation limit of 200. The recorded files identify the Python/NumPy implementation and exact source versions. Each finite numerical output \(c^P\) is saved as an exact dyadic rational. The model-price reference interval gives
\[
|c^P-c|\le\max\{|c^P-c^-|,|c^P-c^+|\}.
\tag{8.12}
\]
This bound includes the implementation's state, exponent, quadrature, truncation, and floating-point errors. The saved outputs can therefore be compared directly without a separate certification of an infinite-integral analytic Padé price. The numerical objective uses the same quote-price midpoint intervals. We assert selection preservation only when both the numerical and model objectives are strictly separated on the finite set and have the same minimiser. The assertion concerns the specified implementation, candidates, and input setting.

The constant state barrier in Section 4 is useful for a uniform-in-time guarantee, but using it before the pricing integral can lose the finite history relevant to a particular maturity. We now retain that history. The fractional comparison and positive resolvent are established tools [Kopteva2021v2]; the following result connects them to the derivative-based pricing exponent, in the physical time scale, without requiring numerical evaluation of a Mittag--Leffler resolvent.

**Theorem 3.3 (finite-history pricing envelope).** Let \(0<\alpha<1\), \(\nu>0\), and let the target and fixed reference states \(Z,\widehat Z\in AC[0,T]\) have zero initial value. Suppose

\[
D_C^\alpha Z=\nu F(Z),\quad
r=D_C^\alpha\widehat Z-\nu F(\widehat Z),\quad |r(t)|\le R(t),
\qquad F(z)=-b+dz+z^2/2,
\tag{N1}
\]

where \(R\ge0\) is bounded and measurable, \(\Re d=-s_0\), \(\Re Z\le0\), \(\Re\widehat Z\le\epsilon_R\), and \(\sigma=s_0-\epsilon_R/2>0\). Let \(\xi\in AC[0,T]\), \(\xi(0)=V_0\ge0\), and \(q_\alpha=(I^{1-\alpha}\xi)'\ge0\) almost everywhere. Define both exponents using their Caputo derivatives, as in Section 5. With physical damping \(\lambda=\nu\sigma\),

\[
|L_T-\widehat L_T|
\le \nu^{-1}(q_\alpha*k_\lambda*R)(T)
\le \nu^{-1}(\xi*R)(T),
\tag{N2}
\]

where \(q_\alpha=(I^{1-\alpha}\xi)'\) and \(k_\lambda(t)=t^{\alpha-1}E_{\alpha,\alpha}(-\lambda t^\alpha)\). In particular, a constant normalized residual bound \(R/\nu\le\delta_F\) gives

\[
|L_T-\widehat L_T|\le\eta_0
=\delta_F\int_0^T\xi(s)\,ds.
\tag{N3}
\]

This conditional theorem does not establish the regularity of additional parameter domains. The original certified trajectories satisfy its prerequisites; other applications must verify them independently.

**Proof.** For \(e=Z-\widehat Z\), exact quadratic linearization gives
\(D_C^\alpha e=\nu[d+(Z+\widehat Z)/2]e-r\), whose coefficient has real part at most \(-\lambda\). For the convex regularization \(v_\varepsilon=\sqrt{|e|^2+\varepsilon^2}-\varepsilon\), the Caputo convexity inequality yields

\[
D_C^\alpha v_\varepsilon+\lambda v_\varepsilon\le R.
\tag{N4}
\]

Here \(|e|^2/\sqrt{|e|^2+\varepsilon^2}\ge v_\varepsilon\) and \(|e|/\sqrt{|e|^2+\varepsilon^2}\le1\); no ordinary chain rule is used. For an AC curve, the difference between the gradient paired with its Caputo derivative and the Caputo derivative of the convex function is a sum of nonnegative Bregman history remainders. Causal smooth approximation in \(W^{1,1}\) gives the same inequality almost everywhere, with Caputo derivatives converging in \(L^1\). The positive zero-initial-value inverse of \(D_C^\alpha+\lambda\) gives \(v_\varepsilon\le k_\lambda*R\), and the limit gives \(|e|\le k_\lambda*R\). Section 5's integration-by-parts identity then yields the first inequality in (N2).

Write \(g_\beta=t^{\beta-1}/\Gamma(\beta)\). Crucially, the curve's initial value contributes to

\[
q_\alpha=V_0g_{1-\alpha}+g_{1-\alpha}*\xi',
\quad g_\alpha*q_\alpha=V_0+\int_0^t\xi'(s)\,ds=\xi(t).
\tag{N5}
\]

The resolvent identity is \(g_\alpha-k_\lambda=\lambda g_\alpha*k_\lambda\ge0\). Associativity and positivity therefore give \(q_\alpha*k_\lambda*R\le q_\alpha*g_\alpha*R=\xi*R\). All kernels are locally integrable and the finite-horizon convolutions are absolutely integrable under the stated assumptions. This proves (N2)--(N3). The entire fractional history enters the convolution; no time cell is restarted. The factor \(\nu^{-1}\) remains because \(R\) is the physical residual. ∎

For a partition \(0=t_0<\cdots<t_M=T\) and a certified physical residual envelope \(R(t)\le R_j\) on each closed cell,

\[
|L_T-\widehat L_T|\le\eta_{\rm time}
:=\nu^{-1}\sum_{j=0}^{M-1}R_j
\left[J_0(T-t_j)-J_0(T-t_{j+1})\right],
\quad J_0(z)=\int_0^z\xi(s)\,ds.
\tag{N6}
\]

The weights are nonnegative, and are strictly positive for the frozen curve with \(V_0>0\). They are obtained from the same rigorously enclosed forward-curve moments used for the reference exponent. When residual cells and integration bins differ, taking the maximum over every intersecting residual cell is a valid bin envelope, including both boundary cells. Sampling the bin centre would not suffice.

Use the minimum of (N2), (N3), (N6), and any earlier independently valid exponent bounds for the same reference object. The resulting \(\eta_n\) proves

\[
|\phi_n-\widehat\phi_n|
\le \min\{1,|\widehat\phi_n|\}(e^{\eta_n}-1).
\tag{N7}
\]

The updated node radius is the minimum of the earlier valid radius and an outward arithmetic upper bound for the right-hand side of (N7). The factor one uses the true half-shift transform modulus bound from the verified martingale/Cauchy--Schwarz assumptions in Appendix A. The final output error remains translated by \(d=\bar c-c^{\rm fast}\); its finite omitted nodes, strip, true infinite tail, and arithmetic remainder retain their earlier complete certificates. A derivative-based exponent is required: a substitution-based exponent adds a separate residual conversion and cannot silently use (N2).

**Proposition S.1 (safe finite refinement).** Fix the output, reference, coefficients, and complete remainder. Replacing a node radius by the smaller of its old radius and a newly proved radius yields a nested joint error set. Consequently every task direction has a nonincreasing certified radius. For a task direction \(w\), choose \(R_w\) to bound the remainder support in both directions \(w\) and \(-w\), and rational \(U_n\) to bound the common node coefficient modulus. The symmetric remainder construction used in the numerical examples satisfies this requirement. Let

\[
B_0\ge R_w+\sum_nU_n\varepsilon_n^0,\quad
g=B_0-R_w-\sum_nU_n\varepsilon_n^0\ge0.
\tag{N8}
\]

An exact update \(B\leftarrow B-U_n(\varepsilon_n^{\rm old}-\varepsilon_n^{\rm new})\) preserves the invariant \(B=g+R_w+\sum_nU_n\varepsilon_n\). A financial budget is returned as certified only when \(DF(|w^\top d|+B)\le\tau\). An initially sufficient bound needs zero actions. If all finitely many admissible updates suffice and the policy visits every unprocessed action, it terminates in at most that many actions. Otherwise it returns the valid unresolved interval; this does not prove that the actual error exceeds the budget.

**Proof.** Disk inclusion is preserved by finite products, the pricing map, and addition of the same remainder. Support is monotone under inclusion. The invariant follows by subtracting one nonnegative exact decrement while retaining the initial rounding margin. The stopping and finite-exhaustion statements follow from the invariant and the finite action list. ∎

Choosing the current largest \(U_n\varepsilon_n\) is a valid scheduling policy, not a theorem of minimum cost. If all alternative radii have already been certified and every upgrade is assigned unit cost, sorting the exact decrements \(U_n(\varepsilon_n^0-\varepsilon_n^1)\) gives the minimum number of upgrades needed to satisfy a fixed scalar budget. The exchange argument replaces any selected smaller decrement by an unselected larger decrement without reducing progress. The 82-upgrade result in Section 11.3 concerns only the specified global-maximum-residual finite-history menu; it does not assert optimality for the separately computed time-local radii or other menus. Precomputing the alternative radii is real work and must be included in total cost; minimum action count does not establish minimum runtime or optimal continuous-residual generation.

The transfer is to any finite pricing map and task direction satisfying these conditions. The new connection is the finite-history exponent envelope and its complete actual-output certification interface. Positive resolvents, convexity, support functions, and the fixed-menu exchange argument remain prior tools. More general curves, additional maturities, and signed adjoint residual corrections require their own verified inputs.

To test an unresolved candidate decision with actual pricing outputs, we retain the original twelve strikes, 3700--4800, the six-month maturity, and the other model inputs, but restrict the candidate set to \(\alpha=.52,.60\). We construct synthetic target prices \(m_i=(c_i^{\rm fast,.52}+c_i^{\rm fast,.60})/2\). Interpreting the frozen fast outputs as exact dyadics makes their quadratic objectives \(J=(1/24)\sum_i(c_i-m_i)^2\) exactly equal, row by row; the common value lies in [8.8558783E-8, 8.8558784E-8]. Using the existing complete price certificates gives model-objective intervals [3.8651464E-8, 3.05889870E-7] and [3.2507356E-8, 8.9847876E-8], which overlap. The decision returns \(\{.52,.60\}\) with status `UNSEPARATED`, withholding a unique-winner certificate. As a control, the original SPX-IV-defined quote-midpoint intervals and the same two candidates and price certificates still certify \(\alpha=.52\). This is a synthetic-quote stress test, not an observed market tie, a denser continuous-parameter experiment, or a refit of other parameters. The complete price intervals retain continuous-residual, exponent, quadrature, finite-node, and true infinite-tail errors. Upstream certificates are reused rather than regenerated; exact targets, row identities, source byte identities, and execution records appear in `near-tie-diagnostic.json`.

Before the new propagation calculation, the contract fixed a one-index-point budget for the original 4400--4500 spread, preserving the field, fast output, reference centre, and complete remainder. The known earlier 1.397612095-point result is disclosed in that contract. Theorem 3.3 first recertifies the full finite history using the existing global continuous-residual bounds; this step does not regenerate a field or residual.

| α | Original complete joint points | Finite-history complete points | New full interval in points |
|---|---|---|---|
| 0.52 | 1.397613 | 0.378599 | [-0.378599, 0.045075] |
| 0.60 | 0.504126 | 0.235893 | [-0.235893, 0.083963] |
| 0.90 | 0.396808 | 0.385273 | [0.224062, 0.385273] |

The selected candidate retains its signed centre, approximately -0.166762218 points. Its original 1.230849877-point radius contains approximately 1.044985362 points from used nodes, 0.184437085 from zeroed finite nodes, and 0.001427432 from strip, infinite tail, and reference arithmetic. The complete all-node finite-history bound is 0.378599 points rounded upward, certifying the original one-point budget; a quarter-point budget remains uncertified. No actual implementation error or trading loss is observed.

With the global-maximum-residual finite-history menu, the actual contribution policy certifies one point after 82 valid upgrades, with a complete bound of 0.996744 points. Independent gain sorting also establishes 82 as the minimum upgrade count within that fixed global unit-cost menu; its corresponding signed-marginal menu needs 249. These are recertifications of existing nodes. All 513 alternative-radius computations are charged, and this is not a minimum-runtime result. The other two candidates already satisfy one point and have zero-action primary stops.

The prospective portfolio contract fixes 11 adjacent spreads, 10 adjacent three-strike butterflies, four wide spreads, and three positive baskets. No directions are selected by their results. The following one-point counts all have denominator 28; the marginal box and joint set in each scenario use that scenario's identical node radii.

| α | Old signed marginal | Old joint | New signed marginal | New joint |
|---|---|---|---|---|
| 0.52 | 0/28 | 3/28 | 28/28 | 28/28 |
| 0.60 | 14/28 | 28/28 | 28/28 | 28/28 |
| 0.90 | 27/28 | 27/28 | 27/28 | 28/28 |

At tighter matched budgets, alpha=.52 passes half a point for 13/28 signed-marginal directions and 28/28 joint directions. At a quarter point, alpha=.60 passes 1/28 versus 10/28, and alpha=.90 passes 13/28 versus 20/28. Both methods use the upgraded radii in these comparisons.


All 84 joint intervals lie inside the corresponding signed marginal intervals. The legal directional payoff intersection produces no additional tightening in these cases, a retained negative result. The complete ledgers include positive baskets, wide spreads, and every failed budget. There remains one maturity and the three original candidates. Additional maturities and truly close parameter candidates lack complete new upstream certificates; the synthetic fast-objective tie remains solely an overclaim-rejection diagnostic.

The selected candidate is additionally regenerated over all 513 used nodes and 8189 closed time cells, with exact agreement of every old residual, startup and half-plane endpoint. The preselected 128 physical-time bins use the maximum over every intersecting certified cell and rigorous J0 difference weights. The complete bound further tightens to 0.367258782 points, retaining all omitted nodes, centre and remainder. `time-local-results.json` records the complete ledger and costs; fractional history is not restarted.

When the fully precomputed time-local radii are allowed, independent gain sorting gives a different fixed menu with minimum 81 upgrades: the first 80 yield 1.001460253 points and the first 81 yield 0.997350106 points, certifying one point. The corresponding signed-marginal time-local menu needs 245, with the same centre and remainder. This menu and the global menu with 82 have different alternative radii. The time-local menu also requires complete residual regeneration and all 513 radius computations.

The following definitions specify all 28 directions. Let \(K_i=3700+100i\), \(0\le i\le11\), and let \(e_i\) denote one option unit at strike i; unspecified components are zero.

| Portfolio family | Count | Complete position definition | Gross option units |
|---|---|---|---|
| Adjacent spreads | 11 | \(e_i-e_{i+1}\), \(i=0,\ldots,10\) | 2 |
| Adjacent butterflies | 10 | \(e_i-2e_{i+1}+e_{i+2}\), \(i=0,\ldots,9\) | 4 |
| Wide spreads | 4 | \(e_0-e_3,e_3-e_6,e_6-e_9,e_0-e_{11}\) | 2 |
| All-strike basket | 1 | \(12^{-1}\sum_{i=0}^{11}e_i\) | 1 |
| Lower-strike basket | 1 | \(6^{-1}\sum_{i=0}^{5}e_i\) | 1 |
| Upper-strike basket | 1 | \(6^{-1}\sum_{i=6}^{11}e_i\) | 1 |

The wide endpoints are 3700/4000, 4000/4300, 4300/4600, and 3700/4800. Each option unit is priced in index points; the displayed weights are the fixed position notionals. The reporting currency multiplier is one currency unit per index point; no exchange-contract dollar notional is asserted. With \(c=C/(DF)\), this task has \(DF=4221.86\). Scaling every position by \(a\) scales its absolute-error bound by \(|a|\), so pass counts at a fixed one-point threshold can change. Each positive basket has total weight one; spreads and butterflies have no further normalization. The full direction-by-direction JSON agrees with this table.

Finite-horizon propagation reuses the global continuous residuals and reduces the selected complete bound from 1.397612095 to 0.378598956 points, approximately 72.91%. The time-local envelope then reduces it to 0.367258782 points, an additional approximately 0.011340174 points or 3.00%; their costs are reported separately. The contribution of shared geometry is isolated with matched new node radii: at alpha=.52 and a half-point budget the signed marginal/joint counts are 13/28 and 28/28; at alpha=.60 and a quarter-point budget, 1/28 and 10/28; and at alpha=.90 and a quarter-point budget, 13/28 and 20/28. At one point both new methods achieve 28/28 for alpha=.52, so the entire old-to-new improvement cannot be attributed to shared geometry.