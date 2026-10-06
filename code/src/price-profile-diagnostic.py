"""Self-written offline numerical prices, explicitly NOT certified model prices.

Reference: implicit product integration; forward-variance curve frozen at alpha0.
Rational comparison: characteristic exponent defined using D^alpha Hhat, via an
equivalent fractional convolution kernel; never substitutes F(Hhat) for D Hhat.
The first twelve T=.5 quotes are a declared preliminary subset, not the full
48-quote contract's primary objective.
"""
from pathlib import Path
from fractions import Fraction
import argparse, importlib.util, json, math, time, sys
import numpy as np

BASE=Path(__file__).parent
spec=importlib.util.spec_from_file_location('solver',BASE/'solver-diagnostic.py')
solver=importlib.util.module_from_spec(spec);spec.loader.exec_module(solver)
ALPHA0=.5286;RHO=-.7445;NU=.2897;V0=.0262;THETA=.0721;LAM=.5037

def xi(t):
    z=-LAM*np.maximum(t,0.)**ALPHA0
    term=np.ones_like(z);value=term.copy()
    for k in range(1,45):term=term*z;value+=term/math.gamma(1+k*ALPHA0)
    return THETA+(V0-THETA)*value

def fourier_grid(order):
    cuts=np.r_[np.arange(0,5.0001,.5),np.arange(6,40.0001,2),np.arange(50,200.0001,10)]
    z,w=np.polynomial.legendre.leggauss(order)
    nodes=np.concatenate([(a+b)/2+(b-a)/2*z for a,b in zip(cuts[:-1],cuts[1:])])
    weights=np.concatenate([(b-a)/2*w for a,b in zip(cuts[:-1],cuts[1:])])
    return nodes,weights

def reference(alpha,u,n,T):
    solver.ALPHA=alpha
    y=np.linspace(0,NU*T**alpha,n+1);x=y**(1/alpha);t=x/NU**(1/alpha)
    H=np.zeros((len(y),len(u)),complex);f=np.zeros_like(H)
    c=-(u*u+.25)/2;d=RHO/2+1j*RHO*u;f[0]=c
    for j in range(1,len(y)):
        wl,wr=solver.integration_weights(x[j],x[:j+1]);w=wr[-1]
        history=wl@f[:j]+wr[:-1]@f[1:j]
        g=history+w*c;B=1-w*d
        H[j]=2*g/(B+np.sqrt(B*B-2*w*g))
        f[j]=c+d*H[j]+H[j]*H[j]/2
    return t,H,f

def exponent_linear_F(t,f,T,order):
    z,w=np.polynomial.legendre.leggauss(order)
    left=t[:-1];h=np.diff(t)
    # Fbar is affine in physical t as well as normalized physical x.
    tau=(z+1)/2
    weights=xi(T-(left[:,None]+h[:,None]*tau[None,:]))*w[None,:]*h[:,None]/2
    wl=(weights*(1-tau)[None,:]).sum(axis=1)
    wr=(weights*tau[None,:]).sum(axis=1)
    return wl@f[:-1]+wr@f[1:]

def exponent_fractional_H(alpha,u,T,order,Hfun):
    solver.ALPHA=alpha
    r,w=solver.jacobi(order,-alpha,0.)
    lag=T*(1-r)
    kernel=np.full_like(r,V0)
    for k in range(1,45):
        kernel+=(V0-THETA)*(-LAM)**k*math.gamma(1-alpha)/math.gamma(1+k*ALPHA0-alpha)*lag**(k*ALPHA0)
    H=Hfun(NU*(T*r)**alpha)
    return T**(1-alpha)/(NU*math.gamma(2-alpha))*((kernel*w)[:,None]*H).sum(axis=0)

def pade_exponent(alpha,u,T,order):
    solver.ALPHA=alpha
    def Hfun(y):return np.column_stack([solver.pade(y,float(v)) for v in u])
    return exponent_fractional_H(alpha,u,T,order,Hfun)

def prices(phi,u,w,k):
    phase=np.exp(-1j*u[:,None]*np.log(k)[None,:])
    return 1-np.sqrt(k)/math.pi*((w/(u*u+.25))[:,None]*(phi[:,None]*phase).real).sum(axis=0)

