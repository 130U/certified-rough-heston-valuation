"""Standard vector step plots, rational pass counting before display conversion."""
from pathlib import Path
from fractions import Fraction as Q
import html,json,math
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
HERE=Path(__file__).resolve().parent
W,H=1100,850;parts=[];pdf=canvas.Canvas(str(HERE/'portfolio-pass-counts.pdf'),pagesize=(W,H),invariant=True)
pdf.setTitle('Exact-endpoint certification counts');pdf.setAuthor('Research evidence')
def line(x1,y1,x2,y2,color='#111111',width=1,dash=False):
 parts.append(f'<line x1="{x1:.4f}" y1="{y1:.4f}" x2="{x2:.4f}" y2="{y2:.4f}" stroke="{color}" stroke-width="{width}"'+(' stroke-dasharray="6 4"' if dash else '')+'/>');pdf.setStrokeColor(HexColor(color));pdf.setLineWidth(width);pdf.setDash(6,4) if dash else pdf.setDash();pdf.line(x1,H-y1,x2,H-y2)
def text(x,y,s,size=12,color='#111111',anchor='start'):
 size *= 1.95  # Presentation only: legible at the 396 pt Letter-paper column width.
 parts.append(f'<text x="{x:.4f}" y="{y:.4f}" font-family="Helvetica,Arial,sans-serif" font-size="{size}" fill="{color}" text-anchor="{anchor}">{html.escape(s)}</text>');pdf.setFillColor(HexColor(color));pdf.setFont('Helvetica',size)
 {'start':pdf.drawString,'middle':pdf.drawCentredString,'end':pdf.drawRightString}[anchor](x,H-y,s)
def path(coords,color,dash=False):
 d='M '+' L '.join(f'{x:.4f} {y:.4f}' for x,y in coords);parts.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2.1"'+(' stroke-dasharray="6 4"' if dash else '')+'/>');pdf.setStrokeColor(HexColor(color));pdf.setLineWidth(2.1);pdf.setDash(6,4) if dash else pdf.setDash();p=pdf.beginPath();p.moveTo(coords[0][0],H-coords[0][1])
 for x,y in coords[1:]:p.lineTo(x,H-y)
 pdf.drawPath(p)
def main():
 d=json.loads((HERE/'portfolio-budget-counts.json').read_text(encoding='utf-8'));curves={}
 for r in d['threshold_rows']:curves.setdefault((r['configuration_id'],r['alpha'],r['method']),[]).append(Q(r['exact_threshold_points']))
 text(W/2,27,'Complete certificates: exact upper-endpoint pass counts',19,anchor='middle');text(W/2,47,'28 fixed directions per curve; within-bank joint and marginal methods use identical radii',12,anchor='middle')
 panels=[('13/25','Original field: alpha = .52',[('H0','#888888'),('H1','#1766a5')]),('3/5','Original field: alpha = .60',[('H0','#888888'),('H1','#1766a5')]),('9/10','Original field: alpha = .90',[('H0','#888888'),('H1','#1766a5')]),('13/25','Regenerated field: alpha = .52',[('N1','#7b3294'),('N2','#e08214'),('N2L','#008837')])]
 for index,(alpha,title,banks) in enumerate(panels):
  left=75+(index%2)*535;top=95+(index//2)*355;width=440;height=225
  X=lambda q:left+float(q)*width/2;Y=lambda n:top+height-n*height/28
  text(left,top-19,title,14)
  for n in [0,7,14,21,28]:line(left,Y(n),left+width,Y(n),'#dddddd',.7);text(left-8,Y(n)+4,str(n),11,anchor='end')
  for b in [Q(),Q(1,4),Q(1,2),Q(1),Q(3,2),Q(2)]:line(X(b),top,X(b),top+height,'#eeeeee',.7);text(X(b),top+height+18,str(float(b)).rstrip('0').rstrip('.') if b else '0',10,anchor='middle')
  line(left,top,left,top+height);line(left,top+height,left+width,top+height);text(left+width/2,top+height+38,'Complete tolerance (index points)',11,anchor='middle');text(left,top-4,'Passed',10)
  for bank,color in banks:
   for method in ['marginal','joint']:
    v=curves[bank,alpha,method];events=sorted(set(t for t in v if 0<=t<=2));coords=[(X(0),Y(sum(t<=0 for t in v)))];previous=sum(t<=0 for t in v)
    for t in events:
     current=sum(z<=t for z in v);coords.append((X(t),Y(previous)));coords.append((X(t),Y(current)));previous=current
    coords.append((X(2),Y(previous)));path(coords,color,method=='marginal')
  legend_y=top+height+58
  for k,(bank,color) in enumerate(banks):line(left+k*145,legend_y,left+22+k*145,legend_y,color,2);text(left+28+k*145,legend_y+4,bank,10)
 text(75,800,'Solid: joint. Dashed: signed marginal. H0: old uniform; H1: finite horizon; N1/N2: global; N2L: 128 bins.',11)
 text(75,819,'Shown range: 0-2 points. All exact thresholds are retained in CSV/JSON. Across-bank changes are descriptive.',10.5)
 svg='<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="850" viewBox="0 0 1100 850"><rect width="1100" height="850" fill="white"/>'+''.join(parts)+'</svg>'
 (HERE/'portfolio-pass-counts.svg').write_text(svg,encoding='utf-8');pdf.showPage();pdf.save();print('PASS standard vector budget plots from504 exact thresholds')
if __name__=='__main__':main()
