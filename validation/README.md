# Verification

The publication supplies separate records for file identity, scientific reconstruction and presentation. The [evidence map](../docs/EVIDENCE.md) connects the mathematical claims to their proofs and data; [COMMANDS.md](../COMMANDS.md) gives the executable checks.

| Record | Scope |
| --- | --- |
| [Source manifest](SOURCE-MANIFEST.json) | Byte sizes and SHA-256 identities of the publication files. |
| [Scientific manifest](../SCIENTIFIC-MANIFEST.json) | Identities of the current manuscript, scientific source and numerical inputs used by the reconstruction driver. |
| [Scientific replay](../SCIENTIFIC-REPLAY.json) | Input and driver identities, stage results, return codes, and the scope of the recorded scientific execution. |
| [Article check](article-check.json) | Identities of the English source, generated article and vector displays, with formula counts and rendering diagnostics. |
| [PDF check](pdf-check.json) | PDF identity, page count and the stated scope of layout, font, link and text-geometry checks. |

The six-stage scientific driver verifies its inputs, copies them to an isolated working directory and binds its execution to the current manuscript. `python reproduce.py --stage-only`, run from the project root, prepares that directory for the individual commands. Readers and generators can write local results, so use a fresh staged tree for a separate experiment.

The default driver reconstructs downstream certificates from saved banks, and `--full` also recomputes the complete structural-sign cover. Continuous-residual generation has its own commands. The replay record states which operations were executed, and the proof-obligation matrix in Appendix E identifies the arithmetic and derivative-bound dependencies of each reader.

Article and PDF checks establish the reported presentation and identity properties: file identities, formula counts, fonts, link targets, page geometry and the pages inspected. Scientific execution records state the author's verification scope, and the commands let a reader repeat every stage.
