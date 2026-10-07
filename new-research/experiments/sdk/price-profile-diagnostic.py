"""Self-written offline numerical prices, explicitly NOT certified model prices.

Reference: implicit product integration; forward-variance curve frozen at alpha0.
Rational comparison: characteristic exponent defined using D^alpha Hhat, via an
equivalent fractional convolution kernel; never substitutes F(Hhat) for D Hhat.
The first twelve T=.5 quotes are a declared preliminary subset, not the full
48-quote contract's primary objective.
"""
from pathlib import Path
from fractions import Fraction
import argparse, importlib.util, json, math, sys
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

