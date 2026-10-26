# Classical Heston extensions

Supplement to *Certified Joint Pricing Errors in Rough Heston*, revision of 26 October 2026.

These are the classical-model extensions formerly included as Appendices F--G. They are retained with their equation labels for traceability. They do not establish a complete annual monetary pricing certificate and are not used in the Rough Heston proof chain. References to Sections 2--7 or Appendices A--E refer to the main paper. The thirteen-function construction is a diagnostic with a missing coefficient-bank obligation, not the method used to obtain the Rough Heston results.

## Appendix F. Original-chain classical Heston inclusion

This appendix constructs a classical-Heston input to the joint-error interface. The correlated positive-part chain supplies common original-law occupation probabilities. Standard convex analysis then gives support functions and financial propagation. The terminal witness certifies strict improvement of an outer set; completing an annual monetary pricing certificate also requires the full-price inputs in (F.21).

### F.1. The two laws and admissible modes

Write \(s=S/100=e^Z\), \(d=\kappa\bar v\), \(r=1/100\), \(h=1/768\), and \(s_0=1\). The continuous law \(P\) and the original discrete law \(Q\) are

\[
\begin{aligned}
dZ_t&=(r-V_t/2)dt+\sqrt{V_t}(\rho\,dW_t+\sqrt{1-\rho^2}\,dB_t),\\
dV_t&=(d-\kappa V_t)dt+\xi\sqrt{V_t}\,dW_t,\\
Y&=dh+(1-\kappa h)v+\xi\sqrt{hv}\,G,\qquad V'=Y^+,\\
Z'&=z+rh-hv/2+\sqrt{hv}(\rho G+\sqrt{1-\rho^2}H).
\end{aligned}\tag{F.1}
\]

Here \(G,H\) are independent standard normal variables, and the same \(G\) drives both discrete updates. Throughout the common-moment argument,

\[
\kappa\in[2,4],\quad \bar v,v_0\in[3/100,3/50],\quad
\xi\in[9/50,7/25],\quad \rho\in[-4/5,-3/10].\tag{F.2}
\]

A finite multidate mode has loadings \(\alpha_{i,n}\in\mathbb C\) satisfying

\[
\Re\alpha_{i,n}\le0,\qquad \sum_n|\Re\alpha_{i,n}|\le1/2.\tag{F.3}
\]

The realized prefix is \(H_{ji}\); the remaining stock loading is \(q_{ji}=p_{ji}+i\omega_{ji}\). All observation dates lie on the grid. A fixing moves one loading from the remaining sum to the realized prefix, without changing the underlying mode.

### F.2. Exact continuation, the full kernel, and integrability

**Lemma (exact continuous continuation).** The affine continuation \(u=e^{qz+a+bv}\), initialized with terminal \(a=b=0\), is the continuous conditional expectation of the mode. Between fixings, in remaining-time coordinates,

\[
b'=\tfrac12\xi^2b^2+(\rho\xi q-\kappa)b+\tfrac12(q^2-q),
\qquad a'=rq+db.\tag{F.4}
\]

At fixings \(q\) changes and \(a,b\) continue without resetting. To prove existence, set \(\kappa_p=\kappa-p\rho\xi\), \(\gamma_p=(p^2-p)/2\). On \(\Re b=1\), the real drift is

\[
\tfrac12\xi^2-\kappa_p+\gamma_p
-\tfrac12\{(\xi\Im b+\rho\omega)^2+(1-\rho^2)\omega^2\}<0,
\qquad
\frac{d|b|}{dt}\le(\xi^2/2-\kappa_p)|b|+|q^2-q|/2.\tag{F.5}
\]

Indeed \(p\in[-1/2,0]\), \(\kappa_p\ge1.888\), and \(\gamma_p\le3/8\). The first-crossing argument gives \(\Re b\le1\); the radial estimate excludes explosion on every finite segment. Also \(\Re a\le(6/25)T\).

The identification with an expectation requires more than formal Riccati algebra. Multiply the real loadings by \(5/4\), and let \(L_*(t),p_*(t)\) be the resulting realized and remaining contributions. Then

\[
\mathcal Y_t=e^{L_*(t)+p_*(t)Z_t+4V_t-(24/25)t},\qquad
|\mathcal M_\tau|^{5/4}
\le e^{(5/4)(6/25)T+(24/25)T}\mathcal Y_\tau.\tag{F.6}
\]

Here \(\mathcal M\) is the stopped affine local martingale associated with the mode. The process \(\mathcal Y\) is a nonnegative local supermartingale: its constant drift is nonpositive, and its variance drift is at most \(65/128-4(1.86)+8(7/25)^2<0\). Loading changes cancel at each fixing. Compact stopping and (F.6) give a uniform \(5/4\)-moment bound. Uniform integrability removes stopping, proves the conditional-expectation identity, and covers \(v=0\) and every finite initial state.

The actual one-step propagation retains the entire positive-part Gaussian kernel. For next-step coefficients \(a,b,q\), integration over \(H\) gives

\[
\frac{Q_hu(z,v)}{e^{qz}}=
e^{a+qrh-qhv/2+q^2(1-\rho^2)hv/2}
\int_{\mathbb R}\varphi(g)
e^{q\rho\sqrt{hv}g+b[dh+(1-\kappa h)v+\xi\sqrt{hv}g]^+}\,dg.\tag{F.7}
\]

