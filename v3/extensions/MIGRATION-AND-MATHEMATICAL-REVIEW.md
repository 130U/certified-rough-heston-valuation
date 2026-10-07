# Appendix F/G migration and mathematical review

Revision date: 2026-10-07. This record concerns only the classical appendix migration. The earlier source trees were read without modification. `SOURCE-IDENTITIES.json` fixes each source by relative path, exact SHA256, byte count, and relevant line ranges. The four insertable drafts use temporary unique formula labels F01–F30 and G01–G17; the parent manuscript assigns final appendix numbering.

## Migration map

| Source unit | English source lines | Chinese source lines | New destination | Retained content |
|---|---:|---:|---|---|
| C.1 | 8–77 | 8–77 | F.1–F.2, F01–F08 | Two original laws, parameter domain, loading domain, affine Riccati existence, nonexplosion, stopped moment identification, exact finite telescope |
| C.2 | 78–122 | 78–124 | F.3, F09–F12 | Positive-part negative-tail control, conditional exponential moment, doubled-load Cauchy–Schwarz under original Q |
| C.3 | 123–185 | 125–186 | F.4, F13–F16 | Zero atom, unbounded tail, mean/exponential bounds, both Laplace recursions, all 22 valid rational constraints |
| C.4 | 186–240 | 187–243 | F.5, F17–F20 | Terminal Riccati guards, cubic residual, variation-of-constants bounds, zero/finite/tail profile supremum |
| D.1 and D.2.1 | 246–330 | 249–333 | F.1, F.3, F.7 | Original instruments and original-law shared occupation vector; no mode-tilted probability substitution |
| D.2.2 | 331–367 | 334–370 | F.6, F21–F23 | Complete price premise, joint residual lift, geometric properties, exact support, cross-time maximum |
| D.2.3 | 368–405 | 371–408 | F.6, F24 | Necessary and sufficient common-maximizer/phase criterion, all degeneracies and outer-set boundary |
| D.2.4 | 406–465 | 409–468 | F.7, F25–F28 | Complete terminal rows, primal–dual uniqueness, feasible put-improving direction, qualitative strict gap |
| D.3.1–D.3.2 | 468–539 | 471–542 | G.1, G01–G05 | Independent sufficient admissibility, true traces, global growth, weights, integrability, original-Q defect interface |
| D.3.3 | 540–577 | 543–580 | G.2, G06–G08 | Four signed terms, compact stopping, L1 limits, observation signs, same-field identity |
| D.3.4 | 578–600 | 581–603 | G.3, G09 | Effective sufficient nonnegative bounds and joint signed alternative |
| D.3.5 | 601–654 | 604–657 | G.4, G10–G13 | Explicit analytic nonexact field, generator residual, continuous integral, exact original-Q Gaussian defect and finite full-horizon bound |
| D.4 | 655–703 | 658–707 | F.8, F29–F30 | Portfolio propagation and joint acceptance/target image, compressed as a standard corollary |
| Supplement §§4–6 | 280–532 | — | F.7 and G.5, G14–G17 | Positive Asian coefficient, full-row witness, trial-basis/carry/Hermite diagnostic, archived evidence boundary |

Here the C/D line references point to `extensions/classical-extension-en.md` and `extensions/classical-extension-zh.md` in the fixed read-only source tree. The supplement is `evidence-v2/baseline/english-heston-release/docs/classical-evidence.md`. New public machine paths begin `baseline/english-heston-release/code/classical/`; they must be rebound to the final sanitized release manifest, rather than to old commit URLs.

## Proof review and explicit repairs

