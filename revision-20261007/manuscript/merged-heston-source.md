# Certified Joint Pricing Errors in Heston Models: Residuals, Shared States, and Financial Decisions

## Abstract

We study how verifiable numerical residuals produce price-error outer sets that retain shared error structure and support spread valuation, quotation exclusion, and finite-candidate selection. For rough Heston, the fixed Gatheral--Radoicic six-condition, two-point third-order construction is nonsingular at all real frequencies, has a positive-real-part denominator at positive times, and preserves the left half-plane on \(\alpha\in[.52,.60]\), \(\rho=-.7445\), with zero Riccati mean reversion. Complex Caputo convexity and one-sided dissipation transfer independent continuous residuals to states; a positive exponent kernel, strip quadrature, and true-tail bounds give complete price intervals. At one parameter and maturity, the same Fourier transform errors enter all strikes. Their complex disks yield a joint price set, explicitly translated to the actual fast output. For the specified classical Heston positive-part Euler chain, common original-chain variance probabilities constrain multiple residual modes. Support functions characterize directional bounds and strict tightening. Nonexact trial functions retain a signed identity with discrete defects, continuous residuals, interfaces, and terminal errors. The upstream probability objects are verified separately and meet at the price-error level. A fixed six-month, twelve-strike SPX experiment certifies the unique finite winner \(\alpha=.52\) among \(.52,.60,.90\). Shared-node spread bounds are compared with signed marginal bounds using the complete budget. Each conclusion retains its model, parameter, trajectory, and output assumptions.

**Keywords:** Heston; rough volatility; continuous residual; common states; joint pricing error; outward arithmetic; finite candidates.

## 1. Introduction

Portfolio valuation and calibration concern simultaneous relationships among prices. Valid individual error intervals need not allow their extreme errors to occur in the same direction. Our central question is whether independently verifiable residuals can produce a set containing the actual error vector, retain constraints arising from shared objects, and yield the directional bounds required by a financial decision.

Rough Heston supplies a continuous-residual route: algebraic structure of a fixed approximation, dissipativity of a complex fractional equation, and complete Fourier error analysis establish price inclusion. Classical Heston supplies a discrete-defect route: modes under one original chain share state probabilities, constraining simultaneous residuals. These routes enter one price-error framework while preserving their respective probability laws, signs, and remainders.

Write \(c^*\) for model prices, \(c^{\rm fast}\) for the actual frozen output, and \(\bar c\) for a reference value. Implementation validation concerns \(c^*-c^{\rm fast}\). Rough Heston uses the shared transform errors in \(c^*-\bar c\) and the shift \(\bar c-c^{\rm fast}\). The classical telescoping identity is written as \(p_Q-p_P\), so model-minus-algorithm error requires sign reversal. Original-chain probabilities and continuous-process occupation probabilities are treated separately.

### 1.1. Related work

Gatheral--Radoicic [GR2019, GR2023v1] introduced the two-end rational approximation and its mean-reversion extension. Jeng--Kilicman [JK2020, JK2021] studied global Pade and public SPX data. We analyse the existing third-order construction; continuous-domain sign verification of its raw determinant and Cramer numerators provides the structural result. The formula and endpoint matching are established methods.

Abi Jaber--El Euch [AbiJaberElEuch2018v1] supply the Volterra probability model and affine transform. Caputo history convexity [LiLiu2018], Mittag--Leffler positivity [Simon2014], and strip trapezoidal error theory [TrefethenWeideman2014] supply the analytical tools. Their use here requires the specified complex real-part dissipation, an independent continuous residual for a fixed reference function, and a complete budget for the stated output.

Classical Heston, Euler weak error, and exponential integrability have established treatments [Heston1993, CozmaReisinger2016, MickelNeuenkirch2022v2]. Moment information and convex optimization also have financial-bound precedents [BertsimasPopescu2002, BoydVandenberghe2004]. We construct a residual-vector outer inclusion using common original-chain probabilities and characterize complete-row maximizer and phase conditions. Support-function and convexity algebra remain attributed tools.

The author's preceding Asian valuation manuscript [OuyangAsian2024] certifies implementation error for a specified arithmetic Asian problem. It provides contract and transform background; its Gaussian-smoothing objects and transform catalog are not identified with the thirteen-dimensional trial-field basis.

Bayer and Breneis bound the characteristic-function and European-payoff weak errors of Markovian kernel approximations through the kernel L1 error [BBWeak2023v1]. Their subsequent low-dimensional simulation construction reports second-order weak convergence numerically [BBSimulation2023v1]. Our object is a fixed six-condition rational implementation: raw matching signs establish its structure on the stated domain, an independently enclosed continuous-time residual certifies a reference trajectory, and shared Fourier perturbations propagate the certificate to several strikes and the frozen output. The approximation objects differ, so performance comparisons require a common model contract.

Caputo convexity and pointwise residual comparison have established foundations [LiLiu2018, Kopteva2021v2]. We apply them to the dissipative divided difference of the complex Riccati equation and verify the hypotheses for the specified reference field. Support-function operations are likewise standard [BoydVandenberghe2004]. The model-specific conclusions concern the shared error variables in the complete pricing implementation and their certified effect on a portfolio direction and finite-candidate objectives.


### 1.2. Contributions and evidence

| Object | Retained or added result | Evidence and financial role |
|---|---|---|
| Existing third-order construction | Full-frequency structure on a stated continuous domain | Raw polynomials, complete leaf cover, and recomputable signs; well-definedness |
| Independent reference function | Complex residual-to-state, exponent, and complete price bounds | Fixed coefficients, continuous envelopes, quadrature and true tails |
| Multi-strike output at one parameter | Shared Fourier disks, centre translation, complete directional bounds | Original node radii and exact spread comparison |
| Classical positive-part chain | Common-state inclusion and strictness | Original-Q moments, 102 bands, 22 rows, exact witnesses |
| Nonexact trial functions | Four-contribution signed identity and explicit admissible example | Actual traces, terminal value, integrable weights and full-year envelopes |
| Fixed parameter profile | Strict three-candidate ranking and quote exclusion | Thirty-six price rows, objective intervals, and actual frozen output |

Sections 2--8 give the complete rough-model proofs and fixed candidate example. Section 9 constructs the joint multi-strike error at the actual output. Section 10 supplies the classical common-state implementation. Section 11 presents financial decisions and the complete spread comparison. Section 12 specifies evidence and costs, and Section 13 states applicability. Appendices retain the model, structure-certificate, and original-chain inclusion proofs.


## 2. Mathematical Setting and the Established Six-Condition Third-Order Construction

### 2.1. Variance model, time scales, and price definition

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

### 2.2. The established six-condition [3/3] approximation

Set \(S=s_0-i\rho u=-d\), take the principal square root in \(A=\sqrt{S^2+2b}\), and let \(R=A-S\). The three short-time and long-time coefficients are respectively
\[
b_1=-\frac b{\Gamma(1+\alpha)},\quad
b_2=\frac{Sb}{\Gamma(1+2\alpha)},\quad
b_3=\frac{\Gamma(1+2\alpha)}{\Gamma(1+3\alpha)}
       (d b_2+b_1^2/2),
\tag{2.8}
\]
\[
g_0=-R,\quad g_1=\frac R{A\Gamma(1-\alpha)},\quad
g_2=-\frac R{A^2\Gamma(1-2\alpha)}
       +\frac{R^2}{2A^3\Gamma(1-\alpha)^2}.
\tag{2.9}
\]
For \(1/2<\alpha<1\), \(\Gamma(1-2\alpha)\) is finite and negative. The fixed two-endpoint construction of Gatheral and Radoičić [GR2019] requires
\[
\widehat H(y)=P(y)/Q(y),\quad
Q=1+q_1y+q_2y^2+q_3y^3,
\]
\[
\widehat H=b_1y+b_2y^2+b_3y^3+O(y^4),\quad
\widehat H=g_0+g_1y^{-1}+g_2y^{-2}+O(y^{-3}).
\tag{2.10}
\]
These six conditions give the linear system
\[
\begin{pmatrix}g_0&g_1&g_2\\b_1&-g_0&-g_1\\
b_2&b_1&-g_0\end{pmatrix}
\begin{pmatrix}q_1\\q_2\\q_3\end{pmatrix}
=\begin{pmatrix}b_1\\-b_2\\-b_3\end{pmatrix},
\quad p_1=b_1,\quad p_2=b_2+b_1q_1,\quad p_3=g_0q_3.
\tag{2.11}
\]
Equations (2.8)–(2.11) are the established construction. We next prove invertibility, a nonvanishing denominator, the trajectory half-plane property, and exact-solution error bounds for an independent reference trajectory.

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
\tag{2.12}
\]
The reflection formula and recurrence relations give \(b_1=-fb,b_2=f^2\mathsf d,b_3=f^3\mathsf c\) and \(g_1=V/f,g_2=W/f^2\). In the latter two expressions, the factors \(f,f^2\) occur in the denominators. Direct expansion of the determinant and Cramer numerators of (2.11) gives
\[
\begin{aligned}
\Delta={}&b^2W+2bRV-\mathsf dRW-\mathsf dV^2-R^3,\\
F_1={}&b^2V+b\mathsf dW-bR^2+\mathsf dRV+\mathsf cRW+\mathsf cV^2,\\
F_2={}&-b^2R+b\mathsf dV+b\mathsf cW+\mathsf d^2W+\mathsf dR^2+\mathsf cRV,\\
F_3={}&-b^3+2b\mathsf dR-b\mathsf cV-\mathsf d^2V+\mathsf cR^2.
\end{aligned}
\tag{2.13}
\]
Here \(\Delta\) is exactly the determinant of the original system, and the numerators are \(N_j=f^jF_j\). After establishing \(\Delta\ne0\), we may define \(q_j=N_j/\Delta\), in which case
\[
\Delta P=-fb\Delta y+f^2(\mathsf d\Delta-bF_1)y^2-f^3RF_3y^3,\quad
\Delta Q=\Delta+fF_1y+f^2F_2y^2+f^3F_3y^3.
\tag{2.14}
\]
In physical time, the denominator coefficients are \(\nu^jq_j\); the normalised coefficients \(q_j\) retain their original definition.

## 3. A Full-Frequency Structural Theorem for the Fixed Third-Order Construction

