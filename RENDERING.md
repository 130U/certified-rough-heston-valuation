# Rendering the editorial manuscripts

The canonical editable sources are `manuscript/merged-heston-en.md` and `manuscript/merged-heston-zh.md`. The PDF builder adds a visible linked contents page with page numbers resolved in multiple layout passes. It renders formulas as MathJax SVG outlines and inserts them as native PDF paths. This rendering procedure checks transcription and layout; it does not verify mathematical proofs.

Install the rendering dependencies in a separate environment:

```text
python -m pip install reportlab Pillow pypdf pypdfium2
npm install --no-save mathjax-full@3.2.2
```

Supply `cmr10.ttf`, `cmb10.ttf`, `cmtt10.ttf`, `DejaVuSerif.ttf`, `DejaVuSerif-Italic.ttf` and `DejaVuSans.ttf` from the [fixed Matplotlib v3.10.6 font directory](https://github.com/matplotlib/matplotlib/tree/v3.10.6/lib/matplotlib/mpl-data/fonts/ttf), respecting the accompanying font licences. Supply a CJK TrueType font for Chinese text. Font selection can affect pagination; the released PDFs and their checksums identify the delivered layout.

```text
python scripts/build_pdf.py --document rough-heston --font-dir fonts --node node
python scripts/build_pdf.py --document report --font-dir fonts --cjk-font fonts/CJK.ttf --node node
python qa_pdf.py
```

The budget figure uses the unchanged exact thresholds in `audit-experiments/portfolio-budget-counts.json`. Its editorial version increases text size and display size; it does not change pass counts, thresholds or the 28 fixed portfolio directions. To regenerate the figure before building the manuscripts:

```text
python audit-experiments/plot_budget_counts.py
python audit-experiments/check_figure.py
```

The scientific readers and generators remain separate. Use the fixed V3 scientific ZIP and the commands in the repository README for the stated numerical verification scope.
