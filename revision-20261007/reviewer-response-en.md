# Response to the Internal Review of the B+C Manuscript

We have reorganized B and C around a single question: how can verifiable numerical residuals yield a price-error outer set that preserves shared structure and supports financial decisions? The rough and classical Heston probability models remain separate upstream constructions. Their certified error sets meet at the price level. The preceding Asian manuscript A is cited using the supplied 2024 cover identity. The merger, new proofs, and new computations belong to this revision; they are not retrospectively attributed to that earlier date.

This response distinguishes completed evidence from remaining scope limits. The evidence files below are in `research/bc-merged-20261007/`, unless a released upstream path is specified. The aggregate record `verification.json` now reports `PASS_ALL_COMPLETED_BC_COMPUTATIONAL_AUDITS`; each constituent result has its own stated coverage. We do not assign revised numerical scores to the manuscript.

## R01. Exchangeable computational evidence

The delivery separates stored-record validation, mathematical certificate checking, and fresh regeneration. `full-structure-verification.json` reports successful recomputation of all **211,241** structural leaves from the released raw polynomials with 100-bit outward rational arithmetic, in approximately **194.3 seconds**. The geometric checker separately reconstructs **422,481** tree nodes. This full run is distinguished from the initial 16-leaf check in `verification.json`.

The classical checkers reproduce all 22 probability rows and 918 profile entries and perform 407 exact terminal-witness checks. `adversarial-checks.json` records rejection of deliberately damaged coverage, signs, constraints, nodes, or budgets. Reusing the released interval generator is explicitly disclosed; we do not describe it as an independently implemented transcendental library. Hashes establish object identity, while the mathematical derivations and arithmetic checks establish the claimed inequalities.

## R02. The wider central-frequency T1 dependency

The merged core no longer depends on the wider T1 chain. Its structural theorem retains the independently checkable domain $\alpha\in[.52,.60]$, $\rho=-.7445$, and zero Riccati mean reversion, covering all real frequencies and positive times. Dependent wider-domain implications were removed.

A candidate analytic T1 proof exists in the local preceding manuscript, including Gamma inequalities and Bernstein matrices. We therefore do not claim that no proof exists or that T1 has been disproved. The revision instead avoids an independently unclosed dependency. The $\alpha=.90$ point-price certificate does not enlarge the continuous structural domain. See `math-audit.md` and manuscript Sections 3 and 13.

## R03. Continuous residuals rather than solver-update errors

The manuscript defines the complete reference function $\widehat Z=I^\alpha\bar G$ from frozen coefficients. Initial fractional powers, exact cancellation, interpolation interfaces, physical scaling, and full closed-time envelopes are retained.

`startup-independent.json` reports direct Caputo inversion and startup reconstruction at all **1,539** candidate-frequency combinations. Every reconstructed startup upper bound lies within the corresponding frozen **complete residual radius**. This does not assert reproduction of every narrower first-cell subbound.

`residual-spotcheck.json` reports successful fresh regeneration of the complete closed-time cover $[0,1/2]$ at $u=0,1/8$ for each of the three candidates: six candidate-frequency combinations, with 8,189, 8,189, and 4,093 time subintervals respectively. All four groups of exact dyadic endpoint arrays reproduce the frozen values, and the fresh enclosures lie within the saved bounds. This uses the continuous-field generator rather than solver-update diagnostics. Its coverage is six selected nodes; it is not a fresh full-time replay of all 1,539 certificates.

## R04. Reference and actual fast centres

Section 9 explicitly keeps

$$
c^*-c^{\rm fast}=(\bar c-c^{\rm fast})+(c^*-\bar c).
$$

The reference transform and actual Padé output use their respective frozen definitions. The signed reference-minus-fast discrepancy is retained, and the reference-sum interval radius pays its arithmetic uncertainty. No reference trajectory certificate is transferred to Padé nodes.

`shared-fourier-spread.json` contains exact centre differences, node radii, remainder budgets, and signed output-error intervals. `shared-fourier-independent-verification.json` confirms the support bound through a second coefficient assembly and checks rejection of the omitted-shift error.

## R05. Constraints contain the original-chain probabilities

Appendix C supplies the exact affine continuation, its integrability proof, and the original-$Q$ exponential-moment bound. Complex Cauchy–Schwarz then uses the same original-chain variance probabilities across modes. Gaussian square completion is an integration device, not a replacement probability law.

