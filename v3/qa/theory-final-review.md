# Final theory and manuscript consistency audit

Status: ACCEPTED_WITH_EXPLICIT_SCIENTIFIC_BOUNDARIES.

## Reviewed artifacts

The complete generated English manuscript and the complete generated Chinese manuscript, including Appendices A–G and references, were read. All paths below are relative to the research directory.

| Artifact | SHA256 at full review |
|---|---|
| manuscript/merged-heston-en.md | 42d23438fe54cf33691475ea0fbec591592c061ce083dc114e066d8bb2193031 |
| manuscript/merged-heston-zh.md | 292d1da365c5abd56b5fa7ed0e0d9320ab56053e657a599a152149182665ebea |

This was a read-only review of mathematics, claims, references and their ledger interpretation. Previously accepted scientific computations were not repeated. Exact fractions in the retained centre account were used to check displayed rounding; this does not constitute a fresh regeneration of the underlying continuous residual banks.

## Findings and corrective readback

The preceding review identified manuscript-local problems. The reviewed revision closes them as follows:

1. The main theorem now defines the fractional kernels before use. It preserves AC trajectories, the common zero initial value, physical residual and nonnegative damping. The proof remains authoritative in Appendix C.2, using the full AC bridge in C.1. At zero damping the kernel is the fractional integration kernel, so no division by the damping parameter occurs. The constant-curve formula that divides by that parameter explicitly assumes strict positivity.
2. The introduction assigns finite omitted frequencies to the Fourier perturbation vector. Strip quadrature, the true infinite tail and arithmetic remain separate remainder charges. Section 5 preserves this identity and does not pay finite nodes twice. The broken reference to subsection 4.2 has been replaced by Section 4. The stale statement denying a resolvent implementation is now limited to a separate constant-curve financial experiment, and the old state-barrier paragraph points to the correct appendix.
3. Proposition C.5 now explicitly states positive canonical damping, the nonnegative residual threshold, the exact half-plane, the physical residual scale, AC and positive-time local Lipschitz regularity, and the common zero initial value. Its first-crossing argument is compatible with these conditions: positive-time local Lipschitz paths have a continuous Caputo derivative on compact positive-time intervals, so the almost-everywhere residual inequality extends there by continuity.
4. The H3 and N2 radius displays in the centre-account table are upward decimal endpoints, respectively 0.050546863 and 0.261808769. The nearest-candidate gap is labelled approximate; exact rational endpoints govern its positivity. The fixed-formula floor is displayed with a downward endpoint and is not described as a true-error lower bound. The BL reference floors and ratios are explicitly approximate displays. The English centre table distinguishes approximate signed centres from upward radii and complete bounds.
5. The verification matrix distinguishes obligation identifiers from configuration identifiers, explicitly mapping obligation N2 to configuration N2L. The Chinese kernel experiment is now subsection 7.6 and consistently names the N2L bank. The matrix and discussion preserve the distinction between saved receipts, identity checks, actual independent aggregation and inherited continuous derivative validity.

The final Chinese centre-table copyedit is closed in the readback recorded below. Its sentence now repeats the English convention that centres are approximate, radius and complete-bound columns are upward endpoints, and independently rounded columns need not add exactly. The values were already correct.

## Accepted mathematical and scientific boundaries

