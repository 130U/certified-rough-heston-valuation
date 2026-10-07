"""Exact true-CF envelope from Re-Riccati comparison and the full forward curve.

This needs the model-law and positive exponent-kernel theorems.  It is not a
solver accuracy claim.  All endpoint arithmetic is 100-bit integer dyadic.
"""
from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,hashlib,sys
sp=importlib.util.spec_from_file_location('moments',Path(__file__).with_name('exact-forward-moments.py'))
mo=importlib.util.module_from_spec(sp);sp.loader.exec_module(mo)
I,S=mo.I,mo.S
NU=F(2897,10000);RHO=F(-1489,2000);S0=-RHO/2;T=F(1,2)

def cumulative_q(z,alpha,terms=64):
    z=F(z);alpha=F(alpha)
    if z==0:return I(0)
    power=mo.power(z,1-alpha);w=mo.LAMBDA*mo.power(z,mo.ALPHA0)
    term=I(1);ml=I(0)
    for n in range(terms):
        ml+=term/mo.gamma_cached(2-alpha+n*mo.ALPHA0);term=-term*w
    # All denominator arguments >=1, and Gamma(x)>=e^-1>1/3 there.
    tail=3*w**terms/(1-w);ml+=I(-tail.hi,tail.hi,True)
    return mo.THETA*power/mo.gamma_cached(2-alpha)+(mo.V0-mo.THETA)*power*ml

def time_data(alpha,n=64):
    t=[T*F(j,n) for j in range(n+1)]
    ac=[cumulative_q(T-q,alpha) for q in t]
    masses=[ac[j]-ac[j+1] for j in range(n)]
    # Exact positivity follows from q>=0; rounding intersection is admissible.
    masses=[I(max(0,q.lo),q.hi,True) for q in masses]
    return t,[mo.power(q,alpha) for q in t[:-1]],masses

def envelope_node(u,alpha,td):
    u=F(u);alpha=F(alpha);t,powers,masses=td
    root=(I(S0*S0+(1-RHO*RHO)*u*u+F(1,4))).sqrt()
    r=root-S0;l=(root+S0)/2;g=mo.gamma_cached(1+alpha)
    integral=I(0)
    for p,m in zip(powers,masses):
        z=l*NU*p;integral+=z/(g+z)*m
    exponent=r*integral/NU
    assert exponent.lo>=0
    return mo.signed_exp(-exponent),exponent

def tail_rate(V,alpha,td):
    V=F(V);alpha=F(alpha);t,powers,masses=td
    base=I(1-RHO*RHO).sqrt();br=base-S0/V;assert br.lo>0
    g=mo.gamma_cached(1+alpha);integral=I(0)
    for p,m in zip(powers,masses):
        z=base*NU*V*p/2;integral+=z/(g+z)*m
    return br*integral/NU

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    executed_hash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    mmax=I(F(240000,211093)).sqrt();rows=[]
    for alpha in map(F,['.52','.6','.9']):
        td=time_data(alpha);tails=[]
        for V in [20,32,48,64,80,96,128,160,200]:
            c=tail_rate(V,alpha,td);cl=I(c.lo,c.lo,True)
            bound=mmax*mo.signed_exp(-cl*V)/(mo.dy.PI*cl*V*V)
            tails.append({'V':V,'c_lower':str(F(c.lo,S)),
                'normalized_price_tail_upper':str(F(bound.hi,S))})
        nodes=[]
        for j in range(1025):
            u=F(j,8);b,exponent=envelope_node(u,alpha,td)
            nodes.append({'u':str(u),'CF_modulus_upper':str(F(b.hi,S)),
                'exponent_lower':str(F(exponent.lo,S))})
        rows.append({'alpha':str(alpha),'T':str(T),'rho':str(RHO),'nu':str(NU),
            'time_partition':64,'tails':tails,'frequency_nodes':nodes})
        print('alpha',alpha,[(r['V'],float(F(r['normalized_price_tail_upper']))) for r in tails],flush=True)
    assert hashlib.sha256(Path(__file__).read_bytes()).hexdigest()==executed_hash
    result={'status':'EXACT_TRUE_CF_COMPARISON_ENVELOPE_WITH_MODEL_ASSUMPTIONS',
      'model_proof':'model-admissibility.md','kernel_proof':'fractional-exponent-linearization.md',
      'tail_proof':'direct-real-tail.md','terms':64,'bits':mo.dy.BITS,
      'source_sha256':executed_hash,'cover':rows}
    target=Path(__file__).with_name('direct-tail-certificate.json')
    target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('PASS',target.name,flush=True)

if __name__=='__main__':main()
