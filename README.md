# Certified Joint Pricing Errors in Rough Heston

**Theodore Ouyang**

[Paper](ARTICLE.md) · [English PDF](paper/paper.pdf) · [Results](science/analysis/audit/quarter-exact-ledger.json) · [Code and evidence](EVIDENCE.md)

I develop a deterministic framework for certifying rough Heston option prices and portfolio valuations. The central theorem propagates a continuous fractional Riccati residual through the full time history into the pricing exponent, retaining the initial forward-variance curve and physical scaling. It provides a curve-weighted envelope under nonexpansion and a sharper resolvent envelope under positive dissipation.

I combine this propagation result with a joint price-error set that retains the common complex Fourier perturbations across strikes. Portfolio coefficients are combined before taking the support bound, preserving cancellation within spreads and other positions. Translation to the stored pricing output includes reference displacement, quadrature, omitted frequencies, the infinite tail and arithmetic.

For the paper’s quarter-year **4400–4500 call spread**, the complete error upper bound is **0.233318843 index points**, certifying a **0.25-point accuracy budget**. With the pricing output and error inputs held fixed, preserving the shared error geometry tightens the matched complete bound by approximately **7.56%**.

I also establish an exact structural theorem for the specified Gatheral–Radoicic third-order rational approximation. Matching-system determinants and polynomial-sign arguments prove nonsingularity, separation of the denominator from zero and left-half-plane structure over a continuous parameter domain: $`\alpha\in[.52,.60]`$, $`\rho\in[-.744501,-.744499]`$, zero Riccati mean reversion, all real frequencies and positive times. This replaces checks at selected frequencies with a theorem covering the stated domain.

The rational approximation and endpoint-matching method are due to Gatheral–Radoicic. My contributions are the finite-history pricing envelope, its composition with shared complex-disk geometry, the resulting decision certificates and the exact structural domain proof.

Research began in the second half of 2023. The main writing took place in the first half of 2024. The project was published on GitHub in 2026.

[Calculation guide](COMMANDS.md)

[theodore.oy2025@gmail.com](mailto:theodore.oy2025@gmail.com) · [10@alumni.duke.edu](mailto:10@alumni.duke.edu)

© Theodore Ouyang. All rights reserved.
