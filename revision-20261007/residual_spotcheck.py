"""Regenerate continuous closed-time residuals for two real frequency nodes.

This reuses the continuous-field generator; it never calls the numerical solver.
The selected frequencies are not a complete Fourier certificate.
"""
from __future__ import annotations
from fractions import Fraction as Q
from pathlib import Path
import importlib.util,json,sys,time
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
from audit_paths import release_root
RELEASE=release_root(HERE)
SRC=RELEASE/'code'/'src';FROZEN=RELEASE/'code'/'frozen'

def main():
    sp=importlib.util.spec_from_file_location('fresh_residual',SRC/'certify-field-residual-v3.py')
    mod=importlib.util.module_from_spec(sp);sys.modules['fresh_residual']=mod;sp.loader.exec_module(mod)
    started=time.perf_counter();records=[]
    for alpha,stem,rawname in [
        ('13/25','fixed-field-betap52-u128','field-residual-certificate-point052-v3-u64.json'),
        ('3/5','fixed-field-betap6-u128','field-residual-certificate-point06-v3-u64.json'),
        ('9/10','fixed-field-betap9-u80','field-residual-betap9-u64-v3.json')]:
        before=time.perf_counter()
        fresh=mod.certify(FROZEN/(stem+'.npz'),Q(alpha),.125,4,32)
        raw=json.loads((FROZEN/rawname).read_text(encoding='utf-8'))
        mathematical_keys=['alpha_exact','beta_exact','T_exact','nu_exact','field_sha256','split',
                           'certified_closed_subintervals','first_cell_method','residual_definition',
                           'source_sha256','polynomial_startup_cancellation','combined_derivative_source_sha256',
                           'approx_left_halfplane_certified']
        assert all(fresh[k]==raw[k] for k in mathematical_keys),'mathematical contract mismatch'
        endpoints=['delta_physical_upper_exact_dyadics','first_cell_physical_upper_exact_dyadics',
                   'first_cell_Re_H_div_talpha_upper_exact_dyadics','later_cells_Re_H_upper_exact_dyadics']
        equality={k:fresh[k]==raw[k][:2] for k in endpoints}
        for k in endpoints:
            assert all(Q(a)<=Q(b) for a,b in zip(fresh[k],raw[k][:2])),('fresh enclosure exceeds frozen bound',k)
        filename='fresh-residual-alpha-'+alpha.replace('/','_')+'-u0125.json'
        (HERE/filename).write_text(json.dumps(fresh,indent=2)+'\n',encoding='utf-8')
        rec={'alpha':alpha,'frequency_nodes':fresh['u'],'closed_time_intervals':fresh['certified_closed_subintervals'],
             'all_endpoint_arrays_exactly_match':equality,'fresh_enclosures_within_frozen':True,
             'wall_seconds':time.perf_counter()-before,'result_file':filename}
        records.append(rec);print(json.dumps(rec,indent=2),flush=True)
    result={'status':'PASS_FRESH_CONTINUOUS_RESIDUAL_TWO_NODE_SPOTCHECK','records':records,
            'scope':'Entire [0,1/2] closed-time cover for u=0,1/8 only in each of three fixed fields. Same continuous generator, no solver-update diagnostics. Not a full 513-node replay.',
            'wall_seconds':time.perf_counter()-started}
    (HERE/'residual-spotcheck.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':main()
