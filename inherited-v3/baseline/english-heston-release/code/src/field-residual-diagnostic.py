"""Continuous I^alpha Fbar representation sampled inside every cell; floats only.

Compare ordinary physical-x-linear Fbar and singularity-corrected Fbar.
The latter subtracts the exact x^alpha and x^(2alpha) Taylor terms before
interpolating the remainder.  All residuals reported here are diagnostic,
not certified suprema.  Reference values at the nodes solve an implicit
quadratic, with the same branch selected as in the ordinary solver.
"""
from pathlib import Path
import importlib.util, argparse, json, math, time, sys
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

def residuals(alpha,u,n,T,corrected,fractions):
    started=0;x,y,H,f,field,co=solve(alpha,u,n,T,corrected)
    c,d,b1,b2,b3,a1,a2=co
    maximum=np.zeros(len(u));first=np.zeros(len(u));where=np.zeros(len(u))
    max_Re_field=np.max(f.real,axis=0);max_Re_H=np.zeros(len(u));node_defect=np.zeros(len(u))
    for j in range(n):
        h=x[j+1]-x[j]
        for theta in fractions:
            t=x[j]+theta*h;yt=t**alpha
            evfield=field[j]+theta*(field[j+1]-field[j])
            if theta==1:
                wl,wr=solver.integration_weights(t,x[:j+2])
                linear=wl@field[:j+1]+wr@field[1:j+2]
            else:
                wl,wr=weights_partial(t,x[:j+1])
                linear=wl@field[:j+1]+wr[:-1]@field[1:j+1]+wr[-1]*evfield
            if corrected:
                HH=b1*yt+b2*yt**2+b3*yt**3+linear
                FF=c+a1*yt+a2*yt**2+evfield
            else:HH=linear;FF=evfield
            r=FF-(c+d*HH+HH*HH/2);ar=abs(r)
            take=ar>maximum;maximum[take]=ar[take];where[take]=yt
            if j==0:first=np.maximum(first,ar)
            if theta==1:node_defect=np.maximum(node_defect,abs(HH-H[j+1]))
            max_Re_field=np.maximum(max_Re_field,FF.real);max_Re_H=np.maximum(max_Re_H,HH.real)
    return {'alpha':alpha,'n':n,'T':T,'startup_corrected':corrected,
      'sample_fractions_per_cell':fractions,
      'u':u.tolist(),'sample_global_residual_max':maximum.tolist(),
      'sample_first_cell_residual_max':first.tolist(),'sample_peak_y':where.tolist(),
      'sample_max_Re_field':max_Re_field.tolist(),'sample_max_Re_H':max_Re_H.tolist(),
      'node_integral_identity_defect':node_defect.tolist(),
      'endpoint_H':[[float(z.real),float(z.imag)] for z in H[-1]],
      'physical_time_nodes':(x/NU**(1/alpha)).tolist()}

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    parser=argparse.ArgumentParser();parser.add_argument('--alpha',type=float,default=.5286)
    parser.add_argument('--n',type=int,default=512);parser.add_argument('--T',type=float,default=.5)
    parser.add_argument('--u',default='0,1,3,5,10,20,50,100,200')
    parser.add_argument('--output',default='field-residual-diagnostic.json');args=parser.parse_args()
    u=np.array(list(map(float,args.u.split(','))));reports=[]
    for corrected in [False,True]:
        r=residuals(args.alpha,u,args.n,args.T,corrected,[.125,.25,.5,.75,.875,1.]);reports.append(r)
        print('corrected', corrected, flush=True)
        for j,v in enumerate(u):print('u',v,'first',r['sample_first_cell_residual_max'][j],'all',r['sample_global_residual_max'][j],'ReFmax',r['sample_max_Re_field'][j],flush=True)
    (BASE/args.output).write_text(json.dumps({'status':'FLOAT_SAMPLES_NOT_A_SUPREMUM_CERTIFICATE','reports':reports},indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':main()
