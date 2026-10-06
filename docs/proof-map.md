# Mathematical claims and reproduction artifacts

The complete proofs are in [the rough Heston paper](../manuscript/rough-heston.md), with the canonical TeX-math transcription in [its source Markdown](../manuscript/rough-heston-source.md). The [research report](../manuscript/report.md) organizes the structural mechanism and financial applications. Code verifies or generates the specified finite arithmetic certificates; it complements the analytical proofs.

| Paper location | Mathematical obligation | Released implementation and records |
|---|---|---|
| Section 2 | Physical/normalized variable conventions; six matching conditions; raw Cramer expressions | `code/src/solver-diagnostic.py` contains the unchanged [3/3] formula as a numerical comparison. The paper gives its algebraic derivation and source attribution |
| Section 3; Appendix B | Raw sign inequalities before division; compactification; exact continuous-domain cover | `compact-halfplane-certificate-v2-partial.py` and `interval-pade-certificate.py`; `compact-rough-layer-certificate.json.gz`; default verification reconstructs all 211,241 accepted leaves, exact area 2/25 and 422,481 tree nodes |
| Section 3; Appendix B | Positive raw determinant norm and quantitative denominator margins | Saved rational `B_lower`, `negative_D_lower` and `delta_norm2_lower` in the compact cover; exact uniform minima checked by `code/run.py verify`. Optional `--sample-signs` recalculates individual interval records |
| Section 4 | Complex Caputo convexity and half-plane dissipative comparison; sigma=0 time branch | Analytical proof in the paper. Continuous-field records provide the required approximation half-plane conditions at the fixed frequency nodes |
| Section 5 | Positive D-type exponent kernel; state-to-exponent error transfer and scaling | Analytical Fubini/kernel proof; `exact-forward-moments.py`, `exponent-field-certificate.py`; the three field-exponent certificates and their saved forward weights |
| Section 6 | True model transform, probability strip, quadrature error bound and true infinite tail | Paper Section 6 and Appendix A; `direct-tail-certificate.py`, `direct-tail-certificate.json`; `f8-node-price-aggregate.py` includes node, quadrature and true infinite-tail error bounds |
| Section 7 | Fixed exact dyadic field; startup cancellation; continuous-time residual on each closed interval; dot-product error contract | `certify-field-residual-v3.py`, `combined-field-derivative.py`; raw residual records for alpha=.52/.6/.9; four NPZ objects and metadata; `calibration-field-input-check.py` |
| Section 7 | Lossless conversion from executed residual records to pricing inputs | `residual-certificate-adapter.py`; the three `residual-node-certificate-...json` files. Exact adapter bounds, frequency order, field identity and half-plane conditions are checked by default verification |
| Section 8 | Twelve true-price intervals for each of three candidates | Three `f8-price-...json` files, containing all 36 rows, each component error budget and the exact aggregation vectors |
| Section 8 | Exact least-squares and quote-band objective bounds; strict finite winner; actual Padé reference comparison | `finite-candidate-objective-aggregate.py`, `calibration-interval-aggregate.py`; normalized twelve-row quote inputs; `finite-candidate-calibration-result.json`; `frozen-pade-numeric-output.json`. Default verification recomputes all objective bounds and output-error bounds with Fraction |
| Section 10 | Quote-row separation; call-spread error budget and candidate selection | `compute-finance-usecase.py`; exact application assertions also reproduced by `code/run.py verify`: H=.02, positive objective gap, strikes 4400/4500, spread error below .000634774793739 |
| Appendix A | Legitimate Volterra model, positive forward curve, affine transform and martingale assumptions | Complete mathematical application and citations in the paper; model/curve inputs are explicit in `calibration-contract-finite-T05.json` |

All filenames in the table refer to `code/src` for Python and `code/frozen` for JSON/NPZ unless otherwise stated. [The manifest](../code/MANIFEST.json) identifies current public bytes; [provenance](../code/PROVENANCE.json) additionally identifies original executions and documents metadata relocation.

## Verification and replay boundaries

`verify` checks every stored inequality and complete cover geometry. Its output reports `interval_signs_recomputed=0` by default. Adding `--sample-signs N` recomputes precisely the reported number of accepted leaves using the shipped interval generator. The wider historical source JSON is not needed for the closed [.52,.6] leaf cover; its original digest is retained as a provenance identifier.

`replay aggregate` recalculates price/objective/application results conditional on the shipped continuous residual and exponent records. `replay pipeline` separately recalculates those residuals, field exponents and the tail certificate. Both use a new `out/` working copy, preserving the frozen release. Replays change metadata hashes when they use public relocated inputs or translated proof evidence; the mathematical endpoints can be compared exactly.

The continuous-alpha structural theorem concerns [.52,.6]. Alpha=.9 participates in the three-point reference-price comparison through its own `u80` field. The `u128` alpha=.9 field is retained as an additional own-computed object, with a different identity; the replay uses `u80` to reproduce the actual published case.

## Replay proof aliases

The original programs expect five proof filenames. At staging, the wrapper copies the **entire complete English paper**, rather than a proof stub, under those filenames in `out/work`:

| Replay filename | Relevant complete-paper proof |
|---|---|
| `model-admissibility.md` | Appendix A and model setup |
| `fractional-exponent-linearization.md` | Section 5 and exponent-tail derivation in Section 6 |
| `direct-real-tail.md` | True real-part tail comparison in Section 6 |
| `complex-dissipativity.md` | Section 4 |
| `field-residual-proof.md` | Section 7 and the arithmetic appendix |

This is an explicit evidence relocation. Original historical proof hashes are preserved in provenance; a new replay records the actual English evidence hash. Current byte identity is not retroactively assigned to earlier execution.
