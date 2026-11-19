"""Freeze a self-written startup-corrected physical-time field as binary dyadics.

The NPZ is DATA ONLY.  It does not certify a solver or its residual.  A reader
must interpret each finite binary64 real/imaginary array component exactly, not
as a decimal estimate; array endpoints and coefficients thereby define a fixed
continuous field Gbar(t) for I^alpha Gbar at any candidate alpha.
"""
from pathlib import Path
import importlib.util, argparse, hashlib, json, sys
import numpy as np

BASE=Path(__file__).parent
spec=importlib.util.spec_from_file_location('field',BASE/'field-residual-diagnostic.py')
field=importlib.util.module_from_spec(spec);spec.loader.exec_module(field)

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    parser=argparse.ArgumentParser();parser.add_argument('--beta',default='.52')
    parser.add_argument('--n',type=int,default=2048);parser.add_argument('--U',type=int,default=64)
    args=parser.parse_args();beta=float(args.beta);u=np.arange(0,args.U+.0625,.125)
    x,y,H,f,L,co=field.solve(beta,u,args.n,.5,True)
    c,d,b1,b2,b3,a1,a2=co
    t=x/field.NU**(1/beta);t[0]=0.;t[-1]=.5
    # Exact interpretation after storage: Gbar=nu*c+A1*t^beta+A2*t^(2beta)+LGlin.
    A1=(field.NU**2)*a1;A2=(field.NU**3)*a2;LG=field.NU*L
    out=BASE/('fixed-field-beta'+args.beta.replace('.','p')+'-u'+str(args.U)+'.npz')
    if out.exists():raise FileExistsError('Frozen fields are immutable: choose a new output generation name.')
    np.savez_compressed(out,t=t,u=u,A1=A1,A2=A2,LG=LG)
    assert np.all(np.isfinite(LG)) and np.all(np.diff(t)>0)
    meta={'status':'FROZEN_BINARY64_DYADIC_FIELD_DATA_NOT_RESIDUAL_CERTIFICATE',
      'beta_exact_decimal':args.beta,'T':'1/2','frequency_step':'1/8','frequency_upper':args.U,
      'nu_exact':'2897/10000','rho_exact':'-1489/2000','kappa_exact':'0',
      'c_exact':'-(u^2+1/4)/2','field_definition':'Gbar(t)=nu*c+A1*t^beta+A2*t^(2*beta)+linear_interpolant(t_nodes,LG_nodes)',
      'candidate_curve_definition':'Hhat_alpha(t)=I_t^alpha Gbar(t); D_C^alpha Hhat_alpha=Gbar',
      'coefficient_interpretation':'every NPZ binary64 component is the exact dyadic rational float.as_integer_ratio(); t^beta retains the exact rational beta, not binary64 beta',
      'construction_diagnostic':'implicit quadratic PI with first two singular field terms removed before physical-time linear interpolation',
      'arrays':{'t':list(t.shape),'u':list(u.shape),'A1':list(A1.shape),'A2':list(A2.shape),'LG':list(LG.shape)},
      'initial_LG_exact_zero':bool(np.all(LG[0]==0)),
      't_last_exact_half':bool(t[-1]==.5),'t_first_exact_zero':bool(t[0]==0),
      'file':out.name,'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
      'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'solver_sha256':hashlib.sha256((BASE/'field-residual-diagnostic.py').read_bytes()).hexdigest()}
    out.with_suffix('.json').write_text(json.dumps(meta,indent=2)+'\n',encoding='utf-8')
    print('SAVED',out.name,'nodes',len(t),'frequencies',len(u),'bytes',meta['bytes'],flush=True)

if __name__=='__main__':main()
