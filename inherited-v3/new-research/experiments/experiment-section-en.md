### Real nearby candidates: complete finite-set comparison

The original twelve half-year quotes, forward F=4221.86, discount D=1,
and all other model parameters are fixed. Before computing new results we
froze alpha={0.520,0.525,0.530,0.540,0.550}, a first layer N=1024, and an
upgrade of **all five** candidates to N=2048 if any adjacent joint comparison
remained unresolved. Every point has a newly generated continuous reference
field and a complete closed-time residual bank. Fourier nodes through 64,
all omitted finite nodes through 128, true infinite tails, strip remainder,
reference arithmetic and original quote-conversion intervals are paid.

The objective is the original normalized midpoint loss
J=(1/24) sum_i (c_i-m_i)^2. Here the tiny target interval halfwidth is only
outward arithmetic error in converting the fixed bid/ask-price midpoint;
it is not the market bid/ask halfwidth. Ranking does not establish a uniform
winner for arbitrary quote targets inside those market bands.
A Taylor support enclosure preserves common
Fourier disks in its linear term and charges the full coordinate-radius
quadratic remainder. Its same-radius marginal comparison uses the identical
upstream certificate. Errors across different alpha candidates are not
assumed jointly correlated.

| alpha | N=1024 joint J ×10^8 | N=2048 joint J ×10^8 |
|---:|---:|---:|
| 0.520 | [4.825094, 6.778350] | [5.293449, 6.024095] |
| 0.525 | [5.645378, 7.501414] | [6.097920, 6.798485] |
| 0.530 | [6.748974, 8.517584] | [7.187004, 7.859529] |
| 0.540 | [9.807435, 11.422182] | [10.218707, 10.839486] |
| 0.550 | [14.000658, 15.482012] | [14.387007, 14.960680] |

| Generated layer | Joint strictly separated pairs | Matched marginal pairs |
|---|---:|---:|
| N=1024 | 7/10 | 3/10 |
| N=2048 | 10/10 | 7/10 |

The first layer retained its unresolved close pairs and triggered the frozen
all-candidate upgrade. The final finite grid has alpha=0.520 as a strict minimum.
This is a five-point comparison, not a continuous calibration optimum. All
five candidates remain incompatible with at least one original bid/ask row;
the finite-set result therefore does not identify a market-calibrated model.

### Why certify the frozen output after computing a reference?

We distinguish a frozen production-output audit from freely replacing the
output in a fresh pricing task. The ideal exact correction equals the rational
reference centre, but actual returned reference values, stored binary64
corrections and the final binary64 addition are separately frozen and their
exact dyadic rounding errors are paid. Once a strict reference has already
been computed, returning that reference is the simpler choice for a one-off
price. Frozen-output certificates are useful for auditing an existing library
and for repeated tasks sharing one proof bank; we make no general speed claim.

To test this distinction, a separate descriptive control was frozen after
the N=2048 global account was known. It reuses the complete alpha=0.52
closed residual bank with 128 physical-time propagation bins. Every bin
uses the maximum over all intersecting closed source cells and retains
history from zero. This control leaves the nearby-grid study unchanged.
All five returned-output methods use the same radius, reference, full
remainders, half-year 4400/4500 spread and quarter-point tolerance.

| Returned output | Complete joint bound, points | Matched marginal bound, points | Joint quarter-point decision |
|---|---:|---:|---|
| Frozen Padé | 0.394999331 | 0.514096070 | UNRESOLVED |
| Direct binary64 reference | 0.228237113 | 0.347333852 | PASS |
| Padé + stored correction + binary64 addition | 0.228237113 | 0.347333852 | PASS |
| BL-modified Adams core, 512 steps | 0.229082759 | 0.348179497 | PASS |
| BL-modified Adams core, 1024 steps | 0.228534686 | 0.347631424 | PASS |

The modern comparison implements the BL-modified Adams Riccati core of
Boyarchenko et al. (2025, Section 3.2 and Appendix B): frequency scaling,
leading asymptotic subtraction, linear Adams history and eight Picard
corrections. It is adapted to our declared forward-variance model and uses
flat Fourier inversion. It does not reproduce SINH-CB. Its 512/1024 nominal
spread difference is an empirical diagnostic; deterministic guarantees in
the table come from the complete shared reference certificate and signed
centre translation, not empirical agreement or conformal bootstrap.

We report deterministic mathematical workload only. The two five-candidate
layers generate 15,754,230 complete closed-node residual entries, 5,130 strict
reference exponents and 10,250 true-CF node envelopes. Each point proof
supports all twelve prices; the 28 fixed portfolios require 28×1025 further
joint support terms and **zero** additional residual generation. The descriptive
128-bin control reuses 2,100,735 existing residual entries and pays 128×513
weighted residual terms. Verification reconstructs the complete mathematical
accounts. These counts do not equate binary64 operations with strict dyadic
transcendental primitives and do not support a universal cost ratio.
