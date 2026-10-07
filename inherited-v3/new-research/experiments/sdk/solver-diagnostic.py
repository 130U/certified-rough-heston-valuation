"""OFFLINE FLOAT DIAGNOSTICS ONLY; no interval or continuous-domain certificate.

Implicit product integration interpolates F(H) linearly in physical x.  The grid
is uniform in y=x**alpha, with requested maturity nodes inserted exactly.
The [3/3] is the frozen GR six-condition matrix, not a fitted rational curve.
Caputo residual is independently integrated by Gauss-Jacobi in the y variable.
"""
from pathlib import Path
import argparse, json, math, sys
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


def jacobi(n,a,b):
    k=np.arange(n,dtype=float)
    diag=(b*b-a*a)/((2*k+a+b)*(2*k+a+b+2))
    k=np.arange(1,n,dtype=float)
    off=2/(2*k+a+b)*np.sqrt(k*(k+a)*(k+b)*(k+a+b)/((2*k+a+b-1)*(2*k+a+b+1)))
    matrix=np.diag(diag)+np.diag(off,1)+np.diag(off,-1)
    nodes,vectors=np.linalg.eigh(matrix)
    return (nodes+1)/2,vectors[0]**2


