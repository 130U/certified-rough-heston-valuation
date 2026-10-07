# Certified Joint Pricing Errors in Heston Models

This revision merges the rough-Heston manuscript B and classical-Heston error-structure manuscript C around verified residuals, actual price inclusion, shared error geometry, and financial decisions. The supplied Asian-valuation manuscript A is cited as preceding work. New proofs and computations are dated 7 October 2026 rather than attributed to the supplied 2024 cover version.

Read the [complete manuscript](manuscript/merged-heston.md), [PDF](paper/Theodore-Ouyang-Merged-Heston-EN.pdf), [editable source](manuscript/merged-heston-source.md), and [reviewer response](reviewer-response-en.md).

The main new numerical result is a same-centre, complete-budget shared-Fourier certificate for the original 4400--4500 spread. For alpha=.52, its guaranteed absolute error bound falls from approximately **2.67993 to 1.39761 index points**, a **47.8489%** reduction against the existing signed marginal bound. Reference-minus-fast translation, continuous residuals, all finite nodes, analytic-strip quadrature, the true infinite discrete-rule tail, and interval arithmetic remain in the budget. This is a worst-case guarantee, not an estimate of the realized error. It certifies a two-point diagnostic threshold while leaving the primary one-point threshold uncertified.

## Delivered verification

| Object | Completed check | Scope |
|---|---|---|
| Structural certificate | All 211,241 leaf records regenerated; 422,481 tree nodes reconstructed | Exact raw polynomials and released 100-bit outward rational arithmetic |
| Initial fractional behaviour | Independent startup assembly at all 1,539 candidate-frequency pairs | Direct Caputo reconstruction within complete frozen residual bounds |
| Full-time residuals | Fresh replay at u=0,1/8 for each of three candidates | Six full-time nodes; all saved frequency records separately validated |
| Original-chain constraints | 22 rows and 918 profile values regenerated | Original Q probabilities, zero atom, finite bands, and infinite tail |
| Terminal witness | 407 exact checks | Primal/dual directions, uniqueness, signed derivative, and strictness |
| Shared spread | 1,025 finite nodes for each candidate | Actual fast centre and every remainder; second coefficient assembly checker |
| Synthetic tie | Exact fast-objective equality and overlapping full model intervals | UNSEPARATED; original market-target control still selects alpha=.52 |
| Adversarial inputs | Deliberate corruption rejected | Coverage, signs, constraints, dual direction, nodes, budgets, and centre shift |

The aggregate record is [verification.json](verification.json). Exact records include [full structural regeneration](full-structure-verification.json), [startup assembly](startup-independent.json), [six-node full-time replay](residual-fresh-subset.json), [shared spread](shared-fourier-spread.json), [independent spread check](shared-fourier-independent-verification.json), and [synthetic tie](near-tie-diagnostic.json). The [evidence audit](evidence-audit.md) distinguishes generator replay, mathematical certificate checking, stored-record checking, and independent downstream assembly.

The continuous structural theorem retains its stated domain. A broader T1 chain does not support the merged core; the alpha=.90 point-price certificate does not enlarge that theorem. The portable historical thirteen-dimensional field receipts omit the full coefficient bank, so the manuscript retains a fully explicit analytic trial field and the four-term identity without claiming a complete annual high-dimensional price certificate. Dense parameter profiling, other-parameter refitting, and Greeks certification are not completed results.

## Reproduce

The immutable upstream input is repository commit `6a5134197db60c765ca3aea4f6cdeb2bafbb6617`; baseline artifacts remain unchanged in this revision. Recorded execution used Python 3.12.14 and NumPy 2.3.5. Install the baseline `code/requirements.txt` in an appropriate environment. Run from the repository root:

```text
python code/run.py verify --sample-signs 16
python code/classical/verify_input_bounds.py
python code/classical/verify_terminal.py
python revision-20261007/full_structure_verify.py
python revision-20261007/startup_independent.py
python revision-20261007/shared_fourier_spread.py
python revision-20261007/verify_shared_fourier.py
python revision-20261007/spread_decisions.py
python revision-20261007/near-tie-diagnostic.py
python revision-20261007/adversarial_checks.py
```

The revision scripts rewrite their generated records with fresh runtime metadata. `residual_spotcheck.py` is the longer six-node continuous-field replay and does not run a numerical solver. It is distinct from replaying every frequency. The structural full-leaf run took approximately 194 seconds on the recorded machine; full-time residual costs are reported separately. Mathematical source identity and exact endpoint comparisons, rather than equal runtime strings, define reproducibility.

GitHub mathematics are generated from the canonical source using the baseline presentation converter. Every formula is checked with the restricted base/AMS/newcommand MathJax configuration, and numerical table transcription and equation tags are preserved. PDF math is embedded as vector glyph paths; the PDF is an editable-Markdown artifact, not a claim of successful standalone LaTeX compilation.
