# 经典 Heston 扩展

《Rough Heston 模型的可验证联合定价误差》补充材料，2026年10月26日修订版。

本材料保留旧版附录F–G中的经典模型扩展，并沿用公式标签以便追溯。这些结果尚未建立完整年度金额定价证书，也不用于 Rough Heston 的证明链。对第2–7节或附录A–E的引用均指主文。十三函数构造仍缺少系数库验证，其作用是诊断，并非获得 Rough Heston 结果的方法。

## 附录 F. 经典 Heston 原链联合包含

本附录构造经典Heston模型下的联合误差输入。相关正部离散链提供共同的原概率律占用概率，标准凸分析给出支持函数及金融传播。终端见证认证外包集合的严格改善；年度金额证书还需要(F.21)的完整价格输入。

### F.1. 两个概率律与可容许模态

记 \(s=S/100=e^Z\)、\(d=\kappa\bar v\)、\(r=1/100\)、\(h=1/768\)，取 \(s_0=1\)。连续概率律 \(P\) 与原离散概率律 \(Q\) 为

\[
\begin{aligned}
dZ_t&=(r-V_t/2)dt+\sqrt{V_t}(\rho\,dW_t+\sqrt{1-\rho^2}\,dB_t),\\
dV_t&=(d-\kappa V_t)dt+\xi\sqrt{V_t}\,dW_t,\\
Y&=dh+(1-\kappa h)v+\xi\sqrt{hv}\,G,\qquad V'=Y^+,\\
Z'&=z+rh-hv/2+\sqrt{hv}(\rho G+\sqrt{1-\rho^2}H).
\end{aligned}\tag{F.1}
\]

\(G,H\) 是独立标准正态变量；股票和方差更新共享同一个 \(G\)。共同矩界使用参数域

\[
\kappa\in[2,4],\quad \bar v,v_0\in[3/100,3/50],\quad
\xi\in[9/50,7/25],\quad \rho\in[-4/5,-3/10].\tag{F.2}
\]

有限多日期模态的载荷 \(\alpha_{i,n}\in\mathbb C\) 满足

\[
\Re\alpha_{i,n}\le0,\qquad \sum_n|\Re\alpha_{i,n}|\le1/2.\tag{F.3}
\]

记已实现前缀为 \(H_{ji}\)，剩余股票载荷为 \(q_{ji}=p_{ji}+i\omega_{ji}\)。所有观测日期位于网格上。每次观测将一个载荷从剩余和移入已实现前缀，不改变原模态。

### F.2. 精确延续、完整核与可积性

**引理（精确连续延续）。** 从终端 \(a=b=0\) 出发，仿射延续 \(u=e^{qz+a+bv}\) 等于该模态的连续条件期望。在相邻观测之间，以剩余时间为自变量，

\[
b'=\tfrac12\xi^2b^2+(\rho\xi q-\kappa)b+\tfrac12(q^2-q),
\qquad a'=rq+db.\tag{F.4}
\]

观测时 \(q\) 改变，\(a,b\) 连续延续而不重新启动。令 \(\kappa_p=\kappa-p\rho\xi\)、\(\gamma_p=(p^2-p)/2\)。在 \(\Re b=1\) 上，实部漂移为

\[
\tfrac12\xi^2-\kappa_p+\gamma_p
-\tfrac12\{(\xi\Im b+\rho\omega)^2+(1-\rho^2)\omega^2\}<0,
\qquad
\frac{d|b|}{dt}\le(\xi^2/2-\kappa_p)|b|+|q^2-q|/2.\tag{F.5}
\]

因为 \(p\in[-1/2,0]\)、\(\kappa_p\ge1.888\)、\(\gamma_p\le3/8\)，首次穿越论证给出 \(\Re b\le1\)，径向界排除任何有限区间上的爆炸；同时 \(\Re a\le(6/25)T\)。

仅有形式 Riccati 推导，还不足以识别条件期望。将实载荷乘以 \(5/4\)，记新的已实现与剩余部分为 \(L_*(t),p_*(t)\)，则

\[
\mathcal Y_t=e^{L_*(t)+p_*(t)Z_t+4V_t-(24/25)t},\qquad
|\mathcal M_\tau|^{5/4}
\le e^{(5/4)(6/25)T+(24/25)T}\mathcal Y_\tau.\tag{F.6}
\]

\(\mathcal M\) 是该模态对应的停时仿射局部鞅。\(\mathcal Y\) 是非负局部超鞅：常数漂移非正，方差漂移至多为 \(65/128-4(1.86)+8(7/25)^2<0\)，观测处的载荷变化相互抵消。在紧状态域内停时并使用 (F.6)，得到统一 \(5/4\) 阶矩界。一致可积性解除停时，证明条件期望恒等式；该论证包含 \(v=0\) 和任意有限初始状态。

实际单步传播必须保留完整正部高斯核。对下一步系数 \(a,b,q\)，先积分 \(H\)，得到

\[
\frac{Q_hu(z,v)}{e^{qz}}=
e^{a+qrh-qhv/2+q^2(1-\rho^2)hv/2}
\int_{\mathbb R}\varphi(g)
e^{q\rho\sqrt{hv}g+b[dh+(1-\kappa h)v+\xi\sqrt{hv}g]^+}\,dg.\tag{F.7}
\]

