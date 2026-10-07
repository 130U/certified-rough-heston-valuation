# Classical Heston extension: scope and separate guarantees

This extension preserves the original-chain theory. It does not establish a complete annual currency-valued pricing certificate and is not a main contribution of the rough-Heston paper.

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

The zero band is evaluated at $v=0$; the tail includes its endpoint enclosure, any stationary point, and its zero limit. Rational outward checks cover the guards for all nine modes and all 918 profile entries. These inputs and the primal-dual witness in Appendix D.2.4 close the terminal example's computational obligations. Strict terminal outer-set tightening alone does not give a money-valued annual pricing-error bound.


## Appendix D. Classical Heston: Shared States and Trial-Field Residuals

This section keeps the classical sign \(\Delta^C=p_Q-p_P\). Model-minus-discrete error is its negative. Common probabilities belong only to the stated original \(Q\) chain; continuous residuals are integrated under \(P\). Appendix C gives the original-chain moment and constraint proof.

### Appendix D.1. Fixed mathematical setting

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

### Appendix D.2. Shared state constraints for the original chain

#### Appendix D.2.1. Structural conditions and the core argument

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

#### Appendix D.2.2. From joint residuals to joint prices

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

#### Appendix D.2.3. Criterion for strict tightening

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

#### Appendix D.2.4. Certified example for the original instruments

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

### Appendix D.3. A common framework for exact future-value functions and finite trial fields

#### Appendix D.3.1. Function classes and sufficient conditions

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

#### Appendix D.3.2. Structural condition $H$

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

#### Appendix D.3.3. Core lemma and proof: $H\Rightarrow M$

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

#### Appendix D.3.4. Propagation proposition: $M\Rightarrow B$

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

#### Appendix D.3.5. A fully explicit analytic witness

To verify \(C\setminus A\) directly in Appendix D.3.5, we provide an admissible object independent of the large field-coefficient collection. Fix \(T=1\) and any \(\varepsilon>0\), and take terminal payoff \(R=s_T^{-1/2}\) and field

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


### Appendix D.4. Financial propagation: portfolio values and joint quote-acceptance sets

#### Appendix D.4.1. Portfolio-value bounds

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

#### Appendix D.4.2. Calibration acceptance and target valuation

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