"""OFFLINE FLOAT DIAGNOSTICS ONLY; no interval or continuous-domain certificate.

Implicit product integration interpolates F(H) linearly in physical x.  The grid
is uniform in y=x**alpha, with requested maturity nodes inserted exactly.
The [3/3] is the frozen GR six-condition matrix, not a fitted rational curve.
Caputo residual is independently integrated by Gauss-Jacobi in the y variable.
"""
from pathlib import Path
import argparse, json, math, time, sys
import numpy as np

ALPHA, RHO, NU, KAPPA = .5286, -.7445, .2897, 0.
MATURITIES = np.array([.20083, .28909, .35794, .41658, .42])
U = np.array([0., .1, .25, .5, 1., 2., 3., 5., 10., 20., 50., 100., 200.])


def coefficients(u):
    c = -(u*u+.25)/2
    d = RHO/2 - KAPPA + 1j*RHO*u
    A = np.sqrt(d*d-2*c+0j)
    R = A+d
    b1 = c/math.gamma(1+ALPHA)
    b2 = d*c/math.gamma(1+2*ALPHA)
    b3 = math.gamma(1+2*ALPHA)/math.gamma(1+3*ALPHA)*(d*b2+b1*b1/2)
    g0 = -R
    g1 = R/(A*math.gamma(1-ALPHA))
    g2 = -R/(A*A*math.gamma(1-2*ALPHA))+R*R/(2*A**3*math.gamma(1-ALPHA)**2)
    matrix = np.array([[g0,g1,g2],[b1,-g0,-g1],[b2,b1,-g0]],complex)
    raw_delta = np.linalg.det(matrix)
    q = np.linalg.solve(matrix,np.array([b1,-b2,-b3]))
    p = np.array([0,b1,b2+b1*q[0],g0*q[2]])
    defect = abs(p[3]-(b3+b2*q[0]+b1*q[1]))
    return p,np.r_[1,q],c,d,raw_delta,defect


def pade(y,u,derivative=False):
    p,q,*_ = coefficients(u)
    P=np.polynomial.polynomial.polyval(y,p)
    Q=np.polynomial.polynomial.polyval(y,q)
    if not derivative:return P/Q
    dp=np.polynomial.polynomial.polyval(y,np.arange(1,4)*p[1:])
    dq=np.polynomial.polynomial.polyval(y,np.arange(1,4)*q[1:])
    return (dp*Q-P*dq)/(Q*Q)


def integration_weights(t,previous):
    """Exact analytic linear interpolation weights, evaluated in binary64."""
    left=previous[:-1];h=np.diff(previous);tau=t-left;z=h/tau
    I0=(tau**ALPHA-(tau-h)**ALPHA)/ALPHA
    wr=(tau*I0-(tau**(ALPHA+1)-(tau-h)**(ALPHA+1))/(ALPHA+1))/h
    wl=I0-wr
    small=z<1e-3
    if np.any(small):
        zs=z[small];coef=np.ones_like(zs);sr=np.zeros_like(zs);sl=np.zeros_like(zs)
        for k in range(5):
            sr+=coef/(k+2);sl+=coef/((k+1)*(k+2))
            coef*=zs*(1-ALPHA+k)/(k+1)
        factor=tau[small]**(ALPHA-1)*h[small]
        wr[small]=factor*sr;wl[small]=factor*sl
    wr[-1]=h[-1]**ALPHA/(ALPHA*(ALPHA+1))
    wl[-1]=ALPHA*wr[-1]
    return wl/math.gamma(ALPHA),wr/math.gamma(ALPHA)


