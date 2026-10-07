# Heston 模型的可验证联合定价误差：复残差、共同状态与金融判定

## 摘要

本文研究数值残差如何形成保留共同误差结构的价格外包集合，并据此认证价差估值、报价排除与有限候选选择。对粗糙 Heston 模型，固定 Gatheral–Radoičić 六条件两点三阶有理构造，在 \(\alpha\in[.52,.60]\)、\(\rho=-.7445\)、零 Riccati 均值回复上证明全部实频率的匹配非奇异、正时间分母实部为正及左半平面保持。复值 Caputo 凸性与单侧耗散将独立连续时间残差传至状态；正核特征指数表示、解析条带求积与真实尾界给出完整价格区间。对同一参数及期限的多个执行价，本文保留共同 Fourier 变换误差，以其复圆盘像构造联合价格集合，并显式平移到实际快速输出。对经典 Heston 的指定正部 Euler 链，误差模态受原离散链的共同方差状态概率约束；支持函数刻画方向界与严格收紧条件，非精确试验函数仍满足包含连续残差、离散缺陷、接口及终端项的有符号恒等式。两个模型的上游概率对象分别验证，在下游价格层统一。半年期十二执行价的固定 SPX 实验认证三候选 \(\alpha=.52,.60,.90\) 的唯一有限胜者为 \(.52\)；有限历史传播在同一实际输出下认证原价差的1指数点预算，并对28个预定组合与有符号边际界作完整预算比较。结果的适用范围由模型、轨迹、参数域与实际输出共同确定。

有限历史传播在同一快速输出下，将首选价差完整界从1.397613点收紧至0.378599点，逐时包络进一步至0.367258782点。新增512省略频率的完整认证和合法参考中心平移进一步给出0.115215934点，通过原快速输出的四分之一点任务。在相同新节点半径、0.5点预算下，联合方法通过28/28个预定组合，有符号边际通过13/28。第二个季度期限的完整改进取得联合0.233318843点、有符号边际0.252393939点，分别通过和未通过四分之一点预算，保留此前失败阶段；正分数阶曲线核条件明确。

**关键词：** Heston；粗糙波动率；连续残差；共同状态；联合价格误差；向外区间；有限候选。

## 1. 引言

价差估值和校准判断依赖多个价格同时成立的关系。单个价格的有效误差界不能说明这些误差是否能够同时取到最坏方向。本文的中心问题是：能否从独立可核验的数值残差出发，构造包含真实误差向量的集合，保留共享对象施加的约束，并将其转化为金融任务所需的方向界？

粗糙 Heston 提供一条连续残差路径：固定近似构造的代数结构、复值分数阶方程的耗散性和完整 Fourier 误差分析共同支撑价格包含。经典 Heston 提供另一条离散缺陷路径：多个模态在同一原链下使用共同状态概率，因而逐模态合法的残差组合仍须满足共同可行性。这两条路径进入统一的价格误差框架，但保持各自的模型律、误差符号和余项。

记连续模型价格为 \(c^*\)，实际快速输出为 \(c^{\rm fast}\)，参考值为 \(\bar c\)。全文用于实际定价验证的对象为 \(c^*-c^{\rm fast}\)。粗糙模型采用 \(c^*-\bar c\) 的共同变换误差及平移 \(\bar c-c^{\rm fast}\)。经典模型的望远镜身份按 \(p_Q-p_P\) 书写；用于实际输出的模型减算法误差时须反号。共同原链概率与连续过程占用概率分别处理，不因属于同一研究项目而等同。

### 1.1. 与已有研究的关系

Gatheral–Radoičić [GR2019, GR2023v1] 给出两端匹配有理近似及其均值回复推广，Jeng–Kiliçman [JK2020, JK2021] 研究全局 Padé 与公开 SPX 数据。本文分析的是既有三阶构造；原始行列式与 Cramer 分子的连续域符号验证承担结构性贡献。本文不将近似公式或两端匹配本身归为新方法。

Abi Jaber–El Euch [AbiJaberElEuch2018v1] 提供合法 Volterra 模型与仿射变换。Li–Liu [LiLiu2018] 的 Caputo 历史凸性、Mittag–Leffler 正性 [Simon2014] 和解析条带梯形规则 [TrefethenWeideman2014] 是误差传递的分析基础。这里需要补齐的是指定复方程的实部耗散、固定参考函数的连续残差和指定输出的完整价格预算。

经典 Heston、Euler 弱误差与指数可积性已有系统研究 [Heston1993, CozmaReisinger2016, MickelNeuenkirch2022v2]。矩信息与凸优化用于金融边界亦有先行工作 [BertsimasPopescu2002, BoydVandenberghe2004]。本文采用共同原链概率建立特定残差向量的外包含，并给出完整行的共同最大化见证与相位等号条件。支持函数及凸优化代数作为工具明确归属。

作者的先行 Asian 估值稿 [OuyangAsian2024] 研究指定模型下算术 Asian 的实现误差认证。本文引用其合约及变换背景；共同 Gaussian 平滑、十三个变换对象与本研究试验场的十三维基不作身份等同。

Bayer–Breneis 通过核的 L1 近似误差控制 Markovian 近似的特征函数与 European payoff 弱误差 [BBWeak2023v1]。其后续低维模拟方案报告了二阶弱收敛的数值观察 [BBSimulation2023v1]。本文考察固定的六条件有理实现：先证明原始匹配系统在指定参数域内的结构，再利用独立包围的连续时间残差认证参考轨迹，最后把共同 Fourier 节点扰动传到多个执行价与冻结实现输出。两类工作的近似对象与证据形式不同，其速度与精度比较须采用相同模型合同。

Caputo 凸性与逐时残差比较有既有理论基础 [LiLiu2018, Kopteva2021v2]。本文利用这些工具得到复 Riccati 分差的明确耗散率，并验证指定参考场所需的假设。联合误差部分采用标准支持函数运算 [BoydVandenberghe2004]，专门分析共同误差变量在完整定价实现中的位置，以及相应集合在指定价差与有限候选目标上的可核验界。


### 1.2. 贡献及证据边界

| 研究对象 | 本文保留或新增的结果 | 证据和金融作用 |
|---|---|---|
| 有限历史任务认证 | 完整历史的物理残差到指数传播与可靠升级 | 同输出1点突破、28组合完整公平比较 |
| 既有三阶有理构造 | 指定连续参数域的全频率结构定理 | 原始多项式、完整叶覆盖及可重算符号；确定可定义域 |
| 独立连续参考函数 | 复残差到状态、指数及完整价格的传递 | 固定系数、连续时间包络、求积与真实尾；认证价格 |
| 同参数多执行价输出 | 共同 Fourier 圆盘、中心平移和完整方向界 | 原节点半径及精确算术比较；认证原价差 |
| 经典正部 Euler 链 | 共同状态外包含与严格性判据 | 原 \(Q\) 矩界、102带及22行约束、精确见证 |
| 非精确试验函数 | 含四类贡献的有符号身份及显式合法例 | 真实迹、终值、可积权重和全年有限包络 |
| 固定参数剖面 | 三候选的严格模型排序及报价排除 | 36行价格、目标区间和实际快速输出 |

第2—8节给出粗糙模型的完整上游证明与固定候选实例；第9节建立实际多执行价输出的联合误差；第10节介绍经典模型的第二种共同状态实现，长推导保留于附录D；第11节汇总金融判定及完整价差比较；第12节规定可复核证据与成本；第13节陈述适用范围。附录保留概率模型、结构证书与原链包含证明。


## 2. 数学设定与既有六条件三阶构造

### 2.1. 方差模型、时间尺度和价格对象

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

### 2.2. 六条件 [3/3] 是被分析的既有对象

令 \(S=s_0-i\rho u=-d\)，\(A=\sqrt{S^2+2b}\) 取主根，\(R=A-S\)。短端和长端的三个系数分别为
\[
b_1=-\frac b{\Gamma(1+\alpha)},\quad
b_2=\frac{Sb}{\Gamma(1+2\alpha)},\quad
b_3=\frac{\Gamma(1+2\alpha)}{\Gamma(1+3\alpha)}
       (d b_2+b_1^2/2),
\tag{2.8}
\]
\[
g_0=-R,\quad g_1=\frac R{A\Gamma(1-\alpha)},\quad
g_2=-\frac R{A^2\Gamma(1-2\alpha)}
       +\frac{R^2}{2A^3\Gamma(1-\alpha)^2}.
\tag{2.9}
\]
对 \(1/2<\alpha<1\)，\(\Gamma(1-2\alpha)\) 为负且有限。Gatheral–Radoičić [GR2019] 的固定两端匹配构造要求
\[
\widehat H(y)=P(y)/Q(y),\quad
Q=1+q_1y+q_2y^2+q_3y^3,
\]
\[
\widehat H=b_1y+b_2y^2+b_3y^3+O(y^4),\quad
\widehat H=g_0+g_1y^{-1}+g_2y^{-2}+O(y^{-3}).
\tag{2.10}
\]
这六个条件给线性系统
\[
\begin{pmatrix}g_0&g_1&g_2\\b_1&-g_0&-g_1\\
b_2&b_1&-g_0\end{pmatrix}
\begin{pmatrix}q_1\\q_2\\q_3\end{pmatrix}
=\begin{pmatrix}b_1\\-b_2\\-b_3\end{pmatrix},
\quad p_1=b_1,\quad p_2=b_2+b_1q_1,\quad p_3=g_0q_3.
\tag{2.11}
\]
(2.8)–(2.11) 为既有构造。下文分别证明系统可逆、分母安全、轨迹半平面及独立参考场的真实解误差。

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
\tag{2.12}
\]
反射公式及递推关系给 \(b_1=-fb,b_2=f^2\mathsf d,b_3=f^3\mathsf c\)，\(g_1=V/f,g_2=W/f^2\)。注意后两式是除以 \(f,f^2\)。直接展开 (2.11) 的行列式和 Cramer 分子得到
\[
\begin{aligned}
\Delta={}&b^2W+2bRV-\mathsf dRW-\mathsf dV^2-R^3,\\
F_1={}&b^2V+b\mathsf dW-bR^2+\mathsf dRV+\mathsf cRW+\mathsf cV^2,\\
F_2={}&-b^2R+b\mathsf dV+b\mathsf cW+\mathsf d^2W+\mathsf dR^2+\mathsf cRV,\\
F_3={}&-b^3+2b\mathsf dR-b\mathsf cV-\mathsf d^2V+\mathsf cR^2.
\end{aligned}
\tag{2.13}
\]
\(\Delta\) 恰是原系统行列式，分子为 \(N_j=f^jF_j\)。只有证明 \(\Delta\ne0\) 后才可定义 \(q_j=N_j/\Delta\)，此时
\[
\Delta P=-fb\Delta y+f^2(\mathsf d\Delta-bF_1)y^2-f^3RF_3y^3,\quad
\Delta Q=\Delta+fF_1y+f^2F_2y^2+f^3F_3y^3.
\tag{2.14}
\]
恢复物理时间时，分母系数为 \(\nu^jq_j\)，不是重新定义 \(q_j\)。

## 3. 固定三阶构造的全频率结构定理