| Unit | Classification and status | Hypotheses actually used | Review finding |
|---|---|---|---|
| F.2 continuation | Direct Riccati barriers plus stochastic localization; Verified within stated domain | Nonpositive loads, total real load at most 1/2, finite dates, F02 | Preserved first-crossing and radial estimates. Added the full correlated one-dimensional Gaussian integral, including both sides of the positive-part boundary. No probability-law change is inferred from square completion. |
| F.3 common inclusion | Direct conditional moment and Cauchy–Schwarz; Verified | Original Q, doubled load at most one, global weighted residual envelope | Every mode shares the true original probability vector. Atom and tail cannot be dropped. General-state trial defects require a uniform envelope or enlarged partition. |
| F.4–F.5 terminal inputs | Direct analytic bounds plus exact regeneration; Verified | Fixed theta-star for point bounds, stated conservative domain for reference bounds, outward endpoints | Regenerated all 22 rows, twelve Laplace recursions, and 918 profiles. Zero and tail cases are explicit. |
| F.6 lifted inclusion | Direct convex argument; Verified conditional on F21 | Full coefficients and all remainders, compact convex valid F | Filled in convexity of the lifted quadratic/affine constraints. A union of independently chosen boxes would not prove this claim. Cross-time information retains max-of-sum. |
| F.6 strictness | Direct support subtraction and equality conditions; Verified | Same outer set and its smallest coordinate box | Retained positive-radius phase equality, zero-radius exception, inactive rows, zero direction, attainment. No true-bias lower bound. |
| F.7 terminal witness | Construction plus exact primal–dual/derivative reader; Verified terminal claim | Same prescribed profiles, rows, catalog and probability polytope | Defined the row-maximizer gap separately from the actual directional support gap. The latter is at least the former by coefficient triangle inequality; it need not equal it. |
| F.8 propagation | Direct linear image; Verified conditional on valid inputs | e=p_h−p_c and n=p_h−center in the same stated sets | Standard corollary, not a separate originality claim. Correct signs of the common (n,e) support directions retained. |
| G.1 moments | Direct Lyapunov and original-Q estimate; Verified | Fixed theta-star, one-year horizon, one compatible weight, positive stock state | Replaced an unexplained moment assertion by branch bounds e^(9/50) and e^(11/60), each below 5/4, and a stopped square-weight argument. |
| G.2 signed identity | Direct finite tower and stopped piecewise Itô; Verified | Same deterministic field, genuine compact-uniform traces, L1 residual, UI field values, integrable original-Q defects | Corrected a supplement sign inconsistency: supplement lines 376–380 define J as right-minus-left but write a plus J term. The new draft defines d=left-minus-right and uses plus d. A right-minus-left convention instead requires minus J. The extension's original d convention was already correct. |
| G.4 nonexact field | Explicit construction; Verified | epsilon>0, r=1/100, h=1/768, R=s_T^(−1/2), T=1 | Explicitly integrates the continuous dominating constant and supplies the full original-Q signed enclosure and sufficient bound. Nonexactness is demonstrated at a positive interior variance, without the absent large bank. |
| G.5 archived diagnostic | Conditional saved-data assertion; saved arithmetic Verified, bank regeneration Not checked | Same archived 13-function field and saved interval identities | The selected residual contract remains failed. The reader sums 3080 saved interval boxes; it does not re-create the bank or replay the archived direct integration. No complete monetary PASS, all-trial-space optimum, or actual-bias lower bound is inferred. |

The source support formula and exact terminal bounds were not weakened. The large displayed fractions have been replaced by exact finite definitions: the active 3-by-3 matrix inverse, signed coefficient interval comparisons, the `put_direction.derivative` endpoints, and the `whole_lower` field. Approximate decimal coordinates are explicitly illustrations of an exact witness. Old appendix pointers and old commit URLs are removed from insertable prose.

The trial-function diagnostic is compressed in G.5 because the coefficient bank is absent. Its conditional generator, terminal forcing, exact carry, Hermite integral, positive necessary residual lower bound, and failure status remain. The full historical projection construction and auxiliary tail calculations remain available in the hashed mathematical supplement; they are not represented as newly reexecuted complete certificates. This is a scope reduction of the presentation, not an upgrade of the evidence.

## Actual portable verification performed

All commands used the default read-only mode and the standard library; no `--write` was passed.

| Reader | Executed result | Mathematical scope |
|---|---|---|
| verify_input_bounds.py | PASS_EXACT_MODEL_BOUND_REGENERATION | 22 rows, 102 bands, nine profiles/918 entries, twelve 767-step Laplace recursions; every saved field reproduced |
| verify_terminal.py | PASS_PORTABLE_TERMINAL767_EXACT_ROW_CERTIFICATE | 407 exact feasibility, duality, uniqueness, basis and signed full-row derivative checks |
| verify_field_receipt.py | PASS_EXACT_FIELD_RECEIPT_AND_MODE_BOX_AGGREGATION | 3080 mode-cell boxes, original 64 time pieces, interval aggregation and displayed strict lower bound |

These portable passes have different scopes. In particular, the field receipt pass does not replace a new execution of the missing coefficient bank or establish the sufficient complete-price upper bounds. No elapsed-time or personal environment measurements were collected for the new review record.

## Insertion and publication constraints

The four draft files contain no private system configuration, contact information, private absolute paths, or execution measurements. General model physical times, scientific revision dates, exact numerical precision and node counts are mathematical data and remain. The current read-only source receipt has separate publication metadata requiring cleanup; `MIGRATION-PRIVACY-OBSERVATION.json` records only relative paths, field categories and hashes, with no original private values. No raw receipt or private provenance is copied into this appendix directory. The parent must preserve scientific mathematical fields and legitimately rebind changed public receipt hashes in the final release.

`check_appendices.py` verifies bilingual display-formula equality, the unique temporary-label sequences, paired section structures, absence of old appendix references in the insertion files, and the restricted new-prose privacy patterns. Its output is a presentation and disclosure check, not a mathematical proof. The mathematical classifications above come from the analytic review and the three actual portable reader executions.
