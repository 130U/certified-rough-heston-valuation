# Rough Heston 模型的可验证联合定价误差

## 摘要

本文认证指定粗糙 Heston 定价实现的实际输出误差，并保留多个执行价共同使用的 Fourier 扰动。有限历史传播定理把连续包围的复 Riccati 残差连接至导数形式的定价指数，完整保留 Caputo 历史、曲线初值项与物理时间尺度。共同变换圆盘、解析条带求积、真实频率尾界及向外算术共同构成包含“模型价格减实际输出”的联合集合，显式保留有符号参考中心差。生产端有理构造与独立参考认证沿两条不同证明链展开。十二执行价实验中，在输出和残差包络均不变时，有限历史传播将价差完整界从1.397613点降至0.378599点。季度期限的匹配比较取得联合0.233318843点、边际0.252393939点，只有联合方法通过0.25点预算。省略频率认证及重新定中心的收益分别归因。预先固定的邻近参数认证和直接参考价、中心修正输出对照检验适用性；确定性工作量区分输出、认证、验证与组合复用。失败与未解决结果全部保留。保证针对指定数学模型及实现，不表示市场拟合或实际交易损失。

**关键词：** 粗糙 Heston；连续残差；有限历史；实际输出；联合价格误差；确定性认证。

## 1. 研究问题与贡献

完整、可核验的数值输出误差界，能否保留足够的共同结构，从而改变金融任务的认证决定？同一参数、期限下，每个执行价使用同一组 Fourier 变换值。逐价独立扩张区间，会丢失“每个频率的扰动是同一个复数”这一约束。本文从共同变量构造价格误差集合，不从经验协方差推断确定性误差方向。

研究对象明确如下。令模型价格为 \(c^*\)，存储的生产输出为 \(c^{\rm fast}\)，独立参考中心为 \(\bar c\)。完整包含写成

\[
c^*-c^{\rm fast}=d+\operatorname{Re}(A\delta)+r,
\qquad d=\bar c-c^{\rm fast}.
\tag{1.1}
\]

每个 \(\delta\) 分量是严格包围的共同 Fourier 误差；\(r\) 保留求积、省略有限节点、无限尾和算术误差。参考精化必须同步更新 \(d\) 及其认证不确定性。参考价和快速输出均不等同于精确模型价格。

### 1.1. 三条贡献及其依赖

首要分析贡献，是通过有限历史核把耗散复 Riccati 残差传至 Heston 定价指数。定理3.3提前给出，显式保留曲线初值项与物理因子 \(\nu^{-1}\)。Caputo 凸性和正预解核提供既有比较机制；这里发展的贡献是模型特定的定价泛函连接、可认证历史权重及完整输出预算。

第二条贡献是完整实现层金融认证。共同变换圆盘平移到实际输出，在组合及有限目标方向上求界。季度匹配实验隔离了共同结构改变认证决定的效果。统一消融分别解释传播、逐时包络、省略频率认证与重新定中心。支持函数、凸性以及已知单位成本菜单的排序均作为既有工具，不分别列为原创贡献。

第三条贡献是指定 Gatheral–Radoičić 有理构造的可检查结构域，以及独立生成的参考证书。全频率结论明确限制相关系数、分数阶阶数和均值回复。数值参考的残差证书不由代数符号证明代替。邻近参数合同与输出对照进一步检验可迁移性及适当工作负载。

| 证明支线 | 输入和结论 | 在价格证书中的作用 |
|---|---|---|
| 有理构造 | 两端匹配、原始行列式及分子符号；Padé 输出可定义与左半平面结构 | 检查指定域内的生产公式 |
| 独立参考 | 固定场、完整连续残差、耗散、有限历史指数及完整 Fourier 误差 | 认证参考变换与模型价格包含 |
| 输出平移 | 存储的快速值和独立包围的参考中心 | 将参考包含转为实际输出误差 |

两条证明支线共享数学模型。Padé 符号证书本身不认证价格误差；独立残差路径也不要求 Padé 轨迹充当参考场。

### 1.2. 相关研究与证据形式的区别

Gatheral–Radoičić [GR2019, GR2023v1] 提出两端有理近似，Jeng–Kiliçman [JK2020, JK2021] 分析全局 Padé 与公开 SPX 数据。本文使用其公式及匹配方法，结构结论针对明确认证域内的原始匹配系统。

Abi Jaber–El Euch [AbiJaberElEuch2018v1] 提供 Volterra 模型与仿射变换；Li–Liu [LiLiu2018] 通过正则化建立 Caputo 凸性；Kopteva [Kopteva2021v2] 以正分数阶逆传播逐时残差；Simon [SimonCM2015] 支撑 Mittag–Leffler 正性，Trefethen–Weideman [TrefethenWeideman2014] 提供条带梯形规则。本文写清所需正则性桥接并注明归属。

Ben Hammouda 等 [BenHammouda2026v1，第3.2节] 研究 rough Heston 多层求积与误差控制。其实用容差程序用数值指标替代未知常数，并以数值评估检查容差，而非后验严格认证。该算法目标与本文包含尾部和算术的存储输出确定性包围不同。此区别限定于所引版本及程序，不能扩张为其他方法均无严谨分析的结论。

Boyarchenko–de Innocentis–Levendorskii [BL2025v1] 直接讨论可靠定价、数值偏差及错误校准，其 modified Adams 是相关数值对照；原文将 Conformal Bootstrap 称为 ad-hoc 原理，本文不将其视为确定性区间保证。Hager–Kreher [HK2026v1] 研究 Hurst 参数的解析展开和局部收敛，近似对象不同。Bayer–Breneis [BBWeak2023v1, BBSimulation2023v1] 控制 Markovian 核近似并研究低维模拟，因此比较必须明确模型、输出和保证类型。

这份有边界的文献对照支持上述具体贡献，不证明相对全部未发表或同期方法的优先权。经典 Heston 原链研究保留为独立扩展；其概率对象不同，尚无完整年度货币价格证书，不列入本粗糙 Heston 主文贡献。


## 2. 模型、价格与实际输出

本文的分数阶积分及 Caputo 导数约定为
\[
I^\alpha f(t)=\frac1{\Gamma(\alpha)}\int_0^t(t-s)^{\alpha-1}f(s)\,ds,
\qquad D_C^\alpha v=I^{1-\alpha}v',\quad v\in AC.
\tag{2.1}
\]
在下文所用场的正则性下，\(I^\alpha f\in AC\) 且初值为零，故 \(D_C^\alpha I^\alpha f=f\)。Caputo 算子及其缩放均保留分数阶定义。令 \(a=u-i/2\)，物理 Riccati 状态 \(h\) 满足
\[
D_{C,t}^\alpha h=-\frac{a^2+ia}{2}
 +(i\rho\nu a-\lambda_R)h+\frac{\nu^2}{2}h^2,\qquad h(0)=0.
\tag{2.2}
\]
定义
\[
x=\nu^{1/\alpha}t,\quad y=x^\alpha=\nu t^\alpha,\quad
H(x)=\nu h(t),\quad Z(t)=H(\nu^{1/\alpha}t),\quad
\kappa=\lambda_R/\nu,
\tag{2.3}
\]
\[
b=(u^2+1/4)/2,\quad s_0=\kappa-\rho/2,\quad d=-s_0+i\rho u,\quad
F(z)=-b+dz+z^2/2.
\]
则 \(D_{C,x}^\alpha H=F(H)\)，\(D_{C,t}^\alpha Z=\nu F(Z)\)。归一化状态误差除以 \(\nu\) 才是物理 \(h\) 误差；物理残差 \(r_t=D_t^\alpha\widehat Z-\nu F(\widehat Z)\) 除以 \(\nu\) 才是规范方程的残差预算。

定价与实验部分固定 \(\kappa=0\) 及整条远期方差曲线
\[
\xi_*(t)=\theta+(V_0-\theta)E_{\alpha_0}(-\lambda_\xi t^{\alpha_0}),
\quad
(\alpha_0,V_0,\theta,\lambda_\xi)=(.5286,.0262,.0721,.5037).
\tag{2.4}
\]
曲线参数 \(\lambda_\xi\) 与 Riccati 参数 \(\lambda_R\) 分别定义。候选 \(\alpha\) 变化时 (2.4) 不随之重算。概率模型为
\[
V_t=\xi_*(t)+\nu\int_0^tK_\alpha(t-s)\sqrt{V_s}\,dW_s,\quad
K_\alpha(t)=t^{\alpha-1}/\Gamma(\alpha),\qquad
dS_t=S_t\sqrt{V_t}\,dB_t,\quad d\langle B,W\rangle_t=\rho\,dt.
\tag{2.5}
\]
式(2.5)为零Riccati均值回复下的远期方差表示。附录A依据Abi Jaber–El Euch的定理2.1、2.3及例2.2，验证该曲线所对应的概率模型与仿射变换。

以 \(M_T=S_T/F_T\) 为归一化正鞅，\(\phi_T(a)=\mathbb E M_T^{ia}\)，精确特征指数为
\[
L_T(u)=\int_0^T\xi_*(T-t)F(Z(t,u))\,dt,\quad
\phi_T(u-i/2)=e^{L_T(u)}.
\tag{2.6}
\]
记 \(m=K/F_T,k=\log m,c=C/(DF_T)\)，模型欧式看涨价格为
\[
c=1-\frac{\sqrt m}{\pi}\int_0^\infty
\operatorname{Re}\frac{e^{-iuk}\phi_T(u-i/2)}{u^2+1/4}\,du.
\tag{2.7}
\]
下文的价格由所列模型、输入十进制数和归一化约定共同确定。

## 3. 残差到定价指数的有限历史传播

### 3.1. 正则性与复值耗散

若 \(H=I^\alpha F(H)\) 为有界局部连续解，则 \(H,F(H)\) 为 \(\alpha\)-Hölder。对 \(\alpha>1/2\)，写 \(q=F(H)\)，抵消后的导数公式为
\[
H'(x)=\frac{q(x)x^{\alpha-1}}{\Gamma(\alpha)}
 +\frac{\alpha-1}{\Gamma(\alpha)}
\int_0^x(x-t)^{\alpha-2}[q(t)-q(x)]\,dt.
\tag{3.1}
\]
以下显式估计在初值附近可积：

\[
|H'(x)|\le\frac{\|q\|_\infty x^{\alpha-1}}{\Gamma(\alpha)}+\frac{(1-\alpha)[q]_{C^\alpha}x^{2\alpha-1}}{\Gamma(\alpha)(2\alpha-1)}.
\tag{3.2}
\]

正时间连续性及截断区间极限给出闭区间的绝对连续性；近端指数 \(2\alpha-2>-1\)，远端及第一项可积，故 \(H\in AC\)，正时间局部 \(C^1\)。局部解由有界球上的 Volterra 收缩得到。对 \(v\in AC\) 且正时间局部 Lipschitz，积分分部给
\[
D_C^\alpha v(x)=\frac1{\Gamma(1-\alpha)}
\left\{\frac{v(x)-v(0)}{x^\alpha}
 +\alpha\int_0^x\frac{v(x)-v(t)}{(x-t)^{1+\alpha}}\,dt\right\}.
\tag{3.3}
\]
在全历史正最大值处、零初值时，该导数严格正。由此可证 \(D_C^\alpha v+s v\le D_C^\alpha w+s w\)、\(v(0)=w(0)\)、\(s\ge0\) 蕴含 \(v\le w\)。对于实二维 \(C^1\) 凸函数 \(\Phi\)，将切线不等式分别代入 (3.3) 的两项给
\[
D_C^\alpha\Phi(v)\le\nabla\Phi(v)\cdot D_C^\alpha v.
\tag{3.4}
\]
这是已有 Caputo 历史凸性，而非普通链式法则；使用 Li–Liu [LiLiu2018] 的 Proposition 3.11 的正则性范围，并在此直接重证所需版本。

**引理 3.1。** 设 \(\alpha\in(1/2,1),|\rho|\le1,s_0\ge0\)。规范方程有唯一全局解，\(\operatorname{Re}H(x)<0\) 对 \(x>0\) 成立。若 \(s_0>0\)，
\[
|H(x)|\le\frac b{s_0}[1-E_\alpha(-s_0x^\alpha)]
\le\min\{b/s_0,bx^\alpha/\Gamma(1+\alpha)\}.
\tag{3.5}
\]
\(s_0=0\) 时保留后一时间上界。

**证明。** 写 \(H=X+iY\)，完全平方给
\[
\operatorname{Re}F(H)
=-\frac18-\frac{1-\rho^2}{2}u^2
-\frac12(Y+\rho u)^2-s_0X+\frac12X^2.
\tag{3.6}
\]
若 \(X\) 首次达到小正数 \(\varepsilon<1/2\)，(3.3) 导数为正，(3.6) 却负，矛盾。故 \(X\le0\)。正时间达到零时同样矛盾，因此严格负。

令 \(\psi_\epsilon(z)=\sqrt{|z|^2+\epsilon^2}-\epsilon\)。由 (3.4) 及
\[
\operatorname{Re}(\overline H F(H))
=-bX-s_0|H|^2+\tfrac12X|H|^2,\quad
\frac{|H|^2}{\sqrt{|H|^2+\epsilon^2}}\ge\psi_\epsilon(H),
\]
得 \(D_C^\alpha\psi_\epsilon(H)+s_0\psi_\epsilon(H)\le b\)。与零初值线性标量方程比较，令 \(\epsilon\downarrow0\)，得 (3.5)；标量解由 Mittag–Leffler 级数直接验证。若有限时爆炸，(3.5) 给有界轨迹、\(F(H)\) 有界和一致 Hölder 常数；历史积分在该端点有有限极限，保留既有历史作为强迫项的局部收缩可延拓，矛盾；不重新启动 Caputo 历史。唯一性由逐段 Volterra 收缩给出。证毕。

