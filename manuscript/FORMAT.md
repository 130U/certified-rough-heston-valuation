# Manuscript and presentation formats

The project provides two complete English manuscripts: `rough-heston.md` is the focused rough Heston paper; `report.md` is the companion report on Heston pricing-error mechanisms. Their corresponding PDFs are in `paper/`.

The PDFs follow the user-supplied valuation manuscript: A4, one column, Computer Modern body type, centered title and author block, numbered displays, and continuous page numbering. Formula glyphs are embedded as vector paths. The author name, university line, postal address, and email addresses reproduce the supplied template.

The canonical editable sources are `report-source.md` and `rough-heston-source.md`. The files `report.md` and `rough-heston.md` contain the same prose and mathematics in GitHub's native formula syntax. The corresponding standalone `.tex` files provide an alternative editable typesetting source.

`scripts/build_pdf.py` protects every formula before interpreting prose, sends TeX expressions to MathJax 3.2.2, and draws their SVG outlines as native PDF forms. It records the source and output hashes, formula count, equation tags, and display placements. Rebuilding requires the dependencies listed in `scripts/requirements.txt` and `package.json`.

```sh
python -m pip install -r scripts/requirements.txt
npm install
python scripts/build_pdf.py --document all
python scripts/build_github_manuscripts.py
python scripts/build_tex.py
```

The author details are editable in `author.json`. Presentation changes do not modify frozen numerical inputs or certificates.

The certificate files under `code/` retain their exact bytes in Git, including existing line endings, because their identities are recorded in `code/MANIFEST.json`. An escaped TeX space at the end of a source line is mathematical typesetting syntax and is retained.
