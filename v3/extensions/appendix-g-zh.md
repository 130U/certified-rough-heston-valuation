## 附录 G. 非精确试探函数与有符号误差恒等式

本附录使用同一个确定性试探函数进行连续—离散比较，该函数不必满足后向方程。我们独立于未知精确解陈述充分条件，证明四个有符号项，并构造一个全局可积的非精确解析函数。以下期望未贴现；由 payoff 转为价格时，应将恒等式与界乘以共同贴现因子。

### G.1. 状态、左右迹与可容许条件

采用附录 F 的原概率律 \(P,Q\)、参数及相关正部更新。月度观测之间，状态为 \(x=(s,v,A_m,\ell_m)\)，其中 \(A_m\) 是已观测归一化股票值之和，\(\ell_m\) 是其对数之和。观测映射 \(J_i\) 将当前 \(s,\log s\) 加入相应历史。观测之间的生成器为

\[
\mathcal L=rs\partial_s+(d-\kappa v)\partial_v
+\tfrac12vs^2\partial_{ss}+\rho\xi vs\partial_{sv}
+\tfrac12\xi^2v\partial_{vv}.\tag{G01}
\]

在整个期限选择同一个固定非负权重，例如

\[
\begin{aligned}
W&=e^v\{s^{-1/2}+e^{-\ell_m/24}s^{-(12-m)/24}\},\\
W^{\rm nat}&=e^v\{\mathfrak B_m^{-1/2}+\mathfrak G_m^{-1/2}\},\qquad
\mathfrak B_m=(A_m+(12-m)s)/12,\quad
\mathfrak G_m=e^{\ell_m/12}s^{(12-m)/12}.
\end{aligned}\tag{G02}
\]

两个权重都在观测映射前后精确匹配。算术均值不小于几何均值，所以 \(W^{\rm nat}\le2e^v\mathfrak G_m^{-1/2}\)。两个权重中的历史因子都对应总绝对值至多为 \(1/2\) 的多日期非正实载荷。

**引理（权重矩界）。** 在 \(\theta_*\) 和 \(0\le t\le1\) 上，每个权重满足

\[
\sup_tE_PW(t,X_t)<5/2,\qquad \max_jE_QW(t_j,X_j)<5/2,
\qquad \sup_{\tau\le1}E_PW(\tau,X_\tau)^2<\infty.\tag{G03}
\]

最后的上确界取遍下面紧状态域局部化使用的停时。证明连续单分支界时，对 \(e^{L+pZ+V}\)、\(p\in[-1/2,0]\) 使用生成器；方差系数 \(\gamma_p-\kappa_p+\xi^2/2<0\)，常数漂移 \(rp+d\le d\)，观测时载荷变化抵消。非负停时超鞅给出单分支期望至多为 \(e^{v_0+d}=e^{9/50}<5/4\)。离散概率律使用 (F10)–(F11) 的 \(B=1\) 情形及 \(F_p(1)\le1\)，得到单分支界 \(e^{v_0+d+1/300}=e^{11/60}<5/4\)。将两个分支相加，或用 \(W^{\rm nat}\le2e^v\mathfrak G_m^{-1/2}\)，得到所需一阶界；严格比较由 \(\log(5/4)\ge1/5\) 保证。

平方界使用 \((a+b)^2\le2(a^2+b^2)\)。每个平方分支的总股票载荷至多为一，方差载荷为二；将方差载荷提高到四可支配该分支。连续指数超鞅的方差系数至多为 \(1-4(1.776)+8(7/25)^2<0\)，常数漂移至多为 \(24/25\)，故停时给出统一有限二阶矩；自然权重同理。这足以保证被 \(W\) 支配的函数一致可积，无需假设停时随机积分的极限本身是普通鞅。

\(R\) 是两个概率律下同一终端 payoff 或同一精确有限转换余项。确定性函数 \(\widetilde u\) 在观测之间局部 \(C^{1,2}\)，在 \(v=0\) 处有可用于 Itô 公式的右侧延拓，并在紧状态集上一致存在真正的单侧迹。要求全局界

