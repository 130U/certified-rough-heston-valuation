# Fixed V3 secondary audit

This directory delivers 11 pricing-configuration IDs, the exact matched quarter ledger, all 504 actual complete portfolio thresholds, all 40 nearby pair/method decisions, the closest-pair gap decomposition, a source-checked proof/reader matrix, and frozen-output centre accounting. `config-main-*`, `audit-main-*` and `appendix-e-*` are bilingual manuscript fragments. Figures are supplied as PNG, vector SVG and PDF.

From a release packet containing `baseline/`, `new-research/experiments/` and `v3/audit-experiments/`:

```sh
python v3/audit-experiments/reproduce_audit.py --baseline .
```

`--baseline` also accepts the original fixed V2 evidence root. Without the flag, the driver searches its parent directories for that exact layout. Paths in machine records are canonical packet-relative evidence paths.

The separate reader does not import the audit producer. It verifies the fixed source hashes and derives exact ledgers, threshold counts, pair decisions, gap terms, returned-output centre payments and flag semantics. Nine corruption controls reject omitted paid terms, false pair decisions, lost threshold equality, wrong subcell metadata, unpaid centre movement, erased BL reference floor and an exaggerated `--full` scope. CSVs are checked against exact JSON records.

This is a secondary saved-evidence audit. The previously certified continuous-derivative inequalities and disclosed strict scalar libraries remain inherited. It does not claim a fresh full residual-generator run or an outside referee execution. The original V2 CI source snapshot is identified separately under `historical-ci/`; it checked identities and retained receipt binding, not a large-bank interval replay.

`source-identities-before-portable.json` retains the original source SHA records. `snapshot-identity-bridge.json` explicitly maps them to canonical identities, discloses every changed SHA, and verifies that all five retained exact scientific derivations stay equal. Generator/source-equivalence checks belong to the separate privacy audit.

To rebuild the secondary derivations from a selected fixed snapshot, run `produce_audit.py --baseline <snapshot>`, `proof_matrix.py --baseline <snapshot>`, `bridge_snapshot.py --baseline <snapshot>`, `read_audit_independent.py --baseline <snapshot>`, `write_sections.py`, `plot_budget_counts.py`, `check_figure.py`, and finally `freeze_manifest.py`. These commands write only this audit directory. The reference and continuous bank inputs stay immutable.

Complete-bound displays round upward to nine decimal places. Every scientific decision uses exact rational endpoints. Plot coordinates and decomposed component displays are approximate; complete endpoint tables preserve exact fractions. Only mathematical work counts, evidence bytes, software/source identities and scientific physical-time variables are recorded.