The proof explicitly includes the zero atom, finite bands, infinite tail, and all 22 constraint directions. Upper rows use lower coefficient bounds and upper right-hand sides; lower rows reverse these choices before sign reversal. Nonemptiness follows because the actual probability vector satisfies the constraints. General history-dependent defects require uniform bounds over remaining states or an enlarged partition. See `classical-inclusion-en.md` and the regenerated classical-input record in `verification.json`.

## R06. High-dimensional trial-field claims

The portable material lacks the complete thirteen-dimensional coefficient bank. Its saved integral receipts therefore no longer support a main-text numerical claim of complete annual valuation certification. This missing delivery is documented rather than replaced by an existence argument.

The signed four-contribution identity remains. The fully explicit field H17 supplies an independently inspectable nonexact example with exact terminal value, zero observation jumps, and finite full-year residual and defect envelopes. It establishes the scope of the identity; it does not establish useful prices for the original Asian instruments. See Section 10.3 and `merged-proof-review.md`.

## R07. Strictness at the complete-price scale

The classical terminal example retains its qualitative outer-set separation. Its auxiliary derivative exceeding $3\times10^{-9}$ is not presented as a monetary gap or actual-bias lower bound.

The new rough-model experiment addresses the complete-price requirement directly: the original 4400–4500 spread is compared at the same actual output centre, with all finite nodes and remainders. The absolute bound falls from **2.679931 to 1.397613 index points** for $\alpha=.52$, a conservatively displayed **47.8489%** reduction against the available signed marginal bound. The other candidates improve by 43.9719% and 11.2903%. This is the quantitative full-budget result; it is not a numerical upgrade of the classical terminal gap.

## R08. Complete error accounting

Sections 6, 9, and 12 distinguish continuous-integral-to-infinite-grid discretization, finite omitted nodes assigned zero, the infinite discrete-rule tail, reference transform error, finite-sum arithmetic, and signed centre translation. Omitted finite nodes are counted once as shared transform errors. The infinite discrete tail is controlled by the proved continuous-integral envelope.

The exact node ledgers and `shared-fourier-spread.json` identify each contribution. Invalid inputs, failed certification, unresolved intervals, and successful decisions remain distinct outcomes. Failure of a sufficient numerical budget is not reported as failure of a model property.

## R09. Financial units and an honest budget test

Normalized prices are converted to index points using $DF=4221.86$. `spread-decision-contract.json` fixes a primary one-point diagnostic budget and sensitivity thresholds of 0.25, 0.5, and 2 points before reading the new joint result. This is not described as pre-computation preregistration or a market-suitability criterion.

The $\alpha=.52$ joint bound does **not** certify the primary one-point budget. At the stated two-point threshold, the signed marginal bound is insufficient and the joint bound suffices. `spread-decisions.json` records both the successful and unsuccessful tests. The reduction concerns a guaranteed upper bound, not a measurement of actual error.

## R10. Difficult candidate comparisons

The original experiment remains a conditional three-candidate comparison with the forward curve and other parameters fixed. The best candidate's quote-band exclusions are retained separately from ranking.

`near-tie-diagnostic.json` records a successful separate synthetic test using the exact midpoint of the frozen $.52$ and $.60$ output vectors. Their numerical objectives tie exactly; complete model-price objective intervals overlap, and the checker correctly retains both candidates with status `UNSEPARATED`. The script checks the pinned input identities and retains the original real-quote comparison as a control. It reaggregates the existing complete price certificates rather than regenerating their upstream continuous residuals. This is a synthetic diagnostic, not another market observation. A dense conditional profile and parameter refitting have not been completed or claimed.

## R11. Precise attribution and contribution boundaries

The introduction and contribution table distinguish the established rational construction, Caputo convexity, strip quadrature, moment optimization, and support-function algebra from this revision's model-specific proofs and implementation certificate. `literature-audit.md` compares the approximation objects and guarantee types with relevant primary literature, including Markovian kernel-error results and residual-based fractional analysis.

The candidate contribution is the verified connection from the specified continuous residuals to shared strike errors at the actual output, with complete-budget financial consequences. We do not claim historical priority from unsuccessful searches, treat heuristic convergence diagnostics as inclusion certificates, or infer accuracy superiority by comparing observed errors with worst-case guarantees. Later literature is recorded in the current audit without backdating the earlier manuscript.

## R12. Financial meaning of structural properties

Section 13 separates probability-model validity, approximation structure, complete price certification, shared-output bounds, and finite-candidate decisions. Pole exclusion and half-plane preservation do not independently certify positive definiteness, an arbitrage-free price surface, or Greeks. Each retained conclusion specifies its model, parameter domain, trajectory, numerical centre, and required evidence. Continuous calibration and market-parameter identification remain outside the certified scope.
