# 完整分数阶历史下的残差—指数—组合认证

研究日期：2026-10-07。本文件给出本轮新增可迁移命题及完整推导；冻结的旧近似场、旧残差证书和旧输出均不是本文件的修改对象。所有数值结论仍需逐输入身份检查、向外舍入及独立重算。本文件不以评分或历史优先权代替验收。

## 1. 三条路线与本轮选择

| 路线 | 可证明的推进 | 执行依赖和风险 | 本轮选择 |
|---|---|---|---|
| A：正 resolvent 与定价正核的卷积消去 | 不先把状态误差压成全时间常数，而是直接把完整历史残差传给指数；再得到无需数值计算 resolvent 的上界 | 需要原场全时间残差、复误差耗散、正曲线核；必须保留启动边界项和物理时间的 ν | 主路线，下面完整证明；旧全时间最大残差也能立即使用 |
| B：变系数耗散或更细逐时残差 | 用更负的参考实部提高后期耗散，或为同一场保留每个闭时间单元的残差包络 | 变系数方程需要一个带完整历史的可靠比较求解器；不能把时间单元当独立 ODE。逐时包络本身则可以直接接入 A | 逐时接口完整给出；变系数耗散留作扩展，未承担本轮数值结论 |
| C：按最终任务方向选择认证动作 | 用组合后的 Fourier 系数衡量节点贡献，逐步替换为新有效半径；任一步都保持包含，预算达标即停止 | 贪心顺序不自动最优；取小值只能在同一参考对象下进行。若资源耗尽，应返回当前有效界或可能最优集合 | 给出单调有效性、有限动作的条件终止及耗尽规则 |

最直接的推进不是再优化近似场，而是改变已有完整连续残差向价格指数的传播方式。路线 A 连同 C 支撑 `finite-history.py` 的全时间最大残差分支；该程序本身不使用逐时间单元包络。另行生成的 `time-local-propagation.py` 已在固定 \(\alpha=13/25\)、\(T=1/2\) 的同一参考场上，读取全部513个节点、8189个闭时间单元的连续包络，并按事先固定的128个物理时间组实施完整逐时局部化。两种分支的输入、成本和数值结果分别记录，不能以全局分支的动作最优性代替逐时分支的结论。

## 2. 先行工具与新增命题边界

