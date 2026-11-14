# Evidence and reproduction

The [online paper](../ARTICLE.md) and its [PDF](../paper/paper.pdf) present the mathematical argument. The evidence below follows its dependencies, from the exact Riccati trajectory to the complete portfolio error bound.

| Claim or calculation | Proof, data and verification |
| --- | --- |
| Exact Riccati trajectory and the residual bound of Theorem 3.1 | [Pricing problem](../ARTICLE.md#2-the-pricing-problem), [residual bound](../ARTICLE.md#3-what-a-riccati-residual-costs), [propagation proofs](../ARTICLE.md#appendix-c-propagation-proofs), [finite-history source](../science/baseline/finite-history), [commands](../COMMANDS.md#p1) |
| Residual bounds on complete time cells, including startup | [Residual construction](../ARTICLE.md#appendix-d-the-certified-reference), [startup command](../COMMANDS.md#s2), [low-frequency cover](../COMMANDS.md#r1), [high-frequency cover](../COMMANDS.md#r2) |
| Common transform errors and the exact support of the joint error set | [Joint-error argument](../ARTICLE.md#5-portfolios-transform-error-as-a-common-factor), [exact three-month ledger](../science/analysis/audit/quarter-exact-ledger.json), [reader commands](../COMMANDS.md#q2) |
| Netting ratios, frequency bands, width scan and market scale | [Netting ratio](../ARTICLE.md#5-portfolios-transform-error-as-a-common-factor), [market-scale source and record](../science/analysis/market), [command](../COMMANDS.md#m1) |
| Matched history-kernel comparison | [Kernel source](../science/analysis/kernel), [generation and reader commands](../COMMANDS.md#k1), [experiment accounts](../ARTICLE.md#7-evidence-from-sp-500-options) |
| Finite candidate objectives and stored-output controls | [Source](../science/experiments), [candidate commands](../COMMANDS.md#n1), [output commands](../COMMANDS.md#c1), [public ledgers](../audit-experiments) |
| Structure of the rational output | [Algebraic proof](../ARTICLE.md#appendix-b-the-rational-output), [structural-sign command](../COMMANDS.md#s1) |
| Complete numerical accounting | [Audit source](../science/analysis/audit), [ledger commands](../COMMANDS.md#a1), [experimental record](../ARTICLE.md#appendix-e-experimental-record) |
| Public file identities | [Source manifest](../validation/SOURCE-MANIFEST.json), [checker](../verify_source.py), [command](../COMMANDS.md#source-identities) |
| Article, figures and PDF | [Rendering instructions](RENDERING.md), [article receipt](../validation/article-check.json), [PDF receipt](../validation/pdf-check.json) |

## Matched portfolio result

The three-month 4400–4500 call spread has complete error upper bounds of **0.233318843 index points** under joint aggregation and **0.252393939** under leg-by-leg aggregation with the signed centre. Both use the same stored output, signed reference displacement, 1,025 node radii and remaining error terms. Changing the aggregation tightens the upper bound by approximately **7.56%** and certifies the **quarter-point tolerance**. These are guaranteed upper bounds relative to the model price; the support formula is exact for the constructed error set.

The stored ratio of the joint to the leg-by-leg coefficient at each of the 1,025 nodes agrees with the closed form of Proposition 5.2 to fifteen digits, and the formula of Theorem 5.1 reproduces the stored joint node support of all 28 six-month positions. The [market-scale record](../science/analysis/market/market-scale.json) holds both comparisons.

## Scientific inputs

All **27 numerical banks** are included under `science/`. [SCIENTIFIC-MANIFEST.json](../SCIENTIFIC-MANIFEST.json) records the byte sizes and SHA-256 identities of the manuscript, scientific source and inputs used by the driver. [SOURCE-MANIFEST.json](../validation/SOURCE-MANIFEST.json) inventories the complete publication package.

| Bank group | Files | Contents |
| --- | ---: | --- |
| [Baseline](../science/baseline) | 7 | Fixed reference fields and continuous-residual banks for the finite-history and expanded-reference accounts. |
| [Nearby candidates, N_t = 1024](../science/experiments/N1024) | 10 | Five reference fields and their five closed-cell residual banks. |
| [Nearby candidates, N_t = 2048](../science/experiments/N2048) | 10 | Five reference fields and their five closed-cell residual banks. |

The quotes are the six-month S&P 500 option quotes of 18 June 2021 published by Jeng and Kiliçman (2021), read at a fixed commit of their data repository. The stored output uses the third-order rational approximation of Gatheral and Radoičić. Its structural certificate covers alpha in [.52, .60] at the calibrated correlation, with a verified neighbourhood rho in [-.744501, -.744499], all real frequencies and positive times. The independent reference supplies the pricing-error enclosure. The paper states the hypotheses and dependencies of these two arguments separately.

## Verification scope

The six-stage driver in [reproduce.py](../reproduce.py) checks the input identities, creates an isolated copy tied to the current manuscript, and runs the frontier accounts, correlation checks, correlation controls, candidate and output experiments, dissipative-kernel reader, and exact audit reader. [SCIENTIFIC-REPLAY.json](../SCIENTIFIC-REPLAY.json) records the manuscript and manifest identities, stage outputs, return codes and execution scope. The `--full` option additionally recomputes the complete structural-sign cover.

Saved-bank reconstruction uses the identified continuous-residual derivative bounds and strict arithmetic dependencies. It does not regenerate every continuous bound. The [separate generation commands](../COMMANDS.md#separate-continuous-generation) specify those operations and their cache behaviour. [Appendix E](../ARTICLE.md#appendix-e-experimental-record) identifies the obligations that each reader recomputes and the inputs it shares with a generator.

The market-scale record reads the quote bands, the certified prices and the stored node supports exactly, and evaluates netting ratios, band shares and the width scan in binary64 from the stored radii. Those derived quantities describe the certificates and are not themselves certificates.

The finite-candidate comparison ranks the specified five candidates under the recorded objective. All five are inconsistent with at least one quoted bid–ask band; a finite ranking is separate from continuous calibration and market compatibility. File-identity checks, saved-bank reconstruction, continuous generation and mathematical proof have distinct roles. The [verification guide](../validation/README.md) also distinguishes scientific execution records from presentation checks and external independent reproduction.
