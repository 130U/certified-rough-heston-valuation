# Verification

The publication supplies separate records for file identity, scientific reconstruction and presentation. The [evidence map](../EVIDENCE.md) connects the mathematical claims to their proofs and data; [COMMANDS.md](../COMMANDS.md) gives the executable checks.

| Record | Scope |
| --- | --- |
| [Source manifest](../SOURCE-MANIFEST.json) | Byte sizes and SHA-256 identities of the publication files. |
| [Scientific manifest](../SCIENTIFIC-MANIFEST.json) | Identities of the current manuscript, scientific source and numerical inputs used by the reconstruction driver. |
| [Scientific replay](../SCIENTIFIC-REPLAY.json) | Input and driver identities, stage results, return codes, and the scope of the recorded scientific execution. |
| [Article check](article-check.json) | Identities of the English source, generated article and vector displays, with formula counts and rendering diagnostics. |
| [PDF check](pdf-check.json) | PDF identities, page counts and the stated scope of layout, font, link and text-geometry checks. |

The six-stage scientific driver verifies its inputs, copies them to an isolated working directory and binds its execution to the current manuscript. `python reproduce.py --stage-only`, run from the project root, prepares that directory for the individual commands. Readers and generators can write local results, so use a fresh staged tree for a separate experiment.

The default driver reconstructs downstream certificates from saved banks. `--full` also recomputes the complete original structural-sign cover. Fresh continuous-residual generation has separate commands and dependencies. The replay record states which operations were executed; the proof-obligation matrix in Appendix E identifies the retained arithmetic and derivative-bound dependencies.

Article and PDF checks establish the reported presentation and identity properties. All-page contact-sheet inspection is distinct from line-by-line proofreading, and neither is a certification of mathematical proofs. Scientific execution records describe the author's verification scope; external independent reproduction is a separate undertaking.
