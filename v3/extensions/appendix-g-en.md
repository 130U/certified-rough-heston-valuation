## Appendix G. Nonexact trial fields and the signed error identity

This appendix extends the continuous–discrete comparison to one deterministic trial field that need not solve the backward equation. It states sufficient conditions independently of the unknown exact solution, proves the four signed terms, and gives an explicit globally integrable nonexact field. Expectations below are undiscounted; multiply the identity and its bounds by the common discount factor when converting a payoff to a price.

### G.1. State, traces, and admissibility

Use the original laws \(P,Q\), parameters, and correlated positive-part update of Appendix F. Between monthly fixings the state is \(x=(s,v,A_m,\ell_m)\), where \(A_m\) is the sum of the realized normalized stock values and \(\ell_m\) the sum of their logarithms. The fixing map \(J_i\) adds the current \(s,\log s\) to these histories. Between fixings,

\[
\mathcal L=rs\partial_s+(d-\kappa v)\partial_v
+\tfrac12vs^2\partial_{ss}+\rho\xi vs\partial_{sv}
+\tfrac12\xi^2v\partial_{vv}.\tag{G01}
\]

Choose one fixed nonnegative weight for the entire horizon, for example

\[
\begin{aligned}
W&=e^v\{s^{-1/2}+e^{-\ell_m/24}s^{-(12-m)/24}\},\\
W^{\rm nat}&=e^v\{\mathfrak B_m^{-1/2}+\mathfrak G_m^{-1/2}\},\qquad
\mathfrak B_m=(A_m+(12-m)s)/12,\quad
\mathfrak G_m=e^{\ell_m/12}s^{(12-m)/12}.
\end{aligned}\tag{G02}
\]

Both weights match exactly across the fixing map. Since the arithmetic mean is at least the geometric mean, \(W^{\rm nat}\le2e^v\mathfrak G_m^{-1/2}\). The history factors in both weights are multidate nonpositive real loadings with total absolute value at most \(1/2\).

**Lemma (weight moments).** At \(\theta_*\), over \(0\le t\le1\), either weight satisfies

\[
\sup_tE_PW(t,X_t)<5/2,\qquad \max_jE_QW(t_j,X_j)<5/2,
\qquad \sup_{\tau\le1}E_PW(\tau,X_\tau)^2<\infty.\tag{G03}
\]

The last supremum is over the compact-localization stopping times used below. To prove the first bound for a branch, use the generator on \(e^{L+pZ+V}\), with \(p\in[-1/2,0]\). Its variance coefficient is \(\gamma_p-\kappa_p+\xi^2/2<0\), and its constant drift is \(rp+d\le d\). Loading changes cancel at fixings. Nonnegative stopped supermartingales give branch expectation at most \(e^{v_0+d}=e^{9/50}<5/4\). For the discrete law, (F10)–(F11) with \(B=1\) and \(F_p(1)\le1\) give a branch bound \(e^{v_0+d+1/300}=e^{11/60}<5/4\). Sum two branches, or use \(W^{\rm nat}\le2e^v\mathfrak G_m^{-1/2}\). The strict comparisons follow from \(\log(5/4)\ge1/5\).

For the squared bound, \((a+b)^2\le2(a^2+b^2)\). Each squared branch has total stock loading at most one and variance loading two. Increasing the latter to four dominates it; the continuous exponential-supermartingale variance coefficient is bounded by \(1-4(1.776)+8(7/25)^2<0\), with constant drift at most \(24/25\). Stopping therefore gives a uniform finite second moment. The same argument covers the natural weight. This is enough for uniform integrability of fields dominated by \(W\); no ordinary martingale assumption on the stopped limiting stochastic integral is needed.

Let \(R\) be the same terminal payoff, or the same exact finite conversion remainder, under both laws. The deterministic field \(\widetilde u\) is locally \(C^{1,2}\) between fixings, admits a right-sided extension at \(v=0\) suitable for Itô's formula, and has genuine one-sided traces uniformly on compact state sets. Require global bounds

