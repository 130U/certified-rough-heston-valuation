"""Check every page and mathematical occurrence; render a visual review set."""
from pathlib import Path
import argparse,hashlib,json,re
from PIL import Image,ImageDraw
import pypdfium2 as pdfium
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parent

def main():
    p=argparse.ArgumentParser();p.add_argument('--draft',action='store_true');a=p.parse_args()
    out=ROOT/'qa/rendered';out.mkdir(parents=True,exist_ok=True);report={}
    for name,lang in [('rough-heston','EN'),('report','ZH')]:
        path=ROOT/f'paper/Theodore-Ouyang-Merged-Heston-{lang}.pdf'
        if a.draft and not path.exists():continue
        source_path=ROOT/'manuscript'/('merged-heston-zh.md' if lang=='ZH' else 'merged-heston-en.md')
        source=source_path.read_text(encoding='utf-8')
        if not a.draft:assert 'EDITORIAL PLACEHOLDER' not in source
        log=json.loads((ROOT/f'qa/{name}-pdf-build.json').read_text(encoding='utf-8'))
        if not a.draft:assert hashlib.sha256(source_path.read_bytes()).hexdigest()==log['source_sha256']
        assert log['math_source_occurrences']==len(log['math_occurrences'])
        assert log['math_rendering']['status']=='PASS'
        assert not [d for d in log['displays'] if d['font_pt']<8.5]
        doc=pdfium.PdfDocument(str(path));reader=PdfReader(path)
        assert len(doc)==len(reader.pages)>0
        texts=[];outside=[];corepages=[];selected={0,1,len(doc)-1};contents_pages=[];chronology_pages=[];symbol_pages=[];caption_pages=[];body_fonts={}
        for i,page in enumerate(doc):
            assert list(page.get_size())==[612.0,792.0],(lang,i+1,'not US Letter')
            textpage=page.get_textpage();txt=textpage.get_text_range();texts.append(txt)
            assert len(txt.strip())>30,(lang,i+1,'empty page')
            assert '\ufffd' not in txt and '\x00' not in txt,(lang,i+1,'text marker')
            if 'finite-history pricing envelope' in txt or '有限历史定价' in txt:corepages.append(i+1);selected.add(i)
            if re.search(r'(?m)^(Contents|目录)\s*$',txt):contents_pages.append(i+1);selected.add(i)
            if '2023' in txt and '2024' in txt and '2026' in txt:chronology_pages.append(i+1);selected.add(i)
            if '(F.26)' in txt or '(F.27)' in txt:symbol_pages.append(i+1);selected.add(i)
            if re.search(r'Table\s+(?:\d+|[A-H]\.\d+)|表\s*(?:\d+|[A-H]\.\d+)',txt):caption_pages.append(i+1);selected.add(i)
            if any(x in txt for x in ['0.233318843','candidate','Nearby','邻近','0.115215934','0.252393939','certified correlation','相关系数']):selected.add(i)
            for k in range(textpage.count_chars()):
                ch=textpage.get_text_range(k,1)
                if not ch.strip():continue
                x0,y0,x1,y1=textpage.get_charbox(k)
                if x0<104 or x1>509 or y0<36 or y1>726:outside.append({'page':i+1,'box':[round(x0,2),round(y0,2),round(x1,2),round(y1,2)]})
            textpage.close();page.close()
        contacts=[]
        for start in range(0,len(doc),16):
            sheet=Image.new('RGB',(1000,1480),'#e9e9e9');draw=ImageDraw.Draw(sheet)
            for slot,index in enumerate(range(start,min(start+16,len(doc)))):
                page=doc[index];pic=page.render(scale=.38).to_pil().convert('RGB');pic.thumbnail((235,340))
                x=(slot%4)*250+7;y=(slot//4)*370+23;sheet.paste(pic,(x,y));draw.text((x,y-18),f'{lang} p.{index+1}',fill='black');page.close()
            filename=f'{lang}-contact-{start//16+1}.png';sheet.save(out/filename);contacts.append(filename)
        for i in sorted(selected):
            page=doc[i];page.render(scale=1.5).to_pil().save(out/f'{lang}-page-{i+1}.png');page.close()
        font_names=set()
        for page in reader.pages:
            for font in page['/Resources'].get('/Font',{}).values():
                font=font.get_object();font_names.add(str(font['/BaseFont']))
                if str(font['/BaseFont']).startswith('/NimbusRomNo9L-'):
                    assert '/FontFile' in font['/FontDescriptor'].get_object(),(lang,'Nimbus font not embedded')
        assert '/NimbusRomNo9L-Regu' in font_names and '/NimbusRomNo9L-Medi' in font_names
        assert log['typography']['body_font_pt']==11 and not log['typography']['substitution']
        assert reader.metadata.get('/CreationDate')=='D:20261007' and reader.metadata.get('/ModDate')=='D:20261007'
        assert not outside,(lang,'prose outside the column',outside[:5])
        joined='\n'.join(texts)
        source_tags=re.findall(r'\\tag\{([^{}]+)\}',source)
        assert len(source_tags)==169 and len(set(source_tags))==169
        assert all('('+tag+')' in joined for tag in source_tags),(lang,'missing visible equation number')
        assert not any(bad in joined for bad in ['fullremainders','allactual','allsame-reference','and28'])
        assert symbol_pages and caption_pages and chronology_pages
        report[lang]={'pages':len(doc),'core_theorem_pages':corepages,'formula_occurrences':len(log['math_occurrences']),
          'contents_pages':contents_pages,'chronology_pages':chronology_pages,
          'notation_review_pages':symbol_pages,'table_caption_pages':caption_pages,'embedded_fonts':sorted(font_names),'typography':log['typography'],
          'pdf_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'source_sha256':log['source_sha256'],
          'every_page_read':True,'out_of_frame_prose_glyphs':outside,'contact_sheets':contacts,'selected_pages':[i+1 for i in sorted(selected)]}
        doc.close()
    (ROOT/'qa/manuscript-qa.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({lang:{k:v for k,v in d.items() if k in ['pages','core_theorem_pages','formula_occurrences','out_of_frame_prose_glyphs']} for lang,d in report.items()}))

if __name__=='__main__':main()
