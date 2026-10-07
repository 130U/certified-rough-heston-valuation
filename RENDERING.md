# Rendering the V5 editorial manuscripts

The canonical sources are `manuscript/merged-heston-en.md` and `manuscript/merged-heston-zh.md`. The builder preserves their scientific content, resolves linked contents and PDF bookmarks in multiple layout passes, and embeds formulas as native vector outlines. Layout checks and equation-transcription checks do not verify mathematical proofs.

## Typography

The typography follows the supplied *Attention Is All You Need* PDF: US Letter (612 × 792 pt), one column, a 396 pt text width and 108 pt side margins. The top and bottom text margins are 72 pt. The English body uses the original **Nimbus Roman No9 L** Type 1 family at **11 pt**, with 12.1 pt leading, 5.5 pt paragraph spacing and no first-line indent. Complete regular, italic, bold and bold-italic faces are embedded; no replacement Times font is used. The supplied reference's embedded font subsets are not reused.

The title uses 17.215 pt bold, bracketed by 4 pt and 1 pt horizontal rules. The author uses 11 pt; main headings use 12 pt bold and subordinate headings 11 pt bold. The abstract uses 10 pt with an additional 36 pt indent on each side. Captions and references use 10 pt; dense table cells use 9 pt. The dated title-block label identifies this **2026 editorial edition**, while the author's research, principal writing and GitHub-upload chronology is stated separately in Appendix H and `CHRONOLOGY.json`.

MathJax 3.2.2's TeX glyphs retain the Computer Modern style and are inserted as vector paths, normally at 11 pt, with proportionate sizing for long displays. Four long displays break at their existing clause separators while retaining the exact source expressions. Paragraphs containing inline vector formulas reserve a small internal allowance to prevent mixed-fragment justification overruns; ordinary prose uses the complete 396 pt column. Chinese prose uses a supplied CJK TrueType font; mathematical and Latin text retain the same styles. The reading route follows the abstract. The numbered, linked contents follow the main text and precede Appendix A. There are no forced page breaks or added padding to reach a page count: pagination follows the content and font metrics. Deterministic PDF metadata use the actual 2026-10-07 edition day, without a personal host clock or a retrospective research date.

## Dependencies and fonts

```text
python -m pip install reportlab Pillow pypdf pypdfium2
npm install --no-save mathjax-full@3.2.2
```

The full Nimbus faces, their AFM metrics and licences are included under `local-fonts/nimbus-no9l/`. They come from the [CTAN URW-base35 distribution](https://ctan.org/pkg/urw-base35); `qa/reference-font-provenance.json` records the downloaded distribution and each file's SHA256. Respect its included font licence and PDF-embedding exception.

Supply `cmtt10.ttf`, `DejaVuSerif.ttf` and `DejaVuSans.ttf` in `local-fonts/` from the [fixed Matplotlib v3.10.6 font directory](https://github.com/matplotlib/matplotlib/tree/v3.10.6/lib/matplotlib/mpl-data/fonts/ttf), respecting the corresponding [licences](https://github.com/matplotlib/matplotlib/tree/v3.10.6/lib/matplotlib/mpl-data/fonts). These serve monospace text and characters outside Nimbus's WinAnsi repertoire. Supply a CJK font when rendering Chinese. The released PDF hashes fix the delivered typography; different CJK fonts may change Chinese pagination.

```text
python scripts/build_pdf.py --document rough-heston --font-dir local-fonts
python scripts/build_pdf.py --document report --font-dir local-fonts --cjk-font CJK.ttf
python qa_pdf.py
```

## Budget figure and verification

```text
python audit-experiments/plot_budget_counts.py
python audit-experiments/check_figure.py
```

The budget figure uses unchanged exact thresholds from `audit-experiments/portfolio-budget-counts.json`. Its larger labels and print-sized presentation do not change the 504 thresholds, pass counts or 28 fixed directions.

The readable command index is [COMMANDS.md](COMMANDS.md). Scientific readers run from the separately downloaded, fixed V3 scientific ZIP. Editorial verification runs from the complete V5 source checkout and does not regenerate the scientific evidence.