**Theorem 3.1 (full-frequency structure).** For
\[
\alpha\in[13/25,3/5],\quad \rho=-1489/2000,\quad \kappa=0,\quad
u\in\mathbb R,\quad \nu>0,
\tag{3.1}
\]
the established matching system (2.11) is nonsingular. Its normalised denominator satisfies
\[
\operatorname{Re}q_j>0\ (j=1,2,3),\qquad
\operatorname{Re}Q(y)\ge1,\quad |Q(y)|\ge1\quad(y\ge0).
\tag{3.2}
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
\tag{3.3}
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
Equation (3.3) expresses \(\bar A-\bar S\) in reciprocal form, with a denominator determined directly by the current parameters.

Substitute \(\bar b=1/2\) and (3.3) into (2.12)–(2.13) to obtain the barred original quantities. Homogeneity gives
\[
\Delta=\omega^3\bar\Delta,\qquad F_j=\omega^{3+j}\bar F_j.
\tag{3.4}
\]
Define three real functions
\[
\bar B_j=\operatorname{Re}(\bar F_j\overline{\bar\Delta}).
\tag{3.5}
\]
The rigorous rational covering in Appendix B proves that, throughout the closed rectangle \([13/25,3/5]\times[0,1]\), \(\bar B_j>0\) and
\[
|\bar\Delta|^2\ge
\frac{88110801209184778874628745}{1267650600228229401496703205376}
>\frac1{14400}.
\tag{3.6}
\]
This first establishes \(\Delta\ne0\) and then yields
\(\operatorname{Re}q_j=(f\omega)^j\bar B_j/|\bar\Delta|^2>0\), proving (3.2).

For the trajectory half-plane, the finite convolution in (2.14) gives
\[
|\Delta|^2\operatorname{Re}(P\overline Q)
=\sum_{n=1}^6 f^nD_ny^n,
\tag{3.7}
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
\tag{3.8}
\]
The same rational covering certifies the six compactified quantities \(\bar D_n<0\), with scaling \(D_n=\omega^{7+n}\bar D_n\). Set \(z=f\omega y\). The right-hand side of (3.7) is
\(\omega^7\sum_{n=1}^6\bar D_nz^n\) and is therefore strictly negative for every \(y>0\). Having proved that the denominator is nonzero, division by \(|Q|^2|\Delta|^2\) gives \(\operatorname{Re}\widehat H<0\). Negative frequencies follow by conjugate symmetry of the principal root and matching coefficients. The closed endpoint \(\eta=1\) represents the infinite-frequency limit, so the proof on the closed compactified domain covers every finite frequency. ∎

Positive real parts of the coefficients provide a sufficient condition for a nonvanishing denominator. Appendix B specifies the algebraic identities, elementary-function remainder bounds, and continuous interval covering used in the computer-assisted proof.

## 4. Complex Dissipation and Independent Residual Error Bounds

### 4.1. Regularity, the history formula, and convexity

If \(H=I^\alpha F(H)\) is a bounded local continuous solution, then \(H,F(H)\) are \(\alpha\)-Hölder continuous. For \(\alpha>1/2\), write \(q=F(H)\). Cancellation gives the derivative formula
\[
H'(x)=\frac{q(x)x^{\alpha-1}}{\Gamma(\alpha)}
 +\frac{\alpha-1}{\Gamma(\alpha)}
\int_0^x(x-t)^{\alpha-2}[q(t)-q(x)]\,dt.
\tag{4.1}
\]
The near-endpoint exponent satisfies \(2\alpha-2>-1\); the other endpoint and the first term are integrable. Thus \(H\in AC\) and it is locally \(C^1\) at positive times. Local existence follows from Volterra contraction on a bounded ball. For \(v\in AC\) that is locally Lipschitz at positive times, integration by parts gives
\[
D_C^\alpha v(x)=\frac1{\Gamma(1-\alpha)}
\left\{\frac{v(x)-v(0)}{x^\alpha}
 +\alpha\int_0^x\frac{v(x)-v(t)}{(x-t)^{1+\alpha}}\,dt\right\}.
\tag{4.2}
\]
At a positive maximum over the full history, with zero initial value, this derivative is strictly positive. Consequently, \(D_C^\alpha v+s v\le D_C^\alpha w+s w\), \(v(0)=w(0)\), and \(s\ge0\) imply \(v\le w\). For a convex \(C^1\) function \(\Phi\) on the real plane, apply the supporting-hyperplane inequality to both terms in (4.2) to obtain
\[
D_C^\alpha\Phi(v)\le\nabla\Phi(v)\cdot D_C^\alpha v.
\tag{4.3}
\]
This is the established Caputo history-convexity inequality, rather than an ordinary chain rule. We work within the regularity assumptions of Proposition 3.11 of Li and Liu [LiLiu2018] and directly prove the version needed here.

### 4.2. The global half-plane property of the exact solution

**Lemma 4.1.** Suppose \(\alpha\in(1/2,1),|\rho|\le1,s_0\ge0\). The normalised equation has a unique global solution, and \(\operatorname{Re}H(x)<0\) for \(x>0\). If \(s_0>0\), then
\[
|H(x)|\le\frac b{s_0}[1-E_\alpha(-s_0x^\alpha)]
\le\min\{b/s_0,bx^\alpha/\Gamma(1+\alpha)\}.
\tag{4.4}
\]
When \(s_0=0\), the latter time-dependent bound remains valid.

**Proof.** Write \(H=X+iY\). Completing the square gives
\[
\operatorname{Re}F(H)
=-\frac18-\frac{1-\rho^2}{2}u^2
-\frac12(Y+\rho u)^2-s_0X+\frac12X^2.
\tag{4.5}
\]
If \(X\) first reaches a small positive level \(\varepsilon<1/2\), the derivative in (4.2) is positive, whereas (4.5) is negative, a contradiction. Thus \(X\le0\). Reaching zero at a positive time gives the same contradiction, proving strict negativity.

Let \(\psi_\epsilon(z)=\sqrt{|z|^2+\epsilon^2}-\epsilon\). Equation (4.3), together with
\[
\operatorname{Re}(\overline H F(H))
=-bX-s_0|H|^2+\tfrac12X|H|^2,\quad
\frac{|H|^2}{\sqrt{|H|^2+\epsilon^2}}\ge\psi_\epsilon(H),
\]
gives \(D_C^\alpha\psi_\epsilon(H)+s_0\psi_\epsilon(H)\le b\). Compare with the zero-initial-value linear scalar equation and let \(\epsilon\downarrow0\) to obtain (4.4). The scalar solution is verified directly by the Mittag–Leffler series. If finite-time blow-up occurred, (4.4) would bound the trajectory, \(F(H)\), and a uniform Hölder constant. The history integral would have a finite limit at that endpoint, and local contraction would extend the solution, a contradiction. Successive Volterra contractions give uniqueness. ∎

### 4.3. A stability constant independent of frequency

**Theorem 4.2 (dissipative residual bound).** Suppose \(s_0>0\), \(\widehat H(0)=0\), and \(\widehat H\in AC\), with local Lipschitz regularity at positive times. Assume, for every \(x\in(0,X]\), that
\[
\operatorname{Re}\widehat H\le\epsilon_R<2s_0,\qquad
|D_C^\alpha\widehat H-F(\widehat H)|\le\delta,
\]
Set \(\sigma=s_0-\epsilon_R/2>0\). Then
\[
|H-\widehat H|
\le\frac\delta\sigma[1-E_\alpha(-\sigma x^\alpha)]
\le\delta/\sigma.
\tag{4.6}
\]
In particular, for a trajectory in the left half-plane, one may take \(\epsilon_R=0,\sigma=s_0\). No smallness assumption on \(\delta\) or \(u\) is required.

**Proof.** The error \(e=H-\widehat H\) satisfies
\[
D_C^\alpha e=\left(d+\frac{H+\widehat H}{2}\right)e-r,\quad e(0)=0,\quad
\operatorname{Re}\left(d+\frac{H+\widehat H}{2}\right)\le-\sigma.
\]
Apply (4.3) to \(\psi_\epsilon(e)\) to obtain
\(D_C^\alpha\psi_\epsilon(e)+\sigma\psi_\epsilon(e)\le|r|\le\delta\).
Comparison with the linear scalar solution, followed by \(\epsilon\downarrow0\), proves the claim. Convex regularisation includes points of zero error and applies to the complex error viewed as a vector in the real plane. ∎

If \(\widehat H\) corresponds to the physical-time trajectory \(\widehat Z\) and \(|r_t|/\nu\le\delta_F\) has been certified, the same result gives
\[
\sup_{t\le T}|Z-\widehat Z|\le\delta_F/s_0
\quad\text{if }\operatorname{Re}\widehat Z\le0.
\tag{4.7}
\]
In the numerical example, \(s_0=1489/4000\). This dissipation rate controls the complex error modulus; Section 7 supplies the independent residual \(\delta_F\). The estimate applies the established convexity tool to the specific error propagation considered here.

**Proposition 4.3 (an error radius without an assumed approximate half-plane).** If \(\delta_F<s_0^2/2\), every admissible trajectory with the same initial value satisfies
\[
|Z-\widehat Z|\le E_\delta
=s_0-\sqrt{s_0^2-2\delta_F}
=\frac{2\delta_F}{s_0+\sqrt{s_0^2-2\delta_F}}.
\tag{4.8}
\]
To prove this, rewrite the error terms as \((d+Z)e-e^2/2\). The exact-solution half-plane gives
\(D_t^\alpha|e|\le\nu(-s_0|e|+|e|^2/2+\delta_F)\), interpreted through the same convex regularisation of the modulus. Choose any \(E_\delta<\ell<s_0+\sqrt{s_0^2-2\delta_F}\). The right-hand side is strictly negative at \(|e|=\ell\); a first hitting time of \(\ell\) contradicts (4.2). Letting \(\ell\downarrow E_\delta\) proves the result. This is a sufficient small-residual condition; violating it does not establish an actual error or pole. The completed node trajectories in this example have a certified half-plane property and use (4.7), which does not impose the threshold in (4.8).

## 5. Positive-Kernel Error Propagation for the Derivative-Based Characteristic Exponent

For (2.4), \(\xi_*\in AC\), \(\xi_*'\ge0\), and \(V_0\le\xi_*\le\theta\). Positivity of the scalar resolvent follows from the negative-minimum principle in (4.2), or from the completely monotone representation of Simon [Simon2014]. Define
\[
A_\alpha(t)=(I^{1-\alpha}\xi_*)(t),\quad
q_\alpha(t)=A_\alpha'(t)
=\frac{V_0t^{-\alpha}}{\Gamma(1-\alpha)}+I^{1-\alpha}\xi_*'(t)\ge0.
\tag{5.1}
\]
Both initial exponents \(-\alpha,\alpha_0-\alpha\) exceed \(-1\), so \(q_\alpha\in L^1(0,T)\). Explicitly,
\[
q_\alpha(t)=\frac{V_0t^{-\alpha}}{\Gamma(1-\alpha)}
 +(\theta-V_0)\lambda_\xi t^{\alpha_0-\alpha}
 E_{\alpha_0,1+\alpha_0-\alpha}(-\lambda_\xi t^{\alpha_0}),
\tag{5.2}
\]
\[
A_\alpha(t)=\frac{\theta t^{1-\alpha}}{\Gamma(2-\alpha)}
 +(V_0-\theta)t^{1-\alpha}
 E_{\alpha_0,2-\alpha}(-\lambda_\xi t^{\alpha_0}),\quad A_\alpha(0)=0.
\tag{5.3}
\]
where \(E_{a,b}(z)=\sum_{n=0}^\infty z^n/\Gamma(an+b)\).

**Theorem 5.1.** For a zero-initial-value AC trajectory \(Z,\widehat Z\), use the derivative-based exponent
\[
L_T=\nu^{-1}\int_0^T\xi_*(T-t)D_t^\alpha Z(t)\,dt,\quad
\bar L_T=\nu^{-1}\int_0^T\xi_*(T-t)D_t^\alpha\widehat Z(t)\,dt,
\]
Then
\[
L_T-\bar L_T=\nu^{-1}\int_0^Tq_\alpha(T-t)(Z-\widehat Z)(t)\,dt.
\tag{5.4}
\]
In particular, if \(\sup|Z-\widehat Z|\le E\), then
\[
|L_T-\bar L_T|\le\eta=E A_\alpha(T)/\nu
\le\frac{E\theta T^{1-\alpha}}{\nu\Gamma(2-\alpha)}.
\tag{5.5}
\]

**Proof.** Since \(D_t^\alpha v=I^{1-\alpha}v'\), absolute Fubini changes the exponent integral into
\(\nu^{-1}\int_0^TA_\alpha(T-t)v'(t)\,dt\).
Integration by parts, using \(A_\alpha(0)=v(0)=0\), yields the positive-kernel representation. Absolute Fubini is justified by \(v'\in L^1\) and the continuous, finite curve. Then \(q_\alpha\ge0\) and \(\int q_\alpha=A_\alpha(T)\) give the estimate. ∎

If \(\widehat Z=I^\alpha\bar G\), then \(\bar L=\nu^{-1}\int\xi_*\bar G\) is exactly this derivative-based exponent, so the residual integral is not added again. The substitution-based exponent formed from \(\int\xi_*F(\widehat Z)\) differs by \(\nu^{-1}\int\xi_*r_t\) and requires a separate conversion. All numerical exponent quantities used here are derivative-based.

Using \(\operatorname{Re}L_T\le0\) and the integral identity for the exponential, whenever (5.5) holds,
\[
|e^{L_T}-e^{\bar L_T}|
\le\min\{1,e^{\operatorname{Re}\bar L_T}\}(e^\eta-1).
\tag{5.6}
\]
The first estimate is based at the exact exponent; the second is based at the approximate exponent. Their minimum is a valid bound. The state error may increase with frequency, while decay of the approximate transform under the pricing weight can compensate for part of that increase.

If a model-transform envelope \(B(u)\) and an approximate-modulus bound \(\widehat B(u)\) are also available, then
\[
|e^{L_T}-e^{\bar L_T}|
\le\min\{B+\widehat B,\ \eta(B+\widehat B)/2\}.
\tag{5.7}
\]
The first bound is the triangle inequality. The second follows from
\((L_T-\bar L_T)\int_0^1e^{(1-\tau)\bar L_T+\tau L_T}d\tau\)
and the convexity bound \(e^{(1-\tau)a+\tau b}\le(1-\tau)e^a+\tau e^b\). It can be combined with (5.6) by taking the minimum, or compared with the error bound \(B(u)\) obtained by explicitly setting the node approximation to zero. The calculation uses the smallest of the applicable bounds.

## 6. The Continuous Fourier Integral, the Discrete Grid, and the Infinite Tail

### 6.1. Rigorous analytic-strip discretisation

**Theorem 6.1.** Suppose \(M_T>0,\mathbb E M_T=1\). For any \(0<a_*<1/2,h_*>0\), let
\(g(z)=e^{-ikz}\phi_T(z-i/2)/(z^2+1/4)\). Replacing the integral in (2.7) by the infinite trapezoidal sum incurs a price error of at most
\[
\epsilon_{\rm grid}
=\frac{\sqrt m\,e^{a_*|k|}}
{(1/2-a_*)(e^{2\pi a_*/h_*}-1)}.
\tag{6.1}
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
Conjugate symmetry halves both the two-sided integral and its sum. Multiplication by \(\sqrt m/\pi\) gives (6.1). ∎

This is a specific application of the analytic-strip trapezoidal theory of Trefethen and Weideman [TrefethenWeideman2014]. Each pricing node uses its own continuous-time residual bound; the analytic strip controls the quadrature error between nodes.

### 6.2. Direct high-frequency control of the exact Lewis-contour solution

Fix \(\kappa=0,-1<\rho<0\). Set \(X=-\operatorname{Re}H\ge0\). Equation (4.5) gives
\[
D_x^\alpha X\ge\beta_u-s_0X-X^2/2,\quad
\beta_u=(1-\rho^2)u^2/2+1/8.
\tag{6.2}
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
\tag{6.3}
\]
The comparison argument uses a positive maximum over the full history.

Take \(V>s_0/\sqrt{1-\rho^2}\) and define
\[
a_\rho=\sqrt{1-\rho^2},\quad b_V=a_\rho-s_0/V>0,\quad
f_\alpha(z)=z/(\Gamma(1+\alpha)+z).
\]
For \(u\ge V\), we have \(R_u/u\ge b_V,\ell_u\ge a_\rho u/2\). For any partition of \(J\ge2\), denoted \(0=t_0<\cdots<t_J=T\), the positive kernel in (5.4) and the monotonicity of \(f_\alpha\) give
\[
c_V=\frac{b_V}{\nu}\sum_{j=0}^{J-1}
 f_\alpha(a_\rho\nu Vt_j^\alpha/2)
 [A_\alpha(T-t_j)-A_\alpha(T-t_{j+1})]>0,
\]
\[
|\phi_T(u-i/2)|\le e^{-c_Vu}\quad(u\ge V).
\tag{6.4}
\]
This envelope holds at every continuous high frequency. The time partition constructs a lower sum for the positive-measure integral. The example uses \(J=64\) and rigorous intervals to obtain a positive rational lower bound for \(c_V\). No singular evaluation is performed at \(A_\alpha(0)=0\). The difference between bounds taken from the appropriate sides at distinct endpoints,
\([A_{\rm lo}(T-t_j)-A_{\rm hi}(T-t_{j+1})]_+\),
is a valid lower bound on the mass.

Using the right-endpoint sum of a positive decreasing function, for \(V=Nh_*\) the exact discrete-tail contribution to the normalised price is bounded by
\[
\epsilon_{\rm tail}
\le\frac{\sqrt m}{\pi}\frac{e^{-c_VV}}{c_VV^2}.
\tag{6.5}
\]
The integral tail uses an envelope for the exact solution. Finite nodes assigned the value zero are charged according to the same envelope, so every part of the frequency range has an explicit error contribution.

### 6.3. The complete price-error bound

Suppose the node values \(\widehat\phi_n\) have exact-error bounds \(\varepsilon_n\). The finite price sum
\[
\widehat c_N=1-\frac{h_*\sqrt m}{\pi}
\left(2\operatorname{Re}\widehat\phi_0+
\sum_{n=1}^N\frac{\operatorname{Re}(e^{-inh_*k}\widehat\phi_n)}
{(nh_*)^2+1/4}\right)
\tag{6.6}
\]
satisfies
\[
|c-\widehat c_N|\le\epsilon_{\rm grid}+\epsilon_{\rm tail}
 +\frac{h_*\sqrt m}{\pi}
\left(2\varepsilon_0+
\sum_{n=1}^N\frac{\varepsilon_n}{(nh_*)^2+1/4}\right)
 +\epsilon_{\rm arithmetic}.
\tag{6.7}
\]
The coefficient \(2\) is the product of the trapezoidal half-weight at \(u=0\) and the denominator factor \(1/4\). Rigorous intervals include rounding errors in the phase, square root, exponential, and finite summation. Here \(h_*=1/8,a_*=9/20,N=1024\). The first \(513\) nodes, \(u\le64\), use independent residual bounds; the remaining node approximations are zero, with their errors bounded by the exact-transform envelope. For \(u>128\), we use (6.5). This hybrid rule combines node errors and the tail in one price estimate.

## 7. Continuous-Time Residual Certificates for the Fixed Reference Trajectory

### 7.1. The certified trajectory and its initial interval

For each candidate \(\alpha=\beta\in\{.52,.6,.9\}\) and each \(u=n/8,\ n=0,\ldots,512\), we store
\[
\bar G(t)=\nu c_0+A_1t^\beta+A_2t^{2\beta}+\bar L(t),\quad
c_0=-(u^2+1/4)/2,\quad \widehat Z=I^\alpha\bar G,\quad T=1/2.
\tag{7.1}
\]
Here \(\bar L\) is the continuous piecewise-linear interpolation in physical time at nodes \((t_j,L_j)\), with \(L_0=0\). Nodes and complex coefficients are interpreted as the exact dyadic rationals represented by their binary64 values. The following independent residual controls the continuous-time error of this reference trajectory:
\[
r_t=\bar G-\nu F(\widehat Z),\quad
\delta_F=\nu^{-1}\sup_{0\le t\le T}|r_t|.
\tag{7.2}
\]
Equation (7.1) defines an entire absolutely continuous reference trajectory. Its independent residual gives the model-price intervals, which are then used to bound the output error of the selected [3/3] implementation.

Write
\[
\widehat Z=H_0+J,\quad J=I^\alpha\bar L,\quad
H_0=B_1t^\alpha+B_2t^{\alpha+\beta}+B_3t^{\alpha+2\beta},
\]
\[
B_1=\frac{\nu c_0}{\Gamma(1+\alpha)},\quad
B_2=\frac{A_1\Gamma(1+\beta)}{\Gamma(1+\alpha+\beta)},\quad
B_3=\frac{A_2\Gamma(1+2\beta)}{\Gamma(1+\alpha+2\beta)}.
\tag{7.3}
\]
The initial interval is \(J=L_1t^{\alpha+1}/[t_1\Gamma(2+\alpha)]\). Substitute all generalised powers into (7.2), first cancel \(\nu c_0\) exactly, combine equal powers, and then take \(\sum_p|r_p|t_1^p\). Since every \(p>0\), this bounds the full initial closed interval. The generalised-power expansion retains the fractional initial behaviour.

### 7.2. Rigorous integration and derivative bounds on subsequent intervals

On a source interval \([a,b]\subset[0,q]\), set \(\tau=q-a,h=b-a\). The integral weights for the linear hat functions are
\[
I_0=\{\tau^\alpha-(\tau-h)^\alpha\}/\alpha,\quad
I_1=\{\tau^{\alpha+1}-(\tau-h)^{\alpha+1}\}/(\alpha+1),
\]
\[
w_R=(\tau I_0-I_1)/(h\Gamma(\alpha)),\quad
w_L=I_0/\Gamma(\alpha)-w_R.
\tag{7.4}
\]
These weights are nonnegative. For a truncated interval, recover the endpoints by affine interpolation within the original interval. On the final interval, \(b=q\) can be evaluated directly using
\(w_R=h^\alpha/[\alpha(\alpha+1)\Gamma(\alpha)],w_L=\alpha w_R\).
For \(h/\tau<.01\), retain eight positive-series terms, using respectively
\[
w_R=\frac{h\tau^{\alpha-1}}{\Gamma(\alpha)}
\sum_{k\ge0}\frac{(1-\alpha)_k(h/\tau)^k}{k!(k+2)},\quad
w_L=\frac{h\tau^{\alpha-1}}{\Gamma(\alpha)}
\sum_{k\ge0}\frac{(1-\alpha)_k(h/\tau)^k}{k!(k+1)(k+2)}.
\tag{7.5}
\]
The unscaled tails are each bounded by \(z^8/(1-z)\) because \(0<(1-\alpha)_k/k!\le1\). This reduces interval inflation from subtracting nearly equal endpoint quantities while retaining rigorous history integration.

Subdivide each subsequent original interval twice into four closed subintervals \([a,b]\), with recorded dyadic centres \(m\). Given a derivative bound on the full subinterval,
\[
\sup_{[a,b]}|r_t|\le|r_t(m)|+\max(m-a,b-m)\sup_{[a,b]}|r_t'|.
\tag{7.6}
\]
The ordinary residual derivative may be discontinuous at original nodes. The derivative bounds below hold almost everywhere; absolute continuity of the residual and the fundamental theorem of calculus still imply (7.6). Each of the following three identities provides a derivative bound, and we take their minimum:
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
\tag{7.7}
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
\tag{7.8}
\]
When \(a=t_1\), discard the first upper bound. The second follows from the full Euler Beta integral and is finite. Kernel monotonicity at the endpoints gives the lower bound and the first upper bound. Every \(p,\alpha>0\), so the hypotheses of the classical Beta formula hold.

Using the same \(\widehat Z'\) enclosure and rigorous point values, certify an upper bound for \(\operatorname{Re}\widehat Z\) on every subsequent subinterval. On the initial interval, factor out \(t^\alpha\), leaving a finite bracket; use its negative constant term and the endpoint contributions of the remaining positive parts. Bound (4.7) is used only when the upper real-part bound is nonpositive on every closed interval. This condition therefore covers the entire closed time interval.

### 7.3. Arithmetic bounds and explicit floating-point assumptions

The structural certificate and special functions use outward-rounded intervals with integer endpoints divided by \(2^{100}\). Batched residual weights use IEEE binary64; each basic operation is enlarged outward to adjacent representable numbers. After converting an exact rational Gamma enclosure, endpoint inclusion is checked with Fraction. The logarithm uses exact binary scaling and a twenty-two-term atanh series with \(z\in[0,1/3]\), whose tail is \(2z^{45}/[45(1-z^2)]\). After scaling, the exponential has \(|r|<1\) and a degree-24 Taylor tail bounded by \(3/25!\). These explicit remainders define the intervals for logarithms, exponentials, and noninteger powers.

For matrix multiplication with rigorous weight centres \(W_c\), radii \(W_r\), and recorded dyadic values \(X\), include
\[
\left(\gamma_{2n}\|W_c\|_{1,\mathrm{row}}+
\|W_r\|_{1,\mathrm{row}}\right)\|X\|_{\infty,\mathrm{column}},
\quad \gamma_{2n}=\frac{2n\,2^{-53}}{1-2n\,2^{-53}},
\tag{7.9}
\]
and an additional underflow-error allowance. Induction on products of basic rounding factors gives this estimate and permits different summation association orders. Norm summations are also rounded outward. The calculation assumes round-to-nearest IEEE basic operations, correctly rounded square roots, gradual underflow, and the absence of overflow or NaNs. The supplementary material records source and computation versions. The interval-inclusion conclusions in this section are conditional on these arithmetic assumptions and the stated remainder bounds.

### 7.4. Exponent integration and effective weights for the same trajectory

For the fixed curve, define
\[
J_0(z)=\theta z+(V_0-\theta)zE_{\alpha_0,2}(-\lambda_\xi z^{\alpha_0}),\quad
J_1(z)=\theta z^2/2+
(V_0-\theta)z^2(E_{\alpha_0,2}-E_{\alpha_0,3})(-\lambda_\xi z^{\alpha_0}).
\tag{7.10}
\]
These quantities are respectively \(\int_0^z\xi_*(s)ds,\int_0^zs\xi_*(s)ds\); termwise integration verifies the second formula. If a linear-trajectory interval is \([a,b]\) with \(A=T-b,B=T-a\), its rigorous nonnegative exponent weights are
\[
w_l=\frac{J_1(B)-J_1(A)-A[J_0(B)-J_0(A)]}{b-a},\quad
w_r=\frac{B[J_0(B)-J_0(A)]-J_1(B)+J_1(A)}{b-a}.
\tag{7.11}
\]
The curve moment for the power component \(t^\beta\) is
\[
\int_0^T\xi_*(T-t)t^\beta dt
=\frac{\theta T^{\beta+1}}{\beta+1}
 +(V_0-\theta)\Gamma(\beta+1)T^{\beta+1}
 E_{\alpha_0,\beta+2}(-\lambda_\xi T^{\alpha_0}).
\tag{7.12}
\]
This follows directly from the series and Beta integration. Together with (7.1), it makes \(\bar L\) a rigorous finite sum. Trigonometric phases and complex exponentials also use finite Taylor expansions with explicit tails. On the present horizon, if \(z=\lambda_\xi T^{\alpha_0}<1\), a Mittag–Leffler series tail may be bounded by \(3z^{64}/(1-z)\): all Gamma arguments exceed one, and Euler's integral gives \(\Gamma(\gamma)\ge e^{-1}>1/3\). Rigorous integration encloses the approximate exponent, while (5.5) controls the difference between the model and approximate exponents.

## 8. Finite-Candidate Roughness Selection and Stability of the Specified Third-Order Implementation

### 8.1. Quote definitions and the finite candidate set

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

### 8.2. From model-price intervals to finite-set optimality

**Theorem 8.1 (finite-objective intervals and selection stability).** For each \(\alpha_j\in\Theta_{\rm finite}\), suppose all model prices have certified enclosures
\[
c_i(\alpha_j)\in[p^-_{ij},p^+_{ij}],\quad
B_i\in[b_i^-,b_i^+],\quad
A_i\in[a_i^-,a_i^+],\quad
M_i\in[m_i^-,m_i^+].
\tag{8.4}
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
\tag{8.5}
\]
Then \(J(\alpha_j)\in[L_j,U_j]\). Writing \(L_*=\min_jL_j,U_*=\min_jU_j\), the exact finite-set optimum satisfies
\[
J_*=\min_{\Theta_{\rm finite}}J\in[L_*,U_*].
\tag{8.6}
\]
For \(\varepsilon\ge0\), every exact \(\varepsilon\)-near-optimal candidate belongs to
\[
\{\alpha_j:L_j\le U_*+\varepsilon\};
\tag{8.7}
\]
The condition \(U_j-L_*\le\varepsilon\) is sufficient for that candidate to be near-optimal for the exact objective. If
\[
g:=\min_{j\ne j_0}L_j-U_{j_0}>0,
\tag{8.8}
\]
then \(\alpha_{j_0}\) is the unique minimiser of the model objective on the finite set. If
\[
\min_{\alpha_j\ge.6}L_j>U_*+\varepsilon,
\tag{8.9}
\]
then every exact near-optimal candidate in the finite set satisfies \(\alpha_j<.6\).

Quote consistency is checked separately. If any row satisfies \(p^+_{ij}<b_i^-\) or \(p^-_{ij}>a_i^+\), the candidate cannot lie in all quote bands simultaneously. Conversely, if every row satisfies \(p^-_{ij}\ge b_i^+\) and \(p^+_{ij}\le a_i^-\), then quote consistency is certified. Overlapping intervals without this inner-band condition retain possible consistency; overlap alone does not certify it.

**Proof.** The exact difference \(c_i-M_i\) belongs to the closed interval used in (8.5). The minimum of its square is \(\ell\) and the maximum is \(v\), so the weighted sum encloses every \(J_j\). Each \(J_j\ge L_j\ge L_*\); a candidate attaining the smallest \(U_j\) gives \(J_*\le J_j\le U_*\), proving (8.6). If \(J_j\le J_*+\varepsilon\), then \(L_j\le J_j\le U_*+\varepsilon\), proving (8.7). Conversely, \(J_j-J_*\le U_j-L_*\) gives the stated sufficient inner condition. Under (8.8), every competitor satisfies \(J_j-J_{j_0}\ge L_j-U_{j_0}\ge g>0\), proving uniqueness. Condition (8.9) places the model objective of every selected higher-H candidate above \(J_*+\varepsilon\) and therefore excludes it. No independence assumption on quote errors across candidates is needed.

If \(p^+<b^-\), then the exact price satisfies \(c<B\); if \(p^->a^+\), then \(c>A\). A single such row rules out simultaneous consistency. In the opposite direction, the inner-band conditions give \(B\le b^+\le c\le a^-\le A\). Applying these statements row by row proves the consistency assertions. ∎

**Corollary (objective perturbation).** Suppose another numerical objective \(\widetilde J\) satisfies
\(\sup_{\Theta_{\rm finite}}|\widetilde J-J|\le\delta_J\), and its selected candidate is \(\varepsilon_{\rm alg}\)-near-optimal. Then
\[
J(\widehat\alpha)-J_*
\le2\delta_J+\varepsilon_{\rm alg}.
\tag{8.10}
\]
Indeed, \(J(\widehat\alpha)\le\widetilde J(\widehat\alpha)+\delta_J
\le\min\widetilde J+\varepsilon_{\rm alg}+\delta_J
\le J_*+2\delta_J+\varepsilon_{\rm alg}\).
If the strict gap in (8.8) satisfies \(g>2\delta_J+\varepsilon_{\rm alg}\), the same unique finite-set minimiser must be selected. This selection stability follows from the finite-objective gap and applies to the fixed candidate set (8.2).

### 8.3. Reference computation and error decomposition

For each candidate, a separately implemented product-integration procedure generates and fixes a physical-time reference function
\(\bar G=\nu c_0+A_1t^\beta+A_2t^{2\beta}+\bar L\), where \(\beta=\alpha_j\). Its nodes and coefficients are interpreted as their recorded exact dyadic values. The certified trajectory is \(\widehat Z=I^\alpha\bar G\), rather than the floating-point PI nodes themselves. The initial time interval uses the full generalised-power residual expansion. The remaining closed intervals use rigorous convolution-derivative bounds and the mean value theorem, covering all \(t\in[0,1/2]\). At each Fourier node, division of the physical residual by exact \(\nu\) gives the input to the proved error barrier or certified half-plane linear error estimate.

The recorded exponent is derivative-based: \(\bar L_T=\nu^{-1}\int\xi_*(T-t)\bar G(t)dt\). The positive kernel \(q_\alpha=(I^{1-\alpha}\xi_*)'\ge0\) gives
\[
|L_T-\bar L_T|
\le E_\delta(I^{1-\alpha}\xi_*)(T)/\nu
\le E_\delta\theta T^{1-\alpha}/[\nu\Gamma(2-\alpha)].
\tag{8.11}
\]
No residual integral is added a second time. Gamma and Mittag–Leffler curve moments, trajectory integrals, exponents, phases, and sums for the fixed curve use outward-rounded 100-bit rational intervals.

The positive-half-axis price rule has \(h=1/8\) and analytic-strip width \(a=9/20\). At the available nodes \(u=0:1/8:64\), the recorded trajectories use their actual residual certificates. For nodes above 64 through 128, the approximate transform is explicitly zero and each error is bounded by the exact-transform envelope. Above 128, the proved infinite discrete-rule tail bound obtained from the proved continuous-integral envelope is included. A comparison bound for the real part of the exact Riccati solution and a 64-cell lower sum over the entire positive-kernel curve give the high-frequency envelope. The analytic-strip trapezoidal error is estimated separately. Passage from the full-axis integral to the positive half-axis, including the half-weight at zero, is handled explicitly. The resulting enclosures cover all twelve model prices below and are based on error bounds rather than grid-convergence differences or Richardson diagnostics.

### 8.4. Objective comparison and quote consistency

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

### 8.5. All twelve prices and the total error of the numerical implementation

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

### 8.6. Conditions for the numerical results

This section provides three sets of continuous-time model-price intervals, finite-objective ordering, rowwise quote relations, and output-error and selection-stability bounds for the selected Padé implementation. The GR matching construction, affine model, Caputo comparison, Mittag–Leffler bounds, strip trapezoidal rule, and general objective-gap argument are established methods. The proofs and computations here connect them to the same finite-candidate problem.

The results apply to the three stated candidates, the fixed curve and remaining parameters, a six-month horizon, and twelve normalised quotes defined by implied volatilities. This setting also fixes the objective, numerical outputs, and definition of every error term.

Exact endpoints for all prices and objectives are available in the supplementary numerical material.



## 9. Shared Fourier Errors at the Actual Pricing Output

### 9.1. The error object and its centre

Fix one model parameter, maturity, contour, and reference grid. Let \(c^*\in\mathbb R^p\) be the continuous-model price vector, \(\bar c\) the exact finite reference sum, and \(c^{\rm fast}\) the frozen rational output. For each included frequency let \(\bar\phi_n\) be the reference transform and put \(z_n=\phi(u_n-i/2)-\bar\phi_n\). Section 7 supplies bounds \(|z_n|\le\epsilon_n\); at a deliberately omitted finite node \(\bar\phi_n=0\), the true-transform envelope supplies the radius. The same \(z_n\) enters every strike at this parameter and maturity.

For the Lewis rule in Section 6, set \(m_i=K_i/F\), \(k_i=\log m_i\), and
\[
a_{in}=-\frac{h\sqrt{m_i}}{\pi}\frac{e^{-iu_nk_i}}{u_n^2+1/4}\quad(n>0),\qquad
a_{i0}=-\frac{2h\sqrt{m_i}}{\pi}.
\tag{J1}
\]
The half weight at zero is already included in \(a_{i0}\). The complete error is
\[
c^*-\bar c=\Re\sum_{n=0}^{N}a_{\cdot n}z_n+R,
\qquad R\in\mathcal R,
\tag{J2}
\]
where \(\mathcal R\) includes the true infinite-grid tail and analytic-strip discretisation error. A finite reference sum enclosed by interval arithmetic contributes its centre uncertainty when a numerical representative of \(\bar c\) is used. Omitted finite nodes remain in (J2); they are not also charged as an infinite tail. No stochastic covariance is used in this representation.

### 9.2. Complete inclusion, support, and strictness

**Theorem 9.1 (complete shared-node inclusion).** Suppose (J2) holds, all radii are nonnegative, and \(\mathcal R\) is a nonempty compact convex outer set. Define
\[
\mathcal E_F=\left\{\Re\sum_na_{\cdot n}z_n:|z_n|\le\epsilon_n\right\}+\mathcal R,
\qquad d=\bar c-c^{\rm fast}.
\tag{J3}
\]
Then \(c^*-c^{\rm fast}\in d+\mathcal E_F\), and, for real \(w\),
\[
h_{d+\mathcal E_F}(w)=w^\top d+
\sum_n\epsilon_n\left|\sum_iw_i a_{in}\right|+h_{\mathcal R}(w).
\tag{J4}
\]
If the centre shift is supplied as a box \(d\in[d^-,d^+]\), replace the first term by the support of that box. All numerical evaluations of (J4) must be outward enclosures.

**Proof.** Substituting the actual transform errors in (J2) gives inclusion. The product of complex disks is compact and convex and its real-linear image has those properties. A disk \(|z|\le\epsilon\) has real-linear support \(\epsilon|b|\) for the functional \(\Re(bz)\): Cauchy--Schwarz gives the upper bound, attained at \(z=\epsilon\overline b/|b|\) when \(b\ne0\); when \(b=0\), every feasible point attains it. Independent disks and Minkowski addition give (J4). Translation gives the signed centre term. A box enclosing \(d\) provides a further valid Minkowski outer enclosure even if its coordinates are dependent. \(\square\)

If \(\mathcal R=\prod_i[-\rho_i,\rho_i]\), the smallest coordinate box of this same set has support
\[
h_{\operatorname{rect}(\mathcal E_F)}(w)=
\sum_i|w_i|\left(\sum_n\epsilon_n|a_{in}|+\rho_i\right).
\tag{J5}
\]
Consequently its excess over (J4), before translation, is
\[
G_F(w)=\sum_n\epsilon_n\left(
\sum_i|w_i a_{in}|-\left|\sum_iw_i a_{in}\right|\right)\ge0.
\tag{J6}
\]
It is strictly positive exactly when one positive-radius node has nonzero coefficients \(w_i a_{in}\) that do not all lie on a common nonnegative complex ray. This follows from the equality case of the complex triangle inequality, node by node. Translation does not change widths. This criterion compares the constructed set with its own coordinate box, and does not assert strict improvement over every independently available signed price enclosure.

For any separately established signed model-price box \(\mathcal I\), intersect it with \(\bar c+\mathcal E_F\). The actual model vector belongs to the intersection. Without solving the intersection support problem, the minimum of the two valid directional upper bounds remains valid; likewise take the maximum of the lower bounds. Thus a computation can retain the best signed marginal information while using node cancellation where it improves the complete bound. Nonemptiness of the mathematical intersection follows from inclusion, rather than from empirical agreement between numerical approximations.

### 9.3. A call-spread estimate and finite arithmetic

For \(w=e_i-e_j\), the node coefficient is
\[
|a_{in}-a_{jn}|=\frac{h}{\pi(u_n^2+1/4)}
\left|\sqrt{m_i}e^{-iu_nk_i}-\sqrt{m_j}e^{-iu_nk_j}\right|\quad(n>0).
\tag{J7}
\]
It is the modulus of one combined coefficient, rather than the sum of two moduli. A useful analytic bound, valid with \(b_i=\sqrt{m_i}\), is
\[
|b_ie^{-iuk_i}-b_je^{-iuk_j}|
\le |b_i-b_j|+\min(b_i,b_j)\min\{2,|u|\,|k_i-k_j|\}.
\tag{J8}
\]
To prove it, separate the difference in amplitudes from the phase difference using the smaller amplitude, then apply \(|e^{ix}-e^{iy}|\le\min(2,|x-y|)\). At zero, the spread coefficient is \(2h|b_i-b_j|/\pi\). Low-frequency error therefore cancels for nearby strikes even when the individual node radii are large. High-frequency and tail contributions are still retained.

The implementation below uses rational outward bounds for logarithms, trigonometric functions, square roots, and the circle constant. It encloses the exact coefficient difference before multiplying by the saved radius. Reference-sum and frozen-output intervals supply the signed centre. Taking interval midpoints for display never substitutes for the outward endpoint arithmetic used in a decision.

### 9.4. Safe objective bounds for a joint set

If the target quote \(m^*\) is enclosed around a stored centre \(\bar m\) with \(m^*-\bar m\in\mathcal M\), use \(r=c^{\rm fast}-\bar m\) and replace the output-error set by \(\mathcal E-\mathcal M\). This includes quote-conversion arithmetic with the correct sign. The following formulas otherwise take \(m\) to be exact.

Let \(J(e)=(r+e)^\top W(r+e)/(2p)\), where \(r=c^{\rm fast}-m\), \(W\succeq0\), and the complete output error belongs to a compact convex set \(\mathcal E\). For any trial vector \(e_0\), put \(g_0=W(r+e_0)/p\). Convexity gives the certified lower bound
\[
\inf_{e\in\mathcal E}J(e)\ge
J(e_0)-g_0^\top e_0-h_{\mathcal E}(-g_0).
\tag{J9}
\]
This follows by taking the infimum of the supporting affine function \(J(e_0)+g_0^\top(e-e_0)\). Feasibility of \(e_0\) is unnecessary for validity; it affects sharpness. A numerical primal minimizer becomes a lower-bound certificate only after its support or dual obligation has also been bounded correctly.

If \(M^2\ge\sup_{e\in\mathcal E}e^\top We\), expansion yields
\[
\sup_{e\in\mathcal E}J(e)\le
J(0)+\frac{h_{\mathcal E}(Wr)}p+\frac{M^2}{2p}.
\tag{J10}
\]
A safe choice is any valid coordinate box \(|e_i|\le b_i\): with \(W\) represented exactly, \(M^2=\sum_{ij}|W_{ij}|b_i b_j\) is sufficient. Tighter validated norm bounds may replace it. Maximization of this convex quadratic is not certified by a local stationary point. A supporting function, norm bound, interval subdivision, or valid relaxation must establish the upper direction.

For a finite candidate collection, form valid objective intervals by intersecting (J9)--(J10), when used, with the original interval-square bounds in Theorem 8.1. A unique candidate is certified only if its upper endpoint is smaller than every competing lower endpoint. If this condition is absent, return the nonempty set of candidates whose lower endpoint is at most the least upper endpoint. It contains every exact minimizer. Different candidates have different transform errors; (J4) does not identify their error variables.

The support formula, the equality case of the triangle inequality, and the convexity bounds are established tools. Their role here is to join the model-specific continuous residual certificate to the actual multi-strike pricing output, preserving every required budget and its centre. The numerical comparison in Section 11 is the evidence for the resulting financial improvement.


## 10. Classical Heston: Shared States and Trial-Field Residuals

This section keeps the classical sign \(\Delta^C=p_Q-p_P\). Model-minus-discrete error is its negative. Common probabilities belong only to the stated original \(Q\) chain; continuous residuals are integrated under \(P\). Appendix C gives the original-chain moment and constraint proof.

### 10.1. Fixed mathematical setting

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

### 10.2. Shared state constraints for the original chain

#### 10.2.1. Structural conditions and the core argument

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

The scheme-specific proof includes the complete Gaussian positive-part integral, exact continuous future kernel, exponential moments with doubled nonpositive loadings, the atom at zero, and the unbounded tail. Together they make (H1) an effective inclusion for this model. The full proof is given in [Appendix C and the supplementary classical derivation](../evidence/classical-evidence.md).

#### 10.2.2. From joint residuals to joint prices

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

#### 10.2.3. Criterion for strict tightening

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

#### 10.2.4. Certified example for the original instruments

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
g_{767}=\max F_A+\max F_P-\max(F_A+F_P)>0.
\tag{H8}
\]

Equation (H7) concerns the directional derivative of an auxiliary row; (H8) is a qualitative strict gap for the terminal outer set. For a construction retaining the specified modes and envelope identities and continued through valid timewise product sets, each level satisfies $g_j\ge0$, and the accumulated support gap before payoff intersections satisfies $\sum_jg_j\ge g_{767}>0$. A change in probability information, mode catalogue, or payoff-intersection rule requires application of (H5) to the resulting set.

The evidence consists of the [terminal strict-separation proposition](../evidence/classical-evidence.md), [exact input](https://github.com/130U/certified-rough-heston-valuation/blob/6a5134197db60c765ca3aea4f6cdeb2bafbb6617/code/classical/terminal767-input.json), [result certificate](https://github.com/130U/certified-rough-heston-valuation/blob/6a5134197db60c765ca3aea4f6cdeb2bafbb6617/code/classical/terminal767-result.json), and [independent rational verification](https://github.com/130U/certified-rough-heston-valuation/blob/6a5134197db60c765ca3aea4f6cdeb2bafbb6617/code/classical/terminal767-historical-review.json). The input SHA256 is `5ad2c18e9336db16e3957b9b1f6669f0f9065a13991ebed8a0498df9b942524c`. The independent verification records 407 exact-arithmetic checks.

### 10.3. A common framework for exact future-value functions and finite trial fields

#### 10.3.1. Function classes and sufficient conditions

The object is $X=(P,Q,R,\widetilde u)$, where $R$ is the same original payoff or an exact finite pricing-conversion remainder, and $\widetilde u$ is a deterministic trial field.

| Symbol | Meaning in this analysis |
|---|---|
| $A(X)$ | $\widetilde u$ is the exact continuous future-value function satisfying the integrability and regularity conditions below; its terminal and observation-time conditions agree exactly with $R$. |
| $H(X)$ | The same field satisfies global state-growth bounds, uniform integrability under squared weights, piecewise Itô regularity, genuine observation-time traces, temporal $L^1$ residual domination, terminal-discrepancy domination, and integrable defects under the original $Q$. |
| $\Phi$ | Apply the finite tower property under the original $Q$; under the original $P$, apply piecewise Itô calculus, Lyapunov-based removal of stopping, and $L^1$ traces; subtract the identities. |
| $M(X)$ | A four-term signed residual identity for the same field. |
| $B(X)$ | Certified residual bounds yield an effective interval or monetary bound for the original continuous–discrete price bias. |
| $C(X)$ | A finite deterministic time/state representation satisfying the stated verifiable growth, residual, and interface conditions. |
| $X_\star\in C\setminus A$ | The fully explicit analytic field (H17), whose formulas verify global growth, traces, integrability, exact terminal value, and a nonzero generator residual. |

Here $H$ is a sufficient condition independently defined by field properties; it does not require the trial field to equal the unknown exact solution. For the exact future-value function, the backward equation makes the continuous residual zero, and exact observation and terminal conditions eliminate their respective defects. Consequently, $A\Rightarrow H\Rightarrow M\Rightarrow B$ recovers the telescoping formula for the exact future-value function.

Separate intervals for individual prices do not alone establish shared state structure, because they supply no cross-price compatibility witness. The trial-field extension is expressed by the identity below, while the shared-state inclusion provides a joint error framework retaining price dependence.

#### 10.3.2. Structural condition $H$

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

#### 10.3.3. Core lemma and proof: $H\Rightarrow M$

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

#### 10.3.4. Propagation proposition: $M\Rightarrow B$

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

#### 10.3.5. A fully explicit analytic witness

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


### 10.4. Financial propagation: portfolio values and joint quote-acceptance sets

#### 10.4.1. Portfolio-value bounds

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

#### 10.4.2. Calibration acceptance and target valuation

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



## 11. Financial Decisions with the Complete Error

Section 8 retains the original quotes, parameters, and curve. The model and frozen output uniquely select \(\alpha=.52\), while quotation rows 8 and 9 exclude its full band compatibility. Ranking and quotation compatibility are separate conclusions. They do not identify a market parameter or establish ranking after refitting other parameters. We now recompute the original 4400--4500 spread using Section 9 and compare it with the best signed marginal intervals at the same frozen output.

| α | Symmetric marginal points | Signed marginal points | Joint points | Joint normalized bound | Signed-bound reduction |
|---|---|---|---|---|---|
| 0.52 | 3.593075 | 2.679931 | 1.397613 | 0.000331041790898 | 47.8489% |
| 0.60 | 1.955315 | 0.899772 | 0.504126 | 0.000119408273369 | 43.9719% |
| 0.90 | 0.477839 | 0.447312 | 0.396808 | 0.000093988900141 | 11.2903% |


Absolute bounds are rounded upward and reduction percentages downward; decisions use saved exact fractions. For alpha=.52, the joint full radius is at most 0.000291542087440, while the signed centre is approximately -0.000039499703457. The complete model-minus-fast spread error satisfies
\[
c^*_{4400}-c^*_{4500}-(c^{\rm fast}_{4400}-c^{\rm fast}_{4500})
\in[-0.000331041790898,\;0.000252042383983].
\tag{J11}
\]
Width and absolute error relative to the actual output are distinct quantities. All 1025 finite-node transform errors are counted once; strip error, the true infinite tail, and reference-sum arithmetic uncertainty are retained. This is a complete-budget improvement.

Prices are normalized as \(c=C/(DF)\), with \(D=1,F=4221.86\). Multiply normalized error by \(DF\) for index points. Before reading the new joint result, this diagnostic fixed a primary one-point budget and sensitivity thresholds of 0.25, 0.5, and 2 points. This is not described as pre-computation preregistration or a market-suitability criterion. The alpha=.52 joint bound does not certify the primary one-point budget. At the fixed two-point threshold, the marginal bound is insufficient while the joint bound suffices.

For alpha=.90, the joint signed interval is strictly positive, so the frozen output is below the model spread. Its absolute bound still uses the larger endpoint magnitude. Shared variables are confined to one candidate's same-maturity nodes.

Unique selection requires \(U_{j_0}<\min_{j\ne j_0}L_j\). Otherwise the rule returns an unresolved set containing every exact minimizer. An overlapping-input rejection test verifies the rule; it is not a new near-tie market experiment. Numerical calibration claims remain confined to the three stated candidates. A dense profile, continuous-domain optimization, and refitting other parameters are separate experiments.


### 11.3. Unseparated Candidates under Synthetic Quotes

To test an unresolved candidate decision with actual pricing outputs, we retain the original twelve strikes, 3700--4800, the six-month maturity, and the other model inputs, but restrict the candidate set to \(\alpha=.52,.60\). We construct synthetic target prices \(m_i=(c_i^{\rm fast,.52}+c_i^{\rm fast,.60})/2\). Interpreting the frozen fast outputs as exact dyadics makes their quadratic objectives \(J=(1/24)\sum_i(c_i-m_i)^2\) exactly equal, row by row; the common value lies in [8.8558783E-8, 8.8558784E-8]. Using the existing complete price certificates gives model-objective intervals [3.8651464E-8, 3.05889870E-7] and [3.2507356E-8, 8.9847876E-8], which overlap. The decision returns \(\{.52,.60\}\) with status `UNSEPARATED`, withholding a unique-winner certificate. As a control, the original SPX-IV-defined quote-midpoint intervals and the same two candidates and price certificates still certify \(\alpha=.52\). This is a synthetic-quote stress test, not an observed market tie, a denser continuous-parameter experiment, or a refit of other parameters. The complete price intervals retain continuous-residual, exponent, quadrature, finite-node, and true infinite-tail errors. Upstream certificates are reused rather than regenerated; exact targets, row identities, source byte identities, and execution records appear in `near-tie-diagnostic.json`.


## 12. Evidence, Verification Semantics, and Cost

The baseline is repository commit `6a5134197db60c765ca3aea4f6cdeb2bafbb6617`. The source inventory, exact shared-node ledgers, aggregate certificate, and command logs identify the current objects. Complete cover reconstruction checks 211241 leaves and 422481 tree nodes. Every leaf is additionally recomputed from the raw polynomials using the released 100-bit outward rational interval generator and compared field by field; `full-structure-verification.json` records this run separately from the initial 16-leaf check. This is full sign regeneration, without claiming a separately implemented transcendental library. The original frozen fields and continuous residual records remain the upstream objects. Saved-input checks, independent startup assembly at all 1539 candidate-frequency pairs, and a two-frequency full-time fresh replay for each candidate are distinguished from full-time regeneration at every frequency. A second spread checker does not import the new calculator: it assembles coefficient magnitudes through amplitude differences and a sine identity and checks the centre translation and complete remainder.

For the classical chain, all 22 probability rows and 918 profile entries are reproduced, and 407 exact terminal witness checks test feasibility, dual inequalities, uniqueness, and the signed derivative. Adversarial tests deliberately damage coverage, a sign record, a constraint, a node, or a budget and require rejection. Regeneration, saved-record verification, and independent numerical diagnostics answer different questions and are identified in the logs.

The complete budget assigns reference-state error to transform disks through the positive kernel; reference exponent and finite-sum arithmetic to centre uncertainty; omitted finite nodes to true-transform disks; strip error to continuous-integral/infinite-rule conversion; the true infinite tail to the remainder; and reference-minus-fast discrepancy to a signed translation. No finite node is charged twice as a tail.

The historical thirteen-dimensional field receipts identify saved mode integrals, but the portable package omits the full coefficient bank. The retained trial-function extension uses the fully explicit analytic example, rather than presenting those receipts as a complete annual price certificate. The archive and its scope remain documented in the internal review.

Execution times, versions, sign counts, node counts, and exit states are recorded in `verification.json` and the new spread certificate. Historical residual-generator times of approximately 793, 779, and 194 seconds are not fresh regeneration times. Support aggregation and upstream certification costs are reported separately.

## 13. Applicability and Conclusion

The probability model and integrability establish model prices; Theorem 3.1 establishes rational structure only on its stated continuous domain; complete price intervals additionally require the fixed field, scaling, forward curve, continuous residual, strip bound, and true tail. Joint strike errors share transforms only at one parameter and maturity. Candidate claims concern the fixed curve and the stated finite collection. Classical strictness concerns the specified original chain, modes, probability information, and outer set before payoff-range intersection.

Half-plane preservation alone does not make an approximation a probability characteristic function, an arbitrage-free full surface, or a Greeks certificate. The alpha=.90 price certificate uses its independent field and does not extend Theorem 3.1. The main proof does not rely on a broader central-frequency T1 chain.

The connection is established through actual error inclusion: rough-model residuals produce shared transform disks, classical original-chain states constrain residual feasibility, and their price images yield directional bounds at the actual output centre. The original spread obtains a strictly tighter complete certification bound; candidate ranking and quotation exclusion retain their separate meanings. The resulting analytical and computational claims preserve explicit objects, hypotheses, and quantifiers.


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

Theorem 2.3 of the source requires \(\operatorname{Re}\psi_1\in[0,1]\), a second-state initial transform with nonpositive real part, and a variance forcing term with nonpositive real part. Taking \(\psi_1=ia=1/2+iu\) and zero for the other initial and forcing terms gives (2.2), (2.6), and uniqueness in weak law. With \(\psi_1=1\), the Riccati solution is zero and \(\mathbb E S_T=S_0\) follows. A positive local martingale with constant expectation is a true martingale. Thus the probability strip in (6.1) follows from the continuous-time model. This argument applies established existence and affine-transform theory.

## Appendix B. The Exact Finite Certificate for Theorem 3.1

The certificate domain is \(\mathcal B=[13/25,3/5]\times[0,1]\). Every interval \(I=[\ell/2^{100},r/2^{100}]\) uses integer outward rounding. Rational inputs are rounded down and up; products take extrema over the four endpoint corners and are quantised. Reciprocals first exclude zero. Square roots use integer isqrt and an increment for the upper endpoint. Complex quantities use rectangular real–imaginary interval arithmetic. The analytic lower bounds in (3.3) fix the principal-root and reciprocal branches; no floating-point sign tolerance is used.

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

For each closed rectangle, substitute these enclosures successively into (3.3), (2.12), (2.13), (3.5), and (3.8). Accept only when the lower endpoints of all three \(\bar B_j\) are strictly positive and the upper endpoints of all six \(\bar D_n\) are strictly negative. Otherwise bisect one coordinate at its exact rational midpoint. The two closed children have the parent rectangle as their union, and strict enclosures also cover the shared boundary.

The finite covering contains 211241 leaf rectangles of total rational area exactly \(2/25\). An independent check reconstructs 422481 binary-tree nodes from the root, with maximum depth 19 and each recorded leaf occurring exactly once. In addition to the area check, this excludes missing subtrees, interior overlap, and endpoint gaps. The theorem uses the order interval covered by this complete closed tree.

The stronger rational margins in the complete certificate imply the following bounds. Each simplification has been independently checked using Fraction.

| Quantity on the full compactified domain | Strict lower bound |
|---|---:|
| \(\bar B_1,\bar B_2,\bar B_3\) | \(1/6000,\ 1/8000,\ 1/20000000000\) |
| \(-\bar D_1,-\bar D_2,-\bar D_3\) | \(1/30000,\ 1/2000000000,\ 1/6000\) |
| \(-\bar D_4,-\bar D_5,-\bar D_6\) | \(1/8000,\ 1/15000000,\ 1/100000\) |
| \(|\bar\Delta|^2\) | \(1/14400\) |

The proof consists of rigorous interval inclusion and a complete finite covering. The supplementary material provides the interval implementation, all leaf rectangles, and the tree-structure check for independent verification.



## Appendix C. Original-Chain Probability Inclusion


### C.1. Exact continuation and integrability

Write $s=S/100=e^Z$, $d=\kappa\bar v$, $h=1/768$, and $r=1/100$. Denote the continuous law by $P$ and the actual discrete-chain law by $Q$:

$$
\begin{aligned}
dZ_t&=(r-V_t/2)dt+\sqrt{V_t}(\rho\,dW_t+\sqrt{1-\rho^2}\,dB_t),\\
dV_t&=(d-\kappa V_t)dt+\xi\sqrt{V_t}\,dW_t,\\
Y&=dh+(1-\kappa h)v+\xi\sqrt{hv}\,G,\quad V'=Y^+,\\
Z'&=z+rh-hv/2+\sqrt{hv}(\rho G+\sqrt{1-\rho^2}H).
\end{aligned}
\tag{Q1}
$$

Here $G,H$ are independent standard normal variables; the stock and variance updates share $G$. The parameter box is

$$
\kappa\in[2,4],\quad \bar v,v_0\in[3/100,3/50],\quad
\xi\in[9/50,7/25],\quad \rho\in[-4/5,-3/10].
\tag{Q2}
$$

Each real loading of a finite multidate exponential mode is nonpositive, with total absolute value at most $1/2$. Let $H_{ji}$ be the realized prefix and $q=p+i\omega$ the remaining loading. Between observations, the continuous continuation $u=e^{qz+a+bv}$ satisfies

$$
b'=\tfrac12\xi^2b^2+(\rho\xi q-\kappa)b+\tfrac12(q^2-q),
\qquad a'=rq+db,
\tag{Q3}
$$

starting from zero terminal coefficients. At observations the remaining loading changes, while $a,b$ continue without resetting. Put $\kappa_p=\kappa-p\rho\xi$ and $\gamma_p=(p^2-p)/2$. On $\operatorname{Re}b=1$, the real derivative is

$$
\tfrac12\xi^2-\kappa_p+\gamma_p
-\tfrac12\{(\xi\operatorname{Im}b+\rho\omega)^2+(1-\rho^2)\omega^2\}<0,
\tag{Q4}
$$

since $p\in[-1/2,0]$, $\kappa_p\ge1.888$, and $\gamma_p\le3/8$. A first-crossing argument gives $\operatorname{Re}b\le1$. The radial bound

$$
\frac{d|b|}{dt}\le(\xi^2/2-\kappa_p)|b|+|q^2-q|/2
$$

prevents finite-time explosion, and $\operatorname{Re}a\le(6/25)T$.

To identify the formal continuation with its expectation, multiply all real loadings by $5/4$. Write $L_*(t),p_*(t)$ for the resulting realized and remaining loadings. The process

$$
\mathcal Y_t=\exp\{L_*(t)+p_*(t)Z_t+4V_t-(24/25)t\}
\tag{Q5}
$$

is a nonnegative local supermartingale. Its constant drift is nonpositive; its variance drift is at most $65/128-4(1.86)+8(7/25)^2<0$. Prefix and remaining-loading changes cancel at observations. The stopped affine local martingale $\mathcal M$ satisfies

$$
|\mathcal M_\tau|^{5/4}
\le e^{(5/4)(6/25)T+(24/25)T}\mathcal Y_\tau.
$$

Compact stopping and the supermartingale inequality give a uniform $5/4$-moment bound. Uniform integrability removes stopping and proves the exact continuation, including $v=0$ and every finite starting state. Finite telescoping under the original chain consequently yields

$$
\Phi_{Q,i}-\Phi_{P,i}=\sum_jr_{ji},\qquad
r_{ji}=E_Q[H_{ji}e^{q_{ji}Z_j}D_{ji}(V_j)],
\tag{Q6}
$$

where $D_{ji}(v)$ is the actual one-step $Q$ propagation minus the exact continuous continuation, after removing the common factor $e^{q_{ji}z}$.

### C.2. Original-chain squared moments and common probabilities

For nonpositive real loadings with total absolute value at most one,

$$
E_Q\exp\left\{\sum_{n\le j}\beta_nZ_n+4V_j\right\}
\le K_j:=e^{6/25+(73/75)jh}.
\tag{Q7}
$$

For $p\in[-1,0]$, completing the real Gaussian square in the stock factor changes the variance-candidate mean to $dh+\eta_pv$, where $\eta_p=1-\kappa_ph\ge191/192$. The pointwise bound $(-y)^+\le h(25e)^{-1}e^{-25y/h}$ gives

$$
E(-Y_p)^+\le\frac{h}{25e}
\exp\!\left[-25d+\frac{[-25\eta_p+(625/2)\xi^2]v}{h}\right]
\le\frac{h}{25e^{5/2}}<h/300.
\tag{Q8}
$$

Here $d\ge3/50$, the variance coefficient is at most $-71/192$, and $e^{5/2}>12$. At $v=0$ the negative part is exactly zero. Using $e^{By^+}\le e^{By}+B(-y)^+$ and $F_p(B)=\gamma_ph+\eta_pB+\xi^2hB^2/2$ gives the original conditional expectation

$$
E_Q[e^{pZ'+BV'}\mid z,v]
\le e^{pz+prh}\{e^{Bdh+F_p(B)v}+Bh\,e^{\gamma_phv}/300\}.
$$

Throughout(Q2), $F_p(4)\le4$, $rp\le0$, and $4d\le24/25$. Hence

$$
E_Q[e^{pZ'+4V'}\mid z,v]
\le e^{pz+4v}(e^{4dh}+4h/300)
\le e^{pz+4v+(73/75)h}.
$$

Successive conditioning, cancellation of loading changes, and $4v_0\le6/25$ prove(Q7). Gaussian square completion is an integration device; the resulting expectation remains under the original law $Q$.

For a common variance partition $I_r$, put $\pi_{jr}=Q(V_j\in I_r)$ and $h_{jir}\ge\sup_{v\in I_r}|e^{-2v}D_{ji}(v)|^2$. Split the integrand in(Q6) into $H_{ji}e^{q_{ji}Z_j}e^{2V_j}$ and $e^{-2V_j}D_{ji}(V_j)$. Complex Cauchy–Schwarz and(Q7) then give

$$
|r_{ji}|^2\le K_j\sum_rh_{jir}\pi_{jr}.
\tag{Q9}
$$

Every mode uses the same original-chain probability vector. Stock and history dependence remain in the first squared moment. A general trial-field defect that still depends on other states requires a uniform envelope over them or an enlarged partition. Continuous residuals under $P$ do not share the $Q$ occupation vector without a further proof.

### C.3. The 22 valid terminal probability constraints

Fix $\theta_*=(3,9/200,23/100,-11/20,9/200)$.

For $j=767$, we have $d=27/200$ and $\eta=255/256$. Use

$$
I_0=\{0\},\quad I_r=((r-1)/100,r/100]\ (1\le r\le100),\quad I_{101}=(1,\infty).
\tag{Q10}
$$

These 102 disjoint bands cover the state space. For $v>0$, the one-step mass at zero is $\Phi(-(dh+\eta v)/(\xi\sqrt{hv}))$; at $v=0$, $V'=dh>0$. The atom must be retained separately from the continuous density.

The projection excess satisfies

$$
\epsilon(v)=E[-dh-\eta v-\xi\sqrt{hv}G]^+
\le\frac{h\xi^2}{\eta\sqrt{2\pi e}}e^{-d\eta/\xi^2}<h/200.
$$

For $v=hz>0$, bound the normal negative part by $\xi h\sqrt z\,\varphi((d+\eta z)/(\xi\sqrt z))$, discard the nonnegative $d^2/z$ contribution in the exponent, and maximize $\sqrt z e^{-\eta^2z/(2\xi^2)}$. At zero the excess vanishes. The strict constant follows from $\eta>.99$, $\xi^2<.053$, $d\eta/\xi^2>2$, $\sqrt{2\pi e}>3$, and $e^{-2}<1/4$. The recursion $EV_{n+1}\le dh+\eta EV_n+h/200$ has fixed point $\bar v+1/(200\kappa)$. Starting from $V_0=\bar v$, induction gives

$$
EV_n\le\mu:=7/150.
\tag{Q11}
$$

Let $\lambda=\kappa-2\xi^2=14471/5000$, $\beta=1-\lambda h$, and $M_n=Ee^{4V_n}$. The positive-part inequality and concavity of $x^\beta$ give $M_{n+1}\le e^{4dh}M_n^\beta+h/50$. At $M=5/4$, use $\log(5/4)\ge1/5$, $4d-\lambda/5=-971/25000$, and $1-e^{-x}\ge x/2$ to obtain a decrease of at least $(5/4)(971/25000)h/2>h/50$. Since $M_0=e^{.18}<5/4$, induction and Jensen imply

$$
Ee^{4V_n}\le5/4,\qquad Ee^{-tV_n}\ge e^{-t\mu}\quad(t\ge0).
\tag{Q12}
$$

Take $\mathcal T=\{1,4,16,64,256,(191/192)^2/[2(49/625)h]\}$. For each $t$, set $t_0=t$ and $t_{n+1}=\eta_*t_n-c_*t_n^2$. Gaussian integration and $e^{-tY^+}\le e^{-tY}$ give

$$
E[e^{-tV'}\mid V=v]\le e^{-dh t}\exp[-(\eta t-\xi^2ht^2/2)v].
$$

Successive conditioning with $t_n\ge0$ yields

$$
Ee^{-tV_{767}}\le L_{767}(t)
:=\exp\!\left[-d_*h\sum_{n=0}^{766}t_n-v_*t_{767}\right].
\tag{Q13}
$$

The reference quadruple is $(191/192,(49/625)h/2,3/50,3/100)$; the point quadruple is $(255/256,\xi^2h/2,27/200,9/200)$. The reference uses no larger $\eta_*,d_*,v_*$ and no smaller $c_*$ than the actual values, giving a valid upper bound throughout(Q2). All 767 steps verify $0\le t_n\le\eta_* /(2c_*)$, ensuring monotonicity of the quadratic recursion on the entire rational enclosure.

For every $t\in\mathcal T$, the true probabilities therefore satisfy

$$
\begin{aligned}
\sum_r\inf_{I_r}e^{-tv}\pi_r&\le L^{\rm ref}_{767}(t),\\
\sum_r\inf_{I_r}e^{-tv}\pi_r&\le L^{\rm point}_{767}(t),\\
\sum_r\sup_{I_r}e^{-tv}\pi_r&\ge e^{-t\mu}.
\end{aligned}
\tag{Q14}
$$

The zero-band coefficients are both one; the tail coefficients are zero and $e^{-t}$. Adding $\sum_r\ell_r\pi_r\le\mu$, $\sum_re^{4\ell_r}\pi_r\le5/4$, and the two mass inequalities gives $6\times3+2+2=22$ rows. Nonnegativity is the variable domain. For saved inequalities $A\pi\le b$, upper-bound rows use lower coefficient endpoints and upper right-hand-side endpoints. Lower-bound rows use upper coefficient endpoints and lower right-hand-side endpoints before sign reversal. The saved rational polytope thus contains the actual probability vector. It is nonempty and compact as a closed subset of the probability simplex.

### C.4. Terminal one-step profiles over zero, finite bands, and the tail

The terminal continuation has $a_f=b_f=0$, so the projection difference $e^{b_fY^+}-e^{b_fY}$ is exactly zero. For $q=p+i\omega$, put $g=(q^2-q)/2$, $L=\rho\xi q-\kappa$, and $c=\xi^2/2$. Then

$$
D_q(v)=e^{rqh+hgv}-e^{a(h)+B(h)v},\quad
B'=g+LB+cB^2,\ B(0)=0,\quad a(h)=rqh+d\int_0^hB(t)dt.
\tag{Q15}
$$

The specified modes are $p=-1/48,\omega=64$ for the Asian profile, and $p=-1/4,\omega=-8,-24,\ldots,-120$ for the put. On $\operatorname{Re}B=0$, the real drift is at most $p(p-1)/2-(279/800)\omega^2<0$, hence $\operatorname{Re}B\le0$. The radial estimate gives $|B(t)|\le|g|t$.

Let $P(t)=b_1t+b_2t^2+b_3t^3$, with $b_1=g$, $b_2=Lg/2$, and $b_3=(L^2g+2cg^2)/6$. The exact guard $\operatorname{Re}b_1+\max(\operatorname{Re}b_2,0)h+\max(\operatorname{Re}b_3,0)h^2<0$ establishes $\operatorname{Re}P\le0$ on the whole step. Its residual is $-\sum_{k=3}^6r_kt^k$, where

$$
r_3=Lb_3+2cb_1b_2,\quad r_4=c(2b_1b_3+b_2^2),\quad
r_5=2cb_2b_3,\quad r_6=cb_3^2.
$$

The difference equation has coefficient $L+c(B+P)$ with real part at most $-\kappa_p$. Variation of constants gives

$$
E_B=\sum_{k=3}^6|r_k|_+\frac{h^{k+1}}{k+1},\qquad
E_A=d\sum_{k=3}^6|r_k|_+\frac{h^{k+2}}{(k+1)(k+2)}.
\tag{Q16}
$$

Define

$$
\begin{aligned}
A_q&=\min\{|-d\int_0^hP|_++E_A,\ d|g|_+h^2/2\},\\
B_q&=\min\{|hg-P(h)|_++E_B,\ (|L|_++\xi^2|g|_+h)|g|_+h^2/2\},\\
m_q&=2-\max\{h\operatorname{Re}g,\min(0,\operatorname{Re}P(h)+E_B)\}>0.
\end{aligned}
\tag{Q17}
$$

The second branches use $|B(t)|\le|g|t$. The exponential-difference integral identity yields, for every $v\ge0$,

$$
|e^{-2v}D_q(v)|\le e^{prh}(A_q+B_qv)e^{-m_qv}.
\tag{Q18}
$$

The band supremum is determined by finite endpoints of the closure or the stationary point $1/m_q-A_q/B_q$; the infinite-tail limit is zero. If $B_q=0$, use the monotone branch without division. The coarse bound $|e^{-2v}D_q(v)|\le2e^{prh-2v}$ also holds. Thus valid input to(Q9) is

$$
h_{qr}=\min\{[4e^{2prh-4\ell_r}]_+,\ [e^{2prh}S_{qr}^2]_+\},\quad
S_{qr}=\sup_{v\in I_r}(A_q+B_qv)e^{-m_qv}.
\tag{Q19}
$$

The zero band is evaluated at $v=0$; the tail includes its endpoint enclosure, any stationary point, and its zero limit. Rational outward checks cover the guards for all nine modes and all 918 profile entries. These inputs and the main text's primal–dual witness close the terminal example's computational obligations. Strict terminal outer-set tightening alone does not give a money-valued annual pricing-error bound.


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

23. **OuyangAsian2024.** Ouyang, Theodore. *Certified Valuation of Arithmetic Asian Options via Common Gaussian Smoothing*. Author manuscript, 2024 cover version; supplied PDF. [Project](https://github.com/130U/certified-valuation-arithmetic-asian-options).

24. **BBWeak2023v1.** Bayer, Christian and Breneis, Simon. *Weak Markovian Approximations of Rough Heston*. 2023. [Version record](https://arxiv.org/abs/2309.07023v1), [original PDF](https://arxiv.org/pdf/2309.07023v1). Version used: arXiv:2309.07023v1, submitted 13 September 2023. The characteristic-function and European-payoff error results are Theorems 2.2 and 2.7.

25. **BBSimulation2023v1.** Bayer, Christian and Breneis, Simon. *Efficient option pricing in the rough Heston model using weak simulation schemes*. 2023. [Version record](https://arxiv.org/abs/2310.04146v1), [original PDF](https://arxiv.org/pdf/2310.04146v1). Version used: arXiv:2310.04146v1, submitted 6 October 2023. This version reports second-order weak convergence numerically on p. 4.

26. **Kopteva2021v2.** Kopteva, Natalia. *Pointwise-in-time a posteriori error control for time-fractional parabolic equations*. Applied Mathematics Letters 123, 107515, 2022. DOI [10.1016/j.aml.2021.107515](https://doi.org/10.1016/j.aml.2021.107515). [Version record](https://arxiv.org/abs/2105.05848v2), [original PDF](https://arxiv.org/pdf/2105.05848v2). Version used: arXiv:2105.05848v2, revised 5 July 2021; first submitted 12 May 2021. The pointwise residual bound and norm inequality are Theorem 2.2 and Lemma 2.8.
