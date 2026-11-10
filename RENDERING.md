# Sources and typesetting

The paper is maintained in [manuscript/merged-heston-en.md](manuscript/merged-heston-en.md). This editable source generates the [online article](ARTICLE.md) and the [PDF](paper/paper.pdf).

The online article uses native inline mathematics and transparent vector displays with separate light and dark colours. `scripts/build_article.py` generates the article and the display assets under `assets/math/`, then records their identities and formula counts in [validation/article-check.json](validation/article-check.json). TeX expressions remain editable in the manuscript source.

The PDF uses A4 pages, a single column and 25 mm margins, with a regular-weight title, centred author and contact line, inset abstract, linked contents, indented paragraphs and centred page numbers. Latin text uses CM-Super Type 1 fonts, including SFRM1095 at 10.909 pt for the body. Formulas are drawn as vector outlines in the Computer Modern style.

The rendering tools use Python, ReportLab, Pillow, Node.js and MathJax 3.2.2. Font licences accompany the redistributable font files. Install the dependencies from the project root:

```text
python -m pip install reportlab pillow matplotlib
npm install --no-save mathjax-full@3.2.2
```

Build the online article:

```text
python -B scripts/build_article.py
```

Build the PDF:

```text
python -B scripts/build_pdf.py --document rough-heston --font-dir local-fonts
```

The publication output is [paper/paper.pdf](paper/paper.pdf).

After building, inspect the pages, equation labels, table placement and links, and compare the article against its source. [validation/pdf-check.json](validation/pdf-check.json) records the PDF identity and the actual scope of page-layout inspection. Refresh the presentation receipts and publication manifest whenever their inputs change. Typesetting and presentation checks are separate from the scientific calculations in [COMMANDS.md](COMMANDS.md).