\[
\begin{aligned}
|\widetilde u|&\le CW,&
|\mathfrak r(t,x)|&\le\eta_c(t)W(t,x),& \int_0^1\eta_c(t)dt&<\infty,\\
|d_i(x)|&\le\eta_iW(t_i-,x),&
|\delta(x)|&\le\eta_TW(1,x),& C,\eta_i,\eta_T&<\infty.
\end{aligned}\tag{G04}
\]

支配必须覆盖所有状态、\(v=0\) 和无界尾部。定义

\[
\begin{aligned}
\mathscr D_j&=Q_j\widetilde u_{j+1}-\widetilde u_j,&
\mathfrak r&=(\partial_t+\mathcal L)\widetilde u,\\
d_i(x)&=\widetilde u(t_i-,x)-\widetilde u(t_i+,J_ix),&
\delta&=R-\widetilde u_N.
\end{aligned}\tag{G05}
\]

跳跃残差定义为**左迹减观测更新后的右迹**。\(Q_j\) 包含原核和步末观测；两个概率律都采用相同的观测后终端约定，每次更新恰计一次。\(\mathscr D_j\) 必须在原 \(Q\) 下可积；有效的完整期限包络为 \(\sum_jE_Q\mathscr D_j\in[L_Q,U_Q]\)。另一充分条件是 \(\lvert\mathscr D_j\rvert\le h\eta_{Q,j}W\)。

这些条件没有通过假设所求误差界来定义可容许性。精确未来值函数只有在上述正则性和支配条件已验证后，才属于此类；有限表示也只有在增长、残差、左右迹、终端值及原核接口均已验证后，才属于此类。

### G.2. 四项有符号恒等式

**定理（同一函数的残差恒等式）。** 在 (G03)–(G05) 和原 \(Q\) 下离散残差可积的条件下，

\[
\boxed{E_QR-E_PR=
\sum_jE_Q\mathscr D_j-E_P\int_0^1\mathfrak r(t,X_t)dt
+\sum_iE_Pd_i+(E_Q-E_P)\delta.}\tag{G06}
\]

**证明。** 原 \(Q\) 下有限条件望远镜求和给出

\[
E_Q\widetilde u_N-\widetilde u_0=\sum_jE_Q\mathscr D_j.\tag{G07}
\]

对 \(P\)，先在紧状态域内、远离观测时刻的闭子区间上局部化，Itô 公式中的随机积分期望为零。(G03) 的二阶矩界与 \(|\widetilde u|\le CW\) 保证停时函数值一致可积，解除停时时得到 \(L^1\) 收敛。Tonelli 及 (G04) 给出 \(E_P\int|\mathfrak r|\le\int\eta_c(t)E_PW(t,X_t)dt<\infty\)，从而可用绝对可积支配解除时间积分中的停时。区间端点趋近观测时刻时，紧集上一致的真正左右迹与连续路径给出几乎处处收敛，同一一致可积性给出 \(L^1\) 收敛。实际函数跳跃为 \(-d_i\)。对所有区间和跳跃求和，得到

\[
E_P\widetilde u_N-\widetilde u_0
=E_P\int_0^1\mathfrak r(t,X_t)dt-\sum_iE_Pd_i.\tag{G08}
\]

由 (G07) 减 (G08)，再分别加入 \(\delta=R-\widetilde u_N\) 的两个期望，共同确定性初值精确抵消，得到 (G06)。采用上述观测后约定，论证也包括终端日的观测。∎

若改为定义 \(J_i^{\rm jump}=\widetilde u(t_i+,J_ix)-\widetilde u(t_i-,x)\)，则 (G06) 对应项必须写作 \(-\sum_iE_PJ_i^{\rm jump}\)。明确符号约定，避免混用两种定义。对精确延续，后向残差、观测残差和终端差均消失，恢复 (F08)；非精确函数则保留四个有符号项。

### G.3. 有效的充分误差界

在 \(\theta_*\) 处，(G06) 和权重引理给出

