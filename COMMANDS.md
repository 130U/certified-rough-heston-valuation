# Verification commands

These commands accompany Appendix E. Each code-block line is a complete command; command text contains no discretionary line breaks or inserted hyphenation.

## Editorial source identities

Run from the root of the complete V5 source checkout, where `inherited-v3/` contains the original 472 V3 source files:

```text
python -B verify_source.py
```

This checks the new editorial manifests, chronology and unchanged inherited V3 source. It does not execute the scientific bank. The small V5 overlay omits `inherited-v3/`; use the full source checkout or supply the exact fixed V3 source under that directory before running this command.

## Complete scientific acceptance

Download and verify the named [V3 scientific archive](https://github.com/130U/certified-rough-heston-valuation/releases/download/v3.0.0-research-20261007/Theodore-Ouyang-Heston-V3-Evidence-20261007.zip), then extract it into a separate working directory. Run from that extracted archive's root:

```text
python -m pip install -r requirements.txt
python reproduce.py --full
```

The root driver first verifies all scientific inputs, makes a fresh working copy and clears identity-matched nearby reader caches before acceptance. `--full` adds the original complete structural-sign cover; it does not regenerate every continuous residual derivative bound. GitHub's automatic source ZIP and the V5 editorial ZIP omit the 27 large NPZ banks needed for these scientific commands.

## Individual scientific obligations

Run the following commands from a **separate disposable extraction of the complete V3 scientific archive**, not from the V5 source tree. Every path below is relative to that scientific archive's root. Individual generators and some readers write local scientific receipts; this disposable extraction preserves the downloaded archive and its frozen input identities. The full driver above is the preferred integrated acceptance entry point. Individual commands inspect the obligation named in Appendix E; they do not independently establish every inherited continuous-derivative or elementary-library theorem.

<a id="s1"></a>
### S1 — Original Padé structural signs

```text
python -B baseline/bc-merged-20261007/full_structure_verify.py
```

<a id="s2"></a>
### S2 — Startup Caputo residual and half-plane enclosure

```text
python -B baseline/bc-merged-20261007/startup_independent.py
```

<a id="r1"></a>
### R1 — Original low-frequency continuous cover

```text
python -B baseline/heston-nine-point-20261007/check-time-envelope.py
```

<a id="r2"></a>
### R2 — High-frequency continuous cover

```text
python -B baseline/heston-frontier-20261007/omission-verify.py
```

<a id="p1"></a>
### P1 — Finite history and low-frequency local price accounts

```text
python -B baseline/heston-nine-point-20261007/verify-finite-history-independent.py
python -B baseline/heston-nine-point-20261007/independent-time-local.py
```

<a id="p2"></a>
### P2 — Expanded-reference half-year output account

```text
python -B baseline/heston-frontier-20261007/independent-omission.py
```

<a id="q1"></a>
### Q1 — Quarter maturity and actual fast output

```text
python -B baseline/heston-frontier-20261007/independent-transfer.py --full
```

<a id="q2"></a>
### Q2 — Quarter full-reference and local complete accounts

```text
python -B baseline/heston-frontier-20261007/independent-transfer-supplement.py --full
```

<a id="n1"></a>
### N1 — Nearby candidate proofs

```text
python -B new-research/experiments/nearby_independent.py --N 1024
python -B new-research/experiments/nearby_independent.py --N 2048
```

These individual readers may reuse an identity-matched per-point cache. The top-level `reproduce.py` removes those caches from its fresh copy before invoking the readers. To reproduce the corresponding actual fast outputs separately:

```text
python -B new-research/experiments/nearby_fast_replay.py --N 1024
python -B new-research/experiments/nearby_fast_replay.py --N 2048
```

<a id="n2"></a>
### N2 — Local 128-bin reused-bank control

```text
python -B new-research/experiments/local_output_independent.py
```

<a id="c1"></a>
### C1 — Matched complete-tolerance output controls

```text
python -B new-research/experiments/workload_controls_independent.py --N 2048 --local128
```

<a id="k1"></a>
### K1 — Dissipative kernel generation and independent assembly

```text
python -B v3/kernel/generate.py --baseline .
python -B v3/kernel/independent.py --baseline .
```

<a id="a1"></a>
### A1 — Secondary scientific audit generation and readback

```text
python -B v3/audit-experiments/produce_audit.py --baseline .
python -B v3/audit-experiments/read_audit_independent.py --baseline .
```

<a id="g1"></a>
### G1 — Classical appendix identities and semantic controls

```text
python -B v3/extensions/check_appendices.py
```

## Separate continuous generation

The following commands are separate operations on a disposable scientific extraction; they do not describe additional work performed by `reproduce.py --full`:

```text
python -B baseline/heston-nine-point-20261007/run_evidence.py --regenerate-continuous
python -B baseline/heston-frontier-20261007/run_frontier.py --regenerate-full
python -B new-research/experiments/nearby_generate.py --N 1024
python -B new-research/experiments/nearby_generate.py --N 2048
```

The low-frequency command regenerates the original alpha=.52 continuous bank. The high-frequency command uses a separate reconstruction clone and preserves the fixed transfer inputs. The nearby generator creates missing components and otherwise retains identity-matched stored components; it does not force replacement of every retained field. Source identities, cache behavior and shared dependencies remain governed by the released proof-obligation matrix and Appendix E.
