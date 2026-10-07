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
\tag{1.1}
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


## 2. Model, price and actual output

Our conventions for the fractional integral and Caputo derivative are
\[
I^\alpha f(t)=\frac1{\Gamma(\alpha)}\int_0^t(t-s)^{\alpha-1}f(s)\,ds,
\qquad D_C^\alpha v=I^{1-\alpha}v',\quad v\in AC.
\tag{2.1}
\]
Under the regularity of the trajectories used below, \(I^\alpha f\in AC\) with zero initial value, so \(D_C^\alpha I^\alpha f=f\). The Caputo operator and all time scalings retain their fractional definitions. Set \(a=u-i/2\). The physical Riccati state \(h\) satisfies
\[
D_{C,t}^\alpha h=-\frac{a^2+ia}{2}
 +(i\rho\nu a-\lambda_R)h+\frac{\nu^2}{2}h^2,\qquad h(0)=0.
\tag{2.2}
\]
Define
\[
x=\nu^{1/\alpha}t,\quad y=x^\alpha=\nu t^\alpha,\quad
H(x)=\nu h(t),\quad Z(t)=H(\nu^{1/\alpha}t),\quad
\kappa=\lambda_R/\nu,
\tag{2.3}
\]
\[
b=(u^2+1/4)/2,\quad s_0=\kappa-\rho/2,\quad d=-s_0+i\rho u,\quad
F(z)=-b+dz+z^2/2.
\]
Then \(D_{C,x}^\alpha H=F(H)\) and \(D_{C,t}^\alpha Z=\nu F(Z)\). Dividing the normalised state error by \(\nu\) gives the physical \(h\) error. Likewise, dividing the physical residual \(r_t=D_t^\alpha\widehat Z-\nu F(\widehat Z)\) by \(\nu\) gives the residual bound for the normalised equation.

For pricing and the numerical example, we fix \(\kappa=0\) and the entire forward variance curve
\[
\xi_*(t)=\theta+(V_0-\theta)E_{\alpha_0}(-\lambda_\xi t^{\alpha_0}),
\quad
(\alpha_0,V_0,\theta,\lambda_\xi)=(.5286,.0262,.0721,.5037).
\tag{2.4}
\]
The curve parameter \(\lambda_\xi\) and Riccati parameter \(\lambda_R\) are defined separately. Curve (2.4) remains fixed when the candidate \(\alpha\) changes. The probability model is
\[
V_t=\xi_*(t)+\nu\int_0^tK_\alpha(t-s)\sqrt{V_s}\,dW_s,\quad
K_\alpha(t)=t^{\alpha-1}/\Gamma(\alpha),\qquad
dS_t=S_t\sqrt{V_t}\,dB_t,\quad d\langle B,W\rangle_t=\rho\,dt.
\tag{2.5}
\]
Equation (2.5) is the forward variance representation with zero Riccati mean reversion. Appendix A verifies the probability model and affine transform associated with this curve using Theorems 2.1 and 2.3 and Example 2.2 of Abi Jaber and El Euch.

Let \(M_T=S_T/F_T\) be the normalised positive martingale and write \(\phi_T(a)=\mathbb E M_T^{ia}\). The exact characteristic exponent is
\[
L_T(u)=\int_0^T\xi_*(T-t)F(Z(t,u))\,dt,\quad
\phi_T(u-i/2)=e^{L_T(u)}.
\tag{2.6}
\]
With \(m=K/F_T,k=\log m,c=C/(DF_T)\), the model European call price is
\[
c=1-\frac{\sqrt m}{\pi}\int_0^\infty
\operatorname{Re}\frac{e^{-iuk}\phi_T(u-i/2)}{u^2+1/4}\,du.
\tag{2.7}
\]
The model specification, decimal inputs, and normalisation jointly define the prices considered below.

## 3. Finite-history propagation to the pricing exponent

### 3.1. Regularity and complex dissipation

If \(H=I^\alpha F(H)\) is a bounded local continuous solution, then \(H,F(H)\) are \(\alpha\)-Hölder continuous. For \(\alpha>1/2\), write \(q=F(H)\). Cancellation gives the derivative formula
\[
H'(x)=\frac{q(x)x^{\alpha-1}}{\Gamma(\alpha)}
 +\frac{\alpha-1}{\Gamma(\alpha)}
\int_0^x(x-t)^{\alpha-2}[q(t)-q(x)]\,dt.
\tag{3.1}
\]
The bound 

\[
|H'(x)|\le\frac{\|q\|_\infty x^{\alpha-1}}{\Gamma(\alpha)}+\frac{(1-\alpha)[q]_{C^\alpha}x^{2\alpha-1}}{\Gamma(\alpha)(2\alpha-1)}.
\tag{3.2}
\]

is integrable at zero. Positive-time continuity and the limit from truncated intervals establish absolute continuity on the closed interval. The near-endpoint exponent satisfies \(2\alpha-2>-1\); the other endpoint and the first term are integrable. Thus \(H\in AC\) and it is locally \(C^1\) at positive times. Local existence follows from Volterra contraction on a bounded ball. For \(v\in AC\) that is locally Lipschitz at positive times, integration by parts gives
\[
D_C^\alpha v(x)=\frac1{\Gamma(1-\alpha)}
\left\{\frac{v(x)-v(0)}{x^\alpha}
 +\alpha\int_0^x\frac{v(x)-v(t)}{(x-t)^{1+\alpha}}\,dt\right\}.
\tag{3.3}
\]
At a positive maximum over the full history, with zero initial value, this derivative is strictly positive. Consequently, \(D_C^\alpha v+s v\le D_C^\alpha w+s w\), \(v(0)=w(0)\), and \(s\ge0\) imply \(v\le w\). For a convex \(C^1\) function \(\Phi\) on the real plane, apply the supporting-hyperplane inequality to both terms in (3.3) to obtain
\[
D_C^\alpha\Phi(v)\le\nabla\Phi(v)\cdot D_C^\alpha v.
\tag{3.4}
\]
This is the established Caputo history-convexity inequality, rather than an ordinary chain rule. We work within the regularity assumptions of Proposition 3.11 of Li and Liu [LiLiu2018] and directly prove the version needed here.

**Lemma 3.1.** Suppose \(\alpha\in(1/2,1),|\rho|\le1,s_0\ge0\). The normalised equation has a unique global solution, and \(\operatorname{Re}H(x)<0\) for \(x>0\). If \(s_0>0\), then
\[
|H(x)|\le\frac b{s_0}[1-E_\alpha(-s_0x^\alpha)]
\le\min\{b/s_0,bx^\alpha/\Gamma(1+\alpha)\}.
\tag{3.5}
\]
When \(s_0=0\), the latter time-dependent bound remains valid.

**Proof.** Write \(H=X+iY\). Completing the square gives
\[
\operatorname{Re}F(H)
=-\frac18-\frac{1-\rho^2}{2}u^2
-\frac12(Y+\rho u)^2-s_0X+\frac12X^2.
\tag{3.6}
\]
If \(X\) first reaches a small positive level \(\varepsilon<1/2\), the derivative in (3.3) is positive, whereas (3.6) is negative, a contradiction. Thus \(X\le0\). Reaching zero at a positive time gives the same contradiction, proving strict negativity.

Let \(\psi_\epsilon(z)=\sqrt{|z|^2+\epsilon^2}-\epsilon\). Equation (3.4), together with
\[
\operatorname{Re}(\overline H F(H))
=-bX-s_0|H|^2+\tfrac12X|H|^2,\quad
\frac{|H|^2}{\sqrt{|H|^2+\epsilon^2}}\ge\psi_\epsilon(H),
\]
gives \(D_C^\alpha\psi_\epsilon(H)+s_0\psi_\epsilon(H)\le b\). Compare with the zero-initial-value linear scalar equation and let \(\epsilon\downarrow0\) to obtain (3.5). The scalar solution is verified directly by the Mittag–Leffler series. If finite-time blow-up occurred, (3.5) would bound the trajectory, \(F(H)\), and a uniform Hölder constant. The history integral would have a finite limit at that endpoint, and local contraction with the previously accumulated history as forcing would extend the solution, a contradiction. The Caputo history is not restarted. Successive Volterra contractions give uniqueness. ∎

**Theorem 3.2 (dissipative residual bound).** Suppose \(s_0>0\), \(\widehat H(0)=0\), and \(\widehat H\in AC\), with local Lipschitz regularity at positive times. Assume, for every \(x\in(0,X]\), that
\[
\operatorname{Re}\widehat H\le\epsilon_R<2s_0,\qquad
|D_C^\alpha\widehat H-F(\widehat H)|\le\delta,
\]
Set \(\sigma=s_0-\epsilon_R/2>0\). Then
\[
|H-\widehat H|
\le\frac\delta\sigma[1-E_\alpha(-\sigma x^\alpha)]
\le\delta/\sigma.
\tag{3.7}
\]
In particular, for a trajectory in the left half-plane, one may take \(\epsilon_R=0,\sigma=s_0\). No smallness assumption on \(\delta\) or \(u\) is required.

**Proof.** The error \(e=H-\widehat H\) satisfies
\[
D_C^\alpha e=\left(d+\frac{H+\widehat H}{2}\right)e-r,\quad e(0)=0,\quad
\operatorname{Re}\left(d+\frac{H+\widehat H}{2}\right)\le-\sigma.
\]
Apply (3.4) to \(\psi_\epsilon(e)\) to obtain
\(D_C^\alpha\psi_\epsilon(e)+\sigma\psi_\epsilon(e)\le|r|\le\delta\).
Comparison with the linear scalar solution, followed by \(\epsilon\downarrow0\), proves the claim. Convex regularisation includes points of zero error and applies to the complex error viewed as a vector in the real plane. ∎

If \(\widehat H\) corresponds to the physical-time trajectory \(\widehat Z\) and \(|r_t|/\nu\le\delta_F\) has been certified, the same result gives
\[
\sup_{t\le T}|Z-\widehat Z|\le\delta_F/s_0
\quad\text{if }\operatorname{Re}\widehat Z\le0.
\tag{3.8}
\]
In the numerical example, \(s_0=1489/4000\). This dissipation rate controls the complex error modulus; Section 4.1 supplies the independent residual \(\delta_F\). The estimate applies the established convexity tool to the specific error propagation considered here.



### 3.2. A regularity bridge for comparison

The scalar comparison mechanism is established fractional-calculus machinery. Li and Liu [LiLiu2018, Proposition 3.11(ii)] give convexity after regularization and passage to a distributional limit. Their Proposition 4.12 concerns specified vector gradient and Hamiltonian flows. Kopteva [Kopteva2021v2, Lemma 2.8 and Theorem 2.2] uses norm convexity and a positive fractional inverse under positive-time Lipschitz hypotheses. The following elementary bridge proves the vector \(AC\) version consumed here directly, including the terminal-time conclusion. It is an adaptation of those tools, not a new general Caputo comparison theorem.