**定理 3.1（全频域结构）。** 对
\[
\alpha\in[13/25,3/5],\quad \rho=-1489/2000,\quad \kappa=0,\quad
u\in\mathbb R,\quad \nu>0,
\tag{3.1}
\]
既有 (2.11) 匹配系统非奇异。其规范分母满足
\[
\operatorname{Re}q_j>0\ (j=1,2,3),\qquad
\operatorname{Re}Q(y)\ge1,\quad |Q(y)|\ge1\quad(y\ge0).
\tag{3.2}
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
\tag{3.3}
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
式(3.3)将 \(\bar A-\bar S\) 写成倒数形式，其分母由当前参数直接确定。

以 \(\bar b=1/2\) 和 (3.3) 代入 (2.12)–(2.13)，得到带横线的原始量。按次数直接得到
\[
\Delta=\omega^3\bar\Delta,\qquad F_j=\omega^{3+j}\bar F_j.
\tag{3.4}
\]
定义三个实函数
\[
\bar B_j=\operatorname{Re}(\bar F_j\overline{\bar\Delta}).
\tag{3.5}
\]
附录 B 的严格有理覆盖证明，在整个闭矩形
\([13/25,3/5]\times[0,1]\) 上 \(\bar B_j>0\)，并且
\[
|\bar\Delta|^2\ge
\frac{88110801209184778874628745}{1267650600228229401496703205376}
>\frac1{14400}.
\tag{3.6}
\]
这一步先强制 \(\Delta\ne0\)，再给
\(\operatorname{Re}q_j=(f\omega)^j\bar B_j/|\bar\Delta|^2>0\)，因而得到 (3.2)。

为证明轨迹半平面，(2.14) 的有限卷积给
\[
|\Delta|^2\operatorname{Re}(P\overline Q)
=\sum_{n=1}^6 f^nD_ny^n,
\tag{3.7}
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
\tag{3.8}
\]
同一有理覆盖认证六个紧化量 \(\bar D_n<0\)；其尺度为 \(D_n=\omega^{7+n}\bar D_n\)。令 \(z=f\omega y\)，(3.7) 等于
\(\omega^7\sum_{n=1}^6\bar D_nz^n\)，故所有 \(y>0\) 上严格负。已证分母非零后，除以 \(|Q|^2|\Delta|^2\) 得 \(\operatorname{Re}\widehat H<0\)。负频率由主根、匹配系数的共轭对称性得到。闭端点 \(\eta=1\) 对应无穷频率极限，因此闭域证明覆盖全部有限频率。证毕。

系数实部正性给出分母无零点的充分条件。附录B列出计算机辅助证明所用的核心代数、基本函数余项和连续区间覆盖。

## 4. 复值耗散性和独立残差误差

### 4.1. 所需正则性、历史公式和凸性

若 \(H=I^\alpha F(H)\) 为有界局部连续解，则 \(H,F(H)\) 为 \(\alpha\)-Hölder。对 \(\alpha>1/2\)，写 \(q=F(H)\)，抵消后的导数公式为
\[
H'(x)=\frac{q(x)x^{\alpha-1}}{\Gamma(\alpha)}
 +\frac{\alpha-1}{\Gamma(\alpha)}
\int_0^x(x-t)^{\alpha-2}[q(t)-q(x)]\,dt.
\tag{4.1}
\]
近端指数 \(2\alpha-2>-1\)，远端及第一项可积，故 \(H\in AC\)，正时间局部 \(C^1\)。局部解由有界球上的 Volterra 收缩得到。对 \(v\in AC\) 且正时间局部 Lipschitz，积分分部给
\[
D_C^\alpha v(x)=\frac1{\Gamma(1-\alpha)}
\left\{\frac{v(x)-v(0)}{x^\alpha}
 +\alpha\int_0^x\frac{v(x)-v(t)}{(x-t)^{1+\alpha}}\,dt\right\}.
\tag{4.2}
\]
在全历史正最大值处、零初值时，该导数严格正。由此可证 \(D_C^\alpha v+s v\le D_C^\alpha w+s w\)、\(v(0)=w(0)\)、\(s\ge0\) 蕴含 \(v\le w\)。对于实二维 \(C^1\) 凸函数 \(\Phi\)，将切线不等式分别代入 (4.2) 的两项给
\[
D_C^\alpha\Phi(v)\le\nabla\Phi(v)\cdot D_C^\alpha v.
\tag{4.3}
\]
这是已有 Caputo 历史凸性，而非普通链式法则；使用 Li–Liu [LiLiu2018] 的 Proposition 3.11 的正则性范围，并在此直接重证所需版本。

### 4.2. 精确解的全局半平面

**引理 4.1。** 设 \(\alpha\in(1/2,1),|\rho|\le1,s_0\ge0\)。规范方程有唯一全局解，\(\operatorname{Re}H(x)<0\) 对 \(x>0\) 成立。若 \(s_0>0\)，
\[
|H(x)|\le\frac b{s_0}[1-E_\alpha(-s_0x^\alpha)]
\le\min\{b/s_0,bx^\alpha/\Gamma(1+\alpha)\}.
\tag{4.4}
\]
\(s_0=0\) 时保留后一时间上界。

**证明。** 写 \(H=X+iY\)，完全平方给
\[
\operatorname{Re}F(H)
=-\frac18-\frac{1-\rho^2}{2}u^2
-\frac12(Y+\rho u)^2-s_0X+\frac12X^2.
\tag{4.5}
\]
若 \(X\) 首次达到小正数 \(\varepsilon<1/2\)，(4.2) 导数为正，(4.5) 却负，矛盾。故 \(X\le0\)。正时间达到零时同样矛盾，因此严格负。

令 \(\psi_\epsilon(z)=\sqrt{|z|^2+\epsilon^2}-\epsilon\)。由 (4.3) 及
\[
\operatorname{Re}(\overline H F(H))
=-bX-s_0|H|^2+\tfrac12X|H|^2,\quad
\frac{|H|^2}{\sqrt{|H|^2+\epsilon^2}}\ge\psi_\epsilon(H),
\]
得 \(D_C^\alpha\psi_\epsilon(H)+s_0\psi_\epsilon(H)\le b\)。与零初值线性标量方程比较，令 \(\epsilon\downarrow0\)，得 (4.4)；标量解由 Mittag–Leffler 级数直接验证。若有限时爆炸，(4.4) 给有界轨迹、\(F(H)\) 有界和一致 Hölder 常数；历史积分在该端点有有限极限，局部收缩可延拓，矛盾。唯一性由逐段 Volterra 收缩给出。证毕。

### 4.3. 频率不进入稳定常数

**定理 4.2（耗散残差界）。** 设 \(s_0>0\)，\(\widehat H(0)=0\)，\(\widehat H\in AC\) 且正时间局部 Lipschitz。若在全部 \(x\in(0,X]\) 上
\[
\operatorname{Re}\widehat H\le\epsilon_R<2s_0,\qquad
|D_C^\alpha\widehat H-F(\widehat H)|\le\delta,
\]
令 \(\sigma=s_0-\epsilon_R/2>0\)，则
\[
|H-\widehat H|
\le\frac\delta\sigma[1-E_\alpha(-\sigma x^\alpha)]
\le\delta/\sigma.
\tag{4.6}
\]
特别地，左半平面轨迹可取 \(\epsilon_R=0,\sigma=s_0\)，不要求 \(\delta\) 小或 \(u\) 小。

**证明。** \(e=H-\widehat H\) 满足
\[
D_C^\alpha e=\left(d+\frac{H+\widehat H}{2}\right)e-r,\quad e(0)=0,\quad
\operatorname{Re}\left(d+\frac{H+\widehat H}{2}\right)\le-\sigma.
\]
对 \(\psi_\epsilon(e)\) 用 (4.3)，得
\(D_C^\alpha\psi_\epsilon(e)+\sigma\psi_\epsilon(e)\le|r|\le\delta\)。
与线性标量解比较并令 \(\epsilon\downarrow0\) 即得。凸正则化适用于零误差，并对复二维误差成立。证毕。

如果 \(\widehat H\) 是物理时间轨迹 \(\widehat Z\)，认证 \(|r_t|/\nu\le\delta_F\)，同一结论为
\[
\sup_{t\le T}|Z-\widehat Z|\le\delta_F/s_0
\quad\text{if }\operatorname{Re}\widehat Z\le0.
\tag{4.7}
\]
本实验 \(s_0=1489/4000\)。该耗散率控制复值误差模长；独立残差 \(\delta_F\) 由第 7 节提供。这里使用已有凸性工具，建立本题的具体误差传递。

**补充命题 4.3（不预设近似半平面的半径）。** 若 \(\delta_F<s_0^2/2\)，则任意同初值合法轨迹满足
\[
|Z-\widehat Z|\le E_\delta
=s_0-\sqrt{s_0^2-2\delta_F}
=\frac{2\delta_F}{s_0+\sqrt{s_0^2-2\delta_F}}.
\tag{4.8}
\]
证明中把误差线性项改写成 \((d+Z)e-e^2/2\)，精确解半平面给
\(D_t^\alpha|e|\le\nu(-s_0|e|+|e|^2/2+\delta_F)\)，以同一凸模长正则化解释。任取 \(E_\delta<\ell<s_0+\sqrt{s_0^2-2\delta_F}\)，右端在 \(|e|=\ell\) 严格负；首次达到 \(\ell\) 与 (4.2) 矛盾。令 \(\ell\downarrow E_\delta\) 得结论。不满足这个充分条件并不意味着实际误差或极点存在。本文完成的节点场已证半平面，使用 (4.7)，不被 (4.8) 门槛限制。

## 5. 导数型特征指数的正核误差传递

对于 (2.4)，\(\xi_*\in AC\)，\(\xi_*'\ge0\)，\(V_0\le\xi_*\le\theta\)。标量正 resolvent 可由 (4.2) 的负最小值原理证明；也可使用 Simon [Simon2014] 的完全单调表示。定义
\[
A_\alpha(t)=(I^{1-\alpha}\xi_*)(t),\quad
q_\alpha(t)=A_\alpha'(t)
=\frac{V_0t^{-\alpha}}{\Gamma(1-\alpha)}+I^{1-\alpha}\xi_*'(t)\ge0.
\tag{5.1}
\]
两个启动指数 \(-\alpha,\alpha_0-\alpha\) 均大于 \(-1\)，故 \(q_\alpha\in L^1(0,T)\)。显式公式为
\[
q_\alpha(t)=\frac{V_0t^{-\alpha}}{\Gamma(1-\alpha)}
 +(\theta-V_0)\lambda_\xi t^{\alpha_0-\alpha}
 E_{\alpha_0,1+\alpha_0-\alpha}(-\lambda_\xi t^{\alpha_0}),
\tag{5.2}
\]
\[
A_\alpha(t)=\frac{\theta t^{1-\alpha}}{\Gamma(2-\alpha)}
 +(V_0-\theta)t^{1-\alpha}
 E_{\alpha_0,2-\alpha}(-\lambda_\xi t^{\alpha_0}),\quad A_\alpha(0)=0.
\tag{5.3}
\]
这里 \(E_{a,b}(z)=\sum_{n=0}^\infty z^n/\Gamma(an+b)\)。

**定理 5.1。** 对零初值 AC 轨迹 \(Z,\widehat Z\)，采用导数型指数
\[
L_T=\nu^{-1}\int_0^T\xi_*(T-t)D_t^\alpha Z(t)\,dt,\quad
\bar L_T=\nu^{-1}\int_0^T\xi_*(T-t)D_t^\alpha\widehat Z(t)\,dt,
\]
则
\[
L_T-\bar L_T=\nu^{-1}\int_0^Tq_\alpha(T-t)(Z-\widehat Z)(t)\,dt.
\tag{5.4}
\]
特别地，\(\sup|Z-\widehat Z|\le E\) 时
\[
|L_T-\bar L_T|\le\eta=E A_\alpha(T)/\nu
\le\frac{E\theta T^{1-\alpha}}{\nu\Gamma(2-\alpha)}.
\tag{5.5}
\]

**证明。** \(D_t^\alpha v=I^{1-\alpha}v'\)，绝对 Fubini 将指数积分变为
\(\nu^{-1}\int_0^TA_\alpha(T-t)v'(t)\,dt\)。
积分分部，因 \(A_\alpha(0)=v(0)=0\)，得到正核表示。绝对 Fubini 的条件来自 \(v'\in L^1\) 和连续有限曲线；再用 \(q_\alpha\ge0\) 及 \(\int q_\alpha=A_\alpha(T)\) 得结论。证毕。

若 \(\widehat Z=I^\alpha\bar G\)，\(\bar L=\nu^{-1}\int\xi_*\bar G\) 正是此导数型指数；不重复加残差积分。改用 \(\int\xi_*F(\widehat Z)\) 的代入型指数，则二者相差 \(\nu^{-1}\int\xi_*r_t\)，必须单独转换。本文数值对象全部使用导数型指数。

由 \(\operatorname{Re}L_T\le0\) 及指数积分恒等式，当 (5.5) 成立时
\[
|e^{L_T}-e^{\bar L_T}|
\le\min\{1,e^{\operatorname{Re}\bar L_T}\}(e^\eta-1).
\tag{5.6}
\]
第一种界从真指数为基点，第二种从近似指数为基点；取二者最小值合法。状态误差随频率可能变大，但在价格权重中，高频近似变换的衰减能够抵消一部分影响。

若另外已有模型变换包络 \(B(u)\) 及近似模上界 \(\widehat B(u)\)，则
\[
|e^{L_T}-e^{\bar L_T}|
\le\min\{B+\widehat B,\ \eta(B+\widehat B)/2\}.
\tag{5.7}
\]
第一项为三角不等式；第二项由
\((L_T-\bar L_T)\int_0^1e^{(1-\tau)\bar L_T+\tau L_T}d\tau\)
及凸性 \(e^{(1-\tau)a+\tau b}\le(1-\tau)e^a+\tau e^b\) 给出。它可与 (5.6) 取最小值，或与明确置零该节点的误差上界 \(B(u)\) 比较。计算时采用所列可用界的最小值。

## 6. 连续 Fourier 积分、离散网格与真实无限尾

### 6.1. 解析条带的严格离散化

**定理 6.1。** 设 \(M_T>0,\mathbb E M_T=1\)，任取 \(0<a_*<1/2,h_*>0\)，令
\(g(z)=e^{-ikz}\phi_T(z-i/2)/(z^2+1/4)\)。则以无限梯形求和代替 (2.7) 的价格误差不超过
\[
\epsilon_{\rm grid}
=\frac{\sqrt m\,e^{a_*|k|}}
{(1/2-a_*)(e^{2\pi a_*/h_*}-1)}.
\tag{6.1}
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
共轭对称把双边积分与和各减半，乘以 \(\sqrt m/\pi\) 得 (6.1)。证毕。

这是 Trefethen–Weideman [TrefethenWeideman2014] 的解析条带梯形理论的具体应用。价格节点采用各自的连续时间残差界，节点间求积误差则由解析条带控制。

### 6.2. 直接控制真实 Lewis 解的高频实部

固定 \(\kappa=0,-1<\rho<0\)。令 \(X=-\operatorname{Re}H\ge0\)，(4.5) 给
\[
D_x^\alpha X\ge\beta_u-s_0X-X^2/2,\quad
\beta_u=(1-\rho^2)u^2/2+1/8.
\tag{6.2}
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
\tag{6.3}
\]
比较论证使用全历史正最大值。

取 \(V>s_0/\sqrt{1-\rho^2}\)，置
\[
a_\rho=\sqrt{1-\rho^2},\quad b_V=a_\rho-s_0/V>0,\quad
f_\alpha(z)=z/(\Gamma(1+\alpha)+z).
\]
对 \(u\ge V\)，\(R_u/u\ge b_V,\ell_u\ge a_\rho u/2\)。任取 \(J\ge2\) 的分格 \(0=t_0<\cdots<t_J=T\)，由正核 (5.4) 及单调 \(f_\alpha\) 得
\[
c_V=\frac{b_V}{\nu}\sum_{j=0}^{J-1}
 f_\alpha(a_\rho\nu Vt_j^\alpha/2)
 [A_\alpha(T-t_j)-A_\alpha(T-t_{j+1})]>0,
\]
\[
|\phi_T(u-i/2)|\le e^{-c_Vu}\quad(u\ge V).
\tag{6.4}
\]
该包络对所有连续高频成立；时间划分用于构造正测度积分的下和。本实验取 \(J=64\)，以严格区间给 \(c_V\) 的正有理下界。端点 \(A_\alpha(0)=0\) 不作奇异求值。两个不同侧端点之差
\([A_{\rm lo}(T-t_j)-A_{\rm hi}(T-t_{j+1})]_+\)
是合法质量下界。

由正递减函数的右端和，对 \(V=Nh_*\)，真实离散尾的归一化价格预算为
\[
\epsilon_{\rm tail}
\le\frac{\sqrt m}{\pi}\frac{e^{-c_VV}}{c_VV^2}.
\tag{6.5}
\]
积分尾项使用精确解的包络。取零的有限节点同样按该包络计入误差，因而整个频率范围均有明确的误差项。

### 6.3. 完整价格预算

若节点值 \(\widehat\phi_n\) 给真实误差 \(\varepsilon_n\)，有限价格和
\[
\widehat c_N=1-\frac{h_*\sqrt m}{\pi}
\left(2\operatorname{Re}\widehat\phi_0+
\sum_{n=1}^N\frac{\operatorname{Re}(e^{-inh_*k}\widehat\phi_n)}
{(nh_*)^2+1/4}\right)
\tag{6.6}
\]
满足
\[
|c-\widehat c_N|\le\epsilon_{\rm grid}+\epsilon_{\rm tail}
 +\frac{h_*\sqrt m}{\pi}
\left(2\varepsilon_0+
\sum_{n=1}^N\frac{\varepsilon_n}{(nh_*)^2+1/4}\right)
 +\epsilon_{\rm arithmetic}.
\tag{6.7}
\]
系数 \(2\) 是 \(u=0\) 处梯形半权与分母 \(1/4\) 的乘积。相位、平方根、指数和有限求和的舍入误差均由严格区间包含。本文 \(h_*=1/8,a_*=9/20,N=1024\)，前 \(513\) 个节点 \(u\le64\) 使用独立残差，余下节点用真实包络、近似值零；\(u>128\) 使用 (6.5)。这一混合规则将节点误差与尾项共同纳入价格估计。

## 7. 固定参考场的连续时间残差证书

### 7.1. 认证对象和启动端

对每个候选点 \(\alpha=\beta\in\{.52,.6,.9\}\) 及每个 \(u=n/8,\ n=0,\ldots,512\)，保存
\[
\bar G(t)=\nu c_0+A_1t^\beta+A_2t^{2\beta}+\bar L(t),\quad
c_0=-(u^2+1/4)/2,\quad \widehat Z=I^\alpha\bar G,\quad T=1/2.
\tag{7.1}
\]
\(\bar L\) 为节点 \((t_j,L_j)\) 的连续物理时间线性插值，\(L_0=0\)。节点及复系数按其binary64表示对应的精确二进有理数解释。该参考轨迹的连续时间误差由下列独立残差控制
\[
r_t=\bar G-\nu F(\widehat Z),\quad
\delta_F=\nu^{-1}\sup_{0\le t\le T}|r_t|.
\tag{7.2}
\]
式(7.1)定义完整的绝对连续参考轨迹。其独立残差给出模型价格区间，再据此估计所选[3/3]流程的输出误差。

写
\[
\widehat Z=H_0+J,\quad J=I^\alpha\bar L,\quad
H_0=B_1t^\alpha+B_2t^{\alpha+\beta}+B_3t^{\alpha+2\beta},
\]
\[
B_1=\frac{\nu c_0}{\Gamma(1+\alpha)},\quad
B_2=\frac{A_1\Gamma(1+\beta)}{\Gamma(1+\alpha+\beta)},\quad
B_3=\frac{A_2\Gamma(1+2\beta)}{\Gamma(1+\alpha+2\beta)}.
\tag{7.3}
\]
首单元 \(J=L_1t^{\alpha+1}/[t_1\Gamma(2+\alpha)]\)。将全部广义幂代入 (7.2)，先精确抵消 \(\nu c_0\)，合并相同幂，再取 \(\sum_p|r_p|t_1^p\)。所有 \(p>0\)，这是整个首闭单元的上界；广义幂展开保留了分数阶启动行为。

### 7.2. 其余时间单元的严格积分与导数界

在源单元 \([a,b]\subset[0,q]\)，令 \(\tau=q-a,h=b-a\)，线性帽函数的积分权重为
\[
I_0=\{\tau^\alpha-(\tau-h)^\alpha\}/\alpha,\quad
I_1=\{\tau^{\alpha+1}-(\tau-h)^{\alpha+1}\}/(\alpha+1),
\]
\[
w_R=(\tau I_0-I_1)/(h\Gamma(\alpha)),\quad
w_L=I_0/\Gamma(\alpha)-w_R.
\tag{7.4}
\]
权重非负。截断单元的端点按原单元 affine 插值恢复；末单元 \(b=q\) 可直接用
\(w_R=h^\alpha/[\alpha(\alpha+1)\Gamma(\alpha)],w_L=\alpha w_R\)。
对 \(h/\tau<.01\)，保留正级数八项，分别使用
\[
w_R=\frac{h\tau^{\alpha-1}}{\Gamma(\alpha)}
\sum_{k\ge0}\frac{(1-\alpha)_k(h/\tau)^k}{k!(k+2)},\quad
w_L=\frac{h\tau^{\alpha-1}}{\Gamma(\alpha)}
\sum_{k\ge0}\frac{(1-\alpha)_k(h/\tau)^k}{k!(k+1)(k+2)}.
\tag{7.5}
\]
无尺度尾各不超过 \(z^8/(1-z)\)，因为 \(0<(1-\alpha)_k/k!\le1\)。这减少近等端点相减造成的区间膨胀，不使用浮点求积替代历史积分。

每个非首原单元二分为四个闭子单元 \([a,b]\)，选保存 二进有理数 中心 \(m\)。若已有整个子单元导数界，则
\[
\sup_{[a,b]}|r_t|\le|r_t(m)|+\max(m-a,b-m)\sup_{[a,b]}|r_t'|.
\tag{7.6}
\]
原节点处残差的普通导数可能不连续，以下导数上界均在几乎处处的意义下成立；残差绝对连续及积分基本定理仍给 (7.6)。全部导数上界通过以下三个恒等式分别建立并取最小值：
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
\tag{7.7}
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
\tag{7.8}
\]
当 \(a=t_1\) 第一上界舍弃，第二上界由完整 Euler Beta 积分得到且有限；下界及第一上界由端点核单调性给出。所有 \(p,\alpha>0\)，经典 Beta 公式假设成立。

用同一 \(\widehat Z'\) 包络与严格点值，认证所有非首子单元的 \(\operatorname{Re}\widehat Z\) 上界。首单元写成 \(t^\alpha\) 乘有限括号，使用负常数项和其余正部的端点贡献。只有全部闭单元实部上端不正时才启用 (4.7)。这里的启用条件覆盖整个闭时间单元。

### 7.3. 算术证明与明确浮点运算假设

结构证书和特殊函数采用端点为整数除以 \(2^{100}\) 的外舍入区间。残差批量权重采用 IEEE binary64，每步基本运算用相邻可表示数向外扩；Gamma 从精确有理包络转换后用 Fraction 比较端点。log 使用二进制精确缩放与 \(z\in[0,1/3]\) 的二十二项 atanh 级数，尾为 \(2z^{45}/[45(1-z^2)]\)。exp 缩放后 \(|r|<1\)，24阶 Taylor 尾为 \(3/25!\)。log、exp和非整数幂分别采用上述显式余项构造区间。

矩阵乘法对严格权重中心 \(W_c\)、半径 \(W_r\) 和保存 二进有理数 值 \(X\) 加入
\[
\left(\gamma_{2n}\|W_c\|_{1,\mathrm{row}}+
\|W_r\|_{1,\mathrm{row}}\right)\|X\|_{\infty,\mathrm{column}},
\quad \gamma_{2n}=\frac{2n\,2^{-53}}{1-2n\,2^{-53}},
\tag{7.9}
\]
再加 下溢误差 预算。该界由基本舍入因子乘积的归纳估计得到，允许不同加法结合顺序；范数求和也外扩。计算采用IEEE基本运算的最近舍入、平方根的正确舍入和渐进下溢，并要求运算过程无溢出或NaN。源码与计算版本见补充材料；本节的包含结论以这些运算假设及所列余项界为依据。

### 7.4. 同一场的指数积分与有效权重

对固定曲线定义
\[
J_0(z)=\theta z+(V_0-\theta)zE_{\alpha_0,2}(-\lambda_\xi z^{\alpha_0}),\quad
J_1(z)=\theta z^2/2+
(V_0-\theta)z^2(E_{\alpha_0,2}-E_{\alpha_0,3})(-\lambda_\xi z^{\alpha_0}).
\tag{7.10}
\]
它们分别为 \(\int_0^z\xi_*(s)ds,\int_0^zs\xi_*(s)ds\)；后式由逐项积分验证。若线性场单元为 \([a,b]\)，\(A=T-b,B=T-a\)，严格非负指数权重为
\[
w_l=\frac{J_1(B)-J_1(A)-A[J_0(B)-J_0(A)]}{b-a},\quad
w_r=\frac{B[J_0(B)-J_0(A)]-J_1(B)+J_1(A)}{b-a}.
\tag{7.11}
\]
幂场 \(t^\beta\) 的曲线矩为
\[
\int_0^T\xi_*(T-t)t^\beta dt
=\frac{\theta T^{\beta+1}}{\beta+1}
 +(V_0-\theta)\Gamma(\beta+1)T^{\beta+1}
 E_{\alpha_0,\beta+2}(-\lambda_\xi T^{\alpha_0}).
\tag{7.12}
\]
由级数和 Beta 积分可直接得到。结合 (7.1)，\(\bar L\) 为严格有限和。三角相位与复指数也使用有限 Taylor 及显式尾。Mittag–Leffler级数的尾项在本期限 \(z=\lambda_\xi T^{\alpha_0}<1\) 时可取 \(3z^{64}/(1-z)\)，因为所有 Gamma 参数大于一且 Euler 积分给 \(\Gamma(\gamma)\ge e^{-1}>1/3\)。严格积分给出近似指数的区间；模型指数与近似指数之差由式(5.5)控制。

## 8. 有限候选粗糙度选择与实际三阶流程的稳定性

### 8.1. 报价定义与有限候选

本文采用公开常态 SPX 样本中数学期限 \(T=1/2\) 的十二行报价，行权价从3700至4800、步长100。原始 CSV 固定在 WoonJeng 数据仓库 commit860049da2b7486fe8aa509061eff23cc28c2ef89。市场买价、卖价隐含波动率列与作者模型计算列分别标识；本节使用市场报价列定义目标，模型价格区间由正文的误差分析得到。

取 \(D=1,F=4221.86\) 下的归一化看涨期权实验。CSV 的 IV 与 T 十进制值作为实验输入的确切有理数；报价 bid/ask IV 经标准 Black–Scholes 公式变为 \(B_i,A_i\)，目标是价格中点 \(M_i=(B_i+A_i)/2\)，不是把报告的 mid-IV 再代入公式。这些输入共同定义下文的归一化报价设定。

固定 \(\rho=-.7445,\nu=.2897,\lambda_R=\kappa=0\)，整条远期方差函数为
\[
\xi_*(t)=.0721+(.0262-.0721)
E_{.5286}(-.5037t^{.5286}).
\tag{8.1}
\]
曲线指数 .5286 和曲线参数 .5037 始终固定；候选 \(\alpha\) 变化时不重新计算曲线，也不把 .5037 代入 Riccati 的均值回复。以上数值来自 [JK2021] 的已发表舍入拟合参数，在本文中用于定义其余输入固定的候选比较。

候选集合为
\[
\Theta_{\rm finite}=\{13/25,3/5,9/10\},\qquad
H=\alpha-\tfrac12\in\{.02,.1,.4\}.
\tag{8.2}
\]
这是其余参数和全部曲线固定的条件目标剖面。阈值 \(H_c=.1\) 只区分本次较低与较高 H 候选；三个候选本身均有 \(H<.5\)，不是粗糙模型与经典 Heston 的二分类。本节的量词为 (8.2) 的完整三候选集合。

模型价格 \(c_i(\alpha)=C_i(\alpha)/(DF)\) 来自合法正 Volterra 方差模型及其真实仿射变换。AbiJaberElEuch2018v1 的模型/核条件在本文已逐项验证；不把有理式无极点当作概率模型合法性。目标为
\[
J(\alpha)=\frac1{24}\sum_{i=1}^{12}
 [c_i(\alpha)-M_i]^2,\qquad
J_{\rm band}(\alpha)=\frac1{24}\sum_{i=1}^{12}
 \operatorname{dist}(c_i(\alpha),[B_i,A_i])^2.
\tag{8.3}
\]
因此归一化价格 RMS 是 \(\sqrt{2J}\)，不是 \(\sqrt{J/6}\)；同一归一化约定适用于目标区间、有限间隙与稳定性常数。

### 8.2. 模型价格区间到有限全局结论：完整定理

**定理 8.1（有限目标区间与选择稳定性）。** 对每个 \(\alpha_j\in\Theta_{\rm finite}\)，设全部模型价格都有已认证包络
\[
c_i(\alpha_j)\in[p^-_{ij},p^+_{ij}],\quad
B_i\in[b_i^-,b_i^+],\quad
A_i\in[a_i^-,a_i^+],\quad
M_i\in[m_i^-,m_i^+].
\tag{8.4}
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
\tag{8.5}
\]
则 \(J(\alpha_j)\in[L_j,U_j]\)。记 \(L_*=\min_jL_j,U_*=\min_jU_j\)，真有限最优值满足
\[
J_*=\min_{\Theta_{\rm finite}}J\in[L_*,U_*].
\tag{8.6}
\]
对 \(\varepsilon\ge0\)，全部真 \(\varepsilon\) 近最优候选都在
\[
\{\alpha_j:L_j\le U_*+\varepsilon\};
\tag{8.7}
\]
条件 \(U_j-L_*\le\varepsilon\) 则充分保证该候选真近最优。若
\[
g:=\min_{j\ne j_0}L_j-U_{j_0}>0,
\tag{8.8}
\]
则 \(\alpha_{j_0}\) 是唯一模型目标的有限最优解。若
\[
\min_{\alpha_j\ge.6}L_j>U_*+\varepsilon,
\tag{8.9}
\]
则所有有限真近最优候选满足 \(\alpha_j<.6\)。

报价相容性另作判定：任一行满足 \(p^+_{ij}<b_i^-\) 或 \(p^-_{ij}>a_i^+\)，可排除该候选同时落在全部报价带内；若每行都有 \(p^-_{ij}\ge b_i^+\) 且 \(p^+_{ij}\le a_i^-\)，则该候选充分认证为报价相容。区间重叠而未满足内带条件只保留“可能相容”，不称相容成立。

**证明。** 真差 \(c_i-M_i\) 位于(8.5)使用的闭区间内。平方的闭区间最小值为 \(\ell\)，最大值为 \(v\)，故加权和给每个 \(J_j\) 的包络。每个 \(J_j\ge L_j\ge L_*\)，而取得最小 \(U_j\) 的候选给 \(J_*\le J_j\le U_*\)，得到(8.6)。若 \(J_j\le J_*+\varepsilon\)，则 \(L_j\le J_j\le U_*+\varepsilon\)，得(8.7)。反之 \(J_j-J_*\le U_j-L_*\)，给所列充分内条件。(8.8)使任一竞争者满足 \(J_j-J_{j_0}\ge L_j-U_{j_0}\ge g>0\)，故唯一。(8.9)使每个选定较高 H 候选的模型目标超过 \(J_*+\varepsilon\)，所以排除。以上并不要求报价误差在不同候选间独立。

若 \(p^+<b^-\)，真实 \(c<B\)；若 \(p^->a^+\)，真实 \(c>A\)，任一行即破坏全行相容。相反，内带条件给 \(B\le b^+\le c\le a^-\le A\)。逐行应用即得相容性声明。证毕。

**目标扰动推论。** 若额外算法目标 \(\widetilde J\) 满足
\(\sup_{\Theta_{\rm finite}}|\widetilde J-J|\le\delta_J\)，且所选候选对其为 \(\varepsilon_{\rm alg}\) 近最优，则
\[
J(\widehat\alpha)-J_*
\le2\delta_J+\varepsilon_{\rm alg}.
\tag{8.10}
\]
证明为 \(J(\widehat\alpha)\le\widetilde J(\widehat\alpha)+\delta_J
\le\min\widetilde J+\varepsilon_{\rm alg}+\delta_J
\le J_*+2\delta_J+\varepsilon_{\rm alg}\)。
如(8.8)的严格间隙 \(g>2\delta_J+\varepsilon_{\rm alg}\)，只能选择该唯一有限胜者。这是由有限目标间隙产生的选择稳定性，适用于 (8.2) 的固定候选集合。

### 8.3. 参考计算与误差分解

每个候选分别使用自写 PI 流程生成并固定物理时间场
\(\bar G=\nu c_0+A_1t^\beta+A_2t^{2\beta}+\bar L\)，其中 \(\beta=\alpha_j\)，节点和系数按保存的精确二进有理数值解释。认证对象为 \(\widehat Z=I^\alpha\bar G\)，不是把浮点 PI 节点直接当精确解。首时间单元采用完整广义幂残差展开；其余闭时间单元采用严格卷积导数及中值定理包络，覆盖全部 \(t\in[0,1/2]\)。逐 Fourier 节点的物理残差除以确切 \(\nu\) 后进入已证误差屏障或已认证半平面线性误差界。

保存指数是导数型 \(\bar L_T=\nu^{-1}\int\xi_*(T-t)\bar G(t)dt\)。正核 \(q_\alpha=(I^{1-\alpha}\xi_*)'\ge0\) 给
\[
|L_T-\bar L_T|
\le E_\delta(I^{1-\alpha}\xi_*)(T)/\nu
\le E_\delta\theta T^{1-\alpha}/[\nu\Gamma(2-\alpha)].
\tag{8.11}
\]
此处不重复附加残差积分。固定曲线的 Gamma/ML 矩、场积分、指数、相位及求和均以100bit向外有理区间计算。

价格正半轴规则固定 \(h=1/8\)，解析条带 \(a=9/20\)。保存场在可用的 \(u=0:1/8:64\) 节点使用实际残差证书；64之后至128的近似变换明确取0，并逐节点计入真实变换包络；128之后的无限离散规则尾由已证连续积分包络控制。真实实部 Riccati 下比较与整条正核曲线的64格下和给高频包络，不依赖经验外推。解析条带梯形误差单独估计；全轴积分到正半轴积分及零节点半权已严格处理。由此得到下面全部十二行的模型价格包络，而不是网格收敛差或Richardson诊断。

### 8.4. 完成的目标比较与报价相容性

| α | H | 真 J 严格区间 | 模型价格 RMS 严格区间 | 实际 Padé 输出 J 严格区间 |
|---|---|---|---|---|
| 0.52 | 0.02 | [0.0000000068962, 0.0000001833669] | [0.00011744, 0.00060559] | [0.0000000708602, 0.0000000708603] |
| 0.60 | 0.10 | [0.0000004535720, 0.0000006021720] | [0.00095244, 0.00109743] | [0.0000006127366, 0.0000006127367] |
| 0.90 | 0.40 | [0.0000082343900, 0.0000083484458] | [0.00405817, 0.00408619] | [0.0000081393603, 0.0000081393604] |

所有表端点按有理数向外取十进制；判定使用未截断的精确有理数端点。 模型目标的唯一最优候选为 α=0.52、H=0.02，竞争者目标与胜者的统一严格间隙下界为 0.0000002702052。 实际 Padé 数值输出的唯一有限最优解 与模型目标的有限最优解 相同，已严格认证。

ε=0 时真最优候选外集合为 \(\{13/25\}\)；所选 α≥.6 较高 H 候选与该最优值严格分离。

| α | 真 J_band 严格区间 | 严格排除报价相容的行号 | 充分认证全部报价相容 |
|---|---|---|---|
| 0.52 | [0.0000000005732, 0.0000000877280] | [8, 9] | 否 |
| 0.60 | [0.0000003444775, 0.0000004648236] | [5, 6, 7, 8, 9, 10, 11] | 否 |
| 0.90 | [0.0000076345237, 0.0000077422463] | [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] | 否 |

最小二乘排序与报价相容性分别由目标区间和逐行价格区间判定。下表同时报告这两项模型验证结果。

### 8.5. 全十二价及实际数值流程的总误差

#### α=0.52，H=0.02

| K | 报价价格中点严格区间 | 真 normalized 价严格区间 | 实际 Padé 二进有理数 输出（显示值） | 该输出对真价总误差上界 |
|---|---|---|---|---|
| 3700 | [0.13916863, 0.13916864] | [0.13882872, 0.13937153] | 0.13910887 | 0.00028016 |
| 3800 | [0.11921230, 0.11921231] | [0.11858902, 0.11913912] | 0.11888921 | 0.00030019 |
| 3900 | [0.09981335, 0.09981336] | [0.09909480, 0.09965209] | 0.09943278 | 0.00033799 |
| 4000 | [0.08123198, 0.08123199] | [0.08055552, 0.08111992] | 0.08092667 | 0.00037115 |
| 4100 | [0.06371452, 0.06371453] | [0.06322696, 0.06379836] | 0.06361496 | 0.00038801 |
| 4200 | [0.04759685, 0.04759686] | [0.04740368, 0.04798201] | 0.04781654 | 0.00041287 |
| 4300 | [0.03333802, 0.03333803] | [0.03349166, 0.03407684] | 0.03393723 | 0.00044558 |
| 4400 | [0.02173166, 0.02173167] | [0.02200137, 0.02259332] | 0.02244498 | 0.00044361 |
| 4500 | [0.01316937, 0.01316938] | [0.01332823, 0.01392686] | 0.01373568 | 0.00040746 |
| 4600 | [0.00760335, 0.00760336] | [0.00746696, 0.00807221] | 0.00785225 | 0.00038529 |
| 4700 | [0.00434644, 0.00434645] | [0.00393703, 0.00454881] | 0.00430503 | 0.00036801 |
| 4800 | [0.00253419, 0.00253420] | [0.00199815, 0.00261641] | 0.00232396 | 0.00032582 |

#### α=0.60，H=0.10

| K | 报价价格中点严格区间 | 真 normalized 价严格区间 | 实际 Padé 二进有理数 输出（显示值） | 该输出对真价总误差上界 |
|---|---|---|---|---|
| 3700 | [0.13916863, 0.13916864] | [0.13908096, 0.13925890] | 0.13914793 | 0.00011096 |
| 3800 | [0.11921230, 0.11921231] | [0.11900101, 0.11918134] | 0.11908020 | 0.00010114 |
| 3900 | [0.09981335, 0.09981336] | [0.09970355, 0.09988623] | 0.09981101 | 0.00010746 |
| 4000 | [0.08123198, 0.08123199] | [0.08138513, 0.08157015] | 0.08152385 | 0.00013873 |
| 4100 | [0.06371452, 0.06371453] | [0.06429081, 0.06447812] | 0.06445106 | 0.00016025 |
| 4200 | [0.04759685, 0.04759686] | [0.04869874, 0.04888832] | 0.04888577 | 0.00018704 |
| 4300 | [0.03333802, 0.03333803] | [0.03496352, 0.03515534] | 0.03518748 | 0.00022397 |
| 4400 | [0.02173166, 0.02173167] | [0.02351737, 0.02371142] | 0.02375739 | 0.00024002 |
| 4500 | [0.01316937, 0.01316938] | [0.01471126, 0.01490749] | 0.01493438 | 0.00022313 |
| 4600 | [0.00760335, 0.00760336] | [0.00857862, 0.00877702] | 0.00878309 | 0.00020447 |
| 4700 | [0.00434644, 0.00434645] | [0.00474038, 0.00494092] | 0.00492883 | 0.00018845 |
| 4800 | [0.00253419, 0.00253420] | [0.00255071, 0.00275338] | 0.00270300 | 0.00015230 |

#### α=0.90，H=0.40

| K | 报价价格中点严格区间 | 真 normalized 价严格区间 | 实际 Padé 二进有理数 输出（显示值） | 该输出对真价总误差上界 |
|---|---|---|---|---|
| 3700 | [0.13916863, 0.13916864] | [0.13880016, 0.13883098] | 0.13876501 | 0.00006596 |
| 3800 | [0.11921230, 0.11921231] | [0.11929811, 0.11932934] | 0.11923074 | 0.00009859 |
| 3900 | [0.09981335, 0.09981336] | [0.10073709, 0.10076873] | 0.10063802 | 0.00013071 |
| 4000 | [0.08123198, 0.08123199] | [0.08327826, 0.08331031] | 0.08315433 | 0.00015597 |
| 4100 | [0.06371452, 0.06371453] | [0.06710772, 0.06714016] | 0.06696694 | 0.00017321 |
| 4200 | [0.04759685, 0.04759686] | [0.05242401, 0.05245684] | 0.05228161 | 0.00017523 |
| 4300 | [0.03333802, 0.03333803] | [0.03943228, 0.03946550] | 0.03931664 | 0.00014886 |
| 4400 | [0.02173166, 0.02173167] | [0.02834450, 0.02837811] | 0.02828552 | 0.00009258 |
| 4500 | [0.01316937, 0.01316938] | [0.01934300, 0.01937699] | 0.01935637 | 0.00002061 |
| 4600 | [0.00760335, 0.00760336] | [0.01249183, 0.01252619] | 0.01257890 | 0.00008707 |
| 4700 | [0.00434644, 0.00434645] | [0.00765389, 0.00768862] | 0.00780424 | 0.00015035 |
| 4800 | [0.00253419, 0.00253420] | [0.00449079, 0.00452590] | 0.00467714 | 0.00018635 |


实际 Padé 流程为本文所选GR六条件 [3/3]，导数型指数用256阶Jacobi规则，Fourier用固定截断上限200的8阶复合Gauss–Legendre规则，实际 Python/NumPy 和源字节版本由固定文件记录。每个实际有限输出 \(c^P\) 以精确二进有理数保存。模型价格的参考区间给出
\[
|c^P-c|\le\max\{|c^P-c^-|,|c^P-c^+|\}.
\tag{8.12}
\]
此式包含该实际流程的全部状态、指数、求积、截断与浮点误差，故不必另给“解析 Padé 无限积分”认证后才比较这批实际输出。其数值目标采用同一报价价格中点区间。当算法目标和模型目标均通过严格有限区间分离且胜者相同，才声明该固定流程保持(8.2)的候选选择；该声明的对象是已固定的算法、候选和输入设定。

### 8.6. 数值结果的条件

本节给出所定义连续时间模型的三组价格区间、有限目标的排序、逐行报价关系以及所选Padé流程的输出误差与选择稳定性。GR匹配构造、仿射模型、Caputo比较、Mittag–Leffler界、strip梯形与一般目标间隙思想分别归属已有工作；本文具体证明和计算把这些工具连接到同一有限候选问题。

本节结果成立于三个预先列明的候选、固定曲线与其他参数、半年期限和十二个 IV 所定义的归一化报价。该范围同时固定了目标函数、算法输出与每一个误差项的定义。

全部价格与目标的精确端点见补充数值材料。



## 9. 实际定价输出的共同 Fourier 误差

### 9.1. 误差对象与数值中心

固定一个模型参数、期限、积分轮廓和参考网格。记连续模型价格向量为 \(c^*\in\mathbb R^p\)，精确有限参考和为 \(\bar c\)，固定快速流程的输出为 \(c^{\rm fast}\)。在每个纳入网格的频率处，令参考变换为 \(\bar\phi_n\)，定义 \(z_n=\phi(u_n-i/2)-\bar\phi_n\)。第7节给出 \(|z_n|\le\epsilon_n\)；明确省去的有限节点取 \(\bar\phi_n=0\)，其半径由真实变换包络提供。同一参数与期限下的全部执行价共享同一个 \(z_n\)。

对第6节的 Lewis 规则，令 \(m_i=K_i/F\)、\(k_i=\log m_i\)，并取
\[
a_{in}=-\frac{h\sqrt{m_i}}{\pi}\frac{e^{-iu_nk_i}}{u_n^2+1/4}\quad(n>0),\qquad
a_{i0}=-\frac{2h\sqrt{m_i}}{\pi}.
\tag{J1}
\]
零节点的半权已纳入 \(a_{i0}\)。完整误差为
\[
c^*-\bar c=\Re\sum_{n=0}^{N}a_{\cdot n}z_n+R,
\qquad R\in\mathcal R.
\tag{J2}
\]
其中 \(\mathcal R\) 包含真实无限网格尾和解析条带离散化误差。用数值代表值代替精确 \(\bar c\) 时，还须纳入有限参考和的区间算术中心不确定性。省去的有限节点属于式(J2)的节点误差，不再重复计入无限尾。这里的共享关系来自确定性变换对象，不依赖随机误差相关系数。

### 9.2. 完整包含、支持函数与严格性

**定理9.1（完整共同节点包含）。** 设式(J2)成立，全部半径非负，\(\mathcal R\) 是非空紧凸外包集合。定义
\[
\mathcal E_F=\left\{\Re\sum_na_{\cdot n}z_n:|z_n|\le\epsilon_n\right\}+\mathcal R,
\qquad d=\bar c-c^{\rm fast}.
\tag{J3}
\]
则 \(c^*-c^{\rm fast}\in d+\mathcal E_F\)，且对实向量 \(w\)，
\[
h_{d+\mathcal E_F}(w)=w^\top d+
\sum_n\epsilon_n\left|\sum_iw_i a_{in}\right|+h_{\mathcal R}(w).
\tag{J4}
\]
若中心差仅以区间盒 \(d\in[d^-,d^+]\) 交付，则将第一项替换为该盒的支持函数。式(J4)的每个数值求值均采用向外包络。

**证明。** 将实际变换误差代入式(J2)，即得包含关系。复圆盘乘积及其实线性像均为紧凸集合。圆盘 \(|z|\le\epsilon\) 对实线性泛函 \(\Re(bz)\) 的支持为 \(\epsilon|b|\)：Cauchy–Schwarz给出上界；当 \(b\ne0\) 时，\(z=\epsilon\overline b/|b|\) 取得该界，当 \(b=0\) 时任意可行点均取得该界。不同圆盘的支持相加，Minkowski和再加上余项支持，得到式(J4)。平移产生有符号中心项。即使中心区间各坐标具有依赖性，用其外包盒作Minkowski和仍保持包含。证毕。

若 \(\mathcal R=\prod_i[-\rho_i,\rho_i]\)，同一集合的最小坐标盒满足
\[
h_{\operatorname{rect}(\mathcal E_F)}(w)=
\sum_i|w_i|\left(\sum_n\epsilon_n|a_{in}|+\rho_i\right).
\tag{J5}
\]
因此，在平移前，其支持超过联合支持的量为
\[
G_F(w)=\sum_n\epsilon_n\left(
\sum_i|w_i a_{in}|-\left|\sum_iw_i a_{in}\right|\right)\ge0.
\tag{J6}
\]
严格正差成立，当且仅当至少一个正半径节点上的非零系数 \(w_i a_{in}\) 不全位于同一条非负复射线。逐节点应用复三角不等式及其等号条件即得证明。平移不改变宽度。这一判据比较所构造集合与其自身的最小坐标盒；另行获得的有符号价格区间仍须纳入实际比较。

设另有已证明的模型价格盒 \(\mathcal I\)，则取 \(\mathcal I\cap(\bar c+\mathcal E_F)\)。实际模型向量属于该交集。即使不求解交集的支持优化，两个有效方向上界的较小值仍是有效上界，两个下界的较大值仍是有效下界。这样可保留最佳边际信息，并在完整预算下使用共同节点的抵消。数学交集的非空性来自真实包含，不由两个近似算法的数值接近推定。

### 9.3. 看涨价差的系数估计与有限算术

对 \(w=e_i-e_j\)，节点系数为
\[
|a_{in}-a_{jn}|=\frac{h}{\pi(u_n^2+1/4)}
\left|\sqrt{m_i}e^{-iu_nk_i}-\sqrt{m_j}e^{-iu_nk_j}\right|\quad(n>0).
\tag{J7}
\]
应先合并同一误差的系数，再取模。记 \(b_i=\sqrt{m_i}\)，则有
\[
|b_ie^{-iuk_i}-b_je^{-iuk_j}|
\le |b_i-b_j|+\min(b_i,b_j)\min\{2,|u|\,|k_i-k_j|\}.
\tag{J8}
\]
证明只需用较小振幅拆出振幅差与相位差，再应用 \(|e^{ix}-e^{iy}|\le\min(2,|x-y|)\)。零节点的价差系数为 \(2h|b_i-b_j|/\pi\)。相近执行价的低频误差由此抵消；高频、求积及尾部贡献仍完整保留。

下文实现以有理向外区间计算对数、三角函数、平方根和圆周率，先包住精确系数差，再乘保存的节点半径。参考和区间与固定快速输出区间共同给出有符号中心差。展示时使用中点，不改变判定所用的向外端点。

### 9.4. 联合集合下方向正确的目标界

若真实目标报价为 \(m^*\)，保存中心为 \(\bar m\)，且 \(m^*-\bar m\in\mathcal M\)，则采用 \(r=c^{\rm fast}-\bar m\)，并将输出误差集合替换为 \(\mathcal E-\mathcal M\)，以正确符号计入报价转换算术。否则，下列公式将 \(m\) 视为确切值。

令 \(J(e)=(r+e)^\top W(r+e)/(2p)\)，其中 \(r=c^{\rm fast}-m\)、\(W\succeq0\)，完整输出误差属于紧凸集合 \(\mathcal E\)。对任意试算向量 \(e_0\)，令 \(g_0=W(r+e_0)/p\)。凸性给出
\[
\inf_{e\in\mathcal E}J(e)\ge
J(e_0)-g_0^\top e_0-h_{\mathcal E}(-g_0).
\tag{J9}
\]
对支撑仿射函数 \(J(e_0)+g_0^\top(e-e_0)\) 取下确界即得。\(e_0\) 的可行性不影响有效性，但影响紧致程度。数值原始最小值只有在支持或对偶义务也被正确包络后，才成为下界证书。

若 \(M^2\ge\sup_{e\in\mathcal E}e^\top We\)，展开平方得
\[
\sup_{e\in\mathcal E}J(e)\le
J(0)+\frac{h_{\mathcal E}(Wr)}p+\frac{M^2}{2p}.
\tag{J10}
\]
例如，任何有效坐标盒 \(|e_i|\le b_i\) 都给出充分选择 \(M^2=\sum_{ij}|W_{ij}|b_i b_j\)。可用更紧的已验证范数界替代。凸二次函数的局部驻点不认证其最大值；上界须由支持函数、范数界、区间细分或有效松弛建立。

对有限候选，可将式(J9)–(J10)所得目标区间与定理8.1的逐坐标平方区间相交。只有当一个候选的上端点小于全部竞争者的下端点时，才认证唯一选择；否则返回下端点不超过最小上端点的候选集合，该集合包含全部真最优候选。不同候选具有不同变换误差，式(J4)不将它们认作同一个变量。

支持函数公式、复三角不等式及凸性界是已有数学工具。本节的作用在于将模型特定的连续残差证书连接至实际多执行价输出，并保留完整预算和数值中心。其金融改进以第11节的完整算术比较为依据。


### 9.5. 完整有限历史与任务方向自适应认证

第4节的全时间状态上界可以认证整个轨迹，但先取稳态上界再进入价格积分，会丢掉指定期限的历史长度。这里把正残差比较与第5节的定价核直接组合。正 resolvent 和 Caputo 凸性属于先行工具；新增连接是在正确物理时间尺度下，证明可直接由曲线与残差的普通正卷积控制导数式定价指数。

**定理9.2（有限历史价格指数包络）。** 设 \(0<\alpha<1\)、\(\nu>0\)，真解与固定参考 \(Z,\widehat Z\in AC[0,T]\) 初值为零，且

\[
D_C^\alpha Z=\nu F(Z),\quad
r=D_C^\alpha\widehat Z-\nu F(\widehat Z),\quad |r|\le R,
\quad F(z)=-b+dz+z^2/2.
\tag{N1}
\]

假设 \(R\ge0\) 有界可测、\(\Re d=-s_0\)、\(\Re Z\le0\)、\(\Re\widehat Z\le\epsilon_R\) 与 \(\sigma=s_0-\epsilon_R/2>0\)。曲线满足 \(\xi\in AC[0,T]\)、\(\xi(0)=V_0\ge0\)，且\(q_\alpha=(I^{1-\alpha}\xi)'\ge0\)几乎处处。两指数均使用第5节的 Caputo 导数式定义。则在物理耗散 \(\lambda=\nu\sigma\) 下，

\[
|L_T-\widehat L_T|
\le\nu^{-1}(q_\alpha*k_\lambda*R)(T)
\le\nu^{-1}(\xi*R)(T),
\tag{N2}
\]

其中 \(q_\alpha=(I^{1-\alpha}\xi)'\)，\(k_\lambda(t)=t^{\alpha-1}E_{\alpha,\alpha}(-\lambda t^\alpha)\)。特别地，若 \(R/\nu\le\delta_F\)，

\[
|L_T-\widehat L_T|\le\eta_0
=\delta_F\int_0^T\xi(s)\,ds.
\tag{N3}
\]

这是前提明确的条件式命题，并不额外证明更低阶参数域的真解正则性；本次固定场需由已有全时间证书满足其条件。

**证明。** 令 \(e=Z-\widehat Z\)。二次式的精确差分给出 \(D_C^\alpha e=\nu[d+(Z+\widehat Z)/2]e-r\)，系数实部不超过 \(-\lambda\)。用凸函数 \(v_\varepsilon=\sqrt{|e|^2+\varepsilon^2}-\varepsilon\) 正则化模长，历史凸性不等式给出

\[
D_C^\alpha v_\varepsilon+\lambda v_\varepsilon\le R.
\tag{N4}
\]

这里使用 \(|e|^2/\sqrt{|e|^2+\varepsilon^2}\ge v_\varepsilon\) 和 \(|e|/\sqrt{|e|^2+\varepsilon^2}\le1\)，不是普通导数链式法则。对 AC 曲线，凸函数梯度与 Caputo 导数配对后减去复合函数的 Caputo 导数，得到非负 Bregman 历史余项之和；在 \(W^{1,1}\) 中作因果光滑逼近、利用 Caputo 导数在 \(L^1\) 中收敛，给出几乎处处的不等式。正的零初值逆给出 \(v_\varepsilon\le k_\lambda*R\)，令 \(\varepsilon\downarrow0\) 得 \(|e|\le k_\lambda*R\)。第5节的积分分部恒等式给出(N2)第一项。

令 \(g_\beta=t^{\beta-1}/\Gamma(\beta)\)。初值项必须保留：

\[
q_\alpha=V_0g_{1-\alpha}+g_{1-\alpha}*\xi',
\quad g_\alpha*q_\alpha=V_0+\int_0^t\xi'(s)ds=\xi(t).
\tag{N5}
\]

再由 resolvent 恒等式 \(g_\alpha-k_\lambda=\lambda g_\alpha*k_\lambda\ge0\)、卷积结合律和正性，得到 \(q_\alpha*k_\lambda*R\le q_\alpha*g_\alpha*R=\xi*R\)。有限期限的核与残差绝对可积，故换序合法。这证明(N2)–(N3)。完整分数阶历史始终保留，时间单元不重新起步；\(\nu^{-1}\) 保留物理残差的正确尺度。∎

若闭时间单元 \([t_j,t_{j+1}]\) 上有 \(R(t)\le R_j\)，则

\[
|L_T-\widehat L_T|\le\eta_{\rm time}
:=\nu^{-1}\sum_jR_j
[J_0(T-t_j)-J_0(T-t_{j+1})],
\quad J_0(z)=\int_0^z\xi(s)ds.
\tag{N6}
\]

权重非负，本次 \(V_0>0\) 的冻结曲线使正长度单元的权重严格为正。权重由原参考指数使用的严格曲线矩积分生成。若原残差单元与汇总分箱不一致，取所有相交闭单元的包络最大值可以证明整个分箱的有效上界；只取箱中心样本不够。

对同一参考对象，新旧指数上界可合法取小值。所得 \(\eta_n\) 证明

\[
|\phi_n-\widehat\phi_n|
\le\min\{1,|\widehat\phi_n|\}(e^{\eta_n}-1).
\tag{N7}
\]

随后取旧有效 CF 半径与(N7)右端向外算术上界的较小值，作为更新节点半径。因子1依赖附录A已核验的鞅与Cauchy–Schwarz条件下真实半移变换模长不超过1。最终价格包含仍以 \(d=\bar c-c^{\rm fast}\) 平移，置零有限节点、条带、真实无限尾和算术余项保持完整。代入式指数另有残差转换项，不能静默使用此导数式结论。

**命题9.3（可靠有限动作算法）。** 固定输出、参考、价格系数与全部余项，只接受同一对象的新有效半径，并对节点取新旧较小值，则误差集合逐步嵌套，每个方向的支持半径不增。对任务方向 \(w\)，令 \(R_w\) 同时界定余项在 \(w\) 与 \(-w\) 两方向的支持，\(U_n\) 为共同节点系数模长的有理上界；本轮数值使用的对称余项满足这一条件。初始半径满足

\[
B_0\ge R_w+\sum_nU_n\varepsilon_n^0,\quad
g=B_0-R_w-\sum_nU_n\varepsilon_n^0\ge0.
\tag{N8}
\]

每次精确更新 \(B\leftarrow B-U_n(\varepsilon_n^{\rm old}-\varepsilon_n^{\rm new})\)，保持 \(B=g+R_w+\sum_nU_n\varepsilon_n\)。只有在严格有理比较证明 \(DF(|w^\top d|+B)\le\tau\) 后才返回预算已认证。初始界已足够时零动作停止。若全部有限动作足以通过，且策略最终访问全部未处理动作，至多在动作总数内停止；资源或动作耗尽则返回当前有效未认证区间，并不证明真误差超过预算。

**证明。** 圆盘包含经有限乘积、线性定价映射及同一余项相加保持包含，支持函数随包含单调。更新恒等式保留原加总产生的非负舍入余量。停止和有限耗尽规则直接由该不变量及有限动作表得到。∎

按当前最大贡献 \(U_n\varepsilon_n\) 排序是有效调度策略，不自动是最优效率定理。若所有替代半径已认证、每次升级按单位动作计费，则按保证减量 \(U_n(\varepsilon_n^0-\varepsilon_n^1)\) 递减排序，给出通过单一标量预算所需的最少升级数：将任何选中的较小减量替换为未选中的较大减量不会减少进展。第11.3节的82动作结果只针对指定的全时间最大残差有限历史菜单，不把单独计算的逐时半径或其他菜单纳入该最少动作结论。这一交换论证不证明最少实际运行时间，替代半径的预计算成本必须全部计入。

迁移范围是满足这些前提的有限定价映射与持仓方向；新增连接是有限历史的指数包络及完整实际输出认证接口。正 resolvent、凸性、支持函数和固定菜单交换论证本身仍是先行工具。更一般曲线、额外期限及有符号伴随残差校正需要各自完成输入认证。


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


## 10. 经典Heston作为第二种上游实现

经典分支的残差模态共享原离散规律Q下的占据概率，完整包含与支持为(H1)–(H4)。严格性和终端见证针对构造的外集合，并未给出完整年度合约的金额改善。附录C证明原链概率约束；附录D保存完整函数类、解析试验场、有符号残差恒等式及终端计算。其作用是共同误差约束的第二种上游实现；当前实用材料尚未取得完整全年十价格证书。下节主要数值贡献来自粗糙模型相对实际输出的完整认证。

## 11. 完整误差下的金融判定

### 11.1. 原价差与基线证书

第8节的固定三候选保持原报价、参数及曲线。真实模型和固定快速输出均唯一选择\(\alpha=.52\)，但该候选仍被第8、9行报价带排除。候选排序与报价相容性分别成立；它们不识别市场真实参数，也不证明重新拟合其余参数后的排序。下面使用原4400–4500价差，按第9节重算共同节点，并与同一快速输出中心下最佳有符号边际区间比较。

| α | 对称边际点数 | 有符号边际点数 | 联合点数 | 联合归一化上界 | 相对有符号界收紧 |
|---|---|---|---|---|---|
| 0.52 | 3.593075 | 2.679931 | 1.397613 | 0.000331041790898 | 47.8489% |
| 0.60 | 1.955315 | 0.899772 | 0.504126 | 0.000119408273369 | 43.9719% |
| 0.90 | 0.477839 | 0.447312 | 0.396808 | 0.000093988900141 | 11.2903% |


表中绝对上界向上取整，收紧比例向下取整；判定使用保存的精确有理端点。α=.52的完整联合半径为0.000291542087440（向上取整），中心差约为-0.000039499703457。其完整模型减快速输出误差位于
\[
c^*_{4400}-c^*_{4500}-(c^{\rm fast}_{4400}-c^{\rm fast}_{4500})
\in[-0.000331041790898,\;0.000252042383983].
\tag{J11}
\]
因此，联合界的宽度与实际输出的绝对误差上界是两个不同对象。上述方向保留有符号中心差，全部1025个有限节点的真实变换误差仅计入一次，另计解析条带误差、真实无限尾与参考和算术半径。该结果是完整预算的收紧。

数值单位为 \(c=C/(DF)\)，本实验 \(D=1,F=4221.86\)。金额或指数点误差等于归一化误差乘以 \(DF\)。本次诊断在读取新联合结果前固定1指数点为主预算，并列0.25、0.5、2点为敏感性阈值；该记录不称为计算前预注册，也不代表用户风险偏好或交易适用性。此前全时间状态上界传播未认证α=.52的1点主预算；第11.3节的有限历史重认证通过该预算；在固定2点阈值上，原边际界不满足而联合界满足。这提供了一个由共同误差结构改变数值判定的例子。

对α=.90，联合有符号区间严格为正，表明该固定快速输出低于真实价差，但绝对上界仍以两端最大值计算。对所有候选，共同误差变量只在本候选的同期限节点之间共享。

唯一候选认证采用 \(U_{j_0}<\min_{j\ne j_0}L_j\)。若区间重叠，算法返回包含所有真最优候选的未分离集合。重叠输入的反向检验验证这一行为；它是判定规则测试，不是新增市场接近平局实证。正文的数值校准主张限于列明的三个候选。连续参数域优化、加密剖面及其余参数重新拟合仍属不同实验。


### 11.2. 合成报价下的未分离候选

为检验候选无法分离时的实际输出，我们保留原十二个执行价3700—4800、半年期限及其余模型输入，仅取\(\alpha=.52,.60\)，并构造合成目标价\(m_i=(c_i^{\rm fast,.52}+c_i^{\rm fast,.60})/2\)。原冻结快速输出按精确二进有理数解释，因此两个快速二次目标\(J=(1/24)\sum_i(c_i-m_i)^2\)逐行严格相等，其共同值位于[8.8558783E-8, 8.8558784E-8]。沿用包含连续残差、指数求值、求积、全部有限节点与真实无限尾的价格证书，模型目标区间分别为[3.8651464E-8, 3.05889870E-7]和[3.2507356E-8, 8.9847876E-8]，二者重叠。严格候选判定返回\(\{.52,.60\}\)及`UNSEPARATED`，不认证唯一胜者。以原SPX隐含波动率所定义的报价目标中点区间为对照时，同一两候选及价格证书仍严格选择\(\alpha=.52\)。这个诊断是合成报价压力测试；其结论不表示市场出现平局，也不涉及连续参数加密或其余参数重新拟合。计算使用完整价格区间，复用上游证书而未重新生成它们；精确目标、逐行恒等式、输入字节身份及运行记录见`near-tie-diagnostic.json`。


### 11.3. 有限历史重认证、系统组合与预定预算

本轮计算前固定原4400–4500价差的1指数点预算，保留原场、原快速输出、原参考中心及全部余项；已知旧1.397612095点结果在协议中披露。定理9.2先用已有全时间最大残差执行完整有限历史重认证。此步骤不重新生成近似场或残差。

| α | 原完整联合点数 | 有限历史完整点数 | 完整新区间（点） |
|---|---|---|---|
| 0.52 | 1.397613 | 0.378599 | [-0.378599, 0.045075] |
| 0.60 | 0.504126 | 0.235893 | [-0.235893, 0.083963] |
| 0.90 | 0.396808 | 0.385273 | [0.224062, 0.385273] |

首选候选的有符号中心仍约-0.166762218点。原1.230849877点半径中，已用节点约1.044985362点、置零有限节点约0.184437085点；条带、无限尾及参考算术合计约0.001427432点。新全节点包络的完整绝对上界为0.378599点（向上舍入）；原1点预算通过。0.25点预算仍未认证。实际误差未被观测，不能把证书缩小解释为实际交易损失下降。

采用全时间最大残差的有限历史菜单时，按当前方向贡献的实际调度在82个有效升级后通过1点，完整上界0.996744点。独立固定菜单收益排序也证明这个全局菜单所需最少升级数为82；相同中心和余项的最佳有符号边际菜单需要249。动作仅重认证已有节点，全部513个替代半径的预计算成本均计入。其他两候选在动作前已通过1点，故主任务停止数为0。

系统协议预先固定11相邻价差、10相邻三执行价蝶式、4宽价差和3同向组合；不按结果筛选方向。下表采用1点预算，分母均28，同一场景中的边际盒与联合集均使用该场景的相同节点半径。

| α | 原有符号边际 | 原联合 | 新有符号边际 | 新联合 |
|---|---|---|---|---|
| 0.52 | 0/28 | 3/28 | 28/28 | 28/28 |
| 0.60 | 14/28 | 28/28 | 28/28 | 28/28 |
| 0.90 | 27/28 | 27/28 | 27/28 | 28/28 |

在更紧预算下，α=.52的0.5点通过数为有符号边际13/28、联合28/28；α=.60的0.25点为1/28与10/28，α=.90为13/28与20/28。这些比较都使用已经共同升级的半径，避免把新联合界与旧边际界混比。


全部84方向的联合区间包含于相同半径生成的有符号边际区间。与合法收益方向界的交集在这84例未进一步收紧；这是本轮如实保留的无收益结果。正向组合、宽价差及全部失败预算详见完整逐行账本。当前实验仍只有一个期限和三个原候选；新增期限与真实接近参数候选尚无完整上游证书。合成快速目标平局测试继续仅用于拒绝过度宣布赢家，不能补足这项证据。

首选候选的513个节点、8189个闭时间单元已经完整新重生成，并与旧全部残差、启动与半平面端点精确核对。预先固定128个物理时间分箱，对所有相交闭单元取最大包络，以严格J0差权重传播，完整上界进一步收紧到0.367258782点。所有原置零节点、中心与余项仍保留。详细账本及成本见 `time-local-results.json`；全分数阶历史未重置。

允许使用已经全部预计算的逐时新半径后，独立收益排序给出另一个固定菜单的最少升级数81：前80个动作仍为1.001460253点，前81个为0.997350106点并通过1点；相同中心和余项的逐时有符号边际菜单最少245次。它与上述全局菜单的82属于不同替代半径集合；逐时菜单还须计入完整残差重生成和全部513半径准备成本。

以下定义固定全部28个方向。令 \(K_i=3700+100i\)，\(0\le i\le11\)，\(e_i\) 为第i个执行价的单位持仓向量；未列分量均为零。

| 类别 | 个数 | 完整持仓定义 | 总绝对持仓 |
|---|---|---|---|
| 相邻价差 | 11 | \(e_i-e_{i+1}\), \(i=0,\ldots,10\) | 2 |
| 相邻蝶式 | 10 | \(e_i-2e_{i+1}+e_{i+2}\), \(i=0,\ldots,9\) | 4 |
| 宽价差 | 4 | \(e_0-e_3,e_3-e_6,e_6-e_9,e_0-e_{11}\) | 2 |
| 全执行价篮子 | 1 | \(12^{-1}\sum_{i=0}^{11}e_i\) | 1 |
| 低执行价篮子 | 1 | \(6^{-1}\sum_{i=0}^{5}e_i\) | 1 |
| 高执行价篮子 | 1 | \(6^{-1}\sum_{i=6}^{11}e_i\) | 1 |

宽价差端点依次为3700/4000、4000/4300、4300/4600及3700/4800。每个价格单位是一份期权的指数点价格，表内权重为固定名义持仓；指数点到报告货币的乘数取1，不宣称交易所合约的美元名义本金。\(c=C/(DF)\)，本任务\(DF=4221.86\)。若全部持仓乘以\(a\)，绝对误差界乘以\(|a|\)，相同一点阈值的通过数可能改变。三个正篮子权重之和均为1；价差和蝶式没有额外归一化。完整逐方向JSON与本表逐项一致。

有限期限传播复用全局连续残差，将首选候选完整上界从1.397612095收紧至0.378598956点，约收紧72.91%。逐时包络随后降至0.367258782点，增加约0.011340174点、相对约3.00%的改善。两项成本分别报告。共同误差结构的贡献用相同新节点半径的边际/联合比较辨识：α=.52在0.5点预算为13/28与28/28；α=.60在0.25点为1/28与10/28；α=.90在0.25点为13/28与20/28。一点预算下α=.52两种新方法均28/28，旧到新的整体改善不能全部归因于共同几何。

### 11.4. 成本范围与失败条件

| 工作 | 本轮耗时（秒） | 范围 |
|---|---|---|
| 三候选新传播全部节点 | 3.524 | 旧残差复用，含补充全节点动作 |
| 原84方向对照 | 16.418 | 含共享系数准备 |
| 新84方向对照 | 13.699 | 同场景公平比较，含准备 |
| 残差新重生成的连续循环阶段 | 997.266 | 513频率，8189闭区间；不含setup及startup |
| 逐时传播及检查 | 1.479 | 复用新完整包络与已验证系数 |

这些耗时与原稿793、779、194秒的历史生成时间区分。此处“新传播”不是从零求场、生成残差和验证全部结构的总成本。固定菜单最少动作数不含未知未来工作的性能承诺。若输出或参考场改变，必须重新取得该对象的中心与证书；固定尾和中心会限制当前菜单可认证的预算。

### 11.5. 认证被省略的有限频率，并同步改变参考中心

此前，$\alpha=13/25$、$T=1/2$ 的 4400–4500 价差证书把 $64<u\le128$ 的近似变换有意设为零。原逐时传播的完整误差上界为 0.367258782 指数点。即使把所有低频误差半径都设为零，该证书仍有 0.352626734 点的预算下限，因为其固定有符号中心、有限频率省略项和完整余项仍须保留。这个下限属于该证书的构造，并非真实数值误差的下界。

在读取新结果前，我们冻结了独立合同：仍用同一价差、同一存储场、同一 $u\le64$ 的实际 Padé 快速输出，以及原有 1、0.5、0.25 点预算。扩大后的参考使用全部 1025 个、截至 128 的已交付非零存储场变换 $\bar\phi_u$，因此必须同步修改“参考值减实际快速输出”的有符号中心。原省略项对 $|\phi_u-0|$ 的上界不能直接充当 $|\phi_u-\bar\phi_u|$ 的上界。新节点采用

$$
|\phi_u-\bar\phi_u|\le\min\left\{B_\alpha(u)+|\bar\phi_u|,
\min(1,|\bar\phi_u|)\bigl(e^{\eta_u}-1\bigr)\right\},
$$

其中第二项依赖完整历史传播定理及已认证的近似解半平面条件。实际计算半径取两项严格向上包络的最小值，因而仍包住变换误差。新中心、其完整向外算术包络、原解析条带预算，以及 128 之外的真实无限尾部，均被明确重算或保留。

已有连续残差证据没有覆盖这 512 个高频节点。因此，本次实际重新构造了同一场在全部 8189 个封闭时间格上的高频物理残差包络，包括首格。所有高频节点的首格和后续近似解实部上界均非正；独立的精确 Caputo 首格装配也在全部 512 个节点通过。保存矩阵检查核验了全部 4,192,768 个残差元素、完整分区、逐节点最大值，以及六项故意缺损负控。另一独立读取器还重新构造全部 1025 个 CF 半径、完整参考中心、替代三角恒等式系数上界与完整预算，其八项负控均被拒绝。收据明确声明共享的标量区间原语和原连续残差包络数学，未将矩阵一致性检查称为全部后续导数格的独立重算。

| 新高频节点的传播方式 | 同一新圆盘的有符号边际界 | 共享节点联合界 | 0.25 点预算 |
| --- | ---: | ---: | --- |
| 完整历史的全局上界 | 0.158585551 | 0.132245064 | 两者均通过 |
| 预先固定的 128 个封闭时间分箱 | 0.137896018 | 0.115215934 | 两者均通过 |

表中绝对误差界均向上舍入。两行的低频节点均保留此前已核验的逐时半径；行名只描述新增高频节点的传播方式。原有符号中心约为 $-0.166762218$ 点，新中心约为 $-0.081698202$ 点，修正约为 $+0.085064016$ 点。两条完整误差区间均已计入该修正，不丢弃中心，也不把新半径错误地配到旧中心。

四分之一点预算的通过主要来自对原先省略的有限频率进行认证，并同步重定位参考中心。同一新圆盘的有符号边际界也已通过该预算；共享节点几何进一步带来约 16.6% 与 16.4% 的上界缩减。本例中，旧、新完整误差区间取交集没有进一步改善；新增高频圆盘也并非全部嵌套于原零中心圆盘，因此不主张节点不确定集合自动嵌套。

本次高频残差重构的父进程冷启动墙时为 575.027420 秒，包含进程启动、NumPy 导入、初始化、计算和矩阵保存。峰工作集为 318,656,512 字节，向上舍入约 303.895 MiB，低于冻结的一 GiB 限制。Python 为 3.12.14、NumPy 为 2.3.5；OMP、OpenBLAS、MKL、NumExpr 的线程设置均固定为一。残差生成采用向外 binary64 区间算术；参考值、曲线矩、指数和最终决策采用 100 位二进有理区间及精确有理数比较。随后单独的参考装配、传播与完整预算重放约需 2.5 秒，复用本次新生成的残差矩阵，不能替代或抹去其生成成本。结论仅针对该固定场、参数点、期限、价差和实际快速输出，不证明最小运行时间的生成策略、盈利能力或一般校准精度。

默认证据顺序为 `omission-verify.py` → `omission-aggregate.py` → `independent-omission.py`。通过 `run_frontier.py --regenerate-full` 可选择在独立工作副本中全量重新生成。精确端点及哈希见 `omission-results.json`、`omission-node-ledger.json`、`omission-residual-high.json`、`omission-full-execution.json` 和两份核验收据。


### 11.6. 第二期限的完整定价认证

在已知半年期限结果之后、计算任何新的三个月价格或误差界之前，固定描述型迁移合同。新任务取 \(T=1/4\)，保留原物理前向方差曲线、三个候选 \(\alpha\in\{13/25,3/5,9/10\}\) 和 4400–4500 看涨价差，使用 \(D=1\)、\(F=4221.86\) 的归一化。这是既有合法模型下的定价任务；未引入新的市场报价或校准结论。附录 A 的模型存在、仿射变换与鞅论证适用于每个有限期限。

旧的连续参考场、物理残差与全时间半平面证书覆盖 \([0,1/2]\)，限制到 \([0,1/4]\) 后仍保留从零开始的同一 Caputo 历史。三个候选的三个月终点均位于原仿射时间单元内部。以 \(\widehat G_{\rm lin}\) 表示存储为 `LG` 的分段仿射余项，分数幂多项式部分保留原解析形式。若 \(t_\ell<T<t_{\ell+1}\)，终点余项严格使用

\[
\widehat G_{\rm lin}(T,u)=(1-r)\widehat G_{\rm lin}(t_\ell,u)+r\widehat G_{\rm lin}(t_{\ell+1},u),
\qquad r=\frac{T-t_\ell}{t_{\ell+1}-t_\ell}.
\tag{TR1}
\]

原存储的 binary64 端点均解释为精确有理数，因而该式保留原连续参考场。新期限的帽函数权重、分数幂矩、参考指数和指数函数区间全部重新求值。指数误差取有限历史界 \(\delta_FJ_0(1/4)\) 与旧状态界经新期限曲线质量传播所得界的较小者；两个界约束同一 D-type 参考指数。

原 Padé 快速定价程序也在 \(T=1/4\) 重新执行，保留原 Fourier 复合求积阶数 8 和时间求积阶数 256。返回的 binary64 看涨价格冻结为精确输出。完整误差区间以新认证参考价格减去该实际输出为中心，计入参考算术、条带误差、有限遗漏频率和真实无限尾。取 \(h=1/8\)，513 个参考节点覆盖 \(0\le u\le64\)；其后至 \(u=128\) 的 512 个节点以零为参考，分别采用新计算的真实 CF 上界。对每个候选，原适用于有限期限的比较证明在 64 个三个月时间单元上重新求值，保留分数阶启动质量，并重新认证 128 之后的正统一衰减率。没有沿用旧半年期限的数值尾界。

| 候选 \(\alpha\) | 共同完整界：指数点 | 同中心有符号边际界：指数点 | 共同：1/4 点 | 共同：1/2 点 | 共同：1 点 | 共同：2 点 |
|---|---:|---:|---|---|---|---|
| 13/25 | 1.207557898 | 1.545191542 | 未认证 | 未认证 | 未认证 | 已认证 |
| 3/5 | 0.801202097 | 1.056299693 | 未认证 | 未认证 | 已认证 | 已认证 |
| 9/10 | 0.497738795 | 0.610152566 | 未认证 | 已认证 | 已认证 | 已认证 |

表中上界由精确有理端点向上舍入。\(\alpha=3/5\) 时，共同界通过一指数点预算，而匹配的有符号边际界未通过；\(\alpha=9/10\) 时，半指数点预算也出现这一差异。在这一初始参考至64的全局传播阶段，三个候选的四分之一点预算均保留为 `NOT_CERTIFIED`，其含义是这些完整上界尚不足以证明该精度，不是实际误差超过预算。每项匹配比较都固定该候选的实际输出、参考中心、上游半径与全部余项，仅改变误差聚合方式。

本次三个候选的新计算在记录的主机上耗时 68.346 秒，计入新快速输出、三个月矩与参考指数、全部真实 CF 包络和尾界、系数与完整聚合。参考场构造和连续残差生成属于复用的上游工作，未计入这次重放时间。所得结果证明另一期限的完整实例已闭合，不推断所有期限的精度或运行时间保证。`independent-transfer.py --full` 不导入迁移聚合程序，独立重放全部 1539 个限制场指数、三个实际快速输出、3075 个真实 CF 包络、系数与完整金融端点；其共享已注明身份的原严格基本算术和矩原语，不另行生成上游残差证书。具体合同、字节身份、分阶段耗时、反向检查与全部预算判定保存在 `transfer-contract.json`、`transfer-results.json` 和 `independent-transfer.json`。

预先约定的可选阶段对 \(\alpha=13/25\) 加入新认证的 \(64<u\le128\) 高频参考，重新计算全部 1025 个三个月参考指数及其算术，实际快速输出保持原值。参考减快速价的中心发生变化，因此旧的零参考遗漏半径被真实 CF 减去新参考的证书取代，完整预算随之重建。该全局传播的完整界为 0.351318692 点，仍未通过四分之一点预算。在已知此结果后，再单独固定一次描述型探索：三个月内取 128 个时间区间，边界为 \(j/512\)。每个相交的原闭时间单元贡献其完整残差上界，跨越新期限的单元也纳入；新正权重为 \(J_0(1/4-a)-J_0(1/4-b)\)。使用精确有理数加总传播，并与同参考下各自有效的全局半径取小值。本轮未再探索其他变体。

| 三个月 \(\alpha=13/25\) 阶段 | 共同完整界：指数点 | 同中心有符号边际界：指数点 | 共同四分之一点判定 |
|---|---:|---:|---|
| 参考至 64，全局传播 | 1.207557898 | 1.545191542 | 未认证 |
| 参考至 128，全局传播 | 0.351318692 | 0.408293698 | 未认证 |
| 同一参考至 128，128 个时间区间 | 0.233318843 | 0.252393939 | 已认证 |

最后一行通过四分之一点预算，而匹配的有符号边际界仍未通过。后两行固定实际输出、参考中心与全部余项，仅改变连续残差包络的传播。新高频残差覆盖原完整半年历史，随后合法限制；没有重新起步三个月历史。高频生成的父进程冷运行耗时 575.027 秒，与复用的原参考场和低频证据分开记录；全部高频参考加入后的三个月重算耗时 72.468 秒，追加时间区间的分组、权重、传播与完整聚合耗时 1.774 秒。这些阶段成本不构成总工作量或运行时间最优结论。`independent-transfer-supplement.py --full` 核对全部 8189×512 个新残差单元节点，重放 1025 个三个月指数及金融项，并用闭区间交集范围独立构造 128 区间的全单元最大值；独立正权重上端点的精确加总重现完整终端区间。全局失败和随后唯一一次探索分别保存在 `transfer-supplement-contract.json`、`transfer-time-local-contract.json` 及其结果中。


本轮冷启动验收采用新解释器、新解压副本和完整--full序列，18项全部退出0。父进程总耗时221.018秒；ZIP验证和解压另计1.593秒，下载未计。Windows job记录整个验收进程树的峰值提交内存665.25 MiB，此值不是峰值RSS。本机Intel Core Ultra7 155U，12核14逻辑处理器，Windows11 10.0.26200，可见物理内存约15.44GiB，Python3.12.14、NumPy2.3.5，向外算术100bit。这次运行OMP/MKL/OpenBLAS线程上限显式设1；旧历史耗时的线程和峰内存没有记录，不追溯填补。其他研究进程可能同时运行，因此这些观测不构成隔离加速测试。父进程计时包含输入哈希、工作副本、解释器启动、全部检查和输出验证；可选完整连续残差重生成另计。完整记录见cold-acceptance.json。

## 12. 证据交付、验证语义与计算成本

本轮完整扩展的单命令为 `python heston-frontier-20261007/run_frontier.py --full`。它先核验FRONTIER-MANIFEST、创建新工作副本，再执行旧完整验收、高频包络检查、完整中心和预算重算、高频独立读回、三候选新期限及全参考/逐时补充独立读回。可选 `--regenerate-full`重新生成新增512高频连续残差。保存包络核验与全连续导数重生成的范围分列。新增(FQ1)–(FQ6)是解析证明；(FQ7)–(FQ8)对应省略节点新中心与完整账本。

固定证据的公开入口为[版本页面](https://github.com/130U/certified-rough-heston-valuation/releases/tag/v0.2.0-certification-20261007)，可直接下载[原有限历史ZIP](https://github.com/130U/certified-rough-heston-valuation/releases/download/v0.2.0-certification-20261007/Theodore-Ouyang-Heston-Finite-History-Evidence-20261007.zip)及[本轮扩展ZIP](https://github.com/130U/certified-rough-heston-valuation/releases/download/v0.2.0-certification-20261007/Theodore-Ouyang-Heston-Frontier-Evidence-20261007-v2.zip)。这里指上传的具名资产；GitHub自动生成的Source code归档不等同于完整证据包。原有限历史ZIP的SHA256为edc25d2ad86c1526f404ec1a46a02a283f0726602f259beaa97eb1219d22d299。扩展包逐文件SHA256和准确运行命令见FRONTIER-MANIFEST.json与README.md。本地重跑和多agent读回是作者侧验收，不能冒称外部审稿人已下载或独立通过。

固定证据包为 `Theodore-Ouyang-Heston-Finite-History-Evidence-20261007.zip`，包含本研究所用全部已发布上游数据、新连续时间包络、独立检查器、成功及失败的完整组合行和可编辑稿源。`BUNDLE-MANIFEST.json`记录逐文件SHA256、字节数与命题组。解压后，单命令 `python heston-nine-point-20261007/run_evidence.py --full` 先核对冻结文件，再在工作副本重生成全部结构符号并执行所有验收；加 `--regenerate-continuous` 则额外重生成首选固定场的全部513个已用残差频率。验收需要Python和NumPy，PDF生成属于另行工具链。

(N2)–(N3)对应有限历史结果及两个独立回查；(N6)对应完整NPZ包络、逐时覆盖检查和独立逐时核验；(N8)对应全部动作轨迹与精确固定菜单阈值端点；第11.3节对应两个相同半径场景的84行组合账本。执行收据保留退出码、版本及父进程耗时。部分向外算术原语共享，这一实现独立性的限制明确披露。


本次证据冻结于仓库commit `6a5134197db60c765ca3aea4f6cdeb2bafbb6617`。输入身份见 `source-inventory.json`；新联合节点账本、精确汇总和命令日志另行交付。数学证明与代码验证分工如下。

| 层次 | 本次交付与验收 | 验证的对象 |
|---|---|---|
| 连续域结构 | 211241个叶的全部原始符号重算及422481个树节点的几何重建 | 每叶原多项式、严格符号和连续域完整覆盖 |
| 连续时间参考 | 原固定NPZ系数、启动消去与全时间残差记录 | 精确二进系数定义的函数；本次不重生成全部上游残差 |
| 原链约束 | 原矩界、102带、22条约束及全部918个剖面重算 | 实际原Q概率包含与约束方向 |
| 终端见证 | 407项精确原始、对偶、唯一性与导数检查 | 指定终端外集合的严格性 |
| 新联合价差 | 三候选各1025节点及完整中心、余项账本 | 相对实际冻结输出的完整方向界 |
| 反向输入 | 破坏覆盖、符号、概率约束、节点或预算的拒绝检查 | 错误对象不能取得原证书身份与判定 |

结构验证中的“记录检查”与“重算区间符号”分别计数。全叶结果见 `full-structure-verification.json`，它独立于此前16叶预检。本次全叶重算采用公开的原始多项式与100bit向外有理区间生成器，并逐字段核对记录；它不声称另写一套超越函数运算库。连续残差验证采用完整保存输入检查、全部1539个频率启动项的独立组装及每候选两频率的全时间新重放，未重新生成全部频率的全时间残差。固定場不由重新生成的浮点场替换；若场改变，必须为新对象取得独立残差证书。新价差另由不导入新增计算器的检查器，以振幅差和正弦恒等式重组系数，并核验中心平移与完整余项。

账本明确区分：参考状态误差经正核进入变换圆盘；参考指数求值区间进入有限和算术半径；有限省略节点由真实变换包络计入圆盘；解析条带预算控制连续积分到无限规则；真实无限尾控制有限规则以后；参考减快速输出构成有符号平移。中心差不计为随机误差，有限节点与无限尾不重复收费。

经典十三维场的历史积分收据可核验保存的数值身份，但当前便携包未包含全部系数银行。本稿以完全显式的解析非精确场支撑试验函数扩展，不据历史收据宣称完整年度价格认证。其档案状态在内部审查中保留。

执行时间、包版本、符号重算数量、节点数量和退出状态以 `verification.json` 及新价差证书为准。原残差生成器的历史时间为约793、779、194秒，不能转述为本次重新生成时间。支持汇总与上游认证的成本分别计量。

## 13. 适用范围与结论

| 性质 | 成立依据及范围 |
|---|---|
| 模型价格及矩条件 | 合法连续概率模型、真实仿射变换和已证明可积性 |
| 三阶近似无正时间极点及半平面 | 定理3.1的固定连续参数域 |
| 完整价格区间 | 指定参考场、物理缩放、曲线、连续残差、求积及尾 |
| 联合价差收紧 | 同参数同期限的共同变换误差与完整中心预算 |
| 有限候选选择 | 固定曲线、其余参数及列明三候选 |
| 经典共同状态严格性 | 指定原链、模态、概率集合及未交收益范围的外集合 |

近似轨迹的半平面性质不单独证明它是合法特征函数，也不直接认证全部期限执行价价格面或Greeks。α=.90的价格区间来自其独立参考场；该候选的存在不扩大定理3.1的结构参数域。合稿的核心证明不依赖中心频率上更宽的T1先行链。

本文的研究连接由真实包含完成：粗糙模型的连续残差形成共同变换圆盘，经典模型的原链状态约束形成共同残差可行集，两者的线性价格像给出方向界，并在实际输出中心下用于金融判定。原价差的完整认证上界得到严格收紧；原候选实验的数学排序与报价排除保持各自的意义。理论扩展及其可复核计算在明确对象和量词下共同构成本文的结论。


本稿的主推进是残差经完整有限历史进入价格指数和实际输出证书。原一点任务已通过；主要突破来自有限期限传播，逐时包络提供较小附加改善，相同半径的紧预算对照体现共同误差结构的价值。新增解析条件和期限任务仅在各自证明、合同和完整账本范围内成立。高频省略节点的新认证按实际输出重新计算中心，不能沿用旧冻结预算的下界作为所有认证方法的下界。完整证据已经提供准确下载入口、逐文件身份和可执行验收；后续外部独立运行仍是另一项证据。

本轮原价差的最佳完整上界为0.115215934点，并取得四分之一点证书。改善来自对新增高频的完整认证和合法中心平移；边际方法在同一新参考下也通过该预算，故这一突破不能全部归因于共同几何。共同结构进一步降低相同半径的方向上界，其作用由匹配比较单独衡量。

新期限T=1/4的单次另列逐时探索取得联合0.233318843点、有符号边际0.252393939点；在同一快速输出、新参考中心、半径和全部余项下，只有联合方向界通过四分之一点。此前全局阶段未通过的结果一并保留，因此该实例检验了方法迁移，也给出共同几何改变任务判定的实质证据。

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

源 Theorem 2.3 要求 \(\operatorname{Re}\psi_1\in[0,1]\)、第二状态初始变换非正实部、方差强制项非正实部。取 \(\psi_1=ia=1/2+iu\)，其他初始/强制项为零，恰给 (2.2)、(2.6)，以及唯一弱分布。取 \(\psi_1=1\)，Riccati 解为零，得到 \(\mathbb E S_T=S_0\)；正局部鞅常均值使其为真鞅。因而 (6.1) 的概率条带来自连续时间模型。此处应用成熟存在性及仿射变换理论，不主张新存在性定理。

## 附录 B. 定理 3.1 的精确有限证书

证书域为 \(\mathcal B=[13/25,3/5]\times[0,1]\)。每个区间 \(I=[\ell/2^{100},r/2^{100}]\) 采用整数外舍入。有理输入上下取整，乘法取四角极值并量化；倒数先排除零，平方根用整数 isqrt 和向上补一，复数用实虚矩形算术。主根及倒数分支已由 (3.3) 的解析下界保证，不用浮点符号容忍度。

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

对每个闭矩形，将这些包络依次代入 (3.3)、(2.12)、(2.13)、(3.5)、(3.8)。只有三条 \(\bar B_j\) 下端严格正、六条 \(\bar D_n\) 上端严格负才接受；否则沿一个坐标的确切有理中点二分。两个闭子矩形并集等于母矩形，共享边界亦由严格包络覆盖。

有限区间覆盖包含 211241 个叶矩形，其有理面积精确为 \(2/25\)。独立检查从根矩形重建 422481 个二叉树节点、最大深度19，每个记录叶子恰出现一次，因此除面积外还排除了遗漏子树、内域重叠与端点空洞。本定理采用该完整闭树所覆盖的阶数区间。

完整证书中的更强有理余量蕴含下表；每次简化转化已用 Fraction 独立检查。

| 全紧化域的量 | 严格下界 |
|---|---:|
| \(\bar B_1,\bar B_2,\bar B_3\) | \(1/6000,\ 1/8000,\ 1/20000000000\) |
| \(-\bar D_1,-\bar D_2,-\bar D_3\) | \(1/30000,\ 1/2000000000,\ 1/6000\) |
| \(-\bar D_4,-\bar D_5,-\bar D_6\) | \(1/8000,\ 1/15000000,\ 1/100000\) |
| \(|\bar\Delta|^2\) | \(1/14400\) |

证明由严格区间包含与完整有限覆盖组成。补充材料给出区间算术实现、全部叶矩形及树结构检查，供逐项复核。



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

10. **GatheralCode2023.** Gatheral, Jim. *RationalRoughHeston: roughHestonPadeLambda.R*. 2023. [原文](https://github.com/jgatheral/RationalRoughHeston/blob/d65ea96e4c113fbb330074dfaea3e7715d650bbd/roughHestonPadeLambda.R)。

11. **WoonJengSPXDataset2021Frozen.** WoonJeng. *Dataset for SPX Calibration of Option Approximations under Rough Heston model*. 2021. [原文](https://github.com/WoonJeng/Dataset-for-SPX-Calibration-of-Option-Approximations-under-Rough-Heston-model/tree/860049da2b7486fe8aa509061eff23cc28c2ef89)。

12. **Gilewicz2005.** Gilewicz, Jacek and Pindor, Maciej and Telega, J. Joachim and Tokarzewski, Stanisław. *N-Point Padé Approximants and Two-Sided Estimates of Errors on the Real Axis for Stieltjes Functions*. Journal of Computational and Applied Mathematics 178(1–2), 247–253, 2005. DOI [10.1016/j.cam.2003.12.051](https://doi.org/10.1016/j.cam.2003.12.051)。

13. **EberleinGlauPapapantoleon2008v1.** Eberlein, Ernst and Glau, Kathrin and Papapantoleon, Antonis. *Analysis of valuation formulae and applications to exotic options in Lévy models*. 2008. [原文](https://arxiv.org/abs/0809.3405v1)。 使用版本：arXiv:0809.3405v1。

14. **Heston1993.** Heston, Steven L. *A Closed-Form Solution for Options with Stochastic Volatility with Applications to Bond and Currency Options*. The Review of Financial Studies 6(2), 327–343, 1993. DOI [10.1093/rfs/6.2.327](https://doi.org/10.1093/rfs/6.2.327)。

15. **CozmaReisinger2016.** Cozma, Andrei and Reisinger, Christoph. *Exponential integrability properties of Euler discretization schemes for the Cox–Ingersoll–Ross process*. Discrete and Continuous Dynamical Systems - B 21(10), 3359–3377, 2016. DOI [10.3934/dcdsb.2016101](https://doi.org/10.3934/dcdsb.2016101)。 使用版本：arXiv:1601.00919v1。

16. **KimKimKimWee2016.** Kim, Bara and Kim, Jeongsim and Kim, Jerim and Wee, In-Suk. *A recursive method for discretely monitored geometric Asian option prices*. Bulletin of the Korean Mathematical Society 53(3), 733–749, 2016. DOI [10.4134/BKMS.b150283](https://doi.org/10.4134/BKMS.b150283)。

17. **BoydVandenberghe2004.** Boyd, Stephen and Vandenberghe, Lieven. *Convex Optimization*. Cambridge University Press, 2004. [原文](https://web.stanford.edu/~boyd/cvxbook/)。

18. **MickelNeuenkirch2022v2.** Mickel, Annalena and Neuenkirch, Andreas. *The weak convergence order of two Euler-type discretization schemes for the log-Heston model*. 2022. [原文](https://arxiv.org/abs/2106.10926v2)。 使用版本：arXiv:2106.10926v2。

19. **BertsimasPopescu2002.** Bertsimas, Dimitris and Popescu, Ioana. *On the Relation between Option and Stock Prices: A Convex Optimization Approach*. Operations Research 50(2), 358–374, 2002. [原文](https://www.mit.edu/~dbertsim/papers/Finance/On%20the%20relation%20between%20option%20and%20stock%20prices-%20a%20convex%20optimization%20approach.pdf)。

20. **Hartmann2008.** Hartmann, Ralf. *Multitarget Error Estimation and Adaptivity in Aerodynamic Flow Simulations*. SIAM Journal on Scientific Computing 31(1), 708–731, 2008. [原文](https://elib.dlr.de/57073/1/Har08a.pdf)。

21. **CboeSPX2022.** Cboe Global Markets. *Cboe to Further Expand S&P 500 Index Options Suite with New and Additional Daily Expirations*. 2022. [原文](https://ir.cboe.com/news/news-details/2022/Cboe-to-Further-Expand-SP-500-Index-Options-Suite-with-New-and-Additional-Daily-Expirations-09-19-2022/default.aspx)。

22. **FederalReserveSR1107.** Board of Governors of the Federal Reserve System and Office of the Comptroller of the Currency. *Supervisory Guidance on Model Risk Management*. Board of Governors of the Federal Reserve System and Office of the Comptroller of the Currency(SR 11-7, Attachment), 2011. [原文](https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf)。 此处引用2011年发布的历史模型验证框架。

23. **OuyangAsian2024.** Ouyang, Theodore. *Certified Valuation of Arithmetic Asian Options via Common Gaussian Smoothing*. Author manuscript, 2024 cover version; supplied PDF. [Project](https://github.com/130U/certified-valuation-arithmetic-asian-options).

24. **BBWeak2023v1.** Bayer, Christian and Breneis, Simon. *Weak Markovian Approximations of Rough Heston*. 2023. [原始版本](https://arxiv.org/abs/2309.07023v1)，[原始 PDF](https://arxiv.org/pdf/2309.07023v1)。所读版本：arXiv:2309.07023v1，2023 年 9 月 13 日提交；特征函数与 European payoff 误差结果见定理 2.2、2.7。

25. **BBSimulation2023v1.** Bayer, Christian and Breneis, Simon. *Efficient option pricing in the rough Heston model using weak simulation schemes*. 2023. [原始版本](https://arxiv.org/abs/2310.04146v1)，[原始 PDF](https://arxiv.org/pdf/2310.04146v1)。所读版本：arXiv:2310.04146v1，2023 年 10 月 6 日提交；该版本页 4 将二阶弱收敛报告为数值观察。

26. **Kopteva2021v2.** Kopteva, Natalia. *Pointwise-in-time a posteriori error control for time-fractional parabolic equations*. Applied Mathematics Letters 123, 107515, 2022. DOI [10.1016/j.aml.2021.107515](https://doi.org/10.1016/j.aml.2021.107515)。[所读原始版本](https://arxiv.org/abs/2105.05848v2)，[原始 PDF](https://arxiv.org/pdf/2105.05848v2)：arXiv:2105.05848v2，2021 年 7 月 5 日修订；首次提交于 2021 年 5 月 12 日。逐时残差界与范数不等式见定理 2.2、引理 2.8。


[ElEuchRosenbaum2017v1] Omar El Euch and Mathieu Rosenbaum. Perfect hedging in rough Heston models. arXiv:1703.05049v1, 15 March 2017. https://arxiv.org/abs/1703.05049v1. Fractional forward-curve relations and their admissibility restrictions are prior results; the present decreasing curve is an analytical propagation example.