Caputo 的凸函数不等式是已有工具，适用依据为 [Li–Liu (2018), Proposition 3.11](https://ins.sjtu.edu.cn/people/leili/publications/Papers/liliu_SIMA2018.pdf)。正 Mittag–Leffler resolvent 和逐时残差比较同样已有：[Kopteva (2022), equation (2.1), Remark 2.1, Theorem 2.2](https://arxiv.org/pdf/2105.05848) 给出正逆算子及残差控制；这里不把该通用公式计为新结果。更高阶和可靠自适应实现的先行研究见 [Franz–Kopteva (2023)](https://arxiv.org/pdf/2211.06272)。

本轮具体增量是：对指定复 Riccati 误差，在正确 ν 尺度下，把该正逆算子与定价曲线的 Caputo 对偶核组合；证明完整有限历史的定价上界可由曲线—残差普通正卷积支配；用同一参考、同一实际快速输出、同一完整余项账本生成可单调替换的 Fourier 半径与任务方向预算。它是模型特定连接和认证算法接口，不能据此宣称正卷积、分数阶比较原理或一般自适应估计的历史原创性。

## 3. 模型、对象与物理时间尺度

取 \(0<\alpha<1\)、\(\nu>0\)、\(s_0>0\)、实频率 \(u\)，定义

\[
g_\beta(t)=t^{\beta-1}/\Gamma(\beta),\qquad
F(z)=-b+dz+z^2/2,\quad
b=(u^2+1/4)/2,\quad d=-s_0+i\rho u.
\tag{FH1}
\]

本节假定目标解和固定参考函数 \(Z,\widehat Z\in AC[0,T]\)，初值均为零，并且

\[
D_{C,t}^\alpha Z=\nu F(Z),\quad
r(t)=D_{C,t}^\alpha\widehat Z-\nu F(\widehat Z),\quad
|r(t)|\le R(t),
\tag{FH2}
\]

其中 \(R\ge0\) 为有界可测包络，所有不等式允许按几乎处处或对应分布意义理解；这不撤销前置的绝对连续假设。还假定

\[
\operatorname{Re}Z(t)\le0,\quad
\operatorname{Re}\widehat Z(t)\le\epsilon_R,\quad
\sigma=s_0-\epsilon_R/2>0.
\tag{FH3}
\]

这些是明确的依赖，不能只因一个场在离散节点上位于左半平面，就宣称 FH3 成立。本次原始点候选全时间证书具有 \(\epsilon_R=0\)。目标解全时间左半平面及绝对连续性由原稿相应引理提供；在原稿 \(\alpha>1/2\) 的设定下适用。写出 \(0<\alpha<1\) 的条件式命题并不额外证明更低阶解的此项正则性。

令 \(x=\nu^{1/\alpha}t\)、\(H(x)=Z(t)\)、\(\widehat H(x)=\widehat Z(t)\)。直接变量代换得

\[
D_{C,t}^\alpha Z(t)=\nu D_{C,x}^\alpha H(x),\qquad
\mathfrak r(x)=r(x/\nu^{1/\alpha})/\nu.
\tag{FH4}
\]

因此规范时间的耗散是 \(\sigma\)，物理时间的耗散是 \(\lambda=\nu\sigma\)。本文件始终令 \(R\) 表示物理残差，\(\varrho=R/\nu\) 表示规范残差在物理时间中的表达。物理原状态 \(h=Z/\nu\) 的误差也需除以 \(\nu\)。变量 \(y=x^\alpha=\nu t^\alpha\) 仅为代数参数，不把 \(D_C^\alpha\) 改写成关于 \(y\) 的普通导数。

## 4. 完整历史的复误差比较

**命题 FH-A（保留历史的耗散比较）。** 在 FH1–FH3 下，设

\[
k_\lambda(t)=t^{\alpha-1}E_{\alpha,\alpha}(-\lambda t^\alpha),
\qquad \lambda=\nu\sigma.
\tag{FH5}
\]

则 \(k_\lambda\ge0\)，且对每个 \(t\in[0,T]\)，

\[
|Z-\widehat Z|(t)\le(k_\lambda*R)(t),\qquad
|h-\widehat h|(t)\le(k_\lambda*\varrho)(t).
\tag{FH6}
\]

**证明。** 令 \(e=Z-\widehat Z\)，则

\[
D_C^\alpha e=\nu\left(d+\frac{Z+\widehat Z}{2}\right)e-r.
\tag{FH7}
\]

括号的实部不超过 \(-\sigma\)。用实平面上的凸函数
\(\psi_\varepsilon(e)=\sqrt{|e|^2+\varepsilon^2}-\varepsilon\) 正则化模长。Caputo 历史凸性给出

\[
D_C^\alpha\psi_\varepsilon(e)
\le\frac{\operatorname{Re}(\overline e D_C^\alpha e)}{\sqrt{|e|^2+\varepsilon^2}}
\le-\lambda\psi_\varepsilon(e)+R.
\tag{FH8}
\]

第二步使用 \(|e|^2/\sqrt{|e|^2+\varepsilon^2}\ge\psi_\varepsilon(e)\)，以及 \(|e|/\sqrt{|e|^2+\varepsilon^2}\le1\)。这是分数阶凸性不等式，不是普通链式法则。具体地，对任意凸光滑 \(\Phi\)，历史公式中的差
\(\nabla\Phi(e(t))\cdot(e(t)-e(s))-[\Phi(e(t))-\Phi(e(s))]\)
为非负 Bregman 余项，初始差项也非负。对一般 AC 函数可先作因果平滑并在 \(W^{1,1}\) 收敛；卷积 \(g_{1-\alpha}\) 在有限区间把导数的 \(L^1\) 收敛传给 Caputo 导数的 \(L^1\) 收敛。对每个固定 \(\varepsilon>0\)，\(\nabla\psi_\varepsilon\) 在有界轨迹上 Lipschitz，故凸性不等式可在 \(L^1\) 中取极限。这明确满足 Li–Liu 分布版本所需的收敛条件。

正核性质可从标准 Hankel 反演直接核对：对 \(\lambda>0\)，

\[
k_\lambda(t)=\frac{\sin(\pi\alpha)}{\pi}
\int_0^\infty e^{-rt}
\frac{r^\alpha}{r^{2\alpha}+2\lambda r^\alpha\cos(\pi\alpha)+\lambda^2}\,dr>0.
\tag{FH9}
\]

这里分母为 \(|r^\alpha e^{i\pi\alpha}+\lambda|^2\)；公式由 \((s^\alpha+\lambda)^{-1}\) 在负实轴上下侧的跳跃获得。主支上无极点，小圆贡献为零。也可使用 FH5 的绝对局部可积级数 \(\sum_{m\ge0}(-\lambda)^m g_{(m+1)\alpha}\) 核对其为 \(D_C^\alpha+\lambda\) 的零初值逆。\(\lambda=0\) 时即 \(k_0=g_\alpha\)。

对任意零初值绝对连续标量函数 \(v\)，有
\(v=k_\lambda*(D_C^\alpha v+\lambda v)\)。这可由上述局部绝对收敛的卷积级数或线性 Volterra 方程的唯一性证明。由于核非负，把 FH8 的右侧用 \(R\) 支配，得 \(\psi_\varepsilon(e)\le k_\lambda*R\)。令 \(\varepsilon\downarrow0\) 得第一式；第二式由 \(h=Z/\nu\) 得到。此论证只需几乎处处不等式及可积历史，不要求分段常数强迫的比较解在每个正时间分界点都局部 Lipschitz。∎

为核查两种时间尺度的一致性，令 \(c=\nu^{1/\alpha}\)，则
\(k_\sigma(c\tau)=c^{\alpha-1}k_{\nu\sigma}(\tau)\)。规范时间卷积换元后的因子是 \(c^\alpha=\nu\)，故恰得到 \(\nu k_{\nu\sigma}*\varrho=k_{\nu\sigma}*R\)，不存在丢失的 \(\nu\)。

## 5. 价格指数中的正卷积消去

假定曲线 \(\xi\in AC[0,T]\)，\(\xi(0)=V_0\ge0\)，\(\xi'\ge0\) 几乎处处。定义

\[
A_\alpha=g_{1-\alpha}*\xi,
\qquad q_\alpha=A_\alpha'
=V_0g_{1-\alpha}+g_{1-\alpha}*\xi'\ge0.
\tag{FH10}
\]

\(q_\alpha\in L^1[0,T]\)。在冻结曲线
\(\xi(t)=\theta+(V_0-\theta)E_{\alpha_0}(-\lambda_\xi t^{\alpha_0})\) 下，\(\xi'\) 在原点可能呈 \(t^{\alpha_0-1}\)，仍可积；此处没有要求启动项可有界求导。

定义目标及参考的 **D-type 指数**

\[
L_T=\nu^{-1}\int_0^T\xi(T-t)D_C^\alpha Z(t)\,dt,
\quad
\widehat L_T=\nu^{-1}\int_0^T\xi(T-t)D_C^\alpha\widehat Z(t)\,dt.
\tag{FH11}
\]

目标式因 FH2 等于原 \(\int\xi F(Z)\)。参考式则必须保持 FH11 的定义；若 \(\widehat Z=I^\alpha\bar G\)，它正是 \(\nu^{-1}\int\xi\bar G\)。

**命题 FH-B（有限历史直接指数界）。** 在以上条件下，

\[
L_T-\widehat L_T=\nu^{-1}(q_\alpha*e)(T),
\tag{FH12}
\]

\[
|L_T-\widehat L_T|
\le\eta_\lambda(T):=\nu^{-1}(q_\alpha*k_\lambda*R)(T)
\le\eta_0(T):=\nu^{-1}(\xi*R)(T)
=(\xi*\varrho)(T).
\tag{FH13}
\]

**证明。** 由 \(D_C^\alpha e=g_{1-\alpha}*e'\)，绝对 Fubini 和一次分部积分得到

\[
\int_0^T\xi(T-t)D_C^\alpha e(t)\,dt
=\int_0^T A_\alpha(T-t)e'(t)\,dt
=\int_0^T q_\alpha(T-t)e(t)\,dt.
\tag{FH14}
\]

边界项恰为零：\(e(0)=0\)、\(A_\alpha(0)=0\)。绝对 Fubini 可由 \(\|\xi\|_\infty T^{1-\alpha}\|e'\|_1/\Gamma(2-\alpha)<\infty\) 支配。再使用 FH6 和正核得 FH13 第一项。

关键消去完全发生在有限时间卷积上。由 Beta 函数的卷积半群关系 \(g_\alpha*g_{1-\alpha}=g_1=1\)，

\[
g_\alpha*q_\alpha
=V_0(g_\alpha*g_{1-\alpha})
+(g_\alpha*g_{1-\alpha})*\xi'
=V_0+\int_0^t\xi'(s)\,ds=\xi(t).
\tag{FH15}
\]

必须保留 \(V_0g_{1-\alpha}\)：若把它遗漏，则右侧错误地变成 \(\xi-V_0\)，给出不合法的小界。本证明无向负时间延拓、无消除原点的捷径。

resolvent 恒等式为

\[
g_\alpha-k_\lambda=\lambda g_\alpha*k_\lambda\ge0.
\tag{FH16}
\]

它可直接从 FH5 的卷积级数逐项消去核对。与 \(q_\alpha\) 卷积得

\[
W_\lambda:=q_\alpha*k_\lambda
=\xi-\lambda\xi*k_\lambda,\qquad 0\le W_\lambda\le\xi.
\tag{FH17}
\]

因此在 Tonelli 下 \(q_\alpha*k_\lambda*R\le\xi*R\)，完成 FH13。∎

较精确、但本轮程序尚未数值评价的核也可写作

\[
W_\lambda(t)=V_0E_\alpha(-\lambda t^\alpha)
+\int_0^tE_\alpha(-\lambda(t-s)^\alpha)\xi'(s)\,ds.
\tag{FH18}
\]

这再一次展示启动边界项，并允许将来可靠评价 \(\eta_\lambda\)。本轮使用 FH13 的 \(\eta_0\) 已无需评价 FH18。

**常数包络的立即可用推论。** 若已有物理残差 \(R\le\nu\delta_F\)，则

\[
|L_T-\widehat L_T|\le\delta_F J_0(T),
\qquad J_0(T):=\int_0^T\xi(s)\,ds.
\tag{FH19}
\]

这是本次 `finite-history.py` 实际使用的分支。它保留整个区间的有限历史，即使输入包络仍为全时间最大值。旧状态上确界给出 \(\eta_\infty=\delta_F A_\alpha(T)/(\nu\sigma)\)；只要原证明依赖成立，\(\min(\eta_0,\eta_\infty)\) 合法，因为两个标量界约束同一 \(|L_T-\widehat L_T|\)。不存在“用不耗散的新界替换模型”或把同一残差积分加两次。若参考使用 \(\int\xi F(\widehat Z)\)，与 D-type 指数之间还差 \(\nu^{-1}\int\xi r\)，必须另行认证；不能直接套用 FH19 后忽略此转换。

**有限历史界的非扩张扩展。** FH13 的粗界 \(\eta_0\) 实际只需
\(\operatorname{Re}(d+(Z+\widehat Z)/2)\le0\)，不需统一严格正的 \(\sigma\)。在相同 AC、零初值和正曲线条件下，FH8 去掉非正耗散项即得 \(D_C^\alpha\psi_\varepsilon(e)\le R\)，从而 \(|e|\le g_\alpha*R\)，再用 FH12 和 FH15 得到同一 \(\eta_0\)。此时没有可取的 \(\delta_F/\sigma\) 无限时间状态界，仍有合法的有限期限定价认证。该扩展是条件数学结论，不在本轮数值中引入新的模型参数点。

## 6. 逐时包络与可向外舍入的精确权重

设 \(0=t_0<\cdots<t_J=T\)，并以完整连续认证证明 \(|r(t)|\le R_j\) 对整个闭单元 \([t_j,t_{j+1}]\) 成立。单元可以重叠端点，但不得留时间空洞。定义

\[
M_j=\int_{t_j}^{t_{j+1}}\xi(T-s)\,ds
=J_0(T-t_j)-J_0(T-t_{j+1})\ge0.
\tag{FH20}
\]

由 FH13 直接得到

\[
\eta_0(T)\le\nu^{-1}\sum_{j=0}^{J-1}R_jM_j.
\tag{FH21}
\]

每个 \(R_j\) 必须是完整历史参考函数的 residual 上界；它不是在 \(t_j\) 重启 Caputo 导数得到的新 ODE residual。FH21 只把一个完整历史比较式的积分分割，没有重置初值或遗忘历史。若仅有节点样本，不可把它们连接成未经认证的包络。冻结曲线有 \(V_0>0\)，因而其正长度单元权重严格为正；一般条件命题只需非负性。

冻结曲线的积分权重有显式公式：

\[
J_0(z)=\theta z+(V_0-\theta)zE_{\alpha_0,2}(-\lambda_\xi z^{\alpha_0}),
\tag{FH22}
\]

\[
J_1(z):=\int_0^zs\xi(s)\,ds
=\theta z^2/2+(V_0-\theta)z^2
\{E_{\alpha_0,2}(-\lambda_\xi z^{\alpha_0})
-E_{\alpha_0,3}(-\lambda_\xi z^{\alpha_0})\}.
\tag{FH23}
\]

公式由绝对一致收敛的 Mittag–Leffler 级数逐项积分给出。两者均包含完整 \(V_0\) 项。对本次 \(0\le z\le1/2\)，\(w=\lambda_\xi z^{\alpha_0}<1\)。截断 \(E_{\alpha_0,\beta}(-w)\) 的前 \(N\) 项（\(\beta=2,3\)）后，因 \(\Gamma(\beta+n\alpha_0)\ge1\)，绝对余项不超过 \(w^N/(1-w)\)。有理输入、Gamma/幂的有理外区间及该显式余项足以对 FH22–FH23 向外舍入；不能以浮点近似的正性替代余项证明。

若可靠认证的是单元上的非负仿射主包络
\(R(t)\le R_j^L(t_{j+1}-t)/h_j+R_j^R(t-t_j)/h_j\)，令
\(A=T-t_{j+1},B=T-t_j,h_j=B-A\)，\(\Delta J_k=J_k(B)-J_k(A)\)，则两端权重为

\[
M_j^L=(\Delta J_1-A\Delta J_0)/h_j,\quad
M_j^R=(B\Delta J_0-\Delta J_1)/h_j,\quad
M_j^L,M_j^R\ge0,\quad M_j^L+M_j^R=M_j.
\tag{FH24}
\]

相应指数界为 \(\nu^{-1}\sum_j(R_j^LM_j^L+R_j^RM_j^R)\)。正性来自非负 hat 函数积分；因此把一个向外区间的下端与零取大是合法交集，不能把有疑问的上端修成正数而继续接受。对于新的细分证书，可先逐点与旧包络取小值；于是精确的加权误差界单调不增。机器端点可能因不同舍入方式略增，最后再与旧有效指数上界取小值即可保留单调性。

**固定粗分组仍为连续包络。** 若新源证书以闭单元 \(S_k\) 完整覆盖 \([0,T]\)，且在整个 \(S_k\) 上有物理残差上界 \(R_k\)，可预先选取较少闭时间组 \(B_j\) 并设置
\(R_j=\max\{R_k:S_k\cap B_j\ne\varnothing\}\)。对任意 \(t\in B_j\)，完整覆盖提供含 \(t\) 的某个 \(S_k\)，它必与 \(B_j\) 相交，故 \(|r(t)|\le R_k\le R_j\)。因此跨组源单元、端点相交、原点和终点均被包含；随后应用 FH21 合法。该分组可以较粗而牺牲紧度，但不能抽样某个子集或跳过跨组单元。本轮 128 个 dyadic 物理时间组采用的正是此规则。

## 7. 指数到特征函数与实际输出

设 \(\phi=e^{L_T}\)、\(\widehat\phi=e^{\widehat L_T}\)，并由同一概率模型的正 martingale 性知 \(|\phi|\le1\)。若 \(|L_T-\widehat L_T|\le\eta\)、\(|\widehat\phi|\le B_{\rm ref}\)，则从两个端点分别分解指数差得到

\[
|\phi-\widehat\phi|
\le\min\{1,B_{\rm ref}\}(e^\eta-1).
\tag{FH25}
\]

**证明。** 使用 \(e^{L}-e^{\widehat L}=e^{\widehat L}(e^{L-\widehat L}-1)\)，以及反向分解 \(e^L(1-e^{\widehat L-L})\)。两式中 \(|e^z-1|\le e^{|z|}-1\)，各自乘数不超过 \(B_{\rm ref}\) 和 1；取小值。∎

额外的真特征函数包络 \(B_{\rm true}\) 还给出独立界 \(B_{\rm true}+B_{\rm ref}\)。若 \(\operatorname{Re}L\le U_{\rm true}\)、\(\operatorname{Re}\widehat L\le U_{\rm ref}\)，沿连接线积分还可得 \(\eta e^{\max(U_{\rm true},U_{\rm ref})}\)，但本轮程序未使用此扩展。所有取小值必须约束同一对 \(\phi,\widehat\phi\)。如采用存储的中心而非精确 \(\widehat\phi\)，要支付中心指数及指数评价的额外算术半径；不得因 FH25 较小而删掉这些项。

本次参考金融价格仍是原连续固定场的参考和，它的全部有限加总算术区间也保留。因此 `finite-history.py` 从原 exponent 文件取得精确参考模长外界，收紧 FH25，并保持原 `stored_field_price` 区间与最终中心平移。旧节点半径与新节点半径取小值合法，不会把固定场证明转给实际 Padé 轨迹。

## 8. 从共同 Fourier 节点到完整组合

对同一模型、期限和网格的合约 \(i\)，以 \(a_{in}\) 表示真实定价线性系数；节点的同一复误差 \(z_n\) 满足 \(|z_n|\le\varepsilon_n\)。保留全部有限节点（含置零节点）及条带、真实无限离散尾、算术项的余集合 \(\mathcal R\)。则

\[
c^*-c^{\rm fast}\in d+\mathcal E,
\quad d=\bar c-c^{\rm fast},\quad
\mathcal E=\{\operatorname{Re}(Az):|z_n|\le\varepsilon_n\}\oplus\mathcal R.
\tag{FH26}
\]

对实持仓 \(w\)，完整支持为

\[
h_{d+\mathcal E}(w)=w^\top d+
\sum_n\varepsilon_n\left|\sum_iw_i a_{in}\right|+h_{\mathcal R}(w).
\tag{FH27}
\]

反方向用 \(-w\) 给出下端点。只有对称余项时才可写成 \(w^\top d\pm B_w\)。FH25 产生新半径 \(\varepsilon_n'\le\varepsilon_n\)，故同一参考中心下有 \(\mathcal E'\subseteq\mathcal E\)。被置零的有限节点、无限尾、条带和中心算术余项未被 FH19 重新认证，应原样保留或另有完整新证明。收益因此来自完整预算的合法收紧，不是从单一残差界推断实际交易损失下降。

## 9. 单调任务方向算法与有限终止

**命题 FH-C（认证动作不损害包含）。** 固定 \(d,\mathcal R,A\)。在每个动作后，只接受同一对象的有效半径，并设置 \(\varepsilon_n^{k+1}=\min(\varepsilon_n^k,\varepsilon_n^{\rm new})\)。则每一步的价格包含成立，\(\mathcal E_{k+1}\subseteq\mathcal E_k\)，每个支持方向的误差半径不增。

**证明。** 较小圆盘包含于较大圆盘，有限乘积及线性映射保持包含；再与同一余集合相加保持包含。支持函数对包含单调。∎

令 \(U_n\ge|\sum_iw_i a_{in}|\) 为固定有理外上界，\(R_w\) 为完整余项半径，初始存储半径满足
\(B_0\ge R_w+\sum_nU_n\varepsilon_n^0\)。定义非负舍入余量 \(g=B_0-R_w-\sum_nU_n\varepsilon_n^0\)。每次精确更新

\[
B_{k+1}=B_k-U_n(\varepsilon_n^k-\varepsilon_n^{k+1})
=g+R_w+\sum_nU_n\varepsilon_n^{k+1}.
\tag{FH28}
\]

所以保留了原初始区间加总与精确端点加总之间的舍入差，并未通过扣减使界失效。该式正是当前 `finite-history.py` 更新的合法不变量。

**停止与条件终止。** 对对称误差集合的单一组合，只有在严格有理比较证明
\(DF(|w^\top d|+B_k)\le\tau\) 时，才返回预算已认证；“≤”的预算包含边界本身合法。若初始界已通过，应以零动作停止。若存在 \(N\) 个确定的有效替换动作，执行全部后界通过预算，且选择规则最终访问全部未访问动作，则至多 \(N\) 次后认证；贪心当前贡献可以满足此有限访问规则。没有声称贪心动作数最优。

本次 \(\alpha=.52\) 的 82 个动作不是重新生成 82 个参考场或连续残差，而是对固定节点证书应用新传播界。所有 513 个候选动作的额外计算属于补充检查，应与首次预算停止的动作和成本分别报告。其他候选若旧界已经通过一指数点预算，其对应主任务为零动作。

若动作耗尽或资源耗尽而尚未通过，返回当前有效区间及“当前包络未认证此预算”。这不证明真实误差超过预算。不得删掉不利的案例，也不得把理论可能的进一步收紧作为已取得结果。

## 10. 有限候选决策的迁移与保留范围

同一候选的误差集合缩小后，真实目标的包含仍成立。对平方目标 \(f(r)=\tfrac12r^\top Wr\)，把共同报价集合 \(\mathcal M\) 纳入 \(\mathcal K=\mathcal E\oplus(-\mathcal M)\)，以参考残差 \(r=\bar c-m_0\) 为中心。任意有效 \(\beta\ge\sup_{e\in\mathcal K}\sqrt{e^\top We}\) 给出安全界

\[
\max\{0,f(r)-h_{\mathcal K}(-Wr)\}
\le J^*\le
f(r)+h_{\mathcal K}(Wr)+\beta^2/2.
\tag{FH29}
\]

证明仅用二次展开、非负二次项和支持函数。上界不是把凸二次函数的最大化当成凸优化。节点缩小后可重新计算这些有效目标界；对舍入不同的新旧界再次取合法交集。若 \(U_k<\min_{j\ne k}L_j\)，返回唯一已认证赢家。否则保留所有 \(L_j\le\min_kU_k\) 的候选；资源耗尽不能据快速点目标宣布赢家。真实最优候选必在此集合内，因为其下界不超过真实目标，而任一其他候选上界不小于该候选真实目标。

本命题只覆盖给定有限候选，不声称连续参数识别、参数 refit、连续 \(\alpha\) 最优点或报价适配已经完成。新条件式传播定理可用于其他合法模型参数和期限，但每个实际例子均需满足全部前提并有其完整误差账本；它不扩大原 Padé 结构域，也不替经典分支完成全年金额证书。

## 11. 核心义务与验收位置

| 义务 | 本文件闭合的推导 | 数值使用必须检查 |
|---|---|---|
| 正则性、零初值、正确 Caputo 对象 | FH2–FH8、FH14；分布/几乎处处比较兼容分段包络 | 原真解引理、固定参考完整定义、系数与初值 |
| 复 Riccati 耗散 | FH7–FH8 | 全时间参考实部证书；只检查节点不够 |
| 原点曲线边界 | FH10、FH15、FH18 | 保留 V0，不得只用曲线导数 |
| 全历史与 ν | FH4–FH6、FH12–FH21 | 物理 residual 除以 ν；不重置 cell |
| 曲线质量的精确积分 | FH22–FH24 与显式级数余项 | 冻结曲线身份、Gamma/幂和负系数向外区间 |
| 指数及 CF 半径 | FH25、同对象 min | 精确参考模长、指数评价及存储中心算术 |
| 完整组合 | FH26–FH28 | 同一实际输出中心、置零节点及全部余项 |
| 成功、失败和耗尽 | FH28–FH29 后的停止规则 | 有理端点比较、全部动作/前缀/成本账本 |

FH-A、FH-B、FH-C 及其条件式传播链已在本文件证明。全局分支调用 FH19、FH25 和 FH28；逐时分支调用 FH20–FH21、闭单元粗分组引理及相同的指数—完整组合接口。`time-envelope-verification.json` 已精确核对513节点全部旧残差、启动及半平面端点和8189个闭单元的完整覆盖；`independent-time-local.json` 已独立重算128权重、所有相交闭单元最大包络、全部513指数/CF半径和1025节点完整终点。逐时完整上界向上显示为0.367258782指数点；1点和0.5点预算通过，0.25点仍未认证。这只完成该参数和期限的逐时分支，不承担变系数耗散、其他候选的逐时新生成或额外期限的数值结论。

成本必须分开陈述：`time-local-results.json` 记录读取既有完整包络、身份检查、权重、全部513节点传播与完整预算加总共1.479秒；新连续残差发生器报告997.266秒的循环阶段。该发生器计时在启动和设置之后开始，故后者不是从零生成或端到端研究成本，也不与旧全局分支的82单位动作混为同一种效率指标。

## Status

PROVABLE AS STATED（FH2–FH3、正曲线和各项数值外包明示成立时的条件命题）。
Verification: Verified

本地分析义务闭合；“Verified”描述本条件推导，不把缺少或尚未读回的数值输入变成已经重算的证据。先行工具已直接读取原论文核验，并在第2节准确引用。

## Dependency Map

FH-A depends on O1–O3; FH-B depends on O4–O6; FH-C depends on O7–O9; FH29 depends on O10.

## Obligation Ledger

- O1 正确对象、物理尺度和零初值 — CLOSED-LOCAL. Closed at: FH1–FH4 的定义及 Caputo 变量代换。
- O2 复模长正则化及全历史比较 — CLOSED-LOCAL. Closed at: FH7–FH8；ψ正则化保留零初值，耗散符号正确。
- O3 正 resolvent 及逆算子 — CLOSED-LOCAL. Closed at: FH5–FH9；标准正核谱表示、卷积级数和零初值逆。
- O4 价格指数 Fubini、边界和 integrability — CLOSED-LOCAL. Closed at: FH10–FH14；q可积、AC历史、A(0)=e(0)=0。
- O5 消去中的曲线启动项及全历史 — CLOSED-LOCAL. Closed at: FH15–FH18；V0项完整，resolvent差非负，无时间单元重置。
- O6 全局和逐时积分权重的精确公式 — CLOSED-LOCAL. Closed at: FH19–FH24；Gamma卷积、曲线原函数、显式级数尾和正hat权重。
- O7 同一 reference 的 CF 取小值及算术 — CLOSED-LOCAL. Closed at: FH25；双端点指数差和明确算术条件。
- O8 同一 actual output 的完整组合包含 — CLOSED-LOCAL. Closed at: FH26–FH27；所有置零节点、条带、无限尾和中心平移保留。
- O9 单调替换、精确舍入余量及条件终止 — CLOSED-LOCAL. Closed at: FH28 及第9节；g非负不变量，公平有限动作和初始零动作，未成功返回当前合法界。
- O10 目标界、报价误差符号及耗尽候选 — CLOSED-LOCAL. Closed at: FH29 及第10节；二次展开、支撑上界、安全范数半径、保留可能最优集合。

## Verification Checks

检查物理R与R/ν、λ=νσ和规范σ；保留V0 g_(1−α)；使用同一固定场的D-type exponent；检查全时间而非仅样本的实部和residual；所有positive convolution经Tonelli且有限；旧界与新界同对象后取min；参数点证书不外推结构域；片段包络不能重启Caputo；所有有限节点和余项保留；系数、中心和实际输出不变；凸二次最大化不作为凸优化；预算通过用完整有理端点，资源耗尽返回有效区间或可能最优集合；本地推导闭合与数值验收分开。
