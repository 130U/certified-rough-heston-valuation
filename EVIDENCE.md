# Evidence and reproduction

The [online paper](ARTICLE.md), [English PDF](paper/paper.pdf) and [Chinese PDF](paper/paper-zh.pdf) present the mathematical argument. The evidence below follows its dependencies, from the exact Riccati trajectory to the complete portfolio error bound.

| Claim or calculation | Proof, data and verification |
| --- | --- |
| Exact Riccati trajectory and propagation of a continuous residual | [Model and regularity](manuscript/merged-heston-en.md), [complete propagation proofs](ARTICLE.md#appendix-c-complete-propagation-proofs-and-analytic-variants), [finite-history source](science/baseline/finite-history), [commands](COMMANDS.md#p1) |
| Residual bounds on complete time cells, including startup | [Residual construction](ARTICLE.md#appendix-d-continuous-certification-and-reliable-refinement), [startup command](COMMANDS.md#s2), [low-frequency cover](COMMANDS.md#r1), [high-frequency cover](COMMANDS.md#r2) |
| Common transform errors and the exact support of the joint outer error set | [Joint-error argument](ARTICLE.md#5-portfolio-errors-from-a-common-transform), [exact quarter-year ledger](science/analysis/audit/quarter-exact-ledger.json), [reader commands](COMMANDS.md#q2) |
| Matched history-kernel comparison | [Kernel source](science/analysis/kernel), [generation and reader commands](COMMANDS.md#k1), [experiment accounts](ARTICLE.md#7-matched-decisions-and-scientific-controls) |
| Finite candidate objectives and stored-output controls | [Source](science/experiments), [candidate commands](COMMANDS.md#n1), [output commands](COMMANDS.md#c1), [public ledgers](audit-experiments) |
| Structural domain of the specified rational output | [Algebraic proof](ARTICLE.md#appendix-b-exact-construction-and-structural-certificates), [structural-sign command](COMMANDS.md#s1) |
| Complete numerical accounting | [Audit source](science/analysis/audit), [ledger commands](COMMANDS.md#a1), [verification duties](ARTICLE.md#appendix-e-complete-experiments-and-verification-duties) |
| Public file identities | [Source manifest](SOURCE-MANIFEST.json), [checker](verify_source.py), [command](COMMANDS.md#source-identities) |
| Article and PDF production | [Rendering instructions](RENDERING.md), [article receipt](validation/article-check.json), [PDF receipt](validation/pdf-check.json) |

## Matched portfolio result

The quarter-year 4400–4500 call spread has complete error upper bounds of **0.233318843 index points** under joint aggregation and **0.252393939** under signed marginal aggregation. Both use the same stored output, signed reference displacement, 1,025 node radii and remaining error terms. Changing the aggregation tightens the upper bound by approximately **7.56%** and certifies the **0.25-point budget**. These are guaranteed upper bounds relative to the model price; the support formula is exact for the constructed outer error set.

## Scientific inputs

All **27 numerical banks** are included under `science/`. [SCIENTIFIC-MANIFEST.json](SCIENTIFIC-MANIFEST.json) records the byte sizes and SHA-256 identities of the manuscript, scientific source and inputs used by the driver. [SOURCE-MANIFEST.json](SOURCE-MANIFEST.json) inventories the complete publication package.

| Bank group | Files | Contents |
| --- | ---: | --- |
| [Baseline](science/baseline) | 7 | Fixed reference fields and continuous-residual banks for the finite-history and expanded-reference accounts. |
| [Nearby candidates, N_t = 1024](science/experiments/N1024) | 10 | Five reference fields and their five closed-cell residual banks. |
| [Nearby candidates, N_t = 2048](science/experiments/N2048) | 10 | Five reference fields and their five closed-cell residual banks. |

The production output uses the third-order rational approximation of Gatheral and Radoicic. Its structural certificate covers alpha in [.52, .60], rho in [-.744501, -.744499], zero Riccati mean reversion, all real frequencies and positive times. The independent reference supplies the pricing-error enclosure. The paper states the hypotheses and dependencies of these two arguments separately.

## Verification scope

The six-stage driver in [reproduce.py](reproduce.py) checks the input identities, creates an isolated copy tied to the current manuscript, and runs the frontier accounts, correlation checks, correlation controls, candidate and output experiments, dissipative-kernel reader, and exact audit reader. [SCIENTIFIC-REPLAY.json](SCIENTIFIC-REPLAY.json) records the manuscript and manifest identities, stage outputs, return codes and execution scope. The `--full` option additionally recomputes the complete original structural-sign cover.

Saved-bank reconstruction uses the identified continuous-residual derivative bounds and strict arithmetic dependencies. It does not regenerate every continuous bound. The [separate generation commands](COMMANDS.md#separate-continuous-generation) specify those operations and their cache behaviour. [Appendix E](ARTICLE.md#appendix-e-complete-experiments-and-verification-duties) identifies the obligations that each reader recomputes and the inputs it shares with a generator.

The finite-candidate comparison ranks the specified five candidates under the recorded objective. All five remain incompatible with at least one original bid/ask row; a finite ranking is separate from continuous calibration and market compatibility. File-identity checks, saved-bank reconstruction, continuous generation and mathematical proof have distinct roles. The [verification guide](validation/README.md) also distinguishes scientific execution records from presentation checks and external independent reproduction.
