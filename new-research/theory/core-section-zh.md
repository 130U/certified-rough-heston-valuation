### 比较论证的一条集中正则性桥梁

标量分数阶比较属于已有工具。Li–Liu [LiLiu2018, Proposition 3.11(ii)] 处理正则化后的凸性及分布极限，其 Proposition 4.12 则讨论指定的向量梯度流与 Hamiltonian 流。Kopteva [Kopteva2021v2, Lemma 2.8、Theorem 2.2] 在正时间 Lipschitz 假设下用范数凸性和正分数阶逆传播逐时残差。以下直接证明本文实际使用的向量 \(AC\) 版本，包括期限终点结论。这是已有工具的适配，不作为新的一般 Caputo 比较定理。

**正则性引理（AC 凸性与连续终点）。** 设 \(0<\alpha<1\)、\(T>0\)、\(v\in AC([0,T];\mathbb R^d)\)，且 \(\Phi\in C^1(\mathbb R^d)\) 凸。则

\[
D_C^\alpha\Phi(v)\le\nabla\Phi(v)\cdot D_C^\alpha v
\quad\text{在 }(0,T)\text{ 上几乎处处成立}.
\tag{AC1}
\]

若 \(u\in AC[0,T]\)、\(u(0)=0\)、\(\lambda\ge0\)、\(0\le R\in L^\infty(0,T)\)，且 \(D_C^\alpha u+\lambda u\le R\) 几乎处处，则

\[
u(t)\le(k_\lambda*R)(t),\quad0\le t\le T,
\qquad k_\lambda(t)=t^{\alpha-1}E_{\alpha,\alpha}(-\lambda t^\alpha).
\tag{AC2}
\]

