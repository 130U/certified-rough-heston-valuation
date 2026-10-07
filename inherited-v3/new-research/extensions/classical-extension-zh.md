# 经典 Heston 扩展：适用范围与独立保证

本扩展保留原链理论。它尚未建立完整年度货币价格认证，也不列入粗糙 Heston 主文贡献。

## 附录 C. 经典原链概率包含的补充证明


### C.1. 精确未来核及积分的合法性

写 $s=S/100=e^Z$、$d=\kappa\bar v$、$h=1/768$、$r=1/100$。连续过程的律记为 $P$，实际离散链的律记为 $Q$：

$$
\begin{aligned}
dZ_t&=(r-V_t/2)dt+\sqrt{V_t}(\rho\,dW_t+\sqrt{1-\rho^2}\,dB_t),\\
dV_t&=(d-\kappa V_t)dt+\xi\sqrt{V_t}\,dW_t,\\
Y&=dh+(1-\kappa h)v+\xi\sqrt{hv}\,G,\quad V'=Y^+,\\
Z'&=z+rh-hv/2+\sqrt{hv}(\rho G+\sqrt{1-\rho^2}H).
\end{aligned}
\tag{Q1}
$$

其中 $G,H$ 独立标准正态，股票与方差更新共享 $G$。本附录的参数盒为

$$
\kappa\in[2,4],\quad \bar v,v_0\in[3/100,3/50],\quad
\xi\in[9/50,7/25],\quad \rho\in[-4/5,-3/10].
\tag{Q2}
$$

有限多日期指数模态的各实载荷非正，总绝对值不超过 $1/2$。记已经实现的前缀为 $H_{ji}$，剩余载荷为 $q=p+i\omega$。两次观测之间，连续未来核 $u=e^{qz+a+bv}$ 的系数满足

$$
b'=\tfrac12\xi^2b^2+(\rho\xi q-\kappa)b+\tfrac12(q^2-q),
\qquad a'=rq+db,
\tag{Q3}
$$

从终端零系数反向延续；观测时刻只更新剩余载荷，$a,b$ 连续。令 $\kappa_p=\kappa-p\rho\xi$、$\gamma_p=(p^2-p)/2$。在 $\operatorname{Re}b=1$ 上，实部导数为

$$
\tfrac12\xi^2-\kappa_p+\gamma_p
-\tfrac12\{(\xi\operatorname{Im}b+\rho\omega)^2+(1-\rho^2)\omega^2\}<0,
\tag{Q4}
$$

因为 $p\in[-1/2,0]$、$\kappa_p\ge1.888$、$\gamma_p\le3/8$。首次穿越论证给 $\operatorname{Re}b\le1$；

$$
\frac{d|b|}{dt}\le(\xi^2/2-\kappa_p)|b|+|q^2-q|/2
$$

防止有限时间爆炸，且 $\operatorname{Re}a\le(6/25)T$。

为证明此形式核确为期望，将全部实载荷乘以 $5/4$。记其已实现和剩余实载荷为 $L_*(t),p_*(t)$，定义

$$
\mathcal Y_t=\exp\{L_*(t)+p_*(t)Z_t+4V_t-(24/25)t\}.
\tag{Q5}
$$

它是非负局部超鞅：常数漂移 $rp_*+4d-24/25\le0$，方差漂移至多 $65/128-4(1.86)+8(7/25)^2<0$。观测更新使前缀和剩余载荷准确抵消。相应停止仿射局部鞅 $\mathcal M$ 满足

$$
|\mathcal M_\tau|^{5/4}
\le e^{(5/4)(6/25)T+(24/25)T}\mathcal Y_\tau.
$$

紧域停止和超鞅不等式给一致 $5/4$ 阶矩，从而一致可积；去停止后得到精确连续未来核，包括 $v=0$ 和任意有限起始状态。原始链的有限塔式分解因此给

$$
\Phi_{Q,i}-\Phi_{P,i}=\sum_jr_{ji},\qquad
r_{ji}=E_Q[H_{ji}e^{q_{ji}Z_j}D_{ji}(V_j)],
\tag{Q6}
$$

其中 $D_{ji}$ 是实际 $Q$ 一步传播与精确连续未来核的差，提出共同 $e^{q_{ji}z}$ 后成为方差的函数。

### C.2. 原始 Q 的平方矩与共同概率

对总绝对值不超过一的非正实载荷，有

$$
E_Q\exp\left\{\sum_{n\le j}\beta_nZ_n+4V_j\right\}
\le K_j:=e^{6/25+(73/75)jh}.
\tag{Q7}
$$

证明从实际相关 Gaussian 核出发。对 $p\in[-1,0]$ 完成股票指数的实 Gaussian 平方后，方差候选的均值成为 $dh+\eta_pv$，$\eta_p=1-\kappa_ph\ge191/192$。点态不等式 $(-y)^+\le h(25e)^{-1}e^{-25y/h}$ 给

