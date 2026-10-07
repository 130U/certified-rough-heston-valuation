# Certified Joint Pricing Errors in Rough Heston

**Theodore Ouyang**

[theodore.oy2025@gmail.com](mailto:theodore.oy2025@gmail.com) · [10@alumni.duke.edu](mailto:10@alumni.duke.edu)

The research was carried out in 2023–2024, with the main articles written in 2024. Some final work was completed in 2026, when the paper and code were uploaded to GitHub.

The paper connects continuous Riccati residuals to complete pricing-error bounds and retains shared Fourier errors across strikes. It covers actual pricing outputs, portfolios and finite candidate comparisons; the classical extensions retain their separately stated scope.

[English paper](https://github.com/130U/certified-rough-heston-valuation/releases/download/paper/Theodore-Ouyang-Certified-Joint-Heston-EN.pdf) · [中文论文](https://github.com/130U/certified-rough-heston-valuation/releases/download/paper/Theodore-Ouyang-Certified-Joint-Heston-ZH.pdf) · [Source archive](https://github.com/130U/certified-rough-heston-valuation/releases/download/paper/Theodore-Ouyang-Heston-Source.zip) · [Complete evidence](https://github.com/130U/certified-rough-heston-valuation/releases/download/paper/Theodore-Ouyang-Heston-Evidence.zip) · [Checksums](https://github.com/130U/certified-rough-heston-valuation/releases/download/paper/SHA256SUMS.txt)

Download the complete evidence archive, verify its checksum and extract it into a separate directory. From its root:

```text
python -m pip install -r requirements.txt
python reproduce.py --full
```

The driver verifies scientific identities, reads the saved banks and reconstructs downstream prices, objectives and decisions in a separate working copy. `--full` also recomputes the original structural-sign cover. Appendix E and [COMMANDS.md](COMMANDS.md) specify each command's scope.

The source archive omits 27 large numerical banks supplied in the complete evidence archive. `python -B verify_source.py` checks source identities. [RENDERING.md](RENDERING.md) documents typesetting.
