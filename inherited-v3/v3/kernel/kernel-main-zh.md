### 耗散定价核的严格计算

定理3.3中的正核可以直接严格计算，不必总以曲线核替代。对 \(\sigma\ge0\)，令 \(\lambda=\nu\sigma\)，定义

\[
K_\lambda=q_\alpha*k_\lambda,\qquad
\eta_{\rm res}=\nu^{-1}(K_\lambda*R)(T),\qquad
0\le K_\lambda=\xi-\lambda\,\xi*k_\lambda\le\xi.
\tag{KR01}
\]

完整残差历史、状态零初值、曲线初值项和物理因子 \(\nu^{-1}\) 均保持定理3.3的原条件。标量正分数阶逆属于已有工具 [Kopteva2021v2, SimonCM2015]；本次落实的是模型特定定价核权重的严格包围，以及它们与同一实际输出完整证书的连接。

**推论（非扩张有限历史传播）。** 定理3.3允许 \(\sigma\ge0\)。当 \(\sigma=0\) 时，

\[
k_0=g_\alpha,\qquad K_0=\xi,\qquad
|L_T-\widehat L_T|\le\nu^{-1}(\xi*R)(T).
\tag{KR02}
\]

这不需要除以耗散率，也不需要无限期限状态半径。曲线条件仍为 \(q_\alpha\ge0\)，而非 \(\xi'\ge0\)；随机模型合法性继续独立验证。原有AC正则性桥接及完整比较证明保留于附录C。

对固定曲线(2.4)，记 \(A_0=\alpha_0\)，并保留其独立曲线参数 \(\lambda_\xi\)。在计算域 \(\lambda T^\alpha<1\) 上，

\[
W_\lambda(t)=\int_0^tK_\lambda(s)\,ds
=\sum_{n=0}^\infty(-\lambda)^n t^{1+n\alpha}
\left[
\frac{\theta}{\Gamma(2+n\alpha)}
+(V_0-\theta)E_{A_0,2+n\alpha}
(-\lambda_\xi t^{A_0})
\right].
\tag{KR03}
\]

单元 \([a_j,b_j]\) 的权重为 \(W_\lambda(T-a_j)-W_\lambda(T-b_j)\)。附录C给出绝对级数尾界与区间差证明。实现固定采用十二层外级数、六十四层曲线级数及100位向外二进原语，包围完整Mittag–Leffler核泛函，显式支付截断和舍入余项；不使用普通浮点Mittag–Leffler值作保证。

**定理3.3的修改。** 将 \(\sigma>0\) 改为 \(\sigma\ge0\)，其余状态、残差、AC、初值、\(q_\alpha\)、尺度及定价泛函条件全部保留。原证明只需要 \(\lambda\ge0\)，零耗散时的分数阶逆为 \(I^\alpha\)。另行涉及 \(1/\sigma\) 的全局状态公式仍要求 \(\sigma>0\)。