\[
\begin{aligned}
|\widetilde u|&\le CW,&
|\mathfrak r(t,x)|&\le\eta_c(t)W(t,x),& \int_0^1\eta_c(t)dt&<\infty,\\
|d_i(x)|&\le\eta_iW(t_i-,x),&
|\delta(x)|&\le\eta_TW(1,x),& C,\eta_i,\eta_T&<\infty.
\end{aligned}\tag{G04}
\]

Domination includes all states, \(v=0\), and the unbounded tail. Define

\[
\begin{aligned}
\mathscr D_j&=Q_j\widetilde u_{j+1}-\widetilde u_j,&
\mathfrak r&=(\partial_t+\mathcal L)\widetilde u,\\
d_i(x)&=\widetilde u(t_i-,x)-\widetilde u(t_i+,J_ix),&
\delta&=R-\widetilde u_N.
\end{aligned}\tag{G05}
\]

The jump defect is **left trace minus right trace after the fixing**. The operator \(Q_j\) includes the original kernel and any fixing at the end of the step. Use the same post-fixing terminal convention in both laws, and count each update once. The defects \(\mathscr D_j\) must be integrable under the original \(Q\); a valid full-horizon enclosure is \(\sum_jE_Q\mathscr D_j\in[L_Q,U_Q]\). A sufficient alternative is \(\lvert\mathscr D_j\rvert\le h\eta_{Q,j}W\).

These conditions do not define admissibility by assuming the desired error bound. An exact future-value field belongs to this class only when the stated regularity and domination are verified. A finite representation also belongs only after its growth, residuals, traces, terminal value, and original-kernel interface have been verified.

### G.2. The four-term signed identity

**Theorem (one-field residual identity).** Under (G03)–(G05) and the integrable original-\(Q\) defects,

\[
\boxed{E_QR-E_PR=
\sum_jE_Q\mathscr D_j-E_P\int_0^1\mathfrak r(t,X_t)dt
+\sum_iE_Pd_i+(E_Q-E_P)\delta.}\tag{G06}
\]

**Proof.** Finite conditional telescoping under \(Q\) gives

\[
E_Q\widetilde u_N-\widetilde u_0=\sum_jE_Q\mathscr D_j.\tag{G07}
\]

For \(P\), localize in compact state domains, on closed subintervals away from fixings. Itô's formula then has a stochastic integral of expectation zero. The second-moment bound in (G03) and \(|\widetilde u|\le CW\) make the stopped field values uniformly integrable, so they converge in \(L^1\) when stopping is removed. Tonelli and (G04) give \(E_P\int|\mathfrak r|\le\int\eta_c(t)E_PW(t,X_t)dt<\infty\), which removes stopping from the time integral by absolute integrable domination. As the subinterval endpoints approach a fixing, compact-uniform genuine traces and continuous paths give almost-sure trace convergence; the same uniform integrability gives \(L^1\) convergence. The actual field jump is \(-d_i\). Summing all intervals and jumps therefore gives

\[
E_P\widetilde u_N-\widetilde u_0
=E_P\int_0^1\mathfrak r(t,X_t)dt-\sum_iE_Pd_i.\tag{G08}
\]

Subtract (G08) from (G07), and add the two terminal defects \(\delta=R-\widetilde u_N\). The common deterministic initial value cancels, giving (G06). The argument also includes a fixing at the terminal date using the specified post-fixing convention. ∎

If one instead defines \(J_i^{\rm jump}=\widetilde u(t_i+,J_ix)-\widetilde u(t_i-,x)\), its term in (G06) is \(-\sum_iE_PJ_i^{\rm jump}\). This explicit sign convention avoids mixing the two definitions. For an exact continuation, the backward residual, fixing defects, and terminal discrepancy vanish, recovering (F08). For a nonexact field all four signed terms remain.

### G.3. Effective sufficient bounds

At \(\theta_*\), (G06) and the moment lemma imply

