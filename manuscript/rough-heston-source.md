# Structural Properties, Price Error Bounds, and Candidate Selection Stability for the Third-Order Rational Rough Heston Approximation

## Abstract

We study the structural properties of the six-condition, two-point third-order rational approximation of Gatheral and Radoičić and the propagation of its numerical error into option prices. On the parameter domain \(\alpha\in[.52,.60]\), \(\rho=-.7445\), with zero Riccati mean reversion, compactification of the Fourier frequency and strict sign bounds for the unnormalised matching polynomials establish nonsingularity at every real frequency, a denominator with positive real part at every positive time, and an approximate trajectory in the left half-plane. For complex reference trajectories satisfying specified regularity and real-part bounds, a two-dimensional convex Caputo inequality and the one-sided dissipation of the Riccati equation convert an independently computed residual into a state error bound. A positive-kernel representation of the characteristic exponent for a fixed nondecreasing forward variance curve, analytic-strip quadrature, and high-frequency tail bounds then give model-price intervals. In a six-month, twelve-strike example defined by public SPX data, the model objectives for \(\alpha=.52,.60,.90\) are strictly separated. The continuous-time model and the specified third-order implementation both select \(\alpha=.52\), with a competing-objective gap exceeding \(2.70205218\times10^{-7}\). The same price intervals support quote-consistency tests and valuation-error control for a call spread. These results provide mathematical guarantees for fast pricing and finite-candidate comparisons under the stated model specification.

**Keywords:** rough Heston; fractional Riccati equation; two-point Padé approximation; pole-free approximation; dissipation; price error; candidate selection stability.

## 1. Introduction

Fourier pricing in the rough Heston model requires the solution of a complex fractional Riccati equation. Rational approximations matched at both time endpoints reduce the cost of solving this equation frequency by frequency and are therefore useful for repeated pricing and parameter comparisons. Financial decisions based on their output require a well-defined approximation, a model-price error bound, and control of the objective function.

We fix the six-condition, two-point third-order construction of Gatheral and Radoičić. Its matching system is formed from short-time and long-time expansion coefficients. Structural analysis first requires nonsingularity of this system, followed by control of the positive-time denominator and approximate trajectory. We establish these properties through sign constraints on the original determinant and Cramer numerators, before any division by the determinant.

The price-error analysis uses an independent reference trajectory and its continuous-time Caputo residual. One-sided dissipation of the Riccati divided difference controls the complex equation. A two-dimensional convex history inequality then yields a positive-kernel comparison for the error modulus. A nondecreasing forward variance curve gives a positive linear-functional representation of characteristic-exponent error. Combined with the analytic strip and high-frequency tail bounds of the underlying probability model, this transfers trajectory information into complete price intervals.

Finally, we compare three roughness candidates while holding the forward variance curve and the remaining parameters fixed. The price intervals establish a strict gap in the model objective and prove that the continuous-time model and the specified fast implementation select the same candidate. The resulting criterion connects numerical accuracy with a particular financial decision: the ordering is preserved whenever the objective perturbation remains within the allowance determined by the competing-objective gap.

### 1.1. Related work

Gatheral and Radoičić [GR2019] introduced a rational approximation of the rough Heston solution by matching its two time endpoints. Their generalisation and author code include a mean-reversion construction [GR2023v1, GatheralCode2023]. Jeng and Kiliçman [JK2020] studied fourth-order global Padé approximations and subsequently examined SPX calibration using publicly released data [JK2021, WoonJengSPXDataset2021Frozen]. We use the established third-order formula and analyse its matching system, denominator, and trajectory on a specified continuous parameter domain, together with error bounds for a specified financial computation.

Two-sided error theory for multipoint Padé approximants of Stieltjes functions is developed by Gilewicz et al. [Gilewicz2005]. Our structural result concerns the original algebraic quantities of the present matching system and verifies the required signs directly. The fixed third-order construction, its parameter domain, and the quantifier over all positive times determine the scope of the theorem.

