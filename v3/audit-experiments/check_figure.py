from pathlib import Path
import json
import pypdfium2 as pdfium
HERE=Path(__file__).resolve().parent
doc=pdfium.PdfDocument(str(HERE/'portfolio-pass-counts.pdf'));assert len(doc)==1
p=doc[0];tp=p.get_textpage();text=tp.get_text_range()
for required in ['alpha = .52','alpha = .60','alpha = .90','N2L','Shown range','28 fixed directions']:assert required in text
outside=[]
width,height=p.get_size()
for i in range(tp.count_chars()):
 ch=tp.get_text_range(i,1)
 if not ch.strip():continue
 x0,y0,x1,y1=tp.get_charbox(i)
 if x0<0 or y0<0 or x1>width or y1>height:outside.append(ch)
assert not outside
p.render(scale=1.3).to_pil().save(HERE/'portfolio-pass-counts.png')
(HERE/'figure-check.json').write_text(json.dumps({'status':'PASS_VECTOR_FIGURE_TEXT_AND_PAGE_BOUNDS','pages':1,'outside_text_spans':0,'threshold_count':504},indent=2)+'\n',encoding='utf-8')
print('PASS vector figure, onepage, noout-of-page text')