- The Caputo argument uses convexity with an AC approximation and almost-everywhere convergence, followed by a continuous endpoint conclusion. It does not apply an ordinary chain rule to the Caputo derivative. The curve initial term and the physical inverse-volatility factor are retained through the pricing functional.
- The dissipative kernel proof retains absolute convergence, the explicit Gamma lower-bound range and both series remainders. The reader's direct double-series expansion is distinct from the producer's power-field moment expansion. Shared interval primitives and inherited upstream derivative proofs remain stated dependencies.
- The four-way kernel comparison keeps the actual output, reference, centres, coefficients, omitted-node treatment and other remainders fixed. The small positive resolvent improvement does not claim a new quarter-point decision. The saved baseline curve endpoints and their upward displays are distinguished correctly.
- Shared Fourier perturbations belong to one candidate and one maturity. The finite-objective comparison explicitly avoids treating different roughness candidates as having the same error vector. Convex quadratic lower tangents and full quadratic upper remainder terms are preserved. Quote-conversion arithmetic is not the market bid/ask half-width.
- The quarter-point change between matched marginal and joint certificates is supported by the declared common-radius account. Different-bank improvements are descriptive comparisons. Actual returned binary64 reference and corrected outputs retain their centre translations and return-rounding charges.
- The narrow continuous correlation strip remains a local structural result rather than a practical broad calibration domain. Its continuous cover is not replaced by a discrete scan. Analytical decreasing curves are not promoted to new probabilistic model admissibility claims.
- Classical appendices retain the original correlated positive-part chain, its common probability vector, atom and unbounded tail. The row-max incompatibility gap is a lower bound on the support difference rather than equality with it. The four-term residual identity has the stated left-minus-right observation sign, sufficient integrability and stopped uniform integrability. Neither the terminal witness nor the archived necessary residual diagnosis is promoted to a complete annual currency certificate.
- Mathematical work counts retain their distinct units and are not converted to speedups or total-cost ratios. The manuscript does not claim external referee execution of author-side validation, observed solver error, market fit, or a finite certificate-to-true-error ratio when the rigorous error interval crosses zero.

## Numbering and attribution

Both manuscripts have 169 unique equation tags with matching identifiers and mathematical content. Searches found no unresolved manuscript placeholders, the obsolete subsection 4.2 reference, or a retained editing directive. Numerical parentheses such as 1.776 and 1.86 are constants rather than missing equation references.

External locators remain unchanged, including El Euch–Rosenbaum Proposition 3.1 and Corollary 3.3; Li–Liu Proposition 3.11(ii) and Proposition 4.12; Kopteva Theorem 2.2 and Lemma 2.8; and Trefethen–Weideman Theorem 5.1. The Simon complete-monotonicity reference remains distinct from the separate Mittag–Leffler inequality reference.

## Final readback

The Chinese centre-table explanation and subsequent editorial changes were read back. Both final sources retain 169 unique equation tags, and no unresolved placeholder or obsolete subsection 4.2 reference was found. The final source identities below include the targeted grid-generation and reference-object clarification described at the end of this audit.

| Frozen final artifact | SHA256 |
|---|---|
| manuscript/merged-heston-en.md | ab206384751f90f04b62b2b5d1a8b8aa007421f58eb04484071185c7b1a23b5a |
| manuscript/merged-heston-zh.md | 9f95fefe0bed312fb3ba65f964756568446e970fb44b1b137c778a5382662b5f |

No result-changing mathematical or claim-consistency issue remains within this manuscript audit. Acceptance is of the stated, conditional scientific claims and their described verification boundaries; it is not an external replication, a new continuous-bank regeneration, or a guarantee of any reviewer score.

An additional targeted readback checked the Chinese E.2 verification-matrix translation against the preceding English rows. Commands, scientific counts, obligation/configuration distinction and all inherited/shared-dependency boundaries remain intact. That intermediate translation revision had Chinese SHA 696d27ed827ab1717e4846903443de080e2af4ce4b84974d0cf590b29a1b1d25; the preceding centre-table revision had SHA 5347608a771b6eb0bc3f355f3dabf5539f7c92b33ed0cec1749af0936abb4372.

The last targeted bilingual check read Section 2's auxiliary-grid construction and Section 4's reference-object clarification. The uniform auxiliary rule, physical-time scaling and exact-arithmetic graded formula are algebraically consistent. The retained `nearby_generate.py` and its `sdk/field-residual-diagnostic.py` implement those rules, force the actual endpoints and save the resulting nodes as exact dyadics. The quarter reader `baseline/heston-frontier-20261007/independent-transfer.py` retains all preceding nodes, appends the exact quarter endpoint, and uses the exact rational bracketing fraction to interpolate the original LG remainder before outward interval integration. Its startup power coefficients and complete earlier history remain present. A continuous integral reference is correctly distinguished from nominal nodal solver states while its defining saved nodes and coefficients retain their exact dyadic meanings. This was source inspection, not a repeated scientific run. The two added descriptions introduce no new numbered equations, and both final tag sequences still match.
