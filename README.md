# Certified Joint Pricing Errors in Rough Heston

Mathematical finance research by **Theodore Ouyang**.

**[Read the article](ARTICLE.md)**

I carry a continuous fractional Riccati residual through the pricing exponent to a complete rough Heston price certificate. The bounds retain the initial curve term and full fractional history, then preserve the Fourier errors shared by different strikes. Finite omitted frequencies, strip quadrature, the true infinite tail and outward rounding remain in the same price-unit error budget.

The work combines fractional analysis with validated computation. Matched comparisons cover 28 portfolio directions and a five-point nearby roughness grid. The error ledgers separate history weighting, shared-error aggregation and reference uncertainty, including budgets that remain unresolved.

## Main result

For a quarter-year 4400–4500 call spread at roughness 0.52 and position multiplier one, retaining shared Fourier errors changes whether the same stored output can be certified to a 0.25-index-point budget:

| Complete error upper bound | Index points | Meets the 0.25-point budget |
| --- | ---: | :---: |
| Joint certificate | 0.233318843 | Yes |
| Signed marginal certificate | 0.252393939 | Unresolved |

Both calculations use the same output, reference centre, node radii and remainders. The difference comes from aggregating the common Fourier errors. These are guaranteed upper bounds relative to the model price.

| Completed result | Mathematical scope |
| --- | --- |
| Finite-history pricing-error envelope | Curve-weighted bound under nonexpansion; sharper resolvent bound under positive dissipation |
| Shared Fourier error certificates | 28 specified portfolio directions with matched marginal and joint comparisons |
| Nearby finite-candidate comparison | Five roughness values, 0.52, 0.525, 0.53, 0.54 and 0.55, with fixed market quotes |
| Actual-output certificates | Frozen Padé, direct-reference, corrected-output and modified-Adams controls with identified reference banks |

Each result retains the model assumptions and configuration stated in the article. The classical common-state and trial-field extensions are developed in separate appendices.

<details>
<summary>中文简介</summary>

本研究由 Theodore Ouyang 完成，将连续分数阶 Riccati 残差接到完整定价误差，并保留不同执行价共享的 Fourier 扰动。季度价差的匹配比较中，联合证书通过 0.25 点预算，边际证书仍无法判定。论文给出完整证明链、误差分账和验证程序。

</details>

## Verification

[Code and evidence](EVIDENCE.md) · [Current release](https://github.com/130U/certified-rough-heston-valuation/releases/tag/paper)

The repository contains scientific source, exact error ledgers and verification procedures. The complete numerical banks are retained by the author; full saved-bank reconstruction requires those banks. [Appendix E](ARTICLE.md#appendix-e-complete-experiments-and-verification-duties) specifies the recomputation scope and shared dependencies.

<details>
<summary>Check the public source</summary>

From the repository root:

```text
python -B verify_source.py
```

This checks file identities. The [command index](COMMANDS.md) gives the saved-bank readers, downstream reconstruction and separate continuous-generation commands, together with their input requirements.

</details>

## Research timeline

Research began in the second half of 2023. The main writing took place in the first half of 2024. The project was published on GitHub in 2026.

[theodore.oy2025@gmail.com](mailto:theodore.oy2025@gmail.com) · [10@alumni.duke.edu](mailto:10@alumni.duke.edu)

© Theodore Ouyang. All rights reserved.
