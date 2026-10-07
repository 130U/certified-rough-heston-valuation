# Assembly and proof-dependency audit

This audit concerns the major-revision assembly, rather than a new numerical certificate. The frozen predecessor was read without modification. Only the theory directory is owned by this audit.

## Required mapping corrections

1. A global theorem-reference map must protect source-paper locators. The citation to El Euch–Rosenbaum is **Proposition 3.1 and Corollary 3.3** of that paper. Mapping the first locator to Proposition 6.1 changes the source and must be rejected.
2. The Chinese Appendix C heading must be recognised by the display-numbering parser. A heading written "## 附录C." is not matched by a parser requiring "## 附录 C.". The intended appendix exponent formulas require C numbering, rather than continuing Appendix B.
3. The Chinese version of Proposition 3.6 requires the same explicit positive-time regularity assumption as its English counterpart:

   > 设参考轨迹绝对连续、在每个正时间邻域局部 Lipschitz，且具有相同初值。若 \(\delta_F<s_0^2/2\)，则其误差满足

4. The Chinese residual-provider reference written "第 7 节" requires the new locator "第4.1节"; replacing only unspaced strings is insufficient.
5. The completely monotone Mittag–Leffler representation in Appendix C cites SimonCM2015 in both languages. Simon2014 remains appropriate for the separately used Mittag–Leffler inequality.

## Proof-dependency checks

- The old omitted-node reference proposition is now correctly under Section 5.1 as Proposition 5.2 in both languages. Its new reference centre is translated to the same actual output, and its finite-node disks, true infinite tail, strip and reference arithmetic remain included.
- The explicit fractional-integral derivative bound near zero is integrable for \(\alpha>1/2\). Combined with the positive-time derivative continuity and the initial limit, it supplies the claimed AC state regularity. Global continuation preserves the earlier history as forcing.
- The finite-history theorem does not rely on the scalar first-hitting proof. Its vector AC modulus comparison uses the directly proved regularity bridge and the positive zero-initial-value inverse. The continuous convolution extends the a.e. state estimate to maturity.
- The pricing composition retains both the curve initial term \(V_0g_{1-\alpha}\) and physical factor \(\nu^{-1}\). The curve extension relaxes an analytical condition only and does not by itself establish stochastic-model admissibility.
- The reference field is continuous and piecewise linear after its explicit startup powers. Consequently its fractional integral is AC and locally Lipschitz at positive times; this supports the separate first-hitting proposition when its small-residual hypotheses hold.
- Appendix A's interval \(\alpha\in[.52,.9]\) covers all five new nearby candidates.
- The continuity result in correlation concerns the specified Padé construction. The independent pricing-reference route has separate hypotheses. No altered-correlation price experiment is implied by Theorem 6.2.
- The successful direct correlation supplement is exploratory after the unresolved prespecified derivative-only attempt. The strict fallback and failed stage remain in evidence. The successful complete supplement has a separate frozen protocol and independent determinant replay.

## Presentation clarifications

The derivative-only global exponent bound may be retained as a complementary result. In the independent-reference description, \(E_\delta\) is available only under its small-residual condition; otherwise the certified approximate half-plane permits the linear state radius \(E=\delta_F/\sigma\). The current experiments principally use the sharper finite-history exponent theorem. The text should avoid making a small-residual premise appear universal.

The theorem order should introduce Theorem 3.2 before Theorem 3.3 if its existing numbering is retained. This is a reading-order issue, not a missing dependency of the finite-history proof.

Source-paper theorem locators, manuscript theorem locators and display-equation identifiers require distinct mapping rules. Protecting citation brackets before an internal theorem rewrite is sufficient for the identified source-locator corruption; source citations in ordinary prose still require deliberate review.

## Read-back after the assembly repair

The regenerated English and Chinese sources were inspected. The El Euch–Rosenbaum locator remains Proposition 3.1; the Chinese exponent appendix has display identifiers C.1–C.7; Chinese Proposition 3.6 explicitly includes positive-time local Lipschitz regularity; the residual-provider locator and completely monotone citation have been corrected. Theorem 3.2 now precedes Theorem 3.3. Both languages contain the full successful correlation interval, 281568 closed cells and 19808 independently replayed direct cells.

The residual-radius clarification in Section 4.3 remains a recommendation at this read-back checkpoint. Removing the Chinese phrase “原定理 9.2” from the central theorem is a minor editorial cleanup.
