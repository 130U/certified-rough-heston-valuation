"""Rigorous integral/exponential of an exact stored field, not true CF accuracy.

All decisions use 100-bit integer dyadic intervals.  Node phi enclosures here
are for exp(Lbar), where Lbar integrates the stored continuous field.  They
must be combined with a separately certified residual before true pricing.
"""
from pathlib import Path
from fractions import Fraction as F
import importlib.util, argparse, json, hashlib, sys
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
