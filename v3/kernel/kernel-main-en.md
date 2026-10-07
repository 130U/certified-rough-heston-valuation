### Strict computation of the dissipative pricing kernel

The positive kernel in Theorem 3.3 can be computed rather than replaced by its curve upper bound. For \(\sigma\ge0\), set \(\lambda=\nu\sigma\) and

\[
K_\lambda=q_\alpha*k_\lambda,\qquad
\eta_{\rm res}=\nu^{-1}(K_\lambda*R)(T),\qquad
0\le K_\lambda=\xi-\lambda\,\xi*k_\lambda\le\xi.
\tag{KR01}
\]

The complete residual history, zero state initial values, curve initial term and physical factor \(\nu^{-1}\) remain those of Theorem 3.3. The scalar inverse and its positivity are established tools [Kopteva2021v2, SimonCM2015]. The additional implementation here rigorously encloses the model's pricing-kernel weights and carries them through the same actual-output certificate.

**Corollary (nonexpansive finite-history propagation).** Theorem 3.3 remains valid with \(\sigma\ge0\). At \(\sigma=0\),

\[
k_0=g_\alpha,\qquad K_0=\xi,\qquad
|L_T-\widehat L_T|\le\nu^{-1}(\xi*R)(T).
\tag{KR02}
\]

No reciprocal damping or infinite-horizon state radius is needed. The curve condition is \(q_\alpha\ge0\), not \(\xi'\ge0\); the stochastic-model hypotheses remain separate. The existing AC regularity bridge and full comparison proof are retained in Appendix C.

For the fixed curve in (2.4), write \(A_0=\alpha_0\) and \(\lambda_\xi\) for its own curve parameter. On the computational domain \(\lambda T^\alpha<1\), define

\[
W_\lambda(t)=\int_0^tK_\lambda(s)\,ds
=\sum_{n=0}^\infty(-\lambda)^n t^{1+n\alpha}
\left[
\frac{\theta}{\Gamma(2+n\alpha)}
+(V_0-\theta)E_{A_0,2+n\alpha}
(-\lambda_\xi t^{A_0})
\right].
\tag{KR03}
\]

A cell \([a_j,b_j]\) has weight \(W_\lambda(T-a_j)-W_\lambda(T-b_j)\). Appendix C provides the absolute series tails and interval-difference proof. The implementation uses twelve outer terms, sixty-four inner curve terms and 100-bit outward dyadic primitives. It is an enclosure of the full Mittag–Leffler kernel functional, with explicit truncation and rounding remainders; ordinary floating-point Mittag–Leffler values do not enter a guarantee.

**Change to Theorem 3.3.** Replace \(\sigma>0\) by \(\sigma\ge0\), leaving all state, residual, AC, initial-value, \(q_\alpha\), scaling and pricing-functional hypotheses intact. Its proof uses \(\lambda\ge0\), and the zero-damping inverse is \(I^\alpha\). Any separate global-state formula involving \(1/\sigma\) still requires \(\sigma>0\).
