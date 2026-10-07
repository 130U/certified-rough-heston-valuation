"""Rigorous integral/exponential of an exact stored field, not true CF accuracy.

All decisions use 100-bit integer dyadic intervals.  Node phi enclosures here
are for exp(Lbar), where Lbar integrates the stored continuous field.  They
must be combined with a separately certified residual before true pricing.
"""
from pathlib import Path
from fractions import Fraction as F
import importlib.util, argparse, json, hashlib, sys, time
import numpy as np
BASE=Path(__file__).parent
sp=importlib.util.spec_from_file_location('moments',BASE/'exact-forward-moments.py')
mo=importlib.util.module_from_spec(sp);sp.loader.exec_module(mo)
I,S,C=mo.I,mo.S,mo.dy.C
NU=F(2897,10000)

def exact(x):return F(*float(x).as_integer_ratio())
def trig(x,cos=False):
    # Choose any integer period and verify the reduced enclosure, so the
    # initial binary64 choice affects efficiency but never correctness.
    n=round(float(F(x.lo+x.hi,2*S))/(2*np.pi))
    z=x-2*n*mo.dy.PI
    assert max(abs(z.lo),abs(z.hi))<4*S
    zz=z.square();term=I(1) if cos else z;total=term
    for k in range(1,65):
        term=-term*zz/((2*k-1)*(2*k) if cos else (2*k)*(2*k+1))
        total+=term
    # Taylor Lagrange remainder on [-4,4]; |sin/cos derivative|<=1.
    import math
    degree=128 if cos else 129
    rem=I(F(4)**(degree+1)/math.factorial(degree+1))
    return total+I(-rem.hi,rem.hi,True)

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    p=argparse.ArgumentParser();p.add_argument('--field',default='fixed-field-betap52.npz')
    args=p.parse_args();start=0;source=BASE/args.field
    executed_source_hash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    before=hashlib.sha256(source.read_bytes()).hexdigest()
    with np.load(source) as archive:data={k:archive[k] for k in archive.files}
    assert hashlib.sha256(source.read_bytes()).hexdigest()==before,'Field changed during read'
    meta=json.loads(source.with_suffix('.json').read_text(encoding='utf-8'))
    assert meta['sha256']==before,'Metadata and stored field do not match'
    beta=F(meta['beta_exact_decimal']);t=[exact(v) for v in data['t']]
    u=[exact(v) for v in data['u']];assert t[0]==0 and t[-1]==F(1,2)
    weightfile=source.with_name(source.stem+'-forward-weights.json')
    weights=mo.linear_field_weights(t,F(1,2),64)
    weightfile.write_text(json.dumps({'field_sha256':before,'terms':64,'weights':[w.bounds() for w in weights]},indent=2)+'\n',encoding='utf-8')
    print('certified forward weights',len(weights),flush=True)
    w0=mo.moments(F(1,2),64)[0]
    w1=mo.power_field_moment(beta,F(1,2),64)
    w2=mo.power_field_moment(2*beta,F(1,2),64)
    report=[]
    for j,uj in enumerate(u):
        a1=complex(data['A1'][j]);a2=complex(data['A2'][j])
        exponent=C(-(uj*uj+F(1,4))/2)*w0
        exponent+=C(exact(a1.real),exact(a1.imag))*w1/NU
        exponent+=C(exact(a2.real),exact(a2.imag))*w2/NU
        for k,w in enumerate(weights):
            q=complex(data['LG'][k,j]);exponent+=C(exact(q.real),exact(q.imag))*w/NU
        magnitude=mo.signed_exp(exponent.re)
        phi=C(magnitude*trig(exponent.im,True),magnitude*trig(exponent.im))
        report.append({'u':str(uj),'exponent_re':exponent.re.bounds(),
            'exponent_im':exponent.im.bounds(),'phi_re':phi.re.bounds(),
            'phi_im':phi.im.bounds(),'phi_modulus':magnitude.bounds()})
        if j and j%128==0:print('nodes',j,'seconds',round(0-start,2),flush=True)
    assert hashlib.sha256(source.read_bytes()).hexdigest()==before,'Field changed during certificate calculation'
    assert hashlib.sha256(Path(__file__).read_bytes()).hexdigest()==executed_source_hash,'Source changed during run'
    result={'status':'EXACT_STORED_FIELD_EXPONENT_COMPONENT_NOT_TRUE_CF_CERTIFICATE',
      'field':source.name,'field_sha256':before,
      'beta':str(beta),'candidate_alpha_note':'Lbar derivative exponent fixed for this field; true error depends on alpha residual',
      'T':'1/2','nu':str(NU),'terms':64,'bits':mo.dy.BITS,'nodes':len(report),
      'maximum_exponent_re_upper':str(max(F(z['exponent_re'][1]) for z in report)),
      'maximum_phi_interval_component_width':str(max(F(z[key][1])-F(z[key][0]) for z in report for key in ['phi_re','phi_im'])),
      'source_sha256':executed_source_hash,
      'cover':report}
    target=source.with_name(source.stem+'-exponent-certificate.json')
    target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('PASS integral component', target.name, flush=True)

if __name__=='__main__':main()