\[
\begin{aligned}
|E_QR-E_PR|&\le\max(|L_Q|,|U_Q|)
+\tfrac52\left(\int_0^1\eta_c(t)dt+\sum_i\eta_i\right)+5\eta_T,\\
|E_QR-E_PR|&\le\tfrac52\left(h\sum_j\eta_{Q,j}
+\int_0^1\eta_c(t)dt+\sum_i\eta_i\right)+5\eta_T
\quad\text{if }|\mathscr D_j|\le h\eta_{Q,j}W.
\end{aligned}\tag{G09}
\]

These are sufficient nonnegative bounds obtained by the triangle inequality. A joint signed enclosure of the four contributions can instead be propagated by its linear image. Separate price intervals alone supply no shared-state compatibility witness. In particular, a necessary lower bound on a residual envelope is not an evaluation of either sufficient upper bound in (G09).

### G.4. A self-contained nonexact analytic field

Fix \(T=1\), \(\varepsilon>0\), and \(R=s_T^{-1/2}\). Consider

\[
a_\varepsilon(t)=1+\varepsilon t(1-t),\qquad
\widetilde u_\varepsilon(t,x)=a_\varepsilon(t)s^{-1/2},\qquad
1\le a_\varepsilon\le C_\varepsilon:=1+\varepsilon/4.\tag{G10}
\]

Use \(W_A=s^{-1/2}e^v\), which is a single branch of the preceding weight proof. The field is globally regular for \(s>0,v\ge0\), is independent of the histories, has exact matching fixing traces and terminal value, and obeys \(|\widetilde u_\varepsilon|\le C_\varepsilon W_A\). Its generator residual is

\[
\mathfrak r_\varepsilon=s^{-1/2}
\{\varepsilon(1-2t)+a_\varepsilon(t)(3v/8-r/2)\}.\tag{G11}
\]

Because \(ve^{-v}\le1/e\), a global dominating function, constant in time, is

\[
\eta_c=\varepsilon+C_\varepsilon(r/2+3/(8e)),\qquad
\int_0^1\eta_c(t)dt=\eta_c<\infty,\qquad \eta_i=\eta_T=0.\tag{G12}
\]

The original stock Gaussian integral is exact even though the stock and variance share \(G\): this field does not depend on next-step variance. It gives

\[
\mathscr D_j=s^{-1/2}\{a_\varepsilon(t_{j+1})e^{h(3v/8-r/2)}-a_\varepsilon(t_j)\},\qquad
|\mathscr D_j|\le h\eta_QW_A,\quad
\eta_Q=\varepsilon+C_\varepsilon\{r/2+3/[8e(1-3h/8)]\}.\tag{G13}
\]

For the bound, write the difference as \((a_{j+1}-a_j)e^{h(3v/8-r/2)}+a_j(e^{h(3v/8-r/2)}-1)\). Use \(|a_{j+1}-a_j|\le\varepsilon h\), \(|e^x-1|\le|x|e^{\max(x,0)}\), and \(ve^{-cv}\le1/(ec)\) for \(c=1-3h/8>0\). Thus every discrete defect is integrable, with the explicit full-horizon enclosure \(\sum_jE_Q\mathscr D_j\in[-(5/2)\eta_Q,(5/2)\eta_Q]\), because \(Nh=1\). Substitution into (G09) gives the finite sufficient bound \((5/2)(\eta_Q+\eta_c)\).

At \(t=1/2,v=r>0\), (G11) equals \(-rC_\varepsilon s^{-1/2}/8<0\). Therefore this field is not the exact future-value function. The exact field for the same negative-power payoff exists by the affine continuation and moment proof of Appendix F, with loading \(-1/2\). The same admissible object class contains both exact and nonexact fields; the four-term identity applies to each. This example is an analytic scope witness, not a numerical certificate for the original market instruments.

### G.5. What the thirteen-function diagnostic does and does not certify

The saved classical trial-field diagnostic has a distinct, conditional role. With \(n=12-m\), \(B=(A_m+ns)/12\), \(y=A_m/(A_m+ns)\), \(\beta=1-y\), and \(z=v/(1+v)\), its branch is \(B^{-q}P(y,v)\). In this subsection \(\Re q=1/2\), so \(B^{-q}\) corresponds to negative stock damping; this \(q\) is not the negative loading \(q\) used in Appendix F. The conjugated generator is

