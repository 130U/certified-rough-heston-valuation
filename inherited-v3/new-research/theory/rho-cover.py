"""Exact continuous-correlation extension; mathematical work counts only."""
from pathlib import Path
from fractions import Fraction as F
import gzip, hashlib, json, math
import dyadic as base

HERE = Path(__file__).resolve().parent
I, C, S = base.I, base.C, base.S
CENTRE = F(-1489, 2000)
HALF_WIDTH = F(1, 1000000)
_gamma, _alpha = {}, {}

class Bound:
    """Upper bounds for modulus and modulus of the rho derivative."""
    def __init__(self, value, derivative=0):
        self.value, self.derivative = F(value), F(derivative)
    def __add__(self, other):
        other = other if isinstance(other, Bound) else Bound(other)
        return Bound(self.value+other.value, self.derivative+other.derivative)
    __radd__ = __add__
    __sub__ = __add__
    def __mul__(self, other):
        other = other if isinstance(other, Bound) else Bound(other)
        return Bound(self.value*other.value,
                     self.derivative*other.value+self.value*other.derivative)
    __rmul__ = __mul__
    def __pow__(self, exponent):
        result = Bound(1)
        for _ in range(exponent): result = result*self
        return result

def lipschitz_constants():
    # |rho|<=3/4; |A|>=sqrt(7)/4>5/8, |R|<=1.
    # A'=Sbar*Sbar'/A, R'=A'-Sbar', |Sbar'|=1.
    sb, ainv, r = Bound(F(3,4), 1), Bound(F(8,5), F(384,125)), Bound(1,F(11,5))
    p, v, m, zeta = Bound(F(2,3)), Bound(F(1,3)), Bound(F(3,2)), Bound(F(2,3))
    b = Bound(F(1,2))
    db = sb*F(1,2) # 1/m<=1
    cb = zeta*(Bound(F(1,8))+sb**2*F(1,2))
    vv = p*r*ainv
    ww = m*p*v*r*ainv**2+p**2*r**2*ainv**3*F(1,2)
    delta = b**2*ww+2*b*r*vv+db*r*ww+db*vv**2+r**3
    f1 = b**2*vv+b*db*ww+b*r**2+db*r*vv+cb*r*ww+cb*vv**2
    f2 = b**2*r+b*db*vv+b*cb*ww+db**2*ww+db*r**2+cb*r*vv
    f3 = b**3+2*b*db*r+b*cb*vv+db**2*vv+cb*r**2
    pp = db*delta+b*f1
    bb = [fj*delta for fj in (f1,f2,f3)]
    dd = [b*delta**2, db*delta**2+2*b*bb[0],
          r*f3*delta+pp*f1+b*delta*f2,
          r*f3*f1+pp*f2+b*delta*f3,
          r*f3*f2+pp*f3, r*f3**2]
    return [q.derivative for q in bb], [q.derivative for q in dd]

def gamma(q):
    if q not in _gamma: _gamma[q] = base.gamma_positive(q)
    return _gamma[q]

def trig(x, cosine=False):
    total, term, x2 = I(0), I(1) if cosine else x, x.square()
    for k in range(32):
        total += (-1)**k*term
        n = 2*k+(0 if cosine else 1)
        term = term*x2/((n+1)*(n+2))
    degree = 64 if cosine else 65
    tail = I(0,x.hi,True)**degree/math.factorial(degree)
    return total+I(-tail.hi,tail.hi,True)

def alpha_constants(left,right):
    key = (left,right)
    if key not in _alpha:
        def endpoint(a):
            g1,g2,g3 = gamma(1+a),gamma(1+2*a),gamma(1+3*a)
            angle = base.PI*a
            return trig(angle)/angle,-trig(angle,True),g2/g1.square(),g2*g1/g3
        pl,vl,ml,zl = endpoint(left)
        pr,vr,mr,zr = endpoint(right)
        _alpha[key] = (I(pr.lo,pl.hi,True),I(vl.lo,vr.hi,True),
                       I(ml.lo,mr.hi,True),I(zr.lo,zl.hi,True))
    return _alpha[key]

