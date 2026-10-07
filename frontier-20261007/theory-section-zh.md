### 9.6. 正分数阶曲线核与参考中心转换

定理9.2所需的曲线条件是 \(q_\alpha=(I^{1-\alpha}\xi)'\) 非负，而非 \(\xi\) 递增。真解和参考仍须属于 \(AC[0,T]\)、具有相同零初值，并满足(N1)的完整时间残差和耗散前提。物理残差仍为 \(R\)，规范残差为 \(R/\nu\)，物理耗散为 \(\lambda=\nu\sigma>0\)。两指数继续采用第5节的D-type定义。这些条件须在每次应用中验证；定价核条件本身不证明随机模型存在，也不扩展已经核验的Riccati正则性域。

对实曲线 \(\xi\in AC[0,T]\)、\(\xi(0)=V_0\ge0\)，精确的充分条件是

\[
q_\alpha=V_0g_{1-\alpha}+g_{1-\alpha}*\xi'\ge0
\quad\text{a.e.},\qquad g_\beta(t)=t^{\beta-1}/\Gamma(\beta).
\tag{FQ1}
\]

不要求 \(\xi'\) 非负。事实上，\(A_\alpha=I^{1-\alpha}\xi=V_0g_{2-\alpha}+g_{2-\alpha}*\xi'\) 绝对连续、\(A_\alpha(0)=0\)，且

\[
\|q_\alpha\|_1\le
\frac{T^{1-\alpha}}{\Gamma(2-\alpha)}(V_0+\|\xi'\|_1),
\qquad g_\alpha*q_\alpha=\xi.
\tag{FQ2}
\]

第二个恒等式由绝对Fubini和 \(g_\alpha*g_{1-\alpha}=g_1\) 给出，对有符号 \(\xi'\) 仍成立；不能删去启动项 \(V_0g_{1-\alpha}\)。(FQ1)进一步推出 \(\xi\ge0\)。因此定理9.2的证明继续成立：积分分部给出 \(L_T-\widehat L_T=\nu^{-1}(q_\alpha*e)(T)\)，正resolvent恒等式给出

\[
0\le q_\alpha*k_\lambda
=\xi-\lambda\xi*k_\lambda\le\xi.
\tag{FQ3}
\]

指数的Fubini步骤由 \(\|\xi\|_\infty T^{1-\alpha}\|e'\|_1/\Gamma(2-\alpha)\) 支配；边界项因 \(e(0)=A_\alpha(0)=0\) 消失。AC情形的Caputo凸性与正零初值逆仍为先行工具 [LiLiu2018, Kopteva2021v2]。完整有限历史卷积、时间单元权重(N6)与节点半径的向外构造均在(FQ1)下有效；单元始终携带全部Caputo历史。

这是对充分曲线条件的严格放宽，不宣称它对所有可能的认证方法必要。若 \(q_\alpha\) 变号，一般安全式是 \(\nu^{-1}(|q_\alpha|*k_\lambda*R)(T)\)，不能未经证明沿用正消去。分数阶forward variance表示及模型可实现性约束已见 [ElEuchRosenbaum2017v1, Proposition 3.1 and Corollary 3.3]；本解析条件不取代这些约束。

**推论9.4（下降解析曲线）。** 设 \(V_0>0\)、\(c>0\)，\(\xi(t)=V_0(1-ct)\)。则

\[
q_\alpha(t)=\frac{V_0t^{-\alpha}}{\Gamma(1-\alpha)}
\left(1-\frac{ct}{1-\alpha}\right).
\tag{FQ4}
\]

因此(FQ1)在 \((0,T)\) 上成立，当且仅当 \(cT\le1-\alpha\)，等号允许。此时 \(\xi(T)\ge\alpha V_0>0\)，但 \(\xi'<0\)。

**证明。** 将常导数 \(-V_0c\) 与 \(g_{1-\alpha}\) 卷积，得到 \(-V_0c\,t^{1-\alpha}/\Gamma(2-\alpha)\)。加入初值项并使用 \(\Gamma(2-\alpha)=(1-\alpha)\Gamma(1-\alpha)\)，得到(FQ4)。括号非负恰等价于所述条件。∎

该例仅为解析说明，未作为新增金融实验，也未宣称已经构造可实现的rough-Heston方差曲线。曲线正性本身并不足以保证(FQ1)：\(1-\alpha<cT<1\) 时仍有 \(\xi>0\)，但期限末段的核为负。

**推论9.5（常曲线的显式传播）。** 在定理9.2的状态前提下，令 \(\xi\equiv V_0\ge0\)。则

\[
q_\alpha*k_\lambda=V_0E_\alpha(-\lambda t^\alpha),\qquad
|L_T-\widehat L_T|\le
\frac{V_0}{\nu}\int_0^T
E_\alpha(-\lambda(T-s)^\alpha)R(s)\,ds.
\tag{FQ5}
\]

若 \(R\le\nu\delta_F\)，显式上界为

\[
\eta_{\rm ML}=V_0\delta_F T E_{\alpha,2}(-\nu\sigma T^\alpha)
\le\min\left\{
V_0\delta_F T,
\frac{V_0\delta_F T^{1-\alpha}}{\nu\sigma\Gamma(2-\alpha)}
\right\}.
\tag{FQ6}
\]

**证明。** 对绝对局部可积的Mittag–Leffler级数逐项卷积，得 \(g_{1-\alpha}*k_\lambda=E_\alpha(-\lambda t^\alpha)\)；逐项积分得 \(\int_0^T E_\alpha(-\lambda t^\alpha)dt=T E_{\alpha,2}(-\lambda T^\alpha)\)。(FQ3)给出 \(0\le E_\alpha\le1\)，证明第一项比较。又有 \(\int_0^tk_\lambda=(1-E_\alpha(-\lambda t^\alpha))/\lambda\le1/\lambda\)，故状态界 \(|e|\le\delta_F/\sigma\) 经非负 \(q_\alpha\) 积分给出第二项比较。∎

显式上界保留有限历史与正确物理尺度。只有新旧界均约束相同D-type目标和参考时，才可合法取小值；代入式参考必须单独认证残差转换项。本推论是解析结论，不宣称已经数值实现Mittag–Leffler加权传播，也不将新模型实例列为已认证。

**命题9.6（同一快速输出下的非零遗漏参考）。** 固定实际快速输出，包括其在遗漏有限节点上的零贡献。在同一有限定价映射中，为这些节点选择可非零的参考 \(\psi_n\)，并证明 \(|\phi_n-\psi_n|\le\rho_n\)。令 \(\bar c'=c_0+\Re(A\psi)\)、\(d'=\bar c'-c^{\rm fast}\)，并使 \(\mathcal R\) 包含全部条带、真实无限尾及新参考算术。则

\[
c^*-c^{\rm fast}\in d'
+\{\Re(Az):|z_n|\le\rho_n\}\oplus\mathcal R.
\tag{FQ7}
\]

对称余项及方向 \(w\) 下，完整绝对预算采用

\[
DF\left(|w^\top d'|+
\sum_n\rho_n\left|\sum_iw_ia_{in}\right|
+h_{\mathcal R}(w)\right)\le\tau.
\tag{FQ8}
\]

非对称余项须同时界定正反方向支持。参考中心改变不改变固定快速输出，但改变 \(d'\)，并要求支付新的中心算术。

**证明。** 在精确定价有限映射中加减新参考，变换误差为 \(z=\phi-\psi\)；余项包含其他完整差异。共同复圆盘的方向支持给出(FQ8)。∎

旧零中心证书 \(|\phi_n|\le\varepsilon_n^0\) 与新中心 \(\psi_n\) 的证书不能直接对半径取小值。在新中心下，旧证书仅给出 \(|\phi_n-\psi_n|\le\varepsilon_n^0+|\psi_n|\)，故安全半径为 \(\min\{\rho_n,\varepsilon_n^0+|\psi_n|\}\)，或保留两个变换圆盘的交集。只有 \(|\psi_n|+\rho_n\le\varepsilon_n^0\) 才保证新圆盘包含于旧圆盘。否则两个独立有效的完整价格区间仍可交集，但不能自动声称同中心单调性。例如 \(\phi=0\) 同时属于 \(D(0,.1)\) 与 \(D(1,2)\)，却不属于 \(D(1,\min(.1,2))\)。边际与联合比较须使用相同更新中心、节点半径和完整余项，新增参考求值与认证均计入成本。
