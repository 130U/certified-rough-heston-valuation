"""Canonicalize TeX formula inputs without rewriting their mathematics."""
import re, hashlib

def strip_tags(source):
    out=[];tags=[];cursor=0
    for match in re.finditer(r'\\tag\*?\s*\{',source):
        start=match.start()
        if start<cursor:continue
        slashes=0;k=start-1
        while k>=0 and source[k]=='\\':slashes+=1;k-=1
        if slashes%2:continue
        arg_start=match.end();depth=1;k=arg_start
        while k<len(source) and depth:
            if source[k]=='\\' and k+1<len(source) and source[k+1] in '{}':k+=2;continue
            if source[k]=='{':depth+=1
            elif source[k]=='}':depth-=1
            k+=1
        if depth:raise ValueError('Unbalanced tag')
        out.append(source[cursor:start]);tags.append(source[arg_start:k-1]);cursor=k
    out.append(source[cursor:])
    return ''.join(out).strip(),tags

def canonical(tex,display):
    clean,tags=strip_tags(tex) if display else (tex.strip(),[])
    ident='m'+hashlib.sha256((('D' if display else 'I')+'\0'+clean).encode()).hexdigest()[:20]
    return ident,clean,tags

# GitHub draws an inline formula as MathML in the browser. An operator name is set with \mathrm,
# a letter variant is a Unicode character, and a named function takes an explicit thin space
# before a bare argument, as TeX would set it.
def _letters(capital,small=None,exceptions=()):
    table={chr(65+i):chr(capital+i) for i in range(26)}
    if small:table.update({chr(97+i):chr(small+i) for i in range(26)})
    table.update(dict(exceptions))
    return table

VARIANTS={
    'mathbb':_letters(0x1D538,0x1D552,[('C','\u2102'),('H','\u210D'),('N','\u2115'),('P','\u2119'),('Q','\u211A'),('R','\u211D'),('Z','\u2124')]),
    'mathcal':_letters(0x1D49C,0x1D4B6,[('B','\u212C'),('E','\u2130'),('F','\u2131'),('H','\u210B'),('I','\u2110'),('L','\u2112'),('M','\u2133'),('R','\u211B'),('e','\u212F'),('g','\u210A'),('o','\u2134')]),
    'mathbf':_letters(0x1D400,0x1D41A),
    'mathsf':_letters(0x1D5A0,0x1D5BA),
}
FUNCTIONS='log|ln|exp|sin|cos|tan|sinh|cosh|tanh'
NO_THIN_SPACE=set(('right bigl bigr Bigl Bigr biggl biggr lbrace rbrace langle rangle lfloor rfloor lceil rceil '
    'lvert rvert lVert rVert quad qquad le ge lt gt ne in to approx sim equiv mid cdot times pm end text '
    'max min sup inf lim det Pr').split())

def _thin_space(tex,k):
    """A thin space belongs at position k when an ordinary symbol follows."""
    rest=tex[k:].lstrip()
    if not rest:return False
    if rest[0]=='\\':
        word=re.match(r'\\([a-zA-Z]+)',rest)
        return bool(word) and word[1] not in NO_THIN_SPACE
    return rest[0].isalnum() or rest[0]=='|' or ord(rest[0])>127

def _after_scripts(tex,k):
    while k<len(tex) and tex[k] in '_^':
        k+=1
        if k<len(tex) and tex[k]=='{':
            depth=0
            while k<len(tex):
                depth+={'{':1,'}':-1}.get(tex[k],0);k+=1
                if not depth:break
        else:
            token=re.match(r'\\[a-zA-Z]+|.',tex[k:],re.S)
            k+=len(token[0]) if token else 0
    return k

def github_inline(tex):
    tex=re.sub(r'\\operatorname\{([^{}]*)\}',r'\\mathrm{\1}',tex)
    def variant(match):
        table=VARIANTS[match[1]]
        letters=match[2].strip('{}')
        if any(c not in table for c in letters):raise ValueError('No Unicode form for '+match[0])
        return ''.join(table[c] for c in letters)
    tex=re.sub(r'\\(mathbb|mathcal|mathbf|mathsf) *(\{[A-Za-z]+\}|[A-Za-z])',variant,tex)
    out=[];cursor=0
    for match in re.finditer(r'\\(?:'+FUNCTIONS+r')(?![a-zA-Z])|\\mathrm\{(?:Re|Im)\}',tex):
        k=_after_scripts(tex,match.end())
        if tex[k:].lstrip()[:2] in ('\\,','\\!','\\;','\\:'):continue
        if _thin_space(tex,k):
            out.append(tex[cursor:k]+'\\,');cursor=k+len(tex[k:])-len(tex[k:].lstrip())
    return absolute_values(''.join(out)+tex[cursor:])

# The browser sets a bare bar as an infix operator, with space on both sides. Bars that pair up as
# absolute values are written \left\vert ... \right\vert, which it sets tight.
SIZED=('left','right','bigl','bigr','Bigl','Bigr','biggl','biggr','middle')
SEPARATES=re.compile(r'\\(?:le|ge|lt|gt|ne|in|to|quad|qquad|mid|approx|sim|equiv|text)(?![a-zA-Z])|\\\\|[,;=<>&]|\\ ')

def _bars(tex):
    found=[];depth=0;k=0;word=''
    while k<len(tex):
        c=tex[k]
        if c=='\\':
            name=re.match(r'\\([a-zA-Z]+)',tex[k:])
            if not name:word='';k+=2;continue
            if name[1]=='vert' and word not in SIZED:
                end=k+len(name[0]);found.append((k,end+(tex[end:end+1]==' '),depth))
            word=name[1];k+=len(name[0]);continue
        if c in '{}':depth+=1 if c=='{' else -1
        elif c=='|' and word not in SIZED:found.append((k,k+1,depth))
        if not c.isspace():word=''
        k+=1
    return found

def _outside_groups(tex):
    out=[];depth=0;k=0
    while k<len(tex):
        if tex[k]=='\\' and k+1<len(tex) and not tex[k+1].isalpha():
            if not depth and tex[k+1] in '\\ ':out.append(tex[k:k+2])
            k+=2;continue
        if tex[k] in '([{':depth+=1
        elif tex[k] in ')]}':depth-=1
        elif not depth:out.append(tex[k])
        k+=1
    return ''.join(out),depth

def absolute_values(tex):
    bars=_bars(tex)
    if not bars or len(bars)%2:return tex
    out=[];cursor=0
    for (a0,a1,depth_a),(b0,b1,depth_b) in zip(bars[0::2],bars[1::2]):
        inner=tex[a1:b0];outside,unclosed=_outside_groups(inner)
        if depth_a!=depth_b or not inner.strip() or unclosed or SEPARATES.search(outside):return tex
        out.append(tex[cursor:a0]+'\\left\\vert'+(' ' if inner[:1].isalpha() else '')+inner+'\\right\\vert'
                   +(' ' if tex[b1:b1+1].isalpha() else ''))
        cursor=b1
    return ''.join(out)+tex[cursor:]
