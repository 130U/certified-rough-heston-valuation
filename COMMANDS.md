# Verification commands

Each code-block line is a complete, copyable command. Paths are relative to the project root. Full scientific checks require the complete numerical banks retained in the author's local evidence archive.

## Source identities

```text
python -B verify_source.py
```

This checks the public source identities. It does not execute the numerical banks. The public checkout omits 27 large banks; the complete scientific commands below require the author's complete local evidence copy.

## Complete scientific check

```text
python -m pip install -r requirements.txt
python reproduce.py --manifest-only
python reproduce.py --full
```

The driver checks the scientific manifest before creating an isolated working copy. It reads saved banks and reconstructs downstream prices, objectives, outputs and decisions. `--full` additionally recomputes the original complete structural-sign cover. Neither mode regenerates every continuous residual derivative bound.

## Individual obligations

Use a separate disposable extraction for individual commands, because generators and some readers write local receipts. The full driver above preserves the distributed input identities and is the preferred integrated check. Individual readers retain the continuous-generator and arithmetic-library dependencies described in Appendix E.

<a id="s1"></a>
### S1 — Original Padé structural signs

```text
python -B science/baseline/continuous/full_structure_verify.py
```

<a id="s2"></a>
### S2 — Startup Caputo residual and half-plane enclosure

```text
python -B science/baseline/continuous/startup_independent.py
```

<a id="r1"></a>
### R1 — Original low-frequency continuous cover

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

<a id="g1"></a>
### G1 — Classical appendix identities and semantic controls

```text
python -B science/analysis/verify_extensions.py
```

## Separate continuous generation

The following commands are separate operations on a disposable scientific extraction; they do not describe additional work performed by `reproduce.py --full`:

```text
python -B science/baseline/finite-history/run_evidence.py --regenerate-continuous
python -B science/baseline/frontier/run_frontier.py --regenerate-full
python -B science/experiments/nearby_generate.py --N 1024
python -B science/experiments/nearby_generate.py --N 2048
```

The low-frequency command regenerates the original alpha=.52 continuous bank. The high-frequency command uses a separate reconstruction clone and preserves the fixed transfer inputs. The nearby generator creates missing components and otherwise retains identity-matched stored components; it does not force replacement of every retained field. Source identities, cache behavior and shared dependencies remain governed by the released proof-obligation matrix and Appendix E.
