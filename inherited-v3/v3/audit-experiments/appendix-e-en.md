### E.2. Numerical identities, scope and evidence map

All configuration IDs and mathematical dimensions are fixed in configuration-registry.json. The following table states the actual reader obligation. Shared elementary interval primitives, shared continuous-derivative generator, reused fixed scientific input and an independently written assembly are distinct types of dependence. These are author-side acceptance checks; no outside referee execution is presumed.

| ID | Obligation | Verification command | Recomputed | Inherited / shared |
| --- | --- | --- | --- | --- |
| S1 | Padé coefficient signs on the original parameter rectangle | python bc-merged-20261007/full_structure_verify.py | 211241 structural sign leaves and rectangle cover | model/parameter definitions; original strict interval algebra and generalized-power primitives |
| S2 | Startup Caputo residual and left-halfplane enclosure | python bc-merged-20261007/startup_independent.py | all 513 frequencies for each of the three original startup cells | stored field dyadics and later-time continuous residuals; Gamma/power/dyadic outward primitives |
| R1 | Full original alpha=.52 low-frequency continuous residual cover | python heston-nine-point-20261007/check-time-envelope.py | 8189 closed cells x513 entries: cover, saved dyadic values and per-node maxima; startup audited separately | derivative inequalities in identified continuous generator; NumPy enclosure with proved dot-product error and strict scalar primitives |
| R2 | Full alpha=.52 high-frequency continuous residual cover | python heston-frontier-20261007/omission-verify.py | 8189 closed cells x512 entries: exact bank, startup/halfplane, saved-node maxima | identified Caputo derivative-generator inequalities; strict scalar primitives and original continuous generator |
| P1 | Global finite-history and low-frequency128-bin price accounts | python heston-nine-point-20261007/verify-finite-history-independent.py; python heston-nine-point-20261007/independent-time-local.py | forward masses, complete cell intersections, 513 tightened radii, all 1025 finite terms and complete spread remainder | continuous residual theorem/validity and identified stored field; strict forward-moment, exponent and true-tail primitives |
| P2 | Expanded-reference frozen half-year output account | python heston-frontier-20261007/independent-omission.py | changed reference centre, all 1025 support terms, old/new complete interval intersection, global/local high-frequency accounts | same actual fast output and continuous residual banks; original strict moment/scalar primitives |
| Q1 | Quarter-maturity used64 certificate and actual fast output | python heston-frontier-20261007/independent-transfer.py --full | all three exact terminal interpolations, 1539 restricted exponents, three original fast-output calculations, all 3075 true finite CF/tail/price terms | larger-horizon continuous residuals and halfplane certificate; strict moment/trig/dyadic/true-tail libraries; original fast implementation used only for output replay |
| Q2 | Quarter full128 global and128-bin complete certificate | python heston-frontier-20261007/independent-transfer-supplement.py --full | all 1025 restricted exponents, all 1025 CF/tail/coefficient/radius terms, all high bank entries, all 128 local weights and exact account | low/high continuous derivative validity; actual fast replay is separately performed by Q1; strict moment/trig/dyadic/true-tail libraries; path helpers of Q1 |
| N1 | Fresh fields/residuals at the five nearby alpha points | python nearby_independent.py --N 1024; python nearby_independent.py --N 2048 | all cells, startup, halfplane, 513 exponents and 1025 CF/coefficient terms per point; all objective/pair decisions | strict proof of continuous residual generator and final propagation theorem; declared sdk outward primitives, stored reference data |
| N2 | Descriptive128-bin reused-bank control, outside nearby objective grid | python local_output_independent.py | 128 exact positive weights, every intersecting closed-bank maximum, 513 tightened radii, all 12 prices and allactual output rounding | complete identity-matched N2048 point proof and continuous residual generator; same strict moment/trig/dyadic primitives |
| C1 | Same model and complete tolerance for frozen/direct/corrected/BL-core outputs | python workload_controls_independent.py --N 2048 --local128 | exact stored-output centre translation, allsame-reference remainder and28 portfolio supports; BL nominal-output metadata identity | reference certificate, BL nominal-output producer and its stored dyadics; same strict outward coefficient primitives |

Exact generation commands, their empty-tree versus retained-input behavior, source hashes and boundary notes are in proof-obligation-matrix.json. Run commands in a disposable relative work copy to preserve the fixed packet. In particular, nearby_generate.py regenerates missing fields/residuals, but retains identity-matched components when present. nearby_independent.py can use an identity-matched per-point cache; the top-level fresh acceptance driver deletes every such cache before invocation.

