# Fixed-portfolio research and evidence boundary

Three executable routes were considered before the systematic run: (1) fixed spreads, butterflies and positive baskets on the released twelve-strike field; (2) valid payoff-bound intersections on the same signed error output; and (3) new continuous candidate certificates near a genuine decision tie. Routes (1) and (2) were implemented. Route (3) remains open: the three released candidates do not establish a near-tie certificate, and a synthetic tie is only a corruption/decision test.

The contract fixes 11 adjacent call spreads, 10 adjacent equally spaced call butterflies, four wide call spreads and three positive average call baskets. It fixes point budgets 0.25, 0.5, 1 and 2 before these systematic results are read. This is a prospective fixed-direction extension after the original 4400/4500 result was already known, not a preregistration of the complete research. There are 28 directions for each of the three original candidates at the original half-year maturity. The reported unit is the complete weighted price error in index points; gross units are available in every record.

For each direction, symmetric marginal bounds add absolute coordinate error bounds. Best signed marginal bounds first take the exact support of the signed coordinate intervals, preserving the actual reference-minus-fast centre. Shared Fourier bounds use the same centre, all 1025 finite nodes and the complete grid, true infinite-tail and reference-arithmetic remainder. Legal directional intersections intersect the three scalar interval images of the joint, marginal and payoff constraints. This last operation is a valid outer bound, not the exact support of their full feasible-set intersection.

The finite-history scenario retains exactly these weights, outputs, centres and remainders. Its coordinate marginals are also upgraded with the new node radii before comparison. It therefore does not compare upgraded shared radii against obsolete marginal radii. These arithmetic results depend on the finite-history comparison theorem and its continuous half-plane and positive-kernel hypotheses. The independent finite-history checker reconstructs every radius without importing the new propagation program, using the released interval primitives.

## Complete decision counts

| Scenario | alpha | Budget (points) | Symmetric marginal | Best signed marginal | Shared nodes | Legal direction intersection |
|---|---:|---:|---:|---:|---:|---:|
| baseline | 0.52 | 1/4 | 0/28 | 0/28 | 0/28 | 0/28 |
| baseline | 0.52 | 1/2 | 0/28 | 0/28 | 0/28 | 0/28 |
| baseline | 0.52 | 1 | 0/28 | 0/28 | 3/28 | 3/28 |
| baseline | 0.52 | 2 | 3/28 | 3/28 | 25/28 | 25/28 |
| baseline | 0.6 | 1/4 | 0/28 | 0/28 | 1/28 | 1/28 |
| baseline | 0.6 | 1/2 | 0/28 | 0/28 | 6/28 | 6/28 |
| baseline | 0.6 | 1 | 5/28 | 14/28 | 28/28 | 28/28 |
| baseline | 0.6 | 2 | 20/28 | 28/28 | 28/28 | 28/28 |
| baseline | 0.9 | 1/4 | 0/28 | 5/28 | 18/28 | 18/28 |
| baseline | 0.9 | 1/2 | 3/28 | 24/28 | 25/28 | 25/28 |
| baseline | 0.9 | 1 | 10/28 | 27/28 | 27/28 | 27/28 |
| baseline | 0.9 | 2 | 22/28 | 28/28 | 28/28 | 28/28 |
| finite_history | 0.52 | 1/4 | 0/28 | 0/28 | 2/28 | 2/28 |
| finite_history | 0.52 | 1/2 | 4/28 | 13/28 | 28/28 | 28/28 |
| finite_history | 0.52 | 1 | 10/28 | 28/28 | 28/28 | 28/28 |
| finite_history | 0.52 | 2 | 21/28 | 28/28 | 28/28 | 28/28 |
| finite_history | 0.6 | 1/4 | 0/28 | 1/28 | 10/28 | 10/28 |
| finite_history | 0.6 | 1/2 | 6/28 | 22/28 | 28/28 | 28/28 |
| finite_history | 0.6 | 1 | 14/28 | 28/28 | 28/28 | 28/28 |
| finite_history | 0.6 | 2 | 23/28 | 28/28 | 28/28 | 28/28 |
| finite_history | 0.9 | 1/4 | 0/28 | 13/28 | 20/28 | 20/28 |
| finite_history | 0.9 | 1/2 | 3/28 | 25/28 | 25/28 | 25/28 |
| finite_history | 0.9 | 1 | 12/28 | 27/28 | 28/28 | 28/28 |
| finite_history | 0.9 | 2 | 22/28 | 28/28 | 28/28 | 28/28 |

## Signed-marginal-to-joint reduction ranges

Percentages below are computed from complete absolute error bounds, including the unchanged signed centre. The min/max decimals are rounded upward; exact rational reductions are retained in the receipts.