**证明。** 取光滑 \(f_n\to v'\) 于 \(L^1(0,T)\)，定义 \(v_n(t)=v(0)+\int_0^t f_n(s)ds\)。这样初值完全保留，\(v_n\to v\) 一致，且 \(v_n'\to v'\) 于 \(L^1\)。光滑路径的历史分部积分给出 (AC1) 两侧之差

\[
\frac1{\Gamma(1-\alpha)}\left[
\frac{B_\Phi(v_n(0),v_n(t))}{t^\alpha}
+\alpha\int_0^t\frac{B_\Phi(v_n(s),v_n(t))}{(t-s)^{1+\alpha}}ds\right]\ge0,
\tag{AC3}
\]

其中 \(B_\Phi(a,b)=\Phi(a)-\Phi(b)-\nabla\Phi(b)\cdot(a-b)\ge0\)。梯度在紧路径范围上的界 \(M\) 与光滑路径的局部 Lipschitz 常数 \(L\) 给出 \(B_\Phi(v_n(s),v_n(t))\le2ML|t-s|\)，所以端点核 \((t-s)^{-\alpha}\) 可积。

所有路径落在同一紧集。普通的一阶 \(AC\) 复合规则给出 \(\Phi(v_n)'\to\Phi(v)'\) 于 \(L^1\)，而 Young 不等式给出

\[
\|D_C^\alpha(v_n-v)\|_1
\le\frac{T^{1-\alpha}}{\Gamma(2-\alpha)}\|v_n'-v'\|_1\to0.
\tag{AC4}
\]

同一估计适用于 \(\Phi(v_n)-\Phi(v)\)。梯度的一致收敛还保证右侧乘积在 \(L^1\) 中收敛。取几乎处处收敛的子列，即得 (AC1)。这里仅对普通一阶导数使用复合规则，没有使用 Caputo 链式法则。

设 \(f=D_C^\alpha u+\lambda u\in L^1\)。零初值给出 \(u+\lambda g_\alpha*u=g_\alpha*f\)。预解级数的第 \(n\) 项 \(L^1\) 范数不超过 \(\lambda^{n-1}T^{n\alpha}/\Gamma(1+n\alpha)\)，故局部收敛并给出 \(u=k_\lambda*f\) 几乎处处。\(E_{\alpha,\alpha}(-x)\) 的完全单调性 [SimonML2015] 给出 \(k_\lambda\ge0\)，所以 \(f\le R\) 蕴含 \(u\le k_\lambda*R\)。将核和 \(R\) 零延拓后，核的 \(L^1\) 平移连续性及 \(R\) 的 \(L^\infty\) 界证明右侧连续，且在零点为零。左侧也连续，故不等式推广到 \([0,T]\) 每一点，包括终点。∎

### 本文中心的有限历史定价定理

模型特定的连接，是将复 Riccati 的耗散误差与导数型 Heston 定价泛函复合。完整历史始终从初始时刻计入；满足下列假设的固定参考轨迹均可使用这一结果，生产端 Padé 输出怎样计算由另一条证明链处理。

**定理 3.3（有限历史定价包络；原定理 9.2）。** 设 \(0<\alpha<1\)、\(\nu,T>0\)，且 \(Z,\widehat Z\in AC([0,T];\mathbb C)\) 具有相同零初值。设

\[
D_C^\alpha Z=\nu F(Z),\quad
r=D_C^\alpha\widehat Z-\nu F(\widehat Z),\quad
|r|\le R\in L^\infty(0,T),\quad R\ge0,
\tag{N1}
\]

其中 \(F(z)=-b+dz+z^2/2\)、\(\Re d=-s_0\)、\(\Re Z\le0\)、\(\Re\widehat Z\le\epsilon_R\)、\(\sigma=s_0-\epsilon_R/2>0\)。微分关系和残差界几乎处处成立，状态实部界由连续性逐点成立。设 \(\xi\in AC[0,T]\)、\(\xi(0)=V_0\ge0\)，并要求

\[
q_\alpha=(I^{1-\alpha}\xi)'
=V_0g_{1-\alpha}+g_{1-\alpha}*\xi'\ge0\quad\text{几乎处处}.
\tag{N5}
\]

两指数分别由 \(\nu^{-1}\int_0^T\xi(T-t)D_C^\alpha Z(t)dt\) 及其参考版本定义。令 \(\lambda=\nu\sigma\)，则

\[
|Z-\widehat Z|\le k_\lambda*R,\qquad
|L_T-\widehat L_T|
\le\nu^{-1}(q_\alpha*k_\lambda*R)(T)
\le\nu^{-1}(\xi*R)(T).
\tag{N2}
\]

特别地，若 \(R/\nu\le\delta_F\)，则

\[
|L_T-\widehat L_T|\le\delta_F\int_0^T\xi(s)ds.
\tag{N3}
\]

**证明。** 令 \(e=Z-\widehat Z\)。差商恒等式给出 \(D_C^\alpha e=\nu[d+(Z+\widehat Z)/2]e-r\)，其系数实部不超过 \(-\lambda\)。对 \(v_\varepsilon=(|e|^2+\varepsilon^2)^{1/2}-\varepsilon\) 使用正则性引理，结合 \(|e|^2/(|e|^2+\varepsilon^2)^{1/2}\ge v_\varepsilon\) 及梯度模长不超过 1，得

\[
D_C^\alpha v_\varepsilon+\lambda v_\varepsilon\le R\quad\text{几乎处处}.
\tag{N4}
\]

(AC2) 与 \(\varepsilon\downarrow0\) 给出每个时刻的状态界。绝对 Fubini 给出 \(I^{1-\alpha}\xi=V_0g_{2-\alpha}+g_{2-\alpha}*\xi'\)，其导数即 (N5)，并给出 \(g_\alpha*q_\alpha=\xi\)。因此 \(q_\alpha\in L^1\)、\(\xi\ge0\)。令 \(A_\alpha=I^{1-\alpha}\xi\)，再用绝对 Fubini 和 \(AC\) 分部积分，得到

\[
L_T-\widehat L_T
=\nu^{-1}\int_0^TA_\alpha(T-t)e'(t)dt
=\nu^{-1}(q_\alpha*e)(T).
\tag{CP1}
\]

Fubini 积分由 \(\|\xi\|_\infty T^{1-\alpha}\|e'\|_1/\Gamma(2-\alpha)\) 控制；边界项因 \(A_\alpha(0)=e(0)=0\) 消失。正性给出第一指数界。最后由 \(g_\alpha-k_\lambda=\lambda g_\alpha*k_\lambda\ge0\)，得

\[
0\le q_\alpha*k_\lambda=\xi-\lambda\xi*k_\lambda\le\xi.
\tag{CP2}
\]

结合卷积结合律和非负积分得到其余结论。\(R\) 是物理残差，故因子 \(\nu^{-1}\) 要保留，直到使用 \(R/\nu\le\delta_F\) 才消去。∎

本文保留的原创性主张，是这条 Heston 指数连接、可认证的历史单元权重，以及它们在冻结数值输出完整误差中的落实。凸性、正预解核、圆盘支持函数和单位成本排序属于已有工具。\(q_\alpha\) 的条件仅处理解析传播；概率模型存在性、仿射变换和鞅性质分别核查。

若闭单元 \([a_j,b_j]\) 上有完整历史残差包络 \(R\le R_j\)，则

\[
|L_T-\widehat L_T|
\le\nu^{-1}\sum_jR_j\int_{a_j}^{b_j}(q_\alpha*k_\lambda)(T-s)ds
\le\nu^{-1}\sum_jR_j\int_{a_j}^{b_j}\xi(T-s)ds.
\tag{N6}
\]

第一种权重只有在严格包围后才能用于计算；现有实验实现第二种权重。若定价分区与残差源单元不重合，要对全部相交闭单元取最大残差。任何单元边界都不重启 Caputo 历史。
