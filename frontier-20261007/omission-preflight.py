"""Freeze the expanded-reference experiment before new financial results."""
from pathlib import Path
from fractions import Fraction as Q
import datetime,hashlib,json,platform,os,sys,time
HERE=Path(__file__).resolve().parent;BASE=HERE.parent/'english-heston-release';FROZEN=BASE/'code/frozen'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def main():
    start=time.perf_counter();HERE.mkdir(exist_ok=True)
    names=['fixed-field-betap52-u128.npz','fixed-field-betap52-u128.json','fixed-field-betap52-u128-exponent-certificate.json',
           'field-residual-certificate-point052-v3-u64.json','f8-price-point052-v3-u64.json','frozen-pade-numeric-output.json']
    manifest={r['path']:r['sha256'] for r in load(BASE/'code/MANIFEST.json')['artifacts']}
    for name in names:assert sha(FROZEN/name)==manifest['code/frozen/'+name]
    contract={'contract_id':'same-fast-output-alpha052-extended-reference-u128-v1','written_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'frozen_before_new_high_frequency_financial_results':True,'known_baseline':'Earlier u<=64 reference with deliberate finite omissions; finite-history/time-bin bounds and known 1/.5/.25-point budgets are disclosed prior evidence.',
              'alpha':'13/25','T':'1/2','strikes':['4400','4500'],'weights':['1','-1'],'h':'1/8',
              'fast_output':'Unchanged original saved actual Padé u<=64 output; no solver refit and no changed fast implementation.',
              'reference':'Original exact stored fixed-field-betap52-u128 function, now nonzero reference transform at all 1025 nodes through128.',
              'new_reference_requires_new_signed_center':True,'old_omitted_CF_radius_not_reusable_as_new_reference_error':True,
              'node_radius_rule':'At a newly nonzero node use certified exponent-to-CF error or B_true+|phi_reference|. The old true-minus-zero radius by itself is invalid.',
              'retained_remainders':['original analytic strip','original true infinite tail beyond128','outward new reference arithmetic'],
              'budgets_index_points':['1','1/2','1/4'],'source_sha256':{name:sha(FROZEN/name) for name in names},
              'resource_preapproval':{'status':'ACCEPTED_WITHIN_AUTHORIZED_RESEARCH','maximum_peak_working_set_bytes':1073741824,
                  'initial_plan':'Inspect saved full-node residuals first; if absent/insufficient, certify only newly used512 frequencies over every closed time cell of the unchanged field. Pin BLAS/OMP threads; measure parent cold wall and peak working set.',
                  'no_user_confirmation_required':True},
              'failure_policy':'Retain failed budgets and half-plane/residual failures. No inferred true pricing bias, profitability, minimum runtime or zero-cost receipt generation.'}
    target=HERE/'omission-contract.json'
    if target.exists():raise FileExistsError('Prospective contract already exists; preserve it')
    target.write_text(json.dumps(contract,indent=2)+'\n')
    import numpy as np
    with np.load(FROZEN/names[0],allow_pickle=False) as ar:
        assert ar['u'].shape==(1025,) and np.array_equal(ar['u'],np.arange(1025)/8)
        assert ar['t'].shape==(2049,) and ar['LG'].shape==(2049,1025)
        assert ar['t'][0]==0 and ar['t'][-1]==.5 and np.all(ar['LG'][0]==0)
        field={'nodes':len(ar['u']),'maximum_u':float(ar['u'][-1]),'time_nodes':len(ar['t']),
               'arrays_uncompressed_bytes':sum(ar[k].nbytes for k in ar.files)}
    sources=[]
    roots=[FROZEN,HERE.parent/'pade-calibration-20261006']
    for root in roots:
        for p in sorted(root.glob('*residual*052*.json')):
            d=load(p)
            sources.append({'path':str(p.relative_to(HERE.parent)).replace('\\','/'),'sha256':sha(p),
                            'status':d.get('status'),'field_sha256':d.get('field_sha256'),
                            'u_count':len(d.get('u',d.get('cover',[]))),
                            'u_maximum':max(d.get('u',[float(Q(r['u'])) for r in d.get('cover',[])]),default=None),
                            'alpha_exact':d.get('alpha_exact',d.get('alpha_lower')),
                            'halfplane_certified':d.get('approx_left_halfplane_certified'),
                            'has_complete_physical_residual':bool(d.get('delta_physical_upper_exact_dyadics')),
                            'has_startup_halfplane':bool(d.get('first_cell_Re_H_div_talpha_upper_exact_dyadics')),
                            'has_later_halfplane':bool(d.get('later_cells_Re_H_upper_exact_dyadics')),
                            'continuous_closed_cells':d.get('certified_closed_subintervals'),'recorded_phase_seconds':d.get('seconds')})
    payload={'status':'PASS_CONTRACT_FROZEN_AND_EXISTING_EVIDENCE_INVENTORIED','contract_sha256':sha(target),'field':field,
             'existing_residual_sources':sources,'python':platform.python_version(),'numpy':np.__version__,
             'existing_thread_environment':{k:os.environ.get(k) for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']},
             'wall_seconds':time.perf_counter()-start,'scope':'Read-only inventory and prospective contract; no new financial bound computed.'}
    (HERE/'omission-preflight.json').write_text(json.dumps(payload,indent=2)+'\n');print(json.dumps(payload,indent=2))
if __name__=='__main__':main()
