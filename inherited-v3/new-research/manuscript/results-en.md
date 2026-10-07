## 7. Financial decisions, attribution and output controls

### 7.1. Fixed contracts, units and complete ablation

The original six-month contract uses twelve strikes \(K_i=3700+100i\), \(0\le i\le11\), forward \(F=4221.86\), discount \(D=1\), and the fixed forward-variance curve in (2.4). Prices and task errors are in index points. The position multiplier is one; no exchange-specific currency notional is inferred. Candidate changes affect \(\alpha\) while leaving the curve and other parameters fixed. The three-candidate profile \(.52,.60,.90\) is a finite comparison and excludes several original bid/ask bands; it is not a successful market calibration or a continuous optimum.

The complete \(K=4400\) minus \(K=4500\) task bound is compared below. Each row retains its actual output, signed centre, included finite frequencies, strip, true tail and arithmetic. Displayed upper bounds are rounded upward. The quarter-year study recomputes its maturity-specific reference integral, true-transform envelopes and tails; its upstream full-history certificate is lawfully restricted to the shorter horizon. It does not reuse a six-month exponent or tail value.

| Maturity and stage | Complete joint bound, points | Matched signed marginal bound, points | Interpretation |
|---|---:|---:|---|
| Six months: global state propagation | 1.397612096 | — | Original failed one-point task |
| Six months: finite history, same global residual | 0.378598956 | — | Principal propagation improvement; unchanged output and centre |
| Six months: local envelope, original used nodes | 0.367258782 | — | About 3% further bound reduction |
| Six months: all finite high nodes, global envelope | 0.132245064 | 0.158585551 | High-frequency certification and centre change are included |
| Six months: all finite high nodes, local envelope | 0.115215934 | 0.137896018 | Both methods certify 0.25 points |
| Three months: through 64, global envelope | 1.207557898 | 1.545191542 | Failed 0.25-point task |
| Three months: through 128, global envelope | 0.351318692 | 0.408293698 | Failed 0.25-point task |
| Three months: through 128, local envelope | 0.233318843 | 0.252393939 | Only the joint method certifies 0.25 points |

The first finite-history reduction is about 72.91%, calculated against the displayed old complete bound. It is a reduction of a guaranteed error bound, not an observed reduction of true pricing error or trading loss. The six-month high-frequency refinement legally changes the centre from approximately \(-0.166762218\) to \(-0.081698202\) points. Its improvement therefore cannot be assigned wholly to common-error geometry. The last row compares equal output, centre, node radii and remainders, and isolates a decision changed by retaining the shared error variables. Its time-local refinement was fixed after the failed global stage and is an exploratory transfer experiment, rather than a retrospectively preregistered result.

### 7.2. Twenty-eight portfolio directions

Let \(e_i\) select strike \(K_i\). We keep the exact holdings below, without rescaling them to make a budget pass. Gross weight means \(\sum_i|w_i|\). Every threshold is an absolute error in index points for the specified holding vector.

| Family | Exact direction | Count | Gross weight |
|---|---|---:|---:|
| Adjacent spreads | \(e_i-e_{i+1},\ 0\le i\le10\) | 11 | 2 |
| Adjacent butterflies | \(e_i-2e_{i+1}+e_{i+2},\ 0\le i\le9\) | 10 | 4 |
| Wide spreads | \(e_0-e_3,e_3-e_6,e_6-e_9,e_0-e_{11}\) | 4 | 2 |
| Positive baskets | \(\frac1{12}\sum_{i=0}^{11}e_i,\ \frac16\sum_{i=0}^5e_i,\ \frac16\sum_{i=6}^{11}e_i\) | 3 | 1 |

All methods in each matched comparison use identical upstream radii. At a 0.5-point budget and \(\alpha=.52\), finite-history joint bounds certify 28/28 portfolios against 13/28 signed marginal bounds. At a 0.25-point budget, the corresponding counts are 10/28 against 1/28 for \(\alpha=.60\), and 20/28 against 13/28 for \(\alpha=.90\). At the looser one-point budget for \(.52\), both new methods certify 28/28; that improvement alone cannot isolate the shared structure. A lawful payoff intersection produces no additional tightening in the tested setting. Failure to certify means that this outer bound is insufficient, not that the true error exceeds the threshold.

### 7.3. Prespecified nearby candidates under the original quotes

The original twelve half-year quotes, forward F=4221.86, discount D=1,
and all other model parameters are fixed. Before computing new results we
froze alpha={0.520,0.525,0.530,0.540,0.550}, a first layer N=1024, and an
upgrade of **all five** candidates to N=2048 if any adjacent joint comparison
remained unresolved. Every point has a newly generated continuous reference
field and a complete closed-time residual bank. Fourier nodes through 64,
all omitted finite nodes through 128, true infinite tails, strip remainder,
reference arithmetic and original quote-conversion intervals are paid.

