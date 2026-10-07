All experiments use model parameter $\nu=0.2897$, $\rho=-0.7445$, Riccati mean reversion zero, Fourier step $1/8$, a finite reference/error grid through 128 (1025 nodes), 100-bit outward dyadic arithmetic and 64 forward-moment series terms. The actual Padé output uses composite Gauss–Legendre order 8 through 200 (352 nodes) and Jacobi order 256; its Fourier cutoff is distinct from the certificate cutoff. $N_t$ counts source time cells. The number of frequency nodes is written explicitly to avoid confusing it with $\nu$.

| ID | T | alpha | N_t source cells | nonzero ref nodes | zero finite nodes | subcells | history bins |
| --- | --- | --- | --- | --- | --- | --- | --- |
| H0 | 1/2 | 13/25, 3/5, 9/10 | 2048 / 2048 / 1024 | 513 | 512 | 4 | 0 |
| H1 | 1/2 | 13/25, 3/5, 9/10 | 2048 / 2048 / 1024 | 513 | 512 | 4 | 1 |
| H2 | 1/2 | 13/25 | 2048 | 513 | 512 | 4 | 128 |
| H3 | 1/2 | 13/25 | 2048 | 1025 | 0 | 4 | low128; high1 |
| H4 | 1/2 | 13/25 | 2048 | 1025 | 0 | 4 | 128 |
| Q0 | 1/4 | 13/25, 3/5, 9/10 | 1429 / 1352 / 549 | 513 | 512 | 4 | 1 |
| Q1 | 1/4 | 13/25 | 1429 | 1025 | 0 | 4 | 1 |
| Q2 | 1/4 | 13/25 | 1429 | 1025 | 0 | 4 | 128 |
| N1 | 1/2 | 13/25, 21/40, 53/100, 27/50, 11/20 | 1024 | 513 | 512 | 2 | 1 |
| N2 | 1/2 | 13/25, 21/40, 53/100, 27/50, 11/20 | 2048 | 513 | 512 | 2 | 1 |
| N2L | 1/2 | 13/25 | 2048 | 513 | 512 | 2 | 128 |

H0 uses the old uniform-state propagation; H1 uses finite-horizon global propagation on the identical field. H2 retains the original low-frequency 128-bin bank. H3/H4 expand the same reference centre through 128, retaining that low bank and adding the newly certified high bank with global/128-bin propagation. Q0/Q1/Q2 keep full history from zero and use exact quarter-terminal interpolation of the original half-year field: Q0 has 1430/1353/550 time knots, and Q1/Q2 have 1430 knots. Their larger-horizon continuous banks are reused; quarter moments, output and tails are recomputed. The original alpha=.9 source field has 1025 time knots and 641 stored frequencies through 80; only 513 are nonzero reference nodes in H0/H1/Q0. The .52/.60 original fields have 2049 knots and 1025 stored frequencies through 128.

N1/N2 regenerate each five-point field and its continuous residual bank, with two nonstartup subcells (2047/4095 closed cells). N2L is a separately frozen descriptive 128-bin reuse of N2 at alpha=.52; it does not replace the nearby-grid objective experiment. The old low and high banks each have 8189 closed cells (four nonstartup subcells), for 513 and 512 frequencies respectively. Thus the 0.115215934-point H4 certificate and 0.394999331-point N2L certificate concern different reference centres, node coverage and residual banks. Their difference cannot be attributed solely to 128-bin propagation. BL-core512/1024 are nominal history-stepping controls whose complete guarantees use the explicitly identified N1/N2/N2L reference bank.