def reference(n):
    y=np.unique(np.r_[np.linspace(0,.42,n+1),MATURITIES])
    x=y**(1/ALPHA)
    H=np.zeros((len(x),len(U)),complex)
    c=-(U*U+.25)/2
    d=RHO/2+1j*RHO*U
    f=np.zeros_like(H);f[0]=c
    started=0
    for j in range(1,len(x)):
        wl,wr=integration_weights(x[j],x[:j+1])
        history=wl@f[:j]+wr[:-1]@f[1:j]
        w=wr[-1];g=history+w*c;B=1-w*d
        H[j]=2*g/(B+np.sqrt(B*B-2*w*g))
        f[j]=c+d*H[j]+H[j]*H[j]/2
        if j%(max(1,len(x)//4))==0:
            print('reference',n,'step',j,'elapsed',round(0-started,2),flush=True)
    assert np.all(np.isfinite(H))
    ids=np.searchsorted(y,MATURITIES)
    return y,H,H[ids],{'nodes':len(x),'max_ReH':float(np.max(H.real))}


def jacobi(n,a,b):
    k=np.arange(n,dtype=float)
    diag=(b*b-a*a)/((2*k+a+b)*(2*k+a+b+2))
    k=np.arange(1,n,dtype=float)
    off=2/(2*k+a+b)*np.sqrt(k*(k+a)*(k+b)*(k+a+b)/((2*k+a+b-1)*(2*k+a+b+1)))
    matrix=np.diag(diag)+np.diag(off,1)+np.diag(off,-1)
    nodes,vectors=np.linalg.eigh(matrix)
    return (nodes+1)/2,vectors[0]**2


def residual(u,y,n):
    r,w=jacobi(n,-ALPHA,0.)
    ratio=-np.expm1(np.log(r)/ALPHA)/(1-r)
    factor=ratio**(-ALPHA)
    p,q,c,d,*_=coefficients(u)
    # Subtract constant derivative, whose weighted integral is known exactly.
    deriv=pade(y[:,None]*r[None,:],u,True)-p[1]
    dc=c+(deriv*(factor*w)[None,:]).sum(axis=1)/math.gamma(2-ALPHA)
    H=pade(y,u)
    return dc-(c+d*H+H*H/2)


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    parser=argparse.ArgumentParser()
    parser.add_argument('--n',type=int,default=2048)
    parser.add_argument('--quad',type=int,default=128)
    args=parser.parse_args()
    y,H,v,meta=reference(args.n)
    y2,H2,v2,meta2=reference(2*args.n)
    refined_on_coarse=np.column_stack([np.interp(y,y2,H2[:,k].real)+1j*np.interp(y,y2,H2[:,k].imag) for k in range(len(U))])
    reports=[]
    for j,u in enumerate(U):
        p,q,c,d,delta,defect=coefficients(u)
        yh=np.unique(np.r_[0.,np.geomspace(1e-8,.42,350),np.linspace(0,.42,200)])
        hp=pade(yh,u)
        rd1=residual(u,yh,args.quad);rd2=residual(u,yh,2*args.quad)
        Q=np.polynomial.polynomial.polyval(yh,q)
        ph=pade(MATURITIES,u);er=abs(ph-v2[:,j])
        reports.append({'u':float(u),'raw_delta_abs':float(abs(delta)),
          'matrix_transcription_defect':float(defect),'q':[[float(z.real),float(z.imag)] for z in q],
          'grid_min_abs_Q_scaled':float(np.min(abs(Q)/(1+yh)**3)),
          'grid_max_Re_Pade':float(np.max(hp.real)),
          'grid_max_Re_reference':float(np.max(H2[:,j].real)),
          'reference_refinement_max_difference':float(np.max(abs(refined_on_coarse[:,j]-H[:,j]))),
          'pade_residual_max':float(np.max(abs(rd2))),
          'residual_quadrature_refinement_max_difference':float(np.max(abs(rd2-rd1))),
          'residual_peak_y':float(yh[np.argmax(abs(rd2))]),
          'maturity_errors_H':er.tolist(),
          'reference_maturity_H':[[float(z.real),float(z.imag)] for z in v2[:,j]],
          'pade_maturity_H':[[float(z.real),float(z.imag)] for z in ph]})
    data={'status':'FLOAT_DIAGNOSTIC_ONLY_NOT_A_CERTIFICATE','method':'implicit linear-F fractional product integration on a y-grid; independent rational Caputo quadrature',
      'parameters':{'alpha':ALPHA,'rho':RHO,'nu':NU,'kappa':KAPPA},'Y':MATURITIES.tolist(),
      'physical_T':((MATURITIES/NU)**(1/ALPHA)).tolist(),'reference':meta,'reference_refined':meta2,'reports':reports}
    target=Path(__file__).with_name('solver-diagnostic.json')
    target.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    np.savez_compressed(Path(__file__).with_name('reference-trajectories.npz'),y=y2,H=H2,u=U)
    print('SAVED',target,flush=True)
    for r in reports:
        print('u',r['u'],'refine',r['reference_refinement_max_difference'],
              'errorYmax',r['maturity_errors_H'][-1],'res',r['pade_residual_max'],
              'quad',r['residual_quadrature_refinement_max_difference'],
              'RePade',r['grid_max_Re_Pade'],flush=True)


if __name__=='__main__':main()
