# Revision verification

The current paper is in `manuscript/` and `paper/`. This directory records the scope of verification and retains the exact historical proof source required by the saved scientific receipts.

`receipt-bound-proof-source.md` is an archival input with SHA-256 `972c67c876ab0f858b7827f3048aa5ef7bcaa1b0c71d03ba1578e53025cc26f3`. It is not the current manuscript. Earlier transfer and classical-model receipts bind those bytes under the name `manuscript/merged-heston-en.md`. Later public prose revisions changed that path without changing the receipts. The revision resolves this mismatch by supplying the archival bytes only inside a disposable replay tree, while retaining the current manuscript there as `manuscript/current-publication-en.md`.

The numerical banks, scientific generators, readers and original receipt hashes are preserved. `reproduce.py` records both manuscript identities and the explicit mapping in its new replay receipt. `python reproduce.py --stage-only` prepares the same isolated layout for individual commands; run the commands in `COMMANDS.md` from that printed directory. Directly invoking a historical reader against the current manuscript path can correctly fail its historical identity check.

`SCIENTIFIC-CHECK.json` at the repository root retains the earlier author-side execution record. It is distinct from `revision-check.json`, which records the bounded checks performed for this revision. Identity checks and reconstruction from saved banks do not regenerate the continuous residual derivative bounds.

`article-check.json` identifies the current English source, generated article and vector display assets, including formula counts and rendering diagnostics. `pdf-check.json` records the final PDF identities and the scope of page-layout inspection. These presentation checks do not certify the mathematical proofs.
