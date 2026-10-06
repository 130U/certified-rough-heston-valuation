"""Create editable English LaTeX sources while retaining every TeX formula."""
from pathlib import Path
import re,json,hashlib

ROOT=Path(__file__).resolve().parents[1]
MATH=re.compile(r'\\\[.*?\\\]|\\\(.*?\\\)|(?<!\\)\$\$.*?(?<!\\)\$\$|(?<!\\)\$(?!\$)[^\n$]*?(?<!\\)\$',re.S)

def render(name):
    path=ROOT/'manuscript'/f'{name}-source.md'
    source=path.read_text(encoding='utf-8');math={}
    def protect(m):
        key='MATHPLACEHOLDER'+str(len(math))+'Z';math[key]=m.group();return key
    protected=MATH.sub(protect,source)
    def escape(s):
        chars={'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}
        return ''.join(chars.get(c,c) for c in s)
    def fmt(s):
        out=[]
        for part in re.split(r'(\[[^\]]+\]\([^)]+\))',s):
            link=re.fullmatch(r'\[([^\]]+)\]\(([^)]+)\)',part)
            if link:
                label,url=link.groups();out.append(r'\href{'+url.replace('#',r'\#').replace('%',r'\%')+'}{'+escape(label)+'}')
            else:
                q=escape(part);q=re.sub(r'\*\*(.*?)\*\*',r'\\textbf{\1}',q);q=re.sub(r'`([^`]+)`',r'\\texttt{\1}',q);out.append(q)
        return ''.join(out)
    meta=json.loads((ROOT/'manuscript/author.json').read_text(encoding='utf-8'))
    head=[r'\title{'+fmt(meta['titles'][name])+r'\\[5pt]\large '+fmt(meta['subtitles'][name])+'}',
          r'\author{'+fmt(meta['author']+', '+meta['school'])+r'\\\small '+fmt(meta['address'])+r'\\\texttt{'+escape(meta['emails'][0])+r'}\\\texttt{'+escape(meta['emails'][1])+'}}',r'\date{}',r'\maketitle']
    lines=protected.splitlines();out=head;i=0
    while i<len(lines):
        line=lines[i]
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].startswith('|'):
                cells=[x.strip() for x in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?',x) for x in cells):rows.append(cells)
                i+=1
            n=len(rows[0]);assert all(len(x)==n for x in rows)
            out += [r'\begingroup\scriptsize\setlength{\tabcolsep}{3pt}',r'\begin{longtable}{'+('L{'+f'{.89/n:.6f}'+r'\textwidth}')*n+'}']
            for j,row in enumerate(rows):
                out.append(' & '.join(fmt(x) for x in row)+r'\\')
                if j==0:out.append(r'\hline')
            out.append(r'\end{longtable}\endgroup');continue
        if line.startswith('# '):pass
        elif line.startswith('## '):out.append(r'\section*{'+fmt(line[3:])+'}')
        elif line.startswith('### '):out.append(r'\subsection*{'+fmt(line[4:])+'}')
        elif line.startswith('#### '):out.append(r'\subsubsection*{'+fmt(line[5:])+'}')
        elif line.startswith('- '):out.append(r'\noindent\textbullet\ '+fmt(line[2:])+r'\par')
        else:out.append(fmt(line))
        i+=1
    body='\n'.join(out)
    for key,value in math.items():body=body.replace(key,value)
    assert 'MATHPLACEHOLDER' not in body
    tex=r'''\documentclass[a4paper,11pt]{article}
\usepackage{fontspec,amsmath,amssymb,mathtools,geometry,longtable,array,hyperref}
\setmainfont{Latin Modern Roman}
\setmonofont{Latin Modern Mono}
\geometry{left=28.5mm,right=25.7mm,top=38mm,bottom=33mm}
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
\hypersetup{colorlinks=true,linkcolor=black,urlcolor=blue}
\setlength{\emergencystretch}{4em}
\allowdisplaybreaks
\begin{document}
'''+body+'\n'+r'\end{document}'+'\n'
    target=ROOT/'manuscript'/f'{name}-source.tex';target.write_text(tex,encoding='utf-8',newline='\n')
    return {'file':target.relative_to(ROOT).as_posix(),'source_sha256':hashlib.sha256(source.encode()).hexdigest(),'tex_sha256':hashlib.sha256(tex.encode()).hexdigest(),'math_spans':len(math),'all_math_retained':all(value in tex for value in math.values())}

if __name__=='__main__':
    result={'status':'SOURCE_TRANSCRIPTION_CHECKED','documents':[render(n) for n in ['report','rough-heston']]}
    (ROOT/'qa/tex-transcription.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