| Scenario | alpha | Direction family | Count | Reduction range (%) |
|---|---:|---|---:|---:|
| baseline | 0.52 | adjacent_spread | 11 | 41.9901–51.1518 |
| baseline | 0.52 | adjacent_butterfly | 10 | 64.6863–74.7785 |
| baseline | 0.52 | wide_spread | 4 | 11.8446–34.4210 |
| baseline | 0.52 | positive_basket | 3 | 56.2001–67.7353 |
| baseline | 0.6 | adjacent_spread | 11 | 36.1080–45.9901 |
| baseline | 0.6 | adjacent_butterfly | 10 | 58.6008–70.8492 |
| baseline | 0.6 | wide_spread | 4 | 15.4678–25.4534 |
| baseline | 0.6 | positive_basket | 3 | 34.7597–56.3791 |
| baseline | 0.9 | adjacent_spread | 11 | 11.2904–30.2294 |
| baseline | 0.9 | adjacent_butterfly | 10 | 35.6088–54.6948 |
| baseline | 0.9 | wide_spread | 4 | 4.8268–34.2018 |
| baseline | 0.9 | positive_basket | 3 | 9.4502–28.7905 |
| finite_history | 0.52 | adjacent_spread | 11 | 16.0847–28.3271 |
| finite_history | 0.52 | adjacent_butterfly | 10 | 34.5228–51.6371 |
| finite_history | 0.52 | wide_spread | 4 | 17.7481–36.7479 |
| finite_history | 0.52 | positive_basket | 3 | 21.7608–28.0523 |
| finite_history | 0.6 | adjacent_spread | 11 | 13.4379–23.4265 |
| finite_history | 0.6 | adjacent_butterfly | 10 | 29.9830–48.8744 |
| finite_history | 0.6 | wide_spread | 4 | 17.4026–26.2196 |
| finite_history | 0.6 | positive_basket | 3 | 15.7278–37.0594 |
| finite_history | 0.9 | adjacent_spread | 11 | 7.2662–21.8717 |
| finite_history | 0.9 | adjacent_butterfly | 10 | 26.8859–46.2402 |
| finite_history | 0.9 | wide_spread | 4 | 4.3067–37.4725 |
| finite_history | 0.9 | positive_basket | 3 | 8.0209–26.1496 |

## Original 4400/4500 spread, unchanged financial output

Each displayed bound is rounded upward to nine decimal places. Decisions use the exact rational values, not these display decimals.

| alpha | Scenario | Symmetric marginal (points) | Best signed marginal (points) | Shared nodes (points) |
|---:|---|---:|---:|---:|
| 0.52 | baseline | 3.593074717 | 2.679930311 | 1.397612096 |
| 0.52 | finite_history | 1.389546121 | 0.476401716 | 0.378598956 |
| 0.6 | baseline | 1.955314596 | 0.899771976 | 0.504125014 |
| 0.6 | finite_history | 1.355135751 | 0.299593131 | 0.235892086 |
| 0.9 | baseline | 0.477838028 | 0.447311012 | 0.396807978 |
| 0.9 | finite_history | 0.445987248 | 0.415460232 | 0.385272195 |

## Failures and limits

The lawful payoff intersection gives zero strict improvements in both 84-case scenarios. This is an observed inactive-constraint boundary: no additional gain is attributed to static shape constraints. The interval intersection remains a directional hull; it is not a computed exact support of the full intersection.

The tightest budgets retain failures even after the improved propagation. The failed decisions are fully included in the 84 paired records. No observed actual bias direction, market trading profitability, calibration-stability guarantee or near-tie candidate success is inferred from certificate widths. Positive baskets can still benefit because the complex Fourier coefficients vary in phase across strikes; cancellation is not restricted to portfolios with negative weights.

The original residual, structural and exponent certificates are reused. Coefficient preparation is reusable across all candidates and directions. Each candidate's twelve coordinate marginal radii are reconstructed from the existing residual receipts. The independent menu receipt distinguishes radius reconstruction, gain sorting and prefix selection.

The fixed upgrade-menu result is an exact minimum number of once-only processing actions among the 513 available new-radius upgrades with unit action costs. It is not runtime-optimal and is not a minimum count of new residual-generation calls. The released raw residuals already exist. A complete gain-ranked policy must first compute all new eligible radii before ranking the savings.

## Fixed-menu comparison at alpha=0.52

For the unchanged original 4400/4500 output and one-point budget, sorting certified savings gives 82 shared-node upgrades, versus 249 same-centre signed-marginal upgrades. Both preserve the complete identical grid, true tail and reference-arithmetic remainder. The marginal menu uses the sum of the two coordinate coefficient moduli; the joint menu uses their combined complex modulus. This is a fixed-menu action-count comparison.

| Menu | Minimum upgrade actions | Last failed bound (points, upward) | First certified bound (points, upward) |
|---|---:|---:|---:|
| joint | 82 | 1.000784992 | 0.996743544 |
| best_signed_marginal | 249 | 1.001611566 | 0.996945007 |

The complete work scope includes independent reconstruction of all 513 eligible radii, sorting and selecting both menus, all-candidate checks of coefficient identity and policy steps, corruption controls, and full three-candidate propagation generation and aggregation, including supplementary actions. This scope includes every eligible action, beyond the successful prefix.

The minimum-count statement follows because all gains are nonnegative and each upgrade is available once: no set of k upgrades can remove more radius than the k largest certified gains. The recorded (k−1)-prefix fails and the k-prefix passes. This proof concerns the fixed menu of already available residual receipts and is independent of how expensive a fresh residual certificate might be.

## Replay and trust boundary


The exact trigonometric coefficient enclosures and original certificates remain explicit shared dependencies. The independent propagation checker additionally uses the alternative closed-form spread coefficient identity for the original 4400/4500 direction and rejects omitted nu, zeroed signed centre, deleted nodes and deleted true tail.
