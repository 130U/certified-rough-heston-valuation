# Closed proof obligations for the kernel component

The assumptions are those of Theorem 3.3 and its authoritative AC proof, with sigma >= 0, q_alpha >= 0, nu > 0, zero initial state error, and an integrable physical residual envelope. The computational series additionally assumes the declared forward curve, 0 <= V0 <= theta, lambda*T^alpha < 1 and lambda_xi*T^alpha0 < 1. A curve-kernel assertion is an analytic propagation statement; it asserts neither probabilistic admissibility for a new curve family nor martingale validity beyond the underlying model assumptions.

| Obligation | Closure | Evidence |
| --- | --- | --- |
| Caputo modulus comparison at AC regularity and endpoint passage | CLOSED-CITED / inherited local bridge | Authoritative V2 Appendix C proof, Kopteva source and V2 Li–Liu attribution |
| Positive resolvent for sigma >= 0, including sigma = 0 | CLOSED-CITED and local boundary identity | Kopteva positive inverse; k_0 = g_alpha |
| Initial V0 contribution and physical nu scale | CLOSED-LOCAL | q_alpha*g_alpha = xi; KR01–KR02 and explicit sigma-zero statement |
| Resolvent composition K + lambda*g_alpha*K = xi | CLOSED-LOCAL | Convolution identity in kernel-proof-en.md |
| Unique convergent cumulative series | CLOSED-LOCAL | L1 absolute geometric majorant, KR10–KR12 |
| First omitted outer index and Gamma lower bound | CLOSED-LOCAL | Twelve retained terms omit n >= 12; every argument >= 2; log convexity proof |
| Signed inner curve series and finite tail | CLOSED-LOCAL | KR12–KR13; all signed multiplications are outward intervals |
| Positive cell weights and curve cap | CLOSED-LOCAL | KR14; 0 <= K <= xi; no history restart |
| Closed-cell residual maxima and complete prices | CLOSED-LOCAL machine replay | independent.json: all bank entries, all 128 maxima, all 513 minima and all 12 prices |
| Zero-damping computational boundary | CLOSED-LOCAL machine replay | 129 cumulative endpoints and 128 cell comparisons |
| Reader independence scope | Explicit shared boundary | Separate double Gamma cumulative formula; shared identified strict primitives and upstream proof |

No open obligation is silently promoted to a theorem. The negative-damping case is outside scope. The kernel experiment is one complete fixed configuration, rather than a continuous parameter study. The reported gain is a guaranteed-bound reduction; no observed true error is available from this certificate.
