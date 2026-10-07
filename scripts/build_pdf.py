"""Typeset the complete English manuscripts in the supplied academic style.

Formulas are rendered by MathJax as SVG glyph outlines and embedded as native
PDF paths. No formula is rasterized. Markdown remains the editable source.
"""
from pathlib import Path
import argparse, re, json, hashlib, html, subprocess, os, sys
from PIL import Image
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Flowable, Table, TableStyle, Preformatted, KeepTogether
from reportlab.platypus import Image as PlotImage
from reportlab.platypus.tableofcontents import TableOfContents
# ReportLab's CJK breaker calls ord() on empty inline-image fragments.
# An object-replacement character preserves the image callback and its width.
_BaseParagraph = Paragraph
class Paragraph(_BaseParagraph):
    def breakLinesCJK(self, *args, **kwargs):
        for f in self.frags:
            if getattr(f, 'text', None) == '' and hasattr(f, 'cbDefn'):
                f.text = '\ufffc'
        return super().breakLinesCJK(*args, **kwargs)

from vector_math import MathCanvas
from math_inputs import canonical

ROOT=Path(__file__).resolve().parents[1]
PAT=re.compile(r'\\\[(.*?)\\\]|\\\((.*?)\\\)|(?<!\\)\$\$(.*?)(?<!\\)\$\$|(?<!\\)\$(?!\$)([^\n$]*?)(?<!\\)\$',re.S)
WIDTH=396; MARGIN=108; PAGE_W,PAGE_H=letter
FONT=11.0; LEADING=12.1
TOP=72; BOTTOM=72

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--document',choices=['report','rough-heston','all'],default='rough-heston')
    parser.add_argument('--font-dir',type=Path)
    parser.add_argument('--node',default='node')
    parser.add_argument('--cjk-font',type=Path,help='A locally supplied CJK font for the Chinese manuscript')
    parser.add_argument('--output-dir',type=Path,default=ROOT/'paper')
    args=parser.parse_args()
    if args.font_dir is None:
        import matplotlib
        args.font_dir=Path(matplotlib.get_data_path())/'fonts/ttf'
    fonts=args.font_dir
    nimbus=fonts/'nimbus-no9l'
    for alias,file in [('TimesR','utmr8a'),('TimesB','utmb8a'),('TimesI','utmri8a'),('TimesBI','utmbi8a')]:
        face=pdfmetrics.EmbeddedType1Face(str(nimbus/(file+'.afm')),str(nimbus/(file+'.pfb')))
        pdfmetrics.registerTypeFace(face)
        pdfmetrics.registerFont(pdfmetrics.Font(alias,face.name,'WinAnsiEncoding'))
    pdfmetrics.registerFont(TTFont('Mono',str(fonts/'cmtt10.ttf')))
    # Accented names and Greek letters in prose use a font with Unicode coverage.
    if args.document!='rough-heston' and args.cjk_font is None:
        raise ValueError('Supply --cjk-font for the Chinese manuscript')
    pdfmetrics.registerFont(TTFont('Accent',str(args.cjk_font)) if args.document!='rough-heston' else TTFont('Accent',str(fonts/'DejaVuSerif.ttf')))
    pdfmetrics.registerFont(TTFont('UnicodeFallback',str(fonts/'DejaVuSans.ttf')))
    pdfmetrics.registerFontFamily('TimesR',normal='TimesR',bold='TimesB',italic='TimesI',boldItalic='TimesBI')
    pdfmetrics.registerFontFamily('Mono',normal='Mono',bold='Mono',italic='Mono',boldItalic='Mono')
    def sty(name,**kw):
        base=dict(fontName='TimesR',fontSize=FONT,leading=LEADING,wordWrap=('CJK' if args.document=='report' else None),textColor=colors.black,firstLineIndent=0,alignment=TA_JUSTIFY,allowWidows=0,allowOrphans=0,autoLeading='max',spaceAfter=5.5)
        base.update(kw);return ParagraphStyle(name,**base)
    styles={
      'body':sty('body'),
      'h1':sty('h1',fontName='TimesB',fontSize=12,leading=14,firstLineIndent=0,spaceBefore=12,spaceAfter=6,alignment=TA_LEFT,keepWithNext=True),
      'h2':sty('h2',fontName='TimesB',fontSize=11,leading=12.1,firstLineIndent=0,spaceBefore=10,spaceAfter=5,alignment=TA_LEFT,keepWithNext=True),
      'h3':sty('h3',fontName='TimesB',fontSize=11,leading=12.1,firstLineIndent=0,spaceBefore=8,spaceAfter=4,alignment=TA_LEFT,keepWithNext=True),
      'title':sty('title',fontName='TimesB',fontSize=17.215,leading=20,firstLineIndent=0,spaceAfter=10,alignment=TA_CENTER),
      'subtitle':sty('subtitle',fontSize=9.963,leading=12,firstLineIndent=0,spaceAfter=5,alignment=TA_CENTER),
      'author':sty('author',fontSize=11,leading=12.1,firstLineIndent=0,spaceAfter=1,alignment=TA_CENTER),
      'meta':sty('meta',fontSize=9.963,leading=12,firstLineIndent=0,spaceAfter=1,alignment=TA_CENTER),
      'abstract':sty('abstract',fontSize=10,leading=11.4,firstLineIndent=0,leftIndent=36,rightIndent=36,spaceAfter=5.5),
      'keywords':sty('keywords',fontSize=9.5,leading=11.4,firstLineIndent=0,leftIndent=36,rightIndent=36,alignment=TA_LEFT,spaceAfter=5.5),
      'table':sty('table',fontSize=9,leading=10.2,firstLineIndent=0,alignment=TA_LEFT,spaceAfter=0,embeddedHyphenation=1),
      'tablehead':sty('tablehead',fontName='TimesB',fontSize=9,leading=10.2,firstLineIndent=0,alignment=TA_LEFT,spaceAfter=0,embeddedHyphenation=1),
      'caption':sty('caption',fontSize=10,leading=11.4,firstLineIndent=0,alignment=TA_LEFT,spaceBefore=6,spaceAfter=5,keepWithNext=True),
      'reference':sty('reference',fontSize=10,leading=11.4,alignment=TA_LEFT,leftIndent=23,firstLineIndent=-23,spaceAfter=5),
      'code':sty('code',fontName='Mono',fontSize=8.4,leading=11,firstLineIndent=0,alignment=TA_LEFT,spaceAfter=5),
      'list':sty('list',leftIndent=14,rightIndent=18,firstLineIndent=-14,spaceAfter=5),
    }
    names=['report','rough-heston'] if args.document=='all' else [args.document]
    meta=json.loads((ROOT/'manuscript/author.json').read_text(encoding='utf-8'))
    inputs=[]; documents={};maths={}
    for name in names:
        path=ROOT/'manuscript'/('merged-heston-zh.md' if name=='report' else 'merged-heston-en.md')
        source_identity=digest(path)
        src=path.read_text(encoding='utf-8')
        spans=[]
        def protect(m):
            tex=next(x for x in m.groups() if x is not None)
            display=m.group(1) is not None or m.group(3) is not None
            _,_,tags=canonical(tex,display)
            # Line breaks at existing clause separators preserve every symbol
            # while keeping long displays readable in the reference's narrow column.
            if display and tags in [['2.5'],['F.20'],['F.25'],['G.13']]:
                from math_inputs import strip_tags
                clean,_=strip_tags(tex)
                clean=clean.replace(r'\qquad',r'\\')
                if tags==['2.5']:clean=clean.replace('\\quad\nK_', '\\\\\nK_')
                tex=r'\begin{gathered}'+clean+r'\end{gathered}\tag{'+tags[0]+'}'
            # Print the long exact interval as its two equivalent inequalities.
            # The editable source retains the original interval expression.
            if display and tags==['H7']:
                fractions=re.findall(r'\\frac\{([^{}]+)\}\s*\{([^{}]+)\}',tex)
                assert len(fractions)==2
                lo,hi=[r'\frac{'+a+'}{'+b+'}' for a,b in fractions]
                tex=r'\begin{gathered}'+lo+r"\le\mathcal B'(0),\\ \mathcal B'(0)\le"+hi+r'.\end{gathered}\tag{H7}'
            ident,_,tags=canonical(tex,display)
            key=f'MX{len(maths):06d}Z';row=dict(id=ident,tex=tex,display=display,tags=tags)
            maths[key]=row;inputs.append(row);spans.append(m.group())
            return key
        protected=PAT.sub(protect,src)
        documents[name]=(path,src,protected,spans,source_identity)
    cache=ROOT/'.cache/math';cache.mkdir(parents=True,exist_ok=True)
    ip=cache/'inputs.json';ip.write_text(json.dumps(inputs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    subprocess.run([args.node,str(ROOT/'scripts/render_math.cjs'),str(ip),str(cache)],check=True,stdout=subprocess.DEVNULL)
    mathmeta={x['id']:x for x in json.loads((cache/'metadata.json').read_text(encoding='utf-8'))}
    for ident in mathmeta:
        Image.new('RGBA',(1,1),(0,0,0,0)).save(cache/(ident+'.png'))
    MathCanvas.math_meta=mathmeta;MathCanvas.math_dir=cache
    summary=json.loads((cache/'render-summary.json').read_text(encoding='utf-8'))
    assert summary['status']=='PASS' and not summary['errors']
    args.output_dir.mkdir(parents=True,exist_ok=True)
    reports=[]
    for name,(path,src,protected,spans,source_identity) in documents.items():
        assert digest(path)==source_identity,'The source changed during formula preparation.'
        log={'document':name,'source_sha256':digest(path),'math_occurrences':[], 'displays':[], 'headings':[], 'contents':[], 'tables':[], 'paragraphs':[], 'math_rendering':{'status':summary['status'],'mathjax':summary['mathjax'],'errors':[]},'presentation_equivalences':{'H7':'The exact interval is printed as the same lower and upper inequalities on two lines.'} if name=='report' else {}}
        log['typography']={'paper':'US Letter','page_pt':[PAGE_W,PAGE_H],'column_width_pt':WIDTH,'side_margin_pt':MARGIN,'top_margin_pt':TOP,'bottom_margin_pt':BOTTOM,'body_font':'NimbusRomNo9L-Regu','body_font_pt':FONT,'body_leading_pt':LEADING,'math_style':'MathJax TeX / Computer Modern style, native vector outlines','substitution':False,'explicit_page_breaks':False}
        log['presentation_equivalences'].update({t:'Line breaks at existing clause separators; unchanged mathematical expressions in the canonical source.' for t in ['2.5','F.20','F.25','G.13']})
        def supported(font_name,cp):
            f=pdfmetrics.getFont(font_name)
            if hasattr(f.face,'charToGlyph'):return bool(f.face.charToGlyph.get(cp,0))
            try:code=chr(cp).encode('cp1252')[0]
            except UnicodeEncodeError:return False
            return f.encoding.vector[code] in f.face.glyphWidths
        def esc(text):
            text=text.replace('\u2011','-')
            pieces=[]
            for c in text:
                if ord(c)<128 or supported('TimesR',ord(c)):pieces.append(html.escape(c));continue
                chosen='Accent' if supported('Accent',ord(c)) else 'UnicodeFallback'
                assert supported(chosen,ord(c)),f'Unsupported prose character U+{ord(c):04X}'
                pieces.append(f'<font name="{chosen}">{html.escape(c)}</font>')
            return ''.join(pieces)
        def markup(text,fs=FONT,avail=WIDTH):
            text=re.sub(r'\*\*(.*?)\*\*',r'BOLDOPENPLACEHOLDER\1BOLDCLOSEPLACEHOLDER',text)
            text=re.sub(r'`([^`]+)`',r'MONOOPENPLACEHOLDER\1MONOCLOSEPLACEHOLDER',text)
            pieces=re.split(r'(MX\d{6}Z)',text);out=[]
            for piece in pieces:
                if piece in maths:
                    row=maths[piece];assert not row['display']
                    m=mathmeta[row['id']];scale=min(fs,avail*1000/max(m['widthUnits'],1))
                    w=m['widthUnits']*scale/1000;h=m['heightUnits']*scale/1000;depth=m['depthUnits']*scale/1000
                    out.append(f'<img src="{cache/(row["id"]+".png")}" width="{w:.6f}" height="{h:.6f}" valign="{-depth:.6f}"/>')
                    log['math_occurrences'].append(row['id'])
                else:
                    links={}
                    def protect_link(m):
                        key='LINKPLACEHOLDER'+str(len(links))+'Z'
                        label,url=m.groups()
                        if url.startswith(('https://','http://','mailto:')):
                            links[key]='<link href="'+html.escape(url,quote=True)+'" color="#263A50">'+esc(label)+'</link>'
                        else:
                            links[key]=esc(label)
                        return key
                    piece=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',protect_link,piece)
                    q=esc(piece)
                    q=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',q)
                    q=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<i>\1</i>',q)
                    q=re.sub(r'`([^`]+)`',r'<font name="Mono">\1</font>',q)
                    for key,value in links.items():q=q.replace(key,value)
                    q=q.replace('BOLDOPENPLACEHOLDER','<b>').replace('BOLDCLOSEPLACEHOLDER','</b>').replace('MONOOPENPLACEHOLDER','<font name="Mono">').replace('MONOCLOSEPLACEHOLDER','</font>')
                    out.append(q)
            return ''.join(out)
        class Display(Flowable):
            def __init__(self,key):
                super().__init__();self.row=maths[key];self.m=mathmeta[self.row['id']];self.spaceBefore=8;self.spaceAfter=8
                log['math_occurrences'].append(self.row['id'])
            def wrap(self,availW,availH):
                room=availW-(42 if self.row['tags'] else 0)
                self.fs=min(FONT,room*1000/max(self.m['widthUnits'],1))
                self.w=self.m['widthUnits']*self.fs/1000;self.h=self.m['heightUnits']*self.fs/1000
                self.width=availW;self.height=self.h+3;return self.width,self.height
            def draw(self):
                room=self.width-(42 if self.row['tags'] else 0)
                self.canv.math(self.row['id'],(room-self.w)/2,1.5,self.w,self.h)
                for tag in self.row['tags']:
                    self.canv.setFont('TimesR',10.2);self.canv.drawRightString(self.width,1.5+(self.h-10.2)/2,'('+tag+')')
                log['displays'].append({'id':self.row['id'],'tags':self.row['tags'],'font_pt':round(self.fs,3),'page':self.canv.getPageNumber(),'width_pt':round(self.w,3),'height_pt':round(self.h,3)})
        class Manuscript(BaseDocTemplate):
            def __init__(self,*a,**kw):
                super().__init__(*a,**kw)
                frame=Frame(MARGIN,BOTTOM,WIDTH,PAGE_H-BOTTOM-TOP,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
                self.addPageTemplates(PageTemplate(id='academic',frames=[frame],onPage=self.decorate))
            def decorate(self,c,doc):
                c.saveState();c.setFont('TimesR',10);c.drawCentredString(MARGIN+WIDTH/2,40,str(doc.page));c.restoreState()
            def beforeDocument(self):
                # multiBuild repeats drawing to resolve the contents page.
                # Retain diagnostics from the final pass only.
                log['displays']=[]
                log['contents']=[]
            def afterFlowable(self,f):
                if getattr(f,'heading_key',None):
                    self.canv.bookmarkPage(f.heading_key);self.canv.addOutlineEntry(f.getPlainText(),f.heading_key,level=0,closed=False)
                    self.notify('TOCEntry',(0,f.getPlainText(),self.page,f.heading_key))
                    log['contents'].append({'text':f.getPlainText(),'page':self.page,'key':f.heading_key})
        class TitleRule(Flowable):
            def __init__(self,before=False):
                super().__init__();self.width=WIDTH;self.height=5;self.before=before;self.spaceAfter=10 if before else 9;self.spaceBefore=0 if before else 3
            def draw(self):
                self.canv.setLineWidth(4.0 if self.before else 1.0);self.canv.line(0,2,self.width,2)
        story=[TitleRule(True),Paragraph(esc(meta['titles'][name]),styles['title']),Paragraph(esc(meta['subtitles'][name]),styles['subtitle']),TitleRule(),Paragraph(esc(meta['author']),styles['author'])]
        for email in meta.get('emails',[]):
            story.append(Paragraph('<font name="Mono">'+esc(email)+'</font>',styles['author']))
        if meta.get('date'):story.append(Paragraph(esc(meta['date']),styles['meta']))
        story += [Spacer(1,10),Paragraph(esc('摘要') if name=='report' else '<b>Abstract</b>',sty('abstract-title',fontName='TimesB',fontSize=12,leading=14,firstLineIndent=0,alignment=TA_CENTER,spaceAfter=5,keepWithNext=True))]
        lines=protected.splitlines();i=0;in_abstract=False;cover=True;in_refs=False
        toc=TableOfContents()
        toc.levelStyles=[sty('contents-entry',fontName=('Accent' if name=='report' else 'TimesR'),fontSize=10,leading=11.4,firstLineIndent=0,leftIndent=0,rightIndent=0,alignment=TA_LEFT,spaceBefore=3,spaceAfter=0)]
        toc.dotsMinLevel=0
        def add_contents():
            story.append(Paragraph(esc('目录' if name=='report' else 'Contents'),styles['h1']))
            story.append(Paragraph(esc('主文与附录的阅读导航；页码对应本版。' if name=='report' else 'Navigation to the main text and integrated appendices; page numbers refer to this edition.'),styles['table']))
            story.append(Spacer(1,5))
            story.append(toc)
        # ReportLab's mixed text/inline-image justification can overrun the
        # measured line width. Reserve a small internal allowance only for
        # paragraphs containing vector formulas; the page column is unchanged.
        math_body=ParagraphStyle('body-with-vector-math',parent=styles['body'],rightIndent=18)
        def add_paragraph(buf,style_name):
            ps=math_body if style_name=='body' and 'MX' in buf else styles[style_name]
            if name=='rough-heston' and buf.startswith('The exact rational ') and 'coefficient enclosure' in buf:
                ps=ParagraphStyle('terminal-witness-margin',parent=math_body,rightIndent=25)
            if name=='rough-heston' and buf.startswith('**Proof.** Convolving the constant derivative'):
                ps=ParagraphStyle('analytical-curve-proof-margin',parent=math_body,rightIndent=32)
            story.append(Paragraph(markup(buf,ps.fontSize,WIDTH-ps.rightIndent),ps))
            log['paragraphs'].append(buf)
        def add_prose(text,style_name='body'):
            bits=re.split(r'(MX\d{6}Z)',text);buf=''
            for bit in bits:
                if bit in maths and maths[bit]['display']:
                    if buf.strip():add_paragraph(buf,style_name);buf=''
                    story.append(Display(bit))
                else:buf+=bit
            if buf.strip():add_paragraph(buf,style_name)
        while i<len(lines):
            line=lines[i].strip()
            if not line:i+=1;continue
            fig=re.fullmatch(r'!\[([^\]]+)\]\(([^)]+)\)',line)
            if fig:
                figure_path=(ROOT/fig[2]).resolve()
                assert figure_path.is_relative_to(ROOT.resolve()) and figure_path.is_file()
                with Image.open(figure_path) as pic:w,h=pic.size
                scale=WIDTH/w
                fig_caption=ParagraphStyle('figure-caption',parent=styles['caption'],keepWithNext=False)
                story.extend([Spacer(1,6),KeepTogether([PlotImage(str(figure_path),width=w*scale,height=h*scale),Paragraph(markup(fig[1],fig_caption.fontSize),fig_caption)]),Spacer(1,6)])
                i+=1;continue
            if line.startswith('# '):i+=1;continue
            if line in ['## Abstract','## 摘要']:in_abstract=True;i+=1;continue
            if line.startswith(('**Keywords:','**关键词')):
                add_prose(line,'keywords');cover=False;in_abstract=False;i+=1;continue
            if re.match(r'^\*\*(?:Table\s+[0-9A-Z]|表\s*[0-9A-Z])',line):
                add_prose(line,'caption');i+=1;continue
            if line.startswith('#'):
                if cover:cover=False;in_abstract=False
                level=len(line)-len(line.lstrip('#'));label=line[level:].strip()
                if level==2 and (label.startswith('Appendix A.') or label.startswith('附录 A.')):add_contents()
                in_refs=label in ['References','参考文献']
                style_name='h1' if level==2 else 'h2' if level==3 else 'h3'
                p=Paragraph(markup(label,styles[style_name].fontSize),styles[style_name])
                if level==2:p.heading_key='heading-'+str(len(log['headings']))
                story.append(p);log['headings'].append({'level':level,'text':label});i+=1;continue
            if line.startswith('|'):
                rows=[]
                while i<len(lines) and lines[i].strip().startswith('|'):
                    cells=[x.strip() for x in lines[i].strip().strip('|').split('|')]
                    if not all(re.fullmatch(r':?-+:?',x) for x in cells):rows.append(cells)
                    i+=1
                n=len(rows[0]);assert all(len(row)==n for row in rows),(name,rows)
                weights=[]
                for j in range(n):
                    lengths=[len(re.sub(r'MX\d{6}Z','xxxxxxxxxxx',row[j])) for row in rows]
                    weights.append(max(6,min(42,max(lengths))))
                widths=[WIDTH*x/sum(weights) for x in weights]
                # The configuration IDs and short headers should not break
                # inside words merely to fit a mechanically weighted column.
                if name=='rough-heston' and n==8 and rows[0][0]=='ID':
                    widths=[25,24,93,58,54,50,43,49]
                elif n==5 and rows[0][0]=='ID':
                    remaining=WIDTH-27
                    old_remaining=sum(widths[1:])
                    widths=[27]+[w*remaining/old_remaining for w in widths[1:]]
                code_columns=set()
                if n==5 and rows[0][0]=='ID' and any('`' in row[2] for row in rows[1:]):code_columns={2}
                if n==4 and any('`' in row[1] and '`' in row[2] for row in rows[1:]):code_columns={1,2}
                if code_columns:
                    fixed={j:8+max(pdfmetrics.stringWidth(token,'Mono',styles['table'].fontSize) for row in rows[1:] for token in re.findall(r'`([^`]+)`',row[j])) for j in code_columns}
                    remaining=WIDTH-sum(fixed.values());old_remaining=sum(w for j,w in enumerate(widths) if j not in code_columns)
                    widths=[fixed[j] if j in fixed else w*remaining/old_remaining for j,w in enumerate(widths)]
                # Keep the second-maturity certification words intact in the
                # four narrow decision columns, without changing their text.
                if name=='rough-heston' and n==7 and rows[0][0].startswith('Candidate') and all('Joint:' in cell for cell in rows[0][3:]):
                    widths=[52,83,106,50,50,50,50];widths=[w*WIDTH/sum(widths) for w in widths]
                # Keep numeric row keys, especially four-digit strikes, intact.
                if all(re.fullmatch(r'[-+]?\d+(?:\.\d+)?', row[0]) for row in rows[1:]):
                    key_width=max(44,8+max(pdfmetrics.stringWidth(row[0],'TimesR',styles['table'].fontSize) for row in rows[1:]))
                    if widths[0]<key_width:
                        remaining=WIDTH-key_width
                        old_remaining=sum(widths[1:])
                        widths=[key_width]+[w*remaining/old_remaining for w in widths[1:]]
                # Protect full decimal tokens and short bank IDs. Intervals may
                # wrap after a comma, but their endpoint digits never split.
                minima=[0.0]*n
                for j in range(n):
                    numbers=[token for row in rows[1:] for token in re.findall(r'(?<!\w)[+-]?\d+(?:\.\d+)?(?:e[-+]?\d+)?',row[j])]
                    if numbers:minima[j]=14+max(pdfmetrics.stringWidth(token,'TimesR',styles['table'].fontSize) for token in numbers)
                if all(re.fullmatch(r'[A-Z][A-Z0-9]{0,3}',row[0]) for row in rows[1:]):
                    minima[0]=max(minima[0],30,10+pdfmetrics.stringWidth(rows[0][0],'TimesB',styles['tablehead'].fontSize),10+max(pdfmetrics.stringWidth(row[0],'TimesR',styles['table'].fontSize) for row in rows[1:]))
                locked={j:widths[j] for j in code_columns};original=widths[:]
                for _ in range(n+1):
                    active=[j for j in range(n) if j not in locked]
                    if not active:break
                    remaining=WIDTH-sum(locked.values());weight=sum(original[j] for j in active)
                    candidate={j:original[j]*remaining/weight for j in active}
                    deficient=[j for j in active if candidate[j]<minima[j]]
                    if not deficient:
                        widths=[locked[j] if j in locked else candidate[j] for j in range(n)];break
                    for j in deficient:locked[j]=minima[j]
                else:raise ValueError('Table column constraints failed')
                assert sum(widths)<=WIDTH+.01 and all(widths[j]>=minima[j]-.01 for j in range(n))
                data=[]
                for ri,row in enumerate(rows):
                    style=styles['tablehead'] if ri==0 else styles['table']
                    rendered=[]
                    for j,cell in enumerate(row):
                        cell_style=ParagraphStyle('literal-script-token',parent=style,splitLongWords=False) if j in code_columns else style
                        printable=cell
                        if j not in code_columns:
                            parts=re.split(r'(`[^`]+`|\[[^\]]+\]\([^)]+\))',cell)
                            printable=''.join(part if index%2 else re.sub(r'/(?=[A-Za-z])','/ ',part) for index,part in enumerate(parts))
                        content=markup(printable,style.fontSize,widths[j]-8)
                        if ri==0 and cell.startswith('N_t '):
                            content='<i>N</i><sub>t</sub> '+markup(cell[4:],style.fontSize,widths[j]-8)
                        rendered.append(Paragraph(content,cell_style))
                    data.append(rendered)
                tab=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT',splitByRow=(0 if len(rows)<=5 else 1))
                tab.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,0),.5,colors.black),('LINEBELOW',(0,-1),(-1,-1),.4,colors.black),('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]))
                story += [Spacer(1,5),tab,Spacer(1,8)];log['tables'].append({'rows':len(rows),'columns':n,'cells':rows});continue
            if line.startswith('```'):
                block=[];i+=1
                while i<len(lines) and not lines[i].strip().startswith('```'):block.append(lines[i]);i+=1
                i+=1
                for code in block:
                    width=pdfmetrics.stringWidth(code,'Mono',styles['code'].fontSize)
                    if width>WIDTH:
                        raise ValueError('Long literal command must be linked from COMMANDS.md instead of split inside a word: '+code)
                    story.append(Preformatted(code,styles['code']))
                continue
            if re.fullmatch(r'[-*_]{3,}',line):i+=1;continue
            if line.startswith('- '):add_prose('• '+line[2:],'list');i+=1;continue
            paragraph=[line];i+=1
            while i<len(lines) and lines[i].strip() and not re.match(r'^(?:#|\||- |```)',lines[i].strip()):paragraph.append(lines[i].strip());i+=1
            add_prose(' '.join(paragraph),'abstract' if in_abstract else 'reference' if in_refs else 'body')
        out=args.output_dir/('Theodore-Ouyang-Merged-Heston-ZH.pdf' if name=='report' else 'Theodore-Ouyang-Merged-Heston-EN.pdf')
        doc=Manuscript(str(out),pagesize=letter,title=meta['titles'][name],author=meta['author'],subject=meta['subtitles'][name],pageCompression=1,initialFontName='TimesR',initialFontSize=FONT)
        doc.multiBuild(story,canvasmaker=MathCanvas,maxPasses=5)
        assert digest(path)==source_identity,'The source changed during typesetting.'
        assert len(log['math_occurrences'])==len(spans),(name,len(log['math_occurrences']),len(spans))
        log.update(pdf=out.relative_to(ROOT).as_posix() if out.is_relative_to(ROOT) else out.name,pdf_sha256=digest(out),math_source_occurrences=len(spans),vector_formulas=True)
        (ROOT/'qa').mkdir(exist_ok=True)
        (ROOT/'qa'/f'{name}-pdf-build.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        reports.append({'document':name,'pdf':out.name,'bytes':out.stat().st_size,'formulas':len(spans),'tables':len(log['tables']),'small_displays':[d for d in log['displays'] if d['font_pt']<8.5]})
    print(json.dumps(reports,indent=2))

if __name__=='__main__':main()
