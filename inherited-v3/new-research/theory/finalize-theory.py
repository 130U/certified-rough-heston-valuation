"""Build deterministic mathematical receipts without execution metadata."""
from pathlib import Path
from fractions import Fraction as F
import gzip, hashlib, importlib.util, json
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('rho_generator',HERE/'rho-cover.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
source=json.loads(gzip.decompress((HERE/'legacy-compact-cover.json.gz').read_bytes()))
attempt=json.loads(gzip.decompress((HERE/'rho-cover.json.gz').read_bytes()))
lb,ld=mod.lipschitz_constants()
bm=list(map(F,source['B_uniform_lower']))
dm=list(map(F,source['negative_D_uniform_lower']))
h=min([mod.HALF_WIDTH]+[m/(2*l) for m,l in zip(bm+dm,lb+ld)])
dyadic_h=F(1)
dyadic_exponent=0
while dyadic_h>h:
    dyadic_h/=2
    dyadic_exponent+=1
receipt=dict(
    status='PASS_CONTINUOUS_NONZERO_RHO_FALLBACK',
    rho_centre=str(mod.CENTRE),rho_half_width=str(h),
    rho_interval=list(map(str,(mod.CENTRE-h,mod.CENTRE+h))),
    interval_width=str(2*h),alpha=['13/25','3/5'],kappa='0',
    eta=['0','1'],frequency='all real frequencies by compactification and conjugacy',
    readable_dyadic_half_width=str(dyadic_h),readable_dyadic_exponent=dyadic_exponent,
    readable_dyadic_interval=list(map(str,(mod.CENTRE-dyadic_h,mod.CENTRE+dyadic_h))),
    B_uniform_extended_lower=[str(m-l*h) for m,l in zip(bm,lb)],
    negative_D_uniform_extended_lower=[str(m-l*h) for m,l in zip(dm,ld)],
    B_rho_lipschitz=list(map(str,lb)),D_rho_lipschitz=list(map(str,ld)),
    upstream_sha256=hashlib.sha256((HERE/'legacy-compact-cover.json.gz').read_bytes()).hexdigest(),
    primary_attempt_sha256=hashlib.sha256((HERE/'rho-cover.json.gz').read_bytes()).hexdigest(),
    protocol_sha256=hashlib.sha256((HERE/'rho-protocol.json').read_bytes()).hexdigest(),
    primary_attempt_status=attempt['status'],
    primary_half_width=str(mod.HALF_WIDTH),
    primary_unresolved_area=attempt['exact_unresolved_area'],
    primary_refined_evaluations=attempt['refined_evaluations'],
    primary_protocol_deviation='The first generator applied the work limit at its next failing leaf, causing one additional evaluation beyond 150000. No complete-domain claim is made from that partial attempt.',
    scope='The certified nonzero strip is a conservative persistence result, not a practical broad calibration domain and not a new price certificate at another correlation.')
assert all(F(s)>0 for s in receipt['B_uniform_extended_lower']+receipt['negative_D_uniform_extended_lower'])
(HERE/'rho-fallback.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:receipt[k] for k in ('status','rho_half_width','interval_width','primary_unresolved_area')}))
