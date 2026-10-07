# Certified Joint Pricing Errors in Rough Heston — V5

**Theodore Ouyang**

Author-reported chronology: the underlying research was conducted in 2023; the principal articles were written in 2024; the materials were uploaded to GitHub in 2026. The merged manuscript's additional proofs, scientific code, experiments, evidence assembly and recorded verification belong to the 2026 revision. See [the author chronology](AUTHOR-CHRONOLOGY.md) and its [machine-readable record](CHRONOLOGY.json).

V5 is an editorial and typesetting edition following V3.1. It retains the fixed V3 numerical results, scientific code, saved evidence and recorded acceptance. The editorial edition date is October 7, 2026.

[English PDF](https://github.com/130U/certified-rough-heston-valuation/releases/download/v5.0.0-editorial-20261007/Theodore-Ouyang-Merged-Heston-EN.pdf) · [中文 PDF](https://github.com/130U/certified-rough-heston-valuation/releases/download/v5.0.0-editorial-20261007/Theodore-Ouyang-Merged-Heston-ZH.pdf) · [V5 editorial ZIP](https://github.com/130U/certified-rough-heston-valuation/releases/download/v5.0.0-editorial-20261007/Theodore-Ouyang-Heston-V5-Editorial-20261007.zip) · [V5 release](https://github.com/130U/certified-rough-heston-valuation/releases/tag/v5.0.0-editorial-20261007)

The editable manuscripts are [English](manuscript/merged-heston-en.md) and [Chinese](manuscript/merged-heston-zh.md). [The editorial response](EDITORIAL-RESPONSE-ZH.md) records the revised explanations, navigation and layout. [Rendering documentation](RENDERING.md) records the actual font and page specifications and their dependencies. The article explains shared transform errors, finite-history propagation and certification of actual pricing outputs; its classical extensions retain their stated proof and financial scope.

## Scientific evidence and reproduction

The complete numerical evidence remains the fixed [V3 scientific ZIP](https://github.com/130U/certified-rough-heston-valuation/releases/download/v3.0.0-research-20261007/Theodore-Ouyang-Heston-V3-Evidence-20261007.zip), with its [checksum file](https://github.com/130U/certified-rough-heston-valuation/releases/download/v3.0.0-research-20261007/SHA256SUMS.txt). Its SHA256 is:

```text
f4c038b736ec01b3dd9c4e2dcff733665b5b7997f99ee26b64eb5cff0f2ab120
```

Download that named V3 ZIP, verify its checksum and extract it into a separate working directory. Run these commands from the extracted scientific archive's root:

```text
python -m pip install -r requirements.txt
python reproduce.py --full
```

The V5 editorial ZIP and GitHub's automatically generated source ZIPs omit the 27 large NPZ banks needed for scientific execution. The new repository root checks editorial identities; complete scientific execution uses the separately extracted V3 archive. [COMMANDS.md](COMMANDS.md) supplies complete, copyable commands for each Appendix E obligation and for editorial validation.

The V3 driver verifies the scientific manifest and accepts saved evidence in a fresh copy. `--full` additionally includes the original complete structural-sign cover. Neither mode regenerates every continuous residual derivative bound. The separate generation commands and the matrix in Appendix E identify the retained evidence and shared mathematical dependencies.

## Editorial and scientific identities

The original 472 V3 source files, including their manifests, are retained without byte changes under `inherited-v3/`. The original `SCIENTIFIC-MANIFEST.json` and `FRESH-ACCEPTANCE.json` identify the fixed scientific inputs and recorded V3 acceptance. The edited V5 documents and PDF bytes have their own identity.

The new `EDITORIAL-MANIFEST.json` links V5 to the fixed V3 scientific identities and identifies the preceding V3.1 source revision. The new root `SOURCE-MANIFEST.json` identifies the current source tree. The editorial verifier checks this bridge, the inherited source and the chronology's core dates:

```text
python -B verify_source.py
```

This verification does not rerun the scientific bank. The V3 fresh acceptance is author-side execution, not external referee replication. Actual-output bitwise replay is checked on the executing floating-point implementation; universal bitwise equality is not assumed. Unresolved budgets and candidate comparisons remain visible. Classical terminal strictness does not imply a complete annual monetary pricing certificate.

## 中文说明

据作者陈述：基础研究开展于2023年，主要文章撰写于2024年，材料于2026年上传GitHub。2026年的合稿证明补强、科学代码、实验、证据整理和验收归于实际修订阶段。V5仅改进编辑表达与排版；原V3科学数值、代码、证据及验收身份保持不变。

完整科学复现请下载具名V3科学ZIP，并在其解压目录执行上述命令。V5编辑包和GitHub自动源码ZIP均不含27项大型NPZ银行。公开复现元数据保留数学输入、软件依赖版本、证据身份和检查范围。
