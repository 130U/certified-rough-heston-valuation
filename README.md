# Certified Joint Pricing Errors in Rough Heston

**Theodore Ouyang**

[Paper](ARTICLE.md) · [English PDF](paper/paper.pdf) · [Results](science/analysis/audit/quarter-exact-ledger.json) · [Code and evidence](EVIDENCE.md)

Rough Heston captures volatility with memory through a fractional Volterra equation. Its option prices depend on a complex fractional Riccati solution, followed by Fourier integration. Turning an approximate solution into a rigorous price guarantee requires carrying its error through that entire chain. For a portfolio, there is a further mathematical opportunity: different strikes share the same transform errors, so their combined uncertainty has more structure than separate price intervals reveal.

I develop a certificate that preserves both the time history of the Riccati error and the geometry shared across strikes. The continuous residual measures how closely an approximate trajectory satisfies the Riccati equation. My central theorem carries it through a finite-history envelope into the pricing exponent, retaining the initial forward-variance curve and physical scaling. Under positive dissipation, a resolvent kernel gives a sharper envelope by weighting each part of the residual history according to its effect on the final exponent. This connects fractional stability theory directly to a computable financial error bound.

The second step is to treat each uncertain Fourier value as one common complex disk. I combine the strike coefficients before taking the support bound, preserving cancellation within a spread or portfolio. Translating this joint set to the actual stored pricing output gives a certificate for the numerical price someone would use. The centre displacement, quadrature remainder, omitted frequencies, infinite tail and arithmetic all enter the complete result.

For the quarter-year **4400–4500 call spread**, with fractional order $`\alpha=.52`$ ($`H=.02`$) and unit position under the fixed model, retaining the shared geometry lowers the complete error upper bound from **0.252393939 to 0.233318843 index points**, approximately **7.56%**. The output, reference centre and error inputs stay fixed; only their joint aggregation changes.

That difference changes the decision at a **0.25-point accuracy budget**: the joint certificate proves that the output meets the budget, while the signed marginal certificate leaves it unresolved. The significance is that mathematical information already present in the pricing formula can turn an inconclusive numerical guarantee into a conclusive portfolio guarantee, without changing the pricing output.

I also establish an exact structural theorem for the specified Gatheral–Radoicic third-order rational approximation. Matching-system determinants and polynomial-sign arguments prove nonsingularity, separation of the denominator from zero and left-half-plane structure over a continuous parameter domain: $`\alpha\in[.52,.60]`$, $`\rho\in[-.744501,-.744499]`$, zero Riccati mean reversion, all real frequencies and positive times. This replaces checks at selected frequencies with a theorem covering the stated domain.

The joint error set makes portfolio weights part of the mathematical certificate. It carries the common transform structure into the position being valued, and also supports certified comparisons of objectives across fixed candidate parameters.

The rational approximation and endpoint-matching method are due to Gatheral–Radoicic. My contributions are the finite-history pricing envelope, its composition with shared complex-disk geometry, the resulting decision certificates and the exact structural domain proof.

Research began in the second half of 2023. The main writing took place in the first half of 2024. The project was published on GitHub in 2026.

[Calculation guide](COMMANDS.md)

[theodore.oy2025@gmail.com](mailto:theodore.oy2025@gmail.com) · [10@alumni.duke.edu](mailto:10@alumni.duke.edu)

© Theodore Ouyang. All rights reserved.
