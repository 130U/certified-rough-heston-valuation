"""Inspect complete source/formula coverage and render all PDF pages for review."""
from pathlib import Path
import hashlib,json,math,re
from PIL import Image,ImageDraw
import pypdfium2 as pdfium
from pypdf import PdfReader
import pdfplumber
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'qa'/'rendered';OUT.mkdir(parents=True,exist_ok=True)
result={}
for name,lang in [('report','ZH'),('rough-heston','EN')]:
    path=ROOT/'paper'/f'Theodore-Ouyang-Merged-Heston-{lang}.pdf'
    log=json.loads((ROOT/'qa'/f'{name}-pdf-build.json').read_text(encoding='utf-8'))
    doc=pdfium.PdfDocument(str(path));reader=PdfReader(path)
    assert len(doc)==len(reader.pages)>0
    assert log['math_source_occurrences']==len(log['math_occurrences'])
    assert log['math_rendering']['status']=='PASS'
    assert not [x for x in log['displays'] if x['font_pt']<8.5]
    texts=[p.extract_text() or '' for p in reader.pages]
    assert all(len(t.strip())>30 for t in texts),'empty page'
    assert all('\ufffd' not in t and '\ufffc' not in t and '\x00' not in t for t in texts),'unrendered prose marker'
    selected={0,len(doc)-1}
    for i,t in enumerate(texts):
        if any(s in t for s in ['Actual Pricing Outputs','Financial Comparison','Original-Chain Probability','实际定价输出','金融','经典原链概率包含','omitted finite frequencies','second maturity','0.233318843','0.115215934','省略有限频率','第二期限','v2.zip']):selected.add(i)
    for x in log['displays']:
        if any(s in x['tags'] for s in ['J1','J4','J10','J11','Q2','Q9','Q18','H10','N1','N2','N5','N6','N8','FQ1','FQ4','FQ6','FQ8','TR1']):selected.add(x['page']-1)
    contacts=[]
    for start in range(0,len(doc),16):
        sheet=Image.new('RGB',(1000,1480),'#e9e9e9');draw=ImageDraw.Draw(sheet)
        for slot,index in enumerate(range(start,min(start+16,len(doc)))):
            page=doc[index];pic=page.render(scale=.38).to_pil().convert('RGB')
            pic.thumbnail((235,340));x=(slot%4)*250+7;y=(slot//4)*370+23
            sheet.paste(pic,(x,y));draw.text((x,y-18),f'{lang} p.{index+1}',fill='black');page.close()
        target=OUT/f'{lang}-contact-{start//16+1}.png';sheet.save(target);contacts.append(target.name)
    for i in sorted(selected):
        page=doc[i];page.render(scale=1.5).to_pil().save(OUT/f'{lang}-page-{i+1}.png');page.close()
    outside=[]
    with pdfplumber.open(path) as pdf:
        for i,page in enumerate(pdf.pages):
            for ch in page.chars:
                # Formula paths are checked by the builder; this checks prose glyph placement.
                if ch['x0'] < 78 or ch['x1'] > 526 or ch['top'] < 70 or ch['bottom'] > 780:
                    outside.append({'page':i+1,'text':ch['text'],'box':[round(ch[k],2) for k in ['x0','top','x1','bottom']]})
    result[lang]={'pages':len(doc),'pdf_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'source_sha256':log['source_sha256'],'formula_occurrences':len(log['math_occurrences']),
        'display_formulas':len(log['displays']),'tables':len(log['tables']),
        'minimum_display_font_pt':min(x['font_pt'] for x in log['displays']),
        'contact_sheets':contacts,'selected_pages':[i+1 for i in sorted(selected)],
        'prose_bounds_alerts':outside,'status':'PASS_SOURCE_FORMULAS_AND_NONEMPTY_PAGES'}
    doc.close()
(ROOT/'qa'/'pdf-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:{x:v for x,v in row.items() if x not in ['prose_bounds_alerts','contact_sheets','selected_pages']} for k,row in result.items()},indent=2))
print('Prose-bound alerts:',{k:len(v['prose_bounds_alerts']) for k,v in result.items()})
