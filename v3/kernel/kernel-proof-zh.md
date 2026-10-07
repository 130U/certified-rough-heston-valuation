### C.5. 严格耗散权重与非扩张边界

保留定理3.3的完整条件及AC比较证明，只允许 \(\sigma\ge0\)。正则化误差模长满足 \(D_C^\alpha v_\varepsilon+\nu\sigma v_\varepsilon\le R\) 几乎处处；当 \(\lambda=\nu\sigma=0\) 时，同一正逆仍成立，且 \(k_0=g_\alpha\)。连续终点极限与定价泛函连接给出(KR01)–(KR02)，不引入 \(1/\sigma\)。\(q_\alpha\) 中的初值项 \(V_0g_{1-\alpha}\) 和因子 \(\nu^{-1}\) 全部保留。

**命题（累计权重的严格级数）。** 设 \(0<\alpha,A_0<1\)、\(0\le V_0\le\theta\)，固定曲线为
\(\xi(t)=\theta+(V_0-\theta)E_{A_0}(-\lambda_\xi t^{A_0})\)，其中 \(\lambda_\xi\ge0\)，并保留 \(q_\alpha\ge0\)。当 \(\lambda\ge0\)、\(\lambda T^\alpha<1\) 时，(KR03)在 \([0,T]\) 成立。若在指标 \(M\) 之前截断，全部遗漏外级数满足

\[
\left|W_\lambda(t)-\sum_{n=0}^{M-1}(-\lambda)^nW_n(t)\right|
\le
\frac{\theta t(\lambda t^\alpha)^M}{1-\lambda t^\alpha},
\quad
W_n(t)=\int_0^t(\xi*g_{n\alpha})(s)\,ds.
\tag{KR10}
\]

\(g_0\) 表示恒等卷积，因此 \(W_0(t)=\int_0^t\xi\)。

**证明。** 已有预解恒等式 \(k_\lambda+\lambda g_\alpha*k_\lambda=g_\alpha\) 与 \(q_\alpha*g_\alpha=\xi\) 给出
\(K_\lambda+\lambda g_\alpha*K_\lambda=\xi\)。Neumann级数的各项为
\((- \lambda)^n(\xi*g_{n\alpha})\)。因为 \(0\le\xi\le\theta\)，

\[
0\le W_n(t)\le
\frac{\theta t^{1+n\alpha}}{\Gamma(2+n\alpha)}
\le\theta t(t^\alpha)^n.
\tag{KR11}
\]

由对数凸性及 \(\Gamma(1)=\Gamma(2)=1\)，\(\Gamma\) 在 \([2,\infty)\) 递增且不小于一。全部外层分母参数为 \(2+n\alpha\ge2\)，故绝对项的 \(L^1(0,T)\) 范数之和由(KR11)的收敛几何级数控制，允许卷积、积分与求和交换，给出Volterra恒等式及其唯一预解解，并证明(KR10)。第一遗漏指标严格为 \(n=M\)：保留十二项时遗漏 \(n\ge12\)，不是 \(n\ge13\)。

为证明唯一性，两个解的差 \(h\in L^1(0,T)\) 满足 \(h=-\lambda g_\alpha*h\)。迭代得到 \(\|h\|_1\le\lambda^nT^{n\alpha}\|h\|_1/\Gamma(1+n\alpha)\)。充分大的 \(n\) 使Gamma参数不小于二，右侧因子不超过趋于零的 \((\lambda T^\alpha)^n\)，故 \(h=0\)。这不需要假定含 \(\Gamma(1+\alpha)\) 的一步卷积算子已经收缩。

展开曲线Mittag–Leffler函数并使用Beta卷积恒等式，得到

\[
W_n(t)=t^{1+n\alpha}
\left[
\frac{\theta}{\Gamma(2+n\alpha)}
+(V_0-\theta)\sum_{m=0}^{\infty}
\frac{(-\lambda_\xi t^{A_0})^m}
{\Gamma(2+n\alpha+mA_0)}
\right].
\tag{KR12}
\]

当 \(w=\lambda_\xi t^{A_0}<1\) 时，所有内层分母参数亦不小于二，在指标 \(L\) 之前截断的余项满足

\[
\left|\sum_{m=L}^{\infty}
\frac{(-w)^m}{\Gamma(2+n\alpha+mA_0)}\right|
\le \frac{w^L}{1-w}.
\tag{KR13}
\]

采用绝对尾界，不需要未经证明的交错项单调性。本实例通过严格区间检验 \(w<1\) 和 \(\lambda T^\alpha<1\)。包括 \(V_0-\theta\) 的有符号系数先与向外区间相乘再求和，幂、Gamma和指数值都由已识别的二进原语包围。∎

若完整单元 \([a_j,b_j]\) 上有 \(R\le R_j\)，且累计值已包围为 \([W^-(t),W^+(t)]\)，则精确权重属于

\[
\left[
W^-(T-a_j)-W^+(T-b_j),\
W^+(T-a_j)-W^-(T-b_j)
\right].
\tag{KR14}
\]

由 \(0\le K_\lambda\le\xi\)，与非负性及独立认证的曲线权重上界取交是合法的。所得上端 \(\omega_j^+\) 给出

\[
\eta_{\rm res}\le\nu^{-1}\sum_jR_j\omega_j^+.
\tag{KR15}
\]

各分区包络取遍全部相交闭源单元，包括仅在端点相交者。源单元从零开始覆盖完整区间，不重启Caputo历史。

生产器通过已有严格power-field moment除以 \(\Gamma(1+n\alpha)\) 计算 \(W_n\)，保留十二外层项。独立读取器直接实现(KR12)，保留十四外层项与六十四内层项，不导入生产器累计函数或power-field moment函数；检查报告的残差泛函区间包含它更紧的独立区间，继而核验全部变换半径取小及完整价格。Gamma、对数、指数和二进系数原语是共享依赖，上游残差证明沿用，不冒称重新独立推导。