**Regularity lemma (AC convexity and the continuous endpoint).** Let \(0<\alpha<1\), \(T>0\), \(v\in AC([0,T];\mathbb R^d)\), and let \(\Phi\in C^1(\mathbb R^d)\) be convex. With \(D_C^\alpha v=g_{1-\alpha}*v'\),

\[
D_C^\alpha\Phi(v)\le \nabla\Phi(v)\cdot D_C^\alpha v
\quad\text{a.e. on }(0,T).
\tag{3.9}
\]

Let \(u\in AC[0,T]\), \(u(0)=0\), \(\lambda\ge0\), and \(R\in L^\infty(0,T)\) be nonnegative. If \(D_C^\alpha u+\lambda u\le R\) almost everywhere, then

\[
u(t)\le(k_\lambda*R)(t),\qquad 0\le t\le T,
\quad k_\lambda(t)=t^{\alpha-1}E_{\alpha,\alpha}(-\lambda t^\alpha).
\tag{3.10}
\]

**Proof.** Choose smooth \(f_n\to v'\) in \(L^1(0,T)\), and set \(v_n(t)=v(0)+\int_0^t f_n(s)\,ds\). Then \(v_n(0)=v(0)\), \(v_n\to v\) uniformly, and \(v_n'\to v'\) in \(L^1\). For a smooth path, integration by parts expresses the difference between the two sides of (3.9) as

\[
\frac{1}{\Gamma(1-\alpha)}\left[
\frac{B_\Phi(v_n(0),v_n(t))}{t^\alpha}
+\alpha\int_0^t\frac{B_\Phi(v_n(s),v_n(t))}{(t-s)^{1+\alpha}}\,ds
\right]\ge0,
\tag{3.11}
\]

where \(B_\Phi(a,b)=\Phi(a)-\Phi(b)-\nabla\Phi(b)\cdot(a-b)\ge0\). Smooth paths are locally Lipschitz. A gradient bound \(M\) on the compact path range and a local path Lipschitz constant \(L\) give \(B_\Phi(v_n(s),v_n(t))\le2ML|t-s|\). The endpoint kernel \((t-s)^{-\alpha}\) is therefore integrable. The supporting-hyperplane inequality may first be integrated with history truncated at \(t-\delta\), and the classical Caputo integrals converge as \(\delta\downarrow0\).

All path ranges lie in one compact set. Continuity of \(\nabla\Phi\) and the ordinary \(AC\) composition rule give

\[
\|\Phi(v_n)' - \Phi(v)'\|_1\to0,
\qquad
\|D_C^\alpha(v_n-v)\|_1
\le\frac{T^{1-\alpha}}{\Gamma(2-\alpha)}\|v_n'-v'\|_1\to0.
\tag{3.12}
\]

The same convolution estimate applies to \(\Phi(v_n)-\Phi(v)\). Moreover, the products \(\nabla\Phi(v_n)\cdot D_C^\alpha v_n\) converge in \(L^1\) to the corresponding product for \(v\). Passing to an almost-everywhere convergent subsequence proves (3.9). This uses the ordinary composition rule only for the first derivative inside \(AC\); no Caputo chain rule is asserted.

For (3.10), put \(f=D_C^\alpha u+\lambda u\in L^1(0,T)\). The zero initial value gives \(u+\lambda g_\alpha*u=g_\alpha*f\). The locally convergent resolvent series, whose \(n\)-th term has \(L^1(0,T)\) norm bounded by \(\lambda^{n-1}T^{n\alpha}/\Gamma(1+n\alpha)\), gives \(u=k_\lambda*f\) almost everywhere. Complete monotonicity of \(E_{\alpha,\alpha}(-x)\) [SimonCM2015] supplies \(k_\lambda\ge0\), so \(f\le R\) implies \(u\le k_\lambda*R\) almost everywhere. The convolution on the right is continuous: extend \(k_\lambda\) and \(R\) by zero, and use \(L^1\) translation continuity of the kernel with the \(L^\infty\) bound on \(R\). Its value at zero is zero. Since \(u\) is continuous, an almost-everywhere inequality extends to every point of \([0,T]\), including maturity. ∎

### 3.3. The central finite-history pricing theorem

The model-specific step is the composition of the dissipative complex Riccati error with the derivative-based Heston pricing functional. The complete history remains attached to the initial time; the result applies to any fixed reference that satisfies the stated certificate hypotheses, independently of how the production Padé output is computed.

**Theorem 3.3 (finite-history pricing envelope).** Let \(0<\alpha<1\), \(\nu>0\), \(T>0\), and \(Z,\widehat Z\in AC([0,T];\mathbb C)\) have zero initial value. Let

\[
D_C^\alpha Z=\nu F(Z),\quad
r=D_C^\alpha\widehat Z-\nu F(\widehat Z),\quad
|r|\le R\in L^\infty(0,T),\qquad R\ge0,
\tag{3.13}
\]

where \(F(z)=-b+dz+z^2/2\), \(\Re d=-s_0\), \(\Re Z\le0\), \(\Re\widehat Z\le\epsilon_R\), and \(\sigma=s_0-\epsilon_R/2>0\). These equations and inequalities hold almost everywhere; the state bounds hold everywhere by continuity. Let \(\xi\in AC[0,T]\), \(\xi(0)=V_0\ge0\), and assume

\[
q_\alpha=(I^{1-\alpha}\xi)'
=V_0g_{1-\alpha}+g_{1-\alpha}*\xi'\ge0\quad\text{a.e.}
\tag{3.14}
\]

Define \(L_T\) and \(\widehat L_T\) from \(\nu^{-1}\int_0^T\xi(T-t)D_C^\alpha Z(t)\,dt\) and the same expression with \(\widehat Z\). With \(\lambda=\nu\sigma\),

\[
|Z-\widehat Z|\le k_\lambda*R,
\qquad
|L_T-\widehat L_T|
\le\nu^{-1}(q_\alpha*k_\lambda*R)(T)
\le\nu^{-1}(\xi*R)(T).
\tag{3.15}
\]

In particular, \(R/\nu\le\delta_F\) implies

\[
|L_T-\widehat L_T|\le\delta_F\int_0^T\xi(s)\,ds.
\tag{3.16}
\]

**Proof.** For \(e=Z-\widehat Z\), the divided difference gives \(D_C^\alpha e=\nu[d+(Z+\widehat Z)/2]e-r\), with coefficient real part at most \(-\lambda\). Apply the regularity lemma to \(v_\varepsilon=(|e|^2+\varepsilon^2)^{1/2}-\varepsilon\). Since \(\nabla v_\varepsilon\cdot e=|e|^2/(|e|^2+\varepsilon^2)^{1/2}\ge v_\varepsilon\) and \(|\nabla v_\varepsilon|\le1\),

\[
D_C^\alpha v_\varepsilon+\lambda v_\varepsilon\le R\quad\text{a.e.}
\tag{3.17}
\]

Equation (3.10) and the limit \(\varepsilon\downarrow0\) yield the first state inequality at every time. Absolute Fubini gives \(I^{1-\alpha}\xi=V_0g_{2-\alpha}+g_{2-\alpha}*\xi'\), whose derivative is \(N5\), and \(g_\alpha*q_\alpha=\xi\). In particular, \(q_\alpha\in L^1\) and \(\xi\ge0\). Writing \(A_\alpha=I^{1-\alpha}\xi\), another absolute Fubini step followed by \(AC\) integration by parts gives

\[
L_T-\widehat L_T
=\nu^{-1}\int_0^TA_\alpha(T-t)e'(t)\,dt
=\nu^{-1}(q_\alpha*e)(T).
\tag{3.18}
\]

The first Fubini integral is bounded by \(\|\xi\|_\infty T^{1-\alpha}\|e'\|_1/\Gamma(2-\alpha)\); the boundary terms vanish because \(A_\alpha(0)=e(0)=0\). Positivity now proves the first exponent estimate. Finally, \(g_\alpha-k_\lambda=\lambda g_\alpha*k_\lambda\ge0\), whence

\[
0\le q_\alpha*k_\lambda
=\xi-\lambda\xi*k_\lambda\le\xi.
\tag{3.19}
\]

Associativity and nonnegative integration yield the remaining conclusions. The physical residual is \(R\), so its factor \(\nu^{-1}\) remains until \(R/\nu\le\delta_F\) is used. ∎

The novelty claimed here is the explicit Heston pricing-functional connection, its certified cell weights and its inclusion in the complete error of a frozen numerical output. Convexity, resolvent positivity, disk support functions and unit-cost sorting are prior tools. The hypothesis on \(q_\alpha\) is an analytical propagation condition; probability-model existence, the affine transform and the martingale property are checked separately.

For a full-history residual envelope \(R\le R_j\) on each closed cell \([a_j,b_j]\), the computable cell-weight version is

\[
|L_T-\widehat L_T|
\le\nu^{-1}\sum_jR_j\int_{a_j}^{b_j}(q_\alpha*k_\lambda)(T-s)\,ds
\le\nu^{-1}\sum_jR_j\int_{a_j}^{b_j}\xi(T-s)\,ds.
\tag{3.20}
\]

The first weights may be used only when they are enclosed rigorously; the implemented experiments use the second weights. When a pricing partition intersects several source residual cells, its envelope is the maximum over every intersected closed cell. The Caputo history is never restarted at a cell boundary.


### 3.4. Curve condition and the constant-curve kernel

The curve condition in Theorem 3.3 is the nonnegativity of \(q_\alpha=(I^{1-\alpha}\xi)'\), rather than monotonicity of \(\xi\). The state and reference still belong to \(AC[0,T]\), have the same zero initial value, and satisfy the full-time residual and dissipation hypotheses in (3.13). The physical residual remains \(R\), the normalized residual is \(R/\nu\), and physical damping is \(\lambda=\nu\sigma>0\). Both exponents retain the D-type definitions in Section 3. These assumptions are required for each application; the condition on the pricing kernel does not prove stochastic-model existence or extend the verified Riccati regularity domain.

For a real curve \(\xi\in AC[0,T]\) with \(\xi(0)=V_0\ge0\), the precise sufficient condition is

\[
q_\alpha=V_0g_{1-\alpha}+g_{1-\alpha}*\xi'\ge0
\quad\text{a.e.},\qquad g_\beta(t)=t^{\beta-1}/\Gamma(\beta).
\tag{3.21}
\]

No sign is imposed on \(\xi'\). Indeed, \(A_\alpha=I^{1-\alpha}\xi=V_0g_{2-\alpha}+g_{2-\alpha}*\xi'\) is absolutely continuous, \(A_\alpha(0)=0\), and

\[
\|q_\alpha\|_1\le
\frac{T^{1-\alpha}}{\Gamma(2-\alpha)}(V_0+\|\xi'\|_1),
\qquad g_\alpha*q_\alpha=\xi.
\tag{3.22}
\]

Absolute Fubini proves the second identity even for signed \(\xi'\), using \(g_\alpha*g_{1-\alpha}=g_1\). The initial term \(V_0g_{1-\alpha}\) cannot be dropped. Condition (3.21) implies \(\xi\ge0\). Hence the entire proof of Theorem 3.3 continues to hold: integration by parts gives \(L_T-\widehat L_T=\nu^{-1}(q_\alpha*e)(T)\), and the positive resolvent identity gives

\[
0\le q_\alpha*k_\lambda
=\xi-\lambda\xi*k_\lambda\le\xi.
\tag{3.23}
\]

The Fubini step for the exponent is bounded by \(\|\xi\|_\infty T^{1-\alpha}\|e'\|_1/\Gamma(2-\alpha)\); its boundary terms vanish because \(e(0)=A_\alpha(0)=0\). The AC Caputo convexity and the positive zero-initial-value inverse remain the prior tools [LiLiu2018, Kopteva2021v2]. The finite-history convolution, cell-weight bound (3.20), and outward node-radius construction therefore remain valid under (3.21). Cells still carry the complete Caputo history.

This is a strict relaxation of a sufficient curve condition, not a necessary condition for every conceivable certificate. If \(q_\alpha\) changes sign, the safe general estimate is \(\nu^{-1}(|q_\alpha|*k_\lambda*R)(T)\); the positive collapse to \(\xi*R\) cannot be used without further proof. Fractional forward-variance representations and their model-admissibility restrictions already occur in [ElEuchRosenbaum2017v1, Proposition 3.1 and Corollary 3.3]. Our analytical condition does not replace those restrictions.

**Corollary 3.4 (a decreasing analytical curve).** Let \(V_0>0\), \(c>0\), and \(\xi(t)=V_0(1-ct)\). Then

\[
q_\alpha(t)=\frac{V_0t^{-\alpha}}{\Gamma(1-\alpha)}
\left(1-\frac{ct}{1-\alpha}\right).
\tag{3.24}
\]

Thus (3.21) holds on \((0,T)\) if and only if \(cT\le1-\alpha\), including equality. In that case \(\xi(T)\ge\alpha V_0>0\) despite \(\xi'<0\).

**Proof.** Convolving the constant derivative \(-V_0c\) with \(g_{1-\alpha}\) gives \(-V_0c\,t^{1-\alpha}/\Gamma(2-\alpha)\). Adding the initial term and using \(\Gamma(2-\alpha)=(1-\alpha)\Gamma(1-\alpha)\) proves (3.24). Its bracket is nonnegative exactly under the stated condition. ∎

This example is analytical and has not been used as a new financial experiment or asserted to be a realized rough-Heston variance curve. Positivity of the curve alone is insufficient for (3.21): \(1-\alpha<cT<1\) leaves \(\xi>0\) but gives a negative kernel near maturity.

**Corollary 3.5 (explicit constant-curve propagation).** Under Theorem 3.3's state hypotheses, let \(\xi\equiv V_0\ge0\). Then

\[
q_\alpha*k_\lambda=V_0E_\alpha(-\lambda t^\alpha),\qquad
|L_T-\widehat L_T|\le
\frac{V_0}{\nu}\int_0^T
E_\alpha(-\lambda(T-s)^\alpha)R(s)\,ds.
\tag{3.25}
\]

If \(R\le\nu\delta_F\), a closed-form upper bound is

\[
\eta_{\rm ML}=V_0\delta_F T E_{\alpha,2}(-\nu\sigma T^\alpha)
\le\min\left\{
V_0\delta_F T,
\frac{V_0\delta_F T^{1-\alpha}}{\nu\sigma\Gamma(2-\alpha)}
\right\}.
\tag{3.26}
\]

**Proof.** Termwise convolution in the absolutely locally integrable Mittag--Leffler series gives \(g_{1-\alpha}*k_\lambda=E_\alpha(-\lambda t^\alpha)\); termwise integration gives \(\int_0^T E_\alpha(-\lambda t^\alpha)dt=T E_{\alpha,2}(-\lambda T^\alpha)\). Equation (3.23) gives \(0\le E_\alpha\le1\), proving the first comparison. Also \(\int_0^tk_\lambda=(1-E_\alpha(-\lambda t^\alpha))/\lambda\le1/\lambda\). The state envelope \(|e|\le\delta_F/\sigma\), followed by the positive \(q_\alpha\) integral, proves the second comparison. ∎

The explicit bound retains finite history and physical scaling. It may be intersected with earlier independently valid exponent bounds only when all bound the same D-type target and reference. A substitution-based reference requires its separately certified residual conversion. This corollary is analytical; it does not assert that a Mittag--Leffler weighted propagation routine has been numerically implemented or that a new model instance has been certified.

**Proposition 3.6 (an error radius without an assumed approximate half-plane).** If \(\delta_F<s_0^2/2\), every admissible AC trajectory, locally Lipschitz at positive times and with the same initial value, satisfies
\[
|Z-\widehat Z|\le E_\delta
=s_0-\sqrt{s_0^2-2\delta_F}
=\frac{2\delta_F}{s_0+\sqrt{s_0^2-2\delta_F}}.
\tag{3.27}
\]
To prove this, rewrite the error terms as \((d+Z)e-e^2/2\). The exact-solution half-plane gives
\(D_t^\alpha|e|\le\nu(-s_0|e|+|e|^2/2+\delta_F)\), interpreted through the same convex regularisation of the modulus. Choose any \(E_\delta<\ell<s_0+\sqrt{s_0^2-2\delta_F}\). The right-hand side is strictly negative at \(|e|=\ell\); a first hitting time of \(\ell\) contradicts (3.3). Letting \(\ell\downarrow E_\delta\) proves the result. This is a sufficient small-residual condition; violating it does not establish an actual error or pole. The completed node trajectories in this example have a certified half-plane property and use (3.8), which does not impose the threshold in (3.27).

## 4. Continuous reference certificates and complete Fourier prices

### 4.1. Startup, continuous residuals and outward arithmetic

For each candidate \(\alpha=\beta\in\{.52,.6,.9\}\) and each \(u=n/8,\ n=0,\ldots,512\), we store
\[
\bar G(t)=\nu c_0+A_1t^\beta+A_2t^{2\beta}+\bar L(t),\quad
c_0=-(u^2+1/4)/2,\quad \widehat Z=I^\alpha\bar G,\quad T=1/2.
\tag{4.1}
\]
Here \(\bar L\) is the continuous piecewise-linear interpolation in physical time at nodes \((t_j,L_j)\), with \(L_0=0\). Nodes and complex coefficients are interpreted as the exact dyadic rationals represented by their binary64 values. The following independent residual controls the continuous-time error of this reference trajectory:
\[
r_t=\bar G-\nu F(\widehat Z),\quad
\delta_F=\nu^{-1}\sup_{0\le t\le T}|r_t|.
\tag{4.2}
\]
Equation (4.1) defines an entire absolutely continuous reference trajectory. Its independent residual gives the model-price intervals, which are then used to bound the output error of the selected [3/3] implementation.

Write
\[
\widehat Z=H_0+J,\quad J=I^\alpha\bar L,\quad
H_0=B_1t^\alpha+B_2t^{\alpha+\beta}+B_3t^{\alpha+2\beta},
\]
\[
B_1=\frac{\nu c_0}{\Gamma(1+\alpha)},\quad
B_2=\frac{A_1\Gamma(1+\beta)}{\Gamma(1+\alpha+\beta)},\quad
B_3=\frac{A_2\Gamma(1+2\beta)}{\Gamma(1+\alpha+2\beta)}.
\tag{4.3}
\]
The initial interval is \(J=L_1t^{\alpha+1}/[t_1\Gamma(2+\alpha)]\). Substitute all generalised powers into (4.2), first cancel \(\nu c_0\) exactly, combine equal powers, and then take \(\sum_p|r_p|t_1^p\). Since every \(p>0\), this bounds the full initial closed interval. The generalised-power expansion retains the fractional initial behaviour.

On a source interval \([a,b]\subset[0,q]\), set \(\tau=q-a,h=b-a\). The integral weights for the linear hat functions are
\[
I_0=\{\tau^\alpha-(\tau-h)^\alpha\}/\alpha,\quad
I_1=\{\tau^{\alpha+1}-(\tau-h)^{\alpha+1}\}/(\alpha+1),
\]
\[
w_R=(\tau I_0-I_1)/(h\Gamma(\alpha)),\quad
w_L=I_0/\Gamma(\alpha)-w_R.
\tag{4.4}
\]
These weights are nonnegative. For a truncated interval, recover the endpoints by affine interpolation within the original interval. On the final interval, \(b=q\) can be evaluated directly using
\(w_R=h^\alpha/[\alpha(\alpha+1)\Gamma(\alpha)],w_L=\alpha w_R\).
For \(h/\tau<.01\), retain eight positive-series terms, using respectively
\[
w_R=\frac{h\tau^{\alpha-1}}{\Gamma(\alpha)}
\sum_{k\ge0}\frac{(1-\alpha)_k(h/\tau)^k}{k!(k+2)},\quad
w_L=\frac{h\tau^{\alpha-1}}{\Gamma(\alpha)}
\sum_{k\ge0}\frac{(1-\alpha)_k(h/\tau)^k}{k!(k+1)(k+2)}.
\tag{4.5}
\]
The unscaled tails are each bounded by \(z^8/(1-z)\) because \(0<(1-\alpha)_k/k!\le1\). This reduces interval inflation from subtracting nearly equal endpoint quantities while retaining rigorous history integration.

Subdivide each subsequent original interval twice into four closed subintervals \([a,b]\), with recorded dyadic centres \(m\). Given a derivative bound on the full subinterval,
\[
\sup_{[a,b]}|r_t|\le|r_t(m)|+\max(m-a,b-m)\sup_{[a,b]}|r_t'|.
\tag{4.6}
\]
The ordinary residual derivative may be discontinuous at original nodes. The derivative bounds below hold almost everywhere; absolute continuity of the residual and the fundamental theorem of calculus still imply (4.6). Each of the following three identities provides a derivative bound, and we take their minimum:
\[
r_t'=\bar G'-\nu(d+\widehat Z)\widehat Z',
\]
\[
P_r=\nu c_0+A_1t^\beta+A_2t^{2\beta}-\nu F(H_0),\quad
r_t=P_r+\bar L-\nu(d+H_0)J-\nu J^2/2,
\]
\[
r_t'=P_r'+\bar L'-\nu[(d+H_0+J)J'+H_0'J],
\quad
\widehat Z'=\frac{\nu c_0\,t^{\alpha-1}}{\Gamma(\alpha)}+I^\alpha\bar G'.
\tag{4.7}
\]
The constant-kernel weight of a past source interval decreases with the integration endpoint, whereas the weight of the current source interval increases while that endpoint lies within it. Endpoint bounds therefore enclose both types of weight. In the third identity, first combine
\(\bar G'(s)=\beta A_1s^{\beta-1}+2\beta A_2s^{2\beta-1}+\bar L'(s)\) on each source interval and then integrate against the positive kernel, retaining cancellation in the original relation.

The singular terms from the initial source interval are handled directly by fractional-power integrals. For \(p>0,t_1\le a\le q\le b\), the positive weight satisfies
\[
\frac{t_1^pb^{\alpha-1}}{p\Gamma(\alpha)}
\le\frac1{\Gamma(\alpha)}\int_0^{t_1}s^{p-1}(q-s)^{\alpha-1}\,ds
\le\min\left\{
\frac{t_1^p(a-t_1)^{\alpha-1}}{p\Gamma(\alpha)},
\frac{\Gamma(p)}{\Gamma(\alpha+p)}
 \max_{q\in[a,b]}q^{\alpha+p-1}\right\}.
\tag{4.8}
\]
When \(a=t_1\), discard the first upper bound. The second follows from the full Euler Beta integral and is finite. Kernel monotonicity at the endpoints gives the lower bound and the first upper bound. Every \(p,\alpha>0\), so the hypotheses of the classical Beta formula hold.

Using the same \(\widehat Z'\) enclosure and rigorous point values, certify an upper bound for \(\operatorname{Re}\widehat Z\) on every subsequent subinterval. On the initial interval, factor out \(t^\alpha\), leaving a finite bracket; use its negative constant term and the endpoint contributions of the remaining positive parts. Bound (3.8) is used only when the upper real-part bound is nonpositive on every closed interval. This condition therefore covers the entire closed time interval.

The structural certificate and special functions use outward-rounded intervals with integer endpoints divided by \(2^{100}\). Batched residual weights use IEEE binary64; each basic operation is enlarged outward to adjacent representable numbers. After converting an exact rational Gamma enclosure, endpoint inclusion is checked with Fraction. The logarithm uses exact binary scaling and a twenty-two-term atanh series with \(z\in[0,1/3]\), whose tail is \(2z^{45}/[45(1-z^2)]\). After scaling, the exponential has \(|r|<1\) and a degree-24 Taylor tail bounded by \(3/25!\). These explicit remainders define the intervals for logarithms, exponentials, and noninteger powers.

For matrix multiplication with rigorous weight centres \(W_c\), radii \(W_r\), and recorded dyadic values \(X\), include
\[
\left(\gamma_{2n}\|W_c\|_{1,\mathrm{row}}+
\|W_r\|_{1,\mathrm{row}}\right)\|X\|_{\infty,\mathrm{column}},
\quad \gamma_{2n}=\frac{2n\,2^{-53}}{1-2n\,2^{-53}},
\tag{4.9}
\]
and an additional underflow-error allowance. Induction on products of basic rounding factors gives this estimate and permits different summation association orders. Norm summations are also rounded outward. The calculation assumes round-to-nearest IEEE basic operations, correctly rounded square roots, gradual underflow, and the absence of overflow or NaNs. The supplementary material records source and computation versions. The interval-inclusion conclusions in this section are conditional on these arithmetic assumptions and the stated remainder bounds.

For the fixed curve, define
\[
J_0(z)=\theta z+(V_0-\theta)zE_{\alpha_0,2}(-\lambda_\xi z^{\alpha_0}),\quad
J_1(z)=\theta z^2/2+
(V_0-\theta)z^2(E_{\alpha_0,2}-E_{\alpha_0,3})(-\lambda_\xi z^{\alpha_0}).
\tag{4.10}
\]
These quantities are respectively \(\int_0^z\xi_*(s)ds,\int_0^zs\xi_*(s)ds\); termwise integration verifies the second formula. If a linear-trajectory interval is \([a,b]\) with \(A=T-b,B=T-a\), its rigorous nonnegative exponent weights are
\[
w_l=\frac{J_1(B)-J_1(A)-A[J_0(B)-J_0(A)]}{b-a},\quad
w_r=\frac{B[J_0(B)-J_0(A)]-J_1(B)+J_1(A)}{b-a}.
\tag{4.11}
\]
The curve moment for the power component \(t^\beta\) is
\[
\int_0^T\xi_*(T-t)t^\beta dt
=\frac{\theta T^{\beta+1}}{\beta+1}
 +(V_0-\theta)\Gamma(\beta+1)T^{\beta+1}
 E_{\alpha_0,\beta+2}(-\lambda_\xi T^{\alpha_0}).
\tag{4.12}
\]
This follows directly from the series and Beta integration. Together with (4.1), it makes \(\bar L\) a rigorous finite sum. Trigonometric phases and complex exponentials also use finite Taylor expansions with explicit tails. On the present horizon, if \(z=\lambda_\xi T^{\alpha_0}<1\), a Mittag–Leffler series tail may be bounded by \(3z^{64}/(1-z)\): all Gamma arguments exceed one, and Euler's integral gives \(\Gamma(\gamma)\ge e^{-1}>1/3\). Rigorous integration encloses the approximate exponent, while (C.5) controls the difference between the model and approximate exponents.

### 4.2. Analytic-strip quadrature, true tails and price inclusion

**Theorem 4.1.** Suppose \(M_T>0,\mathbb E M_T=1\). For any \(0<a_*<1/2,h_*>0\), let
\(g(z)=e^{-ikz}\phi_T(z-i/2)/(z^2+1/4)\). Replacing the integral in (2.7) by the infinite trapezoidal sum incurs a price error of at most
\[
\epsilon_{\rm grid}
=\frac{\sqrt m\,e^{a_*|k|}}
{(1/2-a_*)(e^{2\pi a_*/h_*}-1)}.
\tag{4.13}
\]

**Proof.** Jensen's inequality gives, within the strip,
\(|\phi_T(z-i/2)|\le\mathbb E M_T^{1/2-\operatorname{Im}z}\le1\).
On compact substrips, \(x^q|\log x|^j\le C(1+x)\), so the transform is analytic. The boundaries \(z=r\pm ia_*\) satisfy
\[
|z^2+1/4|\ge r^2+(1/2-a_*)^2,\quad
\int_{\mathbb R}|g(r\pm ia_*)|\,dr
\le M_*=\frac{\pi e^{a_*|k|}}{1/2-a_*}.
\]
Shift the real-axis Fourier integration contour to the upper and lower boundaries. The vertical integrals vanish by quadratic decay, giving
\(|\widetilde g(\omega)|\le M_*e^{-a_*|\omega|}\).
The absolutely and uniformly convergent periodisation \(\sum_{j\in\mathbb Z}g(x+jh_*)\) has Fourier coefficients
\(h_*^{-1}\widetilde g(2\pi n/h_*)\). Summing at zero and subtracting \(n=0\) gives a two-sided error of at most
\(2M_* /(e^{2\pi a_*/h_*}-1)\).
Conjugate symmetry halves both the two-sided integral and its sum. Multiplication by \(\sqrt m/\pi\) gives (4.13). ∎

This is a specific application of the analytic-strip trapezoidal theory of Trefethen and Weideman [TrefethenWeideman2014]. Each pricing node uses its own continuous-time residual bound; the analytic strip controls the quadrature error between nodes.

Fix \(\kappa=0,-1<\rho<0\). Set \(X=-\operatorname{Re}H\ge0\). Equation (3.6) gives
\[
D_x^\alpha X\ge\beta_u-s_0X-X^2/2,\quad
\beta_u=(1-\rho^2)u^2/2+1/8.
\tag{4.14}
\]
Let \(w\) be the scalar zero-initial-value solution satisfying equality. Comparison gives
\[
X\ge w,\quad 0\le w\le R_u,\quad
R_u=\sqrt{s_0^2+2\beta_u}-s_0,\quad
\ell_u=(s_0+\sqrt{s_0^2+2\beta_u})/2.
\]
Because the right-hand side satisfies \((R_u-w)(s_0+(R_u+w)/2)\ge\ell_u(R_u-w)\), linear comparison and the bound of Simon [Simon2014],
\(E_\alpha(-z)\le(1+z/\Gamma(1+\alpha))^{-1}\), give
\[
-\operatorname{Re}Z(t,u)\ge
R_u\frac{\ell_u\nu t^\alpha}{\Gamma(1+\alpha)+\ell_u\nu t^\alpha}.
\tag{4.15}
\]
The comparison argument uses a positive maximum over the full history.

Take \(V>s_0/\sqrt{1-\rho^2}\) and define
\[
a_\rho=\sqrt{1-\rho^2},\quad b_V=a_\rho-s_0/V>0,\quad
f_\alpha(z)=z/(\Gamma(1+\alpha)+z).
\]
For \(u\ge V\), we have \(R_u/u\ge b_V,\ell_u\ge a_\rho u/2\). For any partition of \(J\ge2\), denoted \(0=t_0<\cdots<t_J=T\), the positive kernel in (C.4) and the monotonicity of \(f_\alpha\) give
\[
c_V=\frac{b_V}{\nu}\sum_{j=0}^{J-1}
 f_\alpha(a_\rho\nu Vt_j^\alpha/2)
 [A_\alpha(T-t_j)-A_\alpha(T-t_{j+1})]>0,
\]
\[
|\phi_T(u-i/2)|\le e^{-c_Vu}\quad(u\ge V).
\tag{4.16}
\]
This envelope holds at every continuous high frequency. The time partition constructs a lower sum for the positive-measure integral. The example uses \(J=64\) and rigorous intervals to obtain a positive rational lower bound for \(c_V\). No singular evaluation is performed at \(A_\alpha(0)=0\). The difference between bounds taken from the appropriate sides at distinct endpoints,
\([A_{\rm lo}(T-t_j)-A_{\rm hi}(T-t_{j+1})]_+\),
is a valid lower bound on the mass.

Using the right-endpoint sum of a positive decreasing function, for \(V=Nh_*\) the exact discrete-tail contribution to the normalised price is bounded by
\[
\epsilon_{\rm tail}
\le\frac{\sqrt m}{\pi}\frac{e^{-c_VV}}{c_VV^2}.
\tag{4.17}
\]
The integral tail uses an envelope for the exact solution. Finite nodes assigned the value zero are charged according to the same envelope, so every part of the frequency range has an explicit error contribution.

Suppose the node values \(\widehat\phi_n\) have exact-error bounds \(\varepsilon_n\). The finite price sum
\[
\widehat c_N=1-\frac{h_*\sqrt m}{\pi}
\left(2\operatorname{Re}\widehat\phi_0+
\sum_{n=1}^N\frac{\operatorname{Re}(e^{-inh_*k}\widehat\phi_n)}
{(nh_*)^2+1/4}\right)
\tag{4.18}
\]
satisfies
\[
|c-\widehat c_N|\le\epsilon_{\rm grid}+\epsilon_{\rm tail}
 +\frac{h_*\sqrt m}{\pi}
\left(2\varepsilon_0+
\sum_{n=1}^N\frac{\varepsilon_n}{(nh_*)^2+1/4}\right)
 +\epsilon_{\rm arithmetic}.
\tag{4.19}
\]
The coefficient \(2\) is the product of the trapezoidal half-weight at \(u=0\) and the denominator factor \(1/4\). Rigorous intervals include rounding errors in the phase, square root, exponential, and finite summation. Here \(h_*=1/8,a_*=9/20,N=1024\). The first \(513\) nodes, \(u\le64\), use independent residual bounds; the remaining node approximations are zero, with their errors bounded by the exact-transform envelope. For \(u>128\), we use (4.17). This hybrid rule combines node errors and the tail in one price estimate.

### 4.3. The independent reference field

For each candidate, a separately implemented product-integration procedure generates and fixes a physical-time reference function
\(\bar G=\nu c_0+A_1t^\beta+A_2t^{2\beta}+\bar L\), where \(\beta=\alpha_j\). Its nodes and coefficients are interpreted as their recorded exact dyadic values. The certified trajectory is \(\widehat Z=I^\alpha\bar G\), rather than the floating-point PI nodes themselves. The initial time interval uses the full generalised-power residual expansion. The remaining closed intervals use rigorous convolution-derivative bounds and the mean value theorem, covering all \(t\in[0,1/2]\). At each Fourier node, division of the physical residual by exact \(\nu\) gives the input to the proved error barrier or certified half-plane linear error estimate.

The recorded exponent is derivative-based: \(\bar L_T=\nu^{-1}\int\xi_*(T-t)\bar G(t)dt\). The positive kernel \(q_\alpha=(I^{1-\alpha}\xi_*)'\ge0\) gives
\[
|L_T-\bar L_T|
\le E_{\rm state}(I^{1-\alpha}\xi_*)(T)/\nu
\le E_{\rm state}\theta T^{1-\alpha}/[\nu\Gamma(2-\alpha)].
\tag{4.20}
\]
No residual integral is added a second time. Gamma and Mittag–Leffler curve moments, trajectory integrals, exponents, phases, and sums for the fixed curve use outward-rounded 100-bit rational intervals.

The positive-half-axis price rule has \(h=1/8\) and analytic-strip width \(a=9/20\). At the available nodes \(u=0:1/8:64\), the recorded trajectories use their actual residual certificates. For nodes above 64 through 128, the approximate transform is explicitly zero and each error is bounded by the exact-transform envelope. Above 128, the proved infinite discrete-rule tail bound obtained from the proved continuous-integral envelope is included. A comparison bound for the real part of the exact Riccati solution and a 64-cell lower sum over the entire positive-kernel curve give the high-frequency envelope. The analytic-strip trapezoidal error is estimated separately. Passage from the full-axis integral to the positive half-axis, including the half-weight at zero, is handled explicitly. The resulting enclosures cover all twelve model prices in the technical appendix and are based on error bounds rather than grid-convergence differences or Richardson diagnostics.

Here \(E_{\rm state}\) is any valid certified state radius: the expression \(E_\delta\) of Proposition 3.6 requires \(\delta_F<s_0^2/2\); at other nodes the certified half-plane bound gives \(E_{\rm state}=\delta_F/\sigma\). The complete new experiments primarily use the finite-history exponent envelope of Theorem 3.3, and retain this global alternative only when valid and tighter. The nearby fields use the same construction with independently generated coefficients and continuous residual banks.

## 5. Shared Fourier errors and financial decisions

### 5.1. Joint inclusion at the frozen output

Fix one model parameter, maturity, contour, and reference grid. Let \(c^*\in\mathbb R^p\) be the continuous-model price vector, \(\bar c\) the exact finite reference sum, and \(c^{\rm fast}\) the frozen rational output. For each included frequency let \(\bar\phi_n\) be the reference transform and put \(z_n=\phi(u_n-i/2)-\bar\phi_n\). Section 4.1 supplies bounds \(|z_n|\le\epsilon_n\); at a deliberately omitted finite node \(\bar\phi_n=0\), the true-transform envelope supplies the radius. The same \(z_n\) enters every strike at this parameter and maturity.

For the Lewis rule in Section 4.2, set \(m_i=K_i/F\), \(k_i=\log m_i\), and
\[
a_{in}=-\frac{h\sqrt{m_i}}{\pi}\frac{e^{-iu_nk_i}}{u_n^2+1/4}\quad(n>0),\qquad
a_{i0}=-\frac{2h\sqrt{m_i}}{\pi}.
\tag{5.1}
\]
The half weight at zero is already included in \(a_{i0}\). The complete error is
\[
c^*-\bar c=\Re\sum_{n=0}^{N}a_{\cdot n}z_n+R,
\qquad R\in\mathcal R,
\tag{5.2}
\]
where \(\mathcal R\) includes the true infinite-grid tail and analytic-strip discretisation error. A finite reference sum enclosed by interval arithmetic contributes its centre uncertainty when a numerical representative of \(\bar c\) is used. Omitted finite nodes remain in (5.2); they are not also charged as an infinite tail. No stochastic covariance is used in this representation.

**Theorem 5.1 (complete shared-node inclusion).** Suppose (5.2) holds, all radii are nonnegative, and \(\mathcal R\) is a nonempty compact convex outer set. Define
\[
\mathcal E_F=\left\{\Re\sum_na_{\cdot n}z_n:|z_n|\le\epsilon_n\right\}+\mathcal R,
\qquad d=\bar c-c^{\rm fast}.
\tag{5.3}
\]
Then \(c^*-c^{\rm fast}\in d+\mathcal E_F\), and, for real \(w\),
\[
h_{d+\mathcal E_F}(w)=w^\top d+
\sum_n\epsilon_n\left|\sum_iw_i a_{in}\right|+h_{\mathcal R}(w).
\tag{5.4}
\]
If the centre shift is supplied as a box \(d\in[d^-,d^+]\), replace the first term by the support of that box. All numerical evaluations of (5.4) must be outward enclosures.

**Proof.** Substituting the actual transform errors in (5.2) gives inclusion. The product of complex disks is compact and convex and its real-linear image has those properties. A disk \(|z|\le\epsilon\) has real-linear support \(\epsilon|b|\) for the functional \(\Re(bz)\): Cauchy--Schwarz gives the upper bound, attained at \(z=\epsilon\overline b/|b|\) when \(b\ne0\); when \(b=0\), every feasible point attains it. Independent disks and Minkowski addition give (5.4). Translation gives the signed centre term. A box enclosing \(d\) provides a further valid Minkowski outer enclosure even if its coordinates are dependent. \(\square\)

If \(\mathcal R=\prod_i[-\rho_i,\rho_i]\), the smallest coordinate box of this same set has support
\[
h_{\operatorname{rect}(\mathcal E_F)}(w)=
\sum_i|w_i|\left(\sum_n\epsilon_n|a_{in}|+\rho_i\right).
\tag{5.5}
\]
Consequently its excess over (5.4), before translation, is
\[
G_F(w)=\sum_n\epsilon_n\left(
\sum_i|w_i a_{in}|-\left|\sum_iw_i a_{in}\right|\right)\ge0.
\tag{5.6}
\]
It is strictly positive exactly when one positive-radius node has nonzero coefficients \(w_i a_{in}\) that do not all lie on a common nonnegative complex ray. This follows from the equality case of the complex triangle inequality, node by node. Translation does not change widths. This criterion compares the constructed set with its own coordinate box, and does not assert strict improvement over every independently available signed price enclosure.

For any separately established signed model-price box \(\mathcal I\), intersect it with \(\bar c+\mathcal E_F\). The actual model vector belongs to the intersection. Without solving the intersection support problem, the minimum of the two valid directional upper bounds remains valid; likewise take the maximum of the lower bounds. Thus a computation can retain the best signed marginal information while using node cancellation where it improves the complete bound. Nonemptiness of the mathematical intersection follows from inclusion, rather than from empirical agreement between numerical approximations.

**Proposition 5.2 (nonzero omitted-node reference at an unchanged fast output).** Fix the actual fast output, including its zero contribution at omitted finite nodes. For the same finite pricing map, select a possibly nonzero reference \(\psi_n\) at those nodes, and prove \(|\phi_n-\psi_n|\le\rho_n\). Let \(\bar c'=c_0+\Re(A\psi)\), \(d'=\bar c'-c^{\rm fast}\), and let \(\mathcal R\) include the complete strip, true infinite tail, and newly enclosed reference arithmetic. Then

\[
c^*-c^{\rm fast}\in d'
+\{\Re(Az):|z_n|\le\rho_n\}\oplus\mathcal R.
\tag{5.7}
\]

For a symmetric remainder and direction \(w\), the complete absolute budget uses

\[
DF\left(|w^\top d'|+
\sum_n\rho_n\left|\sum_iw_ia_{in}\right|
+h_{\mathcal R}(w)\right)\le\tau.
\tag{5.8}
\]

For a nonsymmetric remainder, both support directions must be bounded. A changed reference centre does not change the fixed fast output, but it does change \(d'\) and requires new centre arithmetic.

**Proof.** Subtract and add the new finite reference in the exact finite pricing map; its transform error is \(z=\phi-\psi\). The complete remainder contains the other discrepancies. Directional support of the shared complex disks gives (5.8). ∎

An old zero-centred certificate \(|\phi_n|\le\varepsilon_n^0\) and a new certificate centred at \(\psi_n\) cannot have their radii directly minimized. At the new centre, the old certificate only gives \(|\phi_n-\psi_n|\le\varepsilon_n^0+|\psi_n|\). A safe radius is therefore \(\min\{\rho_n,\varepsilon_n^0+|\psi_n|\}\), or one can retain the two transform disks' intersection. A new disk is nested in the old disk only if \(|\psi_n|+\rho_n\le\varepsilon_n^0\). Otherwise, independently valid complete price intervals may still be intersected, but same-centre monotonicity is not automatic. For example, \(\phi=0\) lies in \(D(0,.1)\) and \(D(1,2)\), but not in \(D(1,\min(.1,2))\). Marginal and joint comparisons must use the same updated centre, node radii, and complete remainder. Any additional reference evaluation and certification is part of the reported cost.

### 5.2. Directional and finite-objective certificates

For \(w=e_i-e_j\), the node coefficient is
\[
|a_{in}-a_{jn}|=\frac{h}{\pi(u_n^2+1/4)}
\left|\sqrt{m_i}e^{-iu_nk_i}-\sqrt{m_j}e^{-iu_nk_j}\right|\quad(n>0).
\tag{5.9}
\]
It is the modulus of one combined coefficient, rather than the sum of two moduli. A useful analytic bound, valid with \(b_i=\sqrt{m_i}\), is
\[
|b_ie^{-iuk_i}-b_je^{-iuk_j}|
\le |b_i-b_j|+\min(b_i,b_j)\min\{2,|u|\,|k_i-k_j|\}.
\tag{5.10}
\]
To prove it, separate the difference in amplitudes from the phase difference using the smaller amplitude, then apply \(|e^{ix}-e^{iy}|\le\min(2,|x-y|)\). At zero, the spread coefficient is \(2h|b_i-b_j|/\pi\). Low-frequency error therefore cancels for nearby strikes even when the individual node radii are large. High-frequency and tail contributions are still retained.

The implementation below uses rational outward bounds for logarithms, trigonometric functions, square roots, and the circle constant. It encloses the exact coefficient difference before multiplying by the saved radius. Reference-sum and frozen-output intervals supply the signed centre. Taking interval midpoints for display never substitutes for the outward endpoint arithmetic used in a decision.

If the target quote \(m^*\) is enclosed around a stored centre \(\bar m\) with \(m^*-\bar m\in\mathcal M\), use \(r=c^{\rm fast}-\bar m\) and replace the output-error set by \(\mathcal E-\mathcal M\). This includes quote-conversion arithmetic with the correct sign. The following formulas otherwise take \(m\) to be exact.

Let \(J(e)=(r+e)^\top W(r+e)/(2p)\), where \(r=c^{\rm fast}-m\), \(W\succeq0\), and the complete output error belongs to a compact convex set \(\mathcal E\). For any trial vector \(e_0\), put \(g_0=W(r+e_0)/p\). Convexity gives the certified lower bound
\[
\inf_{e\in\mathcal E}J(e)\ge
J(e_0)-g_0^\top e_0-h_{\mathcal E}(-g_0).
\tag{5.11}
\]
This follows by taking the infimum of the supporting affine function \(J(e_0)+g_0^\top(e-e_0)\). Feasibility of \(e_0\) is unnecessary for validity; it affects sharpness. A numerical primal minimizer becomes a lower-bound certificate only after its support or dual obligation has also been bounded correctly.

If \(M^2\ge\sup_{e\in\mathcal E}e^\top We\), expansion yields
\[
\sup_{e\in\mathcal E}J(e)\le
J(0)+\frac{h_{\mathcal E}(Wr)}p+\frac{M^2}{2p}.
\tag{5.12}
\]
A safe choice is any valid coordinate box \(|e_i|\le b_i\): with \(W\) represented exactly, \(M^2=\sum_{ij}|W_{ij}|b_i b_j\) is sufficient. Tighter validated norm bounds may replace it. Maximization of this convex quadratic is not certified by a local stationary point. A supporting function, norm bound, interval subdivision, or valid relaxation must establish the upper direction.

For a finite candidate collection, form valid objective intervals by intersecting (5.11)--(5.12), when used, with the original interval-square bounds in Theorem 5.3. A unique candidate is certified only if its upper endpoint is smaller than every competing lower endpoint. If this condition is absent, return the nonempty set of candidates whose lower endpoint is at most the least upper endpoint. It contains every exact minimizer. Different candidates have different transform errors; (5.4) does not identify their error variables.

The support formula, the equality case of the triangle inequality, and the convexity bounds are established tools. Their role here is to join the model-specific continuous residual certificate to the actual multi-strike pricing output, preserving every required budget and its centre. The numerical comparison in Section 7 is the evidence for the resulting financial improvement.

**Theorem 5.3 (finite-objective intervals and selection stability).** For each \(\alpha_j\in\Theta_{\rm finite}\), suppose all model prices have certified enclosures
\[
c_i(\alpha_j)\in[p^-_{ij},p^+_{ij}],\quad
B_i\in[b_i^-,b_i^+],\quad
A_i\in[a_i^-,a_i^+],\quad
M_i\in[m_i^-,m_i^+].
\tag{5.13}
\]
Assume \(b_i^-\le b_i^+\le a_i^-\le a_i^+\). Define
\[
\ell(x,y)=
\begin{cases}0,&x\le0\le y,\\
\min(x^2,y^2),&\text{otherwise},\end{cases}
\quad v(x,y)=\max(x^2,y^2).
\]
\[
L_j=\frac1{24}\sum_i
\ell(p^-_{ij}-m_i^+,p^+_{ij}-m_i^-),\qquad
U_j=\frac1{24}\sum_i
v(p^-_{ij}-m_i^+,p^+_{ij}-m_i^-).
\tag{5.14}
\]
Then \(J(\alpha_j)\in[L_j,U_j]\). Writing \(L_*=\min_jL_j,U_*=\min_jU_j\), the exact finite-set optimum satisfies
\[
J_*=\min_{\Theta_{\rm finite}}J\in[L_*,U_*].
\tag{5.15}
\]
For \(\varepsilon\ge0\), every exact \(\varepsilon\)-near-optimal candidate belongs to
\[
\{\alpha_j:L_j\le U_*+\varepsilon\};
\tag{5.16}
\]
The condition \(U_j-L_*\le\varepsilon\) is sufficient for that candidate to be near-optimal for the exact objective. If
\[
g:=\min_{j\ne j_0}L_j-U_{j_0}>0,
\tag{5.17}
\]
then \(\alpha_{j_0}\) is the unique minimiser of the model objective on the finite set. If
\[
\min_{\alpha_j\ge.6}L_j>U_*+\varepsilon,
\tag{5.18}
\]
then every exact near-optimal candidate in the finite set satisfies \(\alpha_j<.6\).

Quote consistency is checked separately. If any row satisfies \(p^+_{ij}<b_i^-\) or \(p^-_{ij}>a_i^+\), the candidate cannot lie in all quote bands simultaneously. Conversely, if every row satisfies \(p^-_{ij}\ge b_i^+\) and \(p^+_{ij}\le a_i^-\), then quote consistency is certified. Overlapping intervals without this inner-band condition retain possible consistency; overlap alone does not certify it.

**Proof.** The exact difference \(c_i-M_i\) belongs to the closed interval used in (5.14). The minimum of its square is \(\ell\) and the maximum is \(v\), so the weighted sum encloses every \(J_j\). Each \(J_j\ge L_j\ge L_*\); a candidate attaining the smallest \(U_j\) gives \(J_*\le J_j\le U_*\), proving (5.15). If \(J_j\le J_*+\varepsilon\), then \(L_j\le J_j\le U_*+\varepsilon\), proving (5.16). Conversely, \(J_j-J_*\le U_j-L_*\) gives the stated sufficient inner condition. Under (5.17), every competitor satisfies \(J_j-J_{j_0}\ge L_j-U_{j_0}\ge g>0\), proving uniqueness. Condition (5.18) places the model objective of every selected higher-H candidate above \(J_*+\varepsilon\) and therefore excludes it. No independence assumption on quote errors across candidates is needed.

If \(p^+<b^-\), then the exact price satisfies \(c<B\); if \(p^->a^+\), then \(c>A\). A single such row rules out simultaneous consistency. In the opposite direction, the inner-band conditions give \(B\le b^+\le c\le a^-\le A\). Applying these statements row by row proves the consistency assertions. ∎

**Corollary (objective perturbation).** Suppose another numerical objective \(\widetilde J\) satisfies
\(\sup_{\Theta_{\rm finite}}|\widetilde J-J|\le\delta_J\), and its selected candidate is \(\varepsilon_{\rm alg}\)-near-optimal. Then
\[
J(\widehat\alpha)-J_*
\le2\delta_J+\varepsilon_{\rm alg}.
\tag{5.19}
\]
Indeed, \(J(\widehat\alpha)\le\widetilde J(\widehat\alpha)+\delta_J
\le\min\widetilde J+\varepsilon_{\rm alg}+\delta_J
\le J_*+2\delta_J+\varepsilon_{\rm alg}\).
If the strict gap in (5.17) satisfies \(g>2\delta_J+\varepsilon_{\rm alg}\), the same unique finite-set minimiser must be selected. This selection stability follows from the finite-objective gap and applies to the fixed candidate set (8.2).

## 6. Structure of the specified rational construction

Set \(S=s_0-i\rho u=-d\), take the principal square root in \(A=\sqrt{S^2+2b}\), and let \(R=A-S\). The three short-time and long-time coefficients are respectively
\[
b_1=-\frac b{\Gamma(1+\alpha)},\quad
b_2=\frac{Sb}{\Gamma(1+2\alpha)},\quad
b_3=\frac{\Gamma(1+2\alpha)}{\Gamma(1+3\alpha)}
       (d b_2+b_1^2/2),
\tag{6.1}
\]
\[
g_0=-R,\quad g_1=\frac R{A\Gamma(1-\alpha)},\quad
g_2=-\frac R{A^2\Gamma(1-2\alpha)}
       +\frac{R^2}{2A^3\Gamma(1-\alpha)^2}.
\tag{6.2}
\]
For \(1/2<\alpha<1\), \(\Gamma(1-2\alpha)\) is finite and negative. The fixed two-endpoint construction of Gatheral and Radoičić [GR2019] requires
\[
\widehat H(y)=P(y)/Q(y),\quad
Q=1+q_1y+q_2y^2+q_3y^3,
\]
\[
\widehat H=b_1y+b_2y^2+b_3y^3+O(y^4),\quad
\widehat H=g_0+g_1y^{-1}+g_2y^{-2}+O(y^{-3}).
\tag{6.3}
\]
These six conditions give the linear system
\[
\begin{pmatrix}g_0&g_1&g_2\\b_1&-g_0&-g_1\\
b_2&b_1&-g_0\end{pmatrix}
\begin{pmatrix}q_1\\q_2\\q_3\end{pmatrix}
=\begin{pmatrix}b_1\\-b_2\\-b_3\end{pmatrix},
\quad p_1=b_1,\quad p_2=b_2+b_1q_1,\quad p_3=g_0q_3.
\tag{6.4}
\]
Equations (6.1)–(6.4) are the established construction. We next prove invertibility, a nonvanishing denominator, the trajectory half-plane property, and exact-solution error bounds for an independent reference trajectory.

To avoid division by the matching determinant before proving its nonvanishing, define
\[
f=\Gamma(1+\alpha)^{-1},\quad p=\frac{\sin\pi\alpha}{\pi\alpha},
\quad v=-\cos\pi\alpha,\quad
m_\alpha=\frac{\Gamma(1+2\alpha)}{\Gamma(1+\alpha)^2},\quad
\zeta=\frac{\Gamma(1+2\alpha)\Gamma(1+\alpha)}{\Gamma(1+3\alpha)},
\]
\[
\mathsf d=Sb/m_\alpha,\quad
\mathsf c=\zeta(b^2/2-S^2b/m_\alpha),\quad
V=pR/A,\quad W=m_\alpha p v R/A^2+p^2R^2/(2A^3).
\tag{6.5}
\]
The reflection formula and recurrence relations give \(b_1=-fb,b_2=f^2\mathsf d,b_3=f^3\mathsf c\) and \(g_1=V/f,g_2=W/f^2\). In the latter two expressions, the factors \(f,f^2\) occur in the denominators. Direct expansion of the determinant and Cramer numerators of (6.4) gives
\[
\begin{aligned}
\Delta={}&b^2W+2bRV-\mathsf dRW-\mathsf dV^2-R^3,\\
F_1={}&b^2V+b\mathsf dW-bR^2+\mathsf dRV+\mathsf cRW+\mathsf cV^2,\\
F_2={}&-b^2R+b\mathsf dV+b\mathsf cW+\mathsf d^2W+\mathsf dR^2+\mathsf cRV,\\
F_3={}&-b^3+2b\mathsf dR-b\mathsf cV-\mathsf d^2V+\mathsf cR^2.
\end{aligned}
\tag{6.6}
\]
Here \(\Delta\) is exactly the determinant of the original system, and the numerators are \(N_j=f^jF_j\). After establishing \(\Delta\ne0\), we may define \(q_j=N_j/\Delta\), in which case
\[
\Delta P=-fb\Delta y+f^2(\mathsf d\Delta-bF_1)y^2-f^3RF_3y^3,\quad
\Delta Q=\Delta+fF_1y+f^2F_2y^2+f^3F_3y^3.
\tag{6.7}
\]
In physical time, the denominator coefficients are \(\nu^jq_j\); the normalised coefficients \(q_j\) retain their original definition.

**Theorem 6.1 (full-frequency structure).** For
\[
\alpha\in[13/25,3/5],\quad \rho=-1489/2000,\quad \kappa=0,\quad
u\in\mathbb R,\quad \nu>0,
\tag{6.8}
\]
the established matching system (6.4) is nonsingular. Its normalised denominator satisfies
\[
\operatorname{Re}q_j>0\ (j=1,2,3),\qquad
\operatorname{Re}Q(y)\ge1,\quad |Q(y)|\ge1\quad(y\ge0).
\tag{6.9}
\]
Moreover, for \(y>0\), \(\operatorname{Re}\widehat H(y)<0\). The result holds at every positive time and every finite real frequency. Its domain is the stated parameter set; \(\alpha>.6\), a continuous \(\rho\) domain, and nonzero \(\kappa\) are outside the scope of this theorem.

**Proof.** First take \(u\ge0\). Set
\[
\omega=\sqrt{u^2+1/4},\quad \eta=u/(1+u),\quad
j(\eta)=\sqrt{\eta^2+(1-\eta)^2/4},\quad s=-\rho/2,
\]
\[
\bar S=s(1-\eta+2i\eta)/j(\eta),\quad
\bar A=\sqrt{1+\bar S^2},\quad \bar R=(\bar A+\bar S)^{-1}.
\tag{6.10}
\]
Since \(j^2\ge1/5\), these functions are defined on the closed interval \(\eta\in[0,1]\). We have \(|\bar S|=|\rho|\) and
\[
\operatorname{Re}\bar A^2
=1-\rho^2+2(\operatorname{Re}\bar S)^2\ge1-\rho^2>0.
\]
The principal square root is continuous and lies in the first quadrant; \(\operatorname{Re}\bar A,|\bar A|>3/5\). The real part of the Hermitian product of two first-quadrant numbers is nonnegative. Hence
\[
|\bar A+\bar S|^2\ge|\bar A|^2+|\bar S|^2
\ge|\bar A^2-\bar S^2|=1,\quad
|\bar R|\le1,\quad\operatorname{Re}\bar R>0.
\]
Equation (6.10) expresses \(\bar A-\bar S\) in reciprocal form, with a denominator determined directly by the current parameters.

Substitute \(\bar b=1/2\) and (6.10) into (6.5)–(6.6) to obtain the barred original quantities. Homogeneity gives
\[
\Delta=\omega^3\bar\Delta,\qquad F_j=\omega^{3+j}\bar F_j.
\tag{6.11}
\]
Define three real functions
\[
\bar B_j=\operatorname{Re}(\bar F_j\overline{\bar\Delta}).
\tag{6.12}
\]
The rigorous rational covering in Appendix B proves that, throughout the closed rectangle \([13/25,3/5]\times[0,1]\), \(\bar B_j>0\) and
\[
|\bar\Delta|^2\ge
\frac{88110801209184778874628745}{1267650600228229401496703205376}
>\frac1{14400}.
\tag{6.13}
\]
This first establishes \(\Delta\ne0\) and then yields
\(\operatorname{Re}q_j=(f\omega)^j\bar B_j/|\bar\Delta|^2>0\), proving (6.9).

For the trajectory half-plane, the finite convolution in (6.7) gives
\[
|\Delta|^2\operatorname{Re}(P\overline Q)
=\sum_{n=1}^6 f^nD_ny^n,
\tag{6.14}
\]
\[
\begin{aligned}
D_1={}&-b|\Delta|^2,\\
D_2={}&\operatorname{Re}(\mathsf d)|\Delta|^2-2b\operatorname{Re}(F_1\overline\Delta),\\
D_3={}&\operatorname{Re}\{-RF_3\overline\Delta+
(\mathsf d\Delta-bF_1)\overline F_1-b\Delta\overline F_2\},\\
D_4={}&\operatorname{Re}\{-RF_3\overline F_1+
(\mathsf d\Delta-bF_1)\overline F_2-b\Delta\overline F_3\},\\
D_5={}&\operatorname{Re}\{-RF_3\overline F_2+
(\mathsf d\Delta-bF_1)\overline F_3\},\\
D_6={}&-\operatorname{Re}R\,|F_3|^2.
\end{aligned}
\tag{6.15}
\]
The same rational covering certifies the six compactified quantities \(\bar D_n<0\), with scaling \(D_n=\omega^{7+n}\bar D_n\). Set \(z=f\omega y\). The right-hand side of (6.14) is
\(\omega^7\sum_{n=1}^6\bar D_nz^n\) and is therefore strictly negative for every \(y>0\). Having proved that the denominator is nonzero, division by \(|Q|^2|\Delta|^2\) gives \(\operatorname{Re}\widehat H<0\). Negative frequencies follow by conjugate symmetry of the principal root and matching coefficients. The closed endpoint \(\eta=1\) represents the infinite-frequency limit, so the proof on the closed compactified domain covers every finite frequency. ∎

Positive real parts of the coefficients provide a sufficient condition for a nonvanishing denominator. Appendix B specifies the algebraic identities, elementary-function remainder bounds, and continuous interval covering used in the computer-assisted proof.

### A continuous, quantitatively bounded correlation extension

The original domain was chosen to contain the public-data example's correlation and roughness candidates while keeping the six-condition construction fixed. The sign cover established a continuous roughness interval and all frequencies; it was not intended as a theorem over typical calibration boxes. Strict signs imply persistence in correlation. The following result makes that implication quantitative without replacing a continuous cover by a sampled grid.

**Theorem 6.2 (certified correlation persistence).** The conclusions of Theorem 6.1 hold for

\[
\alpha\in[13/25,3/5],\qquad
\rho\in[-744501/10^6,-744499/10^6],\qquad
\kappa=0,
\tag{6.16}
\]

at every real Fourier frequency and every positive time.

**Proof.** Retain the frequency compactification \(\eta=u/(1+u)\), \(0\le\eta\le1\), and the original unnormalized polynomials \(\Delta,F_j,B_j,D_j\). Write \(S_b=-\rho[(1-\eta)+2i\eta]/(2h)\), \(h^2=\eta^2+(1-\eta)^2/4\). Then \(|S_b|=|\rho|\), \(\Re S_b\ge0\) for negative \(\rho\), \(A^2=1+S_b^2\), and \(R=(A+S_b)^{-1}=A-S_b\). Throughout \(|\rho|\le3/4\), the square-root branch remains fixed because \(\Re A^2\ge1-\rho^2>0\). Consequently,

\[
|A|^{-1}\le8/5,\quad |A'|\le6/5,\quad
|(A^{-1})'|\le384/125,\quad |R|\le1,\quad |R'|\le11/5,
\tag{6.17}
\]

where primes denote real \(\rho\) derivatives. The identity \(|R|\le1\) follows from \(|A+S_b|^2\ge1\): the terms \(\Re A\,\Re S_b\) and \(\Im A\,\Im S_b\) are nonnegative, while \(|A|^2=|1+S_b^2|\ge1-|S_b|^2\). Also \(\Re R>0\), since \((\Re A)^2-(\Re S_b)^2=(|1+S_b^2|+1-|S_b|^2)/2>0\).

For the \(\alpha\)-dependent scalars of Theorem 6.1, exact outward endpoint enclosures give

\[
0<p\le2/3,\quad0\le v\le1/3,\quad
1\le m\le3/2,\quad0<\zeta\le2/3.
\tag{6.18}
\]

Here \(p\) decreases and \(v,m\) increase on the stated interval, while \(\zeta\) decreases. The gamma-ratio assertions follow from the increasing digamma function; \(m\ge1\) also follows from log convexity of \(\Gamma\). None depends on \(\rho\).

Apply product-rule modulus bounds to the original polynomial formulas. For every \((\alpha,\eta)\), the resulting exact rational constants \(L_{B,j},L_{D,j}\) satisfy

\[
|\partial_\rho B_j|\le L_{B,j},\qquad
|\partial_\rho D_j|\le L_{D,j}.
\tag{6.19}
\]

They are assembled using pairs \((M,N)\), meaning \(|f|\le M\), \(|f'|\le N\), with addition \((M_1+M_2,N_1+N_2)\) and multiplication \((M_1M_2,N_1M_2+M_1N_2)\). This yields a finite, directly checkable rational derivation rather than a numerical derivative estimate.

Let \(m_{B,j}(C),m_{D,j}(C)\) be the exact original sign lower bounds on a continuous \((\alpha,\eta)\) cell \(C\) at \(\rho_0=-1489/2000\). A cell is certified throughout the target correlation interval whenever all bounds

\[
m_{B,j}(C)-10^{-6}L_{B,j}>0,\qquad
m_{D,j}(C)-10^{-6}L_{D,j}>0
\tag{6.20}
\]

hold. The mean-value theorem proves this sufficient test; it uses a derivative enclosure, not numerical differentiation. It certifies 182002 original leaves and 79758 finer leaves. For the remaining cells, directly evaluate the original complex polynomial formulas with \(\rho\), \(\alpha\) and \(\eta\) all interval valued. Exact outward dyadic arithmetic certifies strict \(B_j>0\) and \(D_j<0\) on 19808 additional closed cells.

The original complete midpoint tree and the exact local splice trees verify that these 281568 cells cover the entire \((\alpha,\eta)\) rectangle without gaps or interior overlap. Their exact area is \(2/25\); each cell carries the entire correlation interval, giving exact three-dimensional volume \(1/6250000\). Hence the raw signs hold for every point of the stated domain. In particular \(\Delta\ne0\), the normalized denominator coefficients have positive real part, and all real numerator coefficients of the half-plane test are negative. The original algebraic implication gives (6.16), including \(\eta=1\), the infinite-frequency limit. Conjugacy supplies negative frequencies. ∎

This is a narrow local robustness result: the total correlation width is \(2\times10^{-6}\). It does not establish a typical broad calibration box or a new price experiment at an altered correlation. The direct interval supplement is explicitly exploratory: its protocol was frozen after the derivative-only attempt left positive unresolved area. The evidence retains that partial result and the separately valid conservative fallback.

The independent reader checks every saved original sign, the original 422481-node partition tree, the local splice geometry, the independently assembled derivative majorants and all 19808 direct cells through separate Cramer matrices and numerator-polynomial convolution. The dyadic primitives and saved original sign generation remain shared dependencies; every old interval-polynomial evaluation is not regenerated. Exact large fractions stay in the machine ledger. Neither a sampled correlation grid nor an assertion of continuity replaces any cell in this proof.


## 7. Financial decisions, attribution and output controls

### 7.1. Fixed contracts, units and complete ablation

The original six-month contract uses twelve strikes \(K_i=3700+100i\), \(0\le i\le11\), forward \(F=4221.86\), discount \(D=1\), and the fixed forward-variance curve in (2.4). Prices and task errors are in index points. The position multiplier is one; no exchange-specific currency notional is inferred. Candidate changes affect \(\alpha\) while leaving the curve and other parameters fixed. The three-candidate profile \(.52,.60,.90\) is a finite comparison and excludes several original bid/ask bands; it is not a successful market calibration or a continuous optimum.

The complete \(K=4400\) minus \(K=4500\) task bound is compared below. Each row retains its actual output, signed centre, included finite frequencies, strip, true tail and arithmetic. Displayed upper bounds are rounded upward. The quarter-year study recomputes its maturity-specific reference integral, true-transform envelopes and tails; its upstream full-history certificate is lawfully restricted to the shorter horizon. It does not reuse a six-month exponent or tail value.

| Maturity and stage | Complete joint bound, points | Matched signed marginal bound, points | Interpretation |
|---|---:|---:|---|
| Six months: global state propagation | 1.397612096 | — | Original failed one-point task |
| Six months: finite history, same global residual | 0.378598956 | — | Principal propagation improvement; unchanged output and centre |
| Six months: local envelope, original used nodes | 0.367258782 | — | About 3% further bound reduction |
| Six months: all finite high nodes, global envelope | 0.132245064 | 0.158585551 | High-frequency certification and centre change are included |
| Six months: all finite high nodes, local envelope | 0.115215934 | 0.137896018 | Both methods certify 0.25 points |
| Three months: through 64, global envelope | 1.207557898 | 1.545191542 | Failed 0.25-point task |
| Three months: through 128, global envelope | 0.351318692 | 0.408293698 | Failed 0.25-point task |
| Three months: through 128, local envelope | 0.233318843 | 0.252393939 | Only the joint method certifies 0.25 points |

The first finite-history reduction is about 72.91%, calculated against the displayed old complete bound. It is a reduction of a guaranteed error bound, not an observed reduction of true pricing error or trading loss. The six-month high-frequency refinement legally changes the centre from approximately \(-0.166762218\) to \(-0.081698202\) points. Its improvement therefore cannot be assigned wholly to common-error geometry. The last row compares equal output, centre, node radii and remainders, and isolates a decision changed by retaining the shared error variables. Its time-local refinement was fixed after the failed global stage and is an exploratory transfer experiment, rather than a retrospectively preregistered result.

### 7.2. Twenty-eight portfolio directions

Let \(e_i\) select strike \(K_i\). We keep the exact holdings below, without rescaling them to make a budget pass. Gross weight means \(\sum_i|w_i|\). Every threshold is an absolute error in index points for the specified holding vector.

| Family | Exact direction | Count | Gross weight |
|---|---|---:|---:|
| Adjacent spreads | \(e_i-e_{i+1},\ 0\le i\le10\) | 11 | 2 |
| Adjacent butterflies | \(e_i-2e_{i+1}+e_{i+2},\ 0\le i\le9\) | 10 | 4 |
| Wide spreads | \(e_0-e_3,e_3-e_6,e_6-e_9,e_0-e_{11}\) | 4 | 2 |
| Positive baskets | \(\frac1{12}\sum_{i=0}^{11}e_i,\ \frac16\sum_{i=0}^5e_i,\ \frac16\sum_{i=6}^{11}e_i\) | 3 | 1 |

All methods in each matched comparison use identical upstream radii. At a 0.5-point budget and \(\alpha=.52\), finite-history joint bounds certify 28/28 portfolios against 13/28 signed marginal bounds. At a 0.25-point budget, the corresponding counts are 10/28 against 1/28 for \(\alpha=.60\), and 20/28 against 13/28 for \(\alpha=.90\). At the looser one-point budget for \(.52\), both new methods certify 28/28; that improvement alone cannot isolate the shared structure. A lawful payoff intersection produces no additional tightening in the tested setting. Failure to certify means that this outer bound is insufficient, not that the true error exceeds the threshold.

### 7.3. Prespecified nearby candidates under the original quotes

The original twelve half-year quotes, forward F=4221.86, discount D=1,
and all other model parameters are fixed. Before computing new results we
froze alpha={0.520,0.525,0.530,0.540,0.550}, a first layer N=1024, and an
upgrade of **all five** candidates to N=2048 if any adjacent joint comparison
remained unresolved. Every point has a newly generated continuous reference
field and a complete closed-time residual bank. Fourier nodes through 64,
all omitted finite nodes through 128, true infinite tails, strip remainder,
reference arithmetic and original quote-conversion intervals are paid.

The objective is the original normalized midpoint loss
\(J=\frac1{24}\sum_i(c_i-m_i)^2\), using normalized calls. Index-point squared units would require multiplication by \(F^2\). Here the tiny target interval halfwidth is only
outward arithmetic error in converting the fixed bid/ask-price midpoint;
it is not the market bid/ask halfwidth. Ranking does not establish a uniform
winner for arbitrary quote targets inside those market bands.
A Taylor support enclosure preserves common
Fourier disks in its linear term and charges the full coordinate-radius
quadratic remainder. Its same-radius marginal comparison uses the identical
upstream certificate. Errors across different alpha candidates are not
assumed jointly correlated.

| alpha | N=1024 joint J ×10^8 | N=2048 joint J ×10^8 |
|---:|---:|---:|
| 0.520 | [4.825094, 6.778350] | [5.293449, 6.024095] |
| 0.525 | [5.645378, 7.501414] | [6.097920, 6.798485] |
| 0.530 | [6.748974, 8.517584] | [7.187004, 7.859529] |
| 0.540 | [9.807435, 11.422182] | [10.218707, 10.839486] |
| 0.550 | [14.000658, 15.482012] | [14.387007, 14.960680] |

| Generated layer | Joint strictly separated pairs | Matched marginal pairs |
|---|---:|---:|
| N=1024 | 7/10 | 3/10 |
| N=2048 | 10/10 | 7/10 |

The first layer retained its unresolved close pairs and triggered the frozen
all-candidate upgrade. The final finite grid has alpha=0.520 as a strict minimum.
This is a five-point comparison, not a continuous calibration optimum. All
five candidates remain incompatible with at least one original bid/ask row;
the finite-set result therefore does not identify a market-calibrated model.


Both layers fully generate every closed-cell residual entry: 15,754,230 entries, 5,130 reference exponents and 10,250 true-transform envelopes in total. Separate readers check complete coverage and maxima, reconstruct all exponents, coefficients and objectives, and reject deliberate corruptions; they share the stated rigorous primitives rather than independently rederive every residual derivative.

### 7.4. Why certify a frozen fast output?

The use case is validation of a stored or externally fixed output: an existing pricing-library audit, a reproducible historical result, or a production output that cannot be replaced in the task being checked. When the reference is already available and output replacement is allowed, directly returning its certified centre is an appropriate control. Centre-correcting the fast output is another control and must include the rounding of both the stored correction and final addition. The reference route does not automatically become an economical online solver merely because its downstream support function is inexpensive.

A separately frozen descriptive control reuses the complete \(N=2048,\alpha=.52\) residual bank with 128 history bins. Every intersected closed source cell contributes to each bin maximum, and all weights are outwardly enclosed. All five methods below use the same model, six-month \(4400-4500\) spread, 0.25-point tolerance, reference centre, node radii, strip and true-tail budget. This control does not change the prespecified nearby-grid experiment.

| Output | Complete joint, points | Matched marginal, points | Joint 0.25-point decision |
|---|---:|---:|---|
| Frozen Padé | 0.394999331 | 0.514096070 | UNRESOLVED |
| Direct reference (binary64) | 0.228237113 | 0.347333852 | PASS |
| Fast + stored correction | 0.228237113 | 0.347333852 | PASS |
| BL core, 512 steps | 0.229082759 | 0.348179497 | PASS |
| BL core, 1024 steps | 0.228534686 | 0.347631424 | PASS |

All five matched marginal bounds remain above 0.25 points. Direct reference and corrected fast values happen to have the same complete bound in this instance; their actual stored values are checked separately. Exact dyadic arithmetic charges the reference return, stored correction and final addition. For these freely replaceable outputs, the reference is simpler than delivering the unchanged fast result. The joint structure still changes the decision for the reference and BL outputs. The BL 512-to-1024 difference is a diagnostic, not its certified error.

The certificate is not free. Its generation encloses 2,100,735 continuous frequency-by-cell residual entries, 513 reference exponents and 1,025 true-transform node bounds, plus the infinite tail and 12,300 price coefficients. Full reading checks all these entries and reconstructs the exponents, coefficients and decisions. Each additional portfolio evaluates 1,025 shared-disk support terms and the complete remainder; 28 portfolios reuse the same bank without further residual generation. This is reuse across directions at one parameter and maturity, not reuse across unverified model parameters.

| Additional output construction | Deterministic mathematical work |
|---|---|
| Original Padé output | 352 Fourier values; 256 Jacobi samples per frequency |
| Direct returned reference | Return the already generated, fully charged centre with binary64 rounding |
| Corrected fast output | Store one correction and perform one binary64 addition per price |
| BL core, 512 steps | 67,371,264 history scalar-vector products; 2,626,560 transformed Riccati evaluations |
| BL core, 1024 steps | 269,222,400 history scalar-vector products; 5,253,120 transformed Riccati evaluations |

These are typed work counts, not interchangeable floating-point operations or a total-cost ratio. The field generation, outward transcendental evaluations and verification remain distinct from nominal output construction. No speed or machine-performance advantage is inferred. Complete ledgers record the additional exponent-quadrature work and both coarse failed control stages.


### 7.5. What the experiments do and do not establish

The modern-method comparison reimplements the modified-Adams Riccati core described by Boyarchenko et al.; it does not reproduce their full SINH deformation or Conformal Bootstrap. Agreement between two discretizations is a numerical diagnostic, not an interval certificate. Any comparison to a complete certified output must pay the independent reference, tails, arithmetic and verification costs required by that guarantee.

The fixed refinement menu certifies reliable termination when the complete task radius meets the budget. Its minimum number of actions assumes that every alternative radius is already certified and every action has unit cost. We retain those assumptions and do not infer minimum work for an unknown menu. Work spent constructing all alternatives remains part of certificate generation. Model fit, market uncertainty, transaction costs and global continuous calibration remain outside the output-error guarantee.


## 8. Applicability and a single reproducibility entry

The mathematical guarantee is conditional on the stated model, affine transform, regular reference trajectory and complete outward enclosures. The curve condition \(q_\alpha\ge0\) is sufficient for the propagation theorem, not by itself a proof of stochastic-model admissibility. The structural domain excludes general mean reversion and broad correlation calibration. A very narrow certified continuous correlation strip is evidence of local robustness only. Unresolved intervals, failed budgets and quote incompatibilities remain valid outcomes.

The formal reproducibility entry is the repository release pinned to `v2.0.0-research-20261007`. Its PDF, editable sources, evidence archive and reproduction command describe that same source revision. The named evidence archive includes the actual scientific inputs and independent readers; GitHub's automatically generated source archive is not substituted for it. A file manifest and checksums detect changes in the package, while scientific readers verify the claims those files support.

From the extracted evidence directory, run `python reproduce.py --full`. The default checks rebuild derived price and task conclusions from the enclosed fields and full residual banks. The full mode additionally exercises the residual generation code against its stored evidence. The nearby-candidate protocol, both refinement levels, failed stages, arithmetic controls and structural fallback are retained. Complete regeneration and independent evidence reading are distinguished. Software dependencies needed for the scientific computation are declared; personal host configuration and elapsed measurements are excluded.

The separate technical appendix holds full price rows, exact large fractions, menu traces and older stage details. The classical original-chain extension has separate claims and has not become a full annual monetary price certificate. These files are linked from the same formal entry, rather than expanded into the main contribution list.

Finite-history propagation explains the main reduction under unchanged residuals. Shared Fourier structure then changes a matched quarter-point certification decision. This combination is useful for an audit of a fixed output and for several directions reusing one parameter-and-maturity certificate. It remains necessary to compare direct reference output when replacement is permitted and to include all certification work. The nearby-grid and output-control results test these uses within explicit limits.


## Appendix A. Verification of the Probability-Model and Strip-Transform Assumptions

The primary source is Abi Jaber–El Euch, arXiv:1803.00477v1, first posted on 2018-03-01, with a PDF title-page date of March 2, 2018. The journal article appeared in 2019 in Statistics & Probability Letters 149, 63–72. Locators refer to the internal pagination of the 13-page preprint: Theorem 2.1 and Example 2.2 on p.4, Theorem 2.3 on p.5, and H2 and Table 1 on pp.9–10. These are preprint, not journal, page numbers.

For \(K_\alpha=t^{\alpha-1}/\Gamma(\alpha)\),
\[
\int_0^hK_\alpha^2dt=
\frac{h^{2\alpha-1}}{(2\alpha-1)\Gamma(\alpha)^2},\quad
\int_0^T(K_\alpha(t+h)-K_\alpha(t))^2dt
\le\frac{h^{2\alpha-1}}{\Gamma(\alpha)^2}
\int_0^\infty[(r+1)^{\alpha-1}-r^{\alpha-1}]^2dr.
\tag{A.1}
\]
The exponent in the latter integral is \(2\alpha-2>-1\) at zero and \(2\alpha-4<-1\) at infinity, so the integral is finite. The resolvent of the first kind,
\[
\mathcal L_\alpha(dt)=t^{-\alpha}dt/\Gamma(1-\alpha),\quad
K_\alpha*\mathcal L_\alpha=1
\tag{A.2}
\]
is verified by the Beta identity and is nonnegative and nonincreasing. The completely monotone spectral measure
\[
\mu_\alpha(dx)=x^{-\alpha}dx/
[\Gamma(\alpha)\Gamma(1-\alpha)]
\tag{A.3}
\]
gives \(K_\alpha(t)=\int e^{-xt}\mu_\alpha(dx)\). Under \(r=xh\), the two spectral integrals in H2 become constants times \(h^{\alpha-1}\) and \(h^{\alpha-1/2}\), respectively. The remaining constants
\(\int(1\wedge r^{-1/2})r^{-\alpha}dr\) and
\(\int r^{-\alpha-1/2}(1\wedge r)dr\) are finite for \(.5<\alpha<1\). Table 1 of the source therefore covers the required shifted-kernel conditions.

Curve (2.4) is nondecreasing, has a nonnegative initial value, and is locally Hölder with exponent \(\alpha_0=.5286\). On \(\alpha\in[.52,.9]\), the kernel has \(\gamma/2=\alpha-.5\le.4<\alpha_0\). Hence the curve-class assumptions in Example 2.2(i) hold, and Theorem 2.1 gives a nonnegative continuous weak variance solution and moment bounds. The equivalent kernel input is
\[
b_\alpha(t)=D_C^\alpha\xi_*(t)=I^{1-\alpha}\xi_*'(t)\ge0,\quad
b_\alpha(t)=
\frac{(\theta-V_0)\lambda_\xi}{\Gamma(1+\alpha_0-\alpha)}
t^{\alpha_0-\alpha}+O(t^{2\alpha_0-\alpha})
\tag{A.4}
\]
Its worst exponent is \(-.3714>-.5\), so it belongs to \(L^2_{\rm loc}\); also \(\xi_*=V_0+K_\alpha*b_\alpha\). The nonnegative input measure meets Example 2.2(ii). This verifies the model specification with a varying kernel and fixed forward variance curve.

Theorem 2.3 of the source requires \(\operatorname{Re}\psi_1\in[0,1]\), a second-state initial transform with nonpositive real part, and a variance forcing term with nonpositive real part. Taking \(\psi_1=ia=1/2+iu\) and zero for the other initial and forcing terms gives (2.2), (2.6), and uniqueness in weak law. With \(\psi_1=1\), the Riccati solution is zero and \(\mathbb E S_T=S_0\) follows. A positive local martingale with constant expectation is a true martingale. Thus the probability strip in (4.13) follows from the continuous-time model. This argument applies established existence and affine-transform theory.

## Appendix B. The Exact Finite Certificate for Theorem 6.1

The certificate domain is \(\mathcal B=[13/25,3/5]\times[0,1]\). Every interval \(I=[\ell/2^{100},r/2^{100}]\) uses integer outward rounding. Rational inputs are rounded down and up; products take extrema over the four endpoint corners and are quantised. Reciprocals first exclude zero. Square roots use integer isqrt and an increment for the upper endpoint. Complex quantities use rectangular real–imaginary interval arithmetic. The analytic lower bounds in (6.10) fix the principal-root and reciprocal branches; no floating-point sign tolerance is used.

The four basic \(\alpha\)-dependent functions \(p,v,m_\alpha,\zeta\) satisfy
\[
p'<0,\quad v'>0,\quad
(\log m_\alpha)'=2[\psi(1+2\alpha)-\psi(1+\alpha)]>0,
\]
\[
(\log\zeta)'=2[\psi(1+2\alpha)-\psi(1+3\alpha)]
 +[\psi(1+\alpha)-\psi(1+3\alpha)]<0.
\tag{B.1}
\]
We have \(\psi'(x)=\sum_{n\ge0}(x+n)^{-2}>0\), and elementary trigonometric identities give the derivatives of \(p,v\). Strict endpoint values therefore enclose each continuous \(\alpha\) interval, without sampling \(\alpha\) at grid points.

The constant \(\pi\) is certified by Machin's identity and one hundred terms of each alternating arctangent series. The logarithm is reduced to \([1,2]\) and evaluated with one hundred positive atanh-series terms and a geometric tail. The exponential is reduced to \([0,1]\), evaluated with one hundred Taylor terms and a geometric tail, and restored by repeated rigorous squaring. For positive real Gamma arguments, recurrence first shifts to \(z\ge20\). Retaining \(B_2,\ldots,B_{20}\) in log Gamma gives the positive-real remainder bound
\[
0<R_{10}(z)<B_{22}/(22\cdot21z^{21}).
\tag{B.2}
\]
In Binet's positive integral, the ten-term geometric remainder of arctangent is positive and bounded by the first omitted power. Integration gives (B.2), consistent with the positive-real Stirling remainder in NIST2010. After exponentiation, divide successively by the recurrence factors. Sine and cosine retain thirty-two terms, with absolute Lagrange tails \(M^{65}/65!,M^{64}/64!\). Bernoulli numbers, factorials, and interval endpoints are exact rationals.

For each closed rectangle, substitute these enclosures successively into (6.10), (6.5), (6.6), (6.12), and (6.15). Accept only when the lower endpoints of all three \(\bar B_j\) are strictly positive and the upper endpoints of all six \(\bar D_n\) are strictly negative. Otherwise bisect one coordinate at its exact rational midpoint. The two closed children have the parent rectangle as their union, and strict enclosures also cover the shared boundary.

The finite covering contains 211241 leaf rectangles of total rational area exactly \(2/25\). An independent check reconstructs 422481 binary-tree nodes from the root, with maximum depth 19 and each recorded leaf occurring exactly once. In addition to the area check, this excludes missing subtrees, interior overlap, and endpoint gaps. The theorem uses the order interval covered by this complete closed tree.

The stronger rational margins in the complete certificate imply the following bounds. Each simplification has been independently checked using Fraction.

| Quantity on the full compactified domain | Strict lower bound |
|---|---:|
| \(\bar B_1,\bar B_2,\bar B_3\) | \(1/6000,\ 1/8000,\ 1/20000000000\) |
| \(-\bar D_1,-\bar D_2,-\bar D_3\) | \(1/30000,\ 1/2000000000,\ 1/6000\) |
| \(-\bar D_4,-\bar D_5,-\bar D_6\) | \(1/8000,\ 1/15000000,\ 1/100000\) |
| \(|\bar\Delta|^2\) | \(1/14400\) |

The proof consists of rigorous interval inclusion and a complete finite covering. The supplementary material provides the interval implementation, all leaf rectangles, and the tree-structure check for independent verification.

## Appendix C. The complementary global exponent bound

For (2.4), \(\xi_*\in AC\), \(\xi_*'\ge0\), and \(V_0\le\xi_*\le\theta\). Positivity of the scalar resolvent follows from the negative-minimum principle in (3.3), or from the completely monotone representation of Simon [SimonCM2015]. Define
\[
A_\alpha(t)=(I^{1-\alpha}\xi_*)(t),\quad
q_\alpha(t)=A_\alpha'(t)
=\frac{V_0t^{-\alpha}}{\Gamma(1-\alpha)}+I^{1-\alpha}\xi_*'(t)\ge0.
\tag{C.1}
\]
Both initial exponents \(-\alpha,\alpha_0-\alpha\) exceed \(-1\), so \(q_\alpha\in L^1(0,T)\). Explicitly,
\[
q_\alpha(t)=\frac{V_0t^{-\alpha}}{\Gamma(1-\alpha)}
 +(\theta-V_0)\lambda_\xi t^{\alpha_0-\alpha}
 E_{\alpha_0,1+\alpha_0-\alpha}(-\lambda_\xi t^{\alpha_0}),
\tag{C.2}
\]
\[
A_\alpha(t)=\frac{\theta t^{1-\alpha}}{\Gamma(2-\alpha)}
 +(V_0-\theta)t^{1-\alpha}
 E_{\alpha_0,2-\alpha}(-\lambda_\xi t^{\alpha_0}),\quad A_\alpha(0)=0.
\tag{C.3}
\]
where \(E_{a,b}(z)=\sum_{n=0}^\infty z^n/\Gamma(an+b)\).

**Theorem C.1.** For a zero-initial-value AC trajectory \(Z,\widehat Z\), use the derivative-based exponent
\[
L_T=\nu^{-1}\int_0^T\xi_*(T-t)D_t^\alpha Z(t)\,dt,\quad
\bar L_T=\nu^{-1}\int_0^T\xi_*(T-t)D_t^\alpha\widehat Z(t)\,dt,
\]
Then
\[
L_T-\bar L_T=\nu^{-1}\int_0^Tq_\alpha(T-t)(Z-\widehat Z)(t)\,dt.
\tag{C.4}
\]
In particular, if \(\sup|Z-\widehat Z|\le E\), then
\[
|L_T-\bar L_T|\le\eta=E A_\alpha(T)/\nu
\le\frac{E\theta T^{1-\alpha}}{\nu\Gamma(2-\alpha)}.
\tag{C.5}
\]

**Proof.** Since \(D_t^\alpha v=I^{1-\alpha}v'\), absolute Fubini changes the exponent integral into
\(\nu^{-1}\int_0^TA_\alpha(T-t)v'(t)\,dt\).
Integration by parts, using \(A_\alpha(0)=v(0)=0\), yields the positive-kernel representation. Absolute Fubini is justified by \(v'\in L^1\) and the continuous, finite curve. Then \(q_\alpha\ge0\) and \(\int q_\alpha=A_\alpha(T)\) give the estimate. ∎

If \(\widehat Z=I^\alpha\bar G\), then \(\bar L=\nu^{-1}\int\xi_*\bar G\) is exactly this derivative-based exponent, so the residual integral is not added again. The substitution-based exponent formed from \(\int\xi_*F(\widehat Z)\) differs by \(\nu^{-1}\int\xi_*r_t\) and requires a separate conversion. All numerical exponent quantities used here are derivative-based.

Using \(\operatorname{Re}L_T\le0\) and the integral identity for the exponential, whenever (C.5) holds,
\[
|e^{L_T}-e^{\bar L_T}|
\le\min\{1,e^{\operatorname{Re}\bar L_T}\}(e^\eta-1).
\tag{C.6}
\]
The first estimate is based at the exact exponent; the second is based at the approximate exponent. Their minimum is a valid bound. The state error may increase with frequency, while decay of the approximate transform under the pricing weight can compensate for part of that increase.

If a model-transform envelope \(B(u)\) and an approximate-modulus bound \(\widehat B(u)\) are also available, then
\[
|e^{L_T}-e^{\bar L_T}|
\le\min\{B+\widehat B,\ \eta(B+\widehat B)/2\}.
\tag{C.7}
\]
The first bound is the triangle inequality. The second follows from
\((L_T-\bar L_T)\int_0^1e^{(1-\tau)\bar L_T+\tau L_T}d\tau\)
and the convexity bound \(e^{(1-\tau)a+\tau b}\le(1-\tau)e^a+\tau e^b\). It can be combined with (C.6) by taking the minimum, or compared with the error bound \(B(u)\) obtained by explicitly setting the node approximation to zero. The calculation uses the smallest of the applicable bounds.

## References

1. **GR2019.** Gatheral, Jim and Radoičić, Radoš. *Rational Approximation of the Rough Heston Solution*. International Journal of Theoretical and Applied Finance 22(3), 1950010, 2019. DOI [10.1142/S0219024919500109](https://doi.org/10.1142/S0219024919500109). The SSRN manuscript dated January 29, 2019 is used.

2. **GR2023v1.** Gatheral, Jim and Radoičić, Radoš. *A Generalization of the Rational Rough Heston Approximation*. Quantitative Finance 24(2), 329–335, 2024. DOI [10.1080/14697688.2024.2302055](https://doi.org/10.1080/14697688.2024.2302055). [Source](https://arxiv.org/abs/2310.09181v1). Version used: arXiv:2310.09181v1.

3. **JK2020.** Siow Woon Jeng and Adem Kiliçman. *Series Expansion and Fourth-Order Global Padé Approximation for a Rough Heston Solution*. Mathematics 8(11), 1968, 2020. DOI [10.3390/math8111968](https://doi.org/10.3390/math8111968).

4. **JK2021.** Siow Woon Jeng and Adem Kiliçman. *SPX Calibration of Option Approximations under Rough Heston Model*. Mathematics 9(21), 2675, 2021. DOI [10.3390/math9212675](https://doi.org/10.3390/math9212675).

5. **AbiJaberElEuch2018v1.** Abi Jaber, Eduardo and El Euch, Omar. *Markovian structure of the Volterra Heston model*. Statistics & Probability Letters 149, 63–72, 2019. DOI [10.1016/j.spl.2019.01.024](https://doi.org/10.1016/j.spl.2019.01.024). Version used: arXiv:1803.00477v1.

6. **LiLiu2018.** Li, Lei and Liu, Jian-Guo. *A Generalized Definition of Caputo Derivatives and Its Application to Fractional ODEs*. SIAM Journal on Mathematical Analysis 50(3), 2867–2900, 2018. DOI [10.1137/17M1160318](https://doi.org/10.1137/17M1160318). The convexity result is Proposition 3.11.

7. **Simon2014.** Simon, Thomas. *Comparing Fréchet and positive stable laws*. 2014. [Source](https://arxiv.org/abs/1310.1888v2). Version used: arXiv:1310.1888v2.

8. **TrefethenWeideman2014.** Trefethen, Lloyd N. and Weideman, J. A. C. *The Exponentially Convergent Trapezoidal Rule*. SIAM Review 56(3), 385–458, 2014. DOI [10.1137/130932132](https://doi.org/10.1137/130932132). Strip quadrature is covered by Theorem 5.1.

9. **NIST2010.** Olver, Frank W. J. and Lozier, Daniel W. and Boisvert, Ronald F. and Clark, Charles W. *NIST Handbook of Mathematical Functions*. Cambridge University Press, 2010. [Source](https://dlmf.nist.gov/).

10. **BBWeak2023v1.** Bayer, Christian and Breneis, Simon. *Weak Markovian Approximations of Rough Heston*. 2023. [Version record](https://arxiv.org/abs/2309.07023v1), [original PDF](https://arxiv.org/pdf/2309.07023v1). Version used: arXiv:2309.07023v1, submitted 13 September 2023. The characteristic-function and European-payoff error results are Theorems 2.2 and 2.7.

11. **BBSimulation2023v1.** Bayer, Christian and Breneis, Simon. *Efficient option pricing in the rough Heston model using weak simulation schemes*. 2023. [Version record](https://arxiv.org/abs/2310.04146v1), [original PDF](https://arxiv.org/pdf/2310.04146v1). Version used: arXiv:2310.04146v1, submitted 6 October 2023. This version reports second-order weak convergence numerically on p. 4.

12. **Kopteva2021v2.** Kopteva, Natalia. *Pointwise-in-time a posteriori error control for time-fractional parabolic equations*. Applied Mathematics Letters 123, 107515, 2022. DOI [10.1016/j.aml.2021.107515](https://doi.org/10.1016/j.aml.2021.107515). [Version record](https://arxiv.org/abs/2105.05848v2), [original PDF](https://arxiv.org/pdf/2105.05848v2). Version used: arXiv:2105.05848v2, revised 5 July 2021; first submitted 12 May 2021. The pointwise residual bound and norm inequality are Theorem 2.2 and Lemma 2.8.

13. **ElEuchRosenbaum2017v1.** El Euch, Omar and Rosenbaum, Mathieu. *Perfect hedging in rough Heston models*. arXiv:1703.05049v1, 2017. [Version](https://arxiv.org/abs/1703.05049v1). The analytical decreasing-curve example is not a new model-admissibility theorem.

14. **SimonCM2015.** Simon, Thomas. *Mittag-Leffler functions and complete monotonicity*. Integral Transforms and Special Functions 26(1), 36–50, 2015. DOI [10.1080/10652469.2014.965704](https://doi.org/10.1080/10652469.2014.965704). [Version](https://arxiv.org/abs/1312.4513v2).

15. **BL2025v1.** Boyarchenko, Svetlana; de Innocentis, Marco; and Levendorskii, Sergei. *Fast reliable pricing and calibration of the rough Heston model*. arXiv:2508.15080v1, 2025. [Version](https://arxiv.org/abs/2508.15080v1). Modified Adams is Section 3.2; Conformal Bootstrap is Section 4.10.

16. **BenHammouda2026v1.** Ben Hammouda, Chiheb; Ben Romdhane, Abderrahmene; Samet, Michael; and Tempone, Raul F. *Single- and Multilevel Quadrature with Error Control for Fourier Pricing under the Rough Heston Model*. arXiv:2609.00438v1, 2026. [Version](https://arxiv.org/abs/2609.00438v1). Practical tolerance interpretation: Section 3.2.

17. **HK2026v1.** Hager, Paul P. and Kreher, Dörte. *Expanding the rough Heston model in H*. arXiv:2606.16619v1, 2026. [Version](https://arxiv.org/abs/2606.16619v1).
