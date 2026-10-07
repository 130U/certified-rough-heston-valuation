# 正分数阶定价核、常曲线传播与遗漏节点重居中

日期：2026-10-07。本文件是新的条件式理论证明与审查记录，不修改 `heston-nine-point-20261007` 的冻结稿件、场或证据。新增解析命题不自动生成新增数值证书。

## 1. 本轮命题与先行边界

本轮把有限历史传播的充分条件从“曲线递增”放宽为“曲线的 Riemann–Liouville 导数核非负”。递增曲线属于该类，但该类包含一定幅度的下降曲线。放宽只作用于指数传播，不证明随机方差过程存在、鞅性或额外参数域的真解正则性。

Caputo 凸性、正 Mittag–Leffler 逆算子、分数阶卷积半群和重居中的三角不等式均为先行工具。本文新增内容是它们在同一复 Riccati、D-type 指数、实际快速输出与完整 Fourier 账本之间的条件推导及核验接口。不能据有限检索声称这些一般数学工具首次被提出。

全文原论文已通过外部 PDF 核验具体定义和证明位置，非仅摘要：

- [Li–Liu, arXiv:1612.05103](https://arxiv.org/pdf/1612.05103)，33页；重点核对第20个 PDF 页面 Proposition 3.11(ii) 的凸性及其局部 L1 收敛前提、第30个 PDF 页面向量推广。下文 AC 假设通过 W1,1 逼近闭合该前提。
- [Kopteva, arXiv:2105.05848v2](https://arxiv.org/pdf/2105.05848v2)，8页；核对式(2.1)、Remark 2.1、Theorem 2.2、Lemma 2.8 和原点修正 Corollary 2.5。其残差比较与正逆算子不计作本文的新一般理论。
- [Franz–Kopteva, arXiv:2211.06272v2](https://arxiv.org/pdf/2211.06272v2)，29页；核对第2节正逆算子、第2.2节非线性线性化与 Corollary 2.12，并查看稳定残差与自适应算法章节。本轮不宣称可靠自适应残差比较的普遍原创。
- [El Euch–Rosenbaum, arXiv:1703.05049v1](https://arxiv.org/pdf/1703.05049v1)，37页；核对第4个 PDF 页面模型条件(4)–(5)、第11–12个 PDF 页面 Proposition 3.1 的分数阶曲线关系、第12个 PDF 页面 Corollary 3.3 与第14个 PDF 页面可实现曲线类。其方差过程参数约束和曲线关系不被本轮解析例取代。

这些是有界相关文献核验，不是排除全世界所有先行结果的优先权证明。作者 PDF 的 SIAM 链接本次返回内部错误；已改读 arXiv 全文核验 Proposition 3.11，版本与链接记录见 `theory-evidence-ledger.json`。

## 2. 全部假设与正确尺度

取有限期限 \(T>0\)、\(0<\alpha<1\)、\(\nu>0\)，并定义

\[
g_\beta(t)=t^{\beta-1}/\Gamma(\beta),\qquad
F(z)=-b+dz+z^2/2.
\tag{TQ1}
\]

假设 \(Z,\widehat Z\in AC([0,T];\mathbb C)\)，\(Z(0)=\widehat Z(0)=0\)，且几乎处处

\[
D_C^\alpha Z=\nu F(Z),\quad
r=D_C^\alpha\widehat Z-\nu F(\widehat Z),\quad
|r|\le R\in L^\infty(0,T),\quad R\ge0.
\tag{TQ2}
\]

其中 \(D_C^\alpha f=g_{1-\alpha}*f'\)，卷积仅取 \([0,t]\) 的完整历史。设 \(\Re d=-s_0\)、\(\Re Z\le0\)、\(\Re\widehat Z\le\epsilon_R\)，并且

\[
\sigma=s_0-\epsilon_R/2>0,\qquad \lambda=\nu\sigma.
\tag{TQ3}
\]

这些是对整个时间区间的前提，离散节点检查不能代替。条件式写出 \(0<\alpha<1\) 不额外证明既有结构区间之外的真解 AC 或左半平面性质。物理残差为 \(R\)，规范残差在物理时间中的表达为 \(R/\nu\)。以 \(x=\nu^{1/\alpha}t\) 换元，\(D_t^\alpha Z=\nu D_x^\alpha H\)，故物理耗散为 \(\nu\sigma\)；不能漏掉这个因子，也不能把 \(\nu t^\alpha\) 当普通 ODE 时间。

假设真实曲线 \(\xi\in AC([0,T];\mathbb R)\)、\(\xi(0)=V_0\ge0\)，不要求 \(\xi'\) 非负。定义

\[
A_\alpha=g_{1-\alpha}*\xi,
\qquad q_\alpha=A_\alpha'
=V_0g_{1-\alpha}+g_{1-\alpha}*\xi',
\qquad q_\alpha\ge0\quad\hbox{a.e.}
\tag{TQ4}
\]

最后一个符号条件是本轮放宽后的充分条件。不是宣称它对一切可能的认证方法都必要。若 \(q_\alpha\) 改变符号，绝对核界仍可用，但不能沿用正消去而漏掉绝对值。

## 3. 曲线核的绝对连续性、启动项与恢复恒等式

由 \(\xi=V_0+g_1*\xi'\)，

\[
A_\alpha=V_0g_{2-\alpha}+g_{2-\alpha}*\xi'.
\tag{TQ5}
\]

\(g_{2-\alpha}\) 在有限区间绝对连续且初值为零；其导数是可积的 \(g_{1-\alpha}\)。因此 \(A_\alpha\in AC[0,T]\)、\(A_\alpha(0)=0\)，且 TQ4 成立。Young 不等式明确给出

\[
\|q_\alpha\|_1\le
\frac{T^{1-\alpha}}{\Gamma(2-\alpha)}
\bigl(V_0+\|\xi'\|_1\bigr)<\infty.
\tag{TQ6}
\]

使用绝对 Fubini 与 \(g_\alpha*g_{1-\alpha}=g_1\)，包括可能为负的 \(\xi'\)，得到

\[
g_\alpha*q_\alpha
=V_0+g_1*\xi'=\xi.
\tag{TQ7}
\]

例如绝对三重卷积由 \(g_\alpha*g_{1-\alpha}*|\xi'|=g_1*|\xi'|\) 支配；不需要把有符号 \(\xi'\) 误称为正函数。TQ7 与 \(q_\alpha\ge0\) 进一步推出 \(\xi\ge0\)。AC 曲线的连续代表使这一非负性扩展到整个 ([0,T])。\(V_0g_{1-\alpha}\) 是必要的启动项，删除它会把 TQ7 错写为 \(\xi-V_0\)。

## 4. 复误差比较与定价消去的完整证明

令 \(e=Z-\widehat Z\)，则

\[
D_C^\alpha e=\nu\left[d+(Z+\widehat Z)/2\right]e-r.
\tag{TQ8}
\]

系数实部不超过 \(-\lambda\)。对凸光滑函数 \(\psi_\varepsilon(e)=\sqrt{|e|^2+\varepsilon^2}-\varepsilon\)，历史凸性给出

\[
D_C^\alpha\psi_\varepsilon(e)+\lambda\psi_\varepsilon(e)\le R.
\tag{TQ9}
\]

理由是 \(\nabla\psi_\varepsilon(e)\cdot D_C^\alpha e=\Re(\bar e D_C^\alpha e)/\sqrt{|e|^2+\varepsilon^2}\)，以及

\[
\frac{|e|^2}{\sqrt{|e|^2+\varepsilon^2}}\ge\psi_\varepsilon(e),
\qquad \frac{|e|}{\sqrt{|e|^2+\varepsilon^2}}\le1.
\]

凸性并非普通链式法则。光滑曲线的历史公式中，差

\[
\nabla\Phi(e(t))\cdot(e(t)-e(s))-
\bigl[\Phi(e(t))-\Phi(e(s))\bigr]\ge0
\]

是非负 Bregman 余项，初始项同样非负。对 AC 曲线作 \(W^{1,1}\) 光滑逼近；在有限区间 \(g_{1-\alpha}\in L^1\)，故 Caputo 导数在 \(L^1\) 中收敛。固定 \(\varepsilon>0\) 时 \(\nabla\psi_\varepsilon\) 在有界轨迹上 Lipschitz，复合函数导数也在 \(L^1\) 中收敛，从而 TQ9 几乎处处成立。分布措辞不削弱 AC 前提。

设

\[
k_\lambda(t)=t^{\alpha-1}E_{\alpha,\alpha}(-\lambda t^\alpha)\ge0.
\tag{TQ10}
\]

该局部可积核是 \(D_C^\alpha+\lambda\) 的零初值逆；其绝对局部可积卷积级数为 \(\sum_{m\ge0}(-\lambda)^m g_{(m+1)\alpha}\)。正性可由标准负轴谱表示证明。对零初值 AC 标量函数 (v)，\(v=k_\lambda*(D_C^\alpha v+\lambda v)\)，所以 TQ9 与正逆给出 \(\psi_\varepsilon(e)\le k_\lambda*R\)。令 \(\varepsilon\downarrow0\)，

\[
|e|\le k_\lambda*R.
\tag{TQ11}
\]

两个指数必须是同一 D-type 对象：

\[
L_T=\nu^{-1}\int_0^T\xi(T-t)D_C^\alpha Z(t)\,dt,
\quad\widehat L_T=\nu^{-1}\int_0^T\xi(T-t)D_C^\alpha\widehat Z(t)\,dt.
\tag{TQ12}
\]

绝对 Fubini 由

\[
\|\xi\|_\infty
\frac{T^{1-\alpha}}{\Gamma(2-\alpha)}\|e'\|_1<\infty
\]

支配。然后对 \(A_\alpha(T-t)e'(t)\) 积分分部；两个边界项因 \(e(0)=A_\alpha(0)=0\) 消失。因此

\[
L_T-\widehat L_T=\nu^{-1}(q_\alpha*e)(T).
\tag{TQ13}
\]

由 TQ4、TQ11，

\[
|L_T-\widehat L_T|\le\eta_\lambda(T)
:=\nu^{-1}(q_\alpha*k_\lambda*R)(T).
\tag{TQ14}
\]

正 resolvent 恒等式为 \(g_\alpha-k_\lambda=\lambda g_\alpha*k_\lambda\ge0\)。与非负 \(q_\alpha\) 卷积，结合 TQ7 得

\[
W_\lambda:=q_\alpha*k_\lambda
=\xi-\lambda\xi*k_\lambda,
\qquad 0\le W_\lambda\le\xi.
\tag{TQ15}
\]

全部绝对换序先由局部 L1 及有界 (R) 保证；对于最终非负卷积还可直接用 Tonelli。因此

\[
|L_T-\widehat L_T|\le\eta_\lambda(T)
\le\eta_0(T):=\nu^{-1}(\xi*R)(T).
\tag{TQ16}
\]

也有 \(W_\lambda=V_0E_\alpha(-\lambda t^\alpha)+E_\alpha(-\lambda\cdot^\alpha)*\xi'\)。放宽后第二项不保证非负，故不能逐项舍掉它；TQ15 的整体非负性来自 \(q_\alpha\ge0\)。这一点区分新的条件与旧的曲线递增充分条件。

若闭单元完整包络为 (R_j)，原正曲线质量权重仍合法，因为 TQ7 推出 \(\xi\ge0\)：

\[
|L_T-\widehat L_T|\le\nu^{-1}\sum_jR_j
\{J_0(T-t_j)-J_0(T-t_{j+1})\},
\qquad J_0(z)=\int_0^z\xi(s)\,ds.
\tag{TQ17}
\]

此式只分割同一个完整历史积分，不重启 Caputo 时间单元。一般权重非负；不能不经证明地称全部曲线具有严格正权重。

## 5. 严格下降仿射曲线的解析例

取 \(V_0>0\)、\(c>0\)，令 \(\xi(t)=V_0(1-ct)\)。直接积分给出

\[
q_\alpha(t)=\frac{V_0t^{-\alpha}}{\Gamma(1-\alpha)}
\left(1-\frac{ct}{1-\alpha}\right).
\tag{TQ18}
\]

因此在 \((0,T)\) 上 \(q_\alpha\ge0\) 几乎处处，当且仅当 \(cT\le1-\alpha\)。等号允许：核仅在终点成为零。该条件推出 \(\xi(T)\ge\alpha V_0>0\)，但 \(\xi'=-V_0c<0\)，故解析条件严格包含旧递增曲线条件。

这里没有构造随机方差过程、验证其漂移约束或鞅性。\(q_\alpha\ge0\) 是传播定理的条件，不单独等价于任何一般 rough-Heston forward curve 的模型可实现性。反例边界也明确：若 \(1-\alpha<cT<1\)，曲线仍严格为正，但 \(q_\alpha\) 在期限末段为负，正消去路线不再适用。此时安全的一般式为 \(\nu^{-1}(|q_\alpha|*k_\lambda*R)(T)\)，不能静默替换成 \(\nu^{-1}(\xi*R)(T)\)。

## 6. 常曲线的显式耗散传播

若 \(\xi\equiv V_0\ge0\)，则 \(q_\alpha=V_0g_{1-\alpha}\)。Mittag–Leffler 级数绝对局部可积并可逐项卷积，给出

\[
g_{1-\alpha}*k_\lambda=E_\alpha(-\lambda t^\alpha),
\quad W_\lambda(t)=V_0E_\alpha(-\lambda t^\alpha).
\tag{TQ19}
\]

于是任意完整物理包络满足

\[
|L_T-\widehat L_T|
\le\frac{V_0}{\nu}\int_0^TE_\alpha(-\lambda(T-s)^\alpha)R(s)\,ds.
\tag{TQ20}
\]

若 \(R\le\nu\delta_F\)，将 Mittag–Leffler 级数逐项积分即得

\[
\eta_{\rm ML}
=V_0\delta_F T E_{\alpha,2}(-\nu\sigma T^\alpha),
\qquad |L_T-\widehat L_T|\le\eta_{\rm ML}
\le V_0\delta_F T.
\tag{TQ21}
\]

右侧比较来自 TQ15 的 \(0\le E_\alpha\le1\)，不依赖浮点观察。另由 \(\int_0^tk_\lambda(s)ds=(1-E_\alpha(-\lambda t^\alpha))/\lambda\le1/\lambda\)，状态界 \( |e|\le\delta_F/\sigma\) 给出

\[
\eta_{\rm ML}\le
\frac{V_0\delta_F T^{1-\alpha}}
{\nu\sigma\Gamma(2-\alpha)}.
\tag{TQ22}
\]

因此新旧界可对同一 D-type 指数取小值。更一般曲线在 TQ4 下也有旧状态界对应的指数界 \(\delta_F A_\alpha(T)/(\nu\sigma)\)，因为 \(\int_0^Tq_\alpha=A_\alpha(T)\ge0\)。如果旧指数采用 substitution-type 参考 \(\int\xi F(\widehat Z)\)，必须额外认证与 TQ12 的残差转换 \(\nu^{-1}\int\xi r\)；不能直接取不约束同一对象的两个界之小值。参考中心存储、指数求值与 Fourier 算术半径同样需保留。解析式不是本轮新增模型的数值验收。

## 7. 遗漏节点的非零参考与同一快速输出

设实际快速输出 \(c^{\rm fast}\) 已固定，其中一组有限频率 \(O\) 的实际实现贡献为零。设完整价格的相同有限截断线性映射为 \(\Re(A\phi)\)，其条带、截断后的真实无限尾等由同一余集合 \(\mathcal R\) 包含。新参考可在 \(O\) 上选取固定复中心 \(\psi_n\ne0\)，但它不改变旧快速输出。将这些中心放入整个参考向量 \(\psi\)，须证明

\[
|\phi_n-\psi_n|\le\rho_n,
\qquad\bar c'=c_0+\Re(A\psi),\qquad
\Delta c'=\bar c'-c^{\rm fast}.
\tag{TQ23}
\]

于是直接从恒等式得到

\[
c^*-c^{\rm fast}\in
\Delta c'+\{\Re(Az):|z_n|\le\rho_n\}\oplus\mathcal R.
\tag{TQ24}
\]

机器实现须将新中心与系数的求值及加总误差纳入 \(\mathcal R\) 的有效新算术部分；“同一实际输出”不意味着“同一参考中心”。若 \(\mathcal R\) 对称，任务方向的完整预算为

\[
DF\left(|w^\top\Delta c'|+
\sum_n\rho_n\left|\sum_iw_ia_{in}\right|
+h_{\mathcal R}(w)\right)\le\tau.
\tag{TQ25}
\]

非对称余集合必须分别评价 \(w\) 和 \(-w\)，或用两方向支持的较大上界。中心本身可能改善或恶化预算，不可只报告新的圆盘半径。

特别地，旧遗漏节点证书为 \( |\phi_n|\le\varepsilon_n^0\)，新证书为 \( |\phi_n-\psi_n|\le\rho_n\)。两个不同中心的半径不能直接取小值。在新中心下，旧证书经三角不等式只提供 \(\varepsilon_n^0+|\psi_n|\)。故一个简单安全更新是

\[
\rho_n^{\rm safe}=\min\{\rho_n,\varepsilon_n^0+|\psi_n|\}.
\tag{TQ26}
\]

更紧的做法保留真实变换的圆盘交集 \(D(0,\varepsilon_n^0)\cap D(\psi_n,\rho_n)\)，其中同一个节点变量仍共享于全部执行价。一般不能声称新圆盘包含于旧圆盘；该圆盘包含恰需 \( |\psi_n|+\rho_n\le\varepsilon_n^0\)。即使它不成立，新证书和旧证书只要各自有效，两个完整实际输出价格区间的交集仍有效。参考改变后，应重新计算 \(\Delta c'\)、支持和算术，不能直接使用旧中心下的减量更新不变量。

例如真实值 \(\phi=0\) 同时满足旧盘 \(D(0,0.1)\) 和新盘 \(D(1,2)\)。错误地将新中心1的半径改成 \(\min(0.1,2)=0.1\) 会排除真实值0。这个反例中两份原证书各自有效，错误完全来自不同中心半径的直接取小值。新旧混合比较须对边际盒与共同集合使用同一新中心和同一节点集合。

## Status

PROVABLE AS STATED（TQ2–TQ4、D-type 参考和完整价格包含等显式前提成立时）。
Verification: Verified

此状态指局部条件式推导闭合，不代表新的残差生成、曲线模型存在或金融实例已通过数值验收。结构扫描不代替数学审查。

## Dependency Map

曲线放宽 depends on O1–O5；下降例 depends on O1 and O6；常曲线传播 depends on O2–O5 and O7；遗漏中心接口 depends on O8–O10。

## Obligation Ledger

- O1 曲线 AC、启动项、q 的 L1 与恢复恒等式 — CLOSED-LOCAL. Closed at: TQ4–TQ7，绝对卷积半群与明确 Young 界。
- O2 物理ν尺度、完整历史和复耗散 — CLOSED-LOCAL. Closed at: TQ2–TQ3、TQ8，不重新起步时间单元。
- O3 AC 凸性与正逆 — CLOSED-LOCAL. Closed at: TQ9–TQ11，W1,1/L1 逼近和正零初值 resolvent。
- O4 指数 Fubini、分部与零边界 — CLOSED-LOCAL. Closed at: TQ12–TQ14，绝对支配及 e(0)=A(0)=0。
- O5 放宽后正消去与非递增曲线权重 — CLOSED-LOCAL. Closed at: TQ7、TQ15–TQ17，q 非负推出ξ非负；不把ξ′误称非负。
- O6 下降仿射条件与可实现性边界 — CLOSED-LOCAL. Closed at: TQ18 及正曲线/負q反例；不证明随机模型存在。
- O7 常曲线ML传播与同对象取min — CLOSED-LOCAL. Closed at: TQ19–TQ22，绝对级数、积分和状态界。
- O8 相同快速输出的新参考中心与全余项 — CLOSED-LOCAL. Closed at: TQ23–TQ25，代数恒等式与双方向支持。
- O9 不同圆盘中心之间的合法转换 — CLOSED-LOCAL. Closed at: TQ26 及圆盘交集/包含条件；不直接取不同中心半径min。
- O10 先行工具、解析结论与数值结论的边界 — CLOSED-LOCAL. Closed at: 第1节原文定位与各节条件范围；新增数值需要单独完整证据。

## Verification Checks

核查曲线为实 AC、q 的启动项和L1；只假设q≥0而不暗用ξ′≥0；核查νσ与R/ν；保持完整Caputo历史；D-type指数必须一致；对含负ξ′的卷积先证绝对Fubini；常曲线ML只逐项使用绝对收敛；下降例不宣称方差模型可实现；新遗漏中心支付价差平移和全部算术；不同中心不能直接半径min；保留置零有限节点、条带、真实无限尾；边际和联合比较使用同一更新场景；失败预算不是实际误差下界；原文有限核验不是普遍优先权证明。
