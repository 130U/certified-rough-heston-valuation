### C.5. Strict dissipative weights and the nonexpansive boundary

Retain the full assumptions and AC comparison proof of Theorem 3.3, but allow \(\sigma\ge0\). The regularized error modulus satisfies \(D_C^\alpha v_\varepsilon+\nu\sigma v_\varepsilon\le R\) almost everywhere. The same positive inverse applies when \(\lambda=\nu\sigma=0\): \(k_0=g_\alpha\). Passing to the continuous endpoint and then composing with the pricing functional gives (KR01)–(KR02). In particular the zero-damping assertion introduces no \(1/\sigma\). The initial contribution \(V_0g_{1-\alpha}\) in \(q_\alpha\) and the factor \(\nu^{-1}\) are unchanged.

**Proposition (a rigorous cumulative-weight series).** Suppose
\(0<\alpha,A_0<1\), \(0\le V_0\le\theta\), and the fixed curve is
\(\xi(t)=\theta+(V_0-\theta)E_{A_0}(-\lambda_\xi t^{A_0})\), with \(\lambda_\xi\ge0\). Retain \(q_\alpha\ge0\). For \(\lambda\ge0\) and \(\lambda T^\alpha<1\), (KR03) holds on \([0,T]\). If it is truncated before index \(M\), the entire omitted outer series satisfies

\[
\left|W_\lambda(t)-\sum_{n=0}^{M-1}(-\lambda)^nW_n(t)\right|
\le
\frac{\theta t(\lambda t^\alpha)^M}{1-\lambda t^\alpha},
\quad
W_n(t)=\int_0^t(\xi*g_{n\alpha})(s)\,ds.
\tag{KR10}
\]

Here \(g_0\) denotes the identity convolution, so \(W_0(t)=\int_0^t\xi\).

**Proof.** The existing resolvent identity \(k_\lambda+\lambda g_\alpha*k_\lambda=g_\alpha\), together with \(q_\alpha*g_\alpha=\xi\), gives
\(K_\lambda+\lambda g_\alpha*K_\lambda=\xi\). The Neumann series has terms
\((- \lambda)^n(\xi*g_{n\alpha})\). Since \(0\le\xi\le\theta\),

\[
0\le W_n(t)\le
\frac{\theta t^{1+n\alpha}}{\Gamma(2+n\alpha)}
\le\theta t(t^\alpha)^n.
\tag{KR11}
\]

Log convexity and \(\Gamma(1)=\Gamma(2)=1\) imply that \(\Gamma\) is increasing and at least one on \([2,\infty)\). Every outer denominator argument is \(2+n\alpha\ge2\). Thus the sum of the \(L^1(0,T)\) norms of the absolute terms is bounded by the convergent geometric series in (KR11). This justifies convolution, integration and interchange, proves the Volterra identity and its unique resolvent solution, and gives (KR10) with the first omitted index exactly \(n=M\). In particular twelve retained terms omit \(n\ge12\), rather than \(n\ge13\).

For uniqueness, the difference \(h\in L^1(0,T)\) of two solutions satisfies \(h=-\lambda g_\alpha*h\). Iterating gives \(\|h\|_1\le\lambda^nT^{n\alpha}\|h\|_1/\Gamma(1+n\alpha)\). For sufficiently large \(n\), the Gamma argument is at least two, and the right-hand factor is at most \((\lambda T^\alpha)^n\), which tends to zero. Thus \(h=0\). This argument does not assume an unjustified one-step contraction involving \(\Gamma(1+\alpha)\).

Expanding the curve Mittag–Leffler function, and using the beta convolution identity, gives

\[
W_n(t)=t^{1+n\alpha}
\left[
\frac{\theta}{\Gamma(2+n\alpha)}
+(V_0-\theta)\sum_{m=0}^{\infty}
\frac{(-\lambda_\xi t^{A_0})^m}
{\Gamma(2+n\alpha+mA_0)}
\right].
\tag{KR12}
\]

When \(w=\lambda_\xi t^{A_0}<1\), every inner denominator also has argument at least two, and its tail before index \(L\) is bounded by

\[
\left|\sum_{m=L}^{\infty}
\frac{(-w)^m}{\Gamma(2+n\alpha+mA_0)}\right|
\le \frac{w^L}{1-w}.
\tag{KR13}
\]

The tails are absolute enclosures; no unproved alternating-series monotonicity is needed. The actual curve and damping satisfy the strict interval checks \(w<1\) and \(\lambda T^\alpha<1\). Signed coefficients, including \(V_0-\theta\), are multiplied by outward intervals before addition. Every power, Gamma value and exponential is enclosed by the identified dyadic primitives. ∎

For a residual envelope \(R\le R_j\) on the complete cell \([a_j,b_j]\), evaluate strict cumulative intervals \([W^-(t),W^+(t)]\). Its exact weight lies in

\[
\left[
W^-(T-a_j)-W^+(T-b_j),\
W^+(T-a_j)-W^-(T-b_j)
\right].
\tag{KR14}
\]

Intersecting with nonnegativity and the independently proved upper curve weight is valid because \(0\le K_\lambda\le\xi\). The resulting upper endpoint \(\omega_j^+\) gives

\[
\eta_{\rm res}\le\nu^{-1}\sum_jR_j\omega_j^+.
\tag{KR15}
\]

Every bin envelope is the maximum over all intersecting closed source cells, including endpoint intersections. Source cells still start at zero and cover the full interval; no Caputo history is restarted.

The producer evaluates \(W_n\) through the existing strict power-field moment divided by \(\Gamma(1+n\alpha)\), retaining twelve outer terms. The separate reader evaluates (KR12) directly, retaining fourteen outer terms and sixty-four inner terms, without importing the producer's cumulative function or the power-field-moment function. It verifies that the claimed residual-functional enclosure contains its tighter independent enclosure, and checks all transform-radius minima and full prices. The Gamma, logarithm, exponential and dyadic coefficient primitives remain shared dependencies; the upstream residual proof is inherited rather than independently rederived.
