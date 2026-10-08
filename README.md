# Certified Joint Pricing Errors in Rough Heston

**Theodore Ouyang**  
[theodore.oy2025@gmail.com](mailto:theodore.oy2025@gmail.com) · [10@alumni.duke.edu](mailto:10@alumni.duke.edu)

I develop deterministic error certificates for rough Heston pricing outputs. The paper carries continuous fractional Riccati residuals through the pricing exponent to complete price bounds, preserving Fourier errors shared across strikes.

**[Read the full paper](ARTICLE.md)**

## A financial decision changed by the mathematics

For a matched three-month 4400–4500 call spread, retaining the shared errors changes whether the same stored output can be certified to a 0.25-index-point budget.

| Complete error upper bound | Index points | Meets the 0.25-point budget |
| :--- | ---: | :---: |
| Joint certificate | 0.233318843 | Yes |
| Signed marginal certificate | 0.252393939 | Unresolved |

Both calculations use the same output, reference centre, node radii and remainders. The difference comes from aggregating the common Fourier errors. These are guaranteed upper bounds relative to the model price.

## Research contribution

The finite-history theorem connects a continuous Riccati residual to the pricing functional, keeping the initial curve term, full fractional history and physical scale. Nonexpansion gives a curve-weighted bound; positive dissipation gives a sharper resolvent bound.

The output certificate includes finite omitted frequencies, strip quadrature, the true infinite tail and arithmetic. Shared transform disks give portfolio and finite-candidate objective bounds. The experiments include 28 specified portfolio directions, a five-point nearby roughness grid, output controls and exact error ledgers.

The paper combines fractional analysis, validated numerics and financial task design. Proofs and verification procedures accompany the results, including failed budgets and the limits of the classical extensions.

## 中文简介

本研究由 Theodore Ouyang 完成，将连续分数阶 Riccati 残差接到完整定价误差，并保留不同执行价共享的 Fourier 扰动。季度价差的匹配比较中，联合证书通过 0.25 点预算，边际证书仍无法判定。论文给出完整证明链、误差分账和验证程序。

## Research timeline

Research began in the second half of 2023, and the main writing took place in the first half of 2024. Final work was completed in 2026, when the paper and code were uploaded to GitHub.

研究始于2023年下半年，主要写作在2024年上半年完成。部分收尾工作于2026年完成，论文与代码于同年上传GitHub。

## Verification materials

This repository contains the online paper, scientific source, error ledgers and verification procedures. The complete numerical banks are retained in the author's local evidence archive. Full saved-bank reconstruction requires those banks. The reported acceptance checks were run by the author; they are distinct from external independent reproduction. Appendix E specifies the recomputation scope and shared dependencies.
