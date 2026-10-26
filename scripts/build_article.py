"""Build the GitHub article directly from the current English manuscript.

Inline formulas use GitHub mathematics; displays use transparent MathJax paths
with light and dark variants. The editable TeX is retained in image alt text.
"""
from pathlib import Path
import argparse, hashlib, html, json, math, re, subprocess
from math_inputs import canonical, strip_tags

ROOT=Path(__file__).resolve().parents[1]
PAT=re.compile(r'\\\[(.*?)\\\]|\\\((.*?)\\\)|(?<!\\)\$\$(.*?)(?<!\\)\$\$|(?<!\\)\$(?!\$)([^\n$]*?)(?<!\\)\$',re.S)

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--node',default='node')
    args=p.parse_args()
    path=ROOT/'manuscript/merged-heston-en.md'
    source=path.read_text(encoding='utf-8')
    source=re.sub(r'(!\[[^\]]*\]\()\.\./',r'\1',source)
    cache=ROOT/'.cache/article-math';cache.mkdir(parents=True,exist_ok=True)
    assets=ROOT/'assets/math';assets.mkdir(parents=True,exist_ok=True)
    rows=[];spans=[]
    for m in PAT.finditer(source):
        tex=next(x for x in m.groups() if x is not None).strip()
        display=m[1] is not None or m[3] is not None
        clean,tags=strip_tags(tex) if display else (tex,[])
        render_tex=clean
        if display and tags:
            render_tex=r'\begin{gathered}'+clean+r'\end{gathered}\qquad\text{('+', '.join(tags)+')}'
        ident,_,_=canonical(render_tex,display)
        rows.append({'tex':render_tex,'display':display})
        spans.append({'start':m.start(),'end':m.end(),'tex':tex,'display':display,'id':ident,'tags':tags})
    ip=cache/'inputs.json';ip.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    subprocess.run([args.node,str(ROOT/'scripts/render_math.cjs'),str(ip),str(cache)],check=True,stdout=subprocess.DEVNULL)
    meta={x['id']:x for x in json.loads((cache/'metadata.json').read_text(encoding='utf-8'))}
    render=json.loads((cache/'render-summary.json').read_text(encoding='utf-8'))
    assert render['status']=='PASS' and not render['errors']
    rendered=[];cursor=0;ledger=[]
    for row in spans:
        rendered.append(source[cursor:row['start']]);cursor=row['end']
        if not row['display']:
            tex=re.sub(r'\s+',' ',row['tex']).strip().replace('<',r'\lt ').replace('>',r'\gt ')
            rendered.append('$`'+tex+'`$')
            continue
        mm=meta[row['id']]
        raw=(cache/(row['id']+'.svg')).read_text(encoding='utf-8')
        width=math.ceil(mm['widthUnits']*18/1000)
        height=math.ceil(mm['heightUnits']*18/1000)
        raw=re.sub(r'width="[^"]*"',f'width="{width}px"',raw,count=1)
        raw=re.sub(r'height="[^"]*"',f'height="{height}px"',raw,count=1)
        names={}
        for theme,color in [('light','#1f2328'),('dark','#f0f6fc')]:
            name='revision-'+row['id']+'-'+theme+'.svg'
            (assets/name).write_text(raw.replace('#000000',color),encoding='utf-8')
            names[theme]='assets/math/'+name
        alt=html.escape(re.sub(r'\s+',' ',row['tex']).strip(),quote=True)
        rendered.append('<p align="center">\n<picture>\n'
            f'  <source media="(prefers-color-scheme: dark)" srcset="{names["dark"]}">\n'
            f'  <source media="(prefers-color-scheme: light)" srcset="{names["light"]}">\n'
            f'  <img src="{names["light"]}" width="{min(width,900)}" alt="{alt}">\n'
            '</picture>\n</p>')
        ledger.append({**row,'paths':names,'width_px':width,'height_px':height})
    rendered.append(source[cursor:])
    used={Path(q).name for r in ledger for q in r['paths'].values()}
    for stale in assets.glob('revision-*.svg'):
        if stale.name not in used:
            assert stale.resolve().parent==assets.resolve()
            stale.unlink()
    article=''.join(rendered)
    headings=re.findall(r'^## (.+)$',article,re.M)
    def anchor(s):
        return re.sub(r'[^a-z0-9 _-]','',s.lower()).replace(' ','-')
    contents='\n'.join('- ['+h+'](#'+anchor(h)+')' for h in headings if h!='Abstract')
    title,rest=article.split('\n',1)
    article=title+'\n\n**Theodore Ouyang**\n\nRevision: 26 October 2026.\n\n[English PDF](paper/paper.pdf) · [Chinese PDF](paper/paper-zh.pdf) · [Evidence](EVIDENCE.md) · [Revision record](REVISION.md)\n\n## Contents\n\n'+contents+'\n'+rest
    assert len(re.findall(r'<picture>',article))==len(ledger)
    (ROOT/'ARTICLE.md').write_text(article,encoding='utf-8')
    qa=ROOT/'qa';qa.mkdir(exist_ok=True)
    receipt={'status':'PASS','source':'manuscript/merged-heston-en.md','source_sha256':digest(path),'article_sha256':digest(ROOT/'ARTICLE.md'),'formula_count':len(spans),'inline_count':len(spans)-len(ledger),'display_count':len(ledger),'equation_tags':[t for r in ledger for t in r['tags']],'mathjax':render['mathjax'],'mathjax_errors':render['errors'],'displays':ledger}
    (qa/'article-build.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:receipt[k] for k in ['status','formula_count','inline_count','display_count','mathjax_errors']}))

if __name__=='__main__':main()