$$
E(-Y_p)^+\le\frac{h}{25e}
\exp\!\left[-25d+\frac{[-25\eta_p+(625/2)\xi^2]v}{h}\right]
\le\frac{h}{25e^{5/2}}<h/300.
\tag{Q8}
$$

这里 $d\ge3/50$，方差系数至多 $-71/192$，且 $e^{5/2}>12$；$v=0$ 时负部准确为零。使用 $e^{By^+}\le e^{By}+B(-y)^+$ 和
$F_p(B)=\gamma_ph+\eta_pB+\xi^2hB^2/2$，可得原始条件期望

$$
E_Q[e^{pZ'+BV'}\mid z,v]
\le e^{pz+prh}\{e^{Bdh+F_p(B)v}+Bh\,e^{\gamma_phv}/300\}.
$$

在(Q2)中，$F_p(4)\le4$、$rp\le0$、$4d\le24/25$，故

$$
E_Q[e^{pZ'+4V'}\mid z,v]
\le e^{pz+4v}(e^{4dh}+4h/300)
\le e^{pz+4v+(73/75)h}.
$$

逐步条件化、准确抵消载荷更新，并使用 $4v_0\le6/25$，得到(Q7)。此计算中的 Gaussian square completion 是积分工具；最终期望仍在原始 $Q$ 下。

取同一方差分区 $I_r$，$\pi_{jr}=Q(V_j\in I_r)$，以及
$h_{jir}\ge\sup_{v\in I_r}|e^{-2v}D_{ji}(v)|^2$。把(Q6)的被积函数拆成 $H_{ji}e^{q_{ji}Z_j}e^{2V_j}$ 与 $e^{-2V_j}D_{ji}(V_j)$，复 Cauchy–Schwarz 和(Q7)给

$$
|r_{ji}|^2\le K_j\sum_rh_{jir}\pi_{jr}.
\tag{Q9}
$$

所有模态共享原始 $Q$ 的 $\pi_j$；股票和历史依赖保留在第一个平方矩中。若一般试验场的缺陷还依赖其他状态，必须对其证明一致包络，或扩大分区。连续 $P$ 下的残差占用律不能替换为此 $Q$ 向量。

### C.3. 终端概率多面体的 22 条有效约束

固定 $\theta_*=(3,9/200,23/100,-11/20,9/200)$、$j=767$，故 $d=27/200$、$\eta=255/256$。取

$$
I_0=\{0\},\quad I_r=((r-1)/100,r/100]\ (1\le r\le100),\quad I_{101}=(1,\infty).
\tag{Q10}
$$

这102带互不相交且覆盖全状态。$v>0$ 时原一步核在零点的质量为 $\Phi(-(dh+\eta v)/(\xi\sqrt{hv}))$；$v=0$ 时 $V'=dh>0$。零原子不得并入连续密度计算。

正部 excess 满足

$$
\epsilon(v)=E[-dh-\eta v-\xi\sqrt{hv}G]^+
\le\frac{h\xi^2}{\eta\sqrt{2\pi e}}e^{-d\eta/\xi^2}<h/200.
$$

对 $v=hz>0$，用 normal negative-part 上界 $\xi h\sqrt z\,\varphi((d+\eta z)/(\xi\sqrt z))$，舍去指数中 $d^2/z$ 的非负贡献，再最大化 $\sqrt z e^{-\eta^2z/(2\xi^2)}$ 即得；$v=0$ 时 excess 为零。严格常数使用 $\eta>.99$、$\xi^2<.053$、$d\eta/\xi^2>2$、$\sqrt{2\pi e}>3$ 和 $e^{-2}<1/4$。由 $EV_{n+1}\le dh+\eta EV_n+h/200$ 的不动点 $\bar v+1/(200\kappa)$，从 $V_0=\bar v$ 归纳得

$$
EV_n\le\mu:=7/150.
\tag{Q11}
$$

令 $\lambda=\kappa-2\xi^2=14471/5000$、$\beta=1-\lambda h$、$M_n=Ee^{4V_n}$。由正部不等式和凹函数 $x^\beta$，
$M_{n+1}\le e^{4dh}M_n^\beta+h/50$。在 $M=5/4$，$\log(5/4)\ge1/5$、$4d-\lambda/5=-971/25000$ 及 $1-e^{-x}\ge x/2$ 给严格向内漂移，下降量至少 $(5/4)(971/25000)h/2>h/50$；$M_0=e^{.18}<5/4$。归纳和 Jensen 得

$$
Ee^{4V_n}\le5/4,\qquad Ee^{-tV_n}\ge e^{-t\mu}\quad(t\ge0).
\tag{Q12}
$$

设 $\mathcal T=\{1,4,16,64,256,(191/192)^2/[2(49/625)h]\}$。对每个 $t$，定义 $t_0=t$、$t_{n+1}=\eta_*t_n-c_*t_n^2$。一步 Gaussian 积分及 $e^{-tY^+}\le e^{-tY}$ 给

