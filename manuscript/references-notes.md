# Reference Versions and Proof Correspondence

This note records the sources and proof materials used by *Structural Properties, Price Error Bounds, and Candidate Selection Stability for the Third-Order Rational Rough Heston Approximation*. It translates the relevant entries of the Chinese reference audit and proof map. Page and theorem locators refer to the versions stated below.

## 1. Model, construction, and analytical tools

| Citation key | Version used and publication record | Locator and role |
|---|---|---|
| GR2019 | Gatheral–Radoičić, *Rational Approximation of the Rough Heston Solution*. The supplied SSRN manuscript has a title-page date of 2019-01-29. The first SSRN posting was 2018-06-20. The journal article appeared online on 2019-05-17 in IJTAF 22(3), 1950010. | §4.1, equations (4.3)–(4.17), pp.7–9: the fixed six-condition third-order construction. The present structural theorem concerns this established approximation. |
| GR2023v1 | Gatheral–Radoičić, *A Generalization of the Rational Rough Heston Approximation*, arXiv:2310.09181v1, submitted 2023-10-13; PDF cover dated 2023-10-16. The journal article appeared online on 2024-01-22 in Quantitative Finance 24(2), 329–335. | Lemma 1.1, §§2–4, Appendix A: the mean-reversion construction and parameterisation. The version used is v1. |
| JK2020 | Jeng–Kiliçman, *Series Expansion and Fourth-Order Global Padé Approximation for a Rough Heston Solution*, publisher PDF, 2020-11-06; Mathematics 8(11), 1968, DOI 10.3390/math8111968. | §§5.1–5.3, equations (43)–(50), §7: fourth-order and two-endpoint matching precedents. Denominator conditions are compared with the specific construction analysed here. |
| JK2021 | Jeng–Kiliçman, *SPX Calibration of Option Approximations under Rough Heston Model*, twelve-page publisher PDF, 2021-10-21; Mathematics 9(21), 2675, DOI 10.3390/math9212675. | Equations 5 and 24, §4, Table 1: model parameters, prior SPX calibration, and the public sample. The published rounded parameters define the fixed conditional comparison in the example. |
| AbiJaberElEuch2018v1 | Abi Jaber–El Euch, *Markovian structure of the Volterra Heston model*, arXiv:1803.00477v1, submitted 2018-03-01; PDF dated 2018-03-02. Journal publication: SPL 149 (2019), 63–72. | Theorems 2.1 and 2.3, Example 2.2, H2, and the fractional-kernel table: the nonnegative variance probability model and affine transform. Appendix A verifies the assumptions used here. |
| LiLiu2018 | Li–Liu, *A Generalized Definition of Caputo Derivatives and Its Application to Fractional ODEs*, author-hosted published PDF; SIMA 50(3) (2018), 2867–2900, DOI 10.1137/17M1160318. | Proposition 3.11, p.2886, equations (38)–(41): the Caputo history formula and convexity tool. Section 4 proves the required adaptation for a regularised two-dimensional norm. |
| Simon2014 | Simon, *Comparing Fréchet and positive stable laws*, arXiv:1310.1888v2. First version: 2013-10-07; version used: 2014-01-27. Journal publication: EJP 19(16), 2014-01-28. | §6.2, Theorem 4, equations (6.4)–(6.8): complete monotonicity and comparison bounds for Mittag–Leffler functions. |
| TrefethenWeideman2014 | Trefethen–Weideman, *The Exponentially Convergent Trapezoidal Rule*, author-hosted published PDF; SIAM Review 56(3) (2014), 385–458, online 2014-08-07. | §5, Theorem 5.1, p.400 and pp.401–403: analytic-strip trapezoidal error. Section 6 verifies the pricing integrand's strip and boundary integrability. |
| NIST2010 | Olver et al., eds., *NIST Handbook of Mathematical Functions*, Cambridge University Press (2010), ISBN 9780521140638. | Classical Gamma/Beta reflection, recurrence, and log-convexity tools. The DLMF link is a locator; the joint inequalities and polynomial certificate used in this paper are proved separately. |
| Gilewicz2005 | Gilewicz–Pindor–Telega–Tokarzewski, *N-Point Padé Approximants and Two-Sided Estimates of Errors on the Real Axis for Stieltjes Functions*, IPPT-hosted published PDF; JCAM 178(1–2) (2005), 247–253, DOI 10.1016/j.cam.2003.12.051. | Lemmas 1–3 and Theorem 4, pp.248 and 250–251: the Stieltjes positive-measure theory. Our matching-construction proof uses its explicitly stated original-coefficient criterion. |
| EberleinGlauPapapantoleon2008v1 | Eberlein–Glau–Papapantoleon, *Analysis of valuation formulae and applications to exotic options in Lévy models*, arXiv:0809.3405v1, 2008-09-19; title as in that version. | Theorem 2.2, conditions (C1)–(C3), pp.5–7: analytical background for Fourier valuation. |