当 \(v>0\) 时，在 \(g_0=-(dh+(1-\kappa h)v)/(\xi\sqrt{hv})\) 处分割积分：第一段的方差指数为零，第二段使用正候选值；两段都必须保留。当 \(v=0\) 时，\(V'=dh\) 是确定值。实高斯平方配方只是积分手段，不能将 \(Q\) 换成依赖模态的概率律。

记去除共同因子 \(e^{q_{ji}z}\) 后，实际传播与精确连续延续之差为 \(D_{ji}(v)\)。有限条件望远镜求和、每次观测恰计一次，给出

\[
\Phi_{Q,i}-\Phi_{P,i}=\sum_{j=0}^{N-1}r_{ji},\qquad
r_{ji}=E_Q[H_{ji}e^{q_{ji}Z_j}D_{ji}(V_j)].\tag{F.8}
\]

下一节的可积性保证这里每一个离散期望都有意义。

### F.3. 原概率律的矩界与共同占用概率

**引理（离散指数矩）。** 对实载荷非正、绝对值总和至多为一的多日期载荷，

\[
E_Q\exp\!\left\{\sum_{n\le j}\beta_n Z_n+4V_j\right\}
\le K_j:=e^{6/25+(73/75)jh}.\tag{F.9}
\]

证明时对 \(p\in[-1,0]\) 的实股票指数配方。候选均值变为 \(dh+\eta_pv\)，其中 \(\eta_p=1-\kappa_ph\ge191/192\)。由 \((-y)^+\le h(25e)^{-1}e^{-25y/h}\)，

\[
E(-Y_p)^+\le\frac{h}{25e}
\exp\!\left\{-25d+\frac{[-25\eta_p+(625/2)\xi^2]v}{h}\right\}
\le\frac{h}{25e^{5/2}}<h/300.\tag{F.10}
\]

参数界保证 \(d\ge3/50\)，方差系数至多为 \(-71/192\)，且 \(e^{5/2}>12\)。在 \(v=0\) 处，负部恰为零。对 \(B\ge0\)，有 \(e^{By^+}\le e^{By}+B(-y)^+\)。定义 \(F_p(B)=\gamma_ph+\eta_pB+\xi^2hB^2/2\)，高斯积分给出

\[
\begin{aligned}
E_Q[e^{pZ'+BV'}\mid z,v]
&\le e^{pz+prh}\{e^{Bdh+F_p(B)v}+Bh\,e^{\gamma_phv}/300\},\\
E_Q[e^{pZ'+4V'}\mid z,v]
&\le e^{pz+4v}(e^{4dh}+4h/300)
\le e^{pz+4v+(73/75)h}.
\end{aligned}\tag{F.11}
\]

这里 \(F_p(4)\le4\)、\(rp\le0\)、\(4d\le24/25\)。逐次条件化，结合观测时载荷变化抵消及 \(4v_0\le6/25\)，证明 (F.9)。

对 \([0,\infty\)) 的有限分区 \(I_r\)，保留零原子和无界尾部，令

\[
\pi_{jr}=Q(V_j\in I_r),\quad
h_{jir}\ge\sup_{v\in I_r}|e^{-2v}D_{ji}(v)|^2,\quad
|r_{ji}|^2\le K_j\sum_rh_{jir}\pi_{jr}=:\mathbf a_{ji}\cdot\pi_j.\tag{F.12}
\]

最后的不等式对 \(H_{ji}e^{q_{ji}Z_j}e^{2V_j}\) 与 \(e^{-2V_j}D_{ji}(V_j)\) 应用复 Cauchy–Schwarz；第一因子的平方矩由 (F.9) 的双倍载荷覆盖。因此每个模态共用同一个原离散链概率向量。若试探残差依赖其他状态，必须对那些状态取统一包络或扩大分区；连续概率律下的残差不能直接继承这些 \(Q\) 概率。

### F.4. 有效的终端概率多面体

固定 \(\theta_*=(\kappa,\bar v,\xi,\rho,v_0)=(3,9/200,23/100,-11/20,9/200)\)、\(j=767\)、\(d=27/200\)、\(\eta=255/256\)。使用

\[
I_0=\{0\},\quad I_r=((r-1)/100,r/100]\ (1\le r\le100),
\quad I_{101}=(1,\infty).\tag{F.13}
\]

对 \(v>0\)，下一步零质量为 \(\Phi(-(dh+\eta v)/(\xi\sqrt{hv}))\)，对 \(v=0\) 则为零。投影增量满足 \(E[-dh-\eta v-\xi\sqrt{hv}G]^+\le h\xi^2e^{-d\eta/\xi^2}/(\eta\sqrt{2\pi e})<h/200\)。其证明令 \(v=hz\)，用高斯密度项控制正态负部，再最大化 \(\sqrt z e^{-\eta^2z/(2\xi^2)}\)。均值递推和正指数递推给出

\[
EV_n\le\mu:=7/150,\qquad
M_{n+1}\le e^{4dh}M_n^{\beta}+h/50,\qquad
Ee^{4V_n}\le5/4,\quad Ee^{-tV_n}\ge e^{-t\mu}.\tag{F.14}
\]

这里 \(M_n=Ee^{4V_n}\)、\(\lambda=\kappa-2\xi^2=14471/5000\)、\(\beta=1-\lambda h\in(0,1)\)。\(x^\beta\) 的凹性给出所列递推。在 \(M=5/4\) 处，使用 \(\log(5/4)\ge1/5\)、\(4d-\lambda/5=-971/25000\)，及 \(0\le x\le1\) 时的 \(1-e^{-x}\ge x/2\)，下降量超过 \(h/50\)。由于 \(M_0=e^{.18}<5/4\)，归纳证明正指数界；Jensen 不等式给出 Laplace 下界。

对 \(t\in\mathcal T=\{1,4,16,64,256,(191/192)^2/[2(49/625)h]\}\)，定义

\[
t_0=t,\quad t_{n+1}=\eta_*t_n-c_*t_n^2,\qquad
L_{767}(t)=\exp\!\left[-d_*h\sum_{n=0}^{766}t_n-v_*t_{767}\right].\tag{F.15}
\]

参考四元组为 \((\eta_*,c_*,d_*,v_*)=(191/192,(49/625)h/2,3/50,3/100)\)，点参数四元组为 \((255/256,\xi^2h/2,27/200,9/200)\)。由 \(e^{-tY^+}\le e^{-tY}\) 及高斯积分，\(E[e^{-tV'}\mid v]\le e^{-dht}e^{-(\eta t-\xi^2ht^2/2)v}\)。全部 767 步递推满足 \(0\le t_n\le\eta_* /(2c_*)\)，所以递推在认证包络内单调；保守的参考参数在整个 (F.2) 域上产生有效上界。

真实终端概率向量满足

\[
\begin{aligned}
\sum_r\inf_{I_r}e^{-tv}\pi_r&\le L^{\rm ref}_{767}(t),&
\sum_r\inf_{I_r}e^{-tv}\pi_r&\le L^{\rm point}_{767}(t),\\
\sum_r\sup_{I_r}e^{-tv}\pi_r&\ge e^{-t\mu},&
\sum_r\ell_r\pi_r&\le\mu,\quad \sum_re^{4\ell_r}\pi_r\le5/4,
\end{aligned}\tag{F.16}
\]

另有非负性和质量为一；\(\ell_r=\inf I_r\)。零原子的 Laplace 系数是一，尾部下确界/上确界是零/\(e^{-t}\)。六组三个约束、两个矩约束、两个带符号质量约束，共 22 行。上界行使用系数下端点及右端上端点；下界行先使用系数上端点和右端下端点，再反号。因此保存的有理多面体 \(\mathcal P_{767}=\{\pi\ge0:A\pi\le b\}\) 包含真实概率，是概率单纯形的非空紧子集。

### F.5. 覆盖整个方差轴的终端残差包络

最后一步的未来方差指数为零，所以正部修正恰好消失。对 \(q=p+i\omega\)，记 \(g=(q^2-q)/2\)、\(L=\rho\xi q-\kappa\)、\(c=\xi^2/2\)，则

\[
D_q(v)=e^{rqh+hgv}-e^{a(h)+B(h)v},\quad
B'=g+LB+cB^2,\ B(0)=0,\qquad a(h)=rqh+d\int_0^hB(t)dt.\tag{F.17}
\]

在 \(\theta_*\) 处，Asian 代表模态为 \((p,\omega)=(-1/48,64)\)，put 代表模态为 \((-1/4,-8),(-1/4,-24),\ldots,(-1/4,-120)\)。在 \(\Re B=0\) 上，实部漂移至多为 \(p(p-1)/2-(279/800)\omega^2<0\)，故 \(\Re B\le0\)，且 \(\lvert B(t)\rvert\le|g|t\)。

令 \(P_3(t)=b_1t+b_2t^2+b_3t^3\)，其中 \(b_1=g\)、\(b_2=Lg/2\)、\(b_3=(L^2g+2cg^2)/6\)。精确检查 \(\Re b_1+\max(\Re b_2,0)h+\max(\Re b_3,0)h^2<0\)，证明 \(\Re P_3\le0\)。其残差为 \(-\sum_{k=3}^6r_kt^k\)，其中 \(r_3=Lb_3+2cb_1b_2\)、\(r_4=c(2b_1b_3+b_2^2)\)、\(r_5=2cb_2b_3\)、\(r_6=cb_3^2\)。由于 \(\Re[L+c(B+P_3)]\le-\kappa_p\)，常数变易公式给出

\[
E_B=\sum_{k=3}^6|r_k|_+\frac{h^{k+1}}{k+1},\qquad
E_A=d\sum_{k=3}^6|r_k|_+\frac{h^{k+2}}{(k+1)(k+2)}.\tag{F.18}
\]

\(|\cdot|_+\) 表示认证的模长上界。定义

\[
\begin{aligned}
A_q&=\min\{|{-d\int_0^hP_3}|_++E_A,\ d|g|_+h^2/2\},\\
B_q&=\min\{|hg-P_3(h)|_++E_B,\ (|L|_++\xi^2|g|_+h)|g|_+h^2/2\},\\
m_q&=2-\max\{h\Re g,\min(0,\Re P_3(h)+E_B)\}>0.
\end{aligned}\tag{F.19}
\]

指数之差的积分公式及两个指数的粗模长界给出

\[
|e^{-2v}D_q(v)|\le e^{prh}(A_q+B_qv)e^{-m_qv},\qquad
h_{qr}=\min\{[4e^{2prh-4\ell_r}]_+,[e^{2prh}S_{qr}^2]_+\},\quad
S_{qr}=\sup_{v\in I_r}(A_q+B_qv)e^{-m_qv}.\tag{F.20}
\]

计算上确界时检查各区间闭包的有限端点，以及位于区间内的驻点 \(1/m_q-A_q/B_q\)。当 \(B_q=0\) 时直接使用单调分支，不做除法。无穷尾部极限为零，零区间在零处求值。精确向外算术验证两个 Riccati 条件和全部 918 项（九模态、102 区间），含尾部；Asian 共轭具有同一包络。

### F.6. 联合包含及其精确严格性判据

假设同一有限模态目录给出完整贴现价格分解

\[
e_k=p_{h,k}-p_{c,k}=\Re\sum_{j,i}c_{ki}r_{ji}+R_k,\qquad |R_k|\le\varrho_k.\tag{F.21}
\]

系数和余项界必须包含所需转换、截断及算术贡献。终端见证本身不能建立这个完整价格前提。设 \(\mathcal F\) 非空、紧、凸，包含实际完整占用向量 \(\Pi=(\pi_j)_j\)。定义

\[
\mathcal E=\left\{\left(\Re\sum_{j,i}c_{ki}z_{ji}\right)_k:
\Pi\in\mathcal F,\ |z_{ji}|^2\le\mathbf a_{ji}\cdot\pi_j\right\}
+\prod_k[-\varrho_k,\varrho_k].\tag{F.22}
\]

**命题（联合价格包含）。** 此集合非空、紧、凸、中心对称，并包含实际 \(e\)。其支持函数为

\[
s_{\mathcal E}(w)=\max_{\Pi\in\mathcal F}\sum_{j,i}
\left|\sum_kw_kc_{ki}\right|\sqrt{\mathbf a_{ji}\cdot\pi_j}
+\sum_k|w_k|\varrho_k.\tag{F.23}
\]

**证明。** 提升后的约束是凸的，因为 \(\lvert z\rvert^2\) 凸而右侧仿射；在紧 \(\mathcal F\) 上，它们闭且有界。线性像再加余项箱体，保持上述几何性质。实际 \((\Pi,r)\) 由 (F.12) 可行。固定 \(\Pi\) 时，每个复圆盘的支持等于半径乘实线性系数的模长，各圆盘的独立相位可达到总和；再对同一概率向量最大化，得到 (F.23)。有跨时间约束时必须保留 \(\max_{\mathcal F}\sum_j\)，不能换成 \(\sum_j\max\)；只有 \(\mathcal F=\prod_j\mathcal P_j\) 才可分离。∎

令 \(F_k(\Pi)=\sum_{j,i}|c_{ki}|\sqrt{\mathbf a_{ji}\cdot\pi_j}\)、\(m_k=\max_{\mathcal F}F_k\)、\(\mathcal B=\operatorname{rect}(\mathcal E)=\prod_k[-m_k-\varrho_k,m_k+\varrho_k]\)，则

\[
\begin{aligned}
s_{\mathcal B}(w)-s_{\mathcal E}(w)
=\min_{\Pi\in\mathcal F}\Big\{
&\sum_k|w_k|[m_k-F_k(\Pi)]\\
&+\sum_{j,i}\big[\sum_k|w_kc_{ki}|-|\sum_kw_kc_{ki}|\big]
\sqrt{\mathbf a_{ji}\cdot\pi_j}\Big\}.
\end{aligned}\tag{F.24}
\]

每项均非负。差值为零，当且仅当存在同一 \(\Pi_*\) 最大化所有活跃完整价格行，并在每个正半径圆盘中，使全部非零 \(w_kc_{ki}\) 位于同一非负复射线上。零半径无需相位条件，\(w=0\) 时差值为零。加减共同价格行值得到 (F.24)，紧性保证最小值达到；不存在该见证时，相对同一外包集合的最小坐标箱体严格改善。这不证明实际偏差达到边界，也不是实际误差下界。加入 payoff 交集后，必须重新对所得集合检查判据。

### F.7. 完整终端价格行的分离见证

工具目录为到期 \(1/4,1/2,1\)、执行价 (90,100,110) 的欧洲 put，另加十二次观测的算术 Asian call spread \((A-95)^+-(A-110)^+\)，\(A=\sum_{m=1}^{12}S_{m/12}/12\)。第八项是一年期平值 put；\(w=\mathbf e_{10}-\mathbf e_8\) 是预先指定的偏差比较，不是优化对冲。

共轭合并后的完整终端价格行为

\[
F_A(\pi)=C_A\sqrt{K_{767}}\sqrt{a\cdot\pi},\quad C_A>0,\qquad
F_P(\pi)=\frac{1600e^{-.01}}{\pi_{\rm circ}}\sqrt{K_{767}}
\sum_{\omega=8,24,\ldots,120}
\frac{\sqrt{d_\omega\cdot\pi}}
{\sqrt{(\omega^2+1/16)(\omega^2+25/16)}}.\tag{F.25}
\]

\(\pi_{\rm circ}\) 是圆周率，\(\pi\) 是概率向量。\(C_A>0\) 需要证明：单纯形 Beta 系数为 \(\mathcal M_K(\zeta)=K(12K/100)^{\sum_m\zeta_m}\prod_m\Gamma(\zeta_m)/\Gamma(2+\sum_m\zeta_m)\)，原目录保留执行价 95 与 110 的系数差。Gamma 因子有限且非零，执行价因子的模长 \(95(11.4)^{1/4}\) 与 \(110(13.2)^{1/4}\) 不同，因此至少一个系数非零。

精确 Asian 原始与对偶见证满足 \(\pi^A\ge0\)、\(A\pi^A\le b\)、\(y\ge0\)、\(A^Ty\ge a\)、\(a\cdot\pi^A=b\cdot y\)。令 \(S=\{1,2,6\}\)，\(J\) 为三个正对偶行（点参数 \(t=256\) 的 Laplace 行、均值行、质量行）。见证的紧凑精确表达为

\[
\pi^A_{S}=A_{J,S}^{-1}b_J,\quad \pi^A_{S^c}=0,\qquad
\det A_{J,S}\ne0,\qquad (A^Ty-a)_{S^c}>0.\tag{F.26}
\]

其非零坐标约为 \((.0276833515163,\ .0487291439380,\ .923587504546)\)。弱对偶证明最优性，互补松弛将任意最优解限制在 \(S\) 和三个活跃等式上，可逆性证明唯一性；严格递增的平方根将唯一性传递给 \(F_A\)。

同一多面体含有支撑为 \(\{5,6\}\) 的精确 \(\pi^B\)。令 \(D_\omega=(\omega^2+1/16)(\omega^2+25/16)\)、\(x_\omega=d_\omega\cdot\pi^A>0\)。辅助 put 行 \(\mathscr B(\pi)=\sum_\omega\sqrt{d_\omega\cdot\pi}/\sqrt{D_\omega}\) 满足

\[
\left.\frac d{dt}\mathscr B((1-t)\pi^A+t\pi^B)\right|_{t=0}
=\sum_\omega\frac{d_\omega\cdot(\pi^B-\pi^A)}{2\sqrt{D_\omega x_\omega}}
\in[L,U],\qquad L>3\cdot10^{-9}.\tag{F.27}
\]

精确有理 \(L,U\) 由 `terminal767-result.json` 的 `put_direction.derivative` 端点指定，无需印出巨大分数。每个系数包络 \([l_\omega,u_\omega]\) 满足 \(0<l_\omega\le u_\omega\) 及 \(4l_\omega^2D_\omega x_\omega\le1\le4u_\omega^2D_\omega x_\omega\)；负方向变化先交换端点再求和。因此完整有符号行导数为正，Asian 最大化点不是 put 最大化点，故

\[
g^{\rm row}_{767}=\max F_A+\max F_P-\max(F_A+F_P)>0,
\qquad s_{\mathcal B_{767}}(w)-s_{\mathcal E_{767}}(w)\ge g^{\rm row}_{767}>0.\tag{F.28}
\]

第二个不等式来自系数的三角不等式；相位抵消只会进一步降低联合支持。在有效的逐时间乘积集合和同一完整目录下，累计的未取交集支持差值至少为该正终端差值。变更目录、概率集合或 payoff 交集，需要重新分析。

在目录 `science/baseline/reference/code/classical/` 中，机器附录为 `terminal767-input.json`、`terminal767-result.json`、`verify_input_bounds.py`、`verify_terminal.py`。第一读取器重生成 22 行、十二条各 767 步的 Laplace 递推及全部 918 个包络项；第二读取器执行 407 项精确见证检查。这些支持终端结论，并未证明完整价格前提 (F.21)、年度金额端点或交易解释。

### F.8. 标准金融传播推论

对有效紧集合 \(e=p_h-p_c\in\mathcal E\)、\(n=p_h-\widehat p_h\in\mathcal N\)，

\[
\begin{aligned}
w^Tp_h-s_{\mathcal E}(w)&\le w^Tp_c\le w^Tp_h+s_{\mathcal E}(-w),\\
w^T\widehat p_h-s_{\mathcal N}(-w)-s_{\mathcal E}(w)
&\le w^Tp_c\le
w^T\widehat p_h+s_{\mathcal N}(w)+s_{\mathcal E}(-w).
\end{aligned}\tag{F.29}
\]

若实际 \((n,e)\) 属于共同紧集合 \(\mathcal K\)，则左端减项改用 \(s_{\mathcal K}(-w,w)\)，右端加项改用 \(s_{\mathcal K}(w,-w)\)。对闭校准接受集合 \(\mathcal Y\)，

\[
\begin{aligned}
\mathcal T_\theta&=\{(n,e)\in\mathcal K_\theta:
\widehat p_{h,\rm cal}+n_{\rm cal}-e_{\rm cal}\in\mathcal Y\},\\
\mathcal A_\theta&=\{\widehat p_{h,10}+n_{10}-e_{10}:(n,e)\in\mathcal T_\theta\}.
\end{aligned}\tag{F.30}
\]

恒等式 \(p_c=p_h-e=\widehat p_h+n-e\) 证明上述结论。非空 \(\mathcal T_\theta\) 紧，目标端点达到；空集合排除与接受规则的兼容性。将共同输入集合扩大为坐标箱体，只会扩大或保持目标集合。这些属于标准集合传播，前提是已取得有效中心和完整误差输入。

## 附录 G. 非精确试探函数与有符号误差恒等式

本附录使用同一个确定性试探函数进行连续—离散比较，该函数不必满足后向方程。我们独立于未知精确解陈述充分条件，证明四个有符号项，并构造一个全局可积的非精确解析函数。以下期望未贴现；由 payoff 转为价格时，应将恒等式与界乘以共同贴现因子。

### G.1. 状态、左右迹与可容许条件

采用附录 F 的原概率律 \(P,Q\)、参数及相关正部更新。月度观测之间，状态为 \(x=(s,v,A_m,\ell_m)\)，其中 \(A_m\) 是已观测归一化股票值之和，\(\ell_m\) 是其对数之和。观测映射 \(J_i\) 将当前 \(s,\log s\) 加入相应历史。观测之间的生成器为

\[
\mathcal L=rs\partial_s+(d-\kappa v)\partial_v
+\tfrac12vs^2\partial_{ss}+\rho\xi vs\partial_{sv}
+\tfrac12\xi^2v\partial_{vv}.\tag{G.1}
\]

在整个期限选择同一个固定非负权重，例如

\[
\begin{aligned}
W&=e^v\{s^{-1/2}+e^{-\ell_m/24}s^{-(12-m)/24}\},\\
W^{\rm nat}&=e^v\{\mathfrak B_m^{-1/2}+\mathfrak G_m^{-1/2}\},\qquad
\mathfrak B_m=(A_m+(12-m)s)/12,\quad
\mathfrak G_m=e^{\ell_m/12}s^{(12-m)/12}.
\end{aligned}\tag{G.2}
\]

两个权重都在观测映射前后精确匹配。算术均值不小于几何均值，所以 \(W^{\rm nat}\le2e^v\mathfrak G_m^{-1/2}\)。两个权重中的历史因子都对应总绝对值至多为 \(1/2\) 的多日期非正实载荷。

**引理（权重矩界）。** 在 \(\theta_*\) 和 \(0\le t\le1\) 上，每个权重满足

\[
\sup_tE_PW(t,X_t)<5/2,\qquad \max_jE_QW(t_j,X_j)<5/2,
\qquad \sup_{\tau\le1}E_PW(\tau,X_\tau)^2<\infty.\tag{G.3}
\]

最后的上确界取遍下面紧状态域局部化使用的停时。证明连续单分支界时，对 \(e^{L+pZ+V}\)、\(p\in[-1/2,0]\) 使用生成器；方差系数 \(\gamma_p-\kappa_p+\xi^2/2<0\)，常数漂移 \(rp+d\le d\)，观测时载荷变化抵消。非负停时超鞅给出单分支期望至多为 \(e^{v_0+d}=e^{9/50}<5/4\)。离散概率律使用 (F.10)–(F.11) 的 \(B=1\) 情形及 \(F_p(1)\le1\)，得到单分支界 \(e^{v_0+d+1/300}=e^{11/60}<5/4\)。将两个分支相加，或用 \(W^{\rm nat}\le2e^v\mathfrak G_m^{-1/2}\)，得到所需一阶界；严格比较由 \(\log(5/4)\ge1/5\) 保证。

平方界使用 \((a+b)^2\le2(a^2+b^2)\)。每个平方分支的总股票载荷至多为一，方差载荷为二；将方差载荷提高到四可支配该分支。连续指数超鞅的方差系数至多为 \(1-4(1.776)+8(7/25)^2<0\)，常数漂移至多为 \(24/25\)，故停时给出统一有限二阶矩；自然权重同理。这足以保证被 \(W\) 支配的函数一致可积，无需假设停时随机积分的极限本身是普通鞅。

\(R\) 是两个概率律下同一终端 payoff 或同一精确有限转换余项。确定性函数 \(\widetilde u\) 在观测之间局部 \(C^{1,2}\)，在 \(v=0\) 处有可用于 Itô 公式的右侧延拓，并在紧状态集上一致存在真正的单侧迹。要求全局界

\[
\begin{aligned}
|\widetilde u|&\le CW,&
|\mathfrak r(t,x)|&\le\eta_c(t)W(t,x),& \int_0^1\eta_c(t)dt&<\infty,\\
|d_i(x)|&\le\eta_iW(t_i-,x),&
|\delta(x)|&\le\eta_TW(1,x),& C,\eta_i,\eta_T&<\infty.
\end{aligned}\tag{G.4}
\]

支配必须覆盖所有状态、\(v=0\) 和无界尾部。定义

\[
\begin{aligned}
\mathscr D_j&=Q_j\widetilde u_{j+1}-\widetilde u_j,&
\mathfrak r&=(\partial_t+\mathcal L)\widetilde u,\\
d_i(x)&=\widetilde u(t_i-,x)-\widetilde u(t_i+,J_ix),&
\delta&=R-\widetilde u_N.
\end{aligned}\tag{G.5}
\]

跳跃残差取左迹减观测更新后的右迹。\(Q_j\) 包含原核和步末观测；两个概率律使用相同的观测后终端约定，每次更新计一次。\(\mathscr D_j\) 须在 \(Q\) 下可积；完整期限包络为 \(\sum_jE_Q\mathscr D_j\in[L_Q,U_Q]\)。另一充分条件为 \(\lvert\mathscr D_j\rvert\le h\eta_{Q,j}W\)。

精确未来值函数须验证正则性和支配界，才能属于此类；有限表示同样需要检查增长、残差、左右迹、终端值及原核接口。

### G.2. 四项有符号恒等式

**定理（同一函数的残差恒等式）。** 在 (G.3)–(G.5) 和原 \(Q\) 下离散残差可积的条件下，

\[
\boxed{E_QR-E_PR=
\sum_jE_Q\mathscr D_j-E_P\int_0^1\mathfrak r(t,X_t)dt
+\sum_iE_Pd_i+(E_Q-E_P)\delta.}\tag{G.6}
\]

**证明。** 原 \(Q\) 下有限条件望远镜求和给出

\[
E_Q\widetilde u_N-\widetilde u_0=\sum_jE_Q\mathscr D_j.\tag{G.7}
\]

对 \(P\)，先在紧状态域内、远离观测时刻的闭子区间上局部化，Itô 公式中的随机积分期望为零。(G.3) 的二阶矩界与 \(|\widetilde u|\le CW\) 保证停时函数值一致可积，解除停时时得到 \(L^1\) 收敛。Tonelli 及 (G.4) 给出 \(E_P\int|\mathfrak r|\le\int\eta_c(t)E_PW(t,X_t)dt<\infty\)，从而可用绝对可积支配解除时间积分中的停时。区间端点趋近观测时刻时，紧集上一致的真正左右迹与连续路径给出几乎处处收敛，同一一致可积性给出 \(L^1\) 收敛。实际函数跳跃为 \(-d_i\)。对所有区间和跳跃求和，得到

\[
E_P\widetilde u_N-\widetilde u_0
=E_P\int_0^1\mathfrak r(t,X_t)dt-\sum_iE_Pd_i.\tag{G.8}
\]

由 (G.7) 减 (G.8)，再分别加入 \(\delta=R-\widetilde u_N\) 的两个期望，共同确定性初值精确抵消，得到 (G.6)。采用上述观测后约定，论证也包括终端日的观测。∎

若改为定义 \(J_i^{\rm jump}=\widetilde u(t_i+,J_ix)-\widetilde u(t_i-,x)\)，则 (G.6) 对应项必须写作 \(-\sum_iE_PJ_i^{\rm jump}\)。明确符号约定，避免混用两种定义。对精确延续，后向残差、观测残差和终端差均消失，恢复 (F.8)；非精确函数则保留四个有符号项。

### G.3. 有效的充分误差界

在 \(\theta_*\) 处，(G.6) 和权重引理给出

\[
\begin{aligned}
|E_QR-E_PR|&\le\max(|L_Q|,|U_Q|)
+\tfrac52\left(\int_0^1\eta_c(t)dt+\sum_i\eta_i\right)+5\eta_T,\\
|E_QR-E_PR|&\le\tfrac52\left(h\sum_j\eta_{Q,j}
+\int_0^1\eta_c(t)dt+\sum_i\eta_i\right)+5\eta_T
\quad\text{if }|\mathscr D_j|\le h\eta_{Q,j}W.
\end{aligned}\tag{G.9}
\]

这是由三角不等式得到的非负充分界；若已取得四项的共同有符号包络，可直接传播其线性像。各价格的独立区间不能自行提供共同状态兼容性见证。尤其，残差包络的必要下界，并不是对 (G.9) 任一充分上界的计算。

### G.4. 自洽的非精确解析函数

固定 \(T=1\)、\(\varepsilon>0\)、\(R=s_T^{-1/2}\)，取

\[
a_\varepsilon(t)=1+\varepsilon t(1-t),\qquad
\widetilde u_\varepsilon(t,x)=a_\varepsilon(t)s^{-1/2},\qquad
1\le a_\varepsilon\le C_\varepsilon:=1+\varepsilon/4.\tag{G.10}
\]

使用单分支权重 \(W_A=s^{-1/2}e^v\)，前面的权重证明同样适用。该函数在 \(s>0,v\ge0\) 上全局正则，不依赖历史，观测左右迹和终端值精确匹配，且 \(|\widetilde u_\varepsilon|\le C_\varepsilon W_A\)。生成器残差为

\[
\mathfrak r_\varepsilon=s^{-1/2}
\{\varepsilon(1-2t)+a_\varepsilon(t)(3v/8-r/2)\}.\tag{G.11}
\]

由 \(ve^{-v}\le1/e\)，可取全局、时间常数型支配函数

\[
\eta_c=\varepsilon+C_\varepsilon(r/2+3/(8e)),\qquad
\int_0^1\eta_c(t)dt=\eta_c<\infty,\qquad \eta_i=\eta_T=0.\tag{G.12}
\]

尽管股票与方差共享 \(G\)，这里的函数不依赖下一步方差，所以原股票高斯积分可以精确计算：

\[
\mathscr D_j=s^{-1/2}\{a_\varepsilon(t_{j+1})e^{h(3v/8-r/2)}-a_\varepsilon(t_j)\},\qquad
|\mathscr D_j|\le h\eta_QW_A,\quad
\eta_Q=\varepsilon+C_\varepsilon\{r/2+3/[8e(1-3h/8)]\}.\tag{G.13}
\]

为证明该界，将差写作 \((a_{j+1}-a_j)e^{h(3v/8-r/2)}+a_j(e^{h(3v/8-r/2)}-1)\)，使用 \(|a_{j+1}-a_j|\le\varepsilon h\)、\(|e^x-1|\le|x|e^{\max(x,0)}\)，及 \(c=1-3h/8>0\) 时的 \(ve^{-cv}\le1/(ec)\)。因此每个离散残差可积；因 \(Nh=1\)，完整期限包络可显式取为 \(\sum_jE_Q\mathscr D_j\in[-(5/2)\eta_Q,(5/2)\eta_Q]\)。代入 (G.9)，得到有限充分界 \((5/2)(\eta_Q+\eta_c)\)。

在 \(t=1/2,v=r>0\) 处，(G.11) 等于 \(-rC_\varepsilon s^{-1/2}/8<0\)，所以该函数不是精确未来值函数。同一个负幂 payoff 的精确函数由附录 F 的仿射延续和矩界证明存在，其载荷为 \(-1/2\)。同一可容许对象类因此既含精确函数，也含非精确函数，四项恒等式对二者均适用。此例是解析适用范围见证，不是原市场工具的数值证书。

### G.5. 十三个基函数诊断的证明范围

保存的经典试探函数诊断具有另一种有条件的用途。令 \(n=12-m\)、\(B=(A_m+ns)/12\)、\(y=A_m/(A_m+ns)\)、\(\beta=1-y\)、\(z=v/(1+v)\)，其分支为 \(B^{-q}P(y,v)\)。本节 \(\Re q=1/2\)，所以 \(B^{-q}\) 对应负股票阻尼；这里的 \(q\) 不同于附录 F 中的负载荷 \(q\) 记号。共轭生成器为

\[
\begin{aligned}
\mathcal L_qP={}&-ry\beta P_y+dP_v-qr\beta P\\
&+v\{\tfrac12y^2\beta^2P_{yy}-\rho\xi y\beta P_{yv}
+\tfrac12\xi^2P_{vv}+(1+q)y\beta^2P_y\\
&\hspace{12mm}-(\kappa+q\rho\xi\beta)P_v+\tfrac12q(q+1)\beta^2P\}.
\end{aligned}\tag{G.14}
\]

基函数为 \(\phi_{ij}=\beta y^iz^j\)、\(0\le i\le2,0\le j\le3\)，另加 \(\psi=v\beta^2\)。它们精确表示终端强迫项 \(\mathcal L_q1=-qr\phi_{00}+q(q+1)\psi/2\)；这是终端生成器补全，不是对所有生成器像的闭合。对有限端点常数，函数使用三次 Hermite 插值及精确物理斜率 \(-Kc-g(q)\)，其中 \(g(q)=-qr e_{00}+q(q+1)e_\psi/2\)。令 \(\gamma=(n-1)/n\)，精确观测传递为

\[
(T_nc)_{\ell j}=\gamma\sum_{i=\ell}^2\binom i\ell\gamma^\ell n^{-i+\ell}c_{ij},
\qquad T_n\psi=\gamma^2\psi.\tag{G.15}
\]

这来自 \(y'=\gamma y+1/n\)、\(B'=B\)、\(\beta'=\gamma\beta\)。终端修正节点为零；精确传递及斜率定义左右迹，浮点生成值不能替代这些定义。有限函数满足 \(|P|\le C_0+C_1v\le(C_0+2C_1/e)e^{v/2}\)。其连续残差关于 \(v\) 至多二次，\(y,z\) 系数有界，因此 \(e^{-v}|F|\le a_0+a_1/e+4a_2/e^2\)。完整使用 (G.9) 仍需要实际系数库、所有状态下的原 \(Q\) 包络及完整期限充分上界。

对保存的首月状态 \(m=0,y=0,v=9/200\)，令 \(w=(1,z,z^2,z^3,0,\ldots,0,v)\)、\(\ell\) 为基函数生成器值行、\(\ell_0=-qr+q(q+1)v/2\)。单个时间片上的精确积分为

\[
\int F_{A,q}dt=
\left[w+\frac{h^2}{12}\ell K\right](c_R-c_L)
+\frac h2\ell(c_L+c_R)+h\ell_0.\tag{G.16}
\]

因为 \(\int c(t)dt=h(c_L+c_R)/2+h^2(s_L-s_R)/12\)，且 \(s_L-s_R=K(c_R-c_L)\)。归档包含全部 3080 个加权复积分区间（385 模态、八单元，覆盖原 64 时间片）。在共同相位零处，对每单元求实模态区间之和，使用 \(\int|F|\ge|\int F|\)，再减去已积分的几何分支上界。精确总值由 `field-result.json` 的数学字段 `whole_lower` 指定：

\[
\int_0^{1/12}\eta_c(t)dt\ge L_*,\qquad
L_*>0.003407444052031154>0.\tag{G.17}
\]

该界拒绝所选分配 \(\int\eta_c\le1/1000\)，记录为`FAIL_SELECTED_INTEGRATED_PDE_CONTRACT_ONLY`；它是此函数的必要条件诊断。读取器`verify_field_receipt.py`核查保存区间的精确聚合，但缺少系数库，不能重生成直接积分。诊断没有对试探空间求最优，也不给有符号价格偏差的下界。显式函数(G.10)另行证明非精确可容许性；完整年度金额证书仍待完成。

目录`science/baseline/reference/code/classical/`提供`field-cell-integrals.json`、`field-result.json`、`field-independent-readback.json`、`provenance.json`和`verify_field_receipt.py`，文件身份由发布清单固定。

## 参考文献

1. **GR2019.** Gatheral, Jim and Radoičić, Radoš. *Rational Approximation of the Rough Heston Solution*. International Journal of Theoretical and Applied Finance 22(3), 1950010, 2019. DOI [10.1142/S0219024919500109](https://doi.org/10.1142/S0219024919500109)。 使用2019年1月29日SSRN稿。

2. **GR2023.** Gatheral, Jim and Radoičić, Radoš. *A Generalization of the Rational Rough Heston Approximation*. Quantitative Finance 24(2), 329–335, 2024. DOI [10.1080/14697688.2024.2302055](https://doi.org/10.1080/14697688.2024.2302055)。[原文](https://arxiv.org/abs/2310.09181v1)。所用预印本：arXiv:2310.09181。

3. **JK2020.** Siow Woon Jeng and Adem Kiliçman. *Series Expansion and Fourth-Order Global Padé Approximation for a Rough Heston Solution*. Mathematics 8(11), 1968, 2020. DOI [10.3390/math8111968](https://doi.org/10.3390/math8111968)。

4. **JK2021.** Siow Woon Jeng and Adem Kiliçman. *SPX Calibration of Option Approximations under Rough Heston Model*. Mathematics 9(21), 2675, 2021. DOI [10.3390/math9212675](https://doi.org/10.3390/math9212675)。

5. **AbiJaberElEuch2018.** Abi Jaber, Eduardo and El Euch, Omar. *Markovian structure of the Volterra Heston model*. Statistics & Probability Letters 149, 63–72, 2019. DOI [10.1016/j.spl.2019.01.024](https://doi.org/10.1016/j.spl.2019.01.024)。 所用预印本：arXiv:1803.00477。

6. **LiLiu2018.** Li, Lei and Liu, Jian-Guo. *A Generalized Definition of Caputo Derivatives and Its Application to Fractional ODEs*. SIAM Journal on Mathematical Analysis 50(3), 2867–2900, 2018. DOI [10.1137/17M1160318](https://doi.org/10.1137/17M1160318)。 凸性工具见命题3.11。

7. **Simon2014.** Simon, Thomas. *Comparing Fréchet and positive stable laws*. 2014. [原文](https://arxiv.org/abs/1310.1888v2)。 所用预印本：arXiv:1310.1888。

8. **TrefethenWeideman2014.** Trefethen, Lloyd N. and Weideman, J. A. C. *The Exponentially Convergent Trapezoidal Rule*. SIAM Review 56(3), 385–458, 2014. DOI [10.1137/130932132](https://doi.org/10.1137/130932132)。 条带求积见定理5.1。

9. **NIST2010.** Olver, Frank W. J. and Lozier, Daniel W. and Boisvert, Ronald F. and Clark, Charles W. *NIST Handbook of Mathematical Functions*. Cambridge University Press, 2010. [原文](https://dlmf.nist.gov/)。

10. **BBWeak2023.** Bayer, Christian and Breneis, Simon. *Weak Markovian Approximations of Rough Heston*. 2023. [预印本](https://arxiv.org/abs/2309.07023v1)，[原始 PDF](https://arxiv.org/pdf/2309.07023v1)。所读预印本：arXiv:2309.07023，2023 年 9 月 13 日提交；特征函数与 European payoff 误差结果见定理 2.2、2.7。

11. **BBSimulation2023.** Bayer, Christian and Breneis, Simon. *Efficient option pricing in the rough Heston model using weak simulation schemes*. 2023. [预印本](https://arxiv.org/abs/2310.04146v1)，[原始 PDF](https://arxiv.org/pdf/2310.04146v1)。所读预印本：arXiv:2310.04146，2023 年 10 月 6 日提交；该预印本第4页 将二阶弱收敛报告为数值观察。

12. **Kopteva2021.** Kopteva, Natalia. *Pointwise-in-time a posteriori error control for time-fractional parabolic equations*. Applied Mathematics Letters 123, 107515, 2022. DOI [10.1016/j.aml.2021.107515](https://doi.org/10.1016/j.aml.2021.107515)。[所读预印本](https://arxiv.org/abs/2105.05848v2)，[原始 PDF](https://arxiv.org/pdf/2105.05848v2)：arXiv:2105.05848，2021 年 7 月 5 日修订；首次提交于 2021 年 5 月 12 日。逐时残差界与范数不等式见定理 2.2、引理 2.8。

13. **ElEuchRosenbaum2017.** El Euch, Omar and Rosenbaum, Mathieu. *Perfect hedging in rough Heston models*. arXiv:1703.05049, 2017. [原文](https://arxiv.org/abs/1703.05049v1). 下降曲线的解析传播条件见本文附录C.3。

14. **SimonCM2015.** Simon, Thomas. *Mittag-Leffler functions and complete monotonicity*. Integral Transforms and Special Functions 26(1), 36–50, 2015. DOI [10.1080/10652469.2014.965704](https://doi.org/10.1080/10652469.2014.965704). [原文](https://arxiv.org/abs/1312.4513v2).

15. **BL2025.** Boyarchenko, Svetlana; de Innocentis, Marco; and Levendorskii, Sergei. *Fast reliable pricing and calibration of the rough Heston model*. arXiv:2508.15080, 2025. [原文](https://arxiv.org/abs/2508.15080v1). modified Adams见第3.2节，Conformal Bootstrap见第4.10节。

16. **BenHammouda2026.** Ben Hammouda, Chiheb; Ben Romdhane, Abderrahmene; Samet, Michael; and Tempone, Raul F. *Single- and Multilevel Quadrature with Error Control for Fourier Pricing under the Rough Heston Model*. arXiv:2609.00438, 2026. [原文](https://arxiv.org/abs/2609.00438v1). 实用容差说明见第3.2节。

17. **HK2026.** Hager, Paul P. and Kreher, Dörte. *Expanding the rough Heston model in H*. arXiv:2606.16619, 2026. [原文](https://arxiv.org/abs/2606.16619v1).
