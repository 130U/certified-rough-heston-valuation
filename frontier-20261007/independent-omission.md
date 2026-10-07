# Independent omitted-node audit

PASS_INDEPENDENT_OMISSION_FULL_HISTORY_RECENTER_AND_BUDGET_AUDIT

Verified all 1025 finite nodes, 8189 closed time cells per node and 128 fixed bins; the actual fast output is unchanged while the complete reference centre changes. Every reference arithmetic, strip and genuine tail term is retained. The checker uses real sine-identity support coefficients and exact Fraction reference sums, and recomputes all node residual-to-CF radii. The shared primitive boundary is explicit in the JSON.

The outward full error bounds about the unchanged fast output are 0.132245064 index points for high-node global propagation and 0.115215934 index points for high-node time-local propagation. Both retain the fixed, already verified low-node time-local radii and pass the 1, 1/2 and 1/4 point budgets. These are certified upper bounds for the original fixed field at alpha = 13/25 and T = 1/2, rather than observations of the actual pricing error.

This checker audits the complete saved envelopes and does not regenerate reference trajectories. The current full high-node reconstruction has a separately recorded parent cold wall time of 575.0274200000567 seconds; the earlier low-node reconstruction is a dependency. The original outward arithmetic primitives and continuous-residual generator inequalities are shared.

- omit_new_signed_reference_correction: rejected.
- missing_high_node: rejected.
- remove_startup_timecell: rejected.
- insert_fractional_history_time_gap: rejected.
- source_checksum_change: rejected.
- wrong_quarter_point_budget: rejected.
- reuse_zero_radius_without_new_centre_translation: rejected.
- delete_strip_tail_reference_arithmetic: rejected.

Run offline from the reader-package root: python research/heston-frontier-20261007/independent-omission.py.
