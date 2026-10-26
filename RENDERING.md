# Sources and typesetting

The 26 October 2026 revision is maintained in [the English source](manuscript/merged-heston-en.md) and [the Chinese source](manuscript/merged-heston-zh.md). The online article and PDFs are generated from these files. The classical Heston extensions are separate [English](supplement/classical-heston-en.md) and [Chinese](supplement/classical-heston-zh.md) supplements; their original F–G equation labels are retained for traceability.

The [online article](ARTICLE.md) uses native inline mathematics and transparent vector displays with separate light and dark colours. The reproducible entry point is `scripts/build_article.py`; the display assets are written under `assets/math/`. TeX expressions remain editable in the manuscript source. Regenerate the article after changing that source so that its prose, equations and navigation agree.

The English and Chinese PDFs use A4 pages, a single column and 25 mm margins, with a regular-weight title, centred author and contact line, inset abstract, blue contents links, indented paragraphs and centred page numbers. Latin text uses the CM-Super Type 1 fonts: SFRM1095 at 10.909 pt for the body and the corresponding optical sizes for headings and the abstract. Chinese text uses an embedded CJK font supplied at build time. Formulas are drawn as vector outlines in the Computer Modern style.

The renderer continues to use Python, ReportLab, Pillow, Node.js and MathJax 3.2.2. Font licences accompany the redistributable font files. Typesetting is a presentation step; it does not execute the scientific checks in [COMMANDS.md](COMMANDS.md).

Install the rendering dependencies from the archive root:

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

Run the PDF builds in sequence because formula preparation uses a shared cache. The renderer writes `paper/Theodore-Ouyang-Certified-Joint-Heston-EN.pdf` and `paper/Theodore-Ouyang-Certified-Joint-Heston-ZH.pdf`, and automatically synchronizes [paper/paper.pdf](paper/paper.pdf) and [paper/paper-zh.pdf](paper/paper-zh.pdf) as byte-identical stable entry points. Update the publication manifest after building.

Before publication, inspect the generated pages, check equation and section links, and compare the online article against its source. A successful renderer exit alone does not establish that the page layout or mathematical content is correct.