**定理 3.2（耗散残差界）。** 设 \(s_0>0\)，\(\widehat H(0)=0\)，\(\widehat H\in AC\) 且正时间局部 Lipschitz。若在全部 \(x\in(0,X]\) 上
\[
\operatorname{Re}\widehat H\le\epsilon_R<2s_0,\qquad
|D_C^\alpha\widehat H-F(\widehat H)|\le\delta,
\]
令 \(\sigma=s_0-\epsilon_R/2>0\)，则
\[
|H-\widehat H|
\le\frac\delta\sigma[1-E_\alpha(-\sigma x^\alpha)]
\le\delta/\sigma.
\tag{3.7}
\]
特别地，左半平面轨迹可取 \(\epsilon_R=0,\sigma=s_0\)，不要求 \(\delta\) 小或 \(u\) 小。

**证明。** \(e=H-\widehat H\) 满足
\[
D_C^\alpha e=\left(d+\frac{H+\widehat H}{2}\right)e-r,\quad e(0)=0,\quad
\operatorname{Re}\left(d+\frac{H+\widehat H}{2}\right)\le-\sigma.
\]
对 \(\psi_\epsilon(e)\) 用 (3.4)，得
\(D_C^\alpha\psi_\epsilon(e)+\sigma\psi_\epsilon(e)\le|r|\le\delta\)。
与线性标量解比较并令 \(\epsilon\downarrow0\) 即得。凸正则化适用于零误差，并对复二维误差成立。证毕。

如果 \(\widehat H\) 是物理时间轨迹 \(\widehat Z\)，认证 \(|r_t|/\nu\le\delta_F\)，同一结论为
\[
\sup_{t\le T}|Z-\widehat Z|\le\delta_F/s_0
\quad\text{if }\operatorname{Re}\widehat Z\le0.
\tag{3.8}
\]
本实验 \(s_0=1489/4000\)。该耗散率控制复值误差模长；独立残差 \(\delta_F\) 由第4.1节提供。这里使用已有凸性工具，建立本题的具体误差传递。



### 3.2. 比较论证的正则性桥梁

标量分数阶比较属于已有工具。Li–Liu [LiLiu2018, Proposition 3.11(ii)] 处理正则化后的凸性及分布极限，其 Proposition 4.12 则讨论指定的向量梯度流与 Hamiltonian 流。Kopteva [Kopteva2021v2, Lemma 2.8、Theorem 2.2] 在正时间 Lipschitz 假设下用范数凸性和正分数阶逆传播逐时残差。以下直接证明本文实际使用的向量 \(AC\) 版本，包括期限终点结论。这是已有工具的适配，不作为新的一般 Caputo 比较定理。

**正则性引理（AC 凸性与连续终点）。** 设 \(0<\alpha<1\)、\(T>0\)、\(v\in AC([0,T];\mathbb R^d)\)，且 \(\Phi\in C^1(\mathbb R^d)\) 凸。则

\[
D_C^\alpha\Phi(v)\le\nabla\Phi(v)\cdot D_C^\alpha v
\quad\text{a.e. on }(0,T).
\tag{3.9}
\]

若 \(u\in AC[0,T]\)、\(u(0)=0\)、\(\lambda\ge0\)、\(0\le R\in L^\infty(0,T)\)，且 \(D_C^\alpha u+\lambda u\le R\) 几乎处处，则

\[
u(t)\le(k_\lambda*R)(t),\quad0\le t\le T,
\qquad k_\lambda(t)=t^{\alpha-1}E_{\alpha,\alpha}(-\lambda t^\alpha).
\tag{3.10}
\]

