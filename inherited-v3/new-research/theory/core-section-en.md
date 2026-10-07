### A single regularity bridge for the comparison argument

The scalar comparison mechanism is established fractional-calculus machinery. Li and Liu [LiLiu2018, Proposition 3.11(ii)] give convexity after regularization and passage to a distributional limit. Their Proposition 4.12 concerns specified vector gradient and Hamiltonian flows. Kopteva [Kopteva2021v2, Lemma 2.8 and Theorem 2.2] uses norm convexity and a positive fractional inverse under positive-time Lipschitz hypotheses. The following elementary bridge proves the vector \(AC\) version consumed here directly, including the terminal-time conclusion. It is an adaptation of those tools, not a new general Caputo comparison theorem.

**Regularity lemma (AC convexity and the continuous endpoint).** Let \(0<\alpha<1\), \(T>0\), \(v\in AC([0,T];\mathbb R^d)\), and let \(\Phi\in C^1(\mathbb R^d)\) be convex. With \(D_C^\alpha v=g_{1-\alpha}*v'\),

\[
D_C^\alpha\Phi(v)\le \nabla\Phi(v)\cdot D_C^\alpha v
\quad\text{a.e. on }(0,T).
\tag{AC1}
\]

Let \(u\in AC[0,T]\), \(u(0)=0\), \(\lambda\ge0\), and \(R\in L^\infty(0,T)\) be nonnegative. If \(D_C^\alpha u+\lambda u\le R\) almost everywhere, then

\[
u(t)\le(k_\lambda*R)(t),\qquad 0\le t\le T,
\quad k_\lambda(t)=t^{\alpha-1}E_{\alpha,\alpha}(-\lambda t^\alpha).
\tag{AC2}
\]

**Proof.** Choose smooth \(f_n\to v'\) in \(L^1(0,T)\), and set \(v_n(t)=v(0)+\int_0^t f_n(s)\,ds\). Then \(v_n(0)=v(0)\), \(v_n\to v\) uniformly, and \(v_n'\to v'\) in \(L^1\). For a smooth path, integration by parts expresses the difference between the two sides of (AC1) as

\[
\frac{1}{\Gamma(1-\alpha)}\left[
\frac{B_\Phi(v_n(0),v_n(t))}{t^\alpha}
+\alpha\int_0^t\frac{B_\Phi(v_n(s),v_n(t))}{(t-s)^{1+\alpha}}\,ds
\right]\ge0,
\tag{AC3}
\]

where \(B_\Phi(a,b)=\Phi(a)-\Phi(b)-\nabla\Phi(b)\cdot(a-b)\ge0\). Smooth paths are locally Lipschitz. A gradient bound \(M\) on the compact path range and a local path Lipschitz constant \(L\) give \(B_\Phi(v_n(s),v_n(t))\le2ML|t-s|\). The endpoint kernel \((t-s)^{-\alpha}\) is therefore integrable. The supporting-hyperplane inequality may first be integrated with history truncated at \(t-\delta\), and the classical Caputo integrals converge as \(\delta\downarrow0\).

All path ranges lie in one compact set. Continuity of \(\nabla\Phi\) and the ordinary \(AC\) composition rule give

\[
\|\Phi(v_n)' - \Phi(v)'\|_1\to0,
\qquad
\|D_C^\alpha(v_n-v)\|_1
\le\frac{T^{1-\alpha}}{\Gamma(2-\alpha)}\|v_n'-v'\|_1\to0.
\tag{AC4}
\]

The same convolution estimate applies to \(\Phi(v_n)-\Phi(v)\). Moreover, the products \(\nabla\Phi(v_n)\cdot D_C^\alpha v_n\) converge in \(L^1\) to the corresponding product for \(v\). Passing to an almost-everywhere convergent subsequence proves (AC1). This uses the ordinary composition rule only for the first derivative inside \(AC\); no Caputo chain rule is asserted.

For (AC2), put \(f=D_C^\alpha u+\lambda u\in L^1(0,T)\). The zero initial value gives \(u+\lambda g_\alpha*u=g_\alpha*f\). The locally convergent resolvent series, whose \(n\)-th term has \(L^1(0,T)\) norm bounded by \(\lambda^{n-1}T^{n\alpha}/\Gamma(1+n\alpha)\), gives \(u=k_\lambda*f\) almost everywhere. Complete monotonicity of \(E_{\alpha,\alpha}(-x)\) [SimonML2015] supplies \(k_\lambda\ge0\), so \(f\le R\) implies \(u\le k_\lambda*R\) almost everywhere. The convolution on the right is continuous: extend \(k_\lambda\) and \(R\) by zero, and use \(L^1\) translation continuity of the kernel with the \(L^\infty\) bound on \(R\). Its value at zero is zero. Since \(u\) is continuous, an almost-everywhere inequality extends to every point of \([0,T]\), including maturity. ∎

### The central finite-history pricing theorem

The model-specific step is the composition of the dissipative complex Riccati error with the derivative-based Heston pricing functional. The complete history remains attached to the initial time; the result applies to any fixed reference that satisfies the stated certificate hypotheses, independently of how the production Padé output is computed.

**Theorem 3.3 (finite-history pricing envelope; formerly Theorem 9.2).** Let \(0<\alpha<1\), \(\nu>0\), \(T>0\), and \(Z,\widehat Z\in AC([0,T];\mathbb C)\) have zero initial value. Let

\[
D_C^\alpha Z=\nu F(Z),\quad
r=D_C^\alpha\widehat Z-\nu F(\widehat Z),\quad
|r|\le R\in L^\infty(0,T),\qquad R\ge0,
\tag{N1}
\]

where \(F(z)=-b+dz+z^2/2\), \(\Re d=-s_0\), \(\Re Z\le0\), \(\Re\widehat Z\le\epsilon_R\), and \(\sigma=s_0-\epsilon_R/2>0\). These equations and inequalities hold almost everywhere; the state bounds hold everywhere by continuity. Let \(\xi\in AC[0,T]\), \(\xi(0)=V_0\ge0\), and assume

\[
q_\alpha=(I^{1-\alpha}\xi)'
=V_0g_{1-\alpha}+g_{1-\alpha}*\xi'\ge0\quad\text{a.e.}
\tag{N5}
\]

Define \(L_T\) and \(\widehat L_T\) from \(\nu^{-1}\int_0^T\xi(T-t)D_C^\alpha Z(t)\,dt\) and the same expression with \(\widehat Z\). With \(\lambda=\nu\sigma\),

\[
|Z-\widehat Z|\le k_\lambda*R,
\qquad
|L_T-\widehat L_T|
\le\nu^{-1}(q_\alpha*k_\lambda*R)(T)
\le\nu^{-1}(\xi*R)(T).
\tag{N2}
\]

In particular, \(R/\nu\le\delta_F\) implies

\[
|L_T-\widehat L_T|\le\delta_F\int_0^T\xi(s)\,ds.
\tag{N3}
\]

**Proof.** For \(e=Z-\widehat Z\), the divided difference gives \(D_C^\alpha e=\nu[d+(Z+\widehat Z)/2]e-r\), with coefficient real part at most \(-\lambda\). Apply the regularity lemma to \(v_\varepsilon=(|e|^2+\varepsilon^2)^{1/2}-\varepsilon\). Since \(\nabla v_\varepsilon\cdot e=|e|^2/(|e|^2+\varepsilon^2)^{1/2}\ge v_\varepsilon\) and \(|\nabla v_\varepsilon|\le1\),

\[
D_C^\alpha v_\varepsilon+\lambda v_\varepsilon\le R\quad\text{a.e.}
\tag{N4}
\]

Equation (AC2) and the limit \(\varepsilon\downarrow0\) yield the first state inequality at every time. Absolute Fubini gives \(I^{1-\alpha}\xi=V_0g_{2-\alpha}+g_{2-\alpha}*\xi'\), whose derivative is \(N5\), and \(g_\alpha*q_\alpha=\xi\). In particular, \(q_\alpha\in L^1\) and \(\xi\ge0\). Writing \(A_\alpha=I^{1-\alpha}\xi\), another absolute Fubini step followed by \(AC\) integration by parts gives

\[
L_T-\widehat L_T
=\nu^{-1}\int_0^TA_\alpha(T-t)e'(t)\,dt
=\nu^{-1}(q_\alpha*e)(T).
\tag{CP1}
\]

The first Fubini integral is bounded by \(\|\xi\|_\infty T^{1-\alpha}\|e'\|_1/\Gamma(2-\alpha)\); the boundary terms vanish because \(A_\alpha(0)=e(0)=0\). Positivity now proves the first exponent estimate. Finally, \(g_\alpha-k_\lambda=\lambda g_\alpha*k_\lambda\ge0\), whence

\[
0\le q_\alpha*k_\lambda
=\xi-\lambda\xi*k_\lambda\le\xi.
\tag{CP2}
\]

Associativity and nonnegative integration yield the remaining conclusions. The physical residual is \(R\), so its factor \(\nu^{-1}\) remains until \(R/\nu\le\delta_F\) is used. ∎

The novelty claimed here is the explicit Heston pricing-functional connection, its certified cell weights and its inclusion in the complete error of a frozen numerical output. Convexity, resolvent positivity, disk support functions and unit-cost sorting are prior tools. The hypothesis on \(q_\alpha\) is an analytical propagation condition; probability-model existence, the affine transform and the martingale property are checked separately.

For a full-history residual envelope \(R\le R_j\) on each closed cell \([a_j,b_j]\), the computable cell-weight version is

\[
|L_T-\widehat L_T|
\le\nu^{-1}\sum_jR_j\int_{a_j}^{b_j}(q_\alpha*k_\lambda)(T-s)\,ds
\le\nu^{-1}\sum_jR_j\int_{a_j}^{b_j}\xi(T-s)\,ds.
\tag{N6}
\]

The first weights may be used only when they are enclosed rigorously; the implemented experiments use the second weights. When a pricing partition intersects several source residual cells, its envelope is the maximum over every intersected closed cell. The Caputo history is never restarted at a cell boundary.