def raw_values(al,ar,el,er):
    p,v,m,zeta = alpha_constants(al,ar)
    eta = I(I(el).lo,I(er).hi,True)
    h = (eta.square()+(1-eta).square()/4).sqrt()
    sigma = -CENTRE/2
    sb = C(sigma*(1-eta)/h,2*sigma*eta/h)
    a = C(1-CENTRE**2+2*sb.re.square(),2*sb.re*sb.im).sqrt_positive_real()
    r = 1/(a+sb)
    b,db = F(1,2),sb/(2*m)
    cb = C(zeta)*(C(F(1,8))-sb*sb/(2*m))
    vv = C(p)*r/a
    ww = C(m*p*v)*r/(a*a)+C(p.square())*r*r/(2*a**3)
    delta = b*b*ww+2*b*r*vv-db*r*ww-db*vv*vv-r**3
    f1 = b*b*vv+b*db*ww-b*r*r+db*r*vv+cb*r*ww+cb*vv*vv
    f2 = -b*b*r+b*db*vv+b*cb*ww+db*db*ww+db*r*r+cb*r*vv
    f3 = -b**3+2*b*db*r-b*cb*vv-db*db*vv+cb*r*r
    bb = [(fj*delta.conj()).re for fj in (f1,f2,f3)]
    pp = db*delta-b*f1
    dd = [-b*delta.norm2(),db.re*delta.norm2()-2*b*bb[0],
          (-r*f3*delta.conj()+pp*f1.conj()-b*delta*f2.conj()).re,
          (-r*f3*f1.conj()+pp*f2.conj()-b*delta*f3.conj()).re,
          (-r*f3*f2.conj()+pp*f3.conj()).re,-r.re*f3.norm2()]
    return bb, dd

def margin_check(row, lb, ld):
    mm = [F(s)-HALF_WIDTH*l for s,l in zip(row['B_lower'],lb)]
    nn = [F(s)-HALF_WIDTH*l for s,l in zip(row['negative_D_lower'],ld)]
    return min(mm+nn)>0, mm, nn

def evaluate(al,ar,el,er):
    bb,dd = raw_values(al,ar,el,er)
    return dict(alpha=[str(al),str(ar)],eta=[str(el),str(er)],
                B_lower=[str(F(z.lo,S)) for z in bb],
                negative_D_lower=[str(F(-z.hi,S)) for z in dd])

