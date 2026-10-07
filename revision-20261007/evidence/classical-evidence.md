# Classical Heston: mathematical evidence and portable certificates

This supplement supports Section 3 of the research report. It provides the probability constraints, one-step envelopes, and exact witnesses for terminal price-row separation, together with the contract and integral evidence for the thirteen-dimensional trial field. Small exact-arithmetic programs reproduce the probability and profile arrays and check the terminal witness. Trial-field evidence is supplied as saved mode-cell integrals and an archived direct-integration readback. The portable checks require no large coefficient bank, optimization problem, or pricing calculation.

## 1. Models and the common-probability mechanism

Write \(s=S/100=e^Z\), \(d=\kappa\bar v\), \(h=1/768\), and \(r=1/100\). The continuous model \(P_\theta\) is

\[
dZ=(r-V/2)\,dt+\sqrt V(\rho\,dW+\sqrt{1-\rho^2}\,dB),
\qquad dV=(d-\kappa V)\,dt+\xi\sqrt V\,dW.
\]

The actual discrete model \(Q_\theta\) uses independent standard normal \(G,H\) and

\[
Y=dh+(1-\kappa h)v+\xi\sqrt{hv}G,\quad V'=Y^+,\quad
Z'=z+rh-hv/2+\sqrt{hv}(\rho G+\sqrt{1-\rho^2}H).
\tag{C1}
\]

The same \(G\) drives stock and variance. The positive part is applied to the real Gaussian candidate, including its negative tail. For the common-moment argument,

\[
\kappa\in[2,4],\quad \bar v,v_0\in[3/100,3/50],\quad
\xi\in[9/50,7/25],\quad \rho\in[-4/5,-3/10].
\tag{C2}
\]

For a finite multi-date exponential mode, require every real loading to be nonpositive and their total absolute value to be at most \(1/2\). Let \(H_{ji}\) be its realized prefix, \(q_{ji}\) its remaining loading, and \(u_{ji}=e^{a_{ji}+b_{ji}v+q_{ji}z}\) its exact continuous continuation. The defect \(D_{ji}(v)\) is the actual \(Q\) propagation of the next continuation minus \(u_{ji}\), after removing the common factor \(e^{q_{ji}z}\). Then

\[
\Delta\Phi_i=\sum_jr_{ji},\qquad
r_{ji}=E_Q[H_{ji}e^{q_{ji}Z_j}D_{ji}(V_j)].
\tag{C3}
\]

These are identities of the original laws, with common original-chain variance probabilities.

### 1.1 Continuation and integrability

Between fixings, the affine coefficients solve

\[
b'=\tfrac12\xi^2b^2+(\rho\xi q-\kappa)b+\tfrac12(q^2-q),
\qquad a'=rq+db.
\tag{C4}
\]

At a fixing, the remaining loading changes and \(a,b\) continue without resetting. Starting from zero terminal coefficients, put \(q=p+i\omega\), \(\kappa_p=\kappa-p\rho\xi\), and \(\gamma_p=(p^2-p)/2\). On \(\Re b=1\), the real drift in (C4) is

\[
\tfrac12\xi^2-\kappa_p+\gamma_p
-\tfrac12\{(\xi\Im b+\rho\omega)^2+(1-\rho^2)\omega^2\}<0.
\]

Here \(p\in[-1/2,0]\), \(\kappa_p\ge1.888\), and \(\gamma_p\le3/8\). Thus \(\Re b\le1\). The radial bound

\[
\frac{d|b|}{dt}\le(\xi^2/2-\kappa_p)|b|+|q^2-q|/2
\]

prevents finite-time explosion on each finite continuation segment. Also \(\Re a\le(6/25)T\).

To identify this formal solution with a true expectation, multiply all real loadings by \(\eta=5/4\). Let \(p_*(t)\) and \(L_*(t)\) denote their remaining sum and realized prefix. The process

\[
\mathcal Y_t=\exp\{L_*(t)+p_*(t)Z_t+4V_t-(24/25)t\}
\]

is a nonnegative local supermartingale: its constant drift is nonpositive, and its variance drift is at most \(65/128-4(1.86)+8(7/25)^2<0\). Prefix and remaining-loading changes cancel at fixings. For the stopped affine local martingale \(\mathcal M\),

\[
|\mathcal M_\tau|^{5/4}
\le e^{(5/4)(6/25)T+(24/25)T}\mathcal Y_\tau.
\]

Compact stopping and the supermartingale inequality give a uniform \(5/4\)-moment bound. Uniform integrability removes stopping and proves the exact continuation and (C3), including finite starting states and \(v=0\).

