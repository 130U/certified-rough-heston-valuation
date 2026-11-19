"""Continuous I^alpha Fbar representation sampled inside every cell; floats only.

Compare ordinary physical-x-linear Fbar and singularity-corrected Fbar.
The latter subtracts the exact x^alpha and x^(2alpha) Taylor terms before
interpolating the remainder.  All residuals reported here are diagnostic,
not certified suprema.  Reference values at the nodes solve an implicit
quadratic, with the same branch selected as in the ordinary solver.
"""
from pathlib import Path
import importlib.util, argparse, json, math, sys
import numpy as np

BASE=Path(__file__).parent
spec=importlib.util.spec_from_file_location('solver',BASE/'solver-diagnostic.py')
solver=importlib.util.module_from_spec(spec);spec.loader.exec_module(solver)
NU=.2897;RHO=-.7445

def solve(alpha,u,n,T,corrected):
    solver.ALPHA=alpha
    y=np.linspace(0,NU*T**alpha,n+1);x=y**(1/alpha)
    c=-(u*u+.25)/2;d=RHO/2+1j*RHO*u
    b1=c/math.gamma(1+alpha);b2=d*c/math.gamma(1+2*alpha)
    a1=d*b1;a2=d*b2+b1*b1/2
    b3=math.gamma(1+2*alpha)/math.gamma(1+3*alpha)*a2
    H=np.zeros((n+1,len(u)),complex);field=np.zeros_like(H)
    f=np.zeros_like(H);f[0]=c
    if not corrected:field[0]=c
    for j in range(1,n+1):
        wl,wr=solver.integration_weights(x[j],x[:j+1]);w=wr[-1]
        history=wl@field[:j]+wr[:-1]@field[1:j]
        if corrected:
            polynomial=b1*y[j]+b2*y[j]**2+b3*y[j]**3
            g=polynomial+history-w*(a1*y[j]+a2*y[j]**2)
        else:g=history+w*c
        B=1-w*d
        H[j]=2*g/(B+np.sqrt(B*B-2*w*g))
        f[j]=c+d*H[j]+H[j]*H[j]/2
        field[j]=f[j]-(c+a1*y[j]+a2*y[j]**2) if corrected else f[j]
    return x,y,H,f,field,(c,d,b1,b2,b3,a1,a2)

def weights_partial(t,grid):
    # Last interval is only partially present; field value at its right endpoint
    # is interpolated from the saved complete interval, outside this function.
    return solver.integration_weights(t,np.r_[grid,t])