def main():
    protocol = json.loads((HERE/'rho-protocol.json').read_text(encoding='utf-8'))
    assert F(protocol['rho_half_width']) == HALF_WIDTH
    upstream = HERE/'legacy-compact-cover.json.gz'
    source = json.loads(gzip.decompress(upstream.read_bytes()))
    assert source['parameters']['alpha'] == ['13/25','3/5']
    assert F(source['parameters']['rho']) == CENTRE
    assert source['status'] == 'EXACT_DYADIC_INTERVAL_COMPLETE_ROUGH_SUBDOMAIN'
    pp,vv,mm,zz = alpha_constants(F(13,25),F(3,5))
    assert 0<pp.lo and pp.hi<=I(F(2,3)).lo
    assert 0<=vv.lo and vv.hi<=I(F(1,3)).lo
    assert I(1).hi<=mm.lo and mm.hi<=I(F(3,2)).lo
    assert 0<zz.lo and zz.hi<=I(F(2,3)).lo
    lb,ld = lipschitz_constants()
    accepted,refined,unresolved = [],[],[]
    todo=[]
    for index,row in enumerate(source['cover']):
        okay,b,d=margin_check(row,lb,ld)
        if okay:
            accepted.append(dict(upstream_leaf=index,
                                 B_extended_lower=list(map(str,b)),
                                 negative_D_extended_lower=list(map(str,d))))
        else:
            todo.append((*map(F,row['alpha']),*map(F,row['eta']),0,index))
    initial_refined=len(todo)
    count=0
    while todo:
        al,ar,el,er,depth,parent=todo.pop()
        count+=1
        try:
            row=evaluate(al,ar,el,er)
            okay,b,d=margin_check(row,lb,ld)
        except (AssertionError,ZeroDivisionError):
            okay=False
        if okay:
            row.update(upstream_leaf=parent,B_extended_lower=list(map(str,b)),
                       negative_D_extended_lower=list(map(str,d)))
            refined.append(row)
        elif depth>=protocol['maximum_additional_leaf_depth'] or count>=protocol['maximum_refined_evaluations']:
            unresolved.append(dict(alpha=list(map(str,(al,ar))),eta=list(map(str,(el,er))),upstream_leaf=parent,additional_depth=depth))
            if count>=protocol['maximum_refined_evaluations']:
                unresolved.extend(dict(alpha=list(map(str,(a,b))),eta=list(map(str,(c,d))),upstream_leaf=j,additional_depth=h)
                                  for a,b,c,d,h,j in todo)
                todo=[]
        else:
            if (ar-al)/(F(3,5)-F(13,25))>=er-el:
                mid=(al+ar)/2
                todo.extend([(mid,ar,el,er,depth+1,parent),(al,mid,el,er,depth+1,parent)])
            else:
                mid=(el+er)/2
                todo.extend([(al,ar,mid,er,depth+1,parent),(al,ar,el,mid,depth+1,parent)])
        if count%2000==0:
            print(json.dumps(dict(refined_evaluations=count,accepted_refined=len(refined),pending=len(todo),unresolved=len(unresolved))),flush=True)
    volume=lambda row:(F(row['alpha'][1])-F(row['alpha'][0]))*(F(row['eta'][1])-F(row['eta'][0]))
    area=sum(volume(source['cover'][r['upstream_leaf']]) for r in accepted)+sum(map(volume,refined))
    unresolved_area=sum(map(volume,unresolved))
    assert area+unresolved_area==F(2,25)
    bounds=accepted+refined
    result=dict(status='PASS_CONTINUOUS_RHO_ALPHA_ALL_FREQUENCY' if not unresolved else 'UNRESOLVED_CONTINUOUS_RHO_EXTENSION',
                parameters=dict(alpha=['13/25','3/5'],rho=list(map(str,(CENTRE-HALF_WIDTH,CENTRE+HALF_WIDTH))),kappa='0',eta=['0','1']),
                original_leaf_count=len(source['cover']),retained_leaf_count=len(accepted),
                initially_refined_leaf_count=initial_refined,refined_evaluations=count,
                new_refined_leaf_count=len(refined),unresolved_leaf_count=len(unresolved),
                exact_accepted_area=str(area),exact_unresolved_area=str(unresolved_area),
                B_rho_lipschitz=list(map(str,lb)),D_rho_lipschitz=list(map(str,ld)),
                B_uniform_extended_lower=[str(min(F(r['B_extended_lower'][j]) for r in bounds)) for j in range(3)],
                negative_D_uniform_extended_lower=[str(min(F(r['negative_D_extended_lower'][j]) for r in bounds)) for j in range(6)],
                alpha_scalar_enclosures=[q.bounds() for q in (pp,vv,mm,zz)],
                upstream_sanitized_sha256=hashlib.sha256(upstream.read_bytes()).hexdigest(),
                protocol_sha256=hashlib.sha256((HERE/'rho-protocol.json').read_bytes()).hexdigest(),
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                dyadic_sha256=hashlib.sha256((HERE/'dyadic.py').read_bytes()).hexdigest(),
                retained=accepted,refined=refined,unresolved=unresolved)
    payload=json.dumps(result,separators=(',',':')).encode('utf-8')
    (HERE/'rho-cover.json.gz').write_bytes(gzip.compress(payload,compresslevel=9,mtime=0))
    print(json.dumps({k:v for k,v in result.items() if k not in ('retained','refined','unresolved')}),flush=True)
    if unresolved: raise SystemExit(1)

if __name__=='__main__': main()
