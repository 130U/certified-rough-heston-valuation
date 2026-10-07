# Certified Joint Pricing Errors in Rough Heston — V3

[Fixed release and four delivery assets](https://github.com/130U/certified-rough-heston-valuation/releases/tag/v3.0.0-research-20261007).

The English and Chinese PDFs have a compact main argument, integrated technical Appendices A–E, and independent classical extensions F–G. The editable current sources are `v3/manuscript/merged-heston-en.md` and `v3/manuscript/merged-heston-zh.md`. `v3/REVISION-RESPONSE-zh.md` gives the complete migration and review response.

Download the named `Theodore-Ouyang-Heston-V3-Evidence-20261007.zip`, verify the checksum file, and extract it. GitHub's automatically generated source archive omits the large NumPy residual banks and cannot replace the named evidence archive.

```text
python -m pip install -r requirements.txt
python reproduce.py --full
```

Scientific computation requires Python 3.12 and NumPy 2.3.5. The verification driver checks the scientific manifest and executes in a fresh copy, without reporting host configuration, user paths, clocks or resource telemetry. The actual-output bitwise replay is checked on the executing floating-point implementation; no universal cross-platform bitwise equality is assumed.

`--full` adds the original full structural-sign cover. The default inherited frontier driver already requests the two full transfer/output readers. Neither mode regenerates every saved continuous residual derivative bound. The explicit obligation matrix in `v3/audit-experiments/appendix-e-en.md` gives the separate regeneration commands, reading scope and shared dependencies. Saved evidence, independent reconstruction, full generator execution and CI source identity are different claims.

The new matched kernel study computes strict resolvent weights and compares four propagation methods at the same output, centre, residual bank and remainder. Its separate reader uses a different cumulative-series expansion, reads every bank entry and reconstructs all twelve prices. Dyadic, Gamma, logarithm and exponential primitives, and the upstream residual proof, remain shared. The experiment retains the failed quarter-point frozen-output budget; the small additional kernel gain is reported with its scope.

The experiment audit includes the quarter-year decision ledger, all unresolved nearby pairs, the closest-pair loss decomposition, fixed-output reference transitions and exact budget–pass-count curves for all 28 declared directions. The plot has PDF/SVG/PNG exports in `v3/audit-experiments`.

The `baseline` and `new-research` directories are inherited, fixed scientific inputs. Current paper claims and verification descriptions are authoritative in `v3`. Privacy-only transforms remove unnecessary execution metadata from the inherited copy and rebind transformed dependency identities; the original V2 stays privately preserved. `BASELINE-TRANSFORM.json` records mathematical JSON-projection and NPZ-byte invariance. This is not a claim that all historical raw generators were rerun after a metadata transform.

`FRESH-ACCEPTANCE.json` records this revision's actual author-side fresh execution. It is not an external referee run. `SCIENTIFIC-MANIFEST.json` seals inputs; `DELIVERY-MANIFEST.json` also binds PDFs and acceptance records. `SOURCE-MANIFEST.json` in the Git checkout identifies source files and the large arrays supplied only by the named release asset. CI verifies source identities and the retained acceptance binding, rather than independently rerunning the large scientific bank.

Appendices F–G preserve original-chain moment/integrability proofs and the signed error identity for inexact trial fields. The terminal strictness witness and incomplete thirteen-dimensional diagnostic do not imply a complete annual monetary pricing certificate. A numerical reference point is never treated as exact truth, and finite-candidate rankings do not imply continuous calibration or market identification.
