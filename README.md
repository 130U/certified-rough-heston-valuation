# Certified Joint Pricing Errors in Rough Heston

**A mathematical framework that certifies rough Heston pricing outputs while preserving the errors shared across strikes.**

Research by **Theodore Ouyang** · [Paper](ARTICLE.md) · [English PDF](paper/paper.pdf) · [Code and evidence](EVIDENCE.md)

Different strikes reuse the same Fourier transform. This research retains that shared structure throughout the certificate, connects a continuous fractional Riccati residual to the pricing exponent, and encloses the error of the actual stored output. In a matched quarter-year call-spread experiment, the joint certificate gives **0.233318843 index points**, passing a **0.25-point budget** that the signed marginal certificate cannot certify.

## A measurable decision improvement

For the **4400–4500 call spread**, maturity $`T=1/4`$, fractional order $`\alpha=.52`$ ($`H=.02`$), and unit position:

| Complete error upper bound | Index points | Certifies the 0.25-point budget |
| --- | ---: | :---: |
| **Joint certificate** | **0.233318843** | **Yes** |
| Signed marginal certificate | 0.252393939 | Unresolved |

The complete upper bound is approximately **7.56% lower**. Both columns use the same stored output, reference centre, **1,025 node radii** and remainders; only the aggregation of the shared Fourier errors changes. The [exact rational ledger](science/analysis/audit/quarter-exact-ledger.json) records every contribution and the threshold decision. [Section 7.6](ARTICLE.md#76-matched-ledgers-and-certificate-resolution) gives the matched comparison.

## Mathematical contributions

The proof chain is **continuous residual → finite-history exponent bound → shared transform disks → complete output-error set**.

**Finite-history propagation into price units.** The central theorem connects the complex fractional Riccati residual to the model's pricing exponent, retaining the initial forward-variance curve term and physical scaling. It supplies a curve-weighted envelope under nonexpansion and a sharper positive-resolvent envelope under dissipation. Certified history weights make the result computable. [Theorem 3.1](ARTICLE.md#3-finite-history-propagation-nonexpansion-and-dissipation) and [Appendix C](ARTICLE.md#appendix-c-complete-propagation-proofs-and-analytic-variants) give the theorem and full propagation proofs.

**Joint certification of the actual output.** One common complex perturbation at each frequency produces a joint price-error set across strikes. Translating that set from the reference centre to the stored fast output yields complete certificates for prices, portfolio directions and finite-candidate objectives. The account includes the centre displacement, finite omitted frequencies, strip quadrature, true infinite tail and outward arithmetic. [Sections 4–5](ARTICLE.md#4-continuous-certificates-and-complete-fourier-prices) construct the certificate.

**A full-frequency structural proof.** Exact matching-system and polynomial-sign certificates establish nonsingularity, denominator separation and left-half-plane structure for the specified Gatheral–Radoicic third-order rational construction. The continuous domain covers $`\alpha\in[.52,.60]`$, $`\rho\in[-.744501,-.744499]`$, zero Riccati mean reversion, all real frequencies and positive times. [Section 6](ARTICLE.md#6-structure-of-the-specified-rational-output) and [Appendix B](ARTICLE.md#appendix-b-exact-construction-and-structural-certificates) contain the algebraic proof and correlation extension.

## Experiments and evidence

| Research output | Scale and purpose | Reading path |
| --- | --- | --- |
| Portfolio certificates | **28 fixed directions** with exact thresholds and matched joint/marginal comparisons | [Portfolio study](ARTICLE.md#72-twenty-eight-portfolio-directions), [threshold ledger](science/analysis/audit/portfolio-exact-thresholds.csv) |
| Nearby candidate comparison | **Five fractional orders**: .520, .525, .530, .540 and .550; two time grids with unchanged quotes and model inputs | [Candidate study](ARTICLE.md#73-prespecified-nearby-candidates-under-the-original-quotes), [source](science/experiments) |
| Actual-output controls | Padé, direct-reference, corrected-output and modified-Adams calculations | [Matched controls](ARTICLE.md#74-why-certify-a-frozen-fast-output), [commands](COMMANDS.md#c1) |
| Published numerical inputs | **27 complete banks**: 7 baseline, 10 at $`N_t=1024`$, 10 at $`N_t=2048`$ | [Evidence inventory](EVIDENCE.md), [scientific manifest](SCIENTIFIC-MANIFEST.json) |

The recorded experiments separate the effects of history weighting, shared geometry, reference uncertainty and centre changes. Their numerical guarantees concern the specified model prices and outputs. Exact fractions, complete banks, source identities and author execution records provide a direct path from each reported decision to its inputs.

The rational approximation and endpoint-matching method are due to **Gatheral–Radoicic**. This project's contributions are the finite-history pricing certificate, shared-output error geometry, matched decision experiments and certified structural domain. [Contributions and dependencies](ARTICLE.md#11-contributions-and-dependencies) identify how the proof chains fit together; [related work](ARTICLE.md#12-related-work) supplies the attribution.

## Inspect the research package

Read the [paper](ARTICLE.md) for the theory, [EVIDENCE.md](EVIDENCE.md) for the experiments, and [COMMANDS.md](COMMANDS.md) for calculation and verification entry points. To inspect the published snapshot and verify its file and scientific-input identities:

```text
git clone --branch paper --depth 1 https://github.com/130U/certified-rough-heston-valuation.git rough-heston
cd rough-heston
python -X utf8 -B verify_source.py
python -X utf8 -B reproduce.py --manifest-only
```

[Appendix E](ARTICLE.md#appendix-e-complete-experiments-and-verification-duties) maps the proof obligations, author-side acceptance records and computational dependencies. The command guide provides individual readers, downstream reconstruction and separate continuous-residual generation procedures.

## Research timeline

Research began in the second half of 2023. The main writing took place in the first half of 2024. The project was published on GitHub in 2026.

[theodore.oy2025@gmail.com](mailto:theodore.oy2025@gmail.com) · [10@alumni.duke.edu](mailto:10@alumni.duke.edu)

© Theodore Ouyang. All rights reserved.