For the explicitly retained V2 entrypoint source snapshots, the complete --full distinction is:

| Entry point | Additional executed obligation | Outside that command |
| --- | --- | --- |
| reproduce.py default | fixed-copy saved evidence readers; original frontier always requests bothquarter readers --full; new nearby reader point caches deleted by this top driver | all continuous residual generators or all structural signs |
| reproduce.py --full | default plus all211241 original structural sign leaves | fresh low/high/new-nearby continuous derivative generation |
| baseline/.../run_evidence.py --regenerate-continuous | original alpha=.52 513-node low continuous generator and retained8189-cell bank | new five-alpha reference/residual generation |
| baseline/.../run_frontier.py --regenerate-full | separate-clone full 512 high continuous generator plus fresh-bank audit | alter fixed quarter input receipts |
| nearby_generate.py --N N | missing field/residual/exponent components; otherwise reuses identified existing components | force regeneration over already retained scientific output |
| publication-v2 CI source.yml | source manifest identities and retained acceptance receipt binding | NumPy bank replay, interval arithmetic replay or residual generation |

Thus the retained V2 reproduce.py --full adds structural-sign regeneration. It does not regenerate all continuous residual derivatives. Its source SHA is not imposed on the new V3 top-level driver. The original low continuous generator requires run_evidence.py --regenerate-continuous; the high-frequency generator requires run_frontier.py --regenerate-full, which uses a distinct reconstruction clone and preserves the fixed transfer input receipts. The historical CI checks source identities and the retained acceptance receipt binding; it does not perform the large-bank interval replay. A stored PASS receipt, byte identities, executed recomputation and a mathematical theorem remain separately identifiable evidence.

The exact closest-pair gap equals the sum of the following signed contributions; scientific notation is a display only:

| Gap contribution | Normalized loss contribution |
| --- | --- |
| reference_midpoint_objective_difference | 7.939186982887e-09 |
| used_node_support_both_candidates | -4.690368762320e-09 |
| finite_zero_support_both_candidates | -1.217354923855e-09 |
| strip_both_candidates | -1.855578458131e-12 |
| true_infinite_tail_both_candidates | -9.568024410400e-11 |
| reference_arithmetic_both_candidates | -6.928606526135e-23 |
| midpoint_conversion_arithmetic_both_candidates | -4.770477111773e-27 |
| candidate_a_quadratic_remainder | -1.195663126282e-09 |
| box_intersection_endpoint_adjustment | 0.000000000000e+00 |

The quarterly account has zero finite omissions; its infinite tail beyond128 remains paid. The unused-node term in the nearby/global controls is nonzero and cannot be dropped by borrowing the quarter full-reference result. Exact ledger fractions and all 40 pair-mode records are delivered with independent secondary readback and intentional corruption controls.

Common ideal strict-reference floor in the BL-core complete bound:

| Bank | Nominal output | Reference floor points | Translation points | Floor / complete bound |
| --- | --- | --- | --- | --- |
| N1 | BL modified-Adams core N=512 | 0.423484833 | 0.000853401 | 99.798887% |
| N1 | BL modified-Adams core N=1024 | 0.423484833 | 0.000305328 | 99.927953% |
| N2 | BL modified-Adams core N=512 | 0.261808768 | 0.000845646 | 99.678039% |
| N2 | BL modified-Adams core N=1024 | 0.261808768 | 0.000297572 | 99.886469% |
| N2L | BL modified-Adams core N=512 | 0.228237113 | 0.000845646 | 99.630856% |
| N2L | BL modified-Adams core N=1024 | 0.228237113 | 0.000297572 | 99.869791% |

The separate returned-reference ratio also pays binary64 return rounding and is retained in the machine ledger. A small BL512/1024 nominal difference is an empirical comparison; its complete guarantee uses the same reference floor plus exact output translation. These floor fractions do not establish an intrinsic BL error estimate.

portfolio-pass-counts.svg and portfolio-pass-counts.pdf show the exact-endpoint pass-count step functions for the original three candidates and the regenerated alpha=.52 controls. Coordinates are converted to display decimals only after exact counting. The plotted 0–2-point range is stated explicitly; all thresholds are retained in the CSV/JSON. Cross-bank curves are descriptive and within-bank methods share radii. Only typed scientific work counts, evidence bytes and version/hash identities are used; no host or duration measurements are part of this audit.
