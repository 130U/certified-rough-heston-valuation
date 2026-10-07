# B+C computational evidence audit, 7 October 2026

The audit uses the local `english-heston-release` package as an immutable source and writes all new results in `bc-merged-20261007`. The successful runtime is the bundled Python 3.12.14 with NumPy 2.3.5. The system `python` command did not provide NumPy; no installation was needed. Preflight reported 16,573,128,704 physical bytes and 3,386,277,888 available bytes, sufficient for the documented approximately 1 GiB structural parsing contract. No full LP, field fitting, or regeneration of the omitted classical coefficient bank was attempted.

## Execution and mathematical meaning

| Check | Actual result | What was recomputed |
|---|---|---|
| Rough package manifest | PASS; 77 artifacts, 152,507,109 bytes | All released bytes and documented public identities |
| Structural cover | PASS; 211,241 leaves, 422,481 midpoint-tree nodes, area 2/25 | Complete disjoint cover geometry, exact minima, all saved strict inequalities |
| Full structural sign regeneration | PASS; all 211,241 exact leaf records identical; 194.3172802 seconds; return code 0 | Raw-polynomial 100-bit interval evaluation on every leaf, including all three B margins, six negative-D margins, raw determinant and real-R margins |
| Rough fixed fields and residual receipts | PASS; four exact fields, three residual candidates, 513 nodes each | Field bytes/shapes/guards, source identities, exact adapters and saved all-time envelopes |
| Fresh continuous residual subset | PASS; u=0 and 1/8 in all three fields | Entire closed time cover: 8,189/8,189/4,093 intervals, all four endpoint arrays exactly identical to frozen values |
| Rough price objectives and financial decisions | PASS; 36 prices and actual stored Padé comparisons | Exact rational objective, winner, quote-row and original spread calculations |
| Classical probability/profile regeneration | PASS; 22 rows, 102 bands, 918 profile entries | Twelve 767-step Laplace recursions and all saved model-bound entries, using 160-bit outward arithmetic |
| Classical terminal witness | PASS; 407 checks | Exact primal/dual feasibility, uniqueness, complete rows and feasible-direction witnesses; no LP solve |
| Classical thirteen-dimensional field receipts | PASS as saved arithmetic | All 3,080 mode-cell integral boxes and the displayed envelope lower bound; no coefficient regeneration or archived direct-integration rerun |
| Shared Fourier price-level experiment | PASS; all 1,025 nodes in each of three real cases | Same-output, full-budget spread support, signed reference-fast shift, nested joint intervals, exact budget decisions |
| Independent startup assembly | PASS; all 1,539 actual frequency startups | Direct Caputo inversion and generalized-power residual assembly against the complete frozen residual bounds; no solver or original residual assembly |
| Second shared-coefficient assembly | PASS; all 3,075 node calculations | Stable real trigonometric coefficient identity confirms every reported complete joint radius; exact center, remainder and decision checks |

The structural regeneration is stronger than counting saved signs or confirming a hash: every leaf is evaluated from the exposed raw mathematical relations and compared field for field. Its elementary Gamma, trigonometric and interval routines are the public executed implementation. We do not call that a wholly independent second arithmetic library or formal verification of those primitives. Analytical derivation and scope checking remain necessary. The structural claim remains alpha in [0.52,0.60], rho=-0.7445 and kappa=0, with the stated compactification; the alpha=0.90 pricing case does not enlarge that structural theorem.

An initial full-cover operation with 16 regenerated leaf signs took 16.0525919 seconds. A separate 64-leaf generator sample took 0.4656659 seconds, suggesting approximately 1,537 seconds if naively extrapolated. The completed full run took 194.3172802 seconds because adjacent leaves reuse alpha/Gamma enclosures. The completed measurement replaces the sample estimate; the estimate was never a mathematical assertion.

## R01: semantic rejection tests

`adversarial_checks.py` tests in-memory corrupted copies after deliberately bypassing file-hash checks. A deleted necessary structural leaf is rejected; a flipped strict sign is rejected; an inflated but still positive sign margin is rejected when compared against raw-polynomial regeneration. A corrupted probability-constraint direction and a negative active dual multiplier are rejected by direct rational feasibility checks. Deleted finite Fourier nodes, negative node radii, and a missing true infinite-tail budget are also rejected. The recorded tests all pass. These are semantic controls, not merely digest mismatch tests. They do not demonstrate rejection of every possible malicious program modification.

The startup assembly additionally rejects missing initial cancellation. The second shared-coefficient checker rejects deletion of the signed reference-fast shift in every actual candidate. No artificial input used by these negative controls is presented as financial evidence.

## R03: continuous field delivery and trust boundary

The NPZ field does not merely save solution samples. It delivers exact dyadic startup coefficients A1/A2, the full t/u arrays, and the continuous piecewise-affine remainder LG. The certified function is reconstructed by fractional integration of Gbar, including startup generalized powers. The residual checker operates on that delivered function and closed time intervals; it does not reuse a solver update error as a continuous residual. The field is point-alpha and fixed-frequency, not a continuous-frequency residual certificate.

