# Sources and typesetting

The paper is maintained in [English](manuscript/merged-heston-en.md) and [Chinese](manuscript/merged-heston-zh.md). These editable sources generate the [online article](ARTICLE.md), [English PDF](paper/paper.pdf) and [Chinese PDF](paper/paper-zh.pdf).

The online article uses native inline mathematics and transparent vector displays with separate light and dark colours. `scripts/build_article.py` generates the article and the display assets under `assets/math/`, then records their identities and formula counts in [validation/article-check.json](validation/article-check.json). TeX expressions remain editable in the manuscript source.

Both PDFs use A4 pages, a single column and 25 mm margins, with a regular-weight title, centred author and contact line, inset abstract, linked contents, indented paragraphs and centred page numbers. Latin text uses CM-Super Type 1 fonts, including SFRM1095 at 10.909 pt for the body. Chinese text uses an embedded CJK font supplied at build time. Formulas are drawn as vector outlines in the Computer Modern style.

The rendering tools use Python, ReportLab, Pillow, Node.js and MathJax 3.2.2. Font licences accompany the redistributable font files. Install the dependencies from the project root:

```text
python -m pip install reportlab pillow matplotlib
npm install --no-save mathjax-full@3.2.2
```

Build the online article:

```text
python -B scripts/build_article.py
```

Build the English PDF:

```text
python -B scripts/build_pdf.py --document rough-heston --font-dir local-fonts
```

For the Chinese PDF, place a font with the required Chinese glyphs at `CJK.ttf`, or substitute its local path:

```text
python -B scripts/build_pdf.py --document report --font-dir local-fonts --cjk-font CJK.ttf
```

Run the PDF builds in sequence because formula preparation uses a shared cache. The publication outputs are [paper/paper.pdf](paper/paper.pdf) and [paper/paper-zh.pdf](paper/paper-zh.pdf).

After building, inspect the pages, equation labels, table placement and links, and compare the article against its source. [validation/pdf-check.json](validation/pdf-check.json) records the PDF identities and the actual scope of page-layout inspection. Refresh the presentation receipts and publication manifest whenever their inputs change. Typesetting and presentation checks are separate from the scientific calculations in [COMMANDS.md](COMMANDS.md).
