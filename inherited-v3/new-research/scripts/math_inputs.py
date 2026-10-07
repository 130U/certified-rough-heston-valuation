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
