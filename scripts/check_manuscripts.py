"""Check the released English sources, mathematical presentation, and links."""
from pathlib import Path
import re, json, hashlib

ROOT=Path(__file__).resolve().parents[1]
PAT=re.compile(r'\\\[.*?\\\]|\\\(.*?\\\)|(?<!\\)\$\$.*?(?<!\\)\$\$|(?<!\\)\$(?!\$)[^\n$]*?(?<!\\)\$',re.S)

def main():
    results=[]
    for name,count,tags in [('report',615,70),('rough-heston',510,86)]:
        path=ROOT/'manuscript'/f'{name}-source.md';source=path.read_text(encoding='utf-8')
        public=(ROOT/'manuscript'/f'{name}.md').read_text(encoding='utf-8')
        spans=PAT.findall(source);assert len(spans)==count,(name,len(spans))
        eqs=re.findall(r'\\tag\{([^{}]+)\}',source)
        assert len(set(eqs))==tags and len(eqs)==tags
        assert re.findall(r'\\tag\{([^{}]+)\}',public)==eqs
        assert not re.search(r'[\u4e00-\u9fff]',source+public),name
        assert not re.search(r'(?:C:\\Users\\|C:/Users/|OneDrive|ChatGPT/Finance)',source+public),name
        linked=[]
        for url in re.findall(r'\[[^\]]+\]\(([^)]+)\)',source):
            if url.startswith(('https://','http://','mailto:','#')):continue
            dest=(path.parent/url.split('#')[0]).resolve();assert dest.exists(),(name,url)
            linked.append(url)
        # Numerical table entries are retained through the presentation build.
        source_prose=PAT.sub('MATH',source)
        public_prose=re.sub(r'```math\n.*?\n```','MATH',public,flags=re.S)
        public_prose=re.sub(r'\$`.*?`\$','MATH',public_prose,flags=re.S)
        source_rows=[x for x in source_prose.splitlines() if x.strip().startswith('|')]
        public_rows=[x for x in public_prose.splitlines() if x.strip().startswith('|')]
        source_numbers=[re.findall(r'(?<![A-Za-z])[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?',x) for x in source_rows]
        public_numbers=[re.findall(r'(?<![A-Za-z])[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?',x) for x in public_rows]
        assert source_numbers==public_numbers,(name,'table values')
        results.append({'document':name,'math_occurrences':count,'unique_equation_tags':tags,'local_links_checked':len(linked),'table_rows_checked':len(source_rows),'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'public_sha256':hashlib.sha256(public.encode()).hexdigest()})
    bib=(ROOT/'manuscript/references.bib').read_text(encoding='utf-8')
    years=list(map(int,re.findall(r'\byear\s*=\s*\{(\d{4})\}',bib)))
    assert years and max(years)<=2024
    result={'status':'PASS_ENGLISH_MANUSCRIPT_PRESENTATION','documents':results,'maximum_bibliographic_year':max(years),'scope':'Source identity, presentation, numerical-table transcription and local links; mathematical proofs are contained in the manuscripts.'}
    out=ROOT/'manuscript/content-verification.json';out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
