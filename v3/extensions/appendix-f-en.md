## Appendix F. Original-chain classical Heston inclusion

This appendix supplies a second, classical-Heston upstream implementation of the joint-error interface. Its model-specific content is the passage from the correlated positive-part chain to a common original-law probability vector. The support-function and financial propagation steps use standard convex analysis. The terminal witness proves strict improvement of an outer set; it does not provide a complete annual monetary pricing certificate.

### F.1. The two laws and admissible modes

Write \(s=S/100=e^Z\), \(d=\kappa\bar v\), \(r=1/100\), \(h=1/768\), and \(s_0=1\). The continuous law \(P\) and the original discrete law \(Q\) are

\[
\begin{aligned}
dZ_t&=(r-V_t/2)dt+\sqrt{V_t}(\rho\,dW_t+\sqrt{1-\rho^2}\,dB_t),\\
dV_t&=(d-\kappa V_t)dt+\xi\sqrt{V_t}\,dW_t,\\
Y&=dh+(1-\kappa h)v+\xi\sqrt{hv}\,G,\qquad V'=Y^+,\\
Z'&=z+rh-hv/2+\sqrt{hv}(\rho G+\sqrt{1-\rho^2}H).
\end{aligned}\tag{F01}
\]

Here \(G,H\) are independent standard normal variables, and the same \(G\) drives both discrete updates. Throughout the common-moment argument,

\[
\kappa\in[2,4],\quad \bar v,v_0\in[3/100,3/50],\quad
\xi\in[9/50,7/25],\quad \rho\in[-4/5,-3/10].\tag{F02}
\]

A finite multidate mode has loadings \(\alpha_{i,n}\in\mathbb C\) satisfying

\[
\Re\alpha_{i,n}\le0,\qquad \sum_n|\Re\alpha_{i,n}|\le1/2.\tag{F03}
\]

The realized prefix is \(H_{ji}\); the remaining stock loading is \(q_{ji}=p_{ji}+i\omega_{ji}\). All observation dates lie on the grid. A fixing moves one loading from the remaining sum to the realized prefix, without changing the underlying mode.

### F.2. Exact continuation, the full kernel, and integrability

**Lemma (exact continuous continuation).** The affine continuation \(u=e^{qz+a+bv}\), initialized with terminal \(a=b=0\), is the continuous conditional expectation of the mode. Between fixings, in remaining-time coordinates,

\[
b'=\tfrac12\xi^2b^2+(\rho\xi q-\kappa)b+\tfrac12(q^2-q),
\qquad a'=rq+db.\tag{F04}
\]

At fixings \(q\) changes and \(a,b\) continue without resetting. To prove existence, set \(\kappa_p=\kappa-p\rho\xi\), \(\gamma_p=(p^2-p)/2\). On \(\Re b=1\), the real drift is

\[
\tfrac12\xi^2-\kappa_p+\gamma_p
-\tfrac12\{(\xi\Im b+\rho\omega)^2+(1-\rho^2)\omega^2\}<0,
\qquad
\frac{d|b|}{dt}\le(\xi^2/2-\kappa_p)|b|+|q^2-q|/2.\tag{F05}
\]

Indeed \(p\in[-1/2,0]\), \(\kappa_p\ge1.888\), and \(\gamma_p\le3/8\). The first-crossing argument gives \(\Re b\le1\); the radial estimate excludes explosion on every finite segment. Also \(\Re a\le(6/25)T\).

The identification with an expectation requires more than formal Riccati algebra. Multiply the real loadings by \(5/4\), and let \(L_*(t),p_*(t)\) be the resulting realized and remaining contributions. Then

\[
\mathcal Y_t=e^{L_*(t)+p_*(t)Z_t+4V_t-(24/25)t},\qquad
|\mathcal M_\tau|^{5/4}
\le e^{(5/4)(6/25)T+(24/25)T}\mathcal Y_\tau.\tag{F06}
\]

Here \(\mathcal M\) is the stopped affine local martingale associated with the mode. The process \(\mathcal Y\) is a nonnegative local supermartingale: its constant drift is nonpositive, and its variance drift is at most \(65/128-4(1.86)+8(7/25)^2<0\). Loading changes cancel at each fixing. Compact stopping and (F06) give a uniform \(5/4\)-moment bound. Uniform integrability removes stopping, proves the conditional-expectation identity, and covers \(v=0\) and every finite initial state.