For \(v>0\) the integral splits at \(g_0=-(dh+(1-\kappa h)v)/(\xi\sqrt{hv})\): the first part has variance exponent zero, and the second uses the positive candidate. Both parts are retained. At \(v=0\), \(V'=dh\) deterministically. Completing a real Gaussian square is an integration device, not a replacement of \(Q\) by a mode-dependent probability law.

Let \(D_{ji}(v)\) be this actual propagation minus the exact continuous continuation, after removal of the common \(e^{q_{ji}z}\). Finite conditional telescoping, including each fixing exactly once, yields

\[
\Phi_{Q,i}-\Phi_{P,i}=\sum_{j=0}^{N-1}r_{ji},\qquad
r_{ji}=E_Q[H_{ji}e^{q_{ji}Z_j}D_{ji}(V_j)].\tag{F.8}
\]

The integrability in the next subsection justifies every discrete expectation in this identity.

### F.3. Original-law moments and shared occupation probabilities

**Lemma (discrete exponential moment).** For nonpositive real multidate loadings of total absolute value at most one,

\[
E_Q\exp\!\left\{\sum_{n\le j}\beta_n Z_n+4V_j\right\}
\le K_j:=e^{6/25+(73/75)jh}.\tag{F.9}
\]

To prove it, complete the real stock square for \(p\in[-1,0]\). The candidate mean becomes \(dh+\eta_pv\), where \(\eta_p=1-\kappa_ph\ge191/192\). Since \((-y)^+\le h(25e)^{-1}e^{-25y/h}\),

\[
E(-Y_p)^+\le\frac{h}{25e}
\exp\!\left\{-25d+\frac{[-25\eta_p+(625/2)\xi^2]v}{h}\right\}
\le\frac{h}{25e^{5/2}}<h/300.\tag{F.10}
\]

The parameter bounds imply \(d\ge3/50\), the variance coefficient is at most \(-71/192\), and \(e^{5/2}>12\). The negative part is exactly zero at \(v=0\). For \(B\ge0\), \(e^{By^+}\le e^{By}+B(-y)^+\). Defining \(F_p(B)=\gamma_ph+\eta_pB+\xi^2hB^2/2\), Gaussian integration therefore gives

\[
\begin{aligned}
E_Q[e^{pZ'+BV'}\mid z,v]
&\le e^{pz+prh}\{e^{Bdh+F_p(B)v}+Bh\,e^{\gamma_phv}/300\},\\
E_Q[e^{pZ'+4V'}\mid z,v]
&\le e^{pz+4v}(e^{4dh}+4h/300)
\le e^{pz+4v+(73/75)h}.
\end{aligned}\tag{F.11}
\]

Here \(F_p(4)\le4\), \(rp\le0\), and \(4d\le24/25\). Successive conditioning and cancellation of loading changes prove (F.9), using \(4v_0\le6/25\).

For a finite partition \(I_r\) of \([0,\infty\)), retain the zero atom and the unbounded tail, and set

\[
\pi_{jr}=Q(V_j\in I_r),\quad
h_{jir}\ge\sup_{v\in I_r}|e^{-2v}D_{ji}(v)|^2,\quad
|r_{ji}|^2\le K_j\sum_rh_{jir}\pi_{jr}=:\mathbf a_{ji}\cdot\pi_j.\tag{F.12}
\]

The last inequality is complex Cauchy–Schwarz applied to \(H_{ji}e^{q_{ji}Z_j}e^{2V_j}\) and \(e^{-2V_j}D_{ji}(V_j)\); its first squared moment is covered by the doubled loadings in (F.9). Thus every mode uses the same original-chain probability vector. If a trial defect depends on additional states, one must bound uniformly over those states or enlarge the partition. Continuous-law residuals do not inherit these \(Q\)-probabilities.

### F.4. A valid terminal probability polytope

Fix \(\theta_*=(\kappa,\bar v,\xi,\rho,v_0)=(3,9/200,23/100,-11/20,9/200)\), \(j=767\), \(d=27/200\), and \(\eta=255/256\). Use

\[
I_0=\{0\},\quad I_r=((r-1)/100,r/100]\ (1\le r\le100),
\quad I_{101}=(1,\infty).\tag{F.13}
\]

For \(v>0\) the next-step zero mass is \(\Phi(-(dh+\eta v)/(\xi\sqrt{hv}))\); at \(v=0\) it is zero. Projection excess satisfies \(E[-dh-\eta v-\xi\sqrt{hv}G]^+\le h\xi^2e^{-d\eta/\xi^2}/(\eta\sqrt{2\pi e})<h/200\). This follows by writing \(v=hz\), bounding the normal negative part by its density term, and maximizing \(\sqrt z e^{-\eta^2z/(2\xi^2)}\). The mean recursion and the positive-exponential recursion give

\[
EV_n\le\mu:=7/150,\qquad
M_{n+1}\le e^{4dh}M_n^{\beta}+h/50,\qquad
Ee^{4V_n}\le5/4,\quad Ee^{-tV_n}\ge e^{-t\mu}.\tag{F.14}
\]

Here \(M_n=Ee^{4V_n}\), \(\lambda=\kappa-2\xi^2=14471/5000\), and \(\beta=1-\lambda h\in(0,1)\). Concavity of \(x^\beta\) gives the displayed recursion. At \(M=5/4\), use \(\log(5/4)\ge1/5\), \(4d-\lambda/5=-971/25000\), and \(1-e^{-x}\ge x/2\) for \(0\le x\le1\); the decrease exceeds \(h/50\). Since \(M_0=e^{.18}<5/4\), induction proves the positive-exponential bound. Jensen gives the Laplace lower bound.

For \(t\in\mathcal T=\{1,4,16,64,256,(191/192)^2/[2(49/625)h]\}\), define

\[
t_0=t,\quad t_{n+1}=\eta_*t_n-c_*t_n^2,\qquad
L_{767}(t)=\exp\!\left[-d_*h\sum_{n=0}^{766}t_n-v_*t_{767}\right].\tag{F.15}
\]

The reference quadruple is \((\eta_*,c_*,d_*,v_*)=(191/192,(49/625)h/2,3/50,3/100)\), and the point quadruple is \((255/256,\xi^2h/2,27/200,9/200)\). The bound \(e^{-tY^+}\le e^{-tY}\) and Gaussian integration give \(E[e^{-tV'}\mid v]\le e^{-dht}e^{-(\eta t-\xi^2ht^2/2)v}\). All 767 recursion steps satisfy \(0\le t_n\le\eta_* /(2c_*)\). Consequently the recursion is monotone on the certified enclosures; the conservative reference choices yield a valid upper bound throughout (F.2).

The true terminal probability vector satisfies

\[
\begin{aligned}
\sum_r\inf_{I_r}e^{-tv}\pi_r&\le L^{\rm ref}_{767}(t),&
\sum_r\inf_{I_r}e^{-tv}\pi_r&\le L^{\rm point}_{767}(t),\\
\sum_r\sup_{I_r}e^{-tv}\pi_r&\ge e^{-t\mu},&
\sum_r\ell_r\pi_r&\le\mu,\quad \sum_re^{4\ell_r}\pi_r\le5/4,
\end{aligned}\tag{F.16}
\]

together with nonnegativity and mass one; \(\ell_r=\inf I_r\). The zero Laplace coefficient is one, and the tail infimum/supremum are zero/\(e^{-t}\). The six triples, two moment rows, and two signed mass rows give 22 inequalities. Upper-bound rows use lower coefficient endpoints and upper right endpoints; lower-bound rows use upper coefficients and lower right endpoints before sign reversal. Thus the saved rational \(\mathcal P_{767}=\{\pi\ge0:A\pi\le b\}\) contains the actual probabilities and is a nonempty compact subset of the simplex.

### F.5. Certified terminal profiles on the entire variance axis

At the final step the future variance exponent is zero, so its positive-part correction vanishes exactly. For \(q=p+i\omega\), write \(g=(q^2-q)/2\), \(L=\rho\xi q-\kappa\), \(c=\xi^2/2\). Then

\[
D_q(v)=e^{rqh+hgv}-e^{a(h)+B(h)v},\quad
B'=g+LB+cB^2,\ B(0)=0,\qquad a(h)=rqh+d\int_0^hB(t)dt.\tag{F.17}
\]

At \(\theta_*\), the Asian representative is \((p,\omega)=(-1/48,64)\), and the put representatives are \((-1/4,-8),(-1/4,-24),\ldots,(-1/4,-120)\). On \(\Re B=0\) the real drift is at most \(p(p-1)/2-(279/800)\omega^2<0\); hence \(\Re B\le0\) and \(\lvert B(t)\rvert\le|g|t\).

Let \(P_3(t)=b_1t+b_2t^2+b_3t^3\), where \(b_1=g\), \(b_2=Lg/2\), \(b_3=(L^2g+2cg^2)/6\). The exact guard \(\Re b_1+\max(\Re b_2,0)h+\max(\Re b_3,0)h^2<0\) proves \(\Re P_3\le0\). Its residual is \(-\sum_{k=3}^6r_kt^k\), with \(r_3=Lb_3+2cb_1b_2\), \(r_4=c(2b_1b_3+b_2^2)\), \(r_5=2cb_2b_3\), \(r_6=cb_3^2\). Since \(\Re[L+c(B+P_3)]\le-\kappa_p\), variation of constants gives

\[
E_B=\sum_{k=3}^6|r_k|_+\frac{h^{k+1}}{k+1},\qquad
E_A=d\sum_{k=3}^6|r_k|_+\frac{h^{k+2}}{(k+1)(k+2)}.\tag{F.18}
\]

The notation \(|\cdot|_+\) denotes a certified upper modulus. Set

\[
\begin{aligned}
A_q&=\min\{|{-d\int_0^hP_3}|_++E_A,\ d|g|_+h^2/2\},\\
B_q&=\min\{|hg-P_3(h)|_++E_B,\ (|L|_++\xi^2|g|_+h)|g|_+h^2/2\},\\
m_q&=2-\max\{h\Re g,\min(0,\Re P_3(h)+E_B)\}>0.
\end{aligned}\tag{F.19}
\]

The exponential-difference integral formula, and the coarse modulus bound for the two exponentials, imply

\[
|e^{-2v}D_q(v)|\le e^{prh}(A_q+B_qv)e^{-m_qv},\qquad
h_{qr}=\min\{[4e^{2prh-4\ell_r}]_+,[e^{2prh}S_{qr}^2]_+\},\quad
S_{qr}=\sup_{v\in I_r}(A_q+B_qv)e^{-m_qv}.\tag{F.20}
\]

The supremum uses finite endpoints of each band closure and the stationary point \(1/m_q-A_q/B_q\) when present. For \(B_q=0\), use the monotone branch without division. The tail limit is zero, and the zero band is evaluated at zero. Exact outward arithmetic verifies both Riccati guards and all 918 entries (nine modes, 102 bands), including the tail. The Asian conjugate has the identical profile.

### F.6. Joint inclusion and its exact strictness criterion

Suppose the same finite mode catalog gives the complete discounted-price decomposition

\[
e_k=p_{h,k}-p_{c,k}=\Re\sum_{j,i}c_{ki}r_{ji}+R_k,\qquad |R_k|\le\varrho_k.\tag{F.21}
\]

The coefficients and the remainder bounds must include all required conversion, truncation, and arithmetic contributions. The terminal witness alone does not establish this full-price premise. Let \(\mathcal F\) be nonempty, compact, convex, and contain the actual full occupation tuple \(\Pi=(\pi_j)_j\). Define

\[
\mathcal E=\left\{\left(\Re\sum_{j,i}c_{ki}z_{ji}\right)_k:
\Pi\in\mathcal F,\ |z_{ji}|^2\le\mathbf a_{ji}\cdot\pi_j\right\}
+\prod_k[-\varrho_k,\varrho_k].\tag{F.22}
\]

**Proposition (joint price inclusion).** This set is nonempty, compact, convex, centrally symmetric, and contains the actual \(e\). Its support is

\[
s_{\mathcal E}(w)=\max_{\Pi\in\mathcal F}\sum_{j,i}
\left|\sum_kw_kc_{ki}\right|\sqrt{\mathbf a_{ji}\cdot\pi_j}
+\sum_k|w_k|\varrho_k.\tag{F.23}
\]

**Proof.** The lifted constraints are convex because \(\lvert z\rvert^2\) is convex and the right side is affine; they are closed and bounded over compact \(\mathcal F\). Their linear image plus the remainder box has the stated geometric properties. The actual \((\Pi,r)\) is feasible by (F.12). For fixed \(\Pi\), the support of each complex disk is its radius times the modulus of the real-linear coefficient. Independent disk phases attain the sum; the common maximization then gives (F.23). With cross-time constraints retain \(\max_{\mathcal F}\sum_j\), rather than \(\sum_j\max\); separation is justified only for \(\mathcal F=\prod_j\mathcal P_j\). ∎

Put \(F_k(\Pi)=\sum_{j,i}|c_{ki}|\sqrt{\mathbf a_{ji}\cdot\pi_j}\), \(m_k=\max_{\mathcal F}F_k\), and \(\mathcal B=\operatorname{rect}(\mathcal E)=\prod_k[-m_k-\varrho_k,m_k+\varrho_k]\). Then

\[
\begin{aligned}
s_{\mathcal B}(w)-s_{\mathcal E}(w)
=\min_{\Pi\in\mathcal F}\Big\{
&\sum_k|w_k|[m_k-F_k(\Pi)]\\
&+\sum_{j,i}\big[\sum_k|w_kc_{ki}|-|\sum_kw_kc_{ki}|\big]
\sqrt{\mathbf a_{ji}\cdot\pi_j}\Big\}.
\end{aligned}\tag{F.24}
\]

Every summand is nonnegative. The gap is zero precisely when one common \(\Pi_*\) maximizes every active complete pricing row and all nonzero \(w_kc_{ki}\) in each positive-radius disk lie on a common nonnegative complex ray. No phase condition is required at zero radius; \(w=0\) has zero gap. Adding and subtracting the common row values proves (F.24), and compactness makes the minimum attained. Absence of such a witness therefore proves strict improvement over the smallest coordinate box of the same outer set. It proves neither boundary attainment by the actual bias nor an actual-error lower bound. After payoff intersections, apply the criterion anew to the resulting set.

### F.7. A complete terminal-row separation witness

The instruments are European puts at maturities \(1/4,1/2,1\) and strikes (90,100,110), followed by the twelve-fixing arithmetic Asian call spread \((A-95)^+-(A-110)^+\), \(A=\sum_{m=1}^{12}S_{m/12}/12\). The eighth instrument is the annual at-the-money put; \(w=\mathbf e_{10}-\mathbf e_8\) is a prespecified bias comparison, not an optimized hedge.

After conjugate reduction, the complete terminal rows are

\[
F_A(\pi)=C_A\sqrt{K_{767}}\sqrt{a\cdot\pi},\quad C_A>0,\qquad
F_P(\pi)=\frac{1600e^{-.01}}{\pi_{\rm circ}}\sqrt{K_{767}}
\sum_{\omega=8,24,\ldots,120}
\frac{\sqrt{d_\omega\cdot\pi}}
{\sqrt{(\omega^2+1/16)(\omega^2+25/16)}}.\tag{F.25}
\]

Here \(\pi_{\rm circ}\) is the circle constant, while \(\pi\) is the probability vector. The strict inequality \(C_A>0\) is substantive: the simplex Beta coefficient is \(\mathcal M_K(\zeta)=K(12K/100)^{\sum_m\zeta_m}\prod_m\Gamma(\zeta_m)/\Gamma(2+\sum_m\zeta_m)\). The original catalog retains the difference between strikes 95 and 110. Its Gamma factors are finite and nonzero, and the strike factors have unequal magnitudes \(95(11.4)^{1/4}\) and \(110(13.2)^{1/4}\), so at least one coefficient is nonzero.

The exact Asian primal and dual satisfy \(\pi^A\ge0\), \(A\pi^A\le b\), \(y\ge0\), \(A^Ty\ge a\), and \(a\cdot\pi^A=b\cdot y\). Let \(S=\{1,2,6\}\) and let \(J\) be the three positive-dual rows (point \(t=256\) Laplace, mean, mass). The exact compact expression for the witness is

\[
\pi^A_{S}=A_{J,S}^{-1}b_J,\quad \pi^A_{S^c}=0,\qquad
\det A_{J,S}\ne0,\qquad (A^Ty-a)_{S^c}>0.\tag{F.26}
\]

Its nonzero coordinates are approximately \((.0276833515163,\ .0487291439380,\ .923587504546)\). Weak duality proves optimality. Complementary slackness forces any optimizer onto \(S\) and onto the three active equalities; nonsingularity proves uniqueness. The strictly increasing square root transfers uniqueness to \(F_A\).

The same polytope contains an exact \(\pi^B\) supported on \(\{5,6\}\). Let \(D_\omega=(\omega^2+1/16)(\omega^2+25/16)\) and \(x_\omega=d_\omega\cdot\pi^A>0\). For the auxiliary put row \(\mathscr B(\pi)=\sum_\omega\sqrt{d_\omega\cdot\pi}/\sqrt{D_\omega}\),

\[
\left.\frac d{dt}\mathscr B((1-t)\pi^A+t\pi^B)\right|_{t=0}
=\sum_\omega\frac{d_\omega\cdot(\pi^B-\pi^A)}{2\sqrt{D_\omega x_\omega}}
\in[L,U],\qquad L>3\cdot10^{-9}.\tag{F.27}
\]

The exact rational \(L,U\) are the `put_direction.derivative` endpoints in `terminal767-result.json`. This reference specifies them exactly without a large printed fraction. Each coefficient enclosure \([l_\omega,u_\omega]\) obeys \(0<l_\omega\le u_\omega\) and \(4l_\omega^2D_\omega x_\omega\le1\le4u_\omega^2D_\omega x_\omega\); negative profile changes reverse endpoints before summation. Thus the signed full-row derivative is positive. The Asian maximizer is not a put maximizer, so

\[
g^{\rm row}_{767}=\max F_A+\max F_P-\max(F_A+F_P)>0,
\qquad s_{\mathcal B_{767}}(w)-s_{\mathcal E_{767}}(w)\ge g^{\rm row}_{767}>0.\tag{F.28}
\]

The second inequality follows from the coefficient triangle inequality; possible phase cancellation can only further reduce the joint support. With valid timewise product sets and the same complete catalog, the accumulated un-intersected support gap is at least this positive terminal gap. A modified catalog, probability set, or payoff intersection requires renewed analysis.

Within `science/baseline/reference/code/classical/`, the machine appendices are `terminal767-input.json`, `terminal767-result.json`, `verify_input_bounds.py`, and `verify_terminal.py`. The first reader regenerates 22 rows, twelve 767-step Laplace recursions, and all 918 profile entries; the second verifies the 407 exact witness checks. These establish the terminal claims and leave the complete-price premise (F.21), annual monetary endpoints, and any trading interpretation unproved by this example.

### F.8. Standard financial propagation corollary

For compact valid sets \(e=p_h-p_c\in\mathcal E\) and \(n=p_h-\widehat p_h\in\mathcal N\),

\[
\begin{aligned}
w^Tp_h-s_{\mathcal E}(w)&\le w^Tp_c\le w^Tp_h+s_{\mathcal E}(-w),\\
w^T\widehat p_h-s_{\mathcal N}(-w)-s_{\mathcal E}(w)
&\le w^Tp_c\le
w^T\widehat p_h+s_{\mathcal N}(w)+s_{\mathcal E}(-w).
\end{aligned}\tag{F.29}
\]

If the actual \((n,e)\) belongs to a common compact \(\mathcal K\), replace the lower subtraction by \(s_{\mathcal K}(-w,w)\) and the upper addition by \(s_{\mathcal K}(w,-w)\). For a closed calibration acceptance set \(\mathcal Y\),

\[
\begin{aligned}
\mathcal T_\theta&=\{(n,e)\in\mathcal K_\theta:
\widehat p_{h,\rm cal}+n_{\rm cal}-e_{\rm cal}\in\mathcal Y\},\\
\mathcal A_\theta&=\{\widehat p_{h,10}+n_{10}-e_{10}:(n,e)\in\mathcal T_\theta\}.
\end{aligned}\tag{F.30}
\]

The identities \(p_c=p_h-e=\widehat p_h+n-e\) prove these statements. Nonempty \(\mathcal T_\theta\) is compact and attains the target endpoints; emptiness excludes compatibility with the acceptance rule. Enlarging the common input set to a coordinate box enlarges or preserves the target set. These are standard set-propagation consequences, conditional on a valid center and complete error inputs.

## Appendix G. Nonexact trial fields and the signed error identity

This appendix extends the continuous–discrete comparison to one deterministic trial field that need not solve the backward equation. It states sufficient conditions independently of the unknown exact solution, proves the four signed terms, and gives an explicit globally integrable nonexact field. Expectations below are undiscounted; multiply the identity and its bounds by the common discount factor when converting a payoff to a price.

### G.1. State, traces, and admissibility

Use the original laws \(P,Q\), parameters, and correlated positive-part update of Appendix F. Between monthly fixings the state is \(x=(s,v,A_m,\ell_m)\), where \(A_m\) is the sum of the realized normalized stock values and \(\ell_m\) the sum of their logarithms. The fixing map \(J_i\) adds the current \(s,\log s\) to these histories. Between fixings,

\[
\mathcal L=rs\partial_s+(d-\kappa v)\partial_v
+\tfrac12vs^2\partial_{ss}+\rho\xi vs\partial_{sv}
+\tfrac12\xi^2v\partial_{vv}.\tag{G.1}
\]

Choose one fixed nonnegative weight for the entire horizon, for example

\[
\begin{aligned}
W&=e^v\{s^{-1/2}+e^{-\ell_m/24}s^{-(12-m)/24}\},\\
W^{\rm nat}&=e^v\{\mathfrak B_m^{-1/2}+\mathfrak G_m^{-1/2}\},\qquad
\mathfrak B_m=(A_m+(12-m)s)/12,\quad
\mathfrak G_m=e^{\ell_m/12}s^{(12-m)/12}.
\end{aligned}\tag{G.2}
\]

Both weights match exactly across the fixing map. Since the arithmetic mean is at least the geometric mean, \(W^{\rm nat}\le2e^v\mathfrak G_m^{-1/2}\). The history factors in both weights are multidate nonpositive real loadings with total absolute value at most \(1/2\).

**Lemma (weight moments).** At \(\theta_*\), over \(0\le t\le1\), either weight satisfies

\[
\sup_tE_PW(t,X_t)<5/2,\qquad \max_jE_QW(t_j,X_j)<5/2,
\qquad \sup_{\tau\le1}E_PW(\tau,X_\tau)^2<\infty.\tag{G.3}
\]

The last supremum is over the compact-localization stopping times used below. To prove the first bound for a branch, use the generator on \(e^{L+pZ+V}\), with \(p\in[-1/2,0]\). Its variance coefficient is \(\gamma_p-\kappa_p+\xi^2/2<0\), and its constant drift is \(rp+d\le d\). Loading changes cancel at fixings. Nonnegative stopped supermartingales give branch expectation at most \(e^{v_0+d}=e^{9/50}<5/4\). For the discrete law, (F.10)–(F.11) with \(B=1\) and \(F_p(1)\le1\) give a branch bound \(e^{v_0+d+1/300}=e^{11/60}<5/4\). Sum two branches, or use \(W^{\rm nat}\le2e^v\mathfrak G_m^{-1/2}\). The strict comparisons follow from \(\log(5/4)\ge1/5\).

For the squared bound, \((a+b)^2\le2(a^2+b^2)\). Each squared branch has total stock loading at most one and variance loading two. Increasing the latter to four dominates it; the continuous exponential-supermartingale variance coefficient is bounded by \(1-4(1.776)+8(7/25)^2<0\), with constant drift at most \(24/25\). Stopping therefore gives a uniform finite second moment. The same argument covers the natural weight. This is enough for uniform integrability of fields dominated by \(W\); no ordinary martingale assumption on the stopped limiting stochastic integral is needed.

Let \(R\) be the same terminal payoff, or the same exact finite conversion remainder, under both laws. The deterministic field \(\widetilde u\) is locally \(C^{1,2}\) between fixings, admits a right-sided extension at \(v=0\) suitable for Itô's formula, and has genuine one-sided traces uniformly on compact state sets. Require global bounds

\[
\begin{aligned}
|\widetilde u|&\le CW,&
|\mathfrak r(t,x)|&\le\eta_c(t)W(t,x),& \int_0^1\eta_c(t)dt&<\infty,\\
|d_i(x)|&\le\eta_iW(t_i-,x),&
|\delta(x)|&\le\eta_TW(1,x),& C,\eta_i,\eta_T&<\infty.
\end{aligned}\tag{G.4}
\]

Domination includes all states, \(v=0\), and the unbounded tail. Define

\[
\begin{aligned}
\mathscr D_j&=Q_j\widetilde u_{j+1}-\widetilde u_j,&
\mathfrak r&=(\partial_t+\mathcal L)\widetilde u,\\
d_i(x)&=\widetilde u(t_i-,x)-\widetilde u(t_i+,J_ix),&
\delta&=R-\widetilde u_N.
\end{aligned}\tag{G.5}
\]

The jump defect is the left trace minus the right trace after the fixing. The operator \(Q_j\) includes the original kernel and the step-end fixing. Both laws use the same post-fixing terminal convention, counting each update once. The defects \(\mathscr D_j\) must be integrable under \(Q\); a full-horizon enclosure is \(\sum_jE_Q\mathscr D_j\in[L_Q,U_Q]\). A sufficient alternative is \(\lvert\mathscr D_j\rvert\le h\eta_{Q,j}W\).

An exact future-value field belongs to this class after its regularity and domination bounds are verified. A finite representation requires the same growth, residual, trace, terminal-value and original-kernel checks.

### G.2. The four-term signed identity

**Theorem (one-field residual identity).** Under (G.3)–(G.5) and the integrable original-\(Q\) defects,

\[
\boxed{E_QR-E_PR=
\sum_jE_Q\mathscr D_j-E_P\int_0^1\mathfrak r(t,X_t)dt
+\sum_iE_Pd_i+(E_Q-E_P)\delta.}\tag{G.6}
\]

**Proof.** Finite conditional telescoping under \(Q\) gives

\[
E_Q\widetilde u_N-\widetilde u_0=\sum_jE_Q\mathscr D_j.\tag{G.7}
\]

For \(P\), localize in compact state domains, on closed subintervals away from fixings. Itô's formula then has a stochastic integral of expectation zero. The second-moment bound in (G.3) and \(|\widetilde u|\le CW\) make the stopped field values uniformly integrable, so they converge in \(L^1\) when stopping is removed. Tonelli and (G.4) give \(E_P\int|\mathfrak r|\le\int\eta_c(t)E_PW(t,X_t)dt<\infty\), which removes stopping from the time integral by absolute integrable domination. As the subinterval endpoints approach a fixing, compact-uniform genuine traces and continuous paths give almost-sure trace convergence; the same uniform integrability gives \(L^1\) convergence. The actual field jump is \(-d_i\). Summing all intervals and jumps therefore gives

\[
E_P\widetilde u_N-\widetilde u_0
=E_P\int_0^1\mathfrak r(t,X_t)dt-\sum_iE_Pd_i.\tag{G.8}
\]

Subtract (G.8) from (G.7), and add the two terminal defects \(\delta=R-\widetilde u_N\). The common deterministic initial value cancels, giving (G.6). The argument also includes a fixing at the terminal date using the specified post-fixing convention. ∎

If one instead defines \(J_i^{\rm jump}=\widetilde u(t_i+,J_ix)-\widetilde u(t_i-,x)\), its term in (G.6) is \(-\sum_iE_PJ_i^{\rm jump}\). This explicit sign convention avoids mixing the two definitions. For an exact continuation, the backward residual, fixing defects, and terminal discrepancy vanish, recovering (F.8). For a nonexact field all four signed terms remain.

### G.3. Effective sufficient bounds

At \(\theta_*\), (G.6) and the moment lemma imply

\[
\begin{aligned}
|E_QR-E_PR|&\le\max(|L_Q|,|U_Q|)
+\tfrac52\left(\int_0^1\eta_c(t)dt+\sum_i\eta_i\right)+5\eta_T,\\
|E_QR-E_PR|&\le\tfrac52\left(h\sum_j\eta_{Q,j}
+\int_0^1\eta_c(t)dt+\sum_i\eta_i\right)+5\eta_T
\quad\text{if }|\mathscr D_j|\le h\eta_{Q,j}W.
\end{aligned}\tag{G.9}
\]

These are sufficient nonnegative bounds obtained by the triangle inequality. A joint signed enclosure of the four contributions can instead be propagated by its linear image. Separate price intervals alone supply no shared-state compatibility witness. In particular, a necessary lower bound on a residual envelope is not an evaluation of either sufficient upper bound in (G.9).

### G.4. A self-contained nonexact analytic field

Fix \(T=1\), \(\varepsilon>0\), and \(R=s_T^{-1/2}\). Consider

\[
a_\varepsilon(t)=1+\varepsilon t(1-t),\qquad
\widetilde u_\varepsilon(t,x)=a_\varepsilon(t)s^{-1/2},\qquad
1\le a_\varepsilon\le C_\varepsilon:=1+\varepsilon/4.\tag{G.10}
\]

Use \(W_A=s^{-1/2}e^v\), which is a single branch of the preceding weight proof. The field is globally regular for \(s>0,v\ge0\), is independent of the histories, has exact matching fixing traces and terminal value, and obeys \(|\widetilde u_\varepsilon|\le C_\varepsilon W_A\). Its generator residual is

\[
\mathfrak r_\varepsilon=s^{-1/2}
\{\varepsilon(1-2t)+a_\varepsilon(t)(3v/8-r/2)\}.\tag{G.11}
\]

Because \(ve^{-v}\le1/e\), a global dominating function, constant in time, is

\[
\eta_c=\varepsilon+C_\varepsilon(r/2+3/(8e)),\qquad
\int_0^1\eta_c(t)dt=\eta_c<\infty,\qquad \eta_i=\eta_T=0.\tag{G.12}
\]

The original stock Gaussian integral is exact even though the stock and variance share \(G\): this field does not depend on next-step variance. It gives

\[
\mathscr D_j=s^{-1/2}\{a_\varepsilon(t_{j+1})e^{h(3v/8-r/2)}-a_\varepsilon(t_j)\},\qquad
|\mathscr D_j|\le h\eta_QW_A,\quad
\eta_Q=\varepsilon+C_\varepsilon\{r/2+3/[8e(1-3h/8)]\}.\tag{G.13}
\]

For the bound, write the difference as \((a_{j+1}-a_j)e^{h(3v/8-r/2)}+a_j(e^{h(3v/8-r/2)}-1)\). Use \(|a_{j+1}-a_j|\le\varepsilon h\), \(|e^x-1|\le|x|e^{\max(x,0)}\), and \(ve^{-cv}\le1/(ec)\) for \(c=1-3h/8>0\). Thus every discrete defect is integrable, with the explicit full-horizon enclosure \(\sum_jE_Q\mathscr D_j\in[-(5/2)\eta_Q,(5/2)\eta_Q]\), because \(Nh=1\). Substitution into (G.9) gives the finite sufficient bound \((5/2)(\eta_Q+\eta_c)\).

At \(t=1/2,v=r>0\), (G.11) equals \(-rC_\varepsilon s^{-1/2}/8<0\). Therefore this field is not the exact future-value function. The exact field for the same negative-power payoff exists by the affine continuation and moment proof of Appendix F, with loading \(-1/2\). The same admissible object class contains both exact and nonexact fields; the four-term identity applies to each. This example is an analytic scope witness, not a numerical certificate for the original market instruments.

### G.5. The thirteen-function diagnostic

The saved classical trial-field diagnostic has a distinct, conditional role. With \(n=12-m\), \(B=(A_m+ns)/12\), \(y=A_m/(A_m+ns)\), \(\beta=1-y\), and \(z=v/(1+v)\), its branch is \(B^{-q}P(y,v)\). In this subsection \(\Re q=1/2\), so \(B^{-q}\) corresponds to negative stock damping; this \(q\) is not the negative loading \(q\) used in Appendix F. The conjugated generator is

\[
\begin{aligned}
\mathcal L_qP={}&-ry\beta P_y+dP_v-qr\beta P\\
&+v\{\tfrac12y^2\beta^2P_{yy}-\rho\xi y\beta P_{yv}
+\tfrac12\xi^2P_{vv}+(1+q)y\beta^2P_y\\
&\hspace{12mm}-(\kappa+q\rho\xi\beta)P_v+\tfrac12q(q+1)\beta^2P\}.
\end{aligned}\tag{G.14}
\]

The basis consists of \(\phi_{ij}=\beta y^iz^j\), \(0\le i\le2,0\le j\le3\), and \(\psi=v\beta^2\). It exactly represents the terminal forcing \(\mathcal L_q1=-qr\phi_{00}+q(q+1)\psi/2\). This is completion of the terminal generator, not closure under every generator image. For finite endpoint constants, the field uses cubic Hermite interpolation with exact physical slopes \(-Kc-g(q)\), where \(g(q)=-qr e_{00}+q(q+1)e_\psi/2\). The exact fixing carry, with \(\gamma=(n-1)/n\), is

\[
(T_nc)_{\ell j}=\gamma\sum_{i=\ell}^2\binom i\ell\gamma^\ell n^{-i+\ell}c_{ij},
\qquad T_n\psi=\gamma^2\psi.\tag{G.15}
\]

It follows from \(y'=\gamma y+1/n\), \(B'=B\), and \(\beta'=\gamma\beta\). Terminal correction nodes are zero. Exact carries and slopes specify the traces; floating generation values do not replace these definitions. The finite field has \(|P|\le C_0+C_1v\le(C_0+2C_1/e)e^{v/2}\). Its continuous residual is a polynomial of degree at most two in \(v\) with bounded \(y,z\) coefficients, so \(e^{-v}|F|\le a_0+a_1/e+4a_2/e^2\). A complete application of (G.9) still requires the actual coefficient bank, all-state original-\(Q\) envelopes, and full-horizon sufficient upper bounds.

For the saved first-month state \(m=0,y=0,v=9/200\), let \(w=(1,z,z^2,z^3,0,\ldots,0,v)\), \(\ell\) be the generator-value row of the basis, and \(\ell_0=-qr+q(q+1)v/2\). Exact integration over one piece gives

\[
\int F_{A,q}dt=
\left[w+\frac{h^2}{12}\ell K\right](c_R-c_L)
+\frac h2\ell(c_L+c_R)+h\ell_0.\tag{G.16}
\]

Indeed \(\int c(t)dt=h(c_L+c_R)/2+h^2(s_L-s_R)/12\), and \(s_L-s_R=K(c_R-c_L)\). The archive contains all 3080 weighted complex integral intervals (385 modes and eight cells, covering the original 64 time pieces). At common phase zero, sum the real mode intervals on each cell, apply \(\int|F|\ge|\int F|\), and subtract the integrated geometric-branch upper bound. The exact aggregate is specified by the mathematical field `whole_lower` in `field-result.json`:

\[
\int_0^{1/12}\eta_c(t)dt\ge L_*,\qquad
L_*>0.003407444052031154>0.\tag{G.17}
\]

The bound rejects the selected allocation \(\int\eta_c\le1/1000\), recorded as `FAIL_SELECTED_INTEGRATED_PDE_CONTRACT_ONLY`. It is a necessary-condition diagnostic for this field. The reader `verify_field_receipt.py` checks the exact aggregation of saved intervals; the absent coefficient bank prevents regeneration of the direct integration. The diagnostic does not optimize over the trial space or give a lower bound on signed price bias. The explicit field (G.10) separately proves nonexact admissibility, and a complete annual monetary certificate remains open.

The files in `science/baseline/reference/code/classical/` are `field-cell-integrals.json`, `field-result.json`, `field-independent-readback.json`, `provenance.json`, and `verify_field_receipt.py`. Publication manifests fix their identities.

## References

1. **GR2019.** Gatheral, Jim and Radoičić, Radoš. *Rational Approximation of the Rough Heston Solution*. International Journal of Theoretical and Applied Finance 22(3), 1950010, 2019. DOI [10.1142/S0219024919500109](https://doi.org/10.1142/S0219024919500109). The SSRN manuscript dated January 29, 2019 is used.

2. **GR2023.** Gatheral, Jim and Radoičić, Radoš. *A Generalization of the Rational Rough Heston Approximation*. Quantitative Finance 24(2), 329–335, 2024. DOI [10.1080/14697688.2024.2302055](https://doi.org/10.1080/14697688.2024.2302055). [Source](https://arxiv.org/abs/2310.09181v1). Preprint consulted: arXiv:2310.09181.

3. **JK2020.** Siow Woon Jeng and Adem Kiliçman. *Series Expansion and Fourth-Order Global Padé Approximation for a Rough Heston Solution*. Mathematics 8(11), 1968, 2020. DOI [10.3390/math8111968](https://doi.org/10.3390/math8111968).

4. **JK2021.** Siow Woon Jeng and Adem Kiliçman. *SPX Calibration of Option Approximations under Rough Heston Model*. Mathematics 9(21), 2675, 2021. DOI [10.3390/math9212675](https://doi.org/10.3390/math9212675).

5. **AbiJaberElEuch2018.** Abi Jaber, Eduardo and El Euch, Omar. *Markovian structure of the Volterra Heston model*. Statistics & Probability Letters 149, 63–72, 2019. DOI [10.1016/j.spl.2019.01.024](https://doi.org/10.1016/j.spl.2019.01.024). Preprint consulted: arXiv:1803.00477.

6. **LiLiu2018.** Li, Lei and Liu, Jian-Guo. *A Generalized Definition of Caputo Derivatives and Its Application to Fractional ODEs*. SIAM Journal on Mathematical Analysis 50(3), 2867–2900, 2018. DOI [10.1137/17M1160318](https://doi.org/10.1137/17M1160318). The convexity result is Proposition 3.11.

7. **Simon2014.** Simon, Thomas. *Comparing Fréchet and positive stable laws*. 2014. [Source](https://arxiv.org/abs/1310.1888v2). Preprint consulted: arXiv:1310.1888.

8. **TrefethenWeideman2014.** Trefethen, Lloyd N. and Weideman, J. A. C. *The Exponentially Convergent Trapezoidal Rule*. SIAM Review 56(3), 385–458, 2014. DOI [10.1137/130932132](https://doi.org/10.1137/130932132). Strip quadrature is covered by Theorem 5.1.

9. **NIST2010.** Olver, Frank W. J. and Lozier, Daniel W. and Boisvert, Ronald F. and Clark, Charles W. *NIST Handbook of Mathematical Functions*. Cambridge University Press, 2010. [Source](https://dlmf.nist.gov/).

10. **BBWeak2023.** Bayer, Christian and Breneis, Simon. *Weak Markovian Approximations of Rough Heston*. 2023. [Preprint](https://arxiv.org/abs/2309.07023v1), [original PDF](https://arxiv.org/pdf/2309.07023v1). Preprint consulted: arXiv:2309.07023, submitted 13 September 2023. The characteristic-function and European-payoff error results are Theorems 2.2 and 2.7.

11. **BBSimulation2023.** Bayer, Christian and Breneis, Simon. *Efficient option pricing in the rough Heston model using weak simulation schemes*. 2023. [Preprint](https://arxiv.org/abs/2310.04146v1), [original PDF](https://arxiv.org/pdf/2310.04146v1). Preprint consulted: arXiv:2310.04146, submitted 6 October 2023. The cited preprint reports second-order weak convergence numerically on p. 4.

12. **Kopteva2021.** Kopteva, Natalia. *Pointwise-in-time a posteriori error control for time-fractional parabolic equations*. Applied Mathematics Letters 123, 107515, 2022. DOI [10.1016/j.aml.2021.107515](https://doi.org/10.1016/j.aml.2021.107515). [Preprint](https://arxiv.org/abs/2105.05848v2), [original PDF](https://arxiv.org/pdf/2105.05848v2). Preprint consulted: arXiv:2105.05848, revised 5 July 2021; first submitted 12 May 2021. The pointwise residual bound and norm inequality are Theorem 2.2 and Lemma 2.8.

13. **ElEuchRosenbaum2017.** El Euch, Omar and Rosenbaum, Mathieu. *Perfect hedging in rough Heston models*. arXiv:1703.05049, 2017. [Paper](https://arxiv.org/abs/1703.05049v1). The analytical decreasing-curve example is not a new model-admissibility theorem.

14. **SimonCM2015.** Simon, Thomas. *Mittag-Leffler functions and complete monotonicity*. Integral Transforms and Special Functions 26(1), 36–50, 2015. DOI [10.1080/10652469.2014.965704](https://doi.org/10.1080/10652469.2014.965704). [Paper](https://arxiv.org/abs/1312.4513v2).

15. **BL2025.** Boyarchenko, Svetlana; de Innocentis, Marco; and Levendorskii, Sergei. *Fast reliable pricing and calibration of the rough Heston model*. arXiv:2508.15080, 2025. [Paper](https://arxiv.org/abs/2508.15080v1). Modified Adams is Section 3.2; Conformal Bootstrap is Section 4.10.

16. **BenHammouda2026.** Ben Hammouda, Chiheb; Ben Romdhane, Abderrahmene; Samet, Michael; and Tempone, Raul F. *Single- and Multilevel Quadrature with Error Control for Fourier Pricing under the Rough Heston Model*. arXiv:2609.00438, 2026. [Paper](https://arxiv.org/abs/2609.00438v1). Practical tolerance interpretation: Section 3.2.

17. **HK2026.** Hager, Paul P. and Kreher, Dörte. *Expanding the rough Heston model in H*. arXiv:2606.16619, 2026. [Paper](https://arxiv.org/abs/2606.16619v1).