\[
\begin{aligned}
|E_QR-E_PR|&\le\max(|L_Q|,|U_Q|)
+\tfrac52\left(\int_0^1\eta_c(t)dt+\sum_i\eta_i\right)+5\eta_T,\\
|E_QR-E_PR|&\le\tfrac52\left(h\sum_j\eta_{Q,j}
+\int_0^1\eta_c(t)dt+\sum_i\eta_i\right)+5\eta_T
\quad\text{if }|\mathscr D_j|\le h\eta_{Q,j}W.
\end{aligned}\tag{G09}
\]

这是由三角不等式得到的非负充分界；若已取得四项的共同有符号包络，可直接传播其线性像。各价格的独立区间不能自行提供共同状态兼容性见证。尤其，残差包络的必要下界，并不是对 (G09) 任一充分上界的计算。

### G.4. 自洽的非精确解析函数

固定 \(T=1\)、\(\varepsilon>0\)、\(R=s_T^{-1/2}\)，取

\[
a_\varepsilon(t)=1+\varepsilon t(1-t),\qquad
\widetilde u_\varepsilon(t,x)=a_\varepsilon(t)s^{-1/2},\qquad
1\le a_\varepsilon\le C_\varepsilon:=1+\varepsilon/4.\tag{G10}
\]

使用单分支权重 \(W_A=s^{-1/2}e^v\)，前面的权重证明同样适用。该函数在 \(s>0,v\ge0\) 上全局正则，不依赖历史，观测左右迹和终端值精确匹配，且 \(|\widetilde u_\varepsilon|\le C_\varepsilon W_A\)。生成器残差为

\[
\mathfrak r_\varepsilon=s^{-1/2}
\{\varepsilon(1-2t)+a_\varepsilon(t)(3v/8-r/2)\}.\tag{G11}
\]

由 \(ve^{-v}\le1/e\)，可取全局、时间常数型支配函数

\[
\eta_c=\varepsilon+C_\varepsilon(r/2+3/(8e)),\qquad
\int_0^1\eta_c(t)dt=\eta_c<\infty,\qquad \eta_i=\eta_T=0.\tag{G12}
\]

尽管股票与方差共享 \(G\)，这里的函数不依赖下一步方差，所以原股票高斯积分可以精确计算：

\[
\mathscr D_j=s^{-1/2}\{a_\varepsilon(t_{j+1})e^{h(3v/8-r/2)}-a_\varepsilon(t_j)\},\qquad
|\mathscr D_j|\le h\eta_QW_A,\quad
\eta_Q=\varepsilon+C_\varepsilon\{r/2+3/[8e(1-3h/8)]\}.\tag{G13}
\]

为证明该界，将差写作 \((a_{j+1}-a_j)e^{h(3v/8-r/2)}+a_j(e^{h(3v/8-r/2)}-1)\)，使用 \(|a_{j+1}-a_j|\le\varepsilon h\)、\(|e^x-1|\le|x|e^{\max(x,0)}\)，及 \(c=1-3h/8>0\) 时的 \(ve^{-cv}\le1/(ec)\)。因此每个离散残差可积；因 \(Nh=1\)，完整期限包络可显式取为 \(\sum_jE_Q\mathscr D_j\in[-(5/2)\eta_Q,(5/2)\eta_Q]\)。代入 (G09)，得到有限充分界 \((5/2)(\eta_Q+\eta_c)\)。

在 \(t=1/2,v=r>0\) 处，(G11) 等于 \(-rC_\varepsilon s^{-1/2}/8<0\)，所以该函数不是精确未来值函数。同一个负幂 payoff 的精确函数由附录 F 的仿射延续和矩界证明存在，其载荷为 \(-1/2\)。同一可容许对象类因此既含精确函数，也含非精确函数，四项恒等式对二者均适用。此例是解析适用范围见证，不是原市场工具的数值证书。

### G.5. 十三个基函数诊断的证明范围

保存的经典试探函数诊断具有另一种有条件的用途。令 \(n=12-m\)、\(B=(A_m+ns)/12\)、\(y=A_m/(A_m+ns)\)、\(\beta=1-y\)、\(z=v/(1+v)\)，其分支为 \(B^{-q}P(y,v)\)。本节 \(\Re q=1/2\)，所以 \(B^{-q}\) 对应负股票阻尼；这里的 \(q\) 不同于附录 F 中的负载荷 \(q\) 记号。共轭生成器为