The actual one-step propagation retains the entire positive-part Gaussian kernel. For next-step coefficients \(a,b,q\), integration over \(H\) gives

\[
\frac{Q_hu(z,v)}{e^{qz}}=
e^{a+qrh-qhv/2+q^2(1-\rho^2)hv/2}
\int_{\mathbb R}\varphi(g)
e^{q\rho\sqrt{hv}g+b[dh+(1-\kappa h)v+\xi\sqrt{hv}g]^+}\,dg.\tag{F07}
\]

For \(v>0\) the integral splits at \(g_0=-(dh+(1-\kappa h)v)/(\xi\sqrt{hv})\): the first part has variance exponent zero, and the second uses the positive candidate. Both parts are retained. At \(v=0\), \(V'=dh\) deterministically. Completing a real Gaussian square is an integration device, not a replacement of \(Q\) by a mode-dependent probability law.

Let \(D_{ji}(v)\) be this actual propagation minus the exact continuous continuation, after removal of the common \(e^{q_{ji}z}\). Finite conditional telescoping, including each fixing exactly once, yields

\[
\Phi_{Q,i}-\Phi_{P,i}=\sum_{j=0}^{N-1}r_{ji},\qquad
r_{ji}=E_Q[H_{ji}e^{q_{ji}Z_j}D_{ji}(V_j)].\tag{F08}
\]

The integrability in the next subsection justifies every discrete expectation in this identity.

### F.3. Original-law moments and shared occupation probabilities

**Lemma (discrete exponential moment).** For nonpositive real multidate loadings of total absolute value at most one,

\[
E_Q\exp\!\left\{\sum_{n\le j}\beta_n Z_n+4V_j\right\}
\le K_j:=e^{6/25+(73/75)jh}.\tag{F09}
\]

To prove it, complete the real stock square for \(p\in[-1,0]\). The candidate mean becomes \(dh+\eta_pv\), where \(\eta_p=1-\kappa_ph\ge191/192\). Since \((-y)^+\le h(25e)^{-1}e^{-25y/h}\),

\[
E(-Y_p)^+\le\frac{h}{25e}
\exp\!\left\{-25d+\frac{[-25\eta_p+(625/2)\xi^2]v}{h}\right\}
\le\frac{h}{25e^{5/2}}<h/300.\tag{F10}
\]

The parameter bounds imply \(d\ge3/50\), the variance coefficient is at most \(-71/192\), and \(e^{5/2}>12\). The negative part is exactly zero at \(v=0\). For \(B\ge0\), \(e^{By^+}\le e^{By}+B(-y)^+\). Defining \(F_p(B)=\gamma_ph+\eta_pB+\xi^2hB^2/2\), Gaussian integration therefore gives

\[
\begin{aligned}
E_Q[e^{pZ'+BV'}\mid z,v]
&\le e^{pz+prh}\{e^{Bdh+F_p(B)v}+Bh\,e^{\gamma_phv}/300\},\\
E_Q[e^{pZ'+4V'}\mid z,v]
&\le e^{pz+4v}(e^{4dh}+4h/300)
\le e^{pz+4v+(73/75)h}.
\end{aligned}\tag{F11}
\]

Here \(F_p(4)\le4\), \(rp\le0\), and \(4d\le24/25\). Successive conditioning and cancellation of loading changes prove (F09), using \(4v_0\le6/25\).

For a finite partition \(I_r\) of \([0,\infty\)), retain the zero atom and the unbounded tail, and set

\[
\pi_{jr}=Q(V_j\in I_r),\quad
h_{jir}\ge\sup_{v\in I_r}|e^{-2v}D_{ji}(v)|^2,\quad
|r_{ji}|^2\le K_j\sum_rh_{jir}\pi_{jr}=:\mathbf a_{ji}\cdot\pi_j.\tag{F12}
\]

The last inequality is complex Cauchy–Schwarz applied to \(H_{ji}e^{q_{ji}Z_j}e^{2V_j}\) and \(e^{-2V_j}D_{ji}(V_j)\); its first squared moment is covered by the doubled loadings in (F09). Thus every mode uses the same original-chain probability vector. If a trial defect depends on additional states, one must bound uniformly over those states or enlarge the partition. Continuous-law residuals do not inherit these \(Q\)-probabilities.

### F.4. A valid terminal probability polytope

Fix \(\theta_*=(\kappa,\bar v,\xi,\rho,v_0)=(3,9/200,23/100,-11/20,9/200)\), \(j=767\), \(d=27/200\), and \(\eta=255/256\). Use

\[
I_0=\{0\},\quad I_r=((r-1)/100,r/100]\ (1\le r\le100),
\quad I_{101}=(1,\infty).\tag{F13}
\]

For \(v>0\) the next-step zero mass is \(\Phi(-(dh+\eta v)/(\xi\sqrt{hv}))\); at \(v=0\) it is zero. Projection excess satisfies \(E[-dh-\eta v-\xi\sqrt{hv}G]^+\le h\xi^2e^{-d\eta/\xi^2}/(\eta\sqrt{2\pi e})<h/200\). This follows by writing \(v=hz\), bounding the normal negative part by its density term, and maximizing \(\sqrt z e^{-\eta^2z/(2\xi^2)}\). The mean recursion and the positive-exponential recursion give

\[
EV_n\le\mu:=7/150,\qquad
M_{n+1}\le e^{4dh}M_n^{\beta}+h/50,\qquad
Ee^{4V_n}\le5/4,\quad Ee^{-tV_n}\ge e^{-t\mu}.\tag{F14}
\]

Here \(M_n=Ee^{4V_n}\), \(\lambda=\kappa-2\xi^2=14471/5000\), and \(\beta=1-\lambda h\in(0,1)\). Concavity of \(x^\beta\) gives the displayed recursion. At \(M=5/4\), use \(\log(5/4)\ge1/5\), \(4d-\lambda/5=-971/25000\), and \(1-e^{-x}\ge x/2\) for \(0\le x\le1\); the decrease exceeds \(h/50\). Since \(M_0=e^{.18}<5/4\), induction proves the positive-exponential bound. Jensen gives the Laplace lower bound.

For \(t\in\mathcal T=\{1,4,16,64,256,(191/192)^2/[2(49/625)h]\}\), define

\[
t_0=t,\quad t_{n+1}=\eta_*t_n-c_*t_n^2,\qquad
L_{767}(t)=\exp\!\left[-d_*h\sum_{n=0}^{766}t_n-v_*t_{767}\right].\tag{F15}
\]

The reference quadruple is \((\eta_*,c_*,d_*,v_*)=(191/192,(49/625)h/2,3/50,3/100)\), and the point quadruple is \((255/256,\xi^2h/2,27/200,9/200)\). The bound \(e^{-tY^+}\le e^{-tY}\) and Gaussian integration give \(E[e^{-tV'}\mid v]\le e^{-dht}e^{-(\eta t-\xi^2ht^2/2)v}\). All 767 recursion steps satisfy \(0\le t_n\le\eta_* /(2c_*)\). Consequently the recursion is monotone on the certified enclosures; the conservative reference choices yield a valid upper bound throughout (F02).

The true terminal probability vector satisfies

\[
\begin{aligned}
\sum_r\inf_{I_r}e^{-tv}\pi_r&\le L^{\rm ref}_{767}(t),&
\sum_r\inf_{I_r}e^{-tv}\pi_r&\le L^{\rm point}_{767}(t),\\
\sum_r\sup_{I_r}e^{-tv}\pi_r&\ge e^{-t\mu},&
\sum_r\ell_r\pi_r&\le\mu,\quad \sum_re^{4\ell_r}\pi_r\le5/4,
\end{aligned}\tag{F16}
\]

together with nonnegativity and mass one; \(\ell_r=\inf I_r\). The zero Laplace coefficient is one, and the tail infimum/supremum are zero/\(e^{-t}\). The six triples, two moment rows, and two signed mass rows give 22 inequalities. Upper-bound rows use lower coefficient endpoints and upper right endpoints; lower-bound rows use upper coefficients and lower right endpoints before sign reversal. Thus the saved rational \(\mathcal P_{767}=\{\pi\ge0:A\pi\le b\}\) contains the actual probabilities and is a nonempty compact subset of the simplex.

### F.5. Certified terminal profiles on the entire variance axis

At the final step the future variance exponent is zero, so its positive-part correction vanishes exactly. For \(q=p+i\omega\), write \(g=(q^2-q)/2\), \(L=\rho\xi q-\kappa\), \(c=\xi^2/2\). Then

\[
D_q(v)=e^{rqh+hgv}-e^{a(h)+B(h)v},\quad
B'=g+LB+cB^2,\ B(0)=0,\qquad a(h)=rqh+d\int_0^hB(t)dt.\tag{F17}
\]

At \(\theta_*\), the Asian representative is \((p,\omega)=(-1/48,64)\), and the put representatives are \((-1/4,-8),(-1/4,-24),\ldots,(-1/4,-120)\). On \(\Re B=0\) the real drift is at most \(p(p-1)/2-(279/800)\omega^2<0\); hence \(\Re B\le0\) and \(\lvert B(t)\rvert\le|g|t\).

Let \(P_3(t)=b_1t+b_2t^2+b_3t^3\), where \(b_1=g\), \(b_2=Lg/2\), \(b_3=(L^2g+2cg^2)/6\). The exact guard \(\Re b_1+\max(\Re b_2,0)h+\max(\Re b_3,0)h^2<0\) proves \(\Re P_3\le0\). Its residual is \(-\sum_{k=3}^6r_kt^k\), with \(r_3=Lb_3+2cb_1b_2\), \(r_4=c(2b_1b_3+b_2^2)\), \(r_5=2cb_2b_3\), \(r_6=cb_3^2\). Since \(\Re[L+c(B+P_3)]\le-\kappa_p\), variation of constants gives

\[
E_B=\sum_{k=3}^6|r_k|_+\frac{h^{k+1}}{k+1},\qquad
E_A=d\sum_{k=3}^6|r_k|_+\frac{h^{k+2}}{(k+1)(k+2)}.\tag{F18}
\]

The notation \(|\cdot|_+\) denotes a certified upper modulus. Set

\[
\begin{aligned}
A_q&=\min\{|{-d\int_0^hP_3}|_++E_A,\ d|g|_+h^2/2\},\\
B_q&=\min\{|hg-P_3(h)|_++E_B,\ (|L|_++\xi^2|g|_+h)|g|_+h^2/2\},\\
m_q&=2-\max\{h\Re g,\min(0,\Re P_3(h)+E_B)\}>0.
\end{aligned}\tag{F19}
\]

The exponential-difference integral formula, and the coarse modulus bound for the two exponentials, imply

\[
|e^{-2v}D_q(v)|\le e^{prh}(A_q+B_qv)e^{-m_qv},\qquad
h_{qr}=\min\{[4e^{2prh-4\ell_r}]_+,[e^{2prh}S_{qr}^2]_+\},\quad
S_{qr}=\sup_{v\in I_r}(A_q+B_qv)e^{-m_qv}.\tag{F20}
\]

The supremum uses finite endpoints of each band closure and the stationary point \(1/m_q-A_q/B_q\) when present. For \(B_q=0\), use the monotone branch without division. The tail limit is zero, and the zero band is evaluated at zero. Exact outward arithmetic verifies both Riccati guards and all 918 entries (nine modes, 102 bands), including the tail. The Asian conjugate has the identical profile.

### F.6. Joint inclusion and its exact strictness criterion

Suppose the same finite mode catalog gives the complete discounted-price decomposition

\[
e_k=p_{h,k}-p_{c,k}=\Re\sum_{j,i}c_{ki}r_{ji}+R_k,\qquad |R_k|\le\varrho_k.\tag{F21}
\]

The coefficients and the remainder bounds must include all required conversion, truncation, and arithmetic contributions. The terminal witness alone does not establish this full-price premise. Let \(\mathcal F\) be nonempty, compact, convex, and contain the actual full occupation tuple \(\Pi=(\pi_j)_j\). Define

\[
\mathcal E=\left\{\left(\Re\sum_{j,i}c_{ki}z_{ji}\right)_k:
\Pi\in\mathcal F,\ |z_{ji}|^2\le\mathbf a_{ji}\cdot\pi_j\right\}
+\prod_k[-\varrho_k,\varrho_k].\tag{F22}
\]

**Proposition (joint price inclusion).** This set is nonempty, compact, convex, centrally symmetric, and contains the actual \(e\). Its support is

\[
s_{\mathcal E}(w)=\max_{\Pi\in\mathcal F}\sum_{j,i}
\left|\sum_kw_kc_{ki}\right|\sqrt{\mathbf a_{ji}\cdot\pi_j}
+\sum_k|w_k|\varrho_k.\tag{F23}
\]

**Proof.** The lifted constraints are convex because \(\lvert z\rvert^2\) is convex and the right side is affine; they are closed and bounded over compact \(\mathcal F\). Their linear image plus the remainder box has the stated geometric properties. The actual \((\Pi,r)\) is feasible by (F12). For fixed \(\Pi\), the support of each complex disk is its radius times the modulus of the real-linear coefficient. Independent disk phases attain the sum; the common maximization then gives (F23). With cross-time constraints retain \(\max_{\mathcal F}\sum_j\), rather than \(\sum_j\max\); separation is justified only for \(\mathcal F=\prod_j\mathcal P_j\). ∎

Put \(F_k(\Pi)=\sum_{j,i}|c_{ki}|\sqrt{\mathbf a_{ji}\cdot\pi_j}\), \(m_k=\max_{\mathcal F}F_k\), and \(\mathcal B=\operatorname{rect}(\mathcal E)=\prod_k[-m_k-\varrho_k,m_k+\varrho_k]\). Then

\[
\begin{aligned}
s_{\mathcal B}(w)-s_{\mathcal E}(w)
=\min_{\Pi\in\mathcal F}\Big\{
&\sum_k|w_k|[m_k-F_k(\Pi)]\\
&+\sum_{j,i}\big[\sum_k|w_kc_{ki}|-|\sum_kw_kc_{ki}|\big]
\sqrt{\mathbf a_{ji}\cdot\pi_j}\Big\}.
\end{aligned}\tag{F24}
\]

Every summand is nonnegative. The gap is zero precisely when one common \(\Pi_*\) maximizes every active complete pricing row and all nonzero \(w_kc_{ki}\) in each positive-radius disk lie on a common nonnegative complex ray. No phase condition is required at zero radius; \(w=0\) has zero gap. Adding and subtracting the common row values proves (F24), and compactness makes the minimum attained. Absence of such a witness therefore proves strict improvement over the smallest coordinate box of the same outer set. It proves neither boundary attainment by the actual bias nor an actual-error lower bound. After payoff intersections, apply the criterion anew to the resulting set.

### F.7. A complete terminal-row separation witness

The instruments are European puts at maturities \(1/4,1/2,1\) and strikes (90,100,110), followed by the twelve-fixing arithmetic Asian call spread \((A-95)^+-(A-110)^+\), \(A=\sum_{m=1}^{12}S_{m/12}/12\). The eighth instrument is the annual at-the-money put; \(w=\mathbf e_{10}-\mathbf e_8\) is a prespecified bias comparison, not an optimized hedge.

After conjugate reduction, the complete terminal rows are

\[
F_A(\pi)=C_A\sqrt{K_{767}}\sqrt{a\cdot\pi},\quad C_A>0,\qquad
F_P(\pi)=\frac{1600e^{-.01}}{\pi_{\rm circ}}\sqrt{K_{767}}
\sum_{\omega=8,24,\ldots,120}
\frac{\sqrt{d_\omega\cdot\pi}}
{\sqrt{(\omega^2+1/16)(\omega^2+25/16)}}.\tag{F25}
\]

Here \(\pi_{\rm circ}\) is the circle constant, while \(\pi\) is the probability vector. The strict inequality \(C_A>0\) is substantive: the simplex Beta coefficient is \(\mathcal M_K(\zeta)=K(12K/100)^{\sum_m\zeta_m}\prod_m\Gamma(\zeta_m)/\Gamma(2+\sum_m\zeta_m)\). The original catalog retains the difference between strikes 95 and 110. Its Gamma factors are finite and nonzero, and the strike factors have unequal magnitudes \(95(11.4)^{1/4}\) and \(110(13.2)^{1/4}\), so at least one coefficient is nonzero.

The exact Asian primal and dual satisfy \(\pi^A\ge0\), \(A\pi^A\le b\), \(y\ge0\), \(A^Ty\ge a\), and \(a\cdot\pi^A=b\cdot y\). Let \(S=\{1,2,6\}\) and let \(J\) be the three positive-dual rows (point \(t=256\) Laplace, mean, mass). The exact compact expression for the witness is

\[
\pi^A_{S}=A_{J,S}^{-1}b_J,\quad \pi^A_{S^c}=0,\qquad
\det A_{J,S}\ne0,\qquad (A^Ty-a)_{S^c}>0.\tag{F26}
\]

Its nonzero coordinates are approximately ((.0276833515163,.0487291439380,.923587504546)). Weak duality proves optimality. Complementary slackness forces any optimizer onto \(S\) and onto the three active equalities; nonsingularity proves uniqueness. The strictly increasing square root transfers uniqueness to \(F_A\).

The same polytope contains an exact \(\pi^B\) supported on ({5,6}). Let \(D_\omega=(\omega^2+1/16)(\omega^2+25/16)\) and \(x_\omega=d_\omega\cdot\pi^A>0\). For the auxiliary put row \(\mathscr B(\pi)=\sum_\omega\sqrt{d_\omega\cdot\pi}/\sqrt{D_\omega}\),

\[
\left.\frac d{dt}\mathscr B((1-t)\pi^A+t\pi^B)\right|_{t=0}
=\sum_\omega\frac{d_\omega\cdot(\pi^B-\pi^A)}{2\sqrt{D_\omega x_\omega}}
\in[L,U],\qquad L>3\cdot10^{-9}.\tag{F27}
\]

The exact rational \(L,U\) are the `put_direction.derivative` endpoints in `terminal767-result.json`. This reference specifies them exactly without a large printed fraction. Each coefficient enclosure \([l_\omega,u_\omega]\) obeys \(0<l_\omega\le u_\omega\) and \(4l_\omega^2D_\omega x_\omega\le1\le4u_\omega^2D_\omega x_\omega\); negative profile changes reverse endpoints before summation. Thus the signed full-row derivative is positive. The Asian maximizer is not a put maximizer, so

\[
g^{\rm row}_{767}=\max F_A+\max F_P-\max(F_A+F_P)>0,
\qquad s_{\mathcal B_{767}}(w)-s_{\mathcal E_{767}}(w)\ge g^{\rm row}_{767}>0.\tag{F28}
\]

The second inequality follows from the coefficient triangle inequality; possible phase cancellation can only further reduce the joint support. With valid timewise product sets and the same complete catalog, the accumulated un-intersected support gap is at least this positive terminal gap. A modified catalog, probability set, or payoff intersection requires renewed analysis.

The machine appendix paths are `baseline/english-heston-release/code/classical/terminal767-input.json`, `terminal767-result.json`, `verify_input_bounds.py`, and `verify_terminal.py`. The first reader regenerates 22 rows, twelve 767-step Laplace recursions, and all 918 profile entries; the second verifies the 407 exact witness checks. These establish the terminal claims and leave the complete-price premise (F21), annual monetary endpoints, and any trading interpretation unproved by this example.

### F.8. Standard financial propagation corollary

For compact valid sets \(e=p_h-p_c\in\mathcal E\) and \(n=p_h-\widehat p_h\in\mathcal N\),

\[
\begin{aligned}
w^Tp_h-s_{\mathcal E}(w)&\le w^Tp_c\le w^Tp_h+s_{\mathcal E}(-w),\\
w^T\widehat p_h-s_{\mathcal N}(-w)-s_{\mathcal E}(w)
&\le w^Tp_c\le
w^T\widehat p_h+s_{\mathcal N}(w)+s_{\mathcal E}(-w).
\end{aligned}\tag{F29}
\]

If the actual \((n,e)\) belongs to a common compact \(\mathcal K\), replace the lower subtraction by \(s_{\mathcal K}(-w,w)\) and the upper addition by \(s_{\mathcal K}(w,-w)\). For a closed calibration acceptance set \(\mathcal Y\),

\[
\begin{aligned}
\mathcal T_\theta&=\{(n,e)\in\mathcal K_\theta:
\widehat p_{h,\rm cal}+n_{\rm cal}-e_{\rm cal}\in\mathcal Y\},\\
\mathcal A_\theta&=\{\widehat p_{h,10}+n_{10}-e_{10}:(n,e)\in\mathcal T_\theta\}.
\end{aligned}\tag{F30}
\]

The identities \(p_c=p_h-e=\widehat p_h+n-e\) prove these statements. Nonempty \(\mathcal T_\theta\) is compact and attains the target endpoints; emptiness excludes compatibility with the acceptance rule. Enlarging the common input set to a coordinate box enlarges or preserves the target set. These are standard set-propagation consequences, conditional on a valid center and complete error inputs.