**证明。** 取光滑 \(f_n\to v'\) 于 \(L^1(0,T)\)，定义 \(v_n(t)=v(0)+\int_0^t f_n(s)ds\)。这样初值完全保留，\(v_n\to v\) 一致，且 \(v_n'\to v'\) 于 \(L^1\)。光滑路径的历史分部积分给出 (3.9) 两侧之差

\[
\frac1{\Gamma(1-\alpha)}\left[
\frac{B_\Phi(v_n(0),v_n(t))}{t^\alpha}
+\alpha\int_0^t\frac{B_\Phi(v_n(s),v_n(t))}{(t-s)^{1+\alpha}}ds\right]\ge0,
\tag{3.11}
\]

其中 \(B_\Phi(a,b)=\Phi(a)-\Phi(b)-\nabla\Phi(b)\cdot(a-b)\ge0\)。梯度在紧路径范围上的界 \(M\) 与光滑路径的局部 Lipschitz 常数 \(L\) 给出 \(B_\Phi(v_n(s),v_n(t))\le2ML|t-s|\)，所以端点核 \((t-s)^{-\alpha}\) 可积。

所有路径落在同一紧集。普通的一阶 \(AC\) 复合规则给出 \(\Phi(v_n)'\to\Phi(v)'\) 于 \(L^1\)，而 Young 不等式给出

\[
\|D_C^\alpha(v_n-v)\|_1
\le\frac{T^{1-\alpha}}{\Gamma(2-\alpha)}\|v_n'-v'\|_1\to0.
\tag{3.12}
\]

同一估计适用于 \(\Phi(v_n)-\Phi(v)\)。梯度的一致收敛还保证右侧乘积在 \(L^1\) 中收敛。取几乎处处收敛的子列，即得 (3.9)。这里仅对普通一阶导数使用复合规则，没有使用 Caputo 链式法则。

设 \(f=D_C^\alpha u+\lambda u\in L^1\)。零初值给出 \(u+\lambda g_\alpha*u=g_\alpha*f\)。预解级数的第 \(n\) 项 \(L^1\) 范数不超过 \(\lambda^{n-1}T^{n\alpha}/\Gamma(1+n\alpha)\)，故局部收敛并给出 \(u=k_\lambda*f\) 几乎处处。\(E_{\alpha,\alpha}(-x)\) 的完全单调性 [SimonCM2015] 给出 \(k_\lambda\ge0\)，所以 \(f\le R\) 蕴含 \(u\le k_\lambda*R\)。将核和 \(R\) 零延拓后，核的 \(L^1\) 平移连续性及 \(R\) 的 \(L^\infty\) 界证明右侧连续，且在零点为零。左侧也连续，故不等式推广到 \([0,T]\) 每一点，包括终点。∎

### 3.3. 核心有限历史定价定理

模型特定的连接，是将复 Riccati 的耗散误差与导数型 Heston 定价泛函复合。完整历史始终从初始时刻计入；满足下列假设的固定参考轨迹均可使用这一结果，生产端 Padé 输出怎样计算由另一条证明链处理。

**定理 3.3（有限历史定价包络）。** 设 \(0<\alpha<1\)、\(\nu,T>0\)，且 \(Z,\widehat Z\in AC([0,T];\mathbb C)\) 具有相同零初值。设

\[
D_C^\alpha Z=\nu F(Z),\quad
r=D_C^\alpha\widehat Z-\nu F(\widehat Z),\quad
|r|\le R\in L^\infty(0,T),\quad R\ge0,
\tag{3.13}
\]

其中 \(F(z)=-b+dz+z^2/2\)、\(\Re d=-s_0\)、\(\Re Z\le0\)、\(\Re\widehat Z\le\epsilon_R\)、\(\sigma=s_0-\epsilon_R/2>0\)。微分关系和残差界几乎处处成立，状态实部界由连续性逐点成立。设 \(\xi\in AC[0,T]\)、\(\xi(0)=V_0\ge0\)，并要求

\[
q_\alpha=(I^{1-\alpha}\xi)'
=V_0g_{1-\alpha}+g_{1-\alpha}*\xi'\ge0\quad\text{a.e.}.
\tag{3.14}
\]

两指数分别由 \(\nu^{-1}\int_0^T\xi(T-t)D_C^\alpha Z(t)dt\) 及其参考版本定义。令 \(\lambda=\nu\sigma\)，则

\[
|Z-\widehat Z|\le k_\lambda*R,\qquad
|L_T-\widehat L_T|
\le\nu^{-1}(q_\alpha*k_\lambda*R)(T)
\le\nu^{-1}(\xi*R)(T).
\tag{3.15}
\]

特别地，若 \(R/\nu\le\delta_F\)，则

\[
|L_T-\widehat L_T|\le\delta_F\int_0^T\xi(s)ds.
\tag{3.16}
\]

**证明。** 令 \(e=Z-\widehat Z\)。差商恒等式给出 \(D_C^\alpha e=\nu[d+(Z+\widehat Z)/2]e-r\)，其系数实部不超过 \(-\lambda\)。对 \(v_\varepsilon=(|e|^2+\varepsilon^2)^{1/2}-\varepsilon\) 使用正则性引理，结合 \(|e|^2/(|e|^2+\varepsilon^2)^{1/2}\ge v_\varepsilon\) 及梯度模长不超过 1，得

\[
D_C^\alpha v_\varepsilon+\lambda v_\varepsilon\le R\quad\text{a.e.}.
\tag{3.17}
\]

(3.10) 与 \(\varepsilon\downarrow0\) 给出每个时刻的状态界。绝对 Fubini 给出 \(I^{1-\alpha}\xi=V_0g_{2-\alpha}+g_{2-\alpha}*\xi'\)，其导数即 (3.14)，并给出 \(g_\alpha*q_\alpha=\xi\)。因此 \(q_\alpha\in L^1\)、\(\xi\ge0\)。令 \(A_\alpha=I^{1-\alpha}\xi\)，再用绝对 Fubini 和 \(AC\) 分部积分，得到

\[
L_T-\widehat L_T
=\nu^{-1}\int_0^TA_\alpha(T-t)e'(t)dt
=\nu^{-1}(q_\alpha*e)(T).
\tag{3.18}
\]

Fubini 积分由 \(\|\xi\|_\infty T^{1-\alpha}\|e'\|_1/\Gamma(2-\alpha)\) 控制；边界项因 \(A_\alpha(0)=e(0)=0\) 消失。正性给出第一指数界。最后由 \(g_\alpha-k_\lambda=\lambda g_\alpha*k_\lambda\ge0\)，得

\[
0\le q_\alpha*k_\lambda=\xi-\lambda\xi*k_\lambda\le\xi.
\tag{3.19}
\]

结合卷积结合律和非负积分得到其余结论。\(R\) 是物理残差，故因子 \(\nu^{-1}\) 要保留，直到使用 \(R/\nu\le\delta_F\) 才消去。∎

本文保留的原创性主张，是这条 Heston 指数连接、可认证的历史单元权重，以及它们在冻结数值输出完整误差中的落实。凸性、正预解核、圆盘支持函数和单位成本排序属于已有工具。\(q_\alpha\) 的条件仅处理解析传播；概率模型存在性、仿射变换和鞅性质分别核查。

若闭单元 \([a_j,b_j]\) 上有完整历史残差包络 \(R\le R_j\)，则

\[
|L_T-\widehat L_T|
\le\nu^{-1}\sum_jR_j\int_{a_j}^{b_j}(q_\alpha*k_\lambda)(T-s)ds
\le\nu^{-1}\sum_jR_j\int_{a_j}^{b_j}\xi(T-s)ds.
\tag{3.20}
\]

第一种权重只有在严格包围后才能用于计算；现有实验实现第二种权重。若定价分区与残差源单元不重合，要对全部相交闭单元取最大残差。任何单元边界都不重启 Caputo 历史。


### 3.4. 曲线条件与常曲线核

定理3.3所需的曲线条件是 \(q_\alpha=(I^{1-\alpha}\xi)'\) 非负，而非 \(\xi\) 递增。真解和参考仍须属于 \(AC[0,T]\)、具有相同零初值，并满足(3.13)的完整时间残差和耗散前提。物理残差仍为 \(R\)，规范残差为 \(R/\nu\)，物理耗散为 \(\lambda=\nu\sigma>0\)。两指数继续采用第3节的D-type定义。这些条件须在每次应用中验证；定价核条件本身不证明随机模型存在，也不扩展已经核验的Riccati正则性域。

对实曲线 \(\xi\in AC[0,T]\)、\(\xi(0)=V_0\ge0\)，精确的充分条件是

\[
q_\alpha=V_0g_{1-\alpha}+g_{1-\alpha}*\xi'\ge0
\quad\text{a.e.},\qquad g_\beta(t)=t^{\beta-1}/\Gamma(\beta).
\tag{3.21}
\]

不要求 \(\xi'\) 非负。事实上，\(A_\alpha=I^{1-\alpha}\xi=V_0g_{2-\alpha}+g_{2-\alpha}*\xi'\) 绝对连续、\(A_\alpha(0)=0\)，且

\[
\|q_\alpha\|_1\le
\frac{T^{1-\alpha}}{\Gamma(2-\alpha)}(V_0+\|\xi'\|_1),
\qquad g_\alpha*q_\alpha=\xi.
\tag{3.22}
\]

第二个恒等式由绝对Fubini和 \(g_\alpha*g_{1-\alpha}=g_1\) 给出，对有符号 \(\xi'\) 仍成立；不能删去启动项 \(V_0g_{1-\alpha}\)。(3.21)进一步推出 \(\xi\ge0\)。因此定理3.3的证明继续成立：积分分部给出 \(L_T-\widehat L_T=\nu^{-1}(q_\alpha*e)(T)\)，正resolvent恒等式给出

\[
0\le q_\alpha*k_\lambda
=\xi-\lambda\xi*k_\lambda\le\xi.
\tag{3.23}
\]

指数的Fubini步骤由 \(\|\xi\|_\infty T^{1-\alpha}\|e'\|_1/\Gamma(2-\alpha)\) 支配；边界项因 \(e(0)=A_\alpha(0)=0\) 消失。AC情形的Caputo凸性与正零初值逆仍为先行工具 [LiLiu2018, Kopteva2021v2]。完整有限历史卷积、时间单元权重(3.20)与节点半径的向外构造均在(3.21)下有效；单元始终携带全部Caputo历史。

这是对充分曲线条件的严格放宽，不宣称它对所有可能的认证方法必要。若 \(q_\alpha\) 变号，一般安全式是 \(\nu^{-1}(|q_\alpha|*k_\lambda*R)(T)\)，不能未经证明沿用正消去。分数阶forward variance表示及模型可实现性约束已见 [ElEuchRosenbaum2017v1, Proposition 3.1 and Corollary 3.3]；本解析条件不取代这些约束。

**推论3.4（下降解析曲线）。** 设 \(V_0>0\)、\(c>0\)，\(\xi(t)=V_0(1-ct)\)。则

\[
q_\alpha(t)=\frac{V_0t^{-\alpha}}{\Gamma(1-\alpha)}
\left(1-\frac{ct}{1-\alpha}\right).
\tag{3.24}
\]

因此(3.21)在 \((0,T)\) 上成立，当且仅当 \(cT\le1-\alpha\)，等号允许。此时 \(\xi(T)\ge\alpha V_0>0\)，但 \(\xi'<0\)。

**证明。** 将常导数 \(-V_0c\) 与 \(g_{1-\alpha}\) 卷积，得到 \(-V_0c\,t^{1-\alpha}/\Gamma(2-\alpha)\)。加入初值项并使用 \(\Gamma(2-\alpha)=(1-\alpha)\Gamma(1-\alpha)\)，得到(3.24)。括号非负恰等价于所述条件。∎

该例仅为解析说明，未作为新增金融实验，也未宣称已经构造可实现的rough-Heston方差曲线。曲线正性本身并不足以保证(3.21)：\(1-\alpha<cT<1\) 时仍有 \(\xi>0\)，但期限末段的核为负。

**推论3.5（常曲线的显式传播）。** 在定理3.3的状态前提下，令 \(\xi\equiv V_0\ge0\)。则

\[
q_\alpha*k_\lambda=V_0E_\alpha(-\lambda t^\alpha),\qquad
|L_T-\widehat L_T|\le
\frac{V_0}{\nu}\int_0^T
E_\alpha(-\lambda(T-s)^\alpha)R(s)\,ds.
\tag{3.25}
\]

若 \(R\le\nu\delta_F\)，显式上界为

\[
\eta_{\rm ML}=V_0\delta_F T E_{\alpha,2}(-\nu\sigma T^\alpha)
\le\min\left\{
V_0\delta_F T,
\frac{V_0\delta_F T^{1-\alpha}}{\nu\sigma\Gamma(2-\alpha)}
\right\}.
\tag{3.26}
\]

**证明。** 对绝对局部可积的Mittag–Leffler级数逐项卷积，得 \(g_{1-\alpha}*k_\lambda=E_\alpha(-\lambda t^\alpha)\)；逐项积分得 \(\int_0^T E_\alpha(-\lambda t^\alpha)dt=T E_{\alpha,2}(-\lambda T^\alpha)\)。(3.23)给出 \(0\le E_\alpha\le1\)，证明第一项比较。又有 \(\int_0^tk_\lambda=(1-E_\alpha(-\lambda t^\alpha))/\lambda\le1/\lambda\)，故状态界 \(|e|\le\delta_F/\sigma\) 经非负 \(q_\alpha\) 积分给出第二项比较。∎

显式上界保留有限历史与正确物理尺度。只有新旧界均约束相同D-type目标和参考时，才可合法取小值；代入式参考必须单独认证残差转换项。本推论是解析结论，不宣称已经数值实现Mittag–Leffler加权传播，也不将新模型实例列为已认证。

**补充命题 3.6（不预设近似半平面的半径）。** 设参考轨迹绝对连续、在每个正时间邻域局部 Lipschitz，且具有相同初值。若 \(\delta_F<s_0^2/2\)，则其误差满足
\[
|Z-\widehat Z|\le E_\delta
=s_0-\sqrt{s_0^2-2\delta_F}
=\frac{2\delta_F}{s_0+\sqrt{s_0^2-2\delta_F}}.
\tag{3.27}
\]
证明中把误差线性项改写成 \((d+Z)e-e^2/2\)，精确解半平面给
\(D_t^\alpha|e|\le\nu(-s_0|e|+|e|^2/2+\delta_F)\)，以同一凸模长正则化解释。任取 \(E_\delta<\ell<s_0+\sqrt{s_0^2-2\delta_F}\)，右端在 \(|e|=\ell\) 严格负；首次达到 \(\ell\) 与 (3.3) 矛盾。令 \(\ell\downarrow E_\delta\) 得结论。不满足这个充分条件并不意味着实际误差或极点存在。本文完成的节点场已证半平面，使用 (3.8)，不被 (3.27) 门槛限制。

## 4. 连续参考认证与完整 Fourier 价格

### 4.1. 初始单元、连续残差与向外算术

对每个候选点 \(\alpha=\beta\in\{.52,.6,.9\}\) 及每个 \(u=n/8,\ n=0,\ldots,512\)，保存
\[
\bar G(t)=\nu c_0+A_1t^\beta+A_2t^{2\beta}+\bar L(t),\quad
c_0=-(u^2+1/4)/2,\quad \widehat Z=I^\alpha\bar G,\quad T=1/2.
\tag{4.1}
\]
\(\bar L\) 为节点 \((t_j,L_j)\) 的连续物理时间线性插值，\(L_0=0\)。节点及复系数按其binary64表示对应的精确二进有理数解释。该参考轨迹的连续时间误差由下列独立残差控制
\[
r_t=\bar G-\nu F(\widehat Z),\quad
\delta_F=\nu^{-1}\sup_{0\le t\le T}|r_t|.
\tag{4.2}
\]
式(4.1)定义完整的绝对连续参考轨迹。其独立残差给出模型价格区间，再据此估计所选[3/3]流程的输出误差。

写
\[
\widehat Z=H_0+J,\quad J=I^\alpha\bar L,\quad
H_0=B_1t^\alpha+B_2t^{\alpha+\beta}+B_3t^{\alpha+2\beta},
\]
\[
B_1=\frac{\nu c_0}{\Gamma(1+\alpha)},\quad
B_2=\frac{A_1\Gamma(1+\beta)}{\Gamma(1+\alpha+\beta)},\quad
B_3=\frac{A_2\Gamma(1+2\beta)}{\Gamma(1+\alpha+2\beta)}.
\tag{4.3}
\]
首单元 \(J=L_1t^{\alpha+1}/[t_1\Gamma(2+\alpha)]\)。将全部广义幂代入 (4.2)，先精确抵消 \(\nu c_0\)，合并相同幂，再取 \(\sum_p|r_p|t_1^p\)。所有 \(p>0\)，这是整个首闭单元的上界；广义幂展开保留了分数阶启动行为。

在源单元 \([a,b]\subset[0,q]\)，令 \(\tau=q-a,h=b-a\)，线性帽函数的积分权重为
\[
I_0=\{\tau^\alpha-(\tau-h)^\alpha\}/\alpha,\quad
I_1=\{\tau^{\alpha+1}-(\tau-h)^{\alpha+1}\}/(\alpha+1),
\]
\[
w_R=(\tau I_0-I_1)/(h\Gamma(\alpha)),\quad
w_L=I_0/\Gamma(\alpha)-w_R.
\tag{4.4}
\]
权重非负。截断单元的端点按原单元 affine 插值恢复；末单元 \(b=q\) 可直接用
\(w_R=h^\alpha/[\alpha(\alpha+1)\Gamma(\alpha)],w_L=\alpha w_R\)。
对 \(h/\tau<.01\)，保留正级数八项，分别使用
\[
w_R=\frac{h\tau^{\alpha-1}}{\Gamma(\alpha)}
\sum_{k\ge0}\frac{(1-\alpha)_k(h/\tau)^k}{k!(k+2)},\quad
w_L=\frac{h\tau^{\alpha-1}}{\Gamma(\alpha)}
\sum_{k\ge0}\frac{(1-\alpha)_k(h/\tau)^k}{k!(k+1)(k+2)}.
\tag{4.5}
\]
无尺度尾各不超过 \(z^8/(1-z)\)，因为 \(0<(1-\alpha)_k/k!\le1\)。这减少近等端点相减造成的区间膨胀，不使用浮点求积替代历史积分。

每个非首原单元二分为四个闭子单元 \([a,b]\)，选保存 二进有理数 中心 \(m\)。若已有整个子单元导数界，则
\[
\sup_{[a,b]}|r_t|\le|r_t(m)|+\max(m-a,b-m)\sup_{[a,b]}|r_t'|.
\tag{4.6}
\]
原节点处残差的普通导数可能不连续，以下导数上界均在几乎处处的意义下成立；残差绝对连续及积分基本定理仍给 (4.6)。全部导数上界通过以下三个恒等式分别建立并取最小值：
\[
r_t'=\bar G'-\nu(d+\widehat Z)\widehat Z',
\]
\[
P_r=\nu c_0+A_1t^\beta+A_2t^{2\beta}-\nu F(H_0),\quad
r_t=P_r+\bar L-\nu(d+H_0)J-\nu J^2/2,
\]
\[
r_t'=P_r'+\bar L'-\nu[(d+H_0+J)J'+H_0'J],
\quad
\widehat Z'=\frac{\nu c_0\,t^{\alpha-1}}{\Gamma(\alpha)}+I^\alpha\bar G'.
\tag{4.7}
\]
过去源单元的常数核权重随积分上限递减；当积分上限位于当前源单元内时，其权重递增。两类权重均由端点给出严格包络。第三式在每个源单元先合并
\(\bar G'(s)=\beta A_1s^{\beta-1}+2\beta A_2s^{2\beta-1}+\bar L'(s)\)，再用正核积分，保留原始关系中的抵消。

首源单元的奇异项以分数幂积分直接处理。对 \(p>0,t_1\le a\le q\le b\)，其正权重满足
\[
\frac{t_1^pb^{\alpha-1}}{p\Gamma(\alpha)}
\le\frac1{\Gamma(\alpha)}\int_0^{t_1}s^{p-1}(q-s)^{\alpha-1}\,ds
\le\min\left\{
\frac{t_1^p(a-t_1)^{\alpha-1}}{p\Gamma(\alpha)},
\frac{\Gamma(p)}{\Gamma(\alpha+p)}
 \max_{q\in[a,b]}q^{\alpha+p-1}\right\}.
\tag{4.8}
\]
当 \(a=t_1\) 第一上界舍弃，第二上界由完整 Euler Beta 积分得到且有限；下界及第一上界由端点核单调性给出。所有 \(p,\alpha>0\)，经典 Beta 公式假设成立。

用同一 \(\widehat Z'\) 包络与严格点值，认证所有非首子单元的 \(\operatorname{Re}\widehat Z\) 上界。首单元写成 \(t^\alpha\) 乘有限括号，使用负常数项和其余正部的端点贡献。只有全部闭单元实部上端不正时才启用 (3.8)。这里的启用条件覆盖整个闭时间单元。

结构证书和特殊函数采用端点为整数除以 \(2^{100}\) 的外舍入区间。残差批量权重采用 IEEE binary64，每步基本运算用相邻可表示数向外扩；Gamma 从精确有理包络转换后用 Fraction 比较端点。log 使用二进制精确缩放与 \(z\in[0,1/3]\) 的二十二项 atanh 级数，尾为 \(2z^{45}/[45(1-z^2)]\)。exp 缩放后 \(|r|<1\)，24阶 Taylor 尾为 \(3/25!\)。log、exp和非整数幂分别采用上述显式余项构造区间。

矩阵乘法对严格权重中心 \(W_c\)、半径 \(W_r\) 和保存 二进有理数 值 \(X\) 加入
\[
\left(\gamma_{2n}\|W_c\|_{1,\mathrm{row}}+
\|W_r\|_{1,\mathrm{row}}\right)\|X\|_{\infty,\mathrm{column}},
\quad \gamma_{2n}=\frac{2n\,2^{-53}}{1-2n\,2^{-53}},
\tag{4.9}
\]
再加 下溢误差 预算。该界由基本舍入因子乘积的归纳估计得到，允许不同加法结合顺序；范数求和也外扩。计算采用IEEE基本运算的最近舍入、平方根的正确舍入和渐进下溢，并要求运算过程无溢出或NaN。源码与计算版本见补充材料；本节的包含结论以这些运算假设及所列余项界为依据。

对固定曲线定义
\[
J_0(z)=\theta z+(V_0-\theta)zE_{\alpha_0,2}(-\lambda_\xi z^{\alpha_0}),\quad
J_1(z)=\theta z^2/2+
(V_0-\theta)z^2(E_{\alpha_0,2}-E_{\alpha_0,3})(-\lambda_\xi z^{\alpha_0}).
\tag{4.10}
\]
它们分别为 \(\int_0^z\xi_*(s)ds,\int_0^zs\xi_*(s)ds\)；后式由逐项积分验证。若线性场单元为 \([a,b]\)，\(A=T-b,B=T-a\)，严格非负指数权重为
\[
w_l=\frac{J_1(B)-J_1(A)-A[J_0(B)-J_0(A)]}{b-a},\quad
w_r=\frac{B[J_0(B)-J_0(A)]-J_1(B)+J_1(A)}{b-a}.
\tag{4.11}
\]
幂场 \(t^\beta\) 的曲线矩为
\[
\int_0^T\xi_*(T-t)t^\beta dt
=\frac{\theta T^{\beta+1}}{\beta+1}
 +(V_0-\theta)\Gamma(\beta+1)T^{\beta+1}
 E_{\alpha_0,\beta+2}(-\lambda_\xi T^{\alpha_0}).
\tag{4.12}
\]
由级数和 Beta 积分可直接得到。结合 (4.1)，\(\bar L\) 为严格有限和。三角相位与复指数也使用有限 Taylor 及显式尾。Mittag–Leffler级数的尾项在本期限 \(z=\lambda_\xi T^{\alpha_0}<1\) 时可取 \(3z^{64}/(1-z)\)，因为所有 Gamma 参数大于一且 Euler 积分给 \(\Gamma(\gamma)\ge e^{-1}>1/3\)。严格积分给出近似指数的区间；模型指数与近似指数之差由式(C.5)控制。

### 4.2. 解析条带、真实尾与价格包含

**定理 4.1。** 设 \(M_T>0,\mathbb E M_T=1\)，任取 \(0<a_*<1/2,h_*>0\)，令
\(g(z)=e^{-ikz}\phi_T(z-i/2)/(z^2+1/4)\)。则以无限梯形求和代替 (2.7) 的价格误差不超过
\[
\epsilon_{\rm grid}
=\frac{\sqrt m\,e^{a_*|k|}}
{(1/2-a_*)(e^{2\pi a_*/h_*}-1)}.
\tag{4.13}
\]

**证明。** Jensen 给条带内
\(|\phi_T(z-i/2)|\le\mathbb E M_T^{1/2-\operatorname{Im}z}\le1\)。
紧子带中 \(x^q|\log x|^j\le C(1+x)\)，故变换解析。边界 \(z=r\pm ia_*\) 满足
\[
|z^2+1/4|\ge r^2+(1/2-a_*)^2,\quad
\int_{\mathbb R}|g(r\pm ia_*)|\,dr
\le M_*=\frac{\pi e^{a_*|k|}}{1/2-a_*}.
\]
把实轴 Fourier 积分线移到上下边界，竖线积分因二次衰减消失，得到
\(|\widetilde g(\omega)|\le M_*e^{-a_*|\omega|}\)。
绝对一致收敛的周期化 \(\sum_{j\in\mathbb Z}g(x+jh_*)\) 具有 Fourier 系数
\(h_*^{-1}\widetilde g(2\pi n/h_*)\)。在零点求和并扣掉 \(n=0\)，双边误差不超过
\(2M_* /(e^{2\pi a_*/h_*}-1)\)。
共轭对称把双边积分与和各减半，乘以 \(\sqrt m/\pi\) 得 (4.13)。证毕。

这是 Trefethen–Weideman [TrefethenWeideman2014] 的解析条带梯形理论的具体应用。价格节点采用各自的连续时间残差界，节点间求积误差则由解析条带控制。

固定 \(\kappa=0,-1<\rho<0\)。令 \(X=-\operatorname{Re}H\ge0\)，(3.6) 给
\[
D_x^\alpha X\ge\beta_u-s_0X-X^2/2,\quad
\beta_u=(1-\rho^2)u^2/2+1/8.
\tag{4.14}
\]
标量零初值解 \(w\) 满足等号，比较给
\[
X\ge w,\quad 0\le w\le R_u,\quad
R_u=\sqrt{s_0^2+2\beta_u}-s_0,\quad
\ell_u=(s_0+\sqrt{s_0^2+2\beta_u})/2.
\]
因为右端 \((R_u-w)(s_0+(R_u+w)/2)\ge\ell_u(R_u-w)\)，线性比较和 Simon [Simon2014] 的上界
\(E_\alpha(-z)\le(1+z/\Gamma(1+\alpha))^{-1}\) 给
\[
-\operatorname{Re}Z(t,u)\ge
R_u\frac{\ell_u\nu t^\alpha}{\Gamma(1+\alpha)+\ell_u\nu t^\alpha}.
\tag{4.15}
\]
比较论证使用全历史正最大值。

取 \(V>s_0/\sqrt{1-\rho^2}\)，置
\[
a_\rho=\sqrt{1-\rho^2},\quad b_V=a_\rho-s_0/V>0,\quad
f_\alpha(z)=z/(\Gamma(1+\alpha)+z).
\]
对 \(u\ge V\)，\(R_u/u\ge b_V,\ell_u\ge a_\rho u/2\)。任取 \(J\ge2\) 的分格 \(0=t_0<\cdots<t_J=T\)，由正核 (C.4) 及单调 \(f_\alpha\) 得
\[
c_V=\frac{b_V}{\nu}\sum_{j=0}^{J-1}
 f_\alpha(a_\rho\nu Vt_j^\alpha/2)
 [A_\alpha(T-t_j)-A_\alpha(T-t_{j+1})]>0,
\]
\[
|\phi_T(u-i/2)|\le e^{-c_Vu}\quad(u\ge V).
\tag{4.16}
\]
该包络对所有连续高频成立；时间划分用于构造正测度积分的下和。本实验取 \(J=64\)，以严格区间给 \(c_V\) 的正有理下界。端点 \(A_\alpha(0)=0\) 不作奇异求值。两个不同侧端点之差
\([A_{\rm lo}(T-t_j)-A_{\rm hi}(T-t_{j+1})]_+\)
是合法质量下界。

由正递减函数的右端和，对 \(V=Nh_*\)，真实离散尾的归一化价格预算为
\[
\epsilon_{\rm tail}
\le\frac{\sqrt m}{\pi}\frac{e^{-c_VV}}{c_VV^2}.
\tag{4.17}
\]
积分尾项使用精确解的包络。取零的有限节点同样按该包络计入误差，因而整个频率范围均有明确的误差项。

若节点值 \(\widehat\phi_n\) 给真实误差 \(\varepsilon_n\)，有限价格和
\[
\widehat c_N=1-\frac{h_*\sqrt m}{\pi}
\left(2\operatorname{Re}\widehat\phi_0+
\sum_{n=1}^N\frac{\operatorname{Re}(e^{-inh_*k}\widehat\phi_n)}
{(nh_*)^2+1/4}\right)
\tag{4.18}
\]
满足
\[
|c-\widehat c_N|\le\epsilon_{\rm grid}+\epsilon_{\rm tail}
 +\frac{h_*\sqrt m}{\pi}
\left(2\varepsilon_0+
\sum_{n=1}^N\frac{\varepsilon_n}{(nh_*)^2+1/4}\right)
 +\epsilon_{\rm arithmetic}.
\tag{4.19}
\]
系数 \(2\) 是 \(u=0\) 处梯形半权与分母 \(1/4\) 的乘积。相位、平方根、指数和有限求和的舍入误差均由严格区间包含。本文 \(h_*=1/8,a_*=9/20,N=1024\)，前 \(513\) 个节点 \(u\le64\) 使用独立残差，余下节点用真实包络、近似值零；\(u>128\) 使用 (4.17)。这一混合规则将节点误差与尾项共同纳入价格估计。

### 4.3. 独立参考场

每个候选分别使用自写 PI 流程生成并固定物理时间场
\(\bar G=\nu c_0+A_1t^\beta+A_2t^{2\beta}+\bar L\)，其中 \(\beta=\alpha_j\)，节点和系数按保存的精确二进有理数值解释。认证对象为 \(\widehat Z=I^\alpha\bar G\)，不是把浮点 PI 节点直接当精确解。首时间单元采用完整广义幂残差展开；其余闭时间单元采用严格卷积导数及中值定理包络，覆盖全部 \(t\in[0,1/2]\)。逐 Fourier 节点的物理残差除以确切 \(\nu\) 后进入已证误差屏障或已认证半平面线性误差界。

保存指数是导数型 \(\bar L_T=\nu^{-1}\int\xi_*(T-t)\bar G(t)dt\)。正核 \(q_\alpha=(I^{1-\alpha}\xi_*)'\ge0\) 给
\[
|L_T-\bar L_T|
\le E_{\rm state}(I^{1-\alpha}\xi_*)(T)/\nu
\le E_{\rm state}\theta T^{1-\alpha}/[\nu\Gamma(2-\alpha)].
\tag{4.20}
\]
此处不重复附加残差积分。固定曲线的 Gamma/ML 矩、场积分、指数、相位及求和均以100bit向外有理区间计算。

价格正半轴规则固定 \(h=1/8\)，解析条带 \(a=9/20\)。保存场在可用的 \(u=0:1/8:64\) 节点使用实际残差证书；64之后至128的近似变换明确取0，并逐节点计入真实变换包络；128之后的无限离散规则尾由已证连续积分包络控制。真实实部 Riccati 下比较与整条正核曲线的64格下和给高频包络，不依赖经验外推。解析条带梯形误差单独估计；全轴积分到正半轴积分及零节点半权已严格处理。由此得到下面全部十二行的模型价格包络，而不是网格收敛差或Richardson诊断。

这里 \(E_{\rm state}\) 是合法认证状态半径：命题3.6的 \(E_\delta\) 要求 \(\delta_F<s_0^2/2\)，其他节点可由已认证半平面取得 \(E_{\rm state}=\delta_F/\sigma\)。新实验优先使用定理3.3的有限历史指数包络，只在合法且更紧时保留全局备选。邻近场按同一构造独立生成系数和连续残差库。

## 5. 共同 Fourier 误差与金融判定

### 5.1. 冻结输出处的联合包含

固定一个模型参数、期限、积分轮廓和参考网格。记连续模型价格向量为 \(c^*\in\mathbb R^p\)，精确有限参考和为 \(\bar c\)，固定快速流程的输出为 \(c^{\rm fast}\)。在每个纳入网格的频率处，令参考变换为 \(\bar\phi_n\)，定义 \(z_n=\phi(u_n-i/2)-\bar\phi_n\)。第4.1节给出 \(|z_n|\le\epsilon_n\)；明确省去的有限节点取 \(\bar\phi_n=0\)，其半径由真实变换包络提供。同一参数与期限下的全部执行价共享同一个 \(z_n\)。

对第4.2节的 Lewis 规则，令 \(m_i=K_i/F\)、\(k_i=\log m_i\)，并取
\[
a_{in}=-\frac{h\sqrt{m_i}}{\pi}\frac{e^{-iu_nk_i}}{u_n^2+1/4}\quad(n>0),\qquad
a_{i0}=-\frac{2h\sqrt{m_i}}{\pi}.
\tag{5.1}
\]
零节点的半权已纳入 \(a_{i0}\)。完整误差为
\[
c^*-\bar c=\Re\sum_{n=0}^{N}a_{\cdot n}z_n+R,
\qquad R\in\mathcal R.
\tag{5.2}
\]
其中 \(\mathcal R\) 包含真实无限网格尾和解析条带离散化误差。用数值代表值代替精确 \(\bar c\) 时，还须纳入有限参考和的区间算术中心不确定性。省去的有限节点属于式(5.2)的节点误差，不再重复计入无限尾。这里的共享关系来自确定性变换对象，不依赖随机误差相关系数。

**定理5.1（完整共同节点包含）。** 设式(5.2)成立，全部半径非负，\(\mathcal R\) 是非空紧凸外包集合。定义
\[
\mathcal E_F=\left\{\Re\sum_na_{\cdot n}z_n:|z_n|\le\epsilon_n\right\}+\mathcal R,
\qquad d=\bar c-c^{\rm fast}.
\tag{5.3}
\]
则 \(c^*-c^{\rm fast}\in d+\mathcal E_F\)，且对实向量 \(w\)，
\[
h_{d+\mathcal E_F}(w)=w^\top d+
\sum_n\epsilon_n\left|\sum_iw_i a_{in}\right|+h_{\mathcal R}(w).
\tag{5.4}
\]
若中心差仅以区间盒 \(d\in[d^-,d^+]\) 交付，则将第一项替换为该盒的支持函数。式(5.4)的每个数值求值均采用向外包络。

**证明。** 将实际变换误差代入式(5.2)，即得包含关系。复圆盘乘积及其实线性像均为紧凸集合。圆盘 \(|z|\le\epsilon\) 对实线性泛函 \(\Re(bz)\) 的支持为 \(\epsilon|b|\)：Cauchy–Schwarz给出上界；当 \(b\ne0\) 时，\(z=\epsilon\overline b/|b|\) 取得该界，当 \(b=0\) 时任意可行点均取得该界。不同圆盘的支持相加，Minkowski和再加上余项支持，得到式(5.4)。平移产生有符号中心项。即使中心区间各坐标具有依赖性，用其外包盒作Minkowski和仍保持包含。证毕。

若 \(\mathcal R=\prod_i[-\rho_i,\rho_i]\)，同一集合的最小坐标盒满足
\[
h_{\operatorname{rect}(\mathcal E_F)}(w)=
\sum_i|w_i|\left(\sum_n\epsilon_n|a_{in}|+\rho_i\right).
\tag{5.5}
\]
因此，在平移前，其支持超过联合支持的量为
\[
G_F(w)=\sum_n\epsilon_n\left(
\sum_i|w_i a_{in}|-\left|\sum_iw_i a_{in}\right|\right)\ge0.
\tag{5.6}
\]
严格正差成立，当且仅当至少一个正半径节点上的非零系数 \(w_i a_{in}\) 不全位于同一条非负复射线。逐节点应用复三角不等式及其等号条件即得证明。平移不改变宽度。这一判据比较所构造集合与其自身的最小坐标盒；另行获得的有符号价格区间仍须纳入实际比较。

设另有已证明的模型价格盒 \(\mathcal I\)，则取 \(\mathcal I\cap(\bar c+\mathcal E_F)\)。实际模型向量属于该交集。即使不求解交集的支持优化，两个有效方向上界的较小值仍是有效上界，两个下界的较大值仍是有效下界。这样可保留最佳边际信息，并在完整预算下使用共同节点的抵消。数学交集的非空性来自真实包含，不由两个近似算法的数值接近推定。

**命题5.2（同一快速输出下的非零遗漏参考）。** 固定实际快速输出，包括其在遗漏有限节点上的零贡献。在同一有限定价映射中，为这些节点选择可非零的参考 \(\psi_n\)，并证明 \(|\phi_n-\psi_n|\le\rho_n\)。令 \(\bar c'=c_0+\Re(A\psi)\)、\(d'=\bar c'-c^{\rm fast}\)，并使 \(\mathcal R\) 包含全部条带、真实无限尾及新参考算术。则

\[
c^*-c^{\rm fast}\in d'
+\{\Re(Az):|z_n|\le\rho_n\}\oplus\mathcal R.
\tag{5.7}
\]

对称余项及方向 \(w\) 下，完整绝对预算采用

\[
DF\left(|w^\top d'|+
\sum_n\rho_n\left|\sum_iw_ia_{in}\right|
+h_{\mathcal R}(w)\right)\le\tau.
\tag{5.8}
\]

非对称余项须同时界定正反方向支持。参考中心改变不改变固定快速输出，但改变 \(d'\)，并要求支付新的中心算术。

**证明。** 在精确定价有限映射中加减新参考，变换误差为 \(z=\phi-\psi\)；余项包含其他完整差异。共同复圆盘的方向支持给出(5.8)。∎

旧零中心证书 \(|\phi_n|\le\varepsilon_n^0\) 与新中心 \(\psi_n\) 的证书不能直接对半径取小值。在新中心下，旧证书仅给出 \(|\phi_n-\psi_n|\le\varepsilon_n^0+|\psi_n|\)，故安全半径为 \(\min\{\rho_n,\varepsilon_n^0+|\psi_n|\}\)，或保留两个变换圆盘的交集。只有 \(|\psi_n|+\rho_n\le\varepsilon_n^0\) 才保证新圆盘包含于旧圆盘。否则两个独立有效的完整价格区间仍可交集，但不能自动声称同中心单调性。例如 \(\phi=0\) 同时属于 \(D(0,.1)\) 与 \(D(1,2)\)，却不属于 \(D(1,\min(.1,2))\)。边际与联合比较须使用相同更新中心、节点半径和完整余项，新增参考求值与认证均计入成本。

### 5.2. 方向与有限目标认证

对 \(w=e_i-e_j\)，节点系数为
\[
|a_{in}-a_{jn}|=\frac{h}{\pi(u_n^2+1/4)}
\left|\sqrt{m_i}e^{-iu_nk_i}-\sqrt{m_j}e^{-iu_nk_j}\right|\quad(n>0).
\tag{5.9}
\]
应先合并同一误差的系数，再取模。记 \(b_i=\sqrt{m_i}\)，则有
\[
|b_ie^{-iuk_i}-b_je^{-iuk_j}|
\le |b_i-b_j|+\min(b_i,b_j)\min\{2,|u|\,|k_i-k_j|\}.
\tag{5.10}
\]
证明只需用较小振幅拆出振幅差与相位差，再应用 \(|e^{ix}-e^{iy}|\le\min(2,|x-y|)\)。零节点的价差系数为 \(2h|b_i-b_j|/\pi\)。相近执行价的低频误差由此抵消；高频、求积及尾部贡献仍完整保留。

下文实现以有理向外区间计算对数、三角函数、平方根和圆周率，先包住精确系数差，再乘保存的节点半径。参考和区间与固定快速输出区间共同给出有符号中心差。展示时使用中点，不改变判定所用的向外端点。

若真实目标报价为 \(m^*\)，保存中心为 \(\bar m\)，且 \(m^*-\bar m\in\mathcal M\)，则采用 \(r=c^{\rm fast}-\bar m\)，并将输出误差集合替换为 \(\mathcal E-\mathcal M\)，以正确符号计入报价转换算术。否则，下列公式将 \(m\) 视为确切值。

令 \(J(e)=(r+e)^\top W(r+e)/(2p)\)，其中 \(r=c^{\rm fast}-m\)、\(W\succeq0\)，完整输出误差属于紧凸集合 \(\mathcal E\)。对任意试算向量 \(e_0\)，令 \(g_0=W(r+e_0)/p\)。凸性给出
\[
\inf_{e\in\mathcal E}J(e)\ge
J(e_0)-g_0^\top e_0-h_{\mathcal E}(-g_0).
\tag{5.11}
\]
对支撑仿射函数 \(J(e_0)+g_0^\top(e-e_0)\) 取下确界即得。\(e_0\) 的可行性不影响有效性，但影响紧致程度。数值原始最小值只有在支持或对偶义务也被正确包络后，才成为下界证书。

若 \(M^2\ge\sup_{e\in\mathcal E}e^\top We\)，展开平方得
\[
\sup_{e\in\mathcal E}J(e)\le
J(0)+\frac{h_{\mathcal E}(Wr)}p+\frac{M^2}{2p}.
\tag{5.12}
\]
例如，任何有效坐标盒 \(|e_i|\le b_i\) 都给出充分选择 \(M^2=\sum_{ij}|W_{ij}|b_i b_j\)。可用更紧的已验证范数界替代。凸二次函数的局部驻点不认证其最大值；上界须由支持函数、范数界、区间细分或有效松弛建立。

对有限候选，可将式(5.11)–(5.12)所得目标区间与定理5.3的逐坐标平方区间相交。只有当一个候选的上端点小于全部竞争者的下端点时，才认证唯一选择；否则返回下端点不超过最小上端点的候选集合，该集合包含全部真最优候选。不同候选具有不同变换误差，式(5.4)不将它们认作同一个变量。

支持函数公式、复三角不等式及凸性界是已有数学工具。本节的作用在于将模型特定的连续残差证书连接至实际多执行价输出，并保留完整预算和数值中心。其金融改进以第7节的完整算术比较为依据。

**定理 5.3（有限目标区间与选择稳定性）。** 对每个 \(\alpha_j\in\Theta_{\rm finite}\)，设全部模型价格都有已认证包络
\[
c_i(\alpha_j)\in[p^-_{ij},p^+_{ij}],\quad
B_i\in[b_i^-,b_i^+],\quad
A_i\in[a_i^-,a_i^+],\quad
M_i\in[m_i^-,m_i^+].
\tag{5.13}
\]
设 \(b_i^-\le b_i^+\le a_i^-\le a_i^+\)。令
\[
\ell(x,y)=
\begin{cases}0,&x\le0\le y,\\
\min(x^2,y^2),&\text{otherwise},\end{cases}
\quad v(x,y)=\max(x^2,y^2).
\]
\[
L_j=\frac1{24}\sum_i
\ell(p^-_{ij}-m_i^+,p^+_{ij}-m_i^-),\qquad
U_j=\frac1{24}\sum_i
v(p^-_{ij}-m_i^+,p^+_{ij}-m_i^-).
\tag{5.14}
\]
则 \(J(\alpha_j)\in[L_j,U_j]\)。记 \(L_*=\min_jL_j,U_*=\min_jU_j\)，真有限最优值满足
\[
J_*=\min_{\Theta_{\rm finite}}J\in[L_*,U_*].
\tag{5.15}
\]
对 \(\varepsilon\ge0\)，全部真 \(\varepsilon\) 近最优候选都在
\[
\{\alpha_j:L_j\le U_*+\varepsilon\};
\tag{5.16}
\]
条件 \(U_j-L_*\le\varepsilon\) 则充分保证该候选真近最优。若
\[
g:=\min_{j\ne j_0}L_j-U_{j_0}>0,
\tag{5.17}
\]
则 \(\alpha_{j_0}\) 是唯一模型目标的有限最优解。若
\[
\min_{\alpha_j\ge.6}L_j>U_*+\varepsilon,
\tag{5.18}
\]
则所有有限真近最优候选满足 \(\alpha_j<.6\)。

报价相容性另作判定：任一行满足 \(p^+_{ij}<b_i^-\) 或 \(p^-_{ij}>a_i^+\)，可排除该候选同时落在全部报价带内；若每行都有 \(p^-_{ij}\ge b_i^+\) 且 \(p^+_{ij}\le a_i^-\)，则该候选充分认证为报价相容。区间重叠而未满足内带条件只保留“可能相容”，不称相容成立。

**证明。** 真差 \(c_i-M_i\) 位于(5.14)使用的闭区间内。平方的闭区间最小值为 \(\ell\)，最大值为 \(v\)，故加权和给每个 \(J_j\) 的包络。每个 \(J_j\ge L_j\ge L_*\)，而取得最小 \(U_j\) 的候选给 \(J_*\le J_j\le U_*\)，得到(5.15)。若 \(J_j\le J_*+\varepsilon\)，则 \(L_j\le J_j\le U_*+\varepsilon\)，得(5.16)。反之 \(J_j-J_*\le U_j-L_*\)，给所列充分内条件。(5.17)使任一竞争者满足 \(J_j-J_{j_0}\ge L_j-U_{j_0}\ge g>0\)，故唯一。(5.18)使每个选定较高 H 候选的模型目标超过 \(J_*+\varepsilon\)，所以排除。以上并不要求报价误差在不同候选间独立。

若 \(p^+<b^-\)，真实 \(c<B\)；若 \(p^->a^+\)，真实 \(c>A\)，任一行即破坏全行相容。相反，内带条件给 \(B\le b^+\le c\le a^-\le A\)。逐行应用即得相容性声明。证毕。

**目标扰动推论。** 若额外算法目标 \(\widetilde J\) 满足
\(\sup_{\Theta_{\rm finite}}|\widetilde J-J|\le\delta_J\)，且所选候选对其为 \(\varepsilon_{\rm alg}\) 近最优，则
\[
J(\widehat\alpha)-J_*
\le2\delta_J+\varepsilon_{\rm alg}.
\tag{5.19}
\]
证明为 \(J(\widehat\alpha)\le\widetilde J(\widehat\alpha)+\delta_J
\le\min\widetilde J+\varepsilon_{\rm alg}+\delta_J
\le J_*+2\delta_J+\varepsilon_{\rm alg}\)。
如(5.17)的严格间隙 \(g>2\delta_J+\varepsilon_{\rm alg}\)，只能选择该唯一有限胜者。这是由有限目标间隙产生的选择稳定性，适用于 (8.2) 的固定候选集合。

## 6. 指定有理构造的结构

令 \(S=s_0-i\rho u=-d\)，\(A=\sqrt{S^2+2b}\) 取主根，\(R=A-S\)。短端和长端的三个系数分别为
\[
b_1=-\frac b{\Gamma(1+\alpha)},\quad
b_2=\frac{Sb}{\Gamma(1+2\alpha)},\quad
b_3=\frac{\Gamma(1+2\alpha)}{\Gamma(1+3\alpha)}
       (d b_2+b_1^2/2),
\tag{6.1}
\]
\[
g_0=-R,\quad g_1=\frac R{A\Gamma(1-\alpha)},\quad
g_2=-\frac R{A^2\Gamma(1-2\alpha)}
       +\frac{R^2}{2A^3\Gamma(1-\alpha)^2}.
\tag{6.2}
\]
对 \(1/2<\alpha<1\)，\(\Gamma(1-2\alpha)\) 为负且有限。Gatheral–Radoičić [GR2019] 的固定两端匹配构造要求
\[
\widehat H(y)=P(y)/Q(y),\quad
Q=1+q_1y+q_2y^2+q_3y^3,
\]
\[
\widehat H=b_1y+b_2y^2+b_3y^3+O(y^4),\quad
\widehat H=g_0+g_1y^{-1}+g_2y^{-2}+O(y^{-3}).
\tag{6.3}
\]
这六个条件给线性系统
\[
\begin{pmatrix}g_0&g_1&g_2\\b_1&-g_0&-g_1\\
b_2&b_1&-g_0\end{pmatrix}
\begin{pmatrix}q_1\\q_2\\q_3\end{pmatrix}
=\begin{pmatrix}b_1\\-b_2\\-b_3\end{pmatrix},
\quad p_1=b_1,\quad p_2=b_2+b_1q_1,\quad p_3=g_0q_3.
\tag{6.4}
\]
(6.1)–(6.4) 为既有构造。下文分别证明系统可逆、分母安全、轨迹半平面及独立参考场的真实解误差。

为避免预先除以匹配行列式，定义
\[
f=\Gamma(1+\alpha)^{-1},\quad p=\frac{\sin\pi\alpha}{\pi\alpha},
\quad v=-\cos\pi\alpha,\quad
m_\alpha=\frac{\Gamma(1+2\alpha)}{\Gamma(1+\alpha)^2},\quad
\zeta=\frac{\Gamma(1+2\alpha)\Gamma(1+\alpha)}{\Gamma(1+3\alpha)},
\]
\[
\mathsf d=Sb/m_\alpha,\quad
\mathsf c=\zeta(b^2/2-S^2b/m_\alpha),\quad
V=pR/A,\quad W=m_\alpha p v R/A^2+p^2R^2/(2A^3).
\tag{6.5}
\]
反射公式及递推关系给 \(b_1=-fb,b_2=f^2\mathsf d,b_3=f^3\mathsf c\)，\(g_1=V/f,g_2=W/f^2\)。注意后两式是除以 \(f,f^2\)。直接展开 (6.4) 的行列式和 Cramer 分子得到
\[
\begin{aligned}
\Delta={}&b^2W+2bRV-\mathsf dRW-\mathsf dV^2-R^3,\\
F_1={}&b^2V+b\mathsf dW-bR^2+\mathsf dRV+\mathsf cRW+\mathsf cV^2,\\
F_2={}&-b^2R+b\mathsf dV+b\mathsf cW+\mathsf d^2W+\mathsf dR^2+\mathsf cRV,\\
F_3={}&-b^3+2b\mathsf dR-b\mathsf cV-\mathsf d^2V+\mathsf cR^2.
\end{aligned}
\tag{6.6}
\]
\(\Delta\) 恰是原系统行列式，分子为 \(N_j=f^jF_j\)。只有证明 \(\Delta\ne0\) 后才可定义 \(q_j=N_j/\Delta\)，此时
\[
\Delta P=-fb\Delta y+f^2(\mathsf d\Delta-bF_1)y^2-f^3RF_3y^3,\quad
\Delta Q=\Delta+fF_1y+f^2F_2y^2+f^3F_3y^3.
\tag{6.7}
\]
恢复物理时间时，分母系数为 \(\nu^jq_j\)，不是重新定义 \(q_j\)。

**定理 6.1（全频域结构）。** 对
\[
\alpha\in[13/25,3/5],\quad \rho=-1489/2000,\quad \kappa=0,\quad
u\in\mathbb R,\quad \nu>0,
\tag{6.8}
\]
既有 (6.4) 匹配系统非奇异。其规范分母满足
\[
\operatorname{Re}q_j>0\ (j=1,2,3),\qquad
\operatorname{Re}Q(y)\ge1,\quad |Q(y)|\ge1\quad(y\ge0).
\tag{6.9}
\]
对 \(y>0\)，\(\operatorname{Re}\widehat H(y)<0\)。该结果覆盖全部正时间和全部有限实频率，不给 \(\alpha>.6\)、连续 \(\rho\) 域或非零 \(\kappa\) 的同一保证。

**证明。** 先取 \(u\ge0\)。令
\[
\omega=\sqrt{u^2+1/4},\quad \eta=u/(1+u),\quad
j(\eta)=\sqrt{\eta^2+(1-\eta)^2/4},\quad s=-\rho/2,
\]
\[
\bar S=s(1-\eta+2i\eta)/j(\eta),\quad
\bar A=\sqrt{1+\bar S^2},\quad \bar R=(\bar A+\bar S)^{-1}.
\tag{6.10}
\]
因 \(j^2\ge1/5\)，这些函数在闭 \(\eta\in[0,1]\) 上有定义。\(|\bar S|=|\rho|\)，且
\[
\operatorname{Re}\bar A^2
=1-\rho^2+2(\operatorname{Re}\bar S)^2\ge1-\rho^2>0.
\]
主根连续并位于第一象限；\(\operatorname{Re}\bar A,|\bar A|>3/5\)。两个第一象限数的内积实部非负，故
\[
|\bar A+\bar S|^2\ge|\bar A|^2+|\bar S|^2
\ge|\bar A^2-\bar S^2|=1,\quad
|\bar R|\le1,\quad\operatorname{Re}\bar R>0.
\]
式(6.10)将 \(\bar A-\bar S\) 写成倒数形式，其分母由当前参数直接确定。

以 \(\bar b=1/2\) 和 (6.10) 代入 (6.5)–(6.6)，得到带横线的原始量。按次数直接得到
\[
\Delta=\omega^3\bar\Delta,\qquad F_j=\omega^{3+j}\bar F_j.
\tag{6.11}
\]
定义三个实函数
\[
\bar B_j=\operatorname{Re}(\bar F_j\overline{\bar\Delta}).
\tag{6.12}
\]
附录 B 的严格有理覆盖证明，在整个闭矩形
\([13/25,3/5]\times[0,1]\) 上 \(\bar B_j>0\)，并且
\[
|\bar\Delta|^2\ge
\frac{88110801209184778874628745}{1267650600228229401496703205376}
>\frac1{14400}.
\tag{6.13}
\]
这一步先强制 \(\Delta\ne0\)，再给
\(\operatorname{Re}q_j=(f\omega)^j\bar B_j/|\bar\Delta|^2>0\)，因而得到 (6.9)。

为证明轨迹半平面，(6.7) 的有限卷积给
\[
|\Delta|^2\operatorname{Re}(P\overline Q)
=\sum_{n=1}^6 f^nD_ny^n,
\tag{6.14}
\]
\[
\begin{aligned}
D_1={}&-b|\Delta|^2,\\
D_2={}&\operatorname{Re}(\mathsf d)|\Delta|^2-2b\operatorname{Re}(F_1\overline\Delta),\\
D_3={}&\operatorname{Re}\{-RF_3\overline\Delta+
(\mathsf d\Delta-bF_1)\overline F_1-b\Delta\overline F_2\},\\
D_4={}&\operatorname{Re}\{-RF_3\overline F_1+
(\mathsf d\Delta-bF_1)\overline F_2-b\Delta\overline F_3\},\\
D_5={}&\operatorname{Re}\{-RF_3\overline F_2+
(\mathsf d\Delta-bF_1)\overline F_3\},\\
D_6={}&-\operatorname{Re}R\,|F_3|^2.
\end{aligned}
\tag{6.15}
\]
同一有理覆盖认证六个紧化量 \(\bar D_n<0\)；其尺度为 \(D_n=\omega^{7+n}\bar D_n\)。令 \(z=f\omega y\)，(6.14) 等于
\(\omega^7\sum_{n=1}^6\bar D_nz^n\)，故所有 \(y>0\) 上严格负。已证分母非零后，除以 \(|Q|^2|\Delta|^2\) 得 \(\operatorname{Re}\widehat H<0\)。负频率由主根、匹配系数的共轭对称性得到。闭端点 \(\eta=1\) 对应无穷频率极限，因此闭域证明覆盖全部有限频率。证毕。

系数实部正性给出分母无零点的充分条件。附录B列出计算机辅助证明所用的核心代数、基本函数余项和连续区间覆盖。

### 有定量范围的连续相关系数扩展

原参数域围绕公开数据实例的相关系数与粗糙度候选选择，同时保持六条件构造不变。原符号覆盖包含连续粗糙度区间和全部频率，并非典型校准参数盒的一般定理。严格符号可推出相关系数方向的持续性；以下把它定量化，没有用离散采样代替连续证明。

**定理 6.2（认证的相关系数持续性）。** 定理 6.1 的结论在

\[
\alpha\in[13/25,3/5],\qquad
\rho\in[-744501/10^6,-744499/10^6],\qquad
\kappa=0
\tag{6.16}
\]

上，对每个实 Fourier 频率和每个正时间成立。

**证明。** 保留频率紧化 \(\eta=u/(1+u)\)、\(0\le\eta\le1\)，以及原始未归一化多项式 \(\Delta,F_j,B_j,D_j\)。令 \(S_b=-\rho[(1-\eta)+2i\eta]/(2h)\)、\(h^2=\eta^2+(1-\eta)^2/4\)。则 \(|S_b|=|\rho|\)，负 \(\rho\) 时 \(\Re S_b\ge0\)，且 \(A^2=1+S_b^2\)、\(R=(A+S_b)^{-1}=A-S_b\)。在 \(|\rho|\le3/4\) 内，因 \(\Re A^2\ge1-\rho^2>0\)，平方根分支始终固定，并有

\[
|A|^{-1}\le8/5,\quad |A'|\le6/5,\quad
|(A^{-1})'|\le384/125,\quad |R|\le1,\quad |R'|\le11/5.
\tag{6.17}
\]

撇号表示实 \(\rho\) 导数。\(|R|\le1\) 由 \(|A+S_b|^2\ge1\) 得到：\(\Re A\,\Re S_b\) 和 \(\Im A\,\Im S_b\) 均非负，且 \(|A|^2=|1+S_b^2|\ge1-|S_b|^2\)。又因 \((\Re A)^2-(\Re S_b)^2=(|1+S_b^2|+1-|S_b|^2)/2>0\)，有 \(\Re R>0\)。

原定理的 \(\alpha\) 标量由严格向外端点包围给出

\[
0<p\le2/3,\quad0\le v\le1/3,\quad
1\le m\le3/2,\quad0<\zeta\le2/3.
\tag{6.18}
\]

其中 \(p\) 递减，\(v,m\) 递增，\(\zeta\) 递减；Gamma 比值的单调性由递增的 digamma 函数给出，\(m\ge1\) 还可直接由 Gamma 的对数凸性得到。这些标量均不依赖 \(\rho\)。

对原多项式逐项使用乘积法则的模长界，得到严格有理常数

\[
|\partial_\rho B_j|\le L_{B,j},\qquad
|\partial_\rho D_j|\le L_{D,j}.
\tag{6.19}
\]

具体组装使用 \((M,N)\) 表示 \(|f|\le M\)、\(|f'|\le N\)，相加取 \((M_1+M_2,N_1+N_2)\)，相乘取 \((M_1M_2,N_1M_2+M_1N_2)\)。这是有限的精确有理推导，不是数值差分导数。

令 \(m_{B,j}(C),m_{D,j}(C)\) 为连续 \((\alpha,\eta)\) 单元 \(C\) 在 \(\rho_0=-1489/2000\) 上的原精确符号下界。若全部

\[
m_{B,j}(C)-10^{-6}L_{B,j}>0,\qquad
m_{D,j}(C)-10^{-6}L_{D,j}>0
\tag{6.20}
\]

成立，则该单元在整个目标相关系数区间上通过认证。这一充分检验由均值定理给出，使用严格导数包围，不使用数值差分。它认证了 182002 个原叶与 79758 个更细叶。对其余单元，同时将 \(\rho,\alpha,\eta\) 作为区间变量直接评价原始复多项式，精确向外二进算术又在 19808 个闭单元上认证严格的 \(B_j>0,D_j<0\)。

原完整二叉中点树与精确局部拼接树核验：这 281568 个单元覆盖整个 \((\alpha,\eta)\) 矩形，没有缺口或内部重叠。精确面积为 \(2/25\)，每个单元都携带整个相关系数区间，三维精确体积为 \(1/6250000\)。因此原始符号对所列域的每一点成立；特别地 \(\Delta\ne0\)，归一化分母系数实部均正，半平面测试的实分子系数均负。原代数蕴含给出 (6.16)，包括 \(\eta=1\) 的无限频率极限；负频率由共轭给出。∎

这是窄范围的局部稳健性结果：相关系数总宽度为 \(2\times10^{-6}\)。它没有建立典型的宽校准盒，也不宣称改变相关系数后已重做价格实验。直接区间补强明确属于探索性阶段：在单用导数界的尝试留下正未决面积后，才固定其协议。证据保留这个未决阶段及独立有效的保守 fallback。

独立读取器检查全部旧符号记录、原 422481 节点分区树、局部拼接几何、独立组装的导数界，并通过另一套 Cramer 矩阵和分子多项式卷积重放全部 19808 个直接单元。二进算术原语和旧符号生成是共享依赖，没有重做每个旧区间多项式计算。巨大精确分数保留在机器账本。离散相关系数网格或连续性声明均不能替代证明中的任何单元。


## 7. 金融判定、收益归因与输出对照

### 7.1. 固定合同、单位与完整消融

原半年合同使用十二执行价 \(K_i=3700+100i\)，\(0\le i\le11\)，远期 \(F=4221.86\)、贴现 \(D=1\)，前向方差曲线固定为(2.4)。价格和任务误差均为指数点，持仓乘数为一，不推定交易所特定货币名义本金。候选只改变 \(\alpha\)，曲线和其他参数保持不变。三候选 \(.52,.60,.90\) 是有限比较，且与多条原 bid/ask 区间不兼容，不表示市场拟合成功或连续最优解。

下表比较 \(K=4400\) 减 \(K=4500\) 的完整任务界。每行保留实际输出、有符号中心、有限节点、条带、真实尾及算术；展示的上界向上舍入。季度研究重算对应期限的参考积分、真实变换包络和尾界，上游完整历史证书依法限制到短期限；不复用半年指数或尾数值。

| 期限与阶段 | 完整联合界，点 | 匹配有符号边际界，点 | 解释 |
|---|---:|---:|---|
| 半年：全局状态传播 | 1.397612096 | — | 原1点任务失败 |
| 半年：有限历史、原全局残差 | 0.378598956 | — | 主要传播改进；输出和中心不变 |
| 半年：逐时包络、原已用节点 | 0.367258782 | — | 约3%的附加收紧 |
| 半年：全部有限高节点、全局包络 | 0.132245064 | 0.158585551 | 包括高频认证和中心更新 |
| 半年：全部有限高节点、逐时包络 | 0.115215934 | 0.137896018 | 两种方法均通过0.25点 |
| 季度：至64、全局包络 | 1.207557898 | 1.545191542 | 0.25点失败 |
| 季度：至128、全局包络 | 0.351318692 | 0.408293698 | 0.25点失败 |
| 季度：至128、逐时包络 | 0.233318843 | 0.252393939 | 只有联合通过0.25点 |

相对表中原完整界，首个有限历史改进约72.91%。收紧的是保证误差界，不是观测到的真实误差或交易损失。半年高频精化合法地把中心从约 \(-0.166762218\) 更新至 \(-0.081698202\) 点，不能把全部收益归于共同几何。末行使用相同输出、中心、节点半径及余项，隔离了共同变量改变认证决定的作用。该逐时精化在全局阶段失败后另行固定，属于探索性期限迁移，不能事后改称预注册实验。

### 7.2. 二十八个组合方向

令 \(e_i\) 选取 \(K_i\)。以下持仓不为通过预算而重新缩放；总绝对权重为 \(\sum_i|w_i|\)。阈值均是指定持仓的指数点绝对误差。

| 类型 | 精确方向 | 数量 | 总绝对权重 |
|---|---|---:|---:|
| 相邻价差 | \(e_i-e_{i+1},\ 0\le i\le10\) | 11 | 2 |
| 相邻蝶式 | \(e_i-2e_{i+1}+e_{i+2},\ 0\le i\le9\) | 10 | 4 |
| 宽价差 | \(e_0-e_3,e_3-e_6,e_6-e_9,e_0-e_{11}\) | 4 | 2 |
| 正篮子 | \(\frac1{12}\sum_{i=0}^{11}e_i,\ \frac16\sum_{i=0}^5e_i,\ \frac16\sum_{i=6}^{11}e_i\) | 3 | 1 |

每组匹配比较的上游半径相同。有限历史方法在 \(\alpha=.52\)、0.5点预算下，联合通过28/28，边际13/28；0.25点预算下，\(\alpha=.60\) 分别10/28与1/28，\(\alpha=.90\) 分别20/28与13/28。\(.52\) 的1点预算下两种新方法均通过28/28，该宽松阈值不能单独识别共同结构收益。合法 payoff 交集在测试中没有进一步收紧。未通过只表示当前外界不足，不表示真实误差超过预算。

### 7.3. 原报价下预先固定的邻近候选

固定原半年 12 条报价、F=4221.86、D=1 及其余模型参数。新结果计算之前
冻结 alpha={0.520,0.525,0.530,0.540,0.550} 和第一层 N=1024；只要任一
相邻 joint 比较 unresolved，就把**全部五点**升级到 N=2048。
每点重新生成连续参考场、完整闭时间残差银行；64 以内已用节点、128 以内
全部有限省略节点、真无限尾、条带、参考算术和原报价转换不确定性全付。
目标为归一化价格平方 \(J=\frac1{24}\sum_i(c_i-m_i)^2\)；若改用指数点平方须统一乘 \(F^2\)。目标区间半宽只支付固定 bid/ask 价格
中点转换的外向算术误差，不是市场 bid/ask 半宽；排名不证明对任意市场
band 内报价目标的统一最优。Taylor 线性项保留共同 Fourier disks，
二次余项按完整坐标半径支付；marginal 对照使用同样上游半径。
不同 alpha 候选的误差没有被假定相关。

| alpha | N=1024 joint J ×10^8 | N=2048 joint J ×10^8 |
|---:|---:|---:|
| 0.520 | [4.825094, 6.778350] | [5.293449, 6.024095] |
| 0.525 | [5.645378, 7.501414] | [6.097920, 6.798485] |
| 0.530 | [6.748974, 8.517584] | [7.187004, 7.859529] |
| 0.540 | [9.807435, 11.422182] | [10.218707, 10.839486] |
| 0.550 | [14.000658, 15.482012] | [14.387007, 14.960680] |

| Generated layer | Joint strictly separated pairs | Matched marginal pairs |
|---|---:|---:|
| N=1024 | 7/10 | 3/10 |
| N=2048 | 10/10 | 7/10 |

第一层保留 unresolved 近邻并触发预先固定的全点升级。
最终五点集合认证 alpha=0.520 是严格最小候选。
这不是连续校准最优性。五点均仍与至少一条原 bid/ask 报价不兼容，
因此也不是市场模型识别。


两层全量生成共15,754,230个闭单元残差条目、5,130个参考指数和10,250个真实变换包络。独立读取器检查完整覆盖及最大值，重构指数、系数和目标并拒绝故意破坏；共享已披露的严格原语，不冒称重新独立推导每个残差导数。

### 7.4. 为什么认证冻结快速输出？

适用场景是存储或外部固定输出的验证：既有定价库审计、可重建的历史结果，或待检查任务中不能替换的生产输出。如果参考已经可用且允许更换返回值，直接返回其认证中心是合理对照。中心修正快速值也必须计入修正量的存储和最终加法舍入。下游支持函数便于复用，不自动意味着整个参考路线适合作为经济的在线求解器。

另行固定的描述性对照复用完整 \(N=2048,\alpha=.52\) 残差库及128历史分区：每个分区对全部相交闭源单元取最大，权重向外包围。五种方法使用相同模型、半年 \(4400-4500\) 价差、0.25点预算、参考中心、节点半径、条带与真实尾。它不改变预先固定的邻近网格主实验。

| 输出 | 完整联合界，点 | 匹配边际界，点 | 联合0.25点决定 |
|---|---:|---:|---|
| 冻结Padé | 0.394999331 | 0.514096070 | 未解决 |
| 直接参考（binary64） | 0.228237113 | 0.347333852 | 通过 |
| 快速值加存储修正 | 0.228237113 | 0.347333852 | 通过 |
| BL核心，512步 | 0.229082759 | 0.348179497 | 通过 |
| BL核心，1024步 | 0.228534686 | 0.347631424 | 通过 |

五种匹配边际界均未通过0.25点。直接参考与修正值在本例碰巧得到相同完整界，但实际存储值分别检查；精确二进有理算术支付参考返回、修正存储和最终加法舍入。允许自由替换输出时，直接参考比保留原快速值更简单。共同结构仍改变了参考及BL输出的认证决定。BL两层差异只是诊断，不是其认证误差。

完整证书生成并非零成本：需认证2,100,735个频率乘闭时间单元残差条目、513个参考指数、1,025个真实变换节点、无限尾及12,300个价格系数。完整读取检查全部条目并重构指数、系数和决定。每个附加组合计算1,025个共同圆盘支持项及完整余项；28组合复用同一库，无需新增残差生成。这是同参数、期限下的方向复用，不是跨未验证参数复用。

| 附加输出构造 | 确定性数学工作 |
|---|---|
| 原Padé | 352个Fourier值，每频率256个Jacobi样本 |
| 直接参考返回 | 返回已生成且完整计费的中心，支付binary64舍入 |
| 修正快速值 | 每价格存储一个修正量并作一次binary64加法 |
| BL核心，512步 | 67,371,264个历史标量向量乘积；2,626,560次修正Riccati求值 |
| BL核心，1024步 | 269,222,400个历史标量向量乘积；5,253,120次修正Riccati求值 |

这些是不同类型的工作量，不等同于统一浮点操作或总成本比。参考场生成、向外超越函数求值及验证与名义输出构造分别披露，不推导速度或机器性能优势。完整账本另列指数求积工作和两个粗包络失败阶段。


### 7.5. 实验能够支持的结论

现代方法对照仅重实现 Boyarchenko 等的 modified-Adams Riccati 核心，不声称复现完整 SINH 变形及 Conformal Bootstrap。两种离散化的接近只是诊断，不是区间证书。要比较完整认证输出，必须计入该保证所需的独立参考、尾部、算术与验证工作。

固定菜单在完整任务半径达到预算时给出可靠终止；最少动作数要求所有替代半径已认证且每动作单位成本。构造全部替代量仍属于证书生成工作，不能推断未知菜单的最少工作量。模型拟合、市场不确定性、交易成本及连续全局校准不属于输出误差保证。


## 8. 适用范围与统一复现入口

数学保证以指定模型、仿射变换、参考轨迹正则性及完整向外包围为条件。\(q_\alpha\ge0\) 是传播定理的条件，本身不证明随机模型合法性。结构域不覆盖一般均值回复或宽相关系数校准；极窄的连续相关系数条带只证明局部稳健性。未解决区间、失败预算和报价不兼容均保留为有效结果。

正式入口是仓库的 `v2.0.0-research-20261007` 发布，其 PDF、可编辑源码、证据包与复现命令固定同一个源码版本。命名证据包包含实际科学输入和独立读取器，不以 GitHub 自动源码归档替代。清单及校验和识别文件变化，科学读取器检查文件所支持的结论。

解压后在证据目录运行 `python reproduce.py --full`。默认检查从固定场及完整残差库重建价格和任务结论；完整模式另以残差生成代码核对存储证据。邻近候选合同、两层精化、失败阶段、算术对照与结构后备均保留。完整重生成与独立证据读取分别说明。公开必要软件依赖，不包含个人宿主配置或运行测量。

独立技术附录存放完整价格行、巨大精确分数、菜单轨迹与早期阶段。经典原链扩展保留独立主张，尚未变成全年完整货币价格证书。这些材料从同一正式入口链接，不增加主文贡献数量。

有限历史传播解释了同一残差下的主要收紧，共同 Fourier 结构进一步改变匹配的四分之一点认证决定。它们服务于冻结输出审计及同参数、期限下多方向复用。允许替换输出时，仍须比较直接参考输出，并计入全部认证工作。邻近网格和输出对照在明确范围内检验了这些用途。


## 附录 A. 概率模型及条带变换的文献应用核验

所用一手来源是 Abi Jaber–El Euch, arXiv:1803.00477v1，首次公开 2018-03-01，PDF 首页 March 2, 2018；正式发表于 2019 年 Statistics & Probability Letters 149, 63–72。引用位置是其 13 页预印本自有页码：p.4 Theorem 2.1、Example 2.2，p.5 Theorem 2.3，pp.9–10 H2 与 Table 1。不是将期刊页码混入预印本。

对 \(K_\alpha=t^{\alpha-1}/\Gamma(\alpha)\)，
\[
\int_0^hK_\alpha^2dt=
\frac{h^{2\alpha-1}}{(2\alpha-1)\Gamma(\alpha)^2},\quad
\int_0^T(K_\alpha(t+h)-K_\alpha(t))^2dt
\le\frac{h^{2\alpha-1}}{\Gamma(\alpha)^2}
\int_0^\infty[(r+1)^{\alpha-1}-r^{\alpha-1}]^2dr.
\tag{A.1}
\]
后一积分在零端指数 \(2\alpha-2>-1\)，大端指数 \(2\alpha-4<-1\)，故有限。第一类 resolvent
\[
\mathcal L_\alpha(dt)=t^{-\alpha}dt/\Gamma(1-\alpha),\quad
K_\alpha*\mathcal L_\alpha=1
\tag{A.2}
\]
由 Beta恒等式验证，且非负非增。完全单调谱测度
\[
\mu_\alpha(dx)=x^{-\alpha}dx/
[\Gamma(\alpha)\Gamma(1-\alpha)]
\tag{A.3}
\]
给 \(K_\alpha(t)=\int e^{-xt}\mu_\alpha(dx)\)。H2 中的两个谱积分分别按 \(r=xh\) 变为常数乘 \(h^{\alpha-1}\)、\(h^{\alpha-1/2}\)，其余常数
\(\int(1\wedge r^{-1/2})r^{-\alpha}dr\)、
\(\int r^{-\alpha-1/2}(1\wedge r)dr\) 在 \(.5<\alpha<1\) 均有限。源文 Table 1 因此涵盖所需 shifted 核条件。

曲线 (2.4) 非递减、非负初值、局部 Hölder \(\alpha_0=.5286\)。在 \(\alpha\in[.52,.9]\) 上，核的 \(\gamma/2=\alpha-.5\le.4<\alpha_0\)。故 Example 2.2(i) 的曲线类假设满足，Theorem 2.1 给非负连续方差弱解及矩界。等价核输入
\[
b_\alpha(t)=D_C^\alpha\xi_*(t)=I^{1-\alpha}\xi_*'(t)\ge0,\quad
b_\alpha(t)=
\frac{(\theta-V_0)\lambda_\xi}{\Gamma(1+\alpha_0-\alpha)}
t^{\alpha_0-\alpha}+O(t^{2\alpha_0-\alpha})
\tag{A.4}
\]
最坏指数 \(-.3714>-.5\)，所以属于 \(L^2_{\rm loc}\)；\(\xi_*=V_0+K_\alpha*b_\alpha\)。非负输入测度也符合 Example 2.2(ii)。这同时解释变动核但固定远期方差曲线的合法性。

源 Theorem 2.3 要求 \(\operatorname{Re}\psi_1\in[0,1]\)、第二状态初始变换非正实部、方差强制项非正实部。取 \(\psi_1=ia=1/2+iu\)，其他初始/强制项为零，恰给 (2.2)、(2.6)，以及唯一弱分布。取 \(\psi_1=1\)，Riccati 解为零，得到 \(\mathbb E S_T=S_0\)；正局部鞅常均值使其为真鞅。因而 (4.13) 的概率条带来自连续时间模型。此处应用成熟存在性及仿射变换理论，不主张新存在性定理。

## 附录 B. 定理 6.1 的精确有限证书

证书域为 \(\mathcal B=[13/25,3/5]\times[0,1]\)。每个区间 \(I=[\ell/2^{100},r/2^{100}]\) 采用整数外舍入。有理输入上下取整，乘法取四角极值并量化；倒数先排除零，平方根用整数 isqrt 和向上补一，复数用实虚矩形算术。主根及倒数分支已由 (6.10) 的解析下界保证，不用浮点符号容忍度。

四个基础 \(\alpha\) 函数 \(p,v,m_\alpha,\zeta\) 满足
\[
p'<0,\quad v'>0,\quad
(\log m_\alpha)'=2[\psi(1+2\alpha)-\psi(1+\alpha)]>0,
\]
\[
(\log\zeta)'=2[\psi(1+2\alpha)-\psi(1+3\alpha)]
 +[\psi(1+\alpha)-\psi(1+3\alpha)]<0.
\tag{B.1}
\]
\(\psi'(x)=\sum_{n\ge0}(x+n)^{-2}>0\)；\(p,v\) 的导数由基本三角恒等式直接给出。因此严格端点值包住整个连续 \(\alpha\) 区间，不使用 \(\alpha\) 扫点。

基础 \(\pi\) 由 Machin 恒等式及各一百项 arctan 交错尾认证；log 归约到 \([1,2]\) 后用一百项 atanh 正级数及几何尾；exp 归约到 \([0,1]\) 后用一百项 Taylor 及几何尾，反复严格平方恢复。正实 Gamma 先递推上移到 \(z\ge20\)，对 log Gamma 保留 \(B_2,\ldots,B_{20}\)，正实余项满足
\[
0<R_{10}(z)<B_{22}/(22\cdot21z^{21}).
\tag{B.2}
\]
Binet 正积分中 arctan 的十项几何余项为正且不超过首遗漏幂，积分后即给 (B.2)，亦为 NIST2010 的正实 Stirling 余项设定；指数化后逐项除回递推因子。sin、cos 各保留三十二项，Lagrange 绝对尾分别为 \(M^{65}/65!,M^{64}/64!\)。Bernoulli、阶乘和区间端点均为确切有理数。

对每个闭矩形，将这些包络依次代入 (6.10)、(6.5)、(6.6)、(6.12)、(6.15)。只有三条 \(\bar B_j\) 下端严格正、六条 \(\bar D_n\) 上端严格负才接受；否则沿一个坐标的确切有理中点二分。两个闭子矩形并集等于母矩形，共享边界亦由严格包络覆盖。

有限区间覆盖包含 211241 个叶矩形，其有理面积精确为 \(2/25\)。独立检查从根矩形重建 422481 个二叉树节点、最大深度19，每个记录叶子恰出现一次，因此除面积外还排除了遗漏子树、内域重叠与端点空洞。本定理采用该完整闭树所覆盖的阶数区间。

完整证书中的更强有理余量蕴含下表；每次简化转化已用 Fraction 独立检查。

| 全紧化域的量 | 严格下界 |
|---|---:|
| \(\bar B_1,\bar B_2,\bar B_3\) | \(1/6000,\ 1/8000,\ 1/20000000000\) |
| \(-\bar D_1,-\bar D_2,-\bar D_3\) | \(1/30000,\ 1/2000000000,\ 1/6000\) |
| \(-\bar D_4,-\bar D_5,-\bar D_6\) | \(1/8000,\ 1/15000000,\ 1/100000\) |
| \(|\bar\Delta|^2\) | \(1/14400\) |

证明由严格区间包含与完整有限覆盖组成。补充材料给出区间算术实现、全部叶矩形及树结构检查，供逐项复核。

## 附录 C. 补充的全局指数界

对于 (2.4)，\(\xi_*\in AC\)，\(\xi_*'\ge0\)，\(V_0\le\xi_*\le\theta\)。标量正 resolvent 可由 (3.3) 的负最小值原理证明；也可使用 Simon [SimonCM2015] 的完全单调表示。定义
\[
A_\alpha(t)=(I^{1-\alpha}\xi_*)(t),\quad
q_\alpha(t)=A_\alpha'(t)
=\frac{V_0t^{-\alpha}}{\Gamma(1-\alpha)}+I^{1-\alpha}\xi_*'(t)\ge0.
\tag{C.1}
\]
两个启动指数 \(-\alpha,\alpha_0-\alpha\) 均大于 \(-1\)，故 \(q_\alpha\in L^1(0,T)\)。显式公式为
\[
q_\alpha(t)=\frac{V_0t^{-\alpha}}{\Gamma(1-\alpha)}
 +(\theta-V_0)\lambda_\xi t^{\alpha_0-\alpha}
 E_{\alpha_0,1+\alpha_0-\alpha}(-\lambda_\xi t^{\alpha_0}),
\tag{C.2}
\]
\[
A_\alpha(t)=\frac{\theta t^{1-\alpha}}{\Gamma(2-\alpha)}
 +(V_0-\theta)t^{1-\alpha}
 E_{\alpha_0,2-\alpha}(-\lambda_\xi t^{\alpha_0}),\quad A_\alpha(0)=0.
\tag{C.3}
\]
这里 \(E_{a,b}(z)=\sum_{n=0}^\infty z^n/\Gamma(an+b)\)。

**定理 C.1。** 对零初值 AC 轨迹 \(Z,\widehat Z\)，采用导数型指数
\[
L_T=\nu^{-1}\int_0^T\xi_*(T-t)D_t^\alpha Z(t)\,dt,\quad
\bar L_T=\nu^{-1}\int_0^T\xi_*(T-t)D_t^\alpha\widehat Z(t)\,dt,
\]
则
\[
L_T-\bar L_T=\nu^{-1}\int_0^Tq_\alpha(T-t)(Z-\widehat Z)(t)\,dt.
\tag{C.4}
\]
特别地，\(\sup|Z-\widehat Z|\le E\) 时
\[
|L_T-\bar L_T|\le\eta=E A_\alpha(T)/\nu
\le\frac{E\theta T^{1-\alpha}}{\nu\Gamma(2-\alpha)}.
\tag{C.5}
\]

**证明。** \(D_t^\alpha v=I^{1-\alpha}v'\)，绝对 Fubini 将指数积分变为
\(\nu^{-1}\int_0^TA_\alpha(T-t)v'(t)\,dt\)。
积分分部，因 \(A_\alpha(0)=v(0)=0\)，得到正核表示。绝对 Fubini 的条件来自 \(v'\in L^1\) 和连续有限曲线；再用 \(q_\alpha\ge0\) 及 \(\int q_\alpha=A_\alpha(T)\) 得结论。证毕。

若 \(\widehat Z=I^\alpha\bar G\)，\(\bar L=\nu^{-1}\int\xi_*\bar G\) 正是此导数型指数；不重复加残差积分。改用 \(\int\xi_*F(\widehat Z)\) 的代入型指数，则二者相差 \(\nu^{-1}\int\xi_*r_t\)，必须单独转换。本文数值对象全部使用导数型指数。

由 \(\operatorname{Re}L_T\le0\) 及指数积分恒等式，当 (C.5) 成立时
\[
|e^{L_T}-e^{\bar L_T}|
\le\min\{1,e^{\operatorname{Re}\bar L_T}\}(e^\eta-1).
\tag{C.6}
\]
第一种界从真指数为基点，第二种从近似指数为基点；取二者最小值合法。状态误差随频率可能变大，但在价格权重中，高频近似变换的衰减能够抵消一部分影响。

若另外已有模型变换包络 \(B(u)\) 及近似模上界 \(\widehat B(u)\)，则
\[
|e^{L_T}-e^{\bar L_T}|
\le\min\{B+\widehat B,\ \eta(B+\widehat B)/2\}.
\tag{C.7}
\]
第一项为三角不等式；第二项由
\((L_T-\bar L_T)\int_0^1e^{(1-\tau)\bar L_T+\tau L_T}d\tau\)
及凸性 \(e^{(1-\tau)a+\tau b}\le(1-\tau)e^a+\tau e^b\) 给出。它可与 (C.6) 取最小值，或与明确置零该节点的误差上界 \(B(u)\) 比较。计算时采用所列可用界的最小值。

## 参考文献

1. **GR2019.** Gatheral, Jim and Radoičić, Radoš. *Rational Approximation of the Rough Heston Solution*. International Journal of Theoretical and Applied Finance 22(3), 1950010, 2019. DOI [10.1142/S0219024919500109](https://doi.org/10.1142/S0219024919500109)。 使用2019年1月29日SSRN稿。

2. **GR2023v1.** Gatheral, Jim and Radoičić, Radoš. *A Generalization of the Rational Rough Heston Approximation*. 2023. [原文](https://arxiv.org/abs/2310.09181v1)。 使用版本：arXiv:2310.09181v1。

3. **JK2020.** Siow Woon Jeng and Adem Kiliçman. *Series Expansion and Fourth-Order Global Padé Approximation for a Rough Heston Solution*. Mathematics 8(11), 1968, 2020. DOI [10.3390/math8111968](https://doi.org/10.3390/math8111968)。

4. **JK2021.** Siow Woon Jeng and Adem Kiliçman. *SPX Calibration of Option Approximations under Rough Heston Model*. Mathematics 9(21), 2675, 2021. DOI [10.3390/math9212675](https://doi.org/10.3390/math9212675)。

5. **AbiJaberElEuch2018v1.** Abi Jaber, Eduardo and El Euch, Omar. *Markovian structure of the Volterra Heston model*. Statistics & Probability Letters 149, 63–72, 2019. DOI [10.1016/j.spl.2019.01.024](https://doi.org/10.1016/j.spl.2019.01.024)。 使用版本：arXiv:1803.00477v1。

6. **LiLiu2018.** Li, Lei and Liu, Jian-Guo. *A Generalized Definition of Caputo Derivatives and Its Application to Fractional ODEs*. SIAM Journal on Mathematical Analysis 50(3), 2867–2900, 2018. DOI [10.1137/17M1160318](https://doi.org/10.1137/17M1160318)。 凸性工具见命题3.11。

7. **Simon2014.** Simon, Thomas. *Comparing Fréchet and positive stable laws*. 2014. [原文](https://arxiv.org/abs/1310.1888v2)。 使用版本：arXiv:1310.1888v2。

8. **TrefethenWeideman2014.** Trefethen, Lloyd N. and Weideman, J. A. C. *The Exponentially Convergent Trapezoidal Rule*. SIAM Review 56(3), 385–458, 2014. DOI [10.1137/130932132](https://doi.org/10.1137/130932132)。 条带求积见定理5.1。

9. **NIST2010.** Olver, Frank W. J. and Lozier, Daniel W. and Boisvert, Ronald F. and Clark, Charles W. *NIST Handbook of Mathematical Functions*. Cambridge University Press, 2010. [原文](https://dlmf.nist.gov/)。

10. **BBWeak2023v1.** Bayer, Christian and Breneis, Simon. *Weak Markovian Approximations of Rough Heston*. 2023. [原始版本](https://arxiv.org/abs/2309.07023v1)，[原始 PDF](https://arxiv.org/pdf/2309.07023v1)。所读版本：arXiv:2309.07023v1，2023 年 9 月 13 日提交；特征函数与 European payoff 误差结果见定理 2.2、2.7。

11. **BBSimulation2023v1.** Bayer, Christian and Breneis, Simon. *Efficient option pricing in the rough Heston model using weak simulation schemes*. 2023. [原始版本](https://arxiv.org/abs/2310.04146v1)，[原始 PDF](https://arxiv.org/pdf/2310.04146v1)。所读版本：arXiv:2310.04146v1，2023 年 10 月 6 日提交；该版本页 4 将二阶弱收敛报告为数值观察。

12. **Kopteva2021v2.** Kopteva, Natalia. *Pointwise-in-time a posteriori error control for time-fractional parabolic equations*. Applied Mathematics Letters 123, 107515, 2022. DOI [10.1016/j.aml.2021.107515](https://doi.org/10.1016/j.aml.2021.107515)。[所读原始版本](https://arxiv.org/abs/2105.05848v2)，[原始 PDF](https://arxiv.org/pdf/2105.05848v2)：arXiv:2105.05848v2，2021 年 7 月 5 日修订；首次提交于 2021 年 5 月 12 日。逐时残差界与范数不等式见定理 2.2、引理 2.8。

13. **ElEuchRosenbaum2017v1.** El Euch, Omar and Rosenbaum, Mathieu. *Perfect hedging in rough Heston models*. arXiv:1703.05049v1, 2017. [Version](https://arxiv.org/abs/1703.05049v1). The analytical decreasing-curve example is not a new model-admissibility theorem.

14. **SimonCM2015.** Simon, Thomas. *Mittag-Leffler functions and complete monotonicity*. Integral Transforms and Special Functions 26(1), 36–50, 2015. DOI [10.1080/10652469.2014.965704](https://doi.org/10.1080/10652469.2014.965704). [Version](https://arxiv.org/abs/1312.4513v2).

15. **BL2025v1.** Boyarchenko, Svetlana; de Innocentis, Marco; and Levendorskii, Sergei. *Fast reliable pricing and calibration of the rough Heston model*. arXiv:2508.15080v1, 2025. [Version](https://arxiv.org/abs/2508.15080v1). Modified Adams is Section 3.2; Conformal Bootstrap is Section 4.10.

16. **BenHammouda2026v1.** Ben Hammouda, Chiheb; Ben Romdhane, Abderrahmene; Samet, Michael; and Tempone, Raul F. *Single- and Multilevel Quadrature with Error Control for Fourier Pricing under the Rough Heston Model*. arXiv:2609.00438v1, 2026. [Version](https://arxiv.org/abs/2609.00438v1). Practical tolerance interpretation: Section 3.2.

17. **HK2026v1.** Hager, Paul P. and Kreher, Dörte. *Expanding the rough Heston model in H*. arXiv:2606.16619v1, 2026. [Version](https://arxiv.org/abs/2606.16619v1).
