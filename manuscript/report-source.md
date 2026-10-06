# Structural Analysis of Heston Pricing Error and Its Financial Implications

## Abstract

This paper studies the structure of numerical pricing error in Heston models and its implications for financial decisions. For the positive-part variance Euler scheme in the classical Heston model, we relate multiple pricing residuals to the common state distribution of the original discrete chain, construct a joint price-error set, and characterize directional portfolio bounds and strict tightening through its support function. Exact pricing functions and approximate functions satisfying growth, trace, and integrability conditions admit the same residual identity; an explicit approximate function satisfies these conditions without solving the continuous pricing equation. For the existing six-condition, two-point, third-order rational approximation in the rough Heston model, we first analyze the unnormalized matching determinant and its Cramer numerators, then establish nonsingularity, a nonvanishing positive-time denominator, and preservation of the left half-plane. Within a specified parameter domain, the structural result covers every real Fourier frequency. One-sided dissipativity of the complex Riccati equation converts an independently evaluated Caputo residual into a state-error bound. A positive-kernel representation of the characteristic exponent propagates this bound to prices, and a strict objective gap establishes stability of finite candidate selection. In a normalized, six-month pricing example defined by a public SPX sample, the model objective values of three candidates are strictly separated, and both the continuous-time model and the specified third-order procedure select \(\alpha=.52\). The same price intervals support quote-consistency tests and error control for a call spread. Each conclusion holds under its stated model, parameter, and pricing assumptions.

**Keywords:** Heston model; numerical pricing; joint error; fractional Riccati equation; rational approximation; dissipativity; stability of candidate selection.

## 1. Introduction

Numerical error in option pricing is commonly assessed through step-size convergence, comparisons with a reference solution, or error estimates for individual prices. Financial decisions often involve several prices simultaneously. Spread valuation uses a difference of two prices, calibration fits a collection of prices, and parameter selection compares several objective values. A numerical basis for these decisions requires analysis of the relationships among price errors and of their propagation from model states to the prices and objectives actually used.

We address two questions. First, when several prices are computed from the same discrete stochastic process, how does shared state information constrain their joint error? Second, when a fast rational approximation is used for the complex fractional equation in rough Heston, how can verifiable properties of the approximate trajectory produce model-price intervals and establish stability of parameter-candidate rankings?

For classical Heston, we fix the positive-part variance Euler update and the log-stock update based on the current variance. Both updates use the same Gaussian increment, which determines the original discrete chain. The full positive-part one-step kernel, the continuous future kernel, and a finite telescoping decomposition yield residual constraints for multiple pricing modes in terms of shared state probabilities. The pricing map turns these constraints into a joint error set. Portfolio-error bounds follow from its support function in the relevant direction.

For rough Heston, we fix the six-condition, third-order construction of Gatheral–Radoičić [GR2019, GR2023v1]. We study its mathematical properties and the conditions for its financial use. The matching equations involve a determinant whose nonvanishing must be established, so we analyze the unnormalized algebraic quantities before division. Complex frequencies produce complex-valued trajectories, so we control the error modulus using one-sided dissipativity. Fourier pricing involves a complete integral, so we combine node errors, quadrature error, and a high-frequency tail bound into price intervals. These steps respectively establish well-definedness of the construction, error relative to the exact solution, and the final pricing error.

The analysis is applied to a specific financial problem. Using a public SPX sample, we compare three roughness candidates while holding the forward variance curve and the other parameters fixed. Rigorous intervals for the model objective establish a strict gap between candidates. The same computation provides quote-band tests and a call-spread error interval. The results therefore support pricing-library validation, ranking checks, and control of numerical accuracy in portfolio valuation.

### 1.1. Main results

The results have four components.

First, for the classical Heston discretization, we construct a joint error set constrained by the common state distribution. The set preserves compatibility among residuals and provides a support-function representation and a criterion for strict tightening in a pricing direction.

Second, exact pricing functions and approximate functions satisfying prescribed growth, trace, and residual-integrability conditions enter the same signed bias identity. An explicit approximate function shows that the framework applies to functions that are not exact solutions of the continuous pricing equation.

Third, we establish structural theorems for the existing third-order rational approximation. At the central frequency, the result covers \(\alpha\in(1/2,1)\) and \(s\in[0,1/2]\) and includes positivity of denominator coefficients, an explicit lower bound, and shape preservation. For complex frequencies, the result covers every real frequency and every positive time on \(\alpha\in[.52,.60]\), \(\rho=-.7445\), \(\kappa=0\).

Fourth, when a complex reference trajectory satisfies a one-sided dissipativity condition, an independent Caputo residual provides a state-error bound. The characteristic exponent and Fourier integral propagate that bound to price intervals. For the three candidates specified here, these intervals establish that the continuous-time model and the designated numerical procedure select the same optimum.

These results serve distinct purposes. The joint error set describes compatibility among prices; the structural theorem specifies a domain in which the rational formula can be used; the residual bound controls the distance to the exact solution; and the price intervals and objective gap certify financial decisions. We prove these connections separately and combine them in the applications.

### 1.2. Related work

Heston [Heston1993] established an affine pricing representation for the classical stochastic-volatility model. Exponential integrability and weak-error analysis provide important foundations for residual analysis of its discretizations. Cozma–Reisinger [CozmaReisinger2016] study exponential integrability of CIR Euler-type schemes, while Mickel–Neuenkirch [MickelNeuenkirch2022v2] study weak convergence orders for log-Heston Euler-type discretizations. Building on these tools, we analyze the specified positive-part one-step kernel and joint errors when several pricing modes use the state probabilities of the same original chain.

Recursive methods for geometrically averaged path payoffs are developed by Kim et al. [KimKimKimWee2016]. Multitarget error estimation and moment-constrained optimization have established methodological foundations [Hartmann2008, BertsimasPopescu2002]; support functions and convex-set operations are standard tools of convex analysis [BoydVandenberghe2004]. Our model-specific analysis makes the constraints valid for the same original discrete chain and propagates them through the complete pricing map. The resulting directional conclusions depend on the particular joint constraints.

Gatheral–Radoičić [GR2019] introduced a two-endpoint rational approximation to the rough Heston Riccati solution. Their generalization and implementation include mean reversion [GR2023v1, GatheralCode2023]. Jeng–Kiliçman [JK2020] study a fourth-order global Padé approximation and subsequently perform SPX calibration and release related data [JK2021, WoonJengSPXDataset2021Frozen]. We use the existing six-condition, third-order formula, analyze its matching system, denominator, and half-plane properties, and study the pricing error and candidate selection associated with specified numerical outputs.

Two-point Padé approximations and positive-denominator results also depend on the underlying function class. For instance, multipoint Padé approximants to Stieltjes functions admit two-sided error estimates [Gilewicz2005]. Here we work directly with the unnormalized algebraic quantities of the matching system and establish the required signs individually. These conditions and the parameter domain determine the objects covered by the theorem.

The fractional stability analysis uses the Caputo convexity tool of Li–Liu [LiLiu2018] and positivity and comparison properties of Mittag–Leffler functions [Simon2014, NIST2010]. We treat the complex equation as a two-dimensional real problem and obtain a positive-kernel comparison from a convex regularization of the error modulus and the one-sided dissipativity of the Riccati divided difference. The underlying probability model and affine transform follow the forward variance formulation of Abi Jaber–El Euch [AbiJaberElEuch2018v1]. Pricing quadrature uses Fourier valuation and analytic-strip methods [EberleinGlauPapapantoleon2008v1, TrefethenWeideman2014].

We distinguish established tools from the results proved here. The rational formulas, Itô formula, convex analysis, Caputo convexity, and analytic-strip quadrature are existing tools. The effective residual constraints in the specified models, structural results on continuous parameter domains, and the price and selection conclusions derived from them form the subject of this paper. The relevant propositions are stated by construction, assumptions, and conclusion.

## 2. Proof Structure and Mathematical Role

### 2.1. From shared state constraints to joint pricing error

For classical Heston, we first establish a shared-probability constraint for one-step residuals. At time level \(j\) and pricing mode \(i\), the residual satisfies
\[
|r_{ji}|^2\le a_{ji}\cdot\pi_j,
\]
Here \(\pi_j\) is the state-occupation probability of the original discrete chain at that time level. Every mode uses the same \(\pi_j\), and the probabilities at all time levels belong jointly to a compact convex set containing the actual occupation vector. Shared probabilities are essential: extreme residuals for different modes must be compatible with the same state distribution.

A finite telescoping decomposition converts these local constraints into mode-error inclusions. The complete pricing map then gives a price-error set \(\mathcal E\). Let \(\widehat p\) denote the numerical price vector, \(p\) the model price vector, and suppose \(p-\widehat p\in\mathcal E\). For a deterministic direction \(w\), define the support function
\[
h_{\mathcal E}(w)=\sup_{e\in\mathcal E}w\cdot e.
\]
The portfolio price therefore satisfies
\[
w\cdot\widehat p-h_{\mathcal E}(-w)
\le w\cdot p
\le w\cdot\widehat p+h_{\mathcal E}(w).
\]
This relation translates the geometry of the joint error directly into a valuation interval. We also give a criterion for strict tightening of this joint set relative to its smallest coordinate box in a specified direction.

### 2.2. From the residual identity to admissible approximate functions

The second classical Heston argument uses the generator of the continuous process and the original discrete one-step operator. For approximate functions satisfying global growth, prescribed trace, and residual-integrability conditions, piecewise Itô calculus, conditional expectation, and removal of stopping yield a signed bias identity. It retains the continuous residual, discrete one-step defect, and interface contributions.

The exact continuous pricing function enters this framework. We also construct an explicit approximate function with the same terminal trace, verify its growth and integrability, and calculate its nonzero continuous residual. The framework thus depends on independently verifiable function properties; solving the exact pricing equation is one way to obtain those properties. The benefit is that more tractable approximate functions can be used while retaining the complete bias identity and corresponding error bounds.

### 2.3. From unnormalized matching algebra to complex dissipativity

For rough Heston, we first analyze the determinant \(\Delta\) and Cramer numerators \(N_j\) of the six-condition matching system. We establish \(\Delta\ne0\) before defining the normalized denominator coefficients \(q_j=N_j/\Delta\). Sign constraints on a continuous parameter domain then give a nonvanishing denominator and left-half-plane preservation of the approximate trajectory.

Consider the normalized Riccati equation
\[
D_C^\alpha H=-b+dH+\tfrac12H^2,
\qquad d=-s_0+i\rho u,
\]
and a reference trajectory \(\widehat H\) with the prescribed regularity and zero initial value. If
\[
\operatorname{Re}\widehat H\le\varepsilon_R,
\qquad 0\le\varepsilon_R\le2s_0,
\qquad
\eta\ge|D_C^\alpha\widehat H-F(\widehat H)|,
\]
then the dissipativity rate is \(\sigma=s_0-\varepsilon_R/2\ge0\). A two-dimensional convex Caputo inequality converts error-modulus control into a positive-kernel comparison. In particular, when \(\sigma>0\) and \(\eta\le\delta\),
\[
|H(x)-\widehat H(x)|
\le\frac{\delta}{\sigma}
\{1-E_\alpha(-\sigma x^\alpha)\}
\le\frac{\delta}{\sigma}.
\]
The stability constant is determined by dissipativity. Frequency enters the independently evaluated residual and trajectory bounds; the propagation of error preserves the equation's dissipative structure. We give real-valued and strictly nonreal examples and prove the comparison under the same conditions.

### 2.4. From price intervals to financial decisions

The positive-kernel representation of the characteristic exponent propagates state error to exponent error. Analytic-strip quadrature and high-frequency tail bounds propagate node error to complete prices. The resulting price intervals support portfolio valuation, quote-consistency tests, and candidate comparison.

For a finite candidate set, suppose the model objective for candidate \(\vartheta\) satisfies
\[
J(\vartheta)\in[L_\vartheta,U_\vartheta].
\]
If a candidate \(\vartheta_*\) satisfies
\[
g:=\min_{\vartheta\ne\vartheta_*}L_\vartheta-U_{\vartheta_*}>0,
\]
then it is the unique optimum in that set. If \(\delta_J\) uniformly bounds the difference between the numerical and model objectives, and \(\varepsilon_{\mathrm{alg}}\) bounds the optimization error, then
\[
2\delta_J+\varepsilon_{\mathrm{alg}}<g
\]
is sufficient to preserve candidate selection. This condition links numerical accuracy to the actual decision gap, rather than imposing an isolated price tolerance unrelated to the objective.

