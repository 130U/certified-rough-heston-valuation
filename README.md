# Certified Joint Pricing Errors in Rough Heston

Deterministic certificates for rough Heston pricing outputs, preserving the Fourier errors shared across strikes.

[Read the paper](ARTICLE.md) · [English PDF](paper/paper.pdf) · [Code and evidence](EVIDENCE.md)

Research by **Theodore Ouyang**.

Pricing several strikes reuses one Fourier transform. This project keeps the common complex perturbation in the error calculation, carries a continuous fractional Riccati residual through the pricing exponent, and certifies the resulting prices and portfolio directions. Every complete budget includes its reference centre, finite omitted frequencies, strip quadrature, true infinite tail and outward arithmetic.

## When shared errors change a decision

For the **quarter-year 4400–4500 call spread**, fractional order $`\alpha=.52`$ ($`H=.02`$), and position multiplier one:

| Complete error upper bound | Index points | Meets the 0.25-point budget |
| --- | ---: | :---: |
| Joint certificate | **0.233318843** | Yes |
| Signed marginal certificate | 0.252393939 | Unresolved |

Both certificates use the same stored output, reference centre, 1,025 node radii and remainders. Only the aggregation of shared Fourier errors changes. The [exact rational ledger](science/analysis/audit/quarter-exact-ledger.json) records every contribution; [Section 7.6](ARTICLE.md#76-matched-ledgers-and-certificate-resolution) explains the matched comparison.

The bounds concern numerical error relative to the specified model price. An unresolved budget does not establish that the actual error exceeds it.

## Verify the published inputs

The public repository and the [paper snapshot](https://github.com/130U/certified-rough-heston-valuation/tree/paper) include **all 27 numerical banks**, alongside the manuscript, scientific source and exact ledgers. [SCIENTIFIC-MANIFEST.json](SCIENTIFIC-MANIFEST.json) fixes their paths, byte sizes and SHA-256 hashes.

Clone the paper snapshot and verify its inputs from the repository root:

```text
git clone --branch paper --depth 1 https://github.com/130U/certified-rough-heston-valuation.git rough-heston
cd rough-heston
python -X utf8 -B verify_source.py
python -X utf8 -B reproduce.py --manifest-only
```

These commands check public-file and scientific-input identities, including all numerical banks. They do not execute the scientific calculations.

**Reconstruction status.** The current public inputs pass both root identity checks, but `reproduce.py --full` stops at the English-manuscript SHA-256 check in [the classical reference manifest](science/baseline/reference/code/classical/MANIFEST.json), which still identifies a different manuscript version. The complete driver has not passed on this public snapshot.

The reconstruction driver is designed to read the banks and rebuild downstream prices, objectives and certificate decisions in an isolated working copy; `--full` also recomputes the original structural-sign cover. It records its steps in `SCIENTIFIC-REPLAY.json`. [COMMANDS.md](COMMANDS.md) gives the pinned dependency installation, reconstruction entry points and separate continuous-residual generation commands. On Windows, use a short checkout path for the nested working copy.

Both reconstruction modes retain the identified arithmetic primitives and saved residual-generator bounds as dependencies; they do not regenerate every continuous derivative. [Appendix E](ARTICLE.md#appendix-e-complete-experiments-and-verification-duties) specifies what each check recomputes and inherits. The paper's recorded acceptance runs were performed by the author.

## The proof and its applications

The central chain is **continuous residual → finite-history exponent bound → common transform disks → complete output-error set**. The propagation theorem retains the initial curve term and physical scaling. It gives a curve-weighted envelope under nonexpansion and a sharper resolvent envelope under positive dissipation.

[Sections 2–5](ARTICLE.md#2-model-units-and-fixed-configurations) specify the model, assumptions and pricing construction. [Appendices C–D](ARTICLE.md#appendix-c-complete-propagation-proofs-and-analytic-variants) give the regularity, propagation and continuous-residual proofs.

| Result | Certified scope |
| --- | --- |
| Finite-history pricing envelope | Full-time residual and regularity hypotheses; nonexpansive and dissipative cases with certified history weights. |
| Shared Fourier error accounts | 28 specified portfolio directions with matched marginal comparisons and reported unresolved budgets. |
| Nearby candidate comparison | Five fixed fractional orders: .520, .525, .530, .540 and .550, under unchanged quotes and model inputs. |
| Actual-output controls | Stored Padé, direct-reference, corrected-output and modified-Adams calculations with identified reference banks. |
| Rational-output structure | The specified construction at all real frequencies and positive times for $`\alpha\in[.52,.60]`$, $`\rho\in[-.744501,-.744499]`$ and zero Riccati mean reversion. |

The rational approximation and endpoint-matching method come from **Gatheral–Radoicic**. The paper certifies their specified construction on the stated structural domain; a separately generated reference field supplies the price-error certificate. [Related work](ARTICLE.md#12-related-work) identifies the analytical and computational dependencies.

The five-point objective ranking establishes a finite-set comparison. Every candidate remains incompatible with at least one original bid/ask row. The classical Heston appendices provide common-state and trial-field extensions; their terminal witness and thirteen-function diagnostic leave a complete annual monetary certificate open.

<details>
<summary>中文简介</summary>

本研究将连续分数阶 Riccati 残差接到完整定价误差，并保留不同执行价共享的 Fourier 扰动。在季度价差的匹配比较中，联合证书通过 0.25 点预算，边际证书仍无法判定。论文给出证明链、精确误差分账与验证程序；27 个数值银行已完整公开，公开文件与科学输入身份校验通过。完整重建驱动目前仍受旧英文稿哈希失配阻塞；连续残差重新生成的命令及各项检查的依赖见验证文档。

</details>

## Research timeline

Research began in the second half of 2023. The main writing took place in the first half of 2024. The project was published on GitHub in 2026.

[theodore.oy2025@gmail.com](mailto:theodore.oy2025@gmail.com) · [10@alumni.duke.edu](mailto:10@alumni.duke.edu)

© Theodore Ouyang. All rights reserved.