The mathematical locators above come from the saved primary-source audit. The English translation does not imply a new full-text reading or establish priority through bibliographic dates. A source supplies the construction, model, or analytical tool assigned to it; the paper's proofs specify the conclusions and assumptions for the present approximation.

## 2. Author implementations, data, and application context

| Citation key | Version and public date | Evidence and use |
|---|---|---|
| GatheralCode2023 | `jgatheral/RationalRoughHeston`, commit `d65ea96e4c113fbb330074dfaea3e7715d650bbd`, 2023-12-14 23:35:28 UTC. | `roughHestonPadeLambda.R`, lines 42–85: the established short-time, long-time, and denominator formulas. Used to identify the author's implementation, parameterisation, and construction. |
| WoonJengSPXDataset2021Frozen | Author repository, commit `860049da2b7486fe8aa509061eff23cc28c2ef89`, 2021-10-08. | README and ordinary-market CSV files; sample dated 2021-06-18. Market bid, ask, and midpoint IVs are distinguished from model columns. Saved market IVs define the normalised experiment. |
| CboeSPX2022 | Official Cboe press release, 2022-09-19, *Cboe to Further Expand S&P 500 Index Options Suite with New and Additional Daily Expirations*. | The SPX/XSP product-features paragraph specifies European exercise and cash settlement. Used only for product characteristics. |
| FederalReserveSR1107 | Federal Reserve and OCC, original SR 11-7 attachment, 2011-04-04. | §V, pp.9–15; p.11 lists three validation components, and p.13 discusses pricing benchmarks and outcomes analysis. Used as historical model-validation context. The price bounds concern specified calculations and quote comparisons. |

Primary application sources:

- [Cboe press release, 19 September 2022](https://ir.cboe.com/news/news-details/2022/Cboe-to-Further-Expand-SP-500-Index-Options-Suite-with-New-and-Additional-Daily-Expirations-09-19-2022/default.aspx).
- [Original SR 11-7 attachment](https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf).
- [Versioned author data repository](https://github.com/WoonJeng/Dataset-for-SPX-Calibration-of-Option-Approximations-under-Rough-Heston-model/tree/860049da2b7486fe8aa509061eff23cc28c2ef89).
- [Versioned Gatheral implementation](https://github.com/jgatheral/RationalRoughHeston/blob/d65ea96e4c113fbb330074dfaea3e7715d650bbd/roughHestonPadeLambda.R).

## 3. Proof and numerical-material correspondence

| Paper result | Location | Mathematical or numerical support |
|---|---|---|
| Nonsingular matching system, positive denominator real part, and left-half-plane trajectory for all real frequencies | Section 3 and Appendix B | Original polynomials, compactification, rigorous elementary-function intervals, and complete closed-rectangle covering; [full-frequency proof appendix](../pade-calibration-20261006/pade-full-frequency-appendix.md). |
| Complex dissipation and independent Caputo-residual bounds | Section 4 | Self-contained history-convexity and regularised-norm proofs; Proposition 3.11 of Li–Liu identifies the underlying convexity tool. |
| State error, characteristic exponent, and complete price error | Sections 5–7 | Positive-kernel exponent representation, the exact model's analytic strip, high-frequency tail, continuous-time residual intervals, and stated IEEE arithmetic assumptions; [price-proof map](../pade-calibration-20261006/PROOF_MAP.md). |
| Exact price, objective, and implementation-output intervals | Section 8 | Thirty-six price rows and three objective tables; [exact finite-candidate aggregation](../pade-calibration-20261006/finite-candidate-calibration-result.json). |
| Finite-candidate decision, rowwise quote separation, and call-spread valuation | Section 10, equations U1–U12 | [Exact financial example](../mechanism-report-20261006/finance-usecase-calculations.json) and [exact aggregation program](../mechanism-report-20261006/compute-finance-usecase.py). |

Normalised prices in Section 8 are denoted by `c_i`, and unnormalised prices by `C_i`. The Riccati constant term is denoted by `c_0`. These conventions separate price units and state-equation notation; the price endpoints and mathematical relations are unchanged.

For the financial example, all candidates use the same fixed forward variance curve, remaining parameters, six-month maturity, twelve IV-defined normalised prices, and squared objective. The full-frequency structural domain is the order interval stated in Theorem 3.1. The three candidate price certificates are assessed through their corresponding reference trajectories. The finite-set decision follows from their strict objective separation.

## 4. Translation verification

The complete English manuscript retains all eleven numbered main sections, three appendices, fifteen reference entries, and sixty-three numerical table rows of the Chinese source. It contains all 510 mathematical spans in the original order. Of these, 508 are preserved verbatim. Two spans translate only Chinese condition text: “if” in equation (4.7) and “otherwise” in the piecewise definition in Section 8.2. Mathematical symbols, conditions, and equation tags are preserved.

The translation introduces no new pricing computation, calibration, mathematical result, or historical completion claim. Its source identity and final manuscript digest are recorded in [translation-qa.json](translation-qa.json). The protected translation files and mathematical mapping are working records rather than additional scientific claims.