$$
E[e^{-tV'}\mid V=v]\le e^{-dh t}\exp[-(\eta t-\xi^2ht^2/2)v].
$$

在 $t_n\ge0$ 下逐步条件化得到

$$
Ee^{-tV_{767}}\le L_{767}(t)
:=\exp\!\left[-d_*h\sum_{n=0}^{766}t_n-v_*t_{767}\right].
\tag{Q13}
$$

reference quadruple 为 $(191/192,(49/625)h/2,3/50,3/100)$；point quadruple 为 $(255/256,\xi^2h/2,27/200,9/200)$。前者的 $\eta_*,d_*,v_*$ 不大于真实值，$c_*$ 不小于真实值，故在(Q2)中给有效上界。所有767步检查 $0\le t_n\le\eta_* /(2c_*)$，保证二次递推在整个有理包络内递增。

对每个 $t\in\mathcal T$，真实概率满足

$$
\begin{aligned}
\sum_r\inf_{I_r}e^{-tv}\pi_r&\le L^{\rm ref}_{767}(t),\\
\sum_r\inf_{I_r}e^{-tv}\pi_r&\le L^{\rm point}_{767}(t),\\
\sum_r\sup_{I_r}e^{-tv}\pi_r&\ge e^{-t\mu}.
\end{aligned}
\tag{Q14}
$$

零带的 Laplace 下上端均为一；尾带分别为零和 $e^{-t}$。再加 $\sum_r\ell_r\pi_r\le\mu$、$\sum_re^{4\ell_r}\pi_r\le5/4$ 和质量上下两行，总计 $6\times3+2+2=22$ 条；非负性为变量域。保存为 $A\pi\le b$ 时，上界行用系数下端和右端上端；下界行用系数上端和右端下端，随后变号。真实概率因而属于保存的有理多面体。该集合非空且是闭单纯形的闭子集，故紧。

### C.4. 终端一步 profile 的零点、有限带与尾部

终端未来核 $a_f=b_f=0$，方差 positive-part 所产生的差 $e^{b_fY^+}-e^{b_fY}$ 准确为零。对 $q=p+i\omega$，令 $g=(q^2-q)/2$、$L=\rho\xi q-\kappa$、$c=\xi^2/2$，则

$$
D_q(v)=e^{rqh+hgv}-e^{a(h)+B(h)v},\quad
B'=g+LB+cB^2,\ B(0)=0,\quad a(h)=rqh+d\int_0^hB(t)dt.
\tag{Q15}
$$

指定模态为 Asian 的 $p=-1/48,\omega=64$ 及 put 的 $p=-1/4,\omega=-8,-24,\ldots,-120$。在 $\operatorname{Re}B=0$ 上，实漂移至多 $p(p-1)/2-(279/800)\omega^2<0$，故 $\operatorname{Re}B\le0$；径向界给 $|B(t)|\le|g|t$。

取 $P(t)=b_1t+b_2t^2+b_3t^3$，$b_1=g$、$b_2=Lg/2$、$b_3=(L^2g+2cg^2)/6$。确切 guard
$\operatorname{Re}b_1+\max(\operatorname{Re}b_2,0)h+\max(\operatorname{Re}b_3,0)h^2<0$
给全步 $\operatorname{Re}P\le0$。残差为 $-\sum_{k=3}^6r_kt^k$，其中

$$
r_3=Lb_3+2cb_1b_2,\quad r_4=c(2b_1b_3+b_2^2),\quad
r_5=2cb_2b_3,\quad r_6=cb_3^2.
$$

差方程的系数为 $L+c(B+P)$，实部不大于 $-\kappa_p$。变参数公式给

$$
E_B=\sum_{k=3}^6|r_k|_+\frac{h^{k+1}}{k+1},\qquad
E_A=d\sum_{k=3}^6|r_k|_+\frac{h^{k+2}}{(k+1)(k+2)}.
\tag{Q16}
$$

设

$$
\begin{aligned}
A_q&=\min\{|-d\int_0^hP|_++E_A,\ d|g|_+h^2/2\},\\
B_q&=\min\{|hg-P(h)|_++E_B,\ (|L|_++\xi^2|g|_+h)|g|_+h^2/2\},\\
m_q&=2-\max\{h\operatorname{Re}g,\min(0,\operatorname{Re}P(h)+E_B)\}>0.
\end{aligned}
\tag{Q17}
$$

第二分支用 $|B(t)|\le|g|t$；指数差的积分恒等式给全 $v\ge0$ 的界

$$
|e^{-2v}D_q(v)|\le e^{prh}(A_q+B_qv)e^{-m_qv}.
\tag{Q18}
$$

其带上确界由闭包的有限端点或驻点 $1/m_q-A_q/B_q$ 的值确定，无限尾极限为零；$B_q=0$ 时直接取单调分支，无需除法。粗分支 $|e^{-2v}D_q(v)|\le2e^{prh-2v}$ 也成立。因此(Q9)可使用

$$
h_{qr}=\min\{[4e^{2prh-4\ell_r}]_+,\ [e^{2prh}S_{qr}^2]_+\},\quad
S_{qr}=\sup_{v\in I_r}(A_q+B_qv)e^{-m_qv}.
\tag{Q19}
$$

零带准确在 $v=0$ 评价；尾带包括端点上包、可能的驻点和零极限。九个指定模态的 guards 与918个 profile 项由有理外舍入检查；这些输入与附录D.2.4的 primal-dual witness 一起关闭终端实例的计算义务。终端外包的严格收紧不单独给完整年度价格的货币误差。


## 附录D. 经典 Heston：共同状态与试验场残差

本节保留经典模型的原符号：\(\Delta^C=p_Q-p_P\)。用于模型减离散输出时取\(-\Delta^C\)。以下共同概率仅属于列明原\(Q\)链；连续残差另在\(P\)下积分。附录C给出原链矩界、分区与约束方向的完整证明。

### 附录D.1. 固定数学对象

令 $s=S/100$，连续过程满足

\[
ds_t=rs_tdt+s_t\sqrt{V_t}(\rho\,dW_t+\sqrt{1-\rho^2}\,dB_t),
\qquad dV_t=(d-\kappa V_t)dt+\xi\sqrt{V_t}\,dW_t,
\]

其中 $d=\kappa\bar v$，$r=1/100$，$s_0=1$。时间步长 $h=1/768$，离散实际一步为

\[
V'=[dh+(1-\kappa h)v+\xi\sqrt{hv}G]^+,
\]
\[
\log(s'/s)=rh-hv/2+\sqrt{hv}(\rho G+\sqrt{1-\rho^2}H),
\]

且 $G,H$ 是独立标准正态随机变量。股票增量与正部方差更新共用 $G$。$P$ 表示连续过程的分布，$Q$ 表示这条原离散链的分布。

理论参数域为

\[
\kappa\in[2,4],\quad \bar v,v_0\in[3/100,3/50],\quad
\xi\in[9/50,7/25],\quad \rho\in[-4/5,-3/10].
\]

固定实例

\[
\theta_*=(\kappa,\bar v,\xi,\rho,v_0)=(3,.045,.23,-.55,.045).
\]

九个标准期权为期限 $1/4,1/2,1$、执行价 $90,100,110$ 的欧式看跌。第十项为一年后到期、采用十二个月度观察值的算术平均亚式看涨价差

\[
R_{10}=(A-95)^+-(A-110)^+,\qquad
A=\frac1{12}\sum_{m=1}^{12}S_{m/12}.
\]

第八项为年度平值看跌；方向 $w=\mathbf e_{10}-\mathbf e_8$ 表示两项价格偏差之差。

### 附录D.2. 第一条机制：共同原链状态约束

#### 附录D.2.1. 结构条件及核心论证

取有限个多日期模式 $i=1,\ldots,M$，加载 $\alpha_{i,n}\in\mathbb C$ 满足

\[
\Re\alpha_{i,n}\le0,\qquad
\sum_n|\Re\alpha_{i,n}|\le\frac12.
\]

连续未来核为经过可积性验证的真实仿射核；实 Gaussian 配方、完整正部积分和有限望远镜给出模式偏差

\[
\Delta\Phi_i=\Phi_{Q,i}-\Phi_{P,i}=
\sum_{j=0}^{N-1}r_{ji}.
\]

将方差轴分割为有限个可测区间 $I_r$，零点和无界尾都包含在分割内。定义同一原 $Q$ 链的概率

\[
\pi_{jr}=Q(V_j\in I_r).
\]

设保存的非负数 $h_{jir}$ 覆盖相应带权实际核残差平方，且

\[
E_Q[W_{ji}^2 e^{4V_j}]\le K_j,
\quad K_j=\exp\{6/25+(73/75)jh\}.
\]

于是复数 Cauchy–Schwarz 给

\[
|r_{ji}|^2\le
K_j\sum_r h_{jir}\pi_{jr}=:a_{ji}\cdot\pi_j.
\tag{H1}
\]

其核心信息在于：式 (H1) 中所有 $i$ 共用**同一个** $\pi_j$，全部时间共用包含真实占用向量的同一个非空紧凸集 \(\mathcal F\)。概率约束须对原 $Q$ 有效；模式倾斜后的分布不能直接替换原概率。

证明的方案特定部分包括：完整 Gaussian 正部积分、真实连续未来核、加倍非正加载的指数矩、零原子以及无界尾。它们共同使 (H1) 成为本模型的有效包含，而非条件模板。完整证明在[附录C及经典模型补充推导](../evidence/classical-evidence.md)。

#### 附录D.2.2. 从联合残差到联合价格

对准确有限价格系数 $c_{ki}\in\mathbb C$，假定价格偏差已经接入带完整余项的接口

\[
e_k=p_{h,k}-p_{c,k}
=\Re\sum_{j,i}c_{ki}r_{ji}+R_k,
\qquad |R_k|\le\varrho_k.
\tag{H2}
\]

定义联合外集合

\[
\mathcal E=
\left\{\left(\Re\sum_{j,i}c_{ki}z_{ji}\right)_k:
\exists\Pi\in\mathcal F,
|z_{ji}|^2\le a_{ji}\cdot\pi_j\right\}
+\prod_k[-\varrho_k,\varrho_k].
\tag{H3}
\]

集合非空、紧、凸、中心对称，且 $e\in\mathcal E$。对 $w\in\mathbb R^{10}$，其支持函数为

\[
s_{\mathcal E}(w)=
\max_{\Pi\in\mathcal F}
\sum_{j,i}\left|\sum_kw_kc_{ki}\right|
\sqrt{a_{ji}\cdot\pi_j}
+\sum_k|w_k|\varrho_k.
\tag{H4}
\]

**桥梁证明。** 固定 $\Pi$ 后，每个 $z_{ji}$ 位于一个复数圆盘，方向 $w$ 对该圆盘的实线性支持恰为系数模乘半径。各圆盘在固定 $\Pi$ 下可独立选相位，因此它们的支持可以相加。随后对**同一个** $\mathcal F$ 最大化，得到 (H4)。紧性保证最大值达到。实际残差及其实际概率提供 (H3) 的可行表示，故价格向量属于集合。证毕。

存在跨时间约束时，准确式为 $\max_{\mathcal F}\sum_j$。仅当 $\mathcal F=\prod_j\mathcal P_j$ 时，才可分解为逐时间最大值之和。

#### 附录D.2.3. 严格收紧的判据

令

\[
F_k(\Pi)=\sum_{j,i}|c_{ki}|\sqrt{a_{ji}\cdot\pi_j},
\quad m_k=\max_{\mathcal F}F_k,
\]
\[
\mathcal B=\operatorname{rect}(\mathcal E)
=\prod_k[-m_k-\varrho_k,m_k+\varrho_k].
\]

这是**同一联合外集合自身的最小坐标矩形**。精确差距

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

各项非负。故 $G(w)=0$ 当且仅当存在同一个 $\Pi_*$ 同时满足：

1. 最大化所有 $w_k\ne0$ 的**完整价格行** $F_k$；
2. 对每个正半径的 $(j,i)$，非零复数 $w_kc_{ki}$ 均位于同一非负射线。

不存在这种共同见证时，$G(w)>0$。这既是充分条件，也是所构造集合相对于其最小矩形严格收紧的必要条件。零半径无需相位条件；零方向的差距为零。

**证明。** 公共余项盒在两边支持之差中准确相消。加减 $\sum_k|w_k|F_k(\Pi)$ 得 (H5)。紧性保证最小值达到；非负和为零要求每个活动行缺额为零，并要求每个正半径处的复数三角不等式达到等号。这给出两项条件。反向代入共同见证得到零差距。证毕。

这项刻画的对象是**外集合的严格收紧**。它不需要假设模型价格偏差在外集合边界达到，也不将外集合差距解释为模型价格偏差的下界。

#### 附录D.2.4. 已认证的原合约实例

指定终端层实例固定 $j=767$、$\theta_*$、同一原模式目录及预先固定的 $\mathcal P_{767}$。分割为

\[
I_0=\{0\},\qquad I_r=((r-1)/100,r/100]\ (1\le r\le100),
\qquad I_{101}=(1,\infty).
\]

这个集合包含原 $Q$ 的真实概率，通过完整均值、指数矩和两组 Laplace 信息约束构成；保存为 102 个非负变量、22 条准确有理约束。全部九条实际一步残差包络已处理零、有限区间 和尾。

Asian 完整终端价格行经共轭化约为

\[
F_A(\pi)=C_A\sqrt{K_{767}}\sqrt{a\cdot\pi},\qquad C_A>0.
\]

一年期平值看跌期权的八频率完整行是

\[
F_P(\pi)=\frac{1600e^{-.01}}{\pi}\sqrt{K_{767}}
\sum_{\omega=8,24,\ldots,120}
\frac{\sqrt{d_\omega\cdot\pi}}
{\sqrt{(\omega^2+1/16)(\omega^2+25/16)}}.
\tag{H6}
\]

准确 原问题/对偶证书证明 $F_A$ 的唯一最大点 $\pi^A$ 仅在区间 1、2、6上有支撑；其十进制近似为

\[
(\pi^A_1,\pi^A_2,\pi^A_6)
\approx(.0276833515163,.0487291439380,.923587504546).
\]

三条具有正对偶乘子的活动约束构成非奇异矩阵，所有非支持指标的约化费用严格为正，因而最优解的唯一性由精确代数得到。

同一概率集合中存在精确可行点 $\pi^B$，支撑 区间 5、6。沿 $\pi(t)=\pi^A+t(\pi^B-\pi^A)$，看跌期权辅助行的导数认证为

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

其下端严格大于 $3\times10^{-9}$。所以 $\pi^A$ 不是看跌期权行的最大点，两条完整价格行没有共同最大点，得到

\[
g_{767}=\max F_A+\max F_P-\max(F_A+F_P)>0.
\tag{H8}
\]

(H7) 是辅助行的方向导数；(H8) 是该终端外集合的定性严格差距。对于保持给定模式、给定包络身份并以有效逐时间乘积集合接续的构造，各层 $g_j\ge0$，于是其累计未截交支持差满足 $\sum_jg_j\ge g_{767}>0$。更换概率信息、模式目录或收益截交规则时，按 (H5) 对该新集合重新验证。

证据为[终端严格分离命题](../evidence/classical-evidence.md)、[准确输入](https://github.com/130U/certified-rough-heston-valuation/blob/6a5134197db60c765ca3aea4f6cdeb2bafbb6617/code/classical/terminal767-input.json)、[结果证书](https://github.com/130U/certified-rough-heston-valuation/blob/6a5134197db60c765ca3aea4f6cdeb2bafbb6617/code/classical/terminal767-result.json)及[独立有理读回](https://github.com/130U/certified-rough-heston-valuation/blob/6a5134197db60c765ca3aea4f6cdeb2bafbb6617/code/classical/terminal767-historical-review.json)。输入 SHA256：`5ad2c18e9336db16e3957b9b1f6669f0f9065a13991ebed8a0498df9b942524c`。独立小检查记录 407 项准确算术检查。

### 附录D.3. 精确未来场与有限试验场的共同框架

#### 附录D.3.1. 函数类别与充分条件

本机制以 $X=(P,Q,R,\widetilde u)$ 为对象，其中 $R$ 是同一个原收益或准确有限价格转换余项，$\widetilde u$ 是一个确定试验场。

| 符号 | 本研究中的具体内容 |
|---|---|
| $A(X)$ | $\widetilde u$ 是满足下述可积/正则条件的精确连续未来值函数；终值和观察时点与 $R$ 准确相合 |
| $H(X)$ | 同一场满足全状态增长、平方权重一致可积、分段 Itô 正则、真实观察时点迹值、时间 $L^1$ 残差支配、终值差支配及原 $Q$ 缺陷可积 |
| $\Phi$ | 对原 $Q$ 用有限 全期望公式；对原 $P$ 用分段 Itô、Lyapunov 去停止及 $L^1$ 迹值；两式相减 |
| $M(X)$ | 同一个场的四项有符号残差恒等式 |
| $B(X)$ | 所有已认证残差上界形成原连续/离散价格偏差的有效区间或金额上界 |
| $C(X)$ | 满足列明可核查增长、残差与接口条件的有限确定时间和状态表示 |
| $X_\star\in C\setminus A$ | 式(H17)的完全显式解析场；公式直接验证全局增长、迹、可积性、准确终值与非零生成元残差 |

这里 $H$ 是充分条件，不定义成“价格偏差可控”，也不要求试验场等于未知精确解。精确未来值函数满足后向方程，连续残差为零；准确观察时点和终值也使对应缺陷为零，因此 $A\Rightarrow H\Rightarrow M\Rightarrow B$ 恢复原精确未来值函数望远镜公式。

“分别已有各个价格的误差区间”本身不能推出共同状态结构：那些区间没有给出跨价格相容性见证。因此，试验场推广由本节恒等式刻画，共同状态包含则提供保留价格依赖信息的联合预算机制。

#### 附录D.3.2. 结构条件 $H$

在两个观察时点之间，全状态为 \(x=(s,v,A_m,\ell_m)\)，\(A_m\) 与 \(\ell_m\) 分别记录已观测股票价格之和与对数股票价格之和。观察时点用准确映射 \(J_i\) 更新历史。生成元为

\[
\mathcal L=rs\partial_s+(d-\kappa v)\partial_v
+\frac12vs^2\partial_{ss}+\rho\xi vs\partial_{sv}
+\frac12\xi^2v\partial_{vv}.
\]

取非负权重 \(W\)，例如

\[
W=s^{-1/2}e^v+e^{-\ell_m/24}s^{-(12-m)/24}e^v,
\]

或固定设定中更适合算术支的自然权重

\[
W^{\rm nat}=\mathfrak B_m^{-1/2}e^v+\mathfrak G_m^{-1/2}e^v,
\quad \mathfrak B_m=(A_m+(12-m)s)/12,
\quad \mathfrak G_m=e^{\ell_m/12}s^{(12-m)/12}.
\]

这些权重观察时点前后保持一致，原 Lyapunov 估计给连续和离散时点的矩上界；在 $\theta_*$、一年内可取 $E_PW,E_QW<5/2$，并给连续停止时刻的平方矩上界。每个近似函数固定一种权重，后续月份不互换。

场 $\widetilde u$ 在各开观察时点区间局部 $C^{1,2}$，在 $v=0$ 具有可用于 Itô 的右侧延拓；两侧在紧状态集上具有一致真实迹值。假设

\[
|\widetilde u|\le CW,\qquad
|\mathfrak r(t,x)|\le\eta_c(t)W(t,x),\quad
\int_0^1\eta_c(t)dt<\infty,
\]
\[
|d_i(x)|\le\eta_iW(t_i-,x),\qquad
|\delta(x)|\le\eta_TW(1,x),
\]

其中

\[
\mathscr D_j=Q_j\widetilde u_{j+1}-\widetilde u_j,
\quad \mathfrak r=(\partial_t+\mathcal L)\widetilde u,
\quad d_i=\widetilde u(t_i-,x)-\widetilde u(t_i+,J_ix),
\quad \delta=R-\widetilde u_N.
\tag{H9}
\]

$Q_j$ 包含原正部核及步末观察时点；终值与 跳跃 采用同一约定，每个更新只记一次。全部支配覆盖全状态、零边界与无界尾。原 $Q$ 下的离散缺陷可积且有已认证全期包含

\[
\sum_j E_Q\mathscr D_j\in[L_Q,U_Q].
\]

#### 附录D.3.3. 核心引理与证明：$H\Rightarrow M$

**核心引理。** 在上述条件下，

\[
\boxed{
E_QR-E_PR=
\sum_jE_Q\mathscr D_j
-E_P\int_0^1\mathfrak r(t,X_t)dt
+\sum_iE_Pd_i+(E_Q-E_P)\delta.}
\tag{H10}
\]

**证明。** 离散有限 全期望公式 给

\[
E_Q\widetilde u_N-\widetilde u_0
=\sum_jE_Q\mathscr D_j.
\]

连续一侧，先在远离观察时点的闭子区间将过程停在紧状态域。局部 Itô 随机积分期望为零。平方权重 Lyapunov 界与 \( |\widetilde u|\le CW\) 给停止场值族一致可积，故场值可去停止。时间 $L^1$ 支配和 \(E_PW\) 的一致上界给

\[
E_P\int_0^1|\mathfrak r(t,X_t)|dt
\le\int_0^1\eta_c(t)E_PW(t,X_t)dt<\infty,
\]

因此残差积分可按绝对可积支配去停止。让子区间端点趋近观察时点时，真实迹值、连续路径和同一一致可积界给 $L^1$ 极限。函数在观察时点的跳跃 为 $-d_i$，所以逐区间求和得

\[
E_P\widetilde u_N-\widetilde u_0
=E_P\int_0^1\mathfrak r(t,X_t)dt-\sum_iE_Pd_i.
\]

两式相减，再将 $\delta=R-\widetilde u_N$ 加入两种期望，得到 (H10)。共同初值准确消去。证毕。

式(H10)为有符号恒等式，各项分别由同一函数在离散链和连续过程中的残差确定。该推导使用成熟 Itô/残差工具，完成本正部核、多观察时点、无界状态空间的尾部和增长条件之间的连接。

#### 附录D.3.4. 桥梁命题：$M\Rightarrow B$

在 $\theta_*$ 下，(H10) 给

\[
|E_QR-E_PR|\le
\max(|L_Q|,|U_Q|)
+\frac52\left(\int_0^1\eta_c(t)dt+\sum_i\eta_i\right)
+5\eta_T.
\tag{H11}
\]

如果离散全态缺陷满足 \( |\mathscr D_j|\le h\eta_{Q,j}W\)，则

\[
|E_QR-E_PR|\le
\frac52\left(h\sum_j\eta_{Q,j}
+\int_0^1\eta_c(t)dt+\sum_i\eta_i\right)+5\eta_T.
\tag{H12}
\]

证明由 (H10) 的各项可积性与三角不等式直接得到。若这些项另有共同有符号信息，可以先取其共同可行集的线性像；(H11)–(H12) 是合法且便于计算的非负上界版本。

#### 附录D.3.5. 完全显式的解析见证

为使 \(C\setminus A\) 的判断可在附录D.3.5中直接复核，再给出一个不依赖大规模场系数的合法对象。固定 \(T=1\)、任意 \(\varepsilon>0\)，取终值 \(R=s_T^{-1/2}\) 和场

\[
a_\varepsilon(t)=1+\varepsilon t(1-t),\qquad
\widetilde u_\varepsilon(t,x)=a_\varepsilon(t)s^{-1/2}.
\tag{H17}
\]

该场不依赖历史，所有观察时点的 跳跃 为零，终值准确，\(1\le a_\varepsilon\le C_\varepsilon:=1+\varepsilon/4\)。令 \(W_A=s^{-1/2}e^v\)；已有连续平方 Lyapunov 和原 \(Q\) 权重估计均适用，且 \(|\widetilde u_\varepsilon|\le C_\varepsilon W_A\)。

真实生成元给

\[
\mathfrak r_\varepsilon
=s^{-1/2}\left\{\varepsilon(1-2t)
+a_\varepsilon(t)\left(\frac{3v}{8}-\frac r2\right)\right\}.
\tag{H18}
\]

由 \(ve^{-v}\le1/e\)，全年连续支配可取常数

\[
\eta_c=\varepsilon+C_\varepsilon\left(\frac r2+\frac3{8e}\right)<\infty.
\tag{H19}
\]

原股票更新的 Gaussian 积分准确给

\[
\mathscr D_j=s^{-1/2}
\left\{a_\varepsilon(t_{j+1})
\exp\!\left[h\left(\frac{3v}{8}-\frac r2\right)\right]
-a_\varepsilon(t_j)\right\}.
\]

利用 \(|a_\varepsilon(t_{j+1})-a_\varepsilon(t_j)|\le\varepsilon h\)、
\(|e^x-1|\le |x|e^{\max(x,0)}\) 及
\(ve^{-cv}\le1/(ec)\)，\(c=1-3h/8>0\)，得到全态界

\[
|\mathscr D_j|\le h\eta_QW_A,\qquad
\eta_Q=\varepsilon+C_\varepsilon
\left(\frac r2+\frac3{8e(1-3h/8)}\right).
\tag{H20}
\]

这些显式有限常数、准确 终值与观察时点条件、全态平滑及平方矩支配给出 \(C\Rightarrow H\) 的直接解析验证。在 \(t=1/2,v=r>0\)，式 (H18) 等于
\(-r(1+\varepsilon/4)s^{-1/2}/8<0\)，所以该场不是满足连续后向方程的精确未来值函数。由此得一个自含的 \(X_\star\in C\setminus A\)。

精确连续未来值函数对该负幂终值属于原合法负加载的仿射类，满足已核验矩条件。因此同一对象类中既有 \(A\) 的精确未来值函数，也有 (H17) 的非精确场；该残差恒等式同样适用于式(H17)定义的近似函数。此解析见证用于证明适用范围扩大，金融使用实例仍采用原合约和准确证书。(H19)–(H20) 提供全年可积的有限充分界，实际报价预算使用其对应场的独立证书。


### 附录D.4. 补充的金融桥梁：组合金额与同向量报价接受集

#### 附录D.4.1. 组合金额界

**命题（联合证书用于线性组合）。** 令 $p_c,p_h\in\mathbb R^d$ 是同一参数下连续/离散的贴现价格，$e=p_h-p_c\in\mathcal E$，$\mathcal E$ 为非空紧集。对确定持仓或价格比较系数 $w\in\mathbb R^d$，有

\[
w^Tp_h-s_{\mathcal E}(w)
\le w^Tp_c\le
w^Tp_h+s_{\mathcal E}(-w).
\tag{H14}
\]

若 $\mathcal E=-\mathcal E$，两侧半宽同为 $s_{\mathcal E}(w)$。若离散价格中心 $\widehat p_h$ 自身满足 $n=p_h-\widehat p_h\in\mathcal N$，则

\[
w^T\widehat p_h-s_{\mathcal N}(-w)-s_{\mathcal E}(w)
\le w^Tp_c\le
w^T\widehat p_h+s_{\mathcal N}(w)+s_{\mathcal E}(-w).
\tag{H15}
\]

若另有包含真实 $(n,e)$ 的同一紧集 $\mathcal K\subseteq\mathbb R^{2d}$，则以 $s_{\mathcal K}(w,-w)$ 及 $s_{\mathcal K}(-w,w)$ 替代 (H15) 的两项和，可完整保留两种误差的共同信息。

**证明。** 因 $p_c=p_h-e$，$w^Te\le s_{\mathcal E}(w)$ 且 $-w^Te\le s_{\mathcal E}(-w)$，得 (H14)。进一步 $p_c=\widehat p_h+n-e$，分别控制 $w^Tn$ 与 $-w^Te$ 得 (H15)；在共同 $(n,e)$ 集合上直接取线性支持即可得到最后一句。证毕。

这是支持函数的标准线性传播，不另列为独立数学创新。它说明主理论如何转成金融输出：对价差、组合市值或预设比较方向，使用整向量误差保证，而不是任意拼接单合约端点。

在原终端实例的 $w=\mathbf e_{10}-\mathbf e_8$ 上，(H8) 证明同信息联合结构给出了严格更小的终端方向预算。该方向对应算术平均亚式期权价差和一年期平值看跌期权的价格比较；它由设定预先固定，不承担最优对冲或交易信号含义。

#### 附录D.4.2. 校准接受规则与目标估值

给定闭的九价接受集 $\mathcal Y$、离散价格中心 \(\widehat p_h\)，以及同一紧误差输入集 $\mathcal K_\theta$ 包含真实 $(n,e)$。定义

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

真实校准价格满足接受规则时，模型目标价格属于 $\mathcal A_\theta$。$\mathcal T_\theta=\varnothing$ 则可以排除该参数在此接受规则下的相容性；非空时目标上下端达到。共同输入扩为坐标矩形只会扩大或保持目标集合。

证明仅需 $p_c=\widehat p_h+n-e$、紧集与闭接受条件的交集仍紧、线性函数在非空紧集上达到极值。该规则保留同一个价格误差向量；适合“用有流动性的标准期权约束参数，再估值路径依赖合约”的流程。具体报价设定取得有效中心与全误差输入后，(H16) 直接成为可计算的筛选和估值接口。