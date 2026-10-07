# Inputs and attribution

The input experiment uses twelve option rows from the public 18 June 2021 SPX sample in the author repository accompanying Siow Woon Jeng and Adem Kiliçman, *SPX Calibration of Option Approximations under Rough Heston Model*, Mathematics 9(21), 2675 (2021), DOI [10.3390/math9212675](https://doi.org/10.3390/math9212675).

Source identity: [author repository at commit 860049da2b7486fe8aa509061eff23cc28c2ef89](https://github.com/WoonJeng/Dataset-for-SPX-Calibration-of-Option-Approximations-under-Rough-Heston-model/tree/860049da2b7486fe8aa509061eff23cc28c2ef89). Readers can obtain the original inputs directly from that pinned repository:

- [README](https://github.com/WoonJeng/Dataset-for-SPX-Calibration-of-Option-Approximations-under-Rough-Heston-model/blob/860049da2b7486fe8aa509061eff23cc28c2ef89/README.md)
- [spx_decomp.csv](https://github.com/WoonJeng/Dataset-for-SPX-Calibration-of-Option-Approximations-under-Rough-Heston-model/blob/860049da2b7486fe8aa509061eff23cc28c2ef89/spx_decomp.csv)
- [spx_pade_data.csv](https://github.com/WoonJeng/Dataset-for-SPX-Calibration-of-Option-Approximations-under-Rough-Heston-model/blob/860049da2b7486fe8aa509061eff23cc28c2ef89/spx_pade_data.csv)

Choose the repository's download action for those exact files. They are external source inputs and are not included in this release. The repository README identifies market bid/ask/mid IV and author model columns separately. This release contains only the twelve factual quote inputs used in the mathematical experiment and the authors' own rational conversion enclosures; unused author-model diagnostic columns have been omitted. It does not redistribute the external CSV collection, MATLAB source, author pricing code, or paper PDFs.

`frozen/normalized-quote-bands.json` specifies the conversion: exact decimal bid/ask IV; exact mathematical time T=1/2; D=1; F=4221.86; normalized European calls c=C/(DF). The fitting target is the arithmetic mean of the two Black–Scholes prices. It is not the Black–Scholes price of the reported midpoint IV. The stored source-file hashes and commit identify the inputs; the public subset has a separate release hash.

The experiment fixes rho=-.7445, nu=.2897, Riccati lambda_R=0, and the entire curve

xi(t)=.0721+(.0262-.0721) E_.5286(-.5037 t^.5286).

It compares alpha=.52,.6,.9. Candidate changes do not change the curve's .5286 exponent or .5037 coefficient. All NPZ arrays and interval results are computations of this research, interpreted as exact binary dyadics or exact rational endpoint strings.

Raw source licenses remain the responsibility of their source owners. Attribution to the paper does not grant a license to its separate repository. The release's code license applies to the included original programs, not to external repositories or data products.