The continuous-time model and its affine transform use the forward variance formulation of Abi Jaber and El Euch [AbiJaberElEuch2018v1]. Fractional error comparison uses the Caputo convexity tools of Li and Liu [LiLiu2018], together with positivity and comparison properties of Mittag–Leffler functions [Simon2014, NIST2010]. The pricing integral and its error analysis use Fourier valuation and analytic-strip quadrature [EberleinGlauPapapantoleon2008v1, TrefethenWeideman2014]. We apply these tools to the dissipation of the complex Riccati equation, the specified forward variance curve, and the recorded numerical outputs, verifying the assumptions at each step.

### 1.2. Main results and organisation

The first result is a full-frequency structural theorem for the established third-order approximation. On \(\alpha\in[.52,.60]\), \(\rho=-.7445\), and \(\kappa=0\), the matching system is nonsingular, the three normalised denominator coefficients have strictly positive real parts, the denominator satisfies \(\operatorname{Re}Q(y)\ge1\), and \(\operatorname{Re}\widehat H(y)<0\) holds for \(y>0\).

The second result is a positive-kernel state error bound for complex reference trajectories with an independent residual envelope and a one-sided real-part bound. Positive dissipation gives the time-uniform bound \(\delta/\sigma\). The positive-kernel exponent representation and the complete Fourier error estimate transfer this state bound into prices.

The final result concerns the specified twelve strikes, three candidates, and fixed forward variance curve. The model-objective intervals are strictly separated, and the specified third-order implementation preserves the model-based candidate selection. The price intervals also yield quote tests and call-spread valuation bounds.

Sections 2–7 present the mathematical setting, structural theorem, stability proof, and price-error analysis and verification. Section 8 gives the finite-candidate example. Section 9 collects the conditions of applicability, and Section 10 presents the financial applications.

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

The positive-half-axis price rule has \(h=1/8\) and analytic-strip width \(a=9/20\). At the available nodes \(u=0:1/8:64\), the recorded trajectories use their actual residual certificates. For nodes above 64 through 128, the approximate transform is explicitly zero and each error is bounded by the exact-transform envelope. Above 128, the proved continuous infinite-tail bound is included. A comparison bound for the real part of the exact Riccati solution and a 64-cell lower sum over the entire positive-kernel curve give the high-frequency envelope. The analytic-strip trapezoidal error is estimated separately. Passage from the full-axis integral to the positive half-axis, including the half-weight at zero, is handled explicitly. The resulting enclosures cover all twelve model prices below and are based on error bounds rather than grid-convergence differences or Richardson diagnostics.

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

## 9. Conditions of Applicability

### 9.1. Structure and stability

Throughout the paper, the approximation is the six-condition, two-point third-order construction. The structural theorem covers every real frequency and every positive time on \(\alpha\in[.52,.60]\), \(\rho=-.7445\), and \(\kappa=0\). This includes the central frequency \(u=0\).

The state-error theorem assumes the specified absolute continuity, local Lipschitz regularity at positive times, zero initial value, one-sided real-part bound, and independent Caputo residual. These conditions give a dissipation rate \(\sigma\ge0\) and a positive-kernel comparison bound. The exponent estimate uses the fixed nondecreasing forward variance curve. The scaling relations in \(\nu\) recover the physical state, normalised state, and residual separately.

### 9.2. Prices and candidate decisions

The pricing results concern the admissible forward variance model and the normalised European prices defined in the paper. Complete intervals include trajectory, quadrature, high-frequency-tail, and arithmetic errors. All comparisons share the same forward-price, discounting, and quote-conversion conventions.

Candidate selection concerns \(\alpha=.52,.60,.90\) over a six-month horizon, with the forward variance curve, correlation, and remaining parameters fixed. The strict model-objective gap gives an explicit tolerance for finite-candidate decisions. Quote tests and call-spread valuation use the same price intervals and therefore share the same model and units.

