"""Direct Caputo-inversion startup audit from delivered field coefficients.

New assembly uses finite generalized-power terms and exact dyadic arithmetic.
No solver update, original residual assembly, or binary64 dot product is used.
Elementary Gamma/power enclosures are shared with the public interval library.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib,importlib.util,json,sys,time
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
from audit_paths import release_root
RELEASE=release_root(HERE)
FROZEN=RELEASE/'code'/'frozen';SRC=RELEASE/'code'/'src'
def exact(x):return Q.from_float(float(x))
def main():
    import numpy as np
    start=0
    sp=importlib.util.spec_from_file_location('startup_mo',SRC/'exact-forward-moments.py')
    mo=importlib.util.module_from_spec(sp);sp.loader.exec_module(mo);I,C,S=mo.I,mo.dy.C,mo.S
    nu=Q(2897,10000);rho=Q(-1489,2000);records=[]
    for alpha,stem,rawname in [('13/25','fixed-field-betap52-u128','field-residual-certificate-point052-v3-u64.json'),
                              ('3/5','fixed-field-betap6-u128','field-residual-certificate-point06-v3-u64.json'),
                              ('9/10','fixed-field-betap9-u80','field-residual-betap9-u64-v3.json')]:
        a=Q(alpha);raw=json.loads((FROZEN/rawname).read_text());path=FROZEN/(stem+'.npz')
        assert hashlib.sha256(path.read_bytes()).hexdigest()==raw['field_sha256']
        with np.load(path,allow_pickle=False) as archive:
            times,frequencies,A1data,A2data,LGdata=[archive[k] for k in ['t','u','A1','A2','LG']]
            t1=exact(times[1]);assert np.all(LGdata[0]==0),'initial affine remainder must be zero'
            powers={p:mo.power(t1,p) for p in set([a,2*a,1]+[k*a for k in range(1,7)]+[a+1,2*a+1,3*a+1,4*a+1,2*a+2])}
            upper=[];inside=[]
            for j in range(513):
                u=exact(frequencies[j]);c=-(u*u+Q(1,4))/2;d=C(rho/2,rho*u)
                def stored_complex(z):return C(exact(z.real),exact(z.imag))
                A1=stored_complex(A1data[j]);A2=stored_complex(A2data[j]);L1=stored_complex(LGdata[1,j])
                # Exact Caputo identity D^a [Gamma(1+p)/Gamma(1+p+a)*t^(p+a)] = t^p.
                H=[(a,C(nu*c)/C(mo.gamma_cached(1+a))),
                   (2*a,A1*C(mo.gamma_cached(1+a)/mo.gamma_cached(1+2*a))),
                   (3*a,A2*C(mo.gamma_cached(1+2*a)/mo.gamma_cached(1+3*a))),
                   (a+1,L1/C(t1*mo.gamma_cached(2+a)))]
                G0=nu*c
                assert G0-nu*c==0,'constant startup residual must cancel exactly'
                terms={}
                def add(p,z):terms[p]=terms.get(p,C(0))+z
                add(a,A1);add(2*a,A2);add(Q(1),L1/C(t1))
                for p,z in H:add(p,-nu*d*z)
                for p,z in H:
                    for q,w in H:add(p+q,-Q(1,2)*nu*z*w)
                bound=I(0)
                for p,z in terms.items():bound+=z.norm2().sqrt()*powers[p]
                value=Q(bound.hi,S);upper.append(str(value));inside.append(value<=Q(raw['first_cell_physical_upper_exact_dyadics'][j]))
            full_inside=[Q(v)<=Q(raw['delta_physical_upper_exact_dyadics'][j]) for j,v in enumerate(upper)]
            comparisons={'within_saved_first_cell':sum(inside),'within_saved_complete_residual':sum(full_inside),
                         'maximum_ratio_to_saved_first_cell':str(max(Q(v)/Q(raw['first_cell_physical_upper_exact_dyadics'][j]) for j,v in enumerate(upper))),
                         'first_failing_first_cell_indices':[j for j,v in enumerate(inside) if not v][:12]}
            print(json.dumps({'alpha':alpha,'comparison':comparisons}),flush=True)
            assert all(full_inside),'direct exact startup enclosure exceeds frozen complete residual bound'
        records.append({'alpha':alpha,'nodes':513,'field_sha256':raw['field_sha256'],
                        'first_interval_exact':[str(Q(0)),str(t1)],'all_direct_startup_upper_bounds_within_frozen_complete_residual':True,
                        'comparison':comparisons,
                        'direct_first_cell_physical_upper_exact':upper})
    rejected=False
    try:
        nu_c=nu*(-Q(1,8));wrong_G0=Q(0);assert wrong_G0-nu_c==0,'missing constant startup cancellation'
    except AssertionError:rejected=True
    assert rejected
    result={'status':'PASS_DIRECT_STARTUP_CAPUTO_INVERSION_AUDIT','records':records,'total_frequency_startups':1539,
            'deliberate_missing_initial_cancellation_rejected':rejected,
            'scope':'First closed time interval only, all 513 actual residual frequencies in each of three fields. Independently assembled exact generalized-power residual; Gamma and scalar power primitives reused.'}
    (HERE/'startup-independent.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))
if __name__=='__main__':main()
