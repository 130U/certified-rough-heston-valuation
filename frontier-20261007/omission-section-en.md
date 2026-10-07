### 11.5. Certifying the omitted finite frequencies with a changed reference centre

The previous 4400–4500 spread certificate at $\alpha=13/25$ and $T=1/2$ deliberately set the approximate transform to zero at $64<u\le128$. Its full time-local bound was 0.367258782 index points. Even setting every low-frequency error radius to zero leaves a 0.352626734-point floor in that particular bound, because its fixed signed centre, finite omissions and complete remainder remain. This is a limitation of that certificate construction, not a lower bound on the true numerical error.

We froze a separate contract for the same spread, unchanged stored field, unchanged actual Padé output through $u=64$, and the existing 1, 0.5 and 0.25-point budgets before reading the new results. The expanded reference uses the already delivered nonzero stored-field transform $\bar\phi_u$ at all 1025 frequencies through 128. Consequently the signed reference-minus-fast centre must change. An old omitted-node bound on $|\phi_u-0|$ cannot be used as a bound on $|\phi_u-\bar\phi_u|$. We instead use

$$
|\phi_u-\bar\phi_u|\le\min\left\{B_\alpha(u)+|\bar\phi_u|,
\min(1,|\bar\phi_u|)\bigl(e^{\eta_u}-1\bigr)\right\},
$$

where the second bound depends on the complete-history propagation theorem and certified approximate half-plane condition. The computed radius is the minimum of rigorously rounded upper enclosures of these two bounds, and therefore still bounds the transform error. The new centre, its full outward arithmetic enclosure, the original analytic strip budget and the genuine infinite tail beyond 128 are all recomputed or retained explicitly.

No saved continuous residual certificate covered these 512 high frequencies. We therefore actually reconstructed their physical residual envelopes on all 8189 closed time cells of the unchanged field, including the first cell. All high-node startup and later approximate real-part upper bounds were nonpositive. A separate exact Caputo startup assembly passed for all 512 nodes. Saved-bank inspection checked all 4,192,768 residual entries, the complete partition, every node maximum and six deliberate failure controls. The independent reader additionally reconstructed all 1025 CF radii, the full reference centre, alternative trigonometric coefficient bounds and complete budgets; all eight of its failure controls were rejected. Scalar interval primitives and the original residual-enclosure mathematics remain shared dependencies, stated explicitly in the receipts.

| Newly certified high-node propagation | Matched signed marginal bound | Shared-node joint bound | 0.25-point budget |
| --- | ---: | ---: | --- |
| Complete-history global bound | 0.158585551 | 0.132245064 | Both pass |
| 128 preselected closed time bins | 0.137896018 | 0.115215934 | Both pass |

All displayed absolute bounds round upward. In both rows, the low frequencies retain their previously checked time-local radii; the row label describes only the new high-frequency propagation. The old signed centre is approximately $-0.166762218$ points, and the new centre approximately $-0.081698202$ points, a correction of $+0.085064016$ points. That correction is included in both complete error intervals. It is never discarded or combined with the old centre when reporting the new bound.

The quarter-point success is primarily enabled by certifying and recentering the previously omitted finite frequencies. The matched marginal bounds also pass the quarter-point budget; shared-node geometry provides a further reduction of approximately 16.6% and 16.4%, respectively. Intersecting the old and new complete error intervals produces no further improvement here. The high-node disks are not all embedded in their former zero-centred disks, so automatic nesting of the node uncertainty sets is not claimed.

Fresh high-node reconstruction took 575.027420 seconds of parent-measured cold wall time, including process startup, NumPy import, initialization, computation and matrix storage. Peak working set was 318,656,512 bytes (303.895 MiB rounded upward), below the frozen one-GiB limit. Python was 3.12.14 and NumPy 2.3.5; OMP, OpenBLAS, MKL and NumExpr thread settings were all pinned to one. Residual generation used outward binary64 interval arithmetic; reference, moment, exponential and final decision arithmetic used 100-bit dyadic intervals and exact rational comparisons. The separate reference, propagation and complete-budget aggregation replay took approximately 2.5 seconds; it reuses the newly generated residual bank and does not include its generation cost. These results concern this fixed field, parameter point, maturity, spread and actual fast output. They do not establish a minimum-runtime generation policy, profitability, or general calibration accuracy.

The default evidence path is `omission-verify.py` → `omission-aggregate.py` → `independent-omission.py`. Full regeneration is optional through `run_frontier.py --regenerate-full`, which operates on a separate working copy. Exact endpoints and hashes are in `omission-results.json`, `omission-node-ledger.json`, `omission-residual-high.json`, `omission-full-execution.json` and the two verification receipts.
