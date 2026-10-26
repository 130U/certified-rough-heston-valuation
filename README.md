# Certified Joint Pricing Errors in Rough Heston

**Theodore Ouyang**

[Paper](ARTICLE.md) · [English PDF](paper/paper.pdf) · [中文 PDF](paper/paper-zh.pdf) · [Evidence](EVIDENCE.md) · [Verification](COMMANDS.md)

This paper develops deterministic error certificates for rough Heston valuations. Starting from the exact fractional Riccati equation, it derives a residual error identity and a finite-history pricing kernel determined by the forward variance curve and the positive fractional resolvent. The resulting propagation bound retains the complete history, the curve's initial value and the physical scaling.

Options with the same maturity and model parameters share one characteristic function. The paper preserves that structure in a joint outer set of price errors and derives its **exact support function**. Combining portfolio coefficients before taking absolute values captures cancellation across strikes. The complete certificate also includes the displacement between the reference and the stored output, finite omitted frequencies, quadrature, the infinite tail and arithmetic.

For the quarter-year **4400–4500 call spread**, joint aggregation lowers the complete error upper bound by **7.56%**, from **0.252393939 to 0.233318843 index points**, and certifies the **0.25-point budget**. The comparison uses the same stored output, reference centre, **1,025 node radii** and remaining error terms. The [exact ledger](science/analysis/audit/quarter-exact-ledger.json) records both accounts.

The accompanying scientific package contains the propagation proofs, a structural certificate for the specified rational output, all **27 numerical banks**, and readers for the reported price and portfolio bounds. The [evidence map](EVIDENCE.md) connects each result to its proof and calculation; the [typesetting guide](RENDERING.md) explains how to build the article and both PDFs from the editable sources.

[theodore.oy2025@gmail.com](mailto:theodore.oy2025@gmail.com) · [10@alumni.duke.edu](mailto:10@alumni.duke.edu)

© Theodore Ouyang. All rights reserved.
