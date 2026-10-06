# Certified Rough Heston Valuation

**Theodore Ouyang · Mathematical finance**

A mathematical study of a practical question: **can a fast rational pricing approximation change the roughness candidate selected from option quotes, and how can that decision be checked?**

The project connects the structure of a fixed third-order rational approximation, complex fractional-Riccati stability, and complete Fourier pricing bounds. It uses explicit model and parameter conditions to turn independently bounded residuals into price intervals and then into a finite-candidate selection guarantee.

**[Read the paper](manuscript/rough-heston.md)** · **[Download the PDF](paper/Theodore-Ouyang-Certified-Rough-Heston-Valuation.pdf)** · **[Reproduce the checks](code/README.md)**

## Principal results

For the Gatheral–Radoičić six-condition two-point third-order construction, the structural theorem holds on

```math
\alpha\in[0.52,0.60],\qquad \rho=-0.7445,\qquad \lambda_R=0,
\qquad u\in\mathbb R,\quad t\ge0.
```

The original matching system is nonsingular. The three normalized denominator coefficients satisfy

```math
\operatorname{Re}q_j>0\quad(j=1,2,3),\qquad
\operatorname{Re}Q(y)\ge1,
```

and the approximation remains in the left half-plane for positive time. The proof works with the raw matching determinant and Cramer numerators before normalization.

For the specified half-year SPX normalized-price example, twelve strikes and the finite candidate set

```math
\alpha\in\{0.52,0.60,0.90\}
```

give a strict model-objective gap greater than **2.70205218 × 10⁻⁷**. Both the continuous-time model and the frozen third-order pricing procedure uniquely select **α = 0.52**, corresponding to **H = 0.02**. This is a fixed-profile comparison: the forward variance curve and the other parameters are held constant across candidates.

The 4400–4500 call spread has the model-price enclosure

```math
c_{4400}-c_{4500}\in[0.008074526019566,\;0.009265076200129].
```

Its frozen rational output differs from the model spread by less than **0.000634774793739** in normalized units (C/(DF)). The experiment sets (D=1), (F=4221.86), and (T=1/2). Definitions, proofs, arithmetic assumptions, and component budgets appear in the full paper.

## Research contributions

- **Structure of a specified existing approximation.** Frequency compactification and exact interval sign conditions prove nonsingularity, positive denominator real parts, and half-plane preservation on a continuous parameter domain.
- **Complex residual-to-state bounds.** A convex Caputo inequality and one-sided Riccati dissipativity control the modulus of a complex error. The residual is computed independently of the reference trajectory.
- **Complete price intervals.** A positive-kernel characteristic-exponent representation transfers the state bound to prices, with Fourier discretization, finite-node errors, and the true infinite tail included in the budget.
- **A decision guarantee for a finite candidate set.** Strict objective intervals establish the stability of the stated roughness choice. The same prices provide quotation-band classifications and a spread-valuation error bound.
- **A broader error mechanism.** The companion report develops common-state joint error sets for the classical Heston Euler chain and extends the bias identity to admissible nonexact trial functions, with an explicit example.

The rational formula, two-end matching construction, convexity tools, and Fourier quadrature have established sources. The contribution concerns the model-specific conditions, their proofs, and the resulting effective guarantees. The manuscripts identify each attribution explicitly.

## Where the results apply

| Result | Domain of validity | Output |
| --- | --- | --- |
| All-frequency rational structure | α in [0.52, 0.60], ρ = -0.7445, zero Riccati mean reversion; all real frequencies and all positive times | Nonsingular matching, positive denominator real parts, and left-half-plane preservation |
| Complex state-error comparison | The stated regularity, independently bounded Caputo residual, and one-sided real-part conditions | A positive-kernel error bound; a uniform δ/σ bound when σ is positive |
| Complete model prices | The fixed nondecreasing forward variance curve, half-year maturity, twelve listed strikes, and the three specified candidates | Outward price intervals with all named error components |
| Finite-candidate stability | The same fixed-profile experiment and finite candidate set | Unique α = 0.52 for the model and the frozen rational procedure |
| Spread valuation | The 4400–4500 call spread in the normalized experiment | Absolute implementation error below 0.000634774793739 |
| Common-state error analysis | The classical Heston chain and admissible residual/trial-function assumptions in the companion report | Joint price-error sets and directional bounds |

Each row has its own hypotheses and proof. In particular, the α = 0.90 reference-price certificate uses an independent reference field; its inclusion in the candidate comparison does not extend the rational structural theorem beyond α = 0.60.

## Applications

**Pricing-library validation.** Compare a specified rational implementation with a model-price enclosure. The enclosure can be tested against a numerical pricing tolerance or combined with a signed portfolio exposure.

**Roughness-candidate selection.** Compare the certified model-objective gap with the allowed objective perturbation. A perturbation below the stated margin preserves the selected candidate in this finite set.

**Quotation consistency.** Use price intervals and bid/ask-derived normalized bands to classify whether a candidate satisfies the prescribed quote constraints. This provides a check independent of the optimizer's reported fitting error.

**Spread valuation.** Propagate the signed price intervals to a call spread and assess the result against a chosen tolerance. Cash-price errors are obtained by multiplying normalized errors by (DF).

These are uses of a numerical-reliability guarantee within the stated model setting. The market example uses publicly supplied implied-volatility observations to define a normalized experiment.

## Reproduce a check

From the repository root:

```sh
python -m venv .venv
# Activate the environment using the command appropriate to your platform.
python -m pip install -r code/requirements.txt
python code/run.py verify
```

The verification command checks file integrity, the recorded exact cover, finite-candidate arithmetic, and the financial application. The [execution guide](code/README.md) distinguishes these checks from replaying the expensive interval and residual calculations.

The companion report's classical witnesses have separate read-only checks:

```sh
python code/classical/verify_package.py
python code/classical/verify_input_bounds.py
python code/classical/verify_terminal.py
python code/classical/verify_field_receipt.py
```

Their model conditions and evidence mapping are given in [the classical supplement](docs/classical-evidence.md).

To rebuild the PDF presentation:

```sh
python -m pip install -r scripts/requirements.txt
npm install
python scripts/build_pdf.py
```

The PDFs use native vector mathematics, matching the A4 single-column style of the author's valuation manuscript.

## Explore the project

| Material | Purpose |
| --- | --- |
| [Rough Heston paper](manuscript/rough-heston.md) | Mathematical setting, structural theorem, proofs, price intervals, and the finite-candidate example |
| [Companion research report](manuscript/report.md) | Common-state error mechanisms and the connection to financial decisions |
| [PDF papers](paper/) | English reading copies in the supplied academic format |
| [Numerical tools](code/) | Portable source, frozen computational inputs, and recorded results |
| [Proof map](docs/proof-map.md) | Correspondence between results, mathematical obligations, and executable evidence |
| [References](manuscript/references.bib) | Verified bibliographic versions used in the manuscripts |
| [Presentation guide](manuscript/FORMAT.md) | Editable sources, author metadata, and PDF reproduction |

**Contact:** [10@alumni.duke.edu](mailto:10@alumni.duke.edu) · [theodore.oy2025@gmail.com](mailto:theodore.oy2025@gmail.com)
