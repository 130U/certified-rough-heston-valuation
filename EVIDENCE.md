# Evidence and reproduction

The [revision verification receipt](validation/revision-check.json) records the checks performed for the 26 October 2026 revision, including exact reassembly of the matched quarter-year bounds and the original quote-band incompatibilities. The [historical proof-source mapping](validation/README.md) keeps the current paper distinct from the archival bytes named by earlier scientific receipts.

The [integrated replay receipt](SCIENTIFIC-REPLAY.json) records a successful run of all seven default driver stages for this revision, including all eight candidate/output-control checks, the dissipative-kernel reader, the secondary audit and the supplementary classical readers. This run did not request the optional complete structural-sign cover and did not regenerate the continuous residual derivative banks.

The [online paper](ARTICLE.md), [English PDF](paper/paper.pdf) and [Chinese PDF](paper/paper-zh.pdf) present the revision of 26 October 2026. The [revision note](REVISION.md) records its relationship to the preceding manuscript. [SOURCE-MANIFEST.json](SOURCE-MANIFEST.json) inventories the publication files; [SCIENTIFIC-MANIFEST.json](SCIENTIFIC-MANIFEST.json) binds the scientific inputs, source and numerical banks. The [`paper` release](https://github.com/130U/certified-rough-heston-valuation/releases/tag/paper) provides the publication package.

The evidence follows the mathematical dependencies of the paper.

| Claim or calculation | Proof, data and verification |
| --- | --- |
| Exact Riccati trajectory and propagation of a continuous residual | [Model and regularity](manuscript/merged-heston-en.md), [complete propagation proofs](ARTICLE.md#appendix-c-complete-propagation-proofs-and-analytic-variants), [finite-history source](science/baseline/finite-history), [commands](COMMANDS.md#p1) |
| Residual bounds on complete time cells, including startup | [Residual construction](ARTICLE.md#appendix-d-continuous-certification-and-reliable-refinement), [startup command](COMMANDS.md#s2), [low-frequency cover](COMMANDS.md#r1), [high-frequency cover](COMMANDS.md#r2) |
| Common transform errors and portfolio support | [Joint-error argument](ARTICLE.md#5-portfolio-errors-from-a-common-transform), [exact quarter-year ledger](science/analysis/audit/quarter-exact-ledger.json), [reader commands](COMMANDS.md#q2) |
| Matched history-kernel comparison | [Kernel source](science/analysis/kernel), [generation and reader commands](COMMANDS.md#k1), [experiment accounts](ARTICLE.md#7-matched-decisions-and-scientific-controls) |
| Finite candidate objectives and stored-output controls | [Source](science/experiments), [candidate commands](COMMANDS.md#n1), [output commands](COMMANDS.md#c1), [public ledgers](audit-experiments) |
| Structural domain of the specified rational output | [Algebraic proof](ARTICLE.md#appendix-b-exact-construction-and-structural-certificates), [original structural-sign command](COMMANDS.md#s1) |
| Detailed accounting of the reported certificates | [Audit source](science/analysis/audit), [ledger commands](COMMANDS.md#a1), [verification duties](ARTICLE.md#appendix-e-complete-experiments-and-verification-duties) |
| Supplementary classical Heston results | [English supplement](supplement/classical-heston-en.md), [Chinese supplement](supplement/classical-heston-zh.md), [extension checks](COMMANDS.md#g1) |
| Public file identities | [Source manifest](SOURCE-MANIFEST.json), [checker](verify_source.py), [command](COMMANDS.md#source-identities) |

All 27 numerical banks are included at their original paths under `science/`. The files retain the byte sizes and SHA-256 hashes recorded in the scientific manifest.

| Bank group | Files | Contents |
| --- | ---: | --- |
| [Baseline](science/baseline) | 7 | Fixed reference fields and continuous-residual banks for the finite-history and expanded-reference accounts. |
| [Nearby candidates, N_t = 1024](science/experiments/N1024) | 10 | Five reference fields and their five closed-cell residual banks. |
| [Nearby candidates, N_t = 2048](science/experiments/N2048) | 10 | Five reference fields and their five closed-cell residual banks. |

The quarter-year 4400–4500 spread has complete upper bounds of 0.233318843 index points under joint aggregation and 0.252393939 under signed marginal aggregation. Both use the same stored output, signed reference displacement, 1,025 node radii and remaining error terms. Only the aggregation differs. A 0.25-point budget is therefore certified by the joint bound in this fixed case. These values are upper bounds, not measurements of the actual error.

`SCIENTIFIC-CHECK.json` records the author's saved-bank acceptance checks. `reproduce.py` reads the published banks and reconstructs downstream prices, objectives and decisions. `--full` also recomputes the original complete structural-sign cover; it does not regenerate every continuous residual derivative bound. [Appendix E](ARTICLE.md#appendix-e-complete-experiments-and-verification-duties) identifies the shared arithmetic and generator dependencies. The [separate generation commands](COMMANDS.md#separate-continuous-generation) describe those additional operations and their cache behaviour.

The finite-candidate comparison ranks the specified five candidates under the recorded objective. It is not a continuous calibration result, and all five candidates remain incompatible with at least one original bid/ask row. The supplementary classical Heston arguments do not establish a complete annual monetary certificate and are not inputs to the rough Heston result.

File-identity checks, saved-bank reconstruction and fresh continuous generation have different scopes. Readers that independently reassemble an expression can still share arithmetic primitives or derivative bounds with a generator. The proof-obligation matrix records those dependencies. Author-side execution records should be distinguished from external independent reproduction.
