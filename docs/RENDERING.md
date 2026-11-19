# Sources and typesetting

The paper is maintained in [manuscript/merged-heston-en.md](../manuscript/merged-heston-en.md). This editable source generates the [online article](../ARTICLE.md), the [LaTeX file](../paper/paper.tex) and the [PDF](../paper/paper.pdf). Section, statement, table and equation numbers are written in the manuscript and carried unchanged into all three, so the article and the PDF agree number for number.

The online article uses native inline mathematics and transparent vector displays with separate light and dark colours. `scripts/build_article.py` generates the article and the display assets under `assets/math/`, then records their identities and formula counts in [validation/article-check.json](../validation/article-check.json).

The PDF is typeset by LaTeX. `scripts/build_pdf.py` converts the manuscript to `paper/paper.tex` and compiles it with Tectonic: A4 pages, one-inch margins, an 11 pt Latin Modern text face, a title page with abstract, keywords and classification codes, numbered sections, and tables set with rules. The figures are drawn by `scripts/build_figures.py` from the saved banks, as vector PDF for the paper and PNG for the article.

The tools use Python with NumPy and Matplotlib, Node.js with MathJax 3.2.2, and Tectonic 0.17. Install the dependencies from the project root:

```text
python -m pip install -r requirements.txt matplotlib
npm install --no-save mathjax-full@3.2.2
```

Draw the figures, then build the article and the PDF:

```text
python -B scripts/build_figures.py
python -B scripts/build_article.py
python -B scripts/build_pdf.py
```

After building, inspect the pages, equation numbers, table placement and links, and compare the article against its source. [validation/pdf-check.json](../validation/pdf-check.json) records the PDF identity and the scope of the page-layout inspection. Refresh the presentation receipts and the publication manifest whenever their inputs change. Typesetting and presentation checks are separate from the scientific calculations in [COMMANDS.md](../COMMANDS.md).
