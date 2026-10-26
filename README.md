# Certified Joint Pricing Errors in Rough Heston

**Theodore Ouyang**

[Paper](ARTICLE.md) · [English PDF](paper/paper.pdf) · [中文 PDF](paper/paper-zh.pdf) · [Evidence](EVIDENCE.md) · [Verification](COMMANDS.md)

Options with the same maturity and model parameters share one characteristic function. Its numerical error therefore enters every strike through known Fourier coefficients. For a portfolio, these coefficients should be combined before their absolute values are taken. This paper develops a deterministic certificate for the error of an already computed rough Heston valuation, retaining that common structure.

The argument starts from the exact fractional Riccati equation. Subtracting a reference trajectory gives a residual error equation; the left half-plane geometry controls its growth. Applying the pricing functional then produces a history kernel determined by the forward variance curve and the positive fractional resolvent. The resulting bound retains the complete history, the initial curve term and the physical scaling. Approximation enters only after these objects and their roles have been specified.

The transform bounds define a joint set of possible price errors. Its support function gives portfolio bounds and identifies when separate price intervals lose information. A complete certificate also accounts for the displacement between the reference and the stored output, finite omitted frequencies, quadrature, the infinite tail and arithmetic. The support formula is exact for this outer error set; the true numerical error need not attain its boundary.

For the specified quarter-year **4400–4500 call spread**, the complete joint upper bound is **0.233318843 index points**, compared with **0.252393939** from signed marginal aggregation. The stored output, reference centre, 1,025 node radii and remaining error terms are identical. Retaining the common errors therefore certifies the **0.25-point budget** in this example. The [exact ledger](science/analysis/audit/quarter-exact-ledger.json) records both accounts. These are error upper bounds relative to the model price.

The principal production output uses the third-order rational approximation of Gatheral and Radoicic. A separate algebraic argument establishes its structural properties for $`\alpha\in[.52,.60]`$, $`\rho\in[-.744501,-.744499]`$, zero Riccati mean reversion, all real frequencies and positive times. The endpoint-matching construction is theirs; an independently certified reference supplies the pricing-error guarantee. Further experiments examine history weights, output replacement and finite candidate comparisons. All five nearby candidates remain incompatible with at least one original bid/ask quote.

The public package includes all **27 numerical banks**. The [verification guide](COMMANDS.md) distinguishes file identities, reconstruction from saved banks and fresh continuous-residual generation. Reconstructing the published results does not by itself regenerate every continuous derivative bound.

This is the **26 October 2026 revision**. See the [revision note](REVISION.md), [source and typesetting guide](RENDERING.md), and [project chronology](PROVENANCE.md). The earlier classical Heston extensions are preserved separately in [English](supplement/classical-heston-en.md) and [Chinese](supplement/classical-heston-zh.md), with their original scope and outstanding obligations.

[theodore.oy2025@gmail.com](mailto:theodore.oy2025@gmail.com) · [10@alumni.duke.edu](mailto:10@alumni.duke.edu)

© Theodore Ouyang. All rights reserved.