\[
\begin{aligned}
\mathcal L_qP={}&-ry\beta P_y+dP_v-qr\beta P\\
&+v\{\tfrac12y^2\beta^2P_{yy}-\rho\xi y\beta P_{yv}
+\tfrac12\xi^2P_{vv}+(1+q)y\beta^2P_y\\
&\hspace{12mm}-(\kappa+q\rho\xi\beta)P_v+\tfrac12q(q+1)\beta^2P\}.
\end{aligned}\tag{G14}
\]

The basis consists of \(\phi_{ij}=\beta y^iz^j\), \(0\le i\le2,0\le j\le3\), and \(\psi=v\beta^2\). It exactly represents the terminal forcing \(\mathcal L_q1=-qr\phi_{00}+q(q+1)\psi/2\). This is completion of the terminal generator, not closure under every generator image. For finite endpoint constants, the field uses cubic Hermite interpolation with exact physical slopes \(-Kc-g(q)\), where \(g(q)=-qr e_{00}+q(q+1)e_\psi/2\). The exact fixing carry, with \(\gamma=(n-1)/n\), is

\[
(T_nc)_{\ell j}=\gamma\sum_{i=\ell}^2\binom i\ell\gamma^\ell n^{-i+\ell}c_{ij},
\qquad T_n\psi=\gamma^2\psi.\tag{G15}
\]

It follows from \(y'=\gamma y+1/n\), \(B'=B\), and \(\beta'=\gamma\beta\). Terminal correction nodes are zero. Exact carries and slopes specify the traces; floating generation values do not replace these definitions. The finite field has \(|P|\le C_0+C_1v\le(C_0+2C_1/e)e^{v/2}\). Its continuous residual is a polynomial of degree at most two in \(v\) with bounded \(y,z\) coefficients, so \(e^{-v}|F|\le a_0+a_1/e+4a_2/e^2\). A complete application of (G09) still requires the actual coefficient bank, all-state original-\(Q\) envelopes, and full-horizon sufficient upper bounds.

For the saved first-month state \(m=0,y=0,v=9/200\), let \(w=(1,z,z^2,z^3,0,\ldots,0,v)\), \(\ell\) be the generator-value row of the basis, and \(\ell_0=-qr+q(q+1)v/2\). Exact integration over one piece gives

\[
\int F_{A,q}dt=
\left[w+\frac{h^2}{12}\ell K\right](c_R-c_L)
+\frac h2\ell(c_L+c_R)+h\ell_0.\tag{G16}
\]

Indeed \(\int c(t)dt=h(c_L+c_R)/2+h^2(s_L-s_R)/12\), and \(s_L-s_R=K(c_R-c_L)\). The archive contains all 3080 weighted complex integral intervals (385 modes and eight cells, covering the original 64 time pieces). At common phase zero, sum the real mode intervals on each cell, apply \(\int|F|\ge|\int F|\), and subtract the integrated geometric-branch upper bound. The exact aggregate is specified by the mathematical field `whole_lower` in `field-result.json`:

\[
\int_0^{1/12}\eta_c(t)dt\ge L_*,\qquad
L_*>0.003407444052031154>0.\tag{G17}
\]

This rejects the selected allocation \(\int\eta_c\le1/1000\), and retains the status `FAIL_SELECTED_INTEGRATED_PDE_CONTRACT_ONLY`. It does not reject every sufficient allocation, minimize over the trial space, or bound the actual signed price bias from below. The portable `verify_field_receipt.py` checks exact saved interval aggregation; it does not regenerate the absent coefficient bank or rerun the archived direct integration. Accordingly, (G17) is an archived-field necessary-condition diagnostic, while the explicit field (G10) independently proves nonexact admissibility without that bank. No complete annual monetary PASS is inferred.

The machine appendix uses `baseline/english-heston-release/code/classical/field-cell-integrals.json`, `field-result.json`, `field-independent-readback.json`, `provenance.json`, and `verify_field_receipt.py`, with publication manifests fixing their scientific identities. Contact, environment, and execution-measurement metadata are unnecessary to these mathematical assertions.