`residual_spotcheck.py` completed the continuous generator replay on the entire closed time cover for u=0 and u=1/8 in each of the three actual fields. It does not call the original numerical solver. All four physical-residual/startup/half-plane endpoint arrays exactly match the frozen values. The three actual executions covered 8,189/8,189/4,093 closed intervals in 425.6651504/402.7877379/85.9920386 seconds respectively, with process return code 0. These are whole-time but two-frequency spotchecks. This audit does not claim a fresh full 513-node continuous residual generation.

The independent startup assembly in `startup_independent.py` has completed all 1,539 actual frequency cases in 1.6717608 seconds in its final recorded run. It uses direct Caputo inversion and exact generalized-power residual terms, with no solver recurrence, original residual assembly, or binary64 dot product; elementary scalar enclosures are shared. Every fresh first-interval bound is within the complete frozen residual bound. The narrower saved first-cell sub-bounds need not contain an alternative valid enclosure: 20/21/21 low-frequency direct bounds are slightly wider, by at most approximately 0.0141 percent, while all complete residual bounds remain sufficient. Those comparisons are delivered rather than hidden.

## R05: actual common probability object

The classical supplement defines pi_jr as probabilities under the actual correlated projected-Gaussian discrete law Q. The zero atom, one hundred finite bands and final infinite band are explicit. Common-probability inclusion is an analytical statement using an unweighted original-chain probability vector and a weighted Cauchy-Schwarz estimate; it is not inferred by identifying tilted mode-dependent laws. The portable regeneration checks all 22 saved inequalities and all 918 profile values from their declared model formulas. The terminal witness therefore supports its stated outer-set row separation. It does not certify a complete annual payoff-price gain or a trading result.

## R06: field receipt boundary

The original thirteen-dimensional numerical field has an identified coefficient-bank hash but no delivered coefficient bank. Its 3,080 interval integrals and archived 384-bit readback reproduce a positive first-month envelope lower bound exceeding 0.003407444052031154. That lower bound rejects the selected 0.001 PDE-envelope allocation. It does not reject the complete sufficient balance, establish a sufficient conversion fee, or bound actual signed price bias from below. The package cannot regenerate this field from coefficients. Its numerical example should remain archival unless the full construction is delivered; the self-contained analytic trial-field identity can be retained separately.

## Complete financial experiment

`shared_fourier_spread.py` reads the original 4400/4500 spread coefficients and the actual 1,025 node radii. It combines the coefficients before each modulus, includes omitted finite nodes exactly once, adds both grid and true infinite-tail budgets, and retains the signed center difference between the certified reference and actual stored fast output. All joint intervals nest inside the best signed marginal intervals by exact rational comparison.

`verify_shared_fourier.py` does not import that calculator. It independently assembles the coefficient modulus through the stable real identity (sqrt(m1)-sqrt(m2))^2+4sqrt(m1 m2)sin^2(u log(m1/m2)/2). Its outward upper bounds confirm all three reported complete radii. It independently checks the signed center, full remainder, actual-output intervals and exact threshold decisions. The delivered upstream radii and elementary scalar interval library remain shared. The calculator took 3.8270675 seconds in its final recorded run; the second-assembly checker took 1.0261616 seconds. These timings were observed while another audit process was active and are not performance guarantees.

The actual implementation-error upper bound falls from 2.6799303107 to 1.3976120954 index points for alpha=0.52; from 0.8997719752 to 0.5041250131 for alpha=0.60; and from 0.4473110112 to 0.3968079780 for alpha=0.90. These displayed upper bounds are rounded upward. Relative to the best signed marginal certificate, descriptive reductions are 47.8489%, 43.9719%, and 11.2904%. At the primary one-point budget alpha=0.52 remains uncertified; at the two-point sensitivity budget the new joint certificate passes where the best signed marginal certificate fails. At alpha=0.60, retaining signed marginal centers alone already changes the one-point outcome relative to the symmetric marginal triangle bound; that change is not attributed to shared Fourier geometry.

The diagnostic decision contract was written before the coordinator read the new results, after child computation had already occurred. It is not prospective preregistration before computation, and these point budgets do not establish economic suitability. Frozen data, fields, candidates and fast outputs were not reselected. Price-error points are obtained by multiplying normalized errors by the frozen discounted forward DF=4,221.86.

## Portable files and commands

All scripts below discover the source release as the sibling `english-heston-release` directory. Run them with the recorded bundled Python executable or an equivalent Python 3.12/NumPy environment.

```
python evidence_runner.py
python full_structure_verify.py
python adversarial_checks.py
python startup_independent.py
python residual_spotcheck.py
python shared_fourier_spread.py
python spread_decisions.py
python verify_shared_fourier.py
```

`verification.json` records package-check operations and their times. `full-structure-verification.json` and `full-structure-stdout.txt` record the completed all-leaf regeneration. `adversarial-checks.json` records semantic corruption tests. `startup-independent.json` records all direct startup enclosures and the missing-cancellation rejection. `shared-fourier-spread.json` and its three complete node ledgers deliver exact new support calculations. `spread-decisions.json` records exact threshold comparisons; `shared-fourier-independent-verification.json` records the second coefficient assembly and signed-shift negative controls. Fresh continuous audit files retain their precise execution scope; no original frozen source is overwritten.