## 3. Classical Heston: Shared States and Trial-Field Residuals

### 3.1. Fixed mathematical setting

Set $s=S/100$. The continuous process satisfies

\[
ds_t=rs_tdt+s_t\sqrt{V_t}(\rho\,dW_t+\sqrt{1-\rho^2}\,dB_t),
\qquad dV_t=(d-\kappa V_t)dt+\xi\sqrt{V_t}\,dW_t,
\]

where $d=\kappa\bar v$, $r=1/100$, and $s_0=1$. With time step $h=1/768$, the actual discrete one-step update is

\[
V'=[dh+(1-\kappa h)v+\xi\sqrt{hv}G]^+,
\]
\[
\log(s'/s)=rh-hv/2+\sqrt{hv}(\rho G+\sqrt{1-\rho^2}H),
\]

Here $G,H$ are independent standard normal random variables. The stock increment and positive-part variance update share $G$. Denote the law of the continuous process by $P$ and the law of this original discrete chain by $Q$.

The theoretical parameter domain is

\[
\kappa\in[2,4],\quad \bar v,v_0\in[3/100,3/50],\quad
\xi\in[9/50,7/25],\quad \rho\in[-4/5,-3/10].
\]

The fixed example uses

\[
\theta_*=(\kappa,\bar v,\xi,\rho,v_0)=(3,.045,.23,-.55,.045).
\]

The nine standard options are European puts with maturities $1/4,1/2,1$ and strikes $90,100,110$. The tenth instrument is an arithmetic-average Asian call spread maturing after one year with twelve monthly observations:

\[
R_{10}=(A-95)^+-(A-110)^+,\qquad
A=\frac1{12}\sum_{m=1}^{12}S_{m/12}.
\]

The eighth instrument is the one-year at-the-money put. The direction $w=\mathbf e_{10}-\mathbf e_8$ compares the pricing biases of these two instruments.

### 3.2. Shared state constraints for the original chain

#### 3.2.1. Structural conditions and the core argument

Consider finitely many multidate modes $i=1,\ldots,M$ with loadings $\alpha_{i,n}\in\mathbb C$ satisfying

\[
\Re\alpha_{i,n}\le0,\qquad
\sum_n|\Re\alpha_{i,n}|\le\frac12.
\]

The continuous future kernel is the exact affine kernel with verified integrability. Completing the real Gaussian square, integrating the full positive-part kernel, and applying a finite telescoping decomposition give the mode bias

\[
\Delta\Phi_i=\Phi_{Q,i}-\Phi_{P,i}=
\sum_{j=0}^{N-1}r_{ji}.
\]

Partition the variance axis into finitely many measurable intervals $I_r$, including zero and the unbounded tail. Define probabilities under the same original $Q$ chain by

\[
\pi_{jr}=Q(V_j\in I_r).
\]

Suppose stored nonnegative quantities $h_{jir}$ bound the corresponding weighted squared kernel residuals, and

\[
E_Q[W_{ji}^2 e^{4V_j}]\le K_j,
\quad K_j=\exp\{6/25+(73/75)jh\}.
\]

Complex Cauchy–Schwarz then gives

\[
|r_{ji}|^2\le
K_j\sum_r h_{jir}\pi_{jr}=:a_{ji}\cdot\pi_j.
\tag{H1}
\]

The essential point in (H1) is that all $i$ use **the same** $\pi_j$, and all time levels share one nonempty compact convex set \(\mathcal F\) containing the actual occupation vector. The probability constraints must be valid for the original $Q$; a mode-tilted distribution cannot be substituted for that law.

The scheme-specific proof includes the complete Gaussian positive-part integral, exact continuous future kernel, exponential moments with doubled nonpositive loadings, the atom at zero, and the unbounded tail. Together they make (H1) an effective inclusion for this model. The full proof is given in [Section 3 and Appendices A–C of the theoretical core](../docs/classical-evidence.md).

#### 3.2.2. From joint residuals to joint prices

For exact finite pricing coefficients $c_{ki}\in\mathbb C$, assume the price bias admits the representation, including the full remainder,

\[
e_k=p_{h,k}-p_{c,k}
=\Re\sum_{j,i}c_{ki}r_{ji}+R_k,
\qquad |R_k|\le\varrho_k.
\tag{H2}
\]

Define the joint outer set

\[
\mathcal E=
\left\{\left(\Re\sum_{j,i}c_{ki}z_{ji}\right)_k:
\exists\Pi\in\mathcal F,
|z_{ji}|^2\le a_{ji}\cdot\pi_j\right\}
+\prod_k[-\varrho_k,\varrho_k].
\tag{H3}
\]

This set is nonempty, compact, convex, and centrally symmetric, and $e\in\mathcal E$. For $w\in\mathbb R^{10}$, its support function is

\[
s_{\mathcal E}(w)=
\max_{\Pi\in\mathcal F}
\sum_{j,i}\left|\sum_kw_kc_{ki}\right|
\sqrt{a_{ji}\cdot\pi_j}
+\sum_k|w_k|\varrho_k.
\tag{H4}
\]

**Proof of the price propagation formula.** For fixed $\Pi$, each $z_{ji}$ lies in a complex disk. Its real-linear support in direction $w$ is exactly the modulus of the coefficient times the radius. Conditional on $\Pi$, phases can be selected independently across disks, so their supports add. Maximizing over **the same** $\mathcal F$ gives (H4). Compactness ensures attainment. The actual residuals and probabilities provide a feasible representation in (H3), establishing inclusion of the price vector. ∎

With cross-time constraints, the exact expression is $\max_{\mathcal F}\sum_j$. It separates into a sum of timewise maxima only when $\mathcal F=\prod_j\mathcal P_j$.

#### 3.2.3. Criterion for strict tightening

Let

\[
F_k(\Pi)=\sum_{j,i}|c_{ki}|\sqrt{a_{ji}\cdot\pi_j},
\quad m_k=\max_{\mathcal F}F_k,
\]
\[
\mathcal B=\operatorname{rect}(\mathcal E)
=\prod_k[-m_k-\varrho_k,m_k+\varrho_k].
\]

This is **the smallest coordinate box of the same joint outer set**. The exact support gap is

\[
\begin{aligned}
G(w)&=s_{\mathcal B}(w)-s_{\mathcal E}(w)\\
&=\min_{\Pi\in\mathcal F}\left\{
\sum_k|w_k|[m_k-F_k(\Pi)]
+\sum_{j,i}\left[
\sum_k|w_kc_{ki}|-\left|\sum_kw_kc_{ki}\right|
\right]\sqrt{a_{ji}\cdot\pi_j}\right\}.
\end{aligned}
\tag{H5}
\]

Every term is nonnegative. Hence $G(w)=0$ if and only if there is a common $\Pi_*$ satisfying both conditions:

1. For every $w_k\ne0$, it maximizes the **complete pricing row** $F_k$.
2. For each positive-radius $(j,i)$, the nonzero complex numbers $w_kc_{ki}$ lie on a common nonnegative ray.

If there is no such common witness, $G(w)>0$. This is necessary and sufficient for strict directional tightening of the constructed set relative to its smallest box. No phase condition is needed at zero radius; the gap in the zero direction is zero.

**Proof.** The common remainder box cancels exactly in the support difference. Adding and subtracting $\sum_k|w_k|F_k(\Pi)$ gives (H5). Compactness ensures that the minimum is attained. A nonnegative sum vanishes only when every active-row deficit vanishes and every complex triangle inequality at positive radius is an equality. These are precisely the two stated conditions. Conversely, substituting a common witness gives a zero gap. ∎

The characterization concerns **strict tightening of an outer set**. It neither assumes that the model price bias attains the outer boundary nor interprets the set gap as a lower bound on the actual pricing bias.

#### 3.2.4. Certified example for the original instruments

The specified terminal-level example fixes $j=767$, $\theta_*$, the original mode catalogue, and the prespecified $\mathcal P_{767}$. The partition is

\[
I_0=\{0\},\qquad I_r=((r-1)/100,r/100]\ (1\le r\le100),
\qquad I_{101}=(1,\infty).
\]

The set contains the actual probabilities under the original $Q$ and is constrained by the full mean, exponential moments, and two groups of Laplace information. It is represented by 102 nonnegative variables and 22 exact rational constraints. All nine actual one-step residual envelopes cover zero, finite intervals, and the tail.

After conjugate reduction, the complete terminal Asian pricing row is

\[
F_A(\pi)=C_A\sqrt{K_{767}}\sqrt{a\cdot\pi},\qquad C_A>0.
\]

The complete eight-frequency row for the one-year at-the-money put is

\[
F_P(\pi)=\frac{1600e^{-.01}}{\pi}\sqrt{K_{767}}
\sum_{\omega=8,24,\ldots,120}
\frac{\sqrt{d_\omega\cdot\pi}}
{\sqrt{(\omega^2+1/16)(\omega^2+25/16)}}.
\tag{H6}
\]

An exact primal–dual certificate establishes that $F_A$ has a unique maximizer $\pi^A$ supported only on intervals 1, 2, and 6. Its decimal approximation is

\[
(\pi^A_1,\pi^A_2,\pi^A_6)
\approx(.0276833515163,.0487291439380,.923587504546).
\]

The three active constraints with positive dual multipliers form a nonsingular matrix. Every unsupported index has strictly positive reduced cost, so uniqueness follows from exact algebra.

The same probability set contains an exact feasible point $\pi^B$ supported on intervals 5 and 6. Along $\pi(t)=\pi^A+t(\pi^B-\pi^A)$, the derivative of the auxiliary put row is certified to lie in

\[
\mathcal B'(0)\in
\left[
\frac{2214102728888110422476248911088843134229}
{730750818665451459101842416358141509827966271488},
\frac{2214102728888110422476248911088843134233}
{730750818665451459101842416358141509827966271488}
\right],
\tag{H7}
\]

Its lower endpoint exceeds $3\times10^{-9}$. Thus $\pi^A$ is not a maximizer of the put row. The two complete pricing rows have no common maximizer, yielding

\[
g_{767}=max F_A+max F_P-max(F_A+F_P)>0.
\tag{H8}
\]

Equation (H7) concerns the directional derivative of an auxiliary row; (H8) is a qualitative strict gap for the terminal outer set. For a construction retaining the specified modes and envelope identities and continued through valid timewise product sets, each level satisfies $g_j\ge0$, and the accumulated support gap before payoff intersections satisfies $\sum_jg_j\ge g_{767}>0$. A change in probability information, mode catalogue, or payoff-intersection rule requires application of (H5) to the resulting set.

The evidence consists of the [terminal strict-separation proposition](../docs/classical-evidence.md), [exact input](../code/classical/terminal767-input.json), [result certificate](../code/classical/terminal767-result.json), and [independent rational verification](../code/classical/terminal767-historical-review.json). The input SHA256 is `5ad2c18e9336db16e3957b9b1f6669f0f9065a13991ebed8a0498df9b942524c`. The independent verification records 407 exact-arithmetic checks.

### 3.3. A common framework for exact future-value functions and finite trial fields

#### 3.3.1. Function classes and sufficient conditions

The object is $X=(P,Q,R,\widetilde u)$, where $R$ is the same original payoff or an exact finite pricing-conversion remainder, and $\widetilde u$ is a deterministic trial field.

| Symbol | Meaning in this analysis |
|---|---|
| $A(X)$ | $\widetilde u$ is the exact continuous future-value function satisfying the integrability and regularity conditions below; its terminal and observation-time conditions agree exactly with $R$. |
| $H(X)$ | The same field satisfies global state-growth bounds, uniform integrability under squared weights, piecewise Itô regularity, genuine observation-time traces, temporal $L^1$ residual domination, terminal-discrepancy domination, and integrable defects under the original $Q$. |
| $\Phi$ | Apply the finite tower property under the original $Q$; under the original $P$, apply piecewise Itô calculus, Lyapunov-based removal of stopping, and $L^1$ traces; subtract the identities. |
| $M(X)$ | A four-term signed residual identity for the same field. |
| $B(X)$ | Certified residual bounds yield an effective interval or monetary bound for the original continuous–discrete price bias. |
| $C(X)$ | A specified finite Hermite field in time, a finite state basis, and verifiable growth, residual, and interface constraints. |
| $X_\star\in C\setminus A$ | The original thirteen-dimensional field with terminal generator completion; its certificate establishes a nonzero continuous residual while its global conditions, observation-time traces, and terminal condition hold. |

Here $H$ is a sufficient condition independently defined by field properties; it does not require the trial field to equal the unknown exact solution. For the exact future-value function, the backward equation makes the continuous residual zero, and exact observation and terminal conditions eliminate their respective defects. Consequently, $A\Rightarrow H\Rightarrow M\Rightarrow B$ recovers the telescoping formula for the exact future-value function.

Separate intervals for individual prices do not alone establish shared state structure, because they supply no cross-price compatibility witness. The trial-field extension is expressed by the identity below, while the shared-state inclusion provides a joint error framework retaining price dependence.

#### 3.3.2. Structural condition $H$

Between observation times, the full state is \(x=(s,v,A_m,\ell_m)\). The variables \(A_m\) and \(\ell_m\) record the sums of observed stock prices and log-stock prices, respectively. The exact map \(J_i\) updates the history at an observation time. The generator is

\[
\mathcal L=rs\partial_s+(d-\kappa v)\partial_v
+\frac12vs^2\partial_{ss}+\rho\xi vs\partial_{sv}
+\frac12\xi^2v\partial_{vv}.
\]

Choose a nonnegative weight \(W\), for example

\[
W=s^{-1/2}e^v+e^{-\ell_m/24}s^{-(12-m)/24}e^v,
\]

or the natural weight better suited to the arithmetic branch in the fixed setting,

\[
W^{\rm nat}=\mathfrak B_m^{-1/2}e^v+\mathfrak G_m^{-1/2}e^v,
\quad \mathfrak B_m=(A_m+(12-m)s)/12,
\quad \mathfrak G_m=e^{\ell_m/12}s^{(12-m)/12}.
\]

These weights agree across observation times. The Lyapunov estimate supplies moment bounds at continuous and discrete times; at $\theta_*$ over one year, one may take $E_PW,E_QW<5/2$, together with squared-moment bounds at continuous stopping times. Each approximate function uses one fixed weight throughout the remaining months.

The field $\widetilde u$ is locally $C^{1,2}$ on each open interval between observations, has a right-sided extension at $v=0$ suitable for Itô calculus, and has genuine one-sided traces uniformly on compact state sets. Assume

\[
|\widetilde u|\le CW,\qquad
|\mathfrak r(t,x)|\le\eta_c(t)W(t,x),\quad
\int_0^1\eta_c(t)dt<\infty,
\]
\[
|d_i(x)|\le\eta_iW(t_i-,x),\qquad
|\delta(x)|\le\eta_TW(1,x),
\]

where

\[
\mathscr D_j=Q_j\widetilde u_{j+1}-\widetilde u_j,
\quad \mathfrak r=(\partial_t+\mathcal L)\widetilde u,
\quad d_i=\widetilde u(t_i-,x)-\widetilde u(t_i+,J_ix),
\quad \delta=R-\widetilde u_N.
\tag{H9}
\]

The operator $Q_j$ includes the original positive-part kernel and any observation at the end of the step. Terminal values and jumps use the same convention, with every update counted once. Domination covers the full state space, the zero boundary, and the unbounded tail. Discrete defects under the original $Q$ are integrable and admit the full-horizon inclusion

\[
\sum_j E_Q\mathscr D_j\in[L_Q,U_Q].
\]

#### 3.3.3. Core lemma and proof: $H\Rightarrow M$

**Core lemma.** Under the stated conditions,

\[
\boxed{
E_QR-E_PR=
\sum_jE_Q\mathscr D_j
-E_P\int_0^1\mathfrak r(t,X_t)dt
+\sum_iE_Pd_i+(E_Q-E_P)\delta.}
\tag{H10}
\]

**Proof.** The finite discrete tower property gives

\[
E_Q\widetilde u_N-\widetilde u_0
=\sum_jE_Q\mathscr D_j.
\]

For the continuous process, first stop it in a compact state domain on a closed subinterval away from observation times. The local Itô stochastic integral has expectation zero. The squared-weight Lyapunov bound and \( |\widetilde u|\le CW\) give uniform integrability of the stopped field values, permitting removal of stopping. Temporal $L^1$ domination and a uniform bound on \(E_PW\) yield

\[
E_P\int_0^1|\mathfrak r(t,X_t)|dt
\le\int_0^1\eta_c(t)E_PW(t,X_t)dt<\infty,
\]

Absolute integrable domination therefore also removes stopping from the residual integral. As subinterval endpoints approach an observation time, genuine traces, continuous paths, and the same uniform-integrability bound give convergence in $L^1$. The function jump at an observation is $-d_i$. Summing over the intervals gives

\[
E_P\widetilde u_N-\widetilde u_0
=E_P\int_0^1\mathfrak r(t,X_t)dt-\sum_iE_Pd_i.
\]

Subtract the two identities and include $\delta=R-\widetilde u_N$ in both expectations to obtain (H10). The common initial value cancels exactly. ∎

Equation (H10) is signed: each contribution is determined by the residual of the same function under the discrete chain or continuous process. Established Itô and residual tools connect the growth and tail assumptions for this positive-part kernel, multiple observation dates, and unbounded state space.

#### 3.3.4. Propagation proposition: $M\Rightarrow B$

At $\theta_*$, (H10) gives

\[
|E_QR-E_PR|\le
\max(|L_Q|,|U_Q|)
+\frac52\left(\int_0^1\eta_c(t)dt+\sum_i\eta_i\right)
+5\eta_T.
\tag{H11}
\]

If the global discrete defect satisfies \( |\mathscr D_j|\le h\eta_{Q,j}W\), then

\[
|E_QR-E_PR|\le
\frac52\left(h\sum_j\eta_{Q,j}
+\int_0^1\eta_c(t)dt+\sum_i\eta_i\right)+5\eta_T.
\tag{H12}
\]

Integrability and the triangle inequality applied to (H10) prove both statements. If joint signed information on the contributions is available, one may instead take the linear image of their joint feasible set. Equations (H11)–(H12) are valid, readily computable nonnegative bounds.

#### 3.3.5. An explicit new class $C\setminus A$

The existing field uses

\[
\widetilde u_q^A=\mathfrak B_m^{-q}
\left[1+\Phi(y,v)c_q(t)\right],\quad
y=\frac{A_m}{A_m+(12-m)s},\quad z=\frac{v}{1+v},
\]

with thirteen state-basis functions

\[
\{(1-y)y^iz^j:0\le i\le2,0\le j\le3\}
\cup\{v(1-y)^2\}.
\]

Cubic Hermite interpolation is used within each original time step, and the final finite coefficients define the field as exact binary rationals. The added basis function \(\psi=v(1-y)^2\) represents exactly the linear variance term in \(L_q1\). The source is

\[
g_q=-qr\,e_{00}+\frac12q(q+1)e_\psi.
\]

Full column rank of evaluation at the fixed state points follows from a polynomial root-counting argument. Exact history-update maps determine adjacent endpoints at all observations, and the terminal value is the prescribed function. The field grows at most linearly in $v$, and the generator residual at most quadratically. The finite coefficients give

\[
|P_q|\le C_{0,q}+C_{1,q}v
\le(C_{0,q}+2C_{1,q}/e)e^{v/2},
\]
\[
e^{-v}|F_q^A|\le a_0+a_1/e+4a_2/e^2,
\]

and exponential tail bounds. These finite global bounds, regularity at zero, and the correlated Gaussian estimates for the original $Q$ establish $C\Rightarrow H$. The source completion concerns the generator applied to the terminal constant; closure of the finite space under all generator images is not required.

In the first month, the stored field has 64 time slices, 385 modes, and 3,080 mode–cell integrals. Independent 384-bit verification of the formulas establishes, at the same admissible state and the same stock phase for the full row, the following continuous-residual envelope integral:

\[
\int_{0}^{1/12}\eta_c(t)dt\ge
.003407444052031154>0.
\tag{H13}
\]

Equation (H13) comes from cell integrals of the actual generator residual at the admissible state and common phase in the original A15 construction. The triangle inequality gives a necessary lower bound for any global envelope. If this field were the exact future-value function, the actual residual integrals would vanish, contradicting the strictly positive certified lower endpoint. Thus **the same stored field** belongs to $C\setminus A$. This establishes an extension of the admissible class: nonexact future-value fields enter the original payoff bias identity and effective error bounds.

Equation (H13) gives a necessary lower bound on the global residual-envelope integral for the fixed weight. Together with the continuous-residual coefficient in (H11), it determines the tolerance required when using this approximate function. The quantity bounded below is the residual-envelope integral.

#### 3.3.6. A fully explicit analytic witness

To verify \(C\setminus A\) directly in the main text, we provide an admissible object independent of the large field-coefficient collection. Fix \(T=1\) and any \(\varepsilon>0\), and take terminal payoff \(R=s_T^{-1/2}\) and field

\[
a_\varepsilon(t)=1+\varepsilon t(1-t),\qquad
\widetilde u_\varepsilon(t,x)=a_\varepsilon(t)s^{-1/2}.
\tag{H17}
\]

The field is history-independent, has zero jumps at all observation times, has the exact terminal value, and satisfies \(1\le a_\varepsilon\le C_\varepsilon:=1+\varepsilon/4\). Set \(W_A=s^{-1/2}e^v\). The continuous squared-weight Lyapunov and original \(Q\) estimates apply, and \(|\widetilde u_\varepsilon|\le C_\varepsilon W_A\).

The exact generator yields

\[
\mathfrak r_\varepsilon
=s^{-1/2}\left\{\varepsilon(1-2t)
+a_\varepsilon(t)\left(\frac{3v}{8}-\frac r2\right)\right\}.
\tag{H18}
\]

Using \(ve^{-v}\le1/e\), a constant continuous dominating function over the full year is

\[
\eta_c=\varepsilon+C_\varepsilon\left(\frac r2+\frac3{8e}\right)<\infty.
\tag{H19}
\]

Gaussian integration of the original stock update gives exactly

\[
\mathscr D_j=s^{-1/2}
\left\{a_\varepsilon(t_{j+1})
\exp\!\left[h\left(\frac{3v}{8}-\frac r2\right)\right]
-a_\varepsilon(t_j)\right\}.
\]

Using \(|a_\varepsilon(t_{j+1})-a_\varepsilon(t_j)|\le\varepsilon h\),
\(|e^x-1|\le |x|e^{\max(x,0)}\), and
\(ve^{-cv}\le1/(ec)\), with \(c=1-3h/8>0\), we obtain the global bound

\[
|\mathscr D_j|\le h\eta_QW_A,\qquad
\eta_Q=\varepsilon+C_\varepsilon
\left(\frac r2+\frac3{8e(1-3h/8)}\right).
\tag{H20}
\]

These explicit finite constants, exact terminal and observation conditions, global regularity, and squared-moment domination directly verify \(C\Rightarrow H\). At \(t=1/2,v=r>0\), (H18) equals
\(-r(1+\varepsilon/4)s^{-1/2}/8<0\), so the field is not an exact future-value function satisfying the continuous backward equation. This gives a self-contained \(X_\star\in C\setminus A\).

For this negative-power terminal payoff, the exact continuous future-value function belongs to the admissible affine class with nonpositive loading and satisfies the established moment conditions. The same object class therefore contains both the exact future-value function in \(A\) and the nonexact field (H17); the residual identity also applies to the latter. This analytic witness establishes the extended scope. The financial example uses the original instruments and exact certificates. Equations (H19)–(H20) provide finite, full-year integrable sufficient bounds; quote-related error bounds use independent certificates for the corresponding field.

The field definition and growth and tail proofs are in the [thirteen-dimensional field specification](../docs/classical-evidence.md). Results are recorded in the [field certificate](../code/classical/field-result.json) and [independent formula verification](../code/classical/field-independent-readback.json). The field SHA256 is `665a91049e2c4dd9463cba2fa6d5cc876b5707e0923a72047dc8a1852890c5a8`.

### 3.4. Financial propagation: portfolio values and joint quote-acceptance sets

#### 3.4.1. Portfolio-value bounds

**Proposition (joint certificates for linear combinations).** Let $p_c,p_h\in\mathbb R^d$ be the discounted continuous and discrete prices at the same parameters, let $e=p_h-p_c\in\mathcal E$, and let $\mathcal E$ be nonempty and compact. For deterministic positions or price-comparison coefficients $w\in\mathbb R^d$,

\[
w^Tp_h-s_{\mathcal E}(w)
\le w^Tp_c\le
w^Tp_h+s_{\mathcal E}(-w).
\tag{H14}
\]

If $\mathcal E=-\mathcal E$, both half-widths equal $s_{\mathcal E}(w)$. If the discrete price center $\widehat p_h$ itself satisfies $n=p_h-\widehat p_h\in\mathcal N$, then

\[
w^T\widehat p_h-s_{\mathcal N}(-w)-s_{\mathcal E}(w)
\le w^Tp_c\le
w^T\widehat p_h+s_{\mathcal N}(w)+s_{\mathcal E}(-w).
\tag{H15}
\]

If the actual $(n,e)$ belongs to a joint compact set $\mathcal K\subseteq\mathbb R^{2d}$, the two-term sums in (H15) can be replaced by $s_{\mathcal K}(w,-w)$ and $s_{\mathcal K}(-w,w)$, retaining joint information about both errors.

**Proof.** Since $p_c=p_h-e$, the inequalities $w^Te\le s_{\mathcal E}(w)$ and $-w^Te\le s_{\mathcal E}(-w)$ give (H14). Next, $p_c=\widehat p_h+n-e$; controlling $w^Tn$ and $-w^Te$ separately gives (H15). Taking linear support directly over the joint $(n,e)$ set proves the final assertion. ∎

This is standard linear propagation by support functions, rather than a separate mathematical innovation. It shows how the main theory produces financial outputs: spreads, portfolio values, and prespecified comparison directions use vector-error guarantees instead of arbitrary combinations of single-instrument endpoints.

For $w=\mathbf e_{10}-\mathbf e_8$ in the original terminal example, (H8) establishes a strictly smaller directional terminal bound using the joint structure with the same information. The direction compares an arithmetic-average Asian call spread with a one-year at-the-money put. It is fixed by the setting and is not an optimal hedge or trading signal.

#### 3.4.2. Calibration acceptance and target valuation

Given a closed acceptance set $\mathcal Y$ for nine prices, a discrete price center \(\widehat p_h\), and a joint compact error-input set $\mathcal K_\theta$ containing the actual $(n,e)$, define

\[
\mathcal T_\theta=
\{(n,e)\in\mathcal K_\theta:
\widehat p_{h,\mathrm{cal}}+n_{\mathrm{cal}}-e_{\mathrm{cal}}
\in\mathcal Y\},
\]
\[
\mathcal A_\theta=
\{\widehat p_{h,10}+n_{10}-e_{10}:(n,e)\in\mathcal T_\theta\}.
\tag{H16}
\]

If the exact calibration prices satisfy the acceptance rule, the model target price belongs to $\mathcal A_\theta$. The condition $\mathcal T_\theta=\varnothing$ excludes compatibility of that parameter with the rule; otherwise the target endpoints are attained. Enlarging the joint input to a coordinate box can only enlarge or preserve the target set.

The proof uses $p_c=\widehat p_h+n-e$, compactness of the intersection with a closed acceptance condition, and attainment of linear extrema on a nonempty compact set. The rule preserves a common price-error vector. It is suited to constraining parameters using liquid standard options before valuing a path-dependent instrument. Once a valid center and complete error inputs are available for a quote specification, (H16) provides a computable screening and valuation map.

## 4. Rough Heston: Unnormalized Sign Conditions and Complex Dissipativity

### 4.1. Objects, structural conditions, and conclusions

Let \(1/2<\alpha<1\), \(u\in\mathbb R\), \(\nu>0\), and \(|\rho|\le1\), and set
\[
b=(u^2+1/4)/2,\qquad s_0=\kappa-\rho/2\ge0,\qquad d=-s_0+i\rho u.
\]
The normalized equation is
\[
D_x^\alpha H=-b+dH+\tfrac12H^2=:F(H),\qquad H(0)=0.
\tag{R1}
\]
Physical time and state are related by
\[
x=\nu^{1/\alpha}t,\qquad y=\nu t^\alpha=x^\alpha,\qquad Z(t)=\nu h(t)=H(\nu^{1/\alpha}t).
\tag{R2}
\]
Thus \(D_t^\alpha Z=\nu F(Z)\). For a stored physical-time field \(\bar G\), set \(\widehat Z=I_t^\alpha\bar G\). Its independent residual is
\[
r_t=\bar G-\nu F(\widehat Z),\qquad |r_t|/\nu\le\delta_F.
\tag{R3}
\]
Errors in \(Z\) and \(H\) use the same state scale; recovery of \(h\) requires division by \(\nu\). The curve parameter \(\lambda_\xi\) belongs to the forward variance curve, whereas \(\kappa=\lambda_R/\nu\) belongs to the linear Riccati term. They are defined separately.

The object class \(\mathcal X\) consists of equation parameters, a precisely specified approximate trajectory, and its time interval. Common admissibility requirements are \(AC[0,X]\), local Lipschitz continuity at positive times, zero initial value, and the classical Caputo residual. Define:

- **Real-valued condition \(A_{\mathrm{real}}\):** \(\rho u=0\); the trajectory is real-valued, \(\widehat H(0)=0\), and \(\widehat H\le0\), with an independent residual envelope. Real-order comparison applies to this class. Shape preservation at the central frequency supplies this condition directly.
- **Trajectory condition \(H_{\mathrm{diss}}\):** \(\widehat H\in AC[0,X]\), local Lipschitz continuity at positive times, and zero initial value; an independently certified constant \(\varepsilon_R\ge0\) satisfies \(\operatorname{Re}\widehat H\le\varepsilon_R\le2s_0\), and there is a continuous nonnegative envelope \(\eta\ge|D_x^\alpha\widehat H-F(\widehat H)|\). Set \(\sigma=s_0-\varepsilon_R/2\ge0\).
- **Intermediate property \(M_{\mathrm{diss}}\):** the complex error satisfies the positive-kernel comparison
  \[
  |H(x)-\widehat H(x)|\le\int_0^x k_\sigma(x-t)\eta(t)\,dt,
  \quad k_\sigma(t)=t^{\alpha-1}E_{\alpha,\alpha}(-\sigma t^\alpha)\ge0.
  \tag{R4}
  \]
- **State conclusion \(B_{\mathrm{state}}\):** when \(\eta\le\delta\), the computable error bound is
  \[
  |H-\widehat H|\le
  \begin{cases}
  \delta\{1-E_\alpha(-\sigma x^\alpha)\}/\sigma\le\delta/\sigma,&\sigma>0,\\
  \delta x^\alpha/\Gamma(1+\alpha),&\sigma=0.
  \end{cases}
  \tag{R5}
  \]

These conditions are verified from the known parameters, stored trajectory, and independent residual. The left-half-plane property of the exact solution is proved from the equation and is not supplied as numerical input.

### 4.2. The core argument: one-sided dissipativity in place of real ordering

#### 4.2.1. Half-plane preservation and regularity of the exact solution

Write \(H=X+iY\). Completing the square gives
\[
\operatorname{Re}F(H)
=-\tfrac18-\tfrac{1-\rho^2}{2}u^2
-\tfrac12(Y+\rho u)^2-s_0X+\tfrac12X^2.
\tag{R6}
\]
A local Volterra contraction provides a unique continuous solution. It is \(\alpha\)-Hölder on bounded time intervals. If \(q=F(H)\), then throughout a local existence interval,
\[
H'(x)=\frac{q(x)x^{\alpha-1}}{\Gamma(\alpha)}
+\frac{\alpha-1}{\Gamma(\alpha)}
\int_0^x(x-t)^{\alpha-2}[q(t)-q(x)]\,dt.
\tag{R7}
\]
Near \(t=x\), the integrable exponent is \(2\alpha-2>-1\), and the initial-time term is the integrable \(x^{\alpha-1}\). Hence \(H\in AC\) and it is locally Lipschitz at positive times.

For a trajectory \(v\) in the same regularity class, integration by parts yields
\[
D_x^\alpha v(x)=\frac1{\Gamma(1-\alpha)}
\left[\frac{v(x)-v(0)}{x^\alpha}
+\alpha\int_0^x\frac{v(x)-v(t)}{(x-t)^{1+\alpha}}\,dt\right].
\tag{R8}
\]
If the real part first reaches \(0<\varepsilon<1/2\), the historical maximum makes the left-hand side strictly positive, whereas (R6) is strictly negative there. Thus \(X\le0\). At a positive time with \(X=0\), the left-hand side of (R8) is nonnegative while (R6) remains strictly negative. Consequently, \(\operatorname{Re}H<0\).

Set \(\psi_\epsilon(z)=\sqrt{|z|^2+\epsilon^2}-\epsilon\), a smooth convex function on the two-dimensional real space. The historical tangent inequality gives
\[
D_x^\alpha\psi_\epsilon(z)
\le\frac{\operatorname{Re}(\bar z D_x^\alpha z)}{\sqrt{|z|^2+\epsilon^2}}.
\tag{R9}
\]
Together with
\[
\operatorname{Re}(\bar H F(H))=-bX-s_0|H|^2+\tfrac12X|H|^2
\]
and \(X\le0\), this yields \(D_x^\alpha\psi_\epsilon(H)+s_0\psi_\epsilon(H)\le b\). Scalar comparison followed by \(\epsilon\downarrow0\) gives
\[
|H(x)|\le
\begin{cases}
b\{1-E_\alpha(-s_0x^\alpha)\}/s_0,&s_0>0,\\
bx^\alpha/\Gamma(1+\alpha),&s_0=0.
\end{cases}
\tag{R10}
\]
The finite-time bound permits continuation, so the solution exists globally.

#### 4.2.2. \(H_{\mathrm{diss}}\Rightarrow M_{\mathrm{diss}}\)

**Core lemma.** For the exact solution of (R1) and a trajectory satisfying \(H_{\mathrm{diss}}\), (R4)–(R5) hold.

**Proof.** Set \(e=H-\widehat H\) and \(r=D_x^\alpha\widehat H-F(\widehat H)\). Factoring the difference of squares gives the exact identity
\[
D_x^\alpha e=\left(d+\frac{H+\widehat H}{2}\right)e-r.
\tag{R11}
\]
The half-plane property of the exact solution and the certified trajectory bound imply
\[
\operatorname{Re}\left(d+\frac{H+\widehat H}{2}\right)
\le-s_0+\varepsilon_R/2=-\sigma.
\tag{R12}
\]
Apply (R9) to \(e\). Since
\( |e|^2/\sqrt{|e|^2+\epsilon^2}\ge\psi_\epsilon(e)\), we obtain
\[
D_x^\alpha\psi_\epsilon(e)+\sigma\psi_\epsilon(e)\le |r|\le\eta,
\qquad \psi_\epsilon(e(0))=0.
\tag{R13}
\]
The scalar Caputo solution with the right-hand side is \(k_\sigma*\eta\). Its positivity follows from the negative historical-minimum principle in (R8): a nonnegative source and zero initial value give a nonnegative solution. Applying this principle to smooth, nonnegative sources of narrowing support gives positivity of the continuous positive-time kernel \(k_\sigma\ge0\). General continuous envelopes follow by uniform approximation. Comparison in (R13) and the limit \(\epsilon\downarrow0\) establish (R4). The kernel mass is
\[
\int_0^xk_\sigma(t)\,dt=
\begin{cases}
\{1-E_\alpha(-\sigma x^\alpha)\}/\sigma,&\sigma>0,\\
x^\alpha/\Gamma(1+\alpha),&\sigma=0,
\end{cases}
\]
which gives (R5). ∎

The key algebra in (R11)–(R12) is that the imaginary term \(i\rho u\) vanishes in the real part of the complex inner product, while the quadratic term is controlled by the real parts of the two trajectories. The stability constant depends on \(s_0\) and the allowed positive part of the reference trajectory, not directly on frequency. A conventional complex-modulus Lipschitz bound involves \(|d|\) and trajectory moduli. Verifying real parts instead keeps the residual bound usable at intermediate and high frequencies. We use Li–Liu's historical convexity tool; the model's algebraic dissipativity and its concrete certificates provide the application-specific content.

#### 4.2.3. Recovery of the real-valued case

If \(A_{\mathrm{real}}\) holds, taking \(\varepsilon_R=0\) gives \(H_{\mathrm{diss}}\) with \(\sigma=s_0\). Hence
\[
A_{\mathrm{real}}\Rightarrow H_{\mathrm{diss}}
\Rightarrow M_{\mathrm{diss}}\Rightarrow B_{\mathrm{state}}.
\tag{R14}
\]
For \(s_0>0\), this recovers the uniform error bound from real-valued dissipative comparison; for \(s_0=0\), it retains the finite-time branch. The endpoint \(\rho=0,\kappa=0\) included in T1 uses the latter branch, preserving the stated quantifiers without division by zero.

### 4.3. Independent structural conditions for the fixed third-order construction

#### 4.3.1. A sufficient criterion before division

Let \(M\) be the existing six-condition matching matrix, \(\Delta\) its unnormalized determinant, and \(N_1,N_2,N_3\) its three Cramer numerators. Before any division, define
\[
\mathcal Q(y)=\Delta+N_1y+N_2y^2+N_3y^3,
\]
\[
\mathcal P(y)=b_1\Delta y+(b_2\Delta+b_1N_1)y^2+g_0N_3y^3.
\tag{R15}
\]
Set
\[
\beta_j=\operatorname{Re}(N_j\bar\Delta),\qquad
\operatorname{Re}[\mathcal P(y)\overline{\mathcal Q(y)}]
=\sum_{n=1}^6\tau_ny^n.
\tag{R16}
\]
Define \(H_{\mathrm{str}}\) by \(\beta_j>0\), \(\tau_n\le0\), and \(\tau_1<0\). These quantities depend only on the matching inputs and unnormalized polynomials.

**Structural lemma.** Condition \(H_{\mathrm{str}}\) implies uniqueness of the matching solution, a nonvanishing normalized denominator for all positive times, and \(\operatorname{Re}\widehat H(y)<0\) for every \(y>0\).

**Proof.** First, \(\beta_1>0\) rules out \(\Delta=0\). Cramer's rule gives \(q_j=N_j/\Delta\) and
\[
\operatorname{Re}q_j=\beta_j/|\Delta|^2>0.
\]
Thus \(\operatorname{Re}Q(y)\ge1\) and consequently \(|Q(y)|\ge1\). By (R15), \(\mathcal P=\Delta P\) and \(\mathcal Q=\Delta Q\), so
\[
\operatorname{Re}\widehat H(y)
=\frac{\sum_{n=1}^6\tau_ny^n}{|\mathcal Q(y)|^2}<0\quad(y>0).
\tag{R17}
\]
This proves the claim. ∎

The two nonvanishing conditions play different roles: \(\Delta\ne0\) ensures existence and uniqueness of the six-condition coefficients, while \(Q(y)\ne0\) allows the resulting rational function to be evaluated along the time axis. The common sign certificate proves them in that order.

The full-frequency structural proof uses \(N_j=f^jF_j\) and \(f=1/\Gamma(1+\alpha)>0\). Accordingly, its quantity \(B_j=\operatorname{Re}(F_j\bar\Delta)\) differs from \(\beta_j\) only by the positive factor \(f^j\), and its \(D_n\) differs from \(\tau_n\) only by the positive factor \(f^n\). All strict sign margins in that proof therefore satisfy \(H_{\mathrm{str}}\) directly.

#### 4.3.2. The central result T1 implies the structural condition

The domain of T1 is \(u=0\), \(1/2<\alpha<1\), and \(0\le s_0\le1/2\). For the same six-condition construction, the determinant is real with \(\Delta\ne0\), and \(q_j>0\). Write
\[
A=\sqrt{s_0^2+1/4},\quad R=A-s_0>0,\quad
B=-b_1>0,\quad D=b_2\ge0.
\]
The large-time coefficients \(g_1,g_2\) are strictly positive, and matching gives
\[
Rq_1=B+g_1q_2+g_2q_3>B.
\]
Moreover, \(m=\Gamma(1+2\alpha)/\Gamma(1+\alpha)^2>1\) and
\[
DR/B^2=8s_0R/m<1,
\quad s_0R=\frac{s_0}{4(A+s_0)}<\frac18.
\]
Hence \(p_2=D-Bq_1<0\), while \(p_1=-B<0\) and \(p_3=-Rq_3<0\). Since \(q_0=1\), each nonzero coefficient of \(P\bar Q=PQ\) is a sum containing at least one product of a negative \(p_k\) and a positive \(q_j\). Thus \(\tau_n<0\) and \(\beta_j=\Delta^2q_j>0\). Therefore,
\[
A_{\mathrm{T1}}\Rightarrow H_{\mathrm{str}}
\Rightarrow \{\Delta\ne0,\ \operatorname{Re}Q\ge1,\ \operatorname{Re}\widehat H<0\}.
\tag{R18}
\]
The Bernstein lower bound \(Q(y)/(1+y)^3\ge901/11294304\) in T1 is a more specific quantitative central-frequency result. The common criterion recovers matching uniqueness, denominator nonvanishing, and the half-plane structure.

#### 4.3.3. A nonzero-frequency domain satisfies the same condition

The continuous domain
\[
\alpha\in[13/25,3/5],\qquad
\rho=-1489/2000,\quad\kappa=0,\quad u\in\mathbb R
\tag{R19}
\]
is compactified using \(\omega=\sqrt{u^2+1/4}\) and \(\eta=u/(1+u)\), mapping \(u\ge0\) to the closed interval \([0,1]\) while preserving
\[
\Delta=\omega^3\bar\Delta,\quad F_j=\omega^{3+j}\bar F_j,
\quad B_j=\omega^{6+j}\bar B_j,\quad D_n=\omega^{7+n}\bar D_n.
\]
The complete closed-rectangle certificate establishes \(\bar B_j>0\), \(\bar D_n<0\), and \(|\bar\Delta|>1/120\). Conjugate symmetry covers negative frequencies. Thus (R19) gives another explicit implication \(C_{\mathrm{str}}\Rightarrow H_{\mathrm{str}}\). The conclusions hold for all \(\nu>0\) and all positive physical times. This parameter domain and the central T1 domain are stated separately; both use the same unnormalized sign criterion.

### 4.4. Objects outside the real-valued class

**Example 1 (a nonreal frequency trajectory).** Take
\[
\alpha=11/20,\quad\rho=-1489/2000,\quad\kappa=0,\quad u=1.
\tag{R20}
\]
These parameters lie in (R19), so the existing third-order approximation satisfies \(H_{\mathrm{str}}\) at all times and \(\operatorname{Re}\widehat H<0\). On every finite interval \(X\), the rational trajectory belongs to the required regularity class. An independently computable residual envelope below verifies \(H_{\mathrm{diss}}\) in full. Write \(Y=X^\alpha\) and
\[
K_P(Y)=\sum_{j=1}^3|p_j|Y^j,\qquad
P'Q-PQ'=\sum_{j=0}^4a_jy^j,\qquad
K_D(Y)=\sum_{j=0}^4|a_j|Y^j,
\]
where
\[
(a_0,a_1,a_2,a_3,a_4)=
(p_1,2p_2,p_2q_1-p_1q_2+3p_3,
2(p_3q_1-p_1q_3),p_3q_2-p_2q_3).
\]
The bound \(|Q|\ge1\) gives \(|\widehat H|\le K_P(Y)\) and
\(|\widehat H'(x)|\le\alpha K_D(Y)x^{\alpha-1}\). The Caputo definition and a Beta integral then yield
\[
|D_x^\alpha\widehat H(x)|\le\Gamma(1+\alpha)K_D(Y).
\]
An exact constant envelope is therefore
\[
\delta_\star(X)=\Gamma(1+\alpha)K_D(Y)+b+|d|K_P(Y)
+\tfrac12K_P(Y)^2.
\tag{R20a}
\]
It is computed directly from the existing six-condition coefficients and uses neither the unknown exact solution nor a floating-point trajectory. At \(X=1\), we have \(Y=1\), \(b=5/8\), and \(|d|=1489\sqrt5/4000\). This provides an admissible envelope throughout the example's time interval. The pricing computation uses a tighter independently evaluated residual certificate. Here \(s_0=1489/4000>0\), and the stability constant is \(4000/1489\).

The nonreal nature of the object can also be established analytically. Locally, \(H=I^\alpha F(H)\) first gives \(H=O(x^\alpha)\). Successive substitution yields
\[
H(x)=-\frac{b}{\Gamma(1+\alpha)}x^\alpha
-\frac{bd}{\Gamma(1+2\alpha)}x^{2\alpha}
+O(x^{3\alpha}).
\tag{R21}
\]
The remainder estimate follows from \(I^\alpha x^{m\alpha}=\Gamma(1+m\alpha)x^{(m+1)\alpha}/\Gamma(1+(m+1)\alpha)\) and requires no assumption of global convergence of the time series. Hence
\[
\operatorname{Im}H(x)=-\frac{b\rho u}{\Gamma(1+2\alpha)}x^{2\alpha}
+O(x^{3\alpha})>0
\]
for sufficiently small positive \(x\). The same third-order approximation matches the first three small-time coefficients and therefore has the same nonzero leading imaginary term. This example satisfies the complex-valued condition but not the real-valued condition. Its strictly nonreal trajectory demonstrates the extension in scope.

**Example 2 (recovery of the real-valued case on the full frequency axis).** When \(\rho=\kappa=0\), the equation is real-valued at every frequency. Set
\[
c=\sqrt{8b}=2\sqrt{u^2+1/4},\quad
\tau=c^{1/\alpha}x,\quad H(x)=cH_0(\tau).
\]
Substitution in (R1) gives exactly
\[
D_\tau^\alpha H_0=-1/8+H_0^2/2.
\tag{R22}
\]
This is the central equation of T1 with \(s_0=0\). The small-time data scale as \(b_n(u)=c^{n+1}b_n(0)\), and the large-time data as \(g_k(u)=c^{1-k}g_k(0)\). Uniqueness of the matching system then implies
\[
\widehat H_u(y)=c\widehat H_0(cy),\qquad q_j(u)=c^jq_j(0).
\tag{R23}
\]
The exact variable transformation transfers the real-denominator and shape properties of T1 to this real-valued class over the full frequency axis. The error uses the \(\sigma=0\) branch of (R5). This example recovers the earlier real-valued case within the common framework, whereas (R20) supplies a complex object outside real-order methods. The transformation itself is an application of the earlier result.

### 4.5. From state certificates to prices and finite selection

#### 4.5.1. Positive-kernel propagation

In the fixed forward variance model with \(\kappa=0\), assume \(\xi\in AC[0,T]\), \(\xi(0)>0\), and \(\xi'\ge0\). Define
\[
q_\alpha(t)=\frac{\xi(0)t^{-\alpha}}{\Gamma(1-\alpha)}
+I^{1-\alpha}\xi'(t)\ge0.
\tag{R24}
\]
For an absolutely continuous trajectory with zero initial value, absolutely justified Fubini interchange and integration by parts give the exact identity for the derivative-based exponent,
\[
L_T-\bar L_T=\frac1\nu\int_0^Tq_\alpha(T-t)
[Z(t)-\widehat Z(t)]\,dt.
\tag{R25}
\]
A sufficient bound for the Fubini interchange is
\((\sup\xi)T^{1-\alpha}\|v'\|_1/\Gamma(2-\alpha)<\infty\). The boundary terms vanish because \(v(0)=0\) and \((I^{1-\alpha}\xi)(0)=0\). If \(|Z-\widehat Z|\le E(t)\), then
\[
|L_T-\bar L_T|\le\eta_T
=\frac1\nu\int_0^Tq_\alpha(T-t)E(t)\,dt.
\tag{R26}
\]
This uses the state error directly, without another large Lipschitz factor from the Riccati field. For \(\widehat Z=I^\alpha\bar G\), the quantity \(\bar L_T=\nu^{-1}\int\xi\bar G\) already uses the derivative-based definition. An exponent defined instead by \(\int\xi F(\widehat Z)\) is converted using \(\nu^{-1}\int\xi r_t\); each definition retains its associated error terms.

The exact transform satisfies \(|e^{L_T}|\le1\), so
\[
|e^{L_T}-e^{\bar L_T}|
\le\min\{1,e^{\operatorname{Re}\bar L_T}\}(e^{\eta_T}-1).
\tag{R27}
\]
This establishes the implication \(M_{\mathrm{diss}}\Rightarrow B_{\mathrm{exponent}}\).

#### 4.5.2. Complete pricing conditions

The complete pricing object consists of a finite set of frequency nodes, the probability model's analytic strip and infinite tail, phase factors, and arithmetic enclosures. Verify \(H_{\mathrm{diss}}\) at every node, then use (R27) to obtain transform error \(\epsilon_n\). Set \(m=K/F\) and \(k=\log m\). The finite Lewis trapezoidal price sum is
\[
\widehat c_N=1-\frac{h\sqrt m}{\pi}
\left[2\operatorname{Re}\widehat\phi_0+
\sum_{n=1}^N\frac{\operatorname{Re}(e^{-inhk}\widehat\phi_n)}{(nh)^2+1/4}\right].
\tag{R28}
\]
The model price satisfies
\[
|c-\widehat c_N|\le\epsilon_{\mathrm{grid}}+\epsilon_{\mathrm{tail}}
+\frac{h\sqrt m}{\pi}\left[2\epsilon_0+
\sum_{n=1}^N\frac{\epsilon_n}{(nh)^2+1/4}\right]
+\epsilon_{\mathrm{arithmetic}}.
\tag{R29}
\]
At \(u=0\), the coefficient \(2\) is the product of the trapezoidal half-weight and the reciprocal denominator \(1/4\). The analytic strip bounds the discretization error between nodes, so the continuous-time certificates at the stored nodes can be combined into an error bound for the complete pricing integral. Denote the combined conditions by \(H_{\mathrm{price}}\): the trajectory certificates at every used node, the exact-model strip and tail bounds, and the arithmetic assumptions all hold. The central-frequency condition \(A_{\mathrm{real}}\) enters the state argument; the complete price enters through \(H_{\mathrm{price}}\).

#### 4.5.3. Finite candidate selection

For a candidate set \(\Theta=\{\alpha_1,\ldots,\alpha_J\}\) and \(n\) quotes, define
\[
J_j=\frac1{2n}\sum_{i=1}^n(C_{ij}-M_i)^2.
\]
If \(C_{ij}\in[p^-_{ij},p^+_{ij}]\) and \(M_i\in[m_i^-,m_i^+]\), set \(r^-_{ij}=p^-_{ij}-m_i^+\) and \(r^+_{ij}=p^+_{ij}-m_i^-\). The lower bound for each squared term is zero if the interval contains zero, and otherwise the smaller squared endpoint. Its upper bound is the larger squared endpoint. Summing gives \(J_j\in[L_j,U_j]\). If
\[
g=\min_{j\ne j_*}L_j-U_{j_*}>0,
\tag{R30}
\]
then \(j_*\) is the unique exact optimum in the finite set. If another objective differs uniformly by at most \(\delta_J\) and the selected point is \(\varepsilon_{\mathrm{alg}}\)-optimal for that objective, then
\[
J(\widehat\alpha)-\min_\Theta J\le2\delta_J+\varepsilon_{\mathrm{alg}}.
\tag{R31}
\]
Thus \(g>2\delta_J+\varepsilon_{\mathrm{alg}}\) preserves the same finite candidate. The proof applies the objective perturbation bound once at the selected point and once at the exact optimum. The conclusion uses a strict objective gap and requires no curvature condition.

Under the specified six-month forward variance curve, the three candidates \(\alpha=0.52,0.60,0.90\) correspond to \(H=0.02,0.10,0.40\). Certified model-objective intervals are

| \(\alpha\) | Model-objective interval (decimal endpoints rounded outward) |
|---:|---:|
| 0.52 | \([6.8962\times10^{-9},1.833669\times10^{-7}]\) |
| 0.60 | \([4.535720\times10^{-7},6.021720\times10^{-7}]\) |
| 0.90 | \([8.2343900\times10^{-6},8.3484458\times10^{-6}]\) |

The exact strict gap satisfies \(g>2.70205\times10^{-7}\). The actual fixed third-order numerical procedure and the model objective both select \(\alpha=0.52\). The selection of \(H=0.02\) is therefore stable under the computational errors included in this setting. Quote-band tests separately provide rowwise compatibility decisions for each candidate. Ranking stability and quote compatibility are independently certified outputs.

### 4.6. Connecting structural conditions and error propagation

The results correspond to the following sufficient conditions and conclusions:
\[
\begin{aligned}
A_{\mathrm{T1}}&\Rightarrow H_{\mathrm{str}}
\xRightarrow{\text{raw Cramer sign conditions}}M_{\mathrm{str}}
\Rightarrow B_{\mathrm{structure}},\\
C_{\mathrm{str}}&\Rightarrow H_{\mathrm{str}},\\
A_{\mathrm{real}}&\Rightarrow H_{\mathrm{diss}}
\xRightarrow{\text{history convexity and model dissipativity}}M_{\mathrm{diss}}
\Rightarrow B_{\mathrm{state/exponent}},\\
C_{\mathrm{complex}}&\Rightarrow H_{\mathrm{diss}},\\
H_{\mathrm{price}}&\Rightarrow B_{\mathrm{price}}
\xRightarrow{\text{finite-candidate objective gap}}B_{\mathrm{selection}}.
\end{aligned}
\tag{R32}
\]
Property \(M_{\mathrm{str}}\) consists of matching uniqueness and coefficient half-plane constraints; \(B_{\mathrm{structure}}\) consists of pole-freeness and trajectory half-plane preservation at all positive times. Condition \(C_{\mathrm{complex}}\) may be supplied by a full-frequency structural certificate and an independent residual, or by a stored reference field with full-time half-plane and residual certificates. Example (R20) lies strictly outside the real-valued class. These structural conditions are sufficient and can be verified from the unnormalized coefficients or stored trajectory.

Equation (R32) separates the independent conditions required at each stage. Matching-coefficient signs determine the rational trajectory's structure; trajectory real parts determine the dissipativity rate; the positive kernel propagates independent residuals to prices; and the objective gap between price intervals determines stability of finite candidate selection. Every step retains the original model and consistent pricing inputs.

## 5. From Error Inclusions to Financial Decisions

The following propositions are direct consequences of support functions, expansion of a squared objective, and the triangle inequality. They connect the two model analyses to financial validation. Their role is to propagate the effective error sets constructed for the models.

### 5.1. Valid portfolio-price intervals

Let \(p\in\mathbb R^n\) be the model price vector and \(\widehat p\) a deterministic numerical output. Suppose it has independently been proved that
\[
e=p-\widehat p\in E,
\]
where \(E\) is nonempty and compact, with support function \(h_E(w)=\max_{e\in E}w\cdot e\). For a fixed position vector \(w\in\mathbb R^n\),
\[
w\cdot p\in[\,w\cdot\widehat p-h_E(-w),\ w\cdot\widehat p+h_E(w)\,].
\tag{D.1}
\]
**Proof.** The minimum is \(\min_{e\in E}w\cdot e=-h_E(-w)\) and the maximum is \(h_E(w)\); add these to the numerical center. If \(E=-E\), the half-width is \(h_E(w)\). A coordinate box \(E=\prod_i[-\varepsilon_i,\varepsilon_i]\) gives \(\sum_i|w_i|\varepsilon_i\). If \(E\) is the classical Heston shared-state set, its support function uses the common probability witness. The strict gap relative to its smallest coordinate box is determined by complete-row maximization and the phase conditions. ∎

For normalized prices \(c_i=C_i/(D_iF_i)\), a cash portfolio uses \(w_i=a_iD_iF_i\). The factors \(D_i,F_i\) must be defined inputs of the normalization. This linear conversion neither changes the model nor produces a return forecast.

### 5.2. Preservation of finite candidate selection

For candidates \(j=1,\ldots,N_{\rm cand}\), the exact objective is
\[
J_j=\frac1{2n}\|p_j-m\|_2^2.
\]
Here \(m\) is the fixed quote target. Let \(\widehat p_j\) and \(r_j=\widehat p_j-m\) be deterministic numerical quantities, with certified inclusion \(p_j-\widehat p_j\in E_j\). Write
\[
\widehat J_j=\frac1{2n}\|r_j\|_2^2,
\qquad R_j^2=\max_{e\in E_j}\|e\|_2^2.
\]
Then
\[
L_j=\max\{0,\widehat J_j-h_{E_j}(-r_j)/n\}
\ \le J_j\le\ 
U_j=\widehat J_j+h_{E_j}(r_j)/n+R_j^2/(2n).
\tag{D.2}
\]
**Proof.** The exact expansion is
\[
J_j=\widehat J_j+\frac{r_j\cdot e_j}{n}+\frac{\|e_j\|_2^2}{2n}.
\]
The linear perturbation belongs to \([-h_{E_j}(-r_j),h_{E_j}(r_j)]\), the squared term belongs to \([0,R_j^2]\), and \(J_j\ge0\). This proves (D.2). ∎

If a candidate \(j_*\) satisfies
\[
g=\min_{j\ne j_*}(L_j-U_{j_*})>0,
\tag{D.3}
\]
then \(j_*\) is the unique optimum of the model objective in the finite set. If another objective satisfies \(\max_j|\widetilde J_j-J_j|\le\delta_J\) and an algorithm returns an \(\varepsilon_{\rm alg}\)-optimal candidate, then
\[
2\delta_J+\varepsilon_{\rm alg}<g
\tag{D.4}
\]
ensures that the algorithm still selects \(j_*\). Indeed, every competitor satisfies \(\widetilde J_j-\widetilde J_{j_*}\ge g-2\delta_J>\varepsilon_{\rm alg}\) and therefore cannot satisfy the algorithm's optimality condition.

If the quote target is itself represented by a rigorous interval, first fix a deterministic center \(\widehat m\), define \(r_j=\widehat p_j-\widehat m\) and \(\widehat J_j=\|r_j\|_2^2/(2n)\), and define the combined error as \(e_j=(p_j-\widehat p_j)-(m-\widehat m)\). Construct \(E_j\) as the Minkowski difference of the price- and quote-error sets. The proof is unchanged. For the present sample, exact interval aggregation of squared terms is more direct than (D.2); we retain the certified objective endpoints instead of replacing them by a coarser estimate.

### 5.3. Rowwise quote-band tests

If the exact price in row \(i\) belongs to \([l_i,u_i]\) and the allowable quote interval is \([b_i,a_i]\), then
\[
l_i>a_i\quad\text{or}\quad u_i<b_i
\tag{D.5}
\]
is sufficient to exclude compatibility strictly. The positive separation is at least \(l_i-a_i\) or \(b_i-u_i\). When quote endpoints also have outer enclosures, use \(a_i^{\rm upper}\) and \(b_i^{\rm lower}\), respectively, so the conclusion holds for the exact endpoints.

**Proof.** The two closed intervals are strictly disjoint. Finite ranking and quote compatibility answer different questions: ranking compares objective values, while compatibility compares prices with quote bands. The present computation certifies both. A model-validation practitioner can retain the stable candidate ranking and identify precisely the strikes at which model inputs and other free parameters should be reexamined. ∎

## 6. Conditions of Applicability and Financial Interpretation

### Objects and parameter domains of the theorems

The joint-error theorem for the classical Heston model concerns the positive-part variance Euler scheme and the stock update using the current variance specified in the main text. Within the stated parameter domain, the mode loadings satisfy the prescribed nonpositive-real-part and total-loading conditions; the state partition includes both the atom at zero and the unbounded tail. The common probability constraints hold for the original discrete chain, and the price map includes all payoff terms. Together, these conditions ensure that the joint error set contains the model price bias.

The bias identity for trial functions assumes explicit growth, trace, local regularity, and residual-integrability conditions. Whenever these conditions hold, the same identity applies both to the exact continuous pricing function and to the nonexact trial function constructed here. Every integral and interface term in the error estimate has a specified mathematical meaning.

The center-frequency structural results for rough Heston cover \(\alpha\in(1/2,1)\), \(s\in[0,1/2]\). The all-frequency structural results cover \(\alpha\in[.52,.60]\), \(\rho=-.7445\), \(\kappa=0\), and hold for every real \(u\) and every positive time. The complex residual theorem assumes regularity of the reference trajectory, a one-sided bound on its real part, and an independent residual envelope. A strictly positive dissipation rate gives a bound uniform in time; at zero dissipation, the estimate retains an explicit time-growth term.

### Prices, units, and the candidate set

The financial example uses normalized European option prices defined by publicly available SPX implied volatilities, with a maturity of six months and twelve strikes. The forward variance curve, \(\rho\), \(\nu\), and the Riccati mean-reversion parameter are held fixed, and the candidate orders are \(\alpha=.52,.60,.90\). Each candidate uses the same price units and objective function.

Under this specification, the model objective intervals establish \(\alpha=.52\) as the unique optimal candidate; the specified third-order procedure makes the same selection. The model objective gap exceeds \(2.70205218\times10^{-7}\), yielding a computable tolerance for objective perturbations. This conclusion applies to the stated finite candidate comparison, with the selected \(\alpha\) corresponding to roughness \(H=.02\).

Quote consistency is assessed by a closed-interval test at each strike. The model price intervals at strikes 4400 and 4500 lie strictly above the respective upper quote endpoints, identifying specific entries for review. The call-spread application uses the same model, maturity, and two strikes. Its output error is less than \(.000634774793739\), and therefore satisfies the illustrative normalized price tolerance of \(.0007\). Prices and errors throughout this comparison use the normalized units defined in the main text.

### Use of the theory

An application first specifies the model, curve, contracts, parameter set, and price units, and then computes the corresponding error set or price intervals. Portfolio valuation uses support functions or interval endpoints; candidate comparison uses the objective gap; quote consistency uses the intersection between model price intervals and quote bands.

This approach connects numerical verification to its intended use. For candidate selection, the required accuracy is determined by the separation between competitors. For spread valuation, the error direction is determined by the position weights. For quote assessment, the decisive information is the strict relation between the model price interval and the quote band. Each application rests on specified inputs, an error inclusion, and a decision criterion.

## 7. Financial Applications: Roughness Candidates, Quote Tests, and Spread Valuation

SPX options are European-style and cash-settled, consistent with the European Fourier pricing framework used here. [Cboe, 2022](https://ir.cboe.com/news/news-details/2022/Cboe-to-Further-Expand-SP-500-Index-Options-Suite-with-New-and-Additional-Daily-Expirations-09-19-2022/default.aspx)

The speed of rational approximation is useful for repeated pricing and parameter searches. The error estimates developed here address three questions relevant to these uses: whether numerical approximation preserves the optimal roughness candidate; whether the difference between model prices and bid–ask quotes retains a definite sign after pricing error is included; and how individual option error bounds translate into a valuation tolerance for an option portfolio. This section answers these questions for a publicly available SPX implied-volatility sample.

Jeng–Kiliçman used third- and fourth-order Padé approximations for SPX calibration and published the associated data and code. [Jeng–Kiliçman, 2021, §4, Table 1](https://www.mdpi.com/2227-7390/9/21/2675) This section uses those public data, holds the remaining model inputs fixed, and applies the price error estimates to finite-candidate calibration and portfolio valuation. All numerical conclusions are based on price intervals for the corresponding model equations.

### 7.1. Data and pricing specification

We select the twelve quote rows with maturity $T=1/2$ from the sample dated June 18, 2021, with strikes $3700,3800,\ldots,4800$. The inputs are the publicly reported bid and ask implied volatilities, denoted by $\sigma_i^{\rm bid}$ and $\sigma_i^{\rm ask}$. Each input is interpreted as its original decimal value. Market quote columns and model-output columns are distinguished according to the authors' documentation. [Data documentation](https://github.com/WoonJeng/Dataset-for-SPX-Calibration-of-Option-Approximations-under-Rough-Heston-model/blob/860049da2b7486fe8aa509061eff23cc28c2ef89/README.md), [Original twelve-row data](https://github.com/WoonJeng/Dataset-for-SPX-Calibration-of-Option-Approximations-under-Rough-Heston-model/blob/860049da2b7486fe8aa509061eff23cc28c2ef89/spx_decomp.csv)

Set the discount factor to $D=1$ and the forward price to $F=4221.86$. For a European call under zero carrying costs, define the normalized price

\[
c=\frac{C}{DF}.
\tag{U1}
\]

Substituting these implied volatilities into the Black–Scholes formula defines the normalized bid and ask quotes
$B_i=\operatorname{BS}(\sigma_i^{\rm bid})/(DF)$, $A_i=\operatorname{BS}(\sigma_i^{\rm ask})/(DF)$, and the price midpoint $M_i=(B_i+A_i)/2$. The public implied-volatility sample therefore determines the quote intervals $[B_i,A_i]$ and the calibration objective used in this section. Price units, the discount factor, and the forward price are part of the pricing specification of this example.

Fix the correlation, volatility coefficient, and Riccati mean-reversion parameter at

\[
\rho=-.7445,\qquad \nu=.2897,\qquad \lambda_R=0,
\]

and fix the forward variance curve as

\[
\xi_*(t)=.0721+(.0262-.0721)
E_{.5286}(-.5037t^{.5286}).
\tag{U2}
\]

Here $E_\beta$ is the Mittag–Leffler function. The exponent $.5286$ and coefficient $.5037$ in the curve are kept the same for all roughness candidates; the mean-reversion parameter in the equation is $\lambda_R=0$. These values are taken from Table 1 of Jeng–Kiliçman and define a conditional calibration problem in which the other inputs remain fixed.

Take the candidate set

\[
\alpha\in\{.52,.60,.90\},\qquad
H=\alpha-\tfrac12\in\{.02,.10,.40\},
\tag{U3}
\]

where $H$ is the roughness parameter. Denote the model prices by $c_i(\alpha)$ and use the squared loss

\[
J(\alpha)=\frac1{24}\sum_{i=1}^{12}[c_i(\alpha)-M_i]^2.
\tag{U4}
\]

The optimality statements below concern the three candidates in (U3), conditional on (U2) and the remaining fixed parameters. The two price calculations being compared are the prices defined by the model equations and the outputs of the selected third-order Padé procedure.

### 7.2. Stability of roughness-candidate selection

For each candidate, verified inclusion intervals are available for all twelve model prices. The reference computation includes the continuous-time residual, characteristic-exponent error, Fourier quadrature error, and integration tails in the price bounds. Substituting these intervals into (U4), then squaring and summing, gives inclusion intervals $[L_j,U_j]$ for the model objective. The third-order Padé outputs are interpreted as the stored binary rational numbers; the rounding intervals from quote conversion are also included in their objective values.

| $\alpha$ | $H$ | Outward interval for the model objective $J$ | Outward interval for the third-order Padé objective |
|---|---|---|---|
| .52 | .02 | $[6.896298\times10^{-9},1.83366853\times10^{-7}]$ | $[7.0860205\times10^{-8},7.0860206\times10^{-8}]$ |
| .60 | .10 | $[4.53572071\times10^{-7},6.02171939\times10^{-7}]$ | $[6.12736652\times10^{-7},6.12736653\times10^{-7}]$ |
| .90 | .40 | $[8.234390086\times10^{-6},8.348445795\times10^{-6}]$ | $[8.139360397\times10^{-6},8.139360398\times10^{-6}]$ |

The exact interval endpoints give the strict objective gap

\[
g:=\min_{j:\alpha_j\ne.52}L_j-U_{.52}
>2.70205218\times10^{-7}.
\tag{U5}
\]

Thus $\alpha=.52$, $H=.02$ is the unique optimal candidate for the model prices on (U3). The third-order Padé objective also has its unique minimum at $.52$, with a strict objective gap exceeding $5.41876447\times10^{-7}$. The approximation procedure therefore preserves the roughness selection on the candidate set considered in this example.

This gap also provides an error tolerance for other numerical implementations. Suppose an implementation returns an objective $\widetilde J$ satisfying

\[
\sup_{\alpha\in\{.52,.60,.90\}}
|\widetilde J(\alpha)-J(\alpha)|\le\delta_J,
\qquad
\widetilde J(\widehat\alpha)\le\min\widetilde J+\varepsilon_{\rm alg},
\]

where $\varepsilon_{\rm alg}\ge0$ is the objective tolerance of the optimization procedure. Then

\[
J(\widehat\alpha)-\min J
\le2\delta_J+\varepsilon_{\rm alg}.
\tag{U6}
\]

**Proof.** The objective error bound and approximate optimality condition give, successively,

\[
J(\widehat\alpha)
\le\widetilde J(\widehat\alpha)+\delta_J
\le\min\widetilde J+\varepsilon_{\rm alg}+\delta_J
\le\min J+2\delta_J+\varepsilon_{\rm alg}.
\]

If $2\delta_J+\varepsilon_{\rm alg}<g$, selection of any other candidate would contradict (U5), so $\widehat\alpha=.52$. In particular, when the implementation minimizes $\widetilde J$ exactly, the following uniform objective error bound is sufficient to preserve that selection:

\[
\delta_J<1.35102609\times10^{-7}.
\tag{U7}
\]

Equation (U6) is a standard objective-perturbation estimate. The calculation specific to this example propagates model price errors into the same quote-based objective and establishes a strictly positive objective gap. The table directly proves that the selected Padé procedure preserves candidate selection, while (U7) provides a sufficient accuracy requirement for other implementations.

In a pricing and calibration workflow, a fast approximation can first evaluate candidate objectives, followed by reference price intervals for the relevant candidates. Strictly separated objective intervals then verify their finite-candidate ranking. Numerical accuracy is thereby determined by the identifiable separation between candidates.

### 7.3. Separation of model prices from quote intervals

Optimality of the selected candidate and its agreement with each quote row are separately testable quantities. Set $\alpha=.52$ and examine strikes $4400$ and $4500$ individually. The results below use the normalized units of (U1).

| Strike | Outward enclosure of the quote interval | Model price interval | Third-order Padé output | Strict lower bound on the model price above the ask |
|---|---|---|---|---|
| 4400 | $[.021578146466486,.021885184947781]$ | $[.022001379841730,.022593310552455]$ | .022444989699935… | $>.000116194893950$ |
| 4500 | $[.013026560676140,.013312188046179]$ | $[.013328234352325,.013926853822165]$ | .013735688886630… | $>.000016046306147$ |

The final column is computed from the original exact interval endpoints and then rounded outward. It gives a strict price difference that remains valid after pricing error is included.

For $K=4400$, denote the third-order Padé output by $c^P_{4400}$. The corresponding model price satisfies

\[
|c^P_{4400}-c_{4400}|
<.000443609858205.
\tag{U8}
\]

The numerical output exceeds the ask by more than $.000559804752154$. After the full pricing error in (U8) is deducted, the price difference remains positive. Direct comparison of the lower model price endpoint with the upper ask endpoint gives the strict lower bound in the table. The comparison at $K=4500$ likewise retains a strictly positive sign.

This example therefore yields two definite conclusions: $H=.02$ has the smallest objective among the three candidates considered, and its model prices at $K=4400,4500$ exceed the ask quotes. The first conclusion concerns candidate selection; the second identifies entries for further examination of the parameter configuration and forward variance curve. Both use the same price error bounds, price units, and model inputs.

This row-by-row test can form part of a pricing-model validation record. The record specifies the data version, price units, model parameters, variance curve, numerical procedure, and model price intervals. Strict separation between a model price interval and its quote interval provides a quantitative basis for reviewing the inputs and parameter configuration.

The model-validation framework described in SR 11-7 (2011, §V) included conceptual soundness, ongoing monitoring, and outcomes analysis. The price intervals here provide a mathematical basis for pricing calculations and quote comparisons. [Historical guidance](https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf)

### 7.4. Valuation error for a call spread

Consider buying a call with strike $4400$ and selling a call with strike $4500$, with the same maturity. Its normalized model value is

\[
v=c_{4400}-c_{4500}.
\tag{U9}
\]

The individual price intervals in the preceding section give

\[
v\in
[.008074526019566,.009265076200129].
\tag{U10}
\]

The corresponding third-order Padé output is

\[
v^P=.008709300813304\ldots,
\qquad
|v^P-v|<.000634774793739.
\tag{U11}
\]

**Proof.** For $c_1\in[\ell_1,r_1]$, $c_2\in[\ell_2,r_2]$, we have

\[
c_1-c_2\in[\ell_1-r_2,r_1-\ell_2].
\]

Substitution of the two model price intervals gives (U10). Computing the distances from $v^P$ to the two exact endpoints, taking their maximum, and rounding outward gives (U11). If the individual price errors are first converted into symmetric intervals and the triangle inequality is then applied, the resulting upper bound is $.000851064392510$. Retaining the signed endpoints of the individual intervals gives the tighter portfolio error bound in (U11). This calculation uses linear operations on marginal price intervals; its accuracy gain comes from the asymmetric endpoint information in the individual price errors.

If the normalized valuation tolerance for this portfolio is $\varepsilon_v=.0007$, then (U11) proves that the selected numerical procedure meets that tolerance. The required valuation accuracy thus has a verifiable decision criterion.

For a finite portfolio of options with the same maturity, let the position quantities be $n_i$, suppose the discounted-forward product $DF$ is known, and assume $|c_i^P-c_i|\le\varepsilon_i$. Then

\[
\left|\sum_i n_i C_i^P-\sum_i n_i C_i\right|
\le DF\sum_i|n_i|\varepsilon_i,
\tag{U12}
\]

If full individual price intervals are available, their endpoints can instead be aggregated according to the signs of the positions: positive positions preserve endpoint order, while negative positions reverse it. This retains more information than summing symmetric error bounds. Given a portfolio tolerance, the resulting calculation identifies which individual price intervals require refinement and allocates pricing accuracy to the corresponding contracts.

### 7.5. Application results and implementation conditions

| Application | Mathematical operation | Result in this example | Use |
|---|---|---|---|
| Roughness-candidate selection | Compare objective intervals for three candidates with the other parameters and variance curve fixed | Model prices and the selected Padé procedure both select $H=.02$; model objective gap $>2.70205218\times10^{-7}$ | Gives a strict criterion and numerical accuracy requirement for finite-candidate ranking |
| Row-by-row quote test | Compare model price inclusion intervals with bid–ask intervals | Model prices at $K=4400,4500$ exceed the respective asks by $>.000116194893950$, $>.000016046306147$ | Identifies quote rows and parameter configurations for further examination |
| Spread valuation | Aggregate price endpoints according to position signs and compare with the numerical output | 4400–4500 call-spread error $<.000634774793739$ | Determines whether the selected procedure meets the valuation tolerance for the specified portfolio |

These conclusions share the following specification: zero-carry normalized prices defined by public implied volatilities, the fixed variance curve (U2), twelve sample rows with maturity $T=1/2$, the candidate set (U3), and the selected six-condition third-order Padé procedure. The proofs underlying the price intervals cover the model state, characteristic exponent, Fourier quadrature, and integration tails. Under this specification, the error estimates give definite results for parameter selection, quote differences, and portfolio valuation.

This section uses standard interval arithmetic, objective-perturbation estimates, and linear portfolio relations to turn the structural properties and price error bounds into financial criteria. These criteria connect the accuracy of a fast approximation to the decision being made: the objective gap controls candidate selection, interval separation controls quote assessment, and position weights together with price errors control portfolio valuation.

## 8. Conclusion

This paper develops two structural approaches to Heston pricing error. For classical Heston, the common state distribution of the original discrete chain constrains multiple residuals, yielding a joint price error set and directional estimates. Independently verifiable growth, trace, and integrability conditions give a bias identity that applies to both exact and nonexact trial functions. For rough Heston, the raw matching algebra establishes structural properties of the existing third-order approximation, while complex one-sided dissipation and an independent fractional residual control the error relative to the true solution.

The characteristic exponent, Fourier pricing, and finite objective gaps then turn these estimates into rigorous price and candidate-selection decisions. The example defined by public SPX data proves preservation of selection on the specified finite candidate set and gives computable error results for quote tests and a call spread. The contribution consists of these particular structures, parameter domains, and financial conclusions, each established under the conditions stated in the main text.

## References

1. **GR2019.** Gatheral, Jim and Radoičić, Radoš. *Rational Approximation of the Rough Heston Solution*. International Journal of Theoretical and Applied Finance 22(3), 1950010, 2019. DOI [10.1142/S0219024919500109](https://doi.org/10.1142/S0219024919500109). The SSRN manuscript dated January 29, 2019 is used.

2. **GR2023v1.** Gatheral, Jim and Radoičić, Radoš. *A Generalization of the Rational Rough Heston Approximation*. 2023. [Source](https://arxiv.org/abs/2310.09181v1). Version used: arXiv:2310.09181v1.

3. **JK2020.** Siow Woon Jeng and Adem Kiliçman. *Series Expansion and Fourth-Order Global Padé Approximation for a Rough Heston Solution*. Mathematics 8(11), 1968, 2020. DOI [10.3390/math8111968](https://doi.org/10.3390/math8111968).

4. **JK2021.** Siow Woon Jeng and Adem Kiliçman. *SPX Calibration of Option Approximations under Rough Heston Model*. Mathematics 9(21), 2675, 2021. DOI [10.3390/math9212675](https://doi.org/10.3390/math9212675).

5. **AbiJaberElEuch2018v1.** Abi Jaber, Eduardo and El Euch, Omar. *Markovian structure of the Volterra Heston model*. Statistics & Probability Letters 149, 63–72, 2019. DOI [10.1016/j.spl.2019.01.024](https://doi.org/10.1016/j.spl.2019.01.024). Version used: arXiv:1803.00477v1.

6. **LiLiu2018.** Li, Lei and Liu, Jian-Guo. *A Generalized Definition of Caputo Derivatives and Its Application to Fractional ODEs*. SIAM Journal on Mathematical Analysis 50(3), 2867–2900, 2018. DOI [10.1137/17M1160318](https://doi.org/10.1137/17M1160318). The convexity result is Proposition 3.11.

7. **Simon2014.** Simon, Thomas. *Comparing Fréchet and positive stable laws*. 2014. [Source](https://arxiv.org/abs/1310.1888v2). Version used: arXiv:1310.1888v2.

8. **TrefethenWeideman2014.** Trefethen, Lloyd N. and Weideman, J. A. C. *The Exponentially Convergent Trapezoidal Rule*. SIAM Review 56(3), 385–458, 2014. DOI [10.1137/130932132](https://doi.org/10.1137/130932132). Strip quadrature is covered by Theorem 5.1.

9. **NIST2010.** Olver, Frank W. J. and Lozier, Daniel W. and Boisvert, Ronald F. and Clark, Charles W. *NIST Handbook of Mathematical Functions*. Cambridge University Press, 2010. [Source](https://dlmf.nist.gov/).

10. **GatheralCode2023.** Gatheral, Jim. *RationalRoughHeston: roughHestonPadeLambda.R*. 2023. [Source](https://github.com/jgatheral/RationalRoughHeston/blob/d65ea96e4c113fbb330074dfaea3e7715d650bbd/roughHestonPadeLambda.R).

11. **WoonJengSPXDataset2021Frozen.** WoonJeng. *Dataset for SPX Calibration of Option Approximations under Rough Heston model*. 2021. [Source](https://github.com/WoonJeng/Dataset-for-SPX-Calibration-of-Option-Approximations-under-Rough-Heston-model/tree/860049da2b7486fe8aa509061eff23cc28c2ef89).

12. **Gilewicz2005.** Gilewicz, Jacek and Pindor, Maciej and Telega, J. Joachim and Tokarzewski, Stanisław. *N-Point Padé Approximants and Two-Sided Estimates of Errors on the Real Axis for Stieltjes Functions*. Journal of Computational and Applied Mathematics 178(1–2), 247–253, 2005. DOI [10.1016/j.cam.2003.12.051](https://doi.org/10.1016/j.cam.2003.12.051).

13. **EberleinGlauPapapantoleon2008v1.** Eberlein, Ernst and Glau, Kathrin and Papapantoleon, Antonis. *Analysis of valuation formulae and applications to exotic options in Lévy models*. 2008. [Source](https://arxiv.org/abs/0809.3405v1). Version used: arXiv:0809.3405v1.

14. **Heston1993.** Heston, Steven L. *A Closed-Form Solution for Options with Stochastic Volatility with Applications to Bond and Currency Options*. The Review of Financial Studies 6(2), 327–343, 1993. DOI [10.1093/rfs/6.2.327](https://doi.org/10.1093/rfs/6.2.327).

15. **CozmaReisinger2016.** Cozma, Andrei and Reisinger, Christoph. *Exponential integrability properties of Euler discretization schemes for the Cox–Ingersoll–Ross process*. Discrete and Continuous Dynamical Systems - B 21(10), 3359–3377, 2016. DOI [10.3934/dcdsb.2016101](https://doi.org/10.3934/dcdsb.2016101). Version used: arXiv:1601.00919v1.

16. **KimKimKimWee2016.** Kim, Bara and Kim, Jeongsim and Kim, Jerim and Wee, In-Suk. *A recursive method for discretely monitored geometric Asian option prices*. Bulletin of the Korean Mathematical Society 53(3), 733–749, 2016. DOI [10.4134/BKMS.b150283](https://doi.org/10.4134/BKMS.b150283).

17. **BoydVandenberghe2004.** Boyd, Stephen and Vandenberghe, Lieven. *Convex Optimization*. Cambridge University Press, 2004. [Source](https://web.stanford.edu/~boyd/cvxbook/).

18. **MickelNeuenkirch2022v2.** Mickel, Annalena and Neuenkirch, Andreas. *The weak convergence order of two Euler-type discretization schemes for the log-Heston model*. 2022. [Source](https://arxiv.org/abs/2106.10926v2). Version used: arXiv:2106.10926v2.

19. **BertsimasPopescu2002.** Bertsimas, Dimitris and Popescu, Ioana. *On the Relation between Option and Stock Prices: A Convex Optimization Approach*. Operations Research 50(2), 358–374, 2002. [Source](https://www.mit.edu/~dbertsim/papers/Finance/On%20the%20relation%20between%20option%20and%20stock%20prices-%20a%20convex%20optimization%20approach.pdf).

20. **Hartmann2008.** Hartmann, Ralf. *Multitarget Error Estimation and Adaptivity in Aerodynamic Flow Simulations*. SIAM Journal on Scientific Computing 31(1), 708–731, 2008. [Source](https://elib.dlr.de/57073/1/Har08a.pdf).

21. **CboeSPX2022.** Cboe Global Markets. *Cboe to Further Expand S&P 500 Index Options Suite with New and Additional Daily Expirations*. 2022. [Source](https://ir.cboe.com/news/news-details/2022/Cboe-to-Further-Expand-SP-500-Index-Options-Suite-with-New-and-Additional-Daily-Expirations-09-19-2022/default.aspx).

22. **FederalReserveSR1107.** Board of Governors of the Federal Reserve System and Office of the Comptroller of the Currency. *Supervisory Guidance on Model Risk Management*. Board of Governors of the Federal Reserve System and Office of the Comptroller of the Currency(SR 11-7, Attachment), 2011. [Source](https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf). This reference concerns the historical model-validation framework published in 2011.