\[
\begin{aligned}
\mathcal L_qP={}&-ry\beta P_y+dP_v-qr\beta P\\
&+v\{\tfrac12y^2\beta^2P_{yy}-\rho\xi y\beta P_{yv}
+\tfrac12\xi^2P_{vv}+(1+q)y\beta^2P_y\\
&\hspace{12mm}-(\kappa+q\rho\xi\beta)P_v+\tfrac12q(q+1)\beta^2P\}.
\end{aligned}\tag{G14}
\]

基函数为 \(\phi_{ij}=\beta y^iz^j\)、\(0\le i\le2,0\le j\le3\)，另加 \(\psi=v\beta^2\)。它们精确表示终端强迫项 \(\mathcal L_q1=-qr\phi_{00}+q(q+1)\psi/2\)；这是终端生成器补全，不是对所有生成器像的闭合。对有限端点常数，函数使用三次 Hermite 插值及精确物理斜率 \(-Kc-g(q)\)，其中 \(g(q)=-qr e_{00}+q(q+1)e_\psi/2\)。令 \(\gamma=(n-1)/n\)，精确观测传递为

\[
(T_nc)_{\ell j}=\gamma\sum_{i=\ell}^2\binom i\ell\gamma^\ell n^{-i+\ell}c_{ij},
\qquad T_n\psi=\gamma^2\psi.\tag{G15}
\]

这来自 \(y'=\gamma y+1/n\)、\(B'=B\)、\(\beta'=\gamma\beta\)。终端修正节点为零；精确传递及斜率定义左右迹，浮点生成值不能替代这些定义。有限函数满足 \(|P|\le C_0+C_1v\le(C_0+2C_1/e)e^{v/2}\)。其连续残差关于 \(v\) 至多二次，\(y,z\) 系数有界，因此 \(e^{-v}|F|\le a_0+a_1/e+4a_2/e^2\)。完整使用 (G09) 仍需要实际系数银行、所有状态下的原 \(Q\) 包络及完整期限充分上界。

对保存的首月状态 \(m=0,y=0,v=9/200\)，令 \(w=(1,z,z^2,z^3,0,\ldots,0,v)\)、\(\ell\) 为基函数生成器值行、\(\ell_0=-qr+q(q+1)v/2\)。单个时间片上的精确积分为

\[
\int F_{A,q}dt=
\left[w+\frac{h^2}{12}\ell K\right](c_R-c_L)
+\frac h2\ell(c_L+c_R)+h\ell_0.\tag{G16}
\]

因为 \(\int c(t)dt=h(c_L+c_R)/2+h^2(s_L-s_R)/12\)，且 \(s_L-s_R=K(c_R-c_L)\)。归档包含全部 3080 个加权复积分区间（385 模态、八单元，覆盖原 64 时间片）。在共同相位零处，对每单元求实模态区间之和，使用 \(\int|F|\ge|\int F|\)，再减去已积分的几何分支上界。精确总值由 `field-result.json` 的数学字段 `whole_lower` 指定：

\[
\int_0^{1/12}\eta_c(t)dt\ge L_*,\qquad
L_*>0.003407444052031154>0.\tag{G17}
\]

它拒绝所选分配 \(\int\eta_c\le1/1000\)，保留状态 `FAIL_SELECTED_INTEGRATED_PDE_CONTRACT_ONLY`；它不拒绝所有充分分配，不对整个试探空间取最优，也不从下方控制实际有符号价格偏差。可移植读取器 `verify_field_receipt.py` 核查保存区间的精确聚合，不重新生成缺失系数银行，也不重跑归档直接积分。因此 (G17) 属于归档函数的必要条件诊断；显式函数 (G10) 则不依赖该银行，独立证明非精确可容许性。这里不推出完整年度金额 PASS。

机器附录使用 `baseline/english-heston-release/code/classical/field-cell-integrals.json`、`field-result.json`、`field-independent-readback.json`、`provenance.json`、`verify_field_receipt.py`，由发布清单固定科学身份。联系字段、运行环境和执行测量元数据均非这些数学断言所必需。