The objective is the original normalized midpoint loss
\(J=\frac1{24}\sum_i(c_i-m_i)^2\), using normalized calls. Index-point squared units would require multiplication by \(F^2\). Here the tiny target interval halfwidth is only
outward arithmetic error in converting the fixed bid/ask-price midpoint;
it is not the market bid/ask halfwidth. Ranking does not establish a uniform
winner for arbitrary quote targets inside those market bands.
A Taylor support enclosure preserves common
Fourier disks in its linear term and charges the full coordinate-radius
quadratic remainder. Its same-radius marginal comparison uses the identical
upstream certificate. Errors across different alpha candidates are not
assumed jointly correlated.

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

The first layer retained its unresolved close pairs and triggered the frozen
all-candidate upgrade. The final finite grid has alpha=0.520 as a strict minimum.
This is a five-point comparison, not a continuous calibration optimum. All
five candidates remain incompatible with at least one original bid/ask row;
the finite-set result therefore does not identify a market-calibrated model.


Both layers fully generate every closed-cell residual entry: 15,754,230 entries, 5,130 reference exponents and 10,250 true-transform envelopes in total. Separate readers check complete coverage and maxima, reconstruct all exponents, coefficients and objectives, and reject deliberate corruptions; they share the stated rigorous primitives rather than independently rederive every residual derivative.

### 7.4. Why certify a frozen fast output?

The use case is validation of a stored or externally fixed output: an existing pricing-library audit, a reproducible historical result, or a production output that cannot be replaced in the task being checked. When the reference is already available and output replacement is allowed, directly returning its certified centre is an appropriate control. Centre-correcting the fast output is another control and must include the rounding of both the stored correction and final addition. The reference route does not automatically become an economical online solver merely because its downstream support function is inexpensive.

A separately frozen descriptive control reuses the complete \(N=2048,\alpha=.52\) residual bank with 128 history bins. Every intersected closed source cell contributes to each bin maximum, and all weights are outwardly enclosed. All five methods below use the same model, six-month \(4400-4500\) spread, 0.25-point tolerance, reference centre, node radii, strip and true-tail budget. This control does not change the prespecified nearby-grid experiment.

| Output | Complete joint, points | Matched marginal, points | Joint 0.25-point decision |
|---|---:|---:|---|
| Frozen Padé | 0.394999331 | 0.514096070 | UNRESOLVED |
| Direct reference (binary64) | 0.228237113 | 0.347333852 | PASS |
| Fast + stored correction | 0.228237113 | 0.347333852 | PASS |
| BL core, 512 steps | 0.229082759 | 0.348179497 | PASS |
| BL core, 1024 steps | 0.228534686 | 0.347631424 | PASS |

All five matched marginal bounds remain above 0.25 points. Direct reference and corrected fast values happen to have the same complete bound in this instance; their actual stored values are checked separately. Exact dyadic arithmetic charges the reference return, stored correction and final addition. For these freely replaceable outputs, the reference is simpler than delivering the unchanged fast result. The joint structure still changes the decision for the reference and BL outputs. The BL 512-to-1024 difference is a diagnostic, not its certified error.

The certificate is not free. Its generation encloses 2,100,735 continuous frequency-by-cell residual entries, 513 reference exponents and 1,025 true-transform node bounds, plus the infinite tail and 12,300 price coefficients. Full reading checks all these entries and reconstructs the exponents, coefficients and decisions. Each additional portfolio evaluates 1,025 shared-disk support terms and the complete remainder; 28 portfolios reuse the same bank without further residual generation. This is reuse across directions at one parameter and maturity, not reuse across unverified model parameters.

| Additional output construction | Deterministic mathematical work |
|---|---|
| Original Padé output | 352 Fourier values; 256 Jacobi samples per frequency |
| Direct returned reference | Return the already generated, fully charged centre with binary64 rounding |
| Corrected fast output | Store one correction and perform one binary64 addition per price |
| BL core, 512 steps | 67,371,264 history scalar-vector products; 2,626,560 transformed Riccati evaluations |
| BL core, 1024 steps | 269,222,400 history scalar-vector products; 5,253,120 transformed Riccati evaluations |

These are typed work counts, not interchangeable floating-point operations or a total-cost ratio. The field generation, outward transcendental evaluations and verification remain distinct from nominal output construction. No speed or machine-performance advantage is inferred. Complete ledgers record the additional exponent-quadrature work and both coarse failed control stages.


### 7.5. What the experiments do and do not establish

The modern-method comparison reimplements the modified-Adams Riccati core described by Boyarchenko et al.; it does not reproduce their full SINH deformation or Conformal Bootstrap. Agreement between two discretizations is a numerical diagnostic, not an interval certificate. Any comparison to a complete certified output must pay the independent reference, tails, arithmetic and verification costs required by that guarantee.

The fixed refinement menu certifies reliable termination when the complete task radius meets the budget. Its minimum number of actions assumes that every alternative radius is already certified and every action has unit cost. We retain those assumptions and do not infer minimum work for an unknown menu. Work spent constructing all alternatives remains part of certificate generation. Model fit, market uncertainty, transaction costs and global continuous calibration remain outside the output-error guarantee.
