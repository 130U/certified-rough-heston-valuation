# Reproduction package

This package supplies the original interval and exact-arithmetic programs, frozen fields, and completed certificate records for the rough Heston manuscript. Python 3.12 and NumPy are sufficient. The release was checked using Python 3.12.14 and NumPy 2.3.5.

From the repository root:

```sh
python -m pip install -r code/requirements.txt
python code/run.py verify
```

The verification output is written to `out/verification.json`. It checks the release hashes; decompresses the structural certificate and verifies its original identity; reconstructs the complete disjoint midpoint tree; checks every recorded strict sign and uniform minimum; checks field identities and guards; and recomputes the thirty-six price objectives, actual Padé comparisons, and financial decisions using `fractions.Fraction`.

The sign-record audit and interval-sign generation are separate operations. To recalculate sixteen evenly spaced leaf records with the original 100-bit generator:

```sh
python code/run.py verify --sample-signs 16
```

Use `--sample-signs 211241` to recalculate every accepted leaf. The latter is a substantial exact-arithmetic computation. Both operations count the number of signs actually recalculated in the output. The default verification audits saved records and cover geometry.

## Files

- `src/`: original self-written algorithms and diagnostic programs. The sole arithmetic-preserving source relocation is in `compute-finance-usecase.py`.
- `frozen/`: the completed structural cover; four field NPZ files; metadata; continuous-time residual and exponent records; true-price bounds; and finite-candidate results.
- `PROVENANCE.json`: original and public hashes, documented path relocation and input selection, and historical evidence identifiers.
- `MANIFEST.json`: identities of all released code and frozen artifacts.
- [QA summary](QA-summary.json): the bounded release checks, including sixteen recalculated interval leaves and exact aggregation replay equality.
- [Exact financial example](frozen/finance-usecase-calculations.json): objectives, quote gaps and the call-spread budget, reaggregated from the public frozen input bytes.
- [Data and attribution](DATA.md), [mathematical and execution scope](SCOPE.md), and [notice](NOTICE.md).

The structural JSON has 211,241 accepted leaves and is shipped as lossless gzip. Each public file is below 100 MiB. The three `u128` fields are about 32 MB each. The additional `u80` field is the exact object used by the alpha=.9 residual and price certificate; it is retained separately.

## Replaying stages

Replays first copy source and frozen inputs to `out/work`. They never overwrite `code/frozen`.

```sh
python code/run.py replay aggregate --out out/aggregate
python code/replay-semantic-check.py --work out/aggregate
python code/run.py replay pipeline --out out/pipeline
python code/run.py replay diagnostic --out out/diagnostic
```

`aggregate` recomputes the price aggregation, finite-candidate objectives and application from saved continuous-time residual/exponent/tail inputs. It does not rerun those input generators. `pipeline` additionally reruns the three continuous-time residual certificates, their adapters, field exponent integration, and true-tail enclosure before aggregation. `diagnostic` reruns the specified floating-point Padé implementation and freezes its outputs; its status remains diagnostic until compared with true-price intervals.

The complete canonical English source paper is copied only into the replay working directory under the five proof-evidence aliases required by the original programs. Section assignments are in [the proof map](../docs/proof-map.md). Proof hashes in a new replay identify that English file; the original execution proof hashes remain recorded in `PROVENANCE.json`. Relocation or translation changes a file hash, not the mathematical field or stored rational endpoint. `replay-semantic-check.py` compares all regenerated price rows, node error records and objective/error vectors with the frozen mathematical values while allowing the documented metadata relocation.

## Cost

Default verification reads about 150 MB of release files and expands a 219 MB structural JSON. Allow approximately 1 GiB of free RAM for parsing and exact tree reconstruction. The frozen fields avoid solver regeneration. Actual verification time is recorded in its output; it depends on the machine.

The expensive replay is optional. The alpha=.52/.6 residual calculation covers 8,189 closed time subintervals at each of 513 fixed frequency nodes; alpha=.9 covers 4,093. Exponent integration contains 1,025/1,025/641 node records. No claim of a fresh full-generator run is made by packaging or a saved-record verification.

Recorded generator times in the original frozen results are approximately 793/779/194 seconds for the three residual certificates and 95/110/27 seconds for their exponent components. These are historical execution times, not a performance guarantee for a different computer. They make the distinction between a short read-back/aggregation run and a full residual replay explicit.

The original programs expose further options through `--help` after staging. `save-fixed-field.py` and `field-residual-diagnostic.py` describe field construction; certificate reproduction uses the shipped exact dyadic fields. Re-generated floating fields are new objects and must receive their own residual certificates.
