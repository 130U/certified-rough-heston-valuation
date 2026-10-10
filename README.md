# Certified Joint Pricing Errors in Rough Heston

Deterministic certificates for stored rough Heston pricing outputs, preserving the Fourier errors shared across strikes.

[Read the paper](ARTICLE.md) · [English PDF](paper/paper.pdf) · [Code and evidence](EVIDENCE.md)

Research by **Theodore Ouyang**.

Pricing several strikes reuses one Fourier transform. This project keeps the common complex perturbation in the error calculation, carries a continuous fractional Riccati residual through the pricing exponent, and certifies the resulting prices and portfolio directions. Every complete budget includes its reference centre, finite omitted frequencies, strip quadrature, true infinite tail and outward arithmetic.

## When shared errors change a decision

For the **quarter-year 4400–4500 call spread**, fractional order $`\alpha=.52`$ ($`H=.02`$), and position multiplier one:

| Complete error upper bound | Index points | Meets the 0.25-point budget |
| --- | ---: | :---: |
| Joint certificate | **0.233318843** | Yes |
| Signed marginal certificate | 0.252393939 | Unresolved |

Both columns use the same stored output, reference centre, 1,025 node radii and remainders. Only the aggregation of shared Fourier errors changes. The [exact rational ledger](science/analysis/audit/quarter-exact-ledger.json) records every contribution; [Section 7.6](ARTICLE.md#76-matched-ledgers-and-certificate-resolution) explains the matched comparison.

The bounds concern numerical error relative to the specified model price. An unresolved budget does not establish that the actual error exceeds it.

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

## Read and verify the evidence

The public checkout contains the manuscript, scientific source, smaller ledgers and verification procedures. **The 27 complete numerical banks are retained in the author's local evidence archive.** Full saved-bank reconstruction requires those banks.

To check the public identities, select the certified [paper release](https://github.com/130U/certified-rough-heston-valuation/releases/tag/paper) and run from its root:

```text
git clone --branch paper --depth 1 https://github.com/130U/certified-rough-heston-valuation.git
cd certified-rough-heston-valuation
python -B verify_source.py
```

This verifies file identities. [COMMANDS.md](COMMANDS.md) separates saved-bank readers, downstream reconstruction and continuous-generation commands, with their input requirements. `reproduce.py --full` reads identified banks, rebuilds downstream results and also recomputes the original structural-sign cover; continuous residual derivatives have separate generation commands.

The acceptance checks are author-side records. Readers share identified arithmetic primitives and residual-generator bounds. [Appendix E](ARTICLE.md#appendix-e-complete-experiments-and-verification-duties) documents what each check recomputes and inherits.

<details>
<summary>中文简介</summary>

本研究将连续分数阶 Riccati 残差接到完整定价误差，并保留不同执行价共享的 Fourier 扰动。在季度价差的匹配比较中，联合证书通过 0.25 点预算，边际证书仍无法判定。论文给出证明链、精确误差分账与验证程序；完整数值银行保存在作者的本地证据档案中。

</details>

## Research timeline

Research began in the second half of 2023. The main writing took place in the first half of 2024. The project was published on GitHub in 2026.

[theodore.oy2025@gmail.com](mailto:theodore.oy2025@gmail.com) · [10@alumni.duke.edu](mailto:10@alumni.duke.edu)

© Theodore Ouyang. All rights reserved.

