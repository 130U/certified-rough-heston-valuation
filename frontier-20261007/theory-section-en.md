### 9.6. Positive fractional curve kernels and changes of reference

The curve condition in Theorem 9.2 is the nonnegativity of \(q_\alpha=(I^{1-\alpha}\xi)'\), rather than monotonicity of \(\xi\). The state and reference still belong to \(AC[0,T]\), have the same zero initial value, and satisfy the full-time residual and dissipation hypotheses in (N1). The physical residual remains \(R\), the normalized residual is \(R/\nu\), and physical damping is \(\lambda=\nu\sigma>0\). Both exponents retain the D-type definitions in Section 5. These assumptions are required for each application; the condition on the pricing kernel does not prove stochastic-model existence or extend the verified Riccati regularity domain.

For a real curve \(\xi\in AC[0,T]\) with \(\xi(0)=V_0\ge0\), the precise sufficient condition is

\[
q_\alpha=V_0g_{1-\alpha}+g_{1-\alpha}*\xi'\ge0
\quad\text{a.e.},\qquad g_\beta(t)=t^{\beta-1}/\Gamma(\beta).
\tag{FQ1}
\]

No sign is imposed on \(\xi'\). Indeed, \(A_\alpha=I^{1-\alpha}\xi=V_0g_{2-\alpha}+g_{2-\alpha}*\xi'\) is absolutely continuous, \(A_\alpha(0)=0\), and

\[
\|q_\alpha\|_1\le
\frac{T^{1-\alpha}}{\Gamma(2-\alpha)}(V_0+\|\xi'\|_1),
\qquad g_\alpha*q_\alpha=\xi.
\tag{FQ2}
\]

Absolute Fubini proves the second identity even for signed \(\xi'\), using \(g_\alpha*g_{1-\alpha}=g_1\). The initial term \(V_0g_{1-\alpha}\) cannot be dropped. Condition (FQ1) implies \(\xi\ge0\). Hence the entire proof of Theorem 9.2 continues to hold: integration by parts gives \(L_T-\widehat L_T=\nu^{-1}(q_\alpha*e)(T)\), and the positive resolvent identity gives

\[
0\le q_\alpha*k_\lambda
=\xi-\lambda\xi*k_\lambda\le\xi.
\tag{FQ3}
\]

The Fubini step for the exponent is bounded by \(\|\xi\|_\infty T^{1-\alpha}\|e'\|_1/\Gamma(2-\alpha)\); its boundary terms vanish because \(e(0)=A_\alpha(0)=0\). The AC Caputo convexity and the positive zero-initial-value inverse remain the prior tools [LiLiu2018, Kopteva2021v2]. The finite-history convolution, cell-weight bound (N6), and outward node-radius construction therefore remain valid under (FQ1). Cells still carry the complete Caputo history.

This is a strict relaxation of a sufficient curve condition, not a necessary condition for every conceivable certificate. If \(q_\alpha\) changes sign, the safe general estimate is \(\nu^{-1}(|q_\alpha|*k_\lambda*R)(T)\); the positive collapse to \(\xi*R\) cannot be used without further proof. Fractional forward-variance representations and their model-admissibility restrictions already occur in [ElEuchRosenbaum2017v1, Proposition 3.1 and Corollary 3.3]. Our analytical condition does not replace those restrictions.

**Corollary 9.4 (a decreasing analytical curve).** Let \(V_0>0\), \(c>0\), and \(\xi(t)=V_0(1-ct)\). Then

\[
q_\alpha(t)=\frac{V_0t^{-\alpha}}{\Gamma(1-\alpha)}
\left(1-\frac{ct}{1-\alpha}\right).
\tag{FQ4}
\]

Thus (FQ1) holds on \((0,T)\) if and only if \(cT\le1-\alpha\), including equality. In that case \(\xi(T)\ge\alpha V_0>0\) despite \(\xi'<0\).

**Proof.** Convolving the constant derivative \(-V_0c\) with \(g_{1-\alpha}\) gives \(-V_0c\,t^{1-\alpha}/\Gamma(2-\alpha)\). Adding the initial term and using \(\Gamma(2-\alpha)=(1-\alpha)\Gamma(1-\alpha)\) proves (FQ4). Its bracket is nonnegative exactly under the stated condition. ∎

This example is analytical and has not been used as a new financial experiment or asserted to be a realized rough-Heston variance curve. Positivity of the curve alone is insufficient for (FQ1): \(1-\alpha<cT<1\) leaves \(\xi>0\) but gives a negative kernel near maturity.

**Corollary 9.5 (explicit constant-curve propagation).** Under Theorem 9.2's state hypotheses, let \(\xi\equiv V_0\ge0\). Then

\[
q_\alpha*k_\lambda=V_0E_\alpha(-\lambda t^\alpha),\qquad
|L_T-\widehat L_T|\le
\frac{V_0}{\nu}\int_0^T
E_\alpha(-\lambda(T-s)^\alpha)R(s)\,ds.
\tag{FQ5}
\]

If \(R\le\nu\delta_F\), a closed-form upper bound is

\[
\eta_{\rm ML}=V_0\delta_F T E_{\alpha,2}(-\nu\sigma T^\alpha)
\le\min\left\{
V_0\delta_F T,
\frac{V_0\delta_F T^{1-\alpha}}{\nu\sigma\Gamma(2-\alpha)}
\right\}.
\tag{FQ6}
\]

**Proof.** Termwise convolution in the absolutely locally integrable Mittag--Leffler series gives \(g_{1-\alpha}*k_\lambda=E_\alpha(-\lambda t^\alpha)\); termwise integration gives \(\int_0^T E_\alpha(-\lambda t^\alpha)dt=T E_{\alpha,2}(-\lambda T^\alpha)\). Equation (FQ3) gives \(0\le E_\alpha\le1\), proving the first comparison. Also \(\int_0^tk_\lambda=(1-E_\alpha(-\lambda t^\alpha))/\lambda\le1/\lambda\). The state envelope \(|e|\le\delta_F/\sigma\), followed by the positive \(q_\alpha\) integral, proves the second comparison. ∎

The explicit bound retains finite history and physical scaling. It may be intersected with earlier independently valid exponent bounds only when all bound the same D-type target and reference. A substitution-based reference requires its separately certified residual conversion. This corollary is analytical; it does not assert that a Mittag--Leffler weighted propagation routine has been numerically implemented or that a new model instance has been certified.

**Proposition 9.6 (nonzero omitted-node reference at an unchanged fast output).** Fix the actual fast output, including its zero contribution at omitted finite nodes. For the same finite pricing map, select a possibly nonzero reference \(\psi_n\) at those nodes, and prove \(|\phi_n-\psi_n|\le\rho_n\). Let \(\bar c'=c_0+\Re(A\psi)\), \(d'=\bar c'-c^{\rm fast}\), and let \(\mathcal R\) include the complete strip, true infinite tail, and newly enclosed reference arithmetic. Then

\[
c^*-c^{\rm fast}\in d'
+\{\Re(Az):|z_n|\le\rho_n\}\oplus\mathcal R.
\tag{FQ7}
\]

For a symmetric remainder and direction \(w\), the complete absolute budget uses

\[
DF\left(|w^\top d'|+
\sum_n\rho_n\left|\sum_iw_ia_{in}\right|
+h_{\mathcal R}(w)\right)\le\tau.
\tag{FQ8}
\]

For a nonsymmetric remainder, both support directions must be bounded. A changed reference centre does not change the fixed fast output, but it does change \(d'\) and requires new centre arithmetic.

**Proof.** Subtract and add the new finite reference in the exact finite pricing map; its transform error is \(z=\phi-\psi\). The complete remainder contains the other discrepancies. Directional support of the shared complex disks gives (FQ8). ∎

An old zero-centred certificate \(|\phi_n|\le\varepsilon_n^0\) and a new certificate centred at \(\psi_n\) cannot have their radii directly minimized. At the new centre, the old certificate only gives \(|\phi_n-\psi_n|\le\varepsilon_n^0+|\psi_n|\). A safe radius is therefore \(\min\{\rho_n,\varepsilon_n^0+|\psi_n|\}\), or one can retain the two transform disks' intersection. A new disk is nested in the old disk only if \(|\psi_n|+\rho_n\le\varepsilon_n^0\). Otherwise, independently valid complete price intervals may still be intersected, but same-centre monotonicity is not automatic. For example, \(\phi=0\) lies in \(D(0,.1)\) and \(D(1,2)\), but not in \(D(1,\min(.1,2))\). Marginal and joint comparisons must use the same updated centre, node radii, and complete remainder. Any additional reference evaluation and certification is part of the reported cost.