### 9.3. Financial implementation

Application begins by stating the pricing specification and intended financial decision. Candidate comparisons allocate numerical error according to the objective gap. Portfolio valuation combines price intervals using position coefficients. Quote tests compare model-price intervals with quote bands. The intended use determines the required accuracy, and each decision can be traced to the mathematical assumptions and price intervals in the paper.

## 10. Financial Applications: Roughness Candidates, Quote Tests, and Call-Spread Valuation

SPX options are European-exercise and cash-settled contracts, consistent with the European Fourier valuation framework used here. [Cboe, 2022](https://ir.cboe.com/news/news-details/2022/Cboe-to-Further-Expand-SP-500-Index-Options-Suite-with-New-and-Additional-Daily-Expirations-09-19-2022/default.aspx)

The speed of rational approximation is useful for repeated pricing and parameter searches. The error estimates address three practical questions: whether numerical approximation preserves the optimal roughness candidate; whether the model-price difference from a bid–ask band retains a definite sign after accounting for numerical error; and how single-option bounds translate into a portfolio valuation tolerance. We answer these questions using a public SPX implied-volatility sample.

Jeng and Kiliçman used third- and fourth-order Padé approximations for SPX calibration and released the corresponding data and code. [Jeng–Kiliçman, 2021, §4 and Table 1](https://www.mdpi.com/2227-7390/9/21/2675) We use these data with the other model inputs fixed and apply the price-error estimates to finite-candidate calibration and portfolio valuation. Every numerical conclusion is based on an interval for a price defined by the corresponding model equation.

### 10.1. Data and pricing specification

Take the twelve quotes at maturity $T=1/2$ in the 18 June 2021 sample, with strikes $3700,3800,\ldots,4800$. The inputs are the public bid and ask implied volatilities, denoted $\sigma_i^{\rm bid}$ and $\sigma_i^{\rm ask}$. Each input is interpreted as its original decimal value. Market-quote columns and model-output columns are distinguished according to the authors' description. [Data description](https://github.com/WoonJeng/Dataset-for-SPX-Calibration-of-Option-Approximations-under-Rough-Heston-model/blob/860049da2b7486fe8aa509061eff23cc28c2ef89/README.md), [original twelve rows](https://github.com/WoonJeng/Dataset-for-SPX-Calibration-of-Option-Approximations-under-Rough-Heston-model/blob/860049da2b7486fe8aa509061eff23cc28c2ef89/spx_decomp.csv).

Set the discount factor $D=1$ and forward price $F=4221.86$. A zero-carry European call defines the common normalised price

\[
c=\frac{C}{DF}.
\tag{U1}
\]

Substitute the implied volatilities into Black–Scholes to define the normalised bid and ask prices
$B_i=\operatorname{BS}(\sigma_i^{\rm bid})/(DF)$ and $A_i=\operatorname{BS}(\sigma_i^{\rm ask})/(DF)$, and the price midpoint $M_i=(B_i+A_i)/2$. The public IV sample thus defines the quote intervals $[B_i,A_i]$ and calibration target used here. The price unit, discount factor, and forward price are part of this example's pricing specification.

Fix the correlation, volatility coefficient, and Riccati mean-reversion parameter at

\[
\rho=-.7445,\qquad \nu=.2897,\qquad \lambda_R=0,
\]

and fix the forward variance curve

\[
\xi_*(t)=.0721+(.0262-.0721)
E_{.5286}(-.5037t^{.5286}).
\tag{U2}
\]

Here $E_\beta$ is the Mittag–Leffler function. The exponent $.5286$ and coefficient $.5037$ remain the same for every roughness candidate; mean reversion in the Riccati equation is $\lambda_R=0$. The values are taken from Table 1 of Jeng and Kiliçman and define a conditional calibration problem with the other inputs fixed.

Take the candidate set

\[
\alpha\in\{.52,.60,.90\},\qquad
H=\alpha-\tfrac12\in\{.02,.10,.40\},
\tag{U3}
\]

where $H$ is the roughness parameter. With model prices $c_i(\alpha)$, use the squared loss

\[
J(\alpha)=\frac1{24}\sum_{i=1}^{12}[c_i(\alpha)-M_i]^2.
\tag{U4}
\]

The optimality conclusions below concern the three candidates in (U3), conditional on (U2) and the other fixed parameters. We compare prices defined by the model equation with outputs of the specified third-order Padé implementation.

### 10.2. Stability of the roughness-candidate selection

For each candidate, all twelve model prices have verified containing intervals. The reference computation includes continuous-time residual, characteristic-exponent, Fourier-quadrature, and integral-tail errors in its price bounds. Squaring and summing these intervals in (U4) gives the model-objective enclosure $[L_j,U_j]$. Third-order Padé outputs are interpreted as their recorded dyadic values; rounding enclosures for quote conversion are included in their objective intervals.

| $\alpha$ | $H$ | Outward interval for the model objective $J$ | Outward interval for the implemented third-order Padé objective |
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

Thus $\alpha=.52$ and $H=.02$ form the unique optimal candidate for model prices on (U3). The third-order Padé objective also has its unique minimum at $.52$, with a strict objective gap exceeding $5.41876447\times10^{-7}$. The approximate procedure therefore preserves roughness selection on the stated candidate set.

The gap also provides an error tolerance for other numerical implementations. Suppose an implementation returns $\widetilde J$ with

\[
\sup_{\alpha\in\{.52,.60,.90\}}
|\widetilde J(\alpha)-J(\alpha)|\le\delta_J,
\qquad
\widetilde J(\widehat\alpha)\le\min\widetilde J+\varepsilon_{\rm alg},
\]

where $\varepsilon_{\rm alg}\ge0$ is the optimisation objective tolerance. Then

\[
J(\widehat\alpha)-\min J
\le2\delta_J+\varepsilon_{\rm alg}.
\tag{U6}
\]

**Proof.** The objective-error bound and near-optimality condition give successively

\[
J(\widehat\alpha)
\le\widetilde J(\widehat\alpha)+\delta_J
\le\min\widetilde J+\varepsilon_{\rm alg}+\delta_J
\le\min J+2\delta_J+\varepsilon_{\rm alg}.
\]

If $2\delta_J+\varepsilon_{\rm alg}<g$, selection of another candidate contradicts (U5), so $\widehat\alpha=.52$. In particular, when the implementation minimises $\widetilde J$ exactly, the following uniform objective-error bound suffices to preserve the selection:

\[
\delta_J<1.35102609\times10^{-7}.
\tag{U7}
\]

Equation (U6) is the standard objective-perturbation estimate. The specific calculation in this example propagates model-price error into the same quote objective and obtains a strictly positive gap. The table directly proves selection preservation for the specified Padé implementation; (U7) gives a sufficient accuracy requirement for other implementations.

In a pricing or calibration workflow, a fast approximation can first compute candidate objectives, followed by reference price intervals for the relevant candidates. Strict separation of the objective intervals confirms their finite-set ordering. The distinguishable gap between candidates therefore determines the numerical accuracy required for this decision.

### 10.3. Separation of model prices from quote intervals

Optimality of a selected candidate and its ability to explain each quoted row are separately testable quantities. For $\alpha=.52$, check strikes $4400$ and $4500$ row by row. All values below use the normalised units in (U1).

| Strike | Outward quote-interval enclosure | Model-price interval | Third-order Padé output | Strict lower bound on model price minus ask |
|---|---|---|---|---|
| 4400 | $[.021578146466486,.021885184947781]$ | $[.022001379841730,.022593310552455]$ | .022444989699935… | $>.000116194893950$ |
| 4500 | $[.013026560676140,.013312188046179]$ | $[.013328234352325,.013926853822165]$ | .013735688886630… | $>.000016046306147$ |

The final column is calculated from the original exact interval endpoints and then rounded outward. It gives a strict price difference that remains valid after pricing error is included.

For $K=4400$, denote the third-order Padé output by $c^P_{4400}$. The model price satisfies

\[
|c^P_{4400}-c_{4400}|
<.000443609858205.
\tag{U8}
\]

The numerical output exceeds the ask by more than $.000559804752154$. Deducting the complete pricing error in (U8) leaves a positive difference. Comparing the lower model-price endpoint directly with the upper ask endpoint gives the strict lower bound in the table. The corresponding comparison for $K=4500$ is also strictly positive.

Hence the example yields two definite conclusions: $H=.02$ has the smallest objective among the three candidates, and its model prices in the two rows $K=4400,4500$ exceed the asks. The first conclusion concerns candidate selection; the second identifies parameter configurations and forward variance assumptions for further examination. Both use the same price-error bounds, units, and model inputs.

This rowwise check can be included in pricing-model validation records. Relevant records contain the data version, price units, model parameters, forward variance curve, numerical implementation, and model-price intervals. Strict separation from the quote intervals provides a quantitative basis for reviewing inputs and parameter specifications.

The historical model-validation framework in SR 11-7 (2011, §V) includes conceptual soundness, ongoing monitoring, and outcomes analysis. The price intervals here supply mathematical evidence for the pricing calculation and quote comparison. [Historical guidance](https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf).

### 10.4. Call-spread valuation error

Consider buying the call with strike $4400$ and selling the call with strike $4500$ at the same maturity. Its normalised model value is

\[
v=c_{4400}-c_{4500}.
\tag{U9}
\]

The individual price intervals above give

\[
v\in
[.008074526019566,.009265076200129].
\tag{U10}
\]

The corresponding third-order Padé output satisfies

\[
v^P=.008709300813304\ldots,
\qquad
|v^P-v|<.000634774793739.
\tag{U11}
\]

**Proof.** For $c_1\in[\ell_1,r_1]$ and $c_2\in[\ell_2,r_2]$,

\[
c_1-c_2\in[\ell_1-r_2,r_1-\ell_2].
\]

Substitution of the two model-price intervals gives (U10). Take the larger of the distances from $v^P$ to the two exact interval endpoints and round outward to obtain (U11). If each single-price error is first symmetrised and the triangle inequality then applied, the upper bound is $.000851064392510$. Retaining the signed endpoints of the individual intervals gives the tighter portfolio bound in (U11). This calculation uses linear operations on marginal price intervals; the improvement comes from their asymmetric endpoint information.

If the normalised valuation-error tolerance is $\varepsilon_v=.0007$, then (U11) proves that the specified implementation meets it. The portfolio accuracy requirement is therefore subject to a verifiable numerical decision.

For a finite same-maturity option portfolio, let $n_i$ be the position sizes and $DF$ the known discounted-forward product. If $|c_i^P-c_i|\le\varepsilon_i$, then

\[
\left|\sum_i n_i C_i^P-\sum_i n_i C_i\right|
\le DF\sum_i|n_i|\varepsilon_i,
\tag{U12}
\]

When full single-price intervals are available, combine their endpoints according to the position signs: positive positions retain the endpoint order, while negative positions reverse it. This preserves more information than summing symmetrised error bounds. A specified portfolio tolerance can then identify which price intervals require refinement and allocate pricing accuracy to the corresponding contracts.

### 10.5. Application results and implementation conditions

| Application | Mathematical operation | Result in this example | Use |
|---|---|---|---|
| Roughness-candidate selection | Compare objective intervals for three candidates with the other parameters and curve fixed | Model prices and the specified Padé implementation both select $H=.02$; model-objective gap $>2.70205218\times10^{-7}$ | A strict finite-set ordering criterion and numerical accuracy requirement |
| Rowwise quote test | Compare model-price enclosures with bid–ask intervals | For $K=4400,4500$, model prices exceed the asks by $>.000116194893950$ and $>.000016046306147$, respectively | Identify quoted rows and parameter specifications for further examination |
| Call-spread valuation | Combine price endpoints by position sign and compare with the numerical output | 4400–4500 call-spread error $<.000634774793739$ | Determine whether the implementation meets the specified portfolio tolerance |

These conclusions share the following specification: zero-carry normalised prices defined by public implied volatilities, fixed forward variance curve (U2), twelve rows at maturity $T=1/2$, candidate set (U3), and the specified six-condition third-order Padé implementation. The price proofs cover the model state, characteristic exponent, Fourier quadrature, and integral tail. Within this setting, the error bounds yield definite results for parameter selection, quote differences, and portfolio valuation.

This section uses standard interval operations, objective-perturbation estimates, and linear portfolio relations to turn the structural properties and price-error bounds into financial criteria. The criteria connect approximation accuracy with the intended decision: the objective gap controls selection, interval separation controls quote testing, and positions and price errors jointly control portfolio valuation.

## 11. Conclusion

We have established structural and error estimates for the existing third-order rational rough Heston approximation. The original matching algebra gives full-frequency well-definedness, denominator positivity, and preservation of the left half-plane. Complex one-sided dissipation converts an independent Caputo residual into a state-error bound. The positive-kernel characteristic exponent and complete Fourier estimates then give model-price intervals.

In the fixed example defined by public SPX data, these intervals strictly separate the three model objectives and prove that the specified third-order implementation preserves selection of \(\alpha=.52\). Quote-consistency tests and the call-spread error interval show how the same theory is used in pricing validation and portfolio valuation. The results provide computable and verifiable mathematical guarantees for the model, parameters, and financial setting stated in the paper.

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

## Appendix C. Numerical Verification Material

The supplementary material records computation parameters, quote inputs, reference-trajectory coefficients, residual intervals, price intervals, and file digests. Each residual and exponent calculation refers to the same reference trajectory. For each candidate, the objective is formed from the twelve price intervals. Decimal endpoints in the tables are outward roundings of the original rational intervals; final decisions use the exact endpoints.

Special functions use the explicit remainders and interval arithmetic in Section 7. Batched floating-point calculations rely on the IEEE arithmetic assumptions in Section 7.3. The correspondence between the analytical arguments and numerical implementation is given in the [proof map](../docs/proof-map.md). Original computation records are listed in the [price-proof material](../docs/proof-map.md); formula, reference, and numerical read-back checks for this manuscript are recorded in the [verification record](../docs/release-verification.json).

## References

1. **GR2019.** Gatheral, Jim and Radoičić, Radoš. *Rational Approximation of the Rough Heston Solution*. International Journal of Theoretical and Applied Finance 22(3), 1950010, 2019. DOI [10.1142/S0219024919500109](https://doi.org/10.1142/S0219024919500109). Version used: SSRN manuscript dated 29 January 2019.

2. **GR2023v1.** Gatheral, Jim and Radoičić, Radoš. *A Generalization of the Rational Rough Heston Approximation*. 2023. [Source](https://arxiv.org/abs/2310.09181v1). Version used: arXiv:2310.09181v1.

3. **JK2020.** Siow Woon Jeng and Adem Kiliçman. *Series Expansion and Fourth-Order Global Padé Approximation for a Rough Heston Solution*. Mathematics 8(11), 1968, 2020. DOI [10.3390/math8111968](https://doi.org/10.3390/math8111968).

4. **JK2021.** Siow Woon Jeng and Adem Kiliçman. *SPX Calibration of Option Approximations under Rough Heston Model*. Mathematics 9(21), 2675, 2021. DOI [10.3390/math9212675](https://doi.org/10.3390/math9212675).

5. **AbiJaberElEuch2018v1.** Abi Jaber, Eduardo and El Euch, Omar. *Markovian structure of the Volterra Heston model*. Statistics & Probability Letters 149, 63–72, 2019. DOI [10.1016/j.spl.2019.01.024](https://doi.org/10.1016/j.spl.2019.01.024). Version used: arXiv:1803.00477v1.

6. **LiLiu2018.** Li, Lei and Liu, Jian-Guo. *A Generalized Definition of Caputo Derivatives and Its Application to Fractional ODEs*. SIAM Journal on Mathematical Analysis 50(3), 2867–2900, 2018. DOI [10.1137/17M1160318](https://doi.org/10.1137/17M1160318). The convexity result is Proposition 3.11.

7. **Simon2014.** Simon, Thomas. *Comparing Fréchet and positive stable laws*. 2014. [Source](https://arxiv.org/abs/1310.1888v2). Version used: arXiv:1310.1888v2.

8. **TrefethenWeideman2014.** Trefethen, Lloyd N. and Weideman, J. A. C. *The Exponentially Convergent Trapezoidal Rule*. SIAM Review 56(3), 385–458, 2014. DOI [10.1137/130932132](https://doi.org/10.1137/130932132). The strip quadrature result is Theorem 5.1.

9. **NIST2010.** Olver, Frank W. J. and Lozier, Daniel W. and Boisvert, Ronald F. and Clark, Charles W. *NIST Handbook of Mathematical Functions*. Cambridge University Press, 2010. [Source](https://dlmf.nist.gov/).

10. **GatheralCode2023.** Gatheral, Jim. *RationalRoughHeston: roughHestonPadeLambda.R*. 2023. [Source](https://github.com/jgatheral/RationalRoughHeston/blob/d65ea96e4c113fbb330074dfaea3e7715d650bbd/roughHestonPadeLambda.R).

11. **WoonJengSPXDataset2021Frozen.** WoonJeng. *Dataset for SPX Calibration of Option Approximations under Rough Heston model*. 2021. [Source](https://github.com/WoonJeng/Dataset-for-SPX-Calibration-of-Option-Approximations-under-Rough-Heston-model/tree/860049da2b7486fe8aa509061eff23cc28c2ef89).

12. **Gilewicz2005.** Gilewicz, Jacek and Pindor, Maciej and Telega, J. Joachim and Tokarzewski, Stanisław. *N-Point Padé Approximants and Two-Sided Estimates of Errors on the Real Axis for Stieltjes Functions*. Journal of Computational and Applied Mathematics 178(1–2), 247–253, 2005. DOI [10.1016/j.cam.2003.12.051](https://doi.org/10.1016/j.cam.2003.12.051).

13. **EberleinGlauPapapantoleon2008v1.** Eberlein, Ernst and Glau, Kathrin and Papapantoleon, Antonis. *Analysis of valuation formulae and applications to exotic options in Lévy models*. 2008. [Source](https://arxiv.org/abs/0809.3405v1). Version used: arXiv:0809.3405v1.

14. **CboeSPX2022.** Cboe Global Markets. *Cboe to Further Expand S&P 500 Index Options Suite with New and Additional Daily Expirations*. 2022. [Source](https://ir.cboe.com/news/news-details/2022/Cboe-to-Further-Expand-SP-500-Index-Options-Suite-with-New-and-Additional-Daily-Expirations-09-19-2022/default.aspx).

15. **FederalReserveSR1107.** Board of Governors of the Federal Reserve System and Office of the Comptroller of the Currency. *Supervisory Guidance on Model Risk Management*. Board of Governors of the Federal Reserve System and Office of the Comptroller of the Currency (SR 11-7, Attachment), 2011. [Source](https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf). Cited for the historical model-validation framework issued in 2011.
