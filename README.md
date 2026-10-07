# Certified Joint Pricing Errors in Rough Heston — V3.1

**Theodore Ouyang**

V3.1 is an editorial edition of the fixed V3 research release. It clarifies the presentation and author chronology while retaining the numerical results, scientific code, saved evidence and recorded V3 acceptance. Author-reported chronology: the underlying research was conducted in 2023; the principal articles were written in 2024; the materials were uploaded to GitHub in 2026. The merged manuscript's additional proofs, experiments and verification records belong to the 2026 revision. See [the author chronology](AUTHOR-CHRONOLOGY.md).

[English PDF](https://github.com/130U/certified-rough-heston-valuation/releases/download/v3.1.0-editorial-20261007/Theodore-Ouyang-Merged-Heston-EN.pdf) · [中文 PDF](https://github.com/130U/certified-rough-heston-valuation/releases/download/v3.1.0-editorial-20261007/Theodore-Ouyang-Merged-Heston-ZH.pdf) · [Editorial overlay ZIP](https://github.com/130U/certified-rough-heston-valuation/releases/download/v3.1.0-editorial-20261007/Theodore-Ouyang-Heston-V3.1-Editorial-20261007.zip) · [V3.1 release](https://github.com/130U/certified-rough-heston-valuation/releases/tag/v3.1.0-editorial-20261007)

The editable manuscripts are [English](manuscript/merged-heston-en.md) and [Chinese](manuscript/merged-heston-zh.md). [The editorial response](EDITORIAL-RESPONSE-ZH.md) describes this edition's changes. The current article explains shared transform errors, finite-history propagation and the certification of actual pricing outputs; its classical extensions retain their stated proof and financial scope.

## Scientific evidence and reproduction

The complete numerical evidence remains the fixed [V3 scientific ZIP](https://github.com/130U/certified-rough-heston-valuation/releases/download/v3.0.0-research-20261007/Theodore-Ouyang-Heston-V3-Evidence-20261007.zip), with its [checksum file](https://github.com/130U/certified-rough-heston-valuation/releases/download/v3.0.0-research-20261007/SHA256SUMS.txt). Its SHA256 is:

```text
f4c038b736ec01b3dd9c4e2dcff733665b5b7997f99ee26b64eb5cff0f2ab120
```

Download that named V3 ZIP, verify its checksum, and extract it into a separate directory. Run the following commands from the extracted V3 archive's root:

```text
python -m pip install -r requirements.txt
python reproduce.py --full
```

The V3.1 editorial overlay and GitHub's generated source archives omit the 27 large NPZ banks needed for this execution. The new repository root contains editorial verification; it does not replace the extracted V3 scientific execution directory.

The V3 driver verifies its scientific manifest and performs saved-evidence acceptance in a fresh copy. `--full` includes the original complete structural-sign cover. It does not regenerate every saved continuous residual derivative bound. The explicit obligation matrix in the V3 archive's `v3/audit-experiments/appendix-e-en.md` distinguishes retained evidence, independent reconstruction and separate generator commands.

## Editorial and scientific identities

The original V3 source, including its manifests, is retained without byte changes under `inherited-v3/`. The original `SCIENTIFIC-MANIFEST.json` and `FRESH-ACCEPTANCE.json` belong to that fixed V3 evidence. They do not certify the V3.1 README, revised prose or new PDF bytes.

The new `EDITORIAL-MANIFEST.json` links the edited material to the fixed V3 scientific identities. The new root `SOURCE-MANIFEST.json` identifies the current source tree. The root editorial verifier checks this bridge and the inherited source identities; it does not rerun the scientific bank.

The recorded V3 fresh acceptance is author-side execution, not external referee replication. Its scope and dependencies remain unchanged. Actual-output bitwise replay is checked on the executing floating-point implementation; universal bitwise equality is not assumed. The paper retains unresolved budgets and candidate comparisons, and the classical terminal strictness result does not imply a complete annual monetary pricing certificate.

Public reproducibility metadata retain mathematical inputs, software dependency versions, evidence identities and verification scope.
