### 7.7. Matched ledgers and certificate resolution

The quarter-maturity decision is attributable to shared aggregation. Q2 uses identical actual output, reference centre, 1025 node radii and all remainders in both columns. Finite omitted-node support is zero because every finite node has a nonzero reference. Values below are in index points; exact fractions are retained in quarter-exact-ledger.json.

| Component | Joint | Signed marginal |
| --- | --- | --- |
| Signed centre | -0.149775146827 | -0.149775146827 |
| Absolute centre charge | 0.149775146827 | 0.149775146827 |
| Used-node support | 0.045461793432 | 0.064536889507 |
| Finite omitted-node support | 0.000000000000 | 0.000000000000 |
| Strip remainder | 0.000026654230 | 0.000026654230 |
| True infinite-tail remainder | 0.038055248032 | 0.038055248032 |
| Reference arithmetic | 4.148871871727e-16 | 4.148871871727e-16 |
| Complete upper bound | 0.233318843 | 0.252393939 |

The joint complete bound is 0.233318843 points versus 0.252393939 points for signed marginal aggregation; only the joint certificate passes the 0.25-point budget. The difference 0.019075095 points is entirely the node-support aggregation difference. Complete-bound displays are rounded upward to nine decimal places; component/centre and gap displays are approximate. Every decision and ledger identity uses exact fractional endpoints. Tiny reference arithmetic is displayed separately, and the signed centre is a locator, not an extra additive charge on top of its absolute value.

Every portfolio curve uses the 28 originally fixed and fully specified directions. Exact endpoints, all threshold breakpoints and pass counts are supplied in portfolio-exact-thresholds.csv and portfolio-budget-counts.json. Certification uses the complete rational endpoint condition $B\leq\tau$, including equality. Between-bank plots show descriptive changes; joint versus signed marginal within one bank uses matched radii. No 28-direction quarterly dataset is inferred from the single quarter spread.

| Bank | alpha | Budget points | Marginal | Joint |
| --- | --- | --- | --- | --- |
| H0 | 13/25 | 1/4 | 0/28 | 0/28 |
| H0 | 13/25 | 1/2 | 0/28 | 0/28 |
| H0 | 13/25 | 1 | 0/28 | 3/28 |
| H1 | 13/25 | 1/4 | 0/28 | 2/28 |
| H1 | 13/25 | 1/2 | 13/28 | 28/28 |
| H1 | 13/25 | 1 | 28/28 | 28/28 |
| H1 | 3/5 | 1/4 | 1/28 | 10/28 |
| H1 | 3/5 | 1/2 | 22/28 | 28/28 |
| H1 | 3/5 | 1 | 28/28 | 28/28 |
| H1 | 9/10 | 1/4 | 13/28 | 20/28 |
| H1 | 9/10 | 1/2 | 25/28 | 25/28 |
| H1 | 9/10 | 1 | 27/28 | 28/28 |
| N1 | 13/25 | 1/4 | 0/28 | 0/28 |
| N1 | 13/25 | 1/2 | 0/28 | 4/28 |
| N1 | 13/25 | 1 | 15/28 | 28/28 |
| N2 | 13/25 | 1/4 | 0/28 | 0/28 |
| N2 | 13/25 | 1/2 | 6/28 | 23/28 |
| N2 | 13/25 | 1 | 28/28 | 28/28 |
| N2L | 13/25 | 1/4 | 0/28 | 1/28 |
| N2L | 13/25 | 1/2 | 11/28 | 26/28 |
| N2L | 13/25 | 1 | 28/28 | 28/28 |

The two nearby levels retain all ten unordered pairs, including unresolved ones:

| N_t | Method | Separated pairs | Complete unresolved list |
| --- | --- | --- | --- |
| 1024 | joint | 7/10 | (0.520, 0.525), (0.520, 0.530), (0.525, 0.530) |
| 1024 | marginal | 3/10 | (0.520, 0.525), (0.520, 0.530), (0.520, 0.540), (0.525, 0.530), (0.525, 0.540), (0.530, 0.540), (0.540, 0.550) |
| 2048 | joint | 10/10 | none |
| 2048 | marginal | 7/10 | (0.520, 0.525), (0.520, 0.530), (0.525, 0.530) |

The closest N2 joint separation, alpha=.520 versus .525, is an exact positive gap of 7.382643478687e-10 in normalized squared-midpoint loss. Its endpoint identity is $J_{0, B}-J_{0, A}-H_B-H_A-Q_A$ plus any box-intersection endpoint adjustment. The gap decomposition, including used nodes, finite zero nodes, reference strip/tail/arithmetic and midpoint-conversion arithmetic, is recorded exactly in nearby-pair-resolution.json. This is a fixed original midpoint-loss ranking. The midpoint-conversion arithmetic interval does not represent the market bid/ask width; all five candidates remain separately bid/ask-incompatible.

The unchanged actual half-year 4400–4500 output admits the following complete centre accounting:

| Bank | Signed centre points | Complete radius points | Complete bound points |
| --- | --- | --- | --- |
| H2 | -0.166762218 | 0.200496564 | 0.367258782 |
| H3 | -0.081698202 | 0.050546862 | 0.132245064 |
| H4 | -0.081698202 | 0.033517732 | 0.115215934 |
| N2 | -0.166762218 | 0.261808768 | 0.428570987 |
| N2L | -0.166762218 | 0.228237113 | 0.394999331 |

Expanding H2 to H3 changes the absolute centre charge as well as the paid reference radius; H3 to H4 retains that new centre. N2 to N2L retains its own reference centre and fullremainders. H4 to N2L is a descriptive cross-bank identity, not an ablation. These transitions are exact in frozen-output-centre-account.json, which also reports the common strict-reference certificate floor as a fraction of each BL-core bound. A dominant floor limits what this comparison can establish about intrinsic solver accuracy. When replacement is permitted and the strict reference is already available, returning that reference directly is the simpler workload; frozen-output audit and free replacement answer different tasks.
