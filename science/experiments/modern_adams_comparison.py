"""BL-modified Adams core, adapted to the declared forward-curve Riccati model.

The asymptotic subtraction, frequency scaling, linear Adams weights, and fixed
Picard corrections follow Boyarchenko et al., arXiv:2508.15080v1, §3.2/App. B.
The affine transform is evaluated for OUR frozen forward curve and kappa=0;
the paper's constant-parameter transform is not imported. This is a comparison
of its Riccati core, not a reproduction of SINH-CB or a certified BL algorithm.
All returned finite binary64 prices can subsequently receive the same strict
reference-centre translation certificate as any arbitrary frozen output.
"""
from pathlib import Path
from fractions import Fraction as Q
import hashlib,importlib.util,json,math,sys
import numpy as np
HERE=Path(__file__).resolve().parent;SDK=HERE/'sdk';sys.dont_write_bytecode=True
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,o):p.write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def module(name,file):
    sp=importlib.util.spec_from_file_location(name,SDK/file);m=importlib.util.module_from_spec(sp);sys.modules[name]=m;sp.loader.exec_module(m);return m
def exact(x):return Q.from_float(float(x))

def modified_adams(alpha,u,N,picard=8):
    t=np.linspace(0,.5,N+1);dt=.5/N;scale=1+np.sqrt(u*u+.25)
    c=-(u*u+.25)/2;d=-.7445/2+1j*(-.7445)*u;nu=.2897
    lead=nu*t[:,None]**alpha*c[None,:]/(math.gamma(1+alpha)*scale[None,:])
    remainder=np.zeros_like(lead,dtype=complex);cache=np.zeros_like(remainder);h=np.zeros_like(remainder)
    factor=dt**alpha/math.gamma(2+alpha)
    failed=False
    with np.errstate(over='ignore',invalid='ignore'):
        for k in range(N):
            a=np.empty(k+1);a[0]=factor*(k**(alpha+1)-(k-alpha)*(k+1)**alpha)
            if k:
                lag=k-np.arange(1,k+1)
                a[1:]=factor*((lag+2)**(alpha+1)+lag**(alpha+1)-2*(lag+1)**(alpha+1))
            predict=a@cache[:k+1]
            def rhs(r):
                z=lead[k+1]+r;return nu*(d*z+scale*z*z/2)
            z=predict+factor*rhs(remainder[k])
            for _ in range(picard):z=predict+factor*rhs(z)
            remainder[k+1]=z;cache[k+1]=rhs(z);h[k+1]=scale*(lead[k+1]+z)
            if not np.all(np.isfinite(h[k+1])):failed=True;break
        f=c[None,:]+d[None,:]*h+h*h/2
    return t,h,f,failed

def main():
    contract=load(HERE/'nearby-contract-execution.json')
    proto={'status':'FROZEN_BEFORE_MODERN_OUTPUTS','alpha':'13/25','T':'1/2','steps':[512,1024],
       'Picard_corrections':8,'u_step':'1/8','u_upper':'64','exponent_time_Gauss_order':16,
       'target_spread':['4400','4500'],'index_point_tolerance':'1/4',
       'source':'https://arxiv.org/html/2508.15080v1#S3.SS2',
       'method_scope':'BL-modified Adams Riccati core adapted to same forward-curve model; flat Fourier inversion, not SINH-CB',
       'proof_scope':'Nominal refinement difference is empirical. Deterministic guarantees, if evaluated, use the complete independent strict reference certificate and pay centre translation.',
       'nearby_contract_sha256':sha(HERE/'nearby-contract-execution.json')}
    pp=HERE/'modern-adams-contract.json'
    text=json.dumps(proto,indent=2)+'\n'
    if pp.exists():assert pp.read_text(encoding='utf-8')==text
    else:pp.write_text(text,encoding='utf-8')
    fast=module('modern_fast','price-profile-diagnostic.py')
    quotes=[r for r in load(SDK/'normalized-quote-bands.json')['rows'] if Q(r['T_decimal_input'])==Q(1,2)]
    m=np.array([float(Q(r['moneyness_fraction'])) for r in quotes]);u=np.arange(513)/8;H=.125
    quad=np.full(513,H);quad[0]=H/2
    records=[]
    for N in proto['steps']:
        t,h,f,failed=modified_adams(.52,u,N)
        workload={'Fourier_nodes':513,'time_steps':N,'history_scalar_vector_products':513*N*(N+1)//2,
           'transformed_Riccati_evaluations':513*(N*(8+2)),
           'exponent_time_quadrature_evaluations':513*N*16,'Picard_corrections_per_step':8}
        if failed:
            records.append({'N':N,'status':'NONFINITE_NOMINAL_OUTPUT_RETAINED','workload':workload});continue
        ex=fast.exponent_linear_F(t,f,.5,16);calls=fast.prices(np.exp(ex),u,quad,m)
        if not np.all(np.isfinite(calls)):
            records.append({'N':N,'status':'NONFINITE_NOMINAL_OUTPUT_RETAINED','workload':workload});continue
        outputs=list(map(exact,calls));records.append({'N':N,'status':'FINITE_NOMINAL_OUTPUT_NOT_INTRINSIC_ACCURACY_CERTIFICATE',
            'exact_stored_call_outputs':list(map(str,outputs)),'spread_points':str((outputs[7]-outputs[8])*Q(211093,50)),
            'workload':workload,'max_node_real_H':str(exact(np.max(h.real)))})
    finite=[r for r in records if 'spread_points' in r]
    diff=str(abs(Q(finite[-1]['spread_points'])-Q(finite[0]['spread_points']))) if len(finite)==2 else None
    save(HERE/'modern-adams-outputs.json',{'status':'EXECUTED_MODERN_RICCATI_CORE_SAME_MODEL_NOMINAL_OUTPUTS',
       'contract_sha256':sha(pp),'executed_source_sha256':sha(Path(__file__)),'rows':records,
       'empirical_512_1024_spread_refinement_difference_points':diff,
       'qualification':'This difference does not bound the true price error. Both strict translation comparisons are computed after the independent candidate certificate is complete.'})
    print('PASS modern modified-Adams execution',[(r['N'],r['status']) for r in records],flush=True)
if __name__=='__main__':main()
