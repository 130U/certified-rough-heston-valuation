# Verification commands

These commands verify the scientific inputs and reconstruct the reported certificates. All 27 numerical banks are included in the public checkout. Start from the project root; the individual obligations below run inside a staged working directory. The [evidence map](EVIDENCE.md) connects each operation to the paper, and [RENDERING.md](RENDERING.md) gives the article and PDF build commands.

## Source identities

```text
python -B verify_source.py --strict
```

This checks the published file identities, including the numerical banks, and rejects files outside the publication manifest. Explicitly excluded local build and working directories are ignored. It does not execute the scientific calculations.

## Saved-bank reconstruction and structural checks

```text
python -m pip install -r requirements.txt
python reproduce.py --manifest-only
python reproduce.py
```

`--manifest-only` checks scientific input identities and their binding to the current manuscript. The default reconstruction driver creates an isolated working copy and runs six stages: frontier accounts, correlation checks, correlation controls, candidate and output experiments, the dissipative-kernel reader, and the exact audit reader. It writes the execution scope and stage results to [SCIENTIFIC-REPLAY.json](SCIENTIFIC-REPLAY.json).

To additionally recompute the complete original structural-sign cover, replace the default run with:

```text
python reproduce.py --full
```

These runs reconstruct prices, objectives, outputs and decisions from saved banks; fresh continuous-residual generation is listed separately below.

## Individual obligations

Prepare an isolated saved-evidence tree before running the individual commands below:

```text
python reproduce.py --stage-only
```

Change into the directory printed by this command. The paths below are relative to that directory, which contains the identified scientific inputs and current manuscript. Generators and some readers write local receipts, so use a fresh staged tree for a separate experiment. The integrated driver above is the preferred combined check. Individual readers retain the continuous-generator and arithmetic-library dependencies described in Appendix E and the [verification guide](validation/README.md).

<a id="s1"></a>
### S1 — Complete Padé structural-sign cover

```text
python -B science/baseline/continuous/full_structure_verify.py
```

<a id="s2"></a>
### S2 — Startup Caputo residual and half-plane enclosure

```text
python -B science/baseline/continuous/startup_independent.py
```

<a id="r1"></a>
### R1 — Low-frequency continuous cover

```text
python -B science/baseline/finite-history/check-time-envelope.py
```

<a id="r2"></a>
### R2 — High-frequency continuous cover

```text
python -B science/baseline/frontier/omission-verify.py
```

<a id="p1"></a>
### P1 — Finite history and low-frequency local price accounts

```text
python -B science/baseline/finite-history/verify-finite-history-independent.py
python -B science/baseline/finite-history/independent-time-local.py
```

<a id="p2"></a>
### P2 — Expanded-reference half-year output account

```text
python -B science/baseline/frontier/independent-omission.py
```

<a id="q1"></a>
### Q1 — Quarter maturity and actual fast output

```text
python -B science/baseline/frontier/independent-transfer.py --full
```

<a id="q2"></a>
### Q2 — Quarter full-reference and local complete accounts

```text
python -B science/baseline/frontier/independent-transfer-supplement.py --full
```

<a id="n1"></a>
### N1 — Nearby candidate proofs

```text
python -B science/experiments/nearby_independent.py --N 1024
python -B science/experiments/nearby_independent.py --N 2048
```

These individual readers may reuse an identity-matched per-point cache. The top-level `reproduce.py` removes those caches from its fresh copy before invoking the readers. To reproduce the corresponding actual fast outputs separately:

```text
python -B science/experiments/nearby_fast_replay.py --N 1024
python -B science/experiments/nearby_fast_replay.py --N 2048
```

<a id="n2"></a>
### N2 — Local 128-bin reused-bank control

```text
python -B science/experiments/local_output_independent.py
```

<a id="c1"></a>
### C1 — Matched complete-tolerance output controls

```text
python -B science/experiments/workload_controls_independent.py --N 2048 --local128
```

<a id="k1"></a>
### K1 — Dissipative kernel generation and independent assembly

```text
python -B science/analysis/kernel/generate.py --baseline science
python -B science/analysis/kernel/independent.py --baseline science
```

<a id="a1"></a>
### A1 — Secondary scientific audit generation and readback

```text
python -B science/analysis/audit/produce_audit.py --baseline science
python -B science/analysis/audit/read_audit_independent.py --baseline science
```

## Separate continuous generation

Run the following commands in a fresh staged scientific tree. They are separate operations from `reproduce.py --full`:

```text
python -B science/baseline/finite-history/run_evidence.py --regenerate-continuous
python -B science/baseline/frontier/run_frontier.py --regenerate-full
python -B science/experiments/nearby_generate.py --N 1024
python -B science/experiments/nearby_generate.py --N 2048
```

The low-frequency command regenerates the alpha=.52 continuous bank. The high-frequency command uses a separate reconstruction clone and preserves the fixed transfer inputs. The nearby generator creates missing components and otherwise retains identity-matched stored components; it does not force replacement of every retained field. Source identities, cache behaviour and shared dependencies are specified in the proof-obligation matrix in Appendix E.