### 1.2 Discrete exponential moment and common inclusion

For nonpositive real loadings of total absolute value at most one,

\[
E_Q\exp\left\{\sum_{n\le j}\beta_nZ_n+4V_j\right\}
\le K_j:=\exp\{6/25+(73/75)jh\}.
\tag{C5}
\]

For completeness, under real stock tilting with \(p\in[-1,0]\), the variance candidate has mean \(dh+\eta_pv\), where \(\eta_p=1-\kappa_ph\ge191/192\). The pointwise inequality \((-y)^+\le h(25e)^{-1}e^{-25y/h}\) gives

\[
E(-Y_p)^+
\le\frac{h}{25e}
\exp\left\{-25d+\frac{[-25\eta_p+(625/2)\xi^2]v}{h}\right\}
\le\frac{h}{25e^{5/2}}<h/300.
\tag{C6}
\]

This uses \(d\ge3/50\), \(-25\eta_p+(625/2)\xi^2\le-71/192\), and the positive Taylor lower bound \(e^{5/2}>12\). At \(v=0\) the actual negative part is zero. For \(B\ge0\), \(e^{BY_p^+}\le e^{BY_p}+B(-Y_p)^+\). If \(F_p(B)=\gamma_ph+\eta_pB+\xi^2hB^2/2\), Gaussian integration gives

\[
E_Q[e^{pZ'+BV'}\mid z,v]
\le e^{pz+prh}\{e^{Bdh+F_p(B)v}+Bh\,e^{\gamma_phv}/300\}.
\]

Throughout (C2), \(F_p(4)\le4\), \(rp\le0\), and \(4d\le24/25\). Hence

\[
E_Q[e^{pZ'+4V'}\mid z,v]\le
e^{pz+4v}\{e^{4dh}+4h/300\}
\le e^{pz+4v+(73/75)h}.
\]

Successive conditioning and cancellation of realized and remaining loadings prove (C5), since \(4v_0\le6/25\).

Let \(\pi_{jr}=Q(V_j\in I_r)\) and choose

\[
h_{jir}\ge\sup_{v\in I_r}|e^{-2v}D_{ji}(v)|^2.
\]

For \(W_{ji}=|H_{ji}e^{q_{ji}Z_j}|\), (C5) bounds \(E_Q[W_{ji}^2e^{4V_j}]\) by \(K_j\). Cauchy--Schwarz then proves

\[
|r_{ji}|^2\le K_j\sum_rh_{jir}\pi_{jr}.
\tag{C7}
\]

Every mode at time \(j\) uses the same \(\pi_j\). No mode-dependent probability vector is introduced.

### 1.3 Support and strictness

Assume the complete price decomposition

\[
e_k=\Re\sum_{j,i}c_{ki}r_{ji}+R_k,\qquad |R_k|\le\varrho_k.
\]

Let \(\mathcal F\) be a nonempty compact convex set containing the actual full probability tuple, and \(f_{ji}(\Pi)=\sqrt{K_j\sum_rh_{jir}\pi_{jr}}\). Maximizing a real linear functional over the disks and then over \(\mathcal F\) gives

\[
s_{\mathcal E}(w)=
\max_{\Pi\in\mathcal F}\sum_{j,i}\left|\sum_kw_kc_{ki}\right|f_{ji}(\Pi)
+\sum_k|w_k|\varrho_k.
\tag{C8}
\]

The perspective constraints \(|z_{ji}|^2\le K_jh_{ji}\cdot\pi_j\) prove convexity; compactness makes the support attained. Write \(F_k(\Pi)=\sum_{j,i}|c_{ki}|f_{ji}(\Pi)\). The smallest coordinate box of this same outer set has support \(\sum_k|w_k|\max_{\mathcal F}F_k+\sum_k|w_k|\varrho_k\). Equality holds precisely when one common \(\Pi\) maximizes all active complete rows and, in every positive-radius disk, all nonzero \(w_kc_{ki}\) lie on a common nonnegative complex ray. Indeed, the differences between the supports are sums of nonnegative lost row maxima and triangle-inequality deficits; equality forces all of them to vanish. The converse follows by substitution.

For \(\mathcal F=\prod_j\mathcal P_j\), supports split into timewise maxima. General cross-time information requires retaining the maximum of the sum. This compares an outer set with its own smallest coordinate box, rather than with actual attainable pricing biases. After payoff-range intersections, the smallest coordinate box of the intersected set is the appropriate new comparison; the un-intersected criterion alone does not establish strictness for it.

