### A continuous, quantitatively bounded correlation extension

The original domain was chosen to contain the public-data example's correlation and roughness candidates while keeping the six-condition construction fixed. The sign cover established a continuous roughness interval and all frequencies; it was not intended as a theorem over typical calibration boxes. Strict signs imply persistence in correlation. The following result makes that implication quantitative without replacing a continuous cover by a sampled grid.

**Theorem 6.2 (certified correlation persistence).** The conclusions of Theorem 6.1 hold for

\[
\alpha\in[13/25,3/5],\qquad
\rho\in[-744501/10^6,-744499/10^6],\qquad
\kappa=0,
\tag{RP1}
\]

at every real Fourier frequency and every positive time.

**Proof.** Retain the frequency compactification \(\eta=u/(1+u)\), \(0\le\eta\le1\), and the original unnormalized polynomials \(\Delta,F_j,B_j,D_j\). Write \(S_b=-\rho[(1-\eta)+2i\eta]/(2h)\), \(h^2=\eta^2+(1-\eta)^2/4\). Then \(|S_b|=|\rho|\), \(\Re S_b\ge0\) for negative \(\rho\), \(A^2=1+S_b^2\), and \(R=(A+S_b)^{-1}=A-S_b\). Throughout \(|\rho|\le3/4\), the square-root branch remains fixed because \(\Re A^2\ge1-\rho^2>0\). Consequently,

\[
|A|^{-1}\le8/5,\quad |A'|\le6/5,\quad
|(A^{-1})'|\le384/125,\quad |R|\le1,\quad |R'|\le11/5,
\tag{RP2}
\]

where primes denote real \(\rho\) derivatives. The identity \(|R|\le1\) follows from \(|A+S_b|^2\ge1\): the terms \(\Re A\,\Re S_b\) and \(\Im A\,\Im S_b\) are nonnegative, while \(|A|^2=|1+S_b^2|\ge1-|S_b|^2\). Also \(\Re R>0\), since \((\Re A)^2-(\Re S_b)^2=(|1+S_b^2|+1-|S_b|^2)/2>0\).

For the \(\alpha\)-dependent scalars of Theorem 6.1, exact outward endpoint enclosures give

\[
0<p\le2/3,\quad0\le v\le1/3,\quad
1\le m\le3/2,\quad0<\zeta\le2/3.
\tag{RP3}
\]

Here \(p\) decreases and \(v,m\) increase on the stated interval, while \(\zeta\) decreases. The gamma-ratio assertions follow from the increasing digamma function; \(m\ge1\) also follows from log convexity of \(\Gamma\). None depends on \(\rho\).

Apply product-rule modulus bounds to the original polynomial formulas. For every \((\alpha,\eta)\), the resulting exact rational constants \(L_{B,j},L_{D,j}\) satisfy

\[
|\partial_\rho B_j|\le L_{B,j},\qquad
|\partial_\rho D_j|\le L_{D,j}.
\tag{RP4}
\]

They are assembled using pairs \((M,N)\), meaning \(|f|\le M\), \(|f'|\le N\), with addition \((M_1+M_2,N_1+N_2)\) and multiplication \((M_1M_2,N_1M_2+M_1N_2)\). This yields a finite, directly checkable rational derivation rather than a numerical derivative estimate.

Let \(m_{B,j}(C),m_{D,j}(C)\) be the exact original sign lower bounds on a continuous \((\alpha,\eta)\) cell \(C\) at \(\rho_0=-1489/2000\). A cell is certified throughout the target correlation interval whenever all bounds

\[
m_{B,j}(C)-10^{-6}L_{B,j}>0,\qquad
m_{D,j}(C)-10^{-6}L_{D,j}>0
\tag{RP5}
\]

hold. The mean-value theorem proves this sufficient test; it uses a derivative enclosure, not numerical differentiation. It certifies 182002 original leaves and 79758 finer leaves. For the remaining cells, directly evaluate the original complex polynomial formulas with \(\rho\), \(\alpha\) and \(\eta\) all interval valued. Exact outward dyadic arithmetic certifies strict \(B_j>0\) and \(D_j<0\) on 19808 additional closed cells.

The original complete midpoint tree and the exact local splice trees verify that these 281568 cells cover the entire \((\alpha,\eta)\) rectangle without gaps or interior overlap. Their exact area is \(2/25\); each cell carries the entire correlation interval, giving exact three-dimensional volume \(1/6250000\). Hence the raw signs hold for every point of the stated domain. In particular \(\Delta\ne0\), the normalized denominator coefficients have positive real part, and all real numerator coefficients of the half-plane test are negative. The original algebraic implication gives (RP1), including \(\eta=1\), the infinite-frequency limit. Conjugacy supplies negative frequencies. ∎

This is a narrow local robustness result: the total correlation width is \(2\times10^{-6}\). It does not establish a typical broad calibration box or a new price experiment at an altered correlation. The direct interval supplement is explicitly exploratory: its protocol was frozen after the derivative-only attempt left positive unresolved area. The evidence retains that partial result and the separately valid conservative fallback.

The independent reader checks every saved original sign, the original 422481-node partition tree, the local splice geometry, the independently assembled derivative majorants and all 19808 direct cells through separate Cramer matrices and numerator-polynomial convolution. The dyadic primitives and saved original sign generation remain shared dependencies; every old interval-polynomial evaluation is not regenerated. Exact large fractions stay in the machine ledger. Neither a sampled correlation grid nor an assertion of continuity replaces any cell in this proof.
