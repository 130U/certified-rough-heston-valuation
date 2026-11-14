"""Typeset the paper: convert the manuscript to LaTeX and compile it with Tectonic.

The manuscript carries its own section, statement, table and equation numbers. The converter keeps every
number as written, so the PDF, the online article and the manuscript agree number for number.
"""
from pathlib import Path
import argparse
import json
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
STATEMENTS = 'Theorem|Proposition|Lemma|Corollary|Assumption|Remark'
MATH = re.compile(r'\\\((.+?)\\\)|\\\[(.+?)\\\]', re.S)
SPECIAL = {'&': r'\&', '%': r'\%', '#': r'\#', '_': r'\_', '$': r'\$', '~': r'\textasciitilde{}', '^': r'\textasciicircum{}',
           '{': r'\{', '}': r'\}', '\\': r'\textbackslash{}', '<': r'\textless{}', '>': r'\textgreater{}', '|': r'\textbar{}',
           'α': r'\(\alpha\)', 'ε': r'\(\varepsilon\)', '≥': r'\(\ge\)', '×': r'\(\times\)'}

PREAMBLE = r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=1in]{geometry}
\usepackage{fontspec}
\usepackage{amsmath,amssymb}
\usepackage{microtype}
\usepackage{graphicx}
\usepackage{booktabs,array,tabularx,longtable,xltabular}
\usepackage{caption}
\usepackage{float}
\usepackage{enumitem}
\usepackage{setspace}
\usepackage{titlesec}
\usepackage{fancyhdr}
\usepackage[hyphens]{url}
\urlstyle{same}
\usepackage[colorlinks=true,linkcolor=black,citecolor=black,urlcolor=linkblue,pdfusetitle,bookmarksnumbered=true,hypertexnames=false]{hyperref}
\usepackage{xcolor}
\definecolor{linkblue}{rgb}{0.12,0.31,0.47}
\setstretch{1.12}
\setlength{\parskip}{0pt}
\setlength{\parindent}{1.4em}
\allowdisplaybreaks[1]
\emergencystretch=2em
\frenchspacing
\titleformat{\section}{\large\bfseries}{\thesection.}{0.5em}{}
\titleformat{\subsection}{\normalsize\bfseries}{\thesubsection.}{0.5em}{}
\titleformat{\subsubsection}[runin]{\normalsize\itshape}{}{0pt}{}[.]
\titlespacing*{\section}{0pt}{1.6\baselineskip}{0.6\baselineskip}
\titlespacing*{\subsection}{0pt}{1.1\baselineskip}{0.4\baselineskip}
\captionsetup{font=small,justification=justified,singlelinecheck=false,skip=6pt}
\pagestyle{fancy}\fancyhf{}\renewcommand{\headrulewidth}{0pt}\fancyfoot[C]{\small\thepage}
\newcommand{\statement}[3]{\par\addvspace{0.7\baselineskip}\noindent\textbf{#1}\if\relax\detokenize{#2}\relax\else\ (#2)\fi\textbf{.}\enspace{#3}\par\addvspace{0.7\baselineskip}}
\newcommand{\proofhead}[1]{\par\addvspace{0.3\baselineskip}\noindent\textit{#1.}\enspace}
\newcommand{\proofend}{\hfill\(\square\)\par\addvspace{0.6\baselineskip}}
\newcolumntype{L}{>{\raggedright\arraybackslash}X}
\newcommand{\code}[1]{\texttt{\small #1}}
'''


def escape(text):
    return ''.join(SPECIAL.get(ch, ch) for ch in text)


def inline(text):
    """Convert one run of manuscript text, keeping mathematics verbatim."""
    store = []

    def stash(match):
        store.append('\\(' + match.group(1).strip() + '\\)' if match.group(1) is not None else display(match.group(2)))
        return '%d' % (len(store) - 1)

    out = re.sub('(\\d+)', lambda m: store[int(m.group(1))], plain(MATH.sub(stash, text)))
    return re.sub(r'\n\s*\n', '\n', out).strip('\n')


def display(body):
    body = body.strip()
    tag = re.search(r'\\tag\{([^}]+)\}', body)
    if tag:
        body = (body[:tag.start()] + body[tag.end():]).strip()
        return '\n\\begin{equation*}\\tag{' + tag.group(1) + '}\n' + body + '\n\\end{equation*}\n'
    return '\n\\[\n' + body + '\n\\]\n'


def plain(text):
    """Text outside mathematics: code spans, links, emphasis and special characters."""
    out, cursor = [], 0
    token = re.compile(r'`([^`]+)`|\[([^\]]+)\]\(([^)]+)\)|\*\*(.+?)\*\*|\*(.+?)\*', re.S)
    for match in token.finditer(text):
        out.append(escape(text[cursor:match.start()]))
        code, label, url, bold, italic = match.groups()
        if code is not None:
            out.append('\\code{' + re.sub(r'(\\_|[-/.])', r'\1\\allowbreak{}', escape(code)) + '}')
        elif label is not None:
            out.append('\\href{' + url.replace('%', '\\%').replace('#', '\\#') + '}{' + plain(label) + '}')
        elif bold is not None:
            out.append('\\textbf{' + plain(bold) + '}')
        else:
            out.append('\\emph{' + plain(italic) + '}')
        cursor = match.end()
    out.append(escape(text[cursor:]))
    return ''.join(out)


def cells(line):
    """Cells of one table row; a bar inside mathematics does not separate cells."""
    line, parts, depth, current = line.strip().strip('|'), [], False, ''
    k = 0
    while k < len(line):
        if line.startswith('\\(', k):
            depth = True
        elif line.startswith('\\)', k):
            depth = False
        if line[k] == '|' and not depth and (k == 0 or line[k - 1] != '\\'):
            parts.append(current.strip())
            current = ''
        else:
            current += line[k]
        k += 1
    parts.append(current.strip())
    return parts


def visible(cell):
    """Approximate printed length of a table cell."""
    cell = re.sub(r'\]\([^)]*\)', '', cell)
    cell = re.sub(r'\\(?:operatorname|mathcal|mathbb|widehat|bar|tfrac|frac|text|rm)\b', '', cell)
    return len(re.sub(r'\\[a-zA-Z]+', 'x', re.sub(r'[{}`*\[\]]|\\[()]', '', cell)))


def table(caption, rows):
    header, align, body = cells(rows[0]), cells(rows[1]), [cells(r) for r in rows[2:]]
    right = [a.endswith(':') for a in align]
    count = len(right)
    natural = [max(visible(row[i]) for row in [header] + body) for i in range(count)]
    wide = sum(natural) + 2 * count > 88
    size = '\\footnotesize' if sum(natural) > 100 or count > 6 else '\\small'
    head = ' & '.join(inline(c) for c in header) + ' \\\\'
    lines = [' & '.join(inline(c) for c in row) + ' \\\\' for row in body]
    if not wide:
        spec = ''.join('r' if r else 'l' for r in right)
        return '\n'.join(['\\begin{table}[H]', '\\caption*{' + inline(caption) + '}', '\\centering' + size,
                          '\\begin{tabular}{@{}' + spec + '@{}}', '\\toprule', head, '\\midrule'] + lines
                         + ['\\bottomrule', '\\end{tabular}', '\\end{table}'])
    # Wide tables share the text width in proportion to their content, and every cell may wrap.
    words = [max(max((len(w) for w in re.sub(r'\]\([^)]*\)', '', row[i]).split()), default=1) for row in [header] + body) for i in range(count)]
    fixed = [natural[i] <= 9 for i in range(count)]
    need = [max(min(natural[i], 44), min(words[i], 16), 4) for i in range(count)]
    flexible = sum(1 for f in fixed if not f)
    total = sum(n for n, f in zip(need, fixed) if not f)
    spec = ''.join(('r' if r else 'l') if f else '>{\\hsize=%.3f\\hsize\\%s\\arraybackslash}X' % (flexible * n / total, 'raggedleft' if r else 'raggedright')
                   for n, f, r in zip(need, fixed, right))
    start = ['{' + size, '\\setlength{\\tabcolsep}{4pt}', '\\begin{xltabular}{\\textwidth}{@{}' + spec + '@{}}',
             '\\caption*{' + inline(caption) + '}\\\\', '\\toprule', head, '\\midrule', '\\endfirsthead', '\\toprule', head, '\\midrule', '\\endhead',
             '\\bottomrule', '\\endfoot']
    return '\n'.join(start + lines + ['\\end{xltabular}', '}'])


def convert(source, author):
    blocks = re.split(r'\n\s*\n', source.replace('\r\n', '\n').strip())
    title = blocks.pop(0)
    assert title.startswith('# ')
    title = title[2:].strip()
    out, front, in_proof, references, appendix = [], {}, False, False, False
    index = 0
    while index < len(blocks):
        block = blocks[index].strip('\n')
        index += 1
        if block == '## Abstract':
            front['abstract'] = inline(blocks[index])
            index += 1
            continue
        meta = re.match(r'\*\*(Keywords|JEL classification|MSC 2020):\*\*\s*(.*)', block, re.S)
        if meta:
            front[meta.group(1)] = inline(meta.group(2))
            continue
        heading = re.match(r'(#{2,4}) (.*)', block)
        if heading:
            level, text = len(heading.group(1)), heading.group(2).strip()
            if text == 'References':
                references = True
                out.append('\\section*{References}\\addcontentsline{toc}{section}{References}\n'
                           '\\begingroup\\small\\setlength{\\parindent}{0pt}\\setlength{\\parskip}{3pt}\\raggedright')
                continue
            numbered = re.match(r'(?:Appendix ([A-E])|((?:\d+|[A-E])(?:\.\d+)?))\. (.*)', text)
            if level == 4 or not numbered:
                out.append('\\subsubsection*{' + inline(text) + '}')
                continue
            letter, number, name = numbered.groups()
            if letter and not appendix:
                appendix = True
                out.append('\\appendix\n\\renewcommand{\\thesection}{Appendix \\Alph{section}}'
                           '\\renewcommand{\\thesubsection}{\\Alph{section}.\\arabic{subsection}}')
            if level == 2:
                counter = ord(letter) - ord('A') if letter else int(number) - 1
                out.append('\\setcounter{section}{%d}\\section{%s}' % (counter, inline(name)))
            else:
                out.append('\\setcounter{subsection}{%d}\\subsection{%s}' % (int(number.split('.')[1]) - 1, inline(name)))
            continue
        if references:
            out.append('\\hangindent=1.4em\\hangafter=1 ' + inline(block) + '\\par')
            continue
        figure = re.match(r'!\[(.*)\]\(\.\./(.+)\.png\)$', block, re.S)
        if figure:
            caption, path = figure.groups()
            width = '0.6' if 'joint-error-set' in path else '0.86' if 'pass-counts' in path else '0.76'
            out.append('\\begin{figure}[H]\\centering\n\\includegraphics[width=%s\\textwidth]{../%s.pdf}\n\\caption*{%s}\n\\end{figure}'
                       % (width, path, inline(re.sub(r'^(Figure \d+)\.', r'**\1.**', caption))))
            continue
        caption = re.match(r'\*\*(Table (?:[A-E]\.)?\d+)\. (.*)\*\*$', block, re.S)
        if caption and index < len(blocks) and blocks[index].lstrip().startswith('|'):
            out.append(table('**' + caption.group(1) + '.** ' + caption.group(2), blocks[index].strip().split('\n')))
            index += 1
            continue
        statement = re.match(r'\*\*((?:' + STATEMENTS + r') (?:[A-E]\.)?\d+(?:\.\d+)?)(?: \((.*?)\))?\.\*\*\s*(.*)', block, re.S)
        if statement:
            head, name, body = statement.groups()
            shape = '' if head.startswith(('Remark', 'Assumption')) else '\\itshape '
            out.append('\\statement{%s}{%s}{%s%s}' % (head, inline(name or ''), shape, inline(body)))
            continue
        proof = re.match(r'\*\*(Proof(?: of [^*]+?)?)\.\*\*\s*(.*)', block, re.S)
        if proof:
            block, in_proof = proof.group(2), True
        if block.lstrip().startswith('- '):
            items = re.split(r'\n(?=- )', block.strip())
            out.append('\\begin{itemize}[leftmargin=1.4em,itemsep=2pt,topsep=4pt]\n'
                       + '\n'.join('\\item ' + inline(i[2:]) for i in items) + '\n\\end{itemize}')
            continue
        ends = in_proof and re.search(r'\\\(\\square\\\)\s*$', block)
        if ends:
            block = block[:ends.start()].rstrip()
        text = inline(block)
        previous = blocks[index - 2].strip() if index >= 2 else ''
        if not proof and previous.startswith('\\[') and previous.endswith('\\]') and not text.startswith('\\begin{equation') \
                and (block[:1].islower() or not re.search(r'\.\s*(?:\\tag\{[^}]+\})?\s*\\\]$', previous)):
            text = '\\noindent ' + text
        if proof:
            text = '\\proofhead{' + inline(proof.group(1)) + '}' + text
        if ends:
            text, in_proof = text + '\\proofend', False
        out.append(text)
    assert not in_proof, 'unterminated proof'
    out.append('\\endgroup')
    contact = ' \\textperiodcentered\\ '.join('\\href{mailto:%s}{%s}' % (e, escape(e)) for e in author['emails'])
    head = [PREAMBLE, '\\hypersetup{pdfauthor={%s},pdftitle={%s}}' % (author['author'], title), '\\begin{document}',
            '\\thispagestyle{empty}', '\\begin{center}', '{\\LARGE\\bfseries ' + inline(title) + '\\par}', '\\vspace{1.6em}',
            '{\\large ' + author['author'] + '\\footnote{' + contact + '. Code, data and verification records: \\url{'
            + author['repository'] + '}.}\\par}', '\\vspace{0.6em}', '{\\normalsize ' + author['date'] + '\\par}', '\\end{center}',
            '\\vspace{1.2em}', '\\begin{center}\\textbf{Abstract}\\end{center}',
            '\\begin{quote}\\small\\setstretch{1.08}\\noindent ' + front['abstract'] + '\\end{quote}', '\\vspace{0.4em}',
            '\\begin{quote}\\small\\noindent\\textbf{Keywords:} ' + front['Keywords'] + '\\par\\smallskip\\noindent\\textbf{JEL classification:} '
            + front['JEL classification'] + '\\par\\smallskip\\noindent\\textbf{MSC 2020:} ' + front['MSC 2020'] + '\\end{quote}',
            '\\newpage', '\\setcounter{footnote}{0}']
    return '\n\n'.join(head + out + ['\\end{document}']) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--engine', default=shutil.which('tectonic') or 'tectonic', help='Path of the Tectonic executable')
    parser.add_argument('--tex-only', action='store_true', help='Write paper/paper.tex without compiling')
    args = parser.parse_args()
    source = (ROOT/'manuscript/merged-heston-en.md').read_text(encoding='utf-8')
    author = json.loads((ROOT/'manuscript/author.json').read_text(encoding='utf-8'))
    tex = convert(source, author)
    target = ROOT/'paper/paper.tex'
    target.write_text(tex, encoding='utf-8')
    if not args.tex_only:
        work = ROOT/'.cache/paper'
        work.mkdir(parents=True, exist_ok=True)
        subprocess.run([args.engine, '-X', 'compile', '--keep-logs', '--outdir', str(work), str(target)], check=True, cwd=ROOT/'paper')
        shutil.copyfile(work/'paper.pdf', ROOT/'paper/paper.pdf')
    print('PASS', target.relative_to(ROOT).as_posix(), len(tex), 'characters')


if __name__ == '__main__':
    main()
