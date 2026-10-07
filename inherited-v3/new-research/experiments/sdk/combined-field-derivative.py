"""Additional strict derivative enclosure, preserving cancellation in Gbar'.

Imported by a separate execution-version only; no existing certificate is
retroactively relabelled.  All arithmetic helpers are the audited outward
interval routines supplied as module M.  First source-cell singularities are
integrated with positive-kernel bounds and a whole-Beta integral cap.
"""
from fractions import Fraction as F
import numpy as np

def value_interval_dot(M,W,V):
    mid=(V[0]+V[1])/2
    rad=M.UP(np.maximum(abs(mid-V[0]),abs(V[1]-mid)))
    center=M.dot_interval(W,mid)
    extra=M.dot_interval(W,rad)[1]
    # W is a positive-kernel enclosure; clip only its known mathematical sign
    # before calling this function, so W*rad has a nonnegative upper bound.
    return M.DN(center[0]-extra),M.UP(center[1]+extra)

def source_intervals(M,t,LG,A1,A2,beta):
    a=t[1:-1];b=t[2:]
    width=M.sub(t[1:],t[:-1])
    sr=M.div(M.sub(LG[1:].real,LG[:-1].real),(width[0][:,None],width[1][:,None]))
    si=M.div(M.sub(LG[1:].imag,LG[:-1].imag),(width[0][:,None],width[1][:,None]))
    Gp=(sr,si)
    re=(Gp[0][0].copy(),Gp[0][1].copy());im=(Gp[1][0].copy(),Gp[1][1].copy())
    rest=((re[0][1:],re[1][1:]),(im[0][1:],im[1][1:]))
    for p,z in [(beta,M.cp(A1)),(2*beta,M.cp(A2))]:
        factor=M.mul(M.power((a,b),M.rational(p-1)),M.rational(p))
        rest=M.cadd(rest,M.cscale(z,(factor[0][:,None],factor[1][:,None])))
    re[0][1:]=rest[0][0];re[1][1:]=rest[0][1]
    im[0][1:]=rest[1][0];im[1][1:]=rest[1][1]
    # First row is treated analytically, not as an infinite derivative box.
    re[0][0]=0.;re[1][0]=0.;im[0][0]=0.;im[1][0]=0.
    return (re,im),(sr[0][0],sr[1][0]),(si[0][0],si[1][0])

def enclosure(M,a,b,t,LG,A1,A2,nu,c,alpha,beta,source=None,weights=None):
    if source is None:source=source_intervals(M,t,LG,A1,A2,beta)
    Gp,sr0,si0=source
    if weights is None:
        wa=M.volterra_weights(a,t,alpha,True);wb=M.volterra_weights(b,t,alpha,True)
        old=t[1:][None,:]<=a[:,None]
        lo=np.where(old,wb[0],wa[0]);hi=np.where(old,wa[1],wb[1])
    else:lo,hi=weights
    W=(np.maximum(lo,0.),np.maximum(hi,0.))
    HP=(value_interval_dot(M,W,Gp[0]),value_interval_dot(M,W,Gp[1]))
    pow0=M.power((a,b),M.rational(alpha-1))
    HP=M.cadd(HP,(M.mul(M.div(M.mul(nu,c),M.gamma(alpha)),(pow0[0][:,None],pow0[1][:,None])),M.pair(np.zeros_like(HP[0][0]))))
    # Add the first source cell's constant LG slope contribution.
    w0=(W[0][:,0,None],W[1][:,0,None])
    HP=M.cadd(HP,(M.mul(w0,sr0),M.mul(w0,si0)))
    t1=t[1]
    for p,z in [(beta,M.cp(A1)),(2*beta,M.cp(A2))]:
        mass=M.div(M.power(np.asarray([t1]),M.rational(p)),M.mul(M.rational(p),M.gamma(alpha)))
        low=M.mul(mass,M.power(b,M.rational(alpha-1)))[0]
        # Whole positive Beta integral: integral_0^q s^(p-1)(q-s)^(alpha-1)/Gamma(alpha).
        whole=M.mul(M.div(M.gamma(p),M.gamma(alpha+p)),M.power((a,b),M.rational(alpha+p-1)))[1]
        ker=np.full_like(a,np.inf);take=a>t1
        if np.any(take):
            delta=M.sub(a[take],t1)
            ker[take]=M.mul(mass,M.power(delta,M.rational(alpha-1)))[1]
        upper=np.minimum(ker,whole)
        Ip=(low,upper)
        contribution=M.cscale(z,(M.mul(M.rational(p),Ip)[0][:,None],M.mul(M.rational(p),Ip)[1][:,None]))
        HP=M.cadd(HP,contribution)
    return HP