## 2. Terminal probability constraints

The terminal witness fixes

\[
\theta_*=(\kappa,\bar v,\xi,\rho,v_0)=(3,9/200,23/100,-11/20,9/200),
\quad j=767.
\]

Use 102 bands:

\[
I_0=\{0\},\quad I_r=((r-1)/100,r/100]\ (1\le r\le100),\quad
I_{101}=(1,\infty).
\tag{C9}
\]

Here \(d=27/200\), \(\eta=255/256\), and \(V'=[dh+\eta v+\xi\sqrt{hv}G]^+\).

### 2.1 Mean and positive exponential bounds

The projection excess satisfies

\[
\epsilon(v)=E[-dh-\eta v-\xi\sqrt{hv}G]^+
\le\frac{h\xi^2}{\eta\sqrt{2\pi e}}e^{-d\eta/\xi^2}<h/200.
\]

For \(v=hz>0\), apply the Gaussian negative-part bound \(\epsilon\le\xi h\sqrt z\,\phi((d+\eta z)/(\xi\sqrt z))\), discard the nonnegative \(d^2/z\) term in the exponent, and maximize the remaining \(\sqrt z e^{-\eta^2z/(2\xi^2)}\). At zero the excess is zero. The strict bound follows from \(\eta>.99\), \(\xi^2<.053\), \(d\eta/\xi^2>2\), \(\sqrt{2\pi e}>3\), and \(e^{-2}<1/4\). Induction gives

\[
EV_n\le\bar v+(1/200)/\kappa=\mu:=7/150.
\tag{C10}
\]

Let \(\lambda=\kappa-2\xi^2=14471/5000\), \(\beta=1-\lambda h\), and \(M_n=Ee^{4V_n}\). The pointwise positive-part bound and concavity of \(x^\beta\) give

\[
E[e^{4V'}\mid v]\le e^{4dh+4\beta v}+h/50,\qquad
M_{n+1}\le e^{4dh}M_n^\beta+h/50.
\]

At \(M=5/4\), \(\log(5/4)\ge1/5\), \(4d-\lambda/5=-971/25000\), and \(1-e^{-x}\ge x/2\) for \(0\le x\le1\). Thus the decrease is at least \((5/4)(971/25000)h/2>h/50\). Since \(M_0=e^{.18}<5/4\), induction and Jensen yield

\[
Ee^{4V_n}\le5/4,\qquad Ee^{-tV_n}\ge e^{-t\mu}\quad(t\ge0).
\tag{C11}
\]

### 2.2 Laplace upper bounds

Use \(\mathcal T=\{1,4,16,64,256,(191/192)^2/[2(49/625)h]\}\). For each \(t\), define \(t_0=t\), \(t_{n+1}=\eta_*t_n-c_*t_n^2\), and

\[
L_{767}(t)=\exp\left\{-d_*h\sum_{n=0}^{766}t_n-v_*t_{767}\right\}.
\tag{C12}
\]

Use the reference quadruple \((191/192,(49/625)h/2,3/50,3/100)\) and the point quadruple \((255/256,\xi^2h/2,27/200,9/200)\). Since \(e^{-tY^+}\le e^{-tY}\), Gaussian integration gives the one-step Laplace upper recursion. The reference coefficients are valid throughout (C2), while the point coefficients specialize to \(\theta_*\). All 767 steps verify \(0\le t_n\le\eta_* /(2c_*)\), so the recursion is increasing throughout its enclosure.

For each \(t\in\mathcal T\), impose

\[
\sum_r\inf_{I_r}e^{-tv}\pi_r\le L_{767}^{\rm ref}(t),\quad
\sum_r\inf_{I_r}e^{-tv}\pi_r\le L_{767}^{\rm point}(t),\quad
\sum_r\sup_{I_r}e^{-tv}\pi_r\ge e^{-t\mu}.
\]

Add \(\sum_rl_r\pi_r\le\mu\), \(\sum_re^{4l_r}\pi_r\le5/4\), nonnegativity, and exact mass one. The tail Laplace infimum is zero, its supremum is \(e^{-t}\), and the zero band is evaluated at zero. In the saved system \(A\pi\le b\), upper-bound rows use lower coefficient enclosures and upper right-hand-side enclosures; lower-bound rows reverse the choices after sign reversal. The resulting 22-row compact polytope contains the actual \(Q\)-probability vector and is therefore nonempty.

## 3. Terminal one-step profiles

At the final step \(a_f=b_f=0\), so the projection difference \(e^{b_fY^+}-e^{b_fY}\) is exactly zero. For \(q=p+i\omega\), set \(g=(q^2-q)/2\), \(L=\rho\xi q-\kappa\), \(c=\xi^2/2\), and

\[
D_q(v)=e^{rqh+hgv}-e^{a(h)+B(h)v},\quad
B'=g+LB+cB^2,\ B(0)=0,\quad
a(h)=rqh+d\int_0^hB(t)dt.
\tag{C13}
\]

The representative modes are \(p=-1/48,\omega=64\) for the Asian profile and \(p=-1/4,\omega=-8,-24,\ldots,-120\) for the complete eight-frequency put row.

On \(\Re B=0\), the real Riccati drift is at most \(p(p-1)/2-(279/800)\omega^2<0\), so \(\Re B\le0\). With \(\kappa_p=\kappa-\rho\xi p>0\), its radial derivative is bounded by \(-\kappa_p|B|+|g|\); hence the whole-step flow exists and \(|B(t)|\le|g|t\).

Let \(P(t)=b_1t+b_2t^2+b_3t^3\), with \(b_1=g\), \(b_2=Lg/2\), \(b_3=(L^2g+2cg^2)/6\). The exact guard \(\Re b_1+\max(\Re b_2,0)h+\max(\Re b_3,0)h^2<0\) proves \(\Re P\le0\). Its residual is \(-\sum_{k=3}^6r_kt^k\), where

\[
r_3=Lb_3+2cb_1b_2,\quad r_4=c(2b_1b_3+b_2^2),\quad
r_5=2cb_2b_3,\quad r_6=cb_3^2.
\]

The difference \(B-P\) has coefficient \(L+c(B+P)\) with real part at most \(-\kappa_p\). Variation of constants gives outward bounds

\[
E_B=\sum_{k=3}^6|r_k|_+\frac{h^{k+1}}{k+1},\qquad
E_A=d\sum_{k=3}^6|r_k|_+\frac{h^{k+2}}{(k+1)(k+2)}.
\]

Set

\[
\begin{aligned}
A_q&=\min\left\{\left|-d\int_0^hP(t)dt\right|_++E_A,\ d|g|_+h^2/2\right\},\\
B_q&=\min\{|hg-P(h)|_++E_B,\ (|L|_++\xi^2|g|_+h)|g|_+h^2/2\},\\
m_q&=2-\max\{h\Re g,\min(0,\Re P(h)+E_B)\}>0.
\end{aligned}
\]

The second branches follow from \(|B(t)|\le|g|t\). The exponential-difference integral formula proves

\[
|e^{-2v}D_q(v)|\le e^{prh}(A_q+B_qv)e^{-m_qv}.
\tag{C14}
\]

The band supremum \(S_{qr}\) of the last profile is attained at a finite endpoint or its stationary point \(1/m_q-A_q/B_q\), if present; its infinite-tail limit is zero. Define

\[
h_{qr}=\min\{[4e^{2prh-4l_r}]_+,\ [e^{2prh}S_{qr}^2]_+\}.
\tag{C15}
\]

Both branches are valid. All nine modes pass both Riccati guards, and all 918 saved entries select the refined branch. Conjugation gives the same Asian profile at \(\omega=-64\).

The implementation uses 160-bit dyadic outward rounding. Positive exponentials are reduced to arguments at most \(1/8\), bounded by forty Taylor terms and a geometric tail, then restored by outward squaring; negative exponentials use reciprocals. Integer square roots enclose exact rational square roots. [model_bounds.py](../code/classical/model_bounds.py) contains only these bounds, without candidate search. [verify_input_bounds.py](../code/classical/verify_input_bounds.py) reproduces every field of [terminal767-input.json](../code/classical/terminal767-input.json), including the constraints, guards, and profiles. This is exact reproduction of the bounding implementation; the mathematical validity is established above.

## 4. Exact terminal price-row separation

Let \(a\) be the Asian square profile and \(d_\omega\) the put square profiles. The complete terminal rows are

\[
F_A(\pi)=C_A\sqrt{K_{767}}\sqrt{a\cdot\pi},\qquad C_A>0,
\tag{C16}
\]

\[
F_P(\pi)=\frac{1600e^{-.01}}\pi\sqrt{K_{767}}
\sum_{\omega=8,24,\ldots,120}
\frac{\sqrt{d_\omega\cdot\pi}}
{\sqrt{(\omega^2+1/16)(\omega^2+25/16)}}.
\tag{C17}
\]

The scalar denominator in the prefactor of (C17) is the circle constant; the other \(\pi\) symbols denote the probability vector. All eight relative put weights are retained. The Asian row is the conjugate-reduced row of the original twelve-date \(95/110\) payoff-transform catalog, whose terminal profiles coincide. Its simplex Beta integral is

\[
\mathcal M_K(s)=K(12K/100)^{\sum_ms_m}
\frac{\prod_m\Gamma(s_m)}{\Gamma(2+\sum_ms_m)}.
\]

The coefficient is a positive common normalization times \(\mathcal M_{95}-\mathcal M_{110}\) at the damped catalog frequencies. Gamma factors are finite and nonzero. The strike factors have unequal magnitudes \(95(11.4)^{1/4}\) and \(110(13.2)^{1/4}\), so at least one coefficient is nonzero. Hence the sum of absolute coefficient magnitudes \(C_A\) is positive. Its magnitude is unnecessary for qualitative separation; full inversion and payoff remainders still belong to the complete-price decomposition.

### 4.1 Unique Asian maximizer

The primal witness has support \(\{1,2,6\}\). With \(N=1224763483833781421664584437384207906751833915425\),

\[
\pi^A_1=33905558047250364446648353945678164610870798859/N,
\quad
\pi^A_2=59681676093752162913738260683252953132397661045/N,
\]
\[
\pi^A_6=1131176249692778894304197822755276789008565455521/N.
\]

The saved dual \(y\ge0\) satisfies \(A^Ty\ge a\) and \(a\cdot\pi^A=b\cdot y\). All reduced costs outside this support are strictly positive. The three positive dual multipliers correspond to the point \(t=256\) Laplace row, mean row, and mass row. Restricted to the support, their matrix has determinant

\[
-\frac{16330179784450418955527792498456105423357785539}
{5846006549323611672814739330865132078623730171904}\ne0.
\]

Weak duality proves optimality. Complementary slackness forces every optimizer to vanish off the support and satisfy those same three equalities. Nonsingularity proves uniqueness. Because (C16) is strictly increasing in \(a\cdot\pi\), \(\pi^A\) is its unique maximizer.

### 4.2 A put-increasing feasible direction

The second feasible vector has support \(\{5,6\}\), with

\[
\pi^B_5=
\frac{243583606221817153033947472119380503275988757165}
{730750818665451459101842416358141509827966271488},
\qquad \pi^B_6=1-\pi^B_5.
\]

Write \(\mathcal B(\pi)=\sum_\omega\sqrt{d_\omega\cdot\pi}/\sqrt{D_\omega}\), \(D_\omega=(\omega^2+1/16)(\omega^2+25/16)\), and \(x_\omega=d_\omega\cdot\pi^A>0\). Along the feasible segment,

\[
\left.\frac d{dt}\mathcal B((1-t)\pi^A+t\pi^B)\right|_{t=0}
=\sum_\omega\frac{d_\omega\cdot(\pi^B-\pi^A)}
{2\sqrt{D_\omega x_\omega}}\in[L,U],
\tag{C18}
\]

where

\[
L=\frac{2214102728888110422476248911088843134229}
{730750818665451459101842416358141509827966271488},
\quad
U=\frac{2214102728888110422476248911088843134233}
{730750818665451459101842416358141509827966271488},
\quad L>3\cdot10^{-9}.
\]

For each interval \([l_\omega,u_\omega]\) of the positive coefficient \(1/(2\sqrt{D_\omega x_\omega})\), exact square comparisons suffice:

\[
0<l_\omega\le u_\omega,\qquad
4l_\omega^2D_\omega x_\omega\le1\le4u_\omega^2D_\omega x_\omega.
\]

Negative profile changes reverse endpoints before summation. Thus (C18) is a signed full-row bound. For sufficiently small \(t>0\), the put row increases, so \(\pi^A\) is not its maximizer. The rows have disjoint maximizer sets.

For \(w=e_{10}-e_8\), this proves the terminal outer-set gap \(g_{767}(w)>0\). With valid other timewise sets, the same complete catalog, and a product probability set, the sum of timewise gaps is at least \(g_{767}\). This concerns un-intersected outer sets. It provides neither a numerical money-valued gap nor a lower bound on actual price bias. Payoff-range intersections and complete-price accuracy require their respective additional conditions.

The witness is in [terminal767-result.json](../code/classical/terminal767-result.json). [verify_terminal.py](../code/classical/verify_terminal.py) performs 407 exact checks of feasibility, dual inequalities, complementary slackness, uniqueness, basis identities, the second feasible vector, and all signed derivative bounds. It calls no LP, SOC, model, or price solver. The [archived adjacent-author review](../code/classical/terminal767-historical-review.json) retains its original role statement and does not constitute external peer review.

## 5. Global trial-field identity and the thirteen-dimensional field

### 5.1 Identity and traces

Between fixings, let \(u_m\) be a trial field, \(r_m=(\partial_t+\mathcal L)u_m\), \(D_j=Q_hu_{j+1}-u_j\), \(J_m\) its actual right trace composed with the fixing map minus its left trace, and \(\tau=R-u_T\) its terminal defect. Under integrable growth, genuine traces, and uniform integrability for stopped continuous calculations,

\[
\Delta R=\sum_jE_QD_j-E_P\int_0^Tr_m\,dt
+\sum_mE_PJ_m+(E_Q-E_P)\tau.
\tag{C19}
\]

The \(Q\) tower telescopes the discrete sum. Piecewise stopped Itô's formula telescopes the continuous integrals, including the actual fixing traces. Subtraction gives (C19); uniform integrability removes stopping.

With exact traces and terminal payoff, the last terms vanish. If \(|D_j|\le h\eta^Q_jW\), \(|r_m|\le\eta_c(t)W\), and \(E_PW,E_QW<5/2\), then

\[
|\Delta R|\le\frac52\left(h\sum_j\eta^Q_j+\int_0^T\eta_c(t)dt\right).
\tag{C20}
\]

A necessary lower bound on \(\int\eta_c\) is not an evaluation of this sufficient upper bound.

### 5.2 Coordinates, basis, and generator

With \(m\) realized arithmetic fixings, let \(A_m\) be their normalized stock-price sum and \(n=12-m\). Set \(B=(A_m+ns)/12\), \(y=A_m/(A_m+ns)\), \(\beta=1-y\), and \(z=v/(1+v)\). For a branch \(B^{-q}P(y,v)\), the conjugated generator is

\[
\begin{aligned}
\mathcal L_qP={}&-ry\beta P_y+dP_v-qr\beta P\\
&+v\{\tfrac12y^2\beta^2P_{yy}-\rho\xi y\beta P_{yv}
+\tfrac12\xi^2P_{vv}+(1+q)y\beta^2P_y\\
&\hspace{20mm}-(\kappa+q\rho\xi\beta)P_v
+\tfrac12q(q+1)\beta^2P\}.
\end{aligned}
\tag{C21}
\]

The twelve original functions are \(\phi_{ij}=\beta y^iz^j\), \(0\le i\le2\), \(0\le j\le3\). The completion adds \(\psi=v\beta^2\). Write the branch polynomial as \(P=1+\Phi c(t)\), with the basis ordered first by \(i\), then by \(j\), and \(\psi\) last. The terminal forcing is represented exactly:

\[
\mathcal L_q1=-qr\phi_{00}+\tfrac12q(q+1)\psi.
\tag{C22}
\]

This is terminal-generator completion, not closure under every generator image. Differentiation gives

\[
\begin{aligned}
\mathcal L_q\psi={}&d\beta^2
+v\beta^2\{(2r+2\rho\xi)y-\kappa-q(r+\rho\xi)\beta\}\\
&+v^2\beta^2\{y^2-2(1+q)y\beta+\tfrac12q(q+1)\beta^2\}.
\end{aligned}
\tag{C23}
\]

The fixed 35 sample pairs use \(y\in\{0,1/4,1/2,3/4,1\}\) and \(z\in\{0,1/64,1/32,1/16,1/8,1/4,1/2\}\). For the thirteen-function row \(\Phi\), let \(M=e^{-v}\Phi\), \(N=e^{-v}\mathcal L_q\Phi\), and \(K=(M^*M)^{-1}M^*N\).

The sampling matrix has full column rank. If \(\beta R(y,z)+av\beta^2\) vanishes at all pairs, four \(y<1\) values force \(R(y,z)+av(1-y)\), a degree-two polynomial in \(y\), to vanish identically for each sampled \(z\). At \(y=0\), multiplication by \(1-z\) gives a degree-four polynomial vanishing at seven \(z\)-values. Evaluation of that zero polynomial at \(z=1\) gives \(a=0\); its remaining degree-three coefficient polynomials vanish identically.

The stored nodes were generated by the fixed floating-point projection and 385 small exponential propagations. After storage, finite floating entries define exact binary-rational constants. The field between original grid points is cubic Hermite interpolation of these endpoints, with exact physical slopes

\[
s=-Kc-g(q),\qquad
g(q)=-qr\,e_{00}+\tfrac12q(q+1)e_\psi.
\tag{C24}
\]

Saved floating forcing values generate nodes only; (C24) defines the final slopes. Terminal correction nodes are exactly zero, giving \(P_T=1\).

### 5.3 Exact fixing carry

At a fixing, \(\gamma=(n-1)/n\), \(y'=\gamma y+1/n\), and \(B'=B\). The original-basis carry is

\[
(T_nc)_{\ell j}=\gamma\sum_{i=\ell}^2
\binom{i}{\ell}\gamma^\ell n^{-i+\ell}c_{ij},\qquad
T_n\psi=\gamma^2\psi.
\tag{C25}
\]

The right endpoints use this rational map, rather than approximate matching of floating values. At \(n=1\) the correction carry vanishes. Thus the traces and terminal value are exact. The full reconstruction retains the arithmetic and geometric branches, their common phase, and all original frequencies.

### 5.4 Growth and the original correlated kernel

Every member of the field satisfies

\[
|P|\le C_0+C_1v\le\widehat C e^{v/2},
\qquad \widehat C=C_0+2C_1/e.
\tag{C26}
\]

For the paired branches, \(W=e^v(B^{-1/2}+C_g^{-1/2})\), with \(C_g=e^{\ell_m/12}s^{n/12}\) and \(\ell_m=\sum_{a=1}^m\log s_{a/12}\). The arithmetic--geometric mean inequality and the negative-moment estimates give \(E_PW,E_QW<5/2\) at \(\theta_*\). Squared weights reduce to total nonpositive stock loading at most one and variance loading two; the stopped continuous exponential-supermartingale argument with the stronger variance loading four supplies uniform integrability.

Write the continuous residual as \(A_0+vA_1+v^2A_2\). For \(|A_k|\le a_k\),

\[
e^{-v}|F|\le a_0+a_1/e+4a_2/e^2,\quad
e^{-v}|F|\le(a_0+2a_1/e+16a_2/e^2)e^{-V_*/2}\quad(v\ge V_*).
\tag{C27}
\]

The actual boundary \(\mathcal L_q\psi|_{v=0}=d\beta^2\) is retained.

For the discrete step, \(\Omega=y+\beta e^{Z'-Z}\), \(y'=y/\Omega\), followed by the actual fixing map where appropriate, and

\[
F_A=E[\Omega^{-q}P_{\rm next}(y',V')]-P_{\rm current}.
\tag{C28}
\]

Both quantities use the correlated kernel (C1), including the zero atom. For \(\lambda\in[-1,0]\), the projected Gaussian estimate gives

\[
E e^{\lambda(Z'-Z)+V'}\le e^{(d+1/300)h+v}.
\]

Consequently, with \(C_h=e^{(d+1/300)h/2}\),

\[
e^{-v}|F_A|\le\widehat C(1+C_h)e^{-V_*/2}\quad(v\ge V_*).
\tag{C29}
\]

On \(\{|G|>L\}\cup\{|H|>L\}\), Cauchy--Schwarz bounds the omitted contribution by \(\widehat C C_h\sqrt{p_L}\), where \(p_L\le\min(1,4e^{-L^2/2})\), without assuming independence from the weighted integrand. The geometric-separation tail retains its common phase and is bounded by \(e^{-D_*/2}(R_A+R_G)\). These are finite global-envelope bounds for (C19); they do not prescribe the numerical size of (C20).

## 6. First-month residual evidence

The candidate coefficient-bank SHA-256 is 665a91049e2c4dd9463cba2fa6d5cc876b5707e0923a72047dc8a1852890c5a8.

The record fixes \(m=0,y=D=0,v=9/200\), all 385 original modes \(q_k=1/2+ik/3\), and the 64 original time pieces in the first month. Eight integration cells are \([i/96,(i+1)/96]\), \(0\le i<8\). The saved mode integrals already include the original price coefficients and normalization \(e^{-9/200}/2\).

At this state let \(w=(1,z,z^2,z^3,0,\ldots,0,v)\), let \(\ell\) be the generator-value row of the thirteen basis functions, and \(\ell_0=-qr+q(q+1)v/2\). Exact cubic Hermite integration on one piece gives

\[
\int F_{A,q}dt=
\left[w+\frac{h^2}{12}\ell K\right](c_R-c_L)
+\frac h2\ell(c_L+c_R)+h\ell_0.
\tag{C30}
\]

Indeed, integrate the derivative to \(w(c_R-c_L)\) and use \(\int c(t)dt=h(c_L+c_R)/2+h^2(s_L-s_R)/12\), with \(s_L-s_R=K(c_R-c_L)\).

At phase zero, the common-phase real integral is the real sum of all 385 weighted integrals. Apply \(\int|F|\ge|\int F|\) on each cell, sum the eight absolute integral lower bounds, and subtract the uniform integrated geometric-branch upper bound. This yields

\[
\int_0^{1/12}\eta_c(t)dt\ge
\frac{211825137980176416264545048578203013986227105463569147286361401899350072719096586865}
{62165404551223330269422781018352605012557018849668464680057997111644937126566671941632}
>0.003407444052031154>0.
\tag{C31}
\]

Thus the selected exact field is nonexact under the stated all-state positive-envelope definition. This is a necessary lower bound for this field's envelope, not for the best approximation in the trial space and not for signed expected price bias. The record also includes a Parseval lower bound; phase zero is larger here.

For the historical allocation \(\int\eta_c\le1/1000\), (C31) rejects that selected allocation. Multiplication by the same factor \(2399/1200\) gives \([0.006812048567352283,0.006812048567352284]\), below the separate complete positive balance \(21581924359/10^{12}\). Hence this test does not reject every possible complete sufficient-error allocation. The original status FAIL_SELECTED_INTEGRATED_PDE_CONTRACT_ONLY is retained.

[field-cell-integrals.json](../code/classical/field-cell-integrals.json) supplies all 3080 complex interval integrals. [field-result.json](../code/classical/field-result.json) supplies the exact aggregate fractions and scientific status. The [independent readback](../code/classical/field-independent-readback.json) records a previously completed 384-bit direct integration of the same candidate and all 64 time pieces. It records neither a sufficient conversion upper bound nor an actual-bias lower bound.

[verify_field_receipt.py](../code/classical/verify_field_receipt.py) checks all saved identities, counts, interval orderings, and outward decimal bounds using exact fractions. It separately sums the real mode boxes at phase zero and confirms the displayed strict lower bound directly from that sum. It does not regenerate the coefficient bank or rerun the archived direct integration.

## 7. Files and reproducibility

Run from the repository root using Python 3.10 or later and only the standard library:

~~~sh
python code/classical/verify_input_bounds.py
python code/classical/verify_terminal.py
python code/classical/verify_field_receipt.py
~~~

The default checks are read-only. Add the optional flag --write to create fresh validation records; doing so changes those records and requires updating the supplement manifest before a new release.

| File | Mathematical role |
| --- | --- |
| [terminal767-input.json](../code/classical/terminal767-input.json) | Exact bands, probability matrix, nine profiles, and bounding metadata |
| [terminal767-result.json](../code/classical/terminal767-result.json) | Exact primal, dual, uniqueness, feasible-direction, and derivative witnesses |
| [terminal767-historical-review.json](../code/classical/terminal767-historical-review.json) | Archived adjacent-author integer verification and stated scope |
| [field-cell-integrals.json](../code/classical/field-cell-integrals.json) | All 3080 weighted complex integral intervals |
| [field-result.json](../code/classical/field-result.json) | Exact envelope aggregates and selected-allocation status |
| [field-independent-readback.json](../code/classical/field-independent-readback.json) | Archived 384-bit direct integration of the same field |
| [provenance.json](../code/classical/provenance.json) | Original and portable identities, transformations, and omitted-bank identity |
| [input-validation.json](../code/classical/input-validation.json) | Exact reproduction of 12 Laplace recursions, 22 rows, and 918 profile entries |
| [terminal-validation.json](../code/classical/terminal-validation.json) | Portable 407-check terminal result |
| [field-validation.json](../code/classical/field-validation.json) | Exact receipt and mode-box aggregation result |

The terminal input, terminal result, historical terminal review, and field mode-cell integrals are byte-identical copies. Two field receipts had private absolute input keys; their portable copies replace these keys by unambiguous basenames and retain every scientific value, candidate identity, result status, and scope statement. Provenance records both hashes. Source documents and the omitted coefficient bank are identified by hashes rather than private workstation links.

The supported claims are common-probability outer inclusion under the stated model and loading conditions, strict terminal outer-set separation for the fixed complete rows, validity of the specified global field, and a positive first-month residual-envelope lower bound for that field. Each has its own hypotheses. None of the records is a complete annual price certificate or evidence of realized trading gains.
