# Revision of 26 October 2026

This revision reorganizes *Certified Joint Pricing Errors in Rough Heston* around the valuation question and its mathematical dependencies. The preceding public baseline is [183ec258](https://github.com/130U/certified-rough-heston-valuation/commit/183ec258). The current [online paper](ARTICLE.md), [English PDF](paper/paper.pdf) and [Chinese PDF](paper/paper-zh.pdf) present the revised exposition.

## Argument and presentation

The paper now begins with the error of a fixed portfolio valuation. It specifies the exact Riccati–Volterra solution before introducing a reference trajectory, obtains the residual equation by subtraction, and derives the history kernel by composing the fractional comparison with the pricing functional. The startup powers are explained through the Riccati equation. The common-transform representation then leads to a portfolio support function and the equality condition for separate error bounds.

These explanations make the construction and its dependencies explicit. The exact-solution statement collects the regularity and existence argument used in the earlier appendix. The support equality condition spells out the relevant equality case of the complex triangle inequality. Neither is presented here as a new research theorem. The revised order describes the logical derivation; the [provenance note](PROVENANCE.md) separately records the project chronology.

The model specification and general arguments precede numerical configurations. The H, Q and N configurations now appear with the experiments, where their role in a matched comparison can be assessed. The Padé formula remains an established production output with a separate structural proof. Its algebraic properties and the independently certified reference continue to have distinct roles.

## Results carried forward

The revision retains the previously reported numerical inputs and results. In particular, the quarter-year 4400–4500 spread retains the complete joint upper bound of 0.233318843 index points and signed marginal upper bound of 0.252393939. Their comparison holds the stored output, reference centre, 1,025 radii and remaining error terms fixed. It certifies the 0.25-point budget under joint aggregation in that configuration.

The finite-history bounds, dissipative-kernel accounts, finite-candidate comparisons, output controls and specified rational structural domain remain subject to their stated hypotheses. The five nearby candidates remain incompatible with at least one original bid/ask row. The finite comparison does not establish a continuous calibration optimum.

This revision does not claim a newly generated experiment or a new numerical rate. Any rerun of a verification procedure has the scope described in [COMMANDS.md](COMMANDS.md), including its use of saved banks and shared arithmetic or derivative bounds.

## Material moved or synchronized

| Material | Current location and role |
| --- | --- |
| Main argument and Appendices A–E | [English source](manuscript/merged-heston-en.md), [Chinese source](manuscript/merged-heston-zh.md), generated article and PDFs |
| Former Appendices F–G | [English classical Heston supplement](supplement/classical-heston-en.md) and [Chinese supplement](supplement/classical-heston-zh.md); original equation labels and limitations retained |
| Former research timeline | [PROVENANCE.md](PROVENANCE.md), with the earlier chronology distinguished from this revision date |
| Repository introduction and evidence map | [README.md](README.md) and [EVIDENCE.md](EVIDENCE.md), aligned with the revised argument |
| Article and PDF production | [RENDERING.md](RENDERING.md), including the reproducible article builder |
| Scientific data and verification procedures | Existing `science/` paths and [COMMANDS.md](COMMANDS.md); all 27 numerical banks retained |

The supplementary classical Heston results do not enter the rough Heston certificate. Their incomplete annual monetary calculation and thirteen-function diagnostic remain explicitly qualified. Moving this material clarifies the main paper's scope while preserving it for inspection.

Publication identities are recorded in [SOURCE-MANIFEST.json](SOURCE-MANIFEST.json); scientific identities are recorded in [SCIENTIFIC-MANIFEST.json](SCIENTIFIC-MANIFEST.json). File identity, reconstruction of reported results and fresh continuous-residual generation remain separate verification tasks.

The revision also repairs historical proof-source lookup in the replay driver. Earlier receipts bind an older manuscript hash, even though the public manuscript has since changed. Their original hashes are retained. The driver supplies the matching archival proof source only inside its isolated work tree and keeps the current publication source alongside it. [The verification note](validation/README.md) records this mapping; scientific generators, readers and numerical banks are unchanged.