def calculate(alpha,n,order=8,T=.5,extra=False):
    started=time.monotonic();u,w=fourier_grid(order)
    rows=[r for r in json.loads((BASE/'normalized-quote-bands.json').read_text(encoding='utf-8'))['rows'] if float(r['T_decimal_input'])==T]
    k=np.array([float(Fraction(r['moneyness_fraction'])) for r in rows])
    target=np.array([float(r['price_mid_target']['lower_decimal_outward']) for r in rows])
    bid=np.array([float(r['normalized_bid']['lower_decimal_outward']) for r in rows]);ask=np.array([float(r['normalized_ask']['upper_decimal_outward']) for r in rows])
    t,H,f=reference(alpha,u,n,T)
    g=exponent_linear_F(t,f,T,8);g2=exponent_linear_F(t,f,T,16)
    gp=pade_exponent(alpha,u,T,256)
    p=prices(np.exp(g2),u,w,k);pp=prices(np.exp(gp),u,w,k)
    distance=np.maximum(np.maximum(bid-p,p-ask),0)
    out={'alpha':alpha,'T':T,'time_nodes':n+1,'fourier_nodes':len(u),'fourier_order':order,
      'seconds':time.monotonic()-started,'J_mid_12':float(np.mean((p-target)**2)/2),
      'J_band_12':float(np.mean(distance**2)/2),'Pade_J_mid_12':float(np.mean((pp-target)**2)/2),
      'max_price_Pade_minus_reference':float(np.max(abs(pp-p))),
      'max_exponent_time_quadrature_refinement_difference':float(np.max(abs(g2-g))),
      'max_Re_Fbar_nodes':float(np.max(f.real)),'max_Re_H_nodes':float(np.max(H.real)),
      'minimum_Re_Fbar_nodes':float(np.min(f.real)),
      'phi_abs_at_largest_fourier_node':float(abs(np.exp(g2[-1]))),
      'normalized_reference_calls':p.tolist(),'normalized_Pade_calls':pp.tolist(),
      'normalized_price_mid_targets':target.tolist(),'K':[r['K_decimal_input'] for r in rows],
      'bid':bid.tolist(),'ask':ask.tolist()}
    if extra:
        # Independent exponent identity applied to the stored reference H curve.
        def Hfun(y):
            ygrid=NU*t**alpha
            return np.column_stack([np.interp(y,ygrid,H[:,j].real)+1j*np.interp(y,ygrid,H[:,j].imag) for j in range(len(u))])
        gi=exponent_fractional_H(alpha,u,T,512,Hfun)
        out['max_reference_exponent_identity_interpolation_difference']=float(np.max(abs(gi-g2)))
        out['price_reference_identity_difference']=float(np.max(abs(prices(np.exp(gi),u,w,k)-p)))
        gp2=pade_exponent(alpha,u,T,512)
        out['Pade_fractional_quadrature_refinement_price_difference']=float(np.max(abs(prices(np.exp(gp2),u,w,k)-pp)))
    return out

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    parser=argparse.ArgumentParser();parser.add_argument('--n',type=int,default=1024)
    parser.add_argument('--order',type=int,default=8);parser.add_argument('--alphas',default='.52,.5286,.54,.56,.58,.6,.62,.65,.7,.75,.8,.85,.9')
    parser.add_argument('--T',type=float,default=.5);parser.add_argument('--extra',action='store_true')
    parser.add_argument('--output',default='price-profile-diagnostic.json');args=parser.parse_args()
    reports=[]
    for alpha in map(float,args.alphas.split(',')):
        r=calculate(alpha,args.n,args.order,args.T,args.extra);reports.append(r)
        print('alpha',alpha,'Jmid',r['J_mid_12'],'Jband',r['J_band_12'],'Padediff',r['max_price_Pade_minus_reference'],'ReFmax',r['max_Re_Fbar_nodes'],'seconds',r['seconds'],flush=True)
    result={'status':'FLOAT_DIAGNOSTIC_NOT_MODEL_PRICE_OR_CALIBRATION_CERTIFICATE',
      'scope':'declared first-maturity twelve-quote diagnostic; not primary 48-quote objective',
      'curve':'fixed alpha0=.5286,V0=.0262,theta=.0721,lambda_xi=.5037',
      'rho':RHO,'nu':NU,'kappa':0.,'frequency_truncation':200.,'reports':reports}
    (BASE/args.output).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':main()
