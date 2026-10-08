# Typesetting

The online article uses native inline mathematics and transparent vector displays, with separate light and dark colours. This keeps the complete paper within GitHub's single-page mathematics limit. Formula content, order and equation numbers are preserved; the original TeX remains in the manuscript sources. The theme-specific display assets are in `assets/math/`.

The English and Chinese papers use A4 pages, a single column and 25 mm margins. The layout follows the supplied reference paper: regular-weight title, centred author and contact line, inset abstract, blue contents links, indented paragraphs and centred page numbers.

Latin text uses the complete CM-Super Type 1 fonts: SFRM1095 at 10.909 pt for the body and the corresponding optical sizes for the title, headings and abstract. Chinese text uses an embedded Song font; the Latin text and formulas retain the same design in both papers. Formulas are drawn as vector outlines in the Computer Modern style.

The editable sources are in `manuscript/`. The renderer uses Python, ReportLab, Pillow, Node.js and MathJax 3.2.2. Font licences accompany the redistributable font files.

Install the rendering dependencies from the archive root:

```text
python -m pip install reportlab pillow matplotlib
npm install --no-save mathjax-full@3.2.2
```

Build the English paper:

```text
python -B scripts/build_pdf.py --document rough-heston --font-dir local-fonts
```

For Chinese, supply a local font with the required Chinese glyphs:

```text
python -B scripts/build_pdf.py --document report --font-dir local-fonts --cjk-font CJK.ttf
```

Run the two commands in sequence. The PDFs are written to `paper/`. Formula preparation uses a shared cache, so parallel builds are unnecessary.
