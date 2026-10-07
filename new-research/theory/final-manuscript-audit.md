# Final manuscript audit

Status: **PASS within the source-review scope; no unresolved editorial or scientific blocker identified.**

## Reviewed sources

| Relative source | SHA256 | Unique display identifiers | Unresolved editorial placeholders |
|---|---|---:|---:|
| manuscript/merged-heston-en.md | 311a57e94eb3671f3bf87ede774dbe05949316e83ca717d7da3b9e66d7d162bc | 107 | 0 |
| manuscript/merged-heston-zh.md | 9ae6215a572fda8df31c52a1422b7f15941a763ad680cac46a7ec1c238c432f2 | 107 | 0 |

The hashes identify the reviewed source contents. A later scientific edit requires a renewed read-back.

## Completed checks

- Both language versions contain the completed nearby-candidate section. The five candidates, all-candidate refinement rule, two-layer interval tables and finite-set conclusions agree. No assembly marker, editorial placeholder, TODO or TBD remains.
- External theorem locators remain source-paper locators: El Euch–Rosenbaum Proposition 3.1 and Corollary 3.3; Li–Liu Proposition 3.11(ii) and the restricted role of Proposition 4.12; Kopteva Lemma 2.8 and Theorem 2.2. Abi Jaber–El Euch's source Theorems 2.1 and 2.3 and Example 2.2 remain distinct from manuscript numbering.
- Each language has 107 distinct display identifiers. The exponent appendix uses C identifiers and does not continue Appendix B. Theorem 3.2 precedes Theorem 3.3. The omitted-node centre-translation result is Proposition 5.2 in Section 5.1.
- The finite-history argument retains the AC bridge, continuous maturity endpoint, curve initial term, physical residual scale and complete Caputo history. The curve condition is analytical; the decreasing curve is explicitly not asserted to be a realised variance curve or a new model-admissibility theorem. The probability-model and affine-transform hypotheses are checked separately.
- The reference description now uses a valid state radius \(E_{\rm state}\). The small-residual radius \(E_\delta\) is conditional on \(\delta_F<s_0^2/2\); the certified approximate half-plane supplies the alternative \(\delta_F/\sigma\). The new experiments principally use the finite-history exponent envelope.
- The nearby loss is explicitly \(J=(1/24)\sum_i(c_i-m_i)^2\) for normalized calls. Index-point squared units require multiplication by \(F^2\). The target interval halfwidth encloses midpoint-conversion arithmetic; it is not a market bid/ask halfwidth. Both languages exclude a uniform winner over arbitrary targets in the market bands.
- The Taylor enclosure charges the quadratic remainder on the upper side and does not use its upper bound to tighten the lower side. Candidate comparisons do not assume common errors across different \(\alpha\). The final strict minimum is a five-point statement, while bid/ask incompatibility and absence of continuous calibration optimality remain explicit.
- The actual binary64 reference, stored correction and final addition are distinguished from the ideal rational correction. The output controls retain the complete reference budget and describe the 128-bin control as a separate descriptive experiment.
- Correlation persistence is restricted to the certified narrow strip. Its exploratory direct supplement, earlier unresolved stage, fallback and shared arithmetic dependencies remain disclosed. No altered-correlation price experiment or broad calibration domain is claimed.
- Typed construction, certification, verification and portfolio-reuse counts are not presented as equivalent operations, total cost or a speed ratio.

## Evidence boundary

This final pass reviewed the assembled sources and the existing complete N2048 reader receipt. It did not rerun previously passed numerical computations. Earlier read-only checks separately recomputed all N1024 loss intervals, candidate decisions, actual return rounding, rational joint-support bounds and the local128 output controls. The existing N2048 receipt records five reconstructed point certificates and all ten pair comparisons. Shared rigorous primitives and the absence of a separately rederived proof of every later residual derivative remain stated limitations.

This audit does not assign a research-quality score, establish priority over all prior work, or verify the final rendered PDF or public release. Those are distinct delivery checks.
