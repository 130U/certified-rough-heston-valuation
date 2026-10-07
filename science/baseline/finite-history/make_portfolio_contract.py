"""Freeze systematic directions before calculating their new outcomes."""
from pathlib import Path
from fractions import Fraction as Q
import hashlib,json
HERE=Path(__file__).resolve().parent
FROZEN=HERE.parent/'reference'/'code'/'frozen'
names=['normalized-quote-bands.json','frozen-pade-numeric-output.json',
       'f8-price-point052-u64.json','f8-price-point06-u64.json','f8-price-betap9-u64-.json']
prices=json.loads((FROZEN/names[2]).read_text())
strikes=[row['K'] for row in prices['rows']]
directions=[]
def direction(name,kind,items):
    weights=[Q(0)]*12
    for index,value in items:weights[index]=Q(value)
    directions.append({'id':name,'kind':kind,'weights':list(map(str,weights)),
                       'active_strikes':[strikes[i] for i,w in enumerate(weights) if w],
                       'gross_units':str(sum(map(abs,weights)))})
for i in range(11):direction('adjacent-spread-'+strikes[i]+'-'+strikes[i+1],'adjacent_spread',[(i,1),(i+1,-1)])
for i in range(10):direction('adjacent-butterfly-'+strikes[i]+'-'+strikes[i+2],'adjacent_butterfly',[(i,1),(i+1,-2),(i+2,1)])
for i,j in [(0,3),(3,6),(6,9),(0,11)]:direction('wide-spread-'+strikes[i]+'-'+strikes[j],'wide_spread',[(i,1),(j,-1)])
for name,indices in [('all',range(12)),('first-half',range(6)),('last-half',range(6,12))]:
    ids=list(indices);direction('positive-basket-'+name,'positive_basket',[(i,Q(1,len(ids))) for i in ids])
contract={'contract_id':'systematic-original-12-strike-portfolios-reference','date':'2026-10-07',
          'freeze_time_utc':'2026-10-07 05:52:04 UTC','new_directions_frozen_before_systematic_results':True,
          'known_before_freeze':'The previously published 4400/4500 spread result and upstream frozen inputs were already known. New systematic outcomes were not calculated.',
          'source_sha256':{name:hashlib.sha256((FROZEN/name).read_bytes()).hexdigest() for name in names},
          'candidates':['13/25','3/5','9/10'],'maturity':'1/2','discount_D':'1','forward_F':'211093/50',
          'normalization':'C/(D F); multiply normalized errors by D F to obtain index points',
          'strikes':strikes,'directions':directions,'point_budgets':['1/4','1/2','1','2'],
          'comparisons':['symmetric_marginal','best_signed_marginal','shared_Fourier','legal_directional_intersection'],
          'intersection_semantics':'Intersect valid directional intervals from the joint set, signed marginal price box and proven true-call payoff bounds. This encloses the actual set intersection; exact intersection support optimization is not claimed.',
          'success_rule':'Exact outward absolute implementation-error upper endpoint <= specified point budget; otherwise NOT_CERTIFIED.',
          'timing_rule':'Report source read, reusable coefficient preparation, each directional support aggregation and each marginal/intersection/decision increment separately. Timings are observations, not performance guarantees.',
          'limitations':['Single unchanged maturity and fixed three candidates.','Bounds improve, not measured actual error or trading loss.','No new residual/field generation.','No inference for additional maturities or nearby alpha values without certificates.']}
target=HERE/'portfolio-contract.json'
if target.exists():raise FileExistsError('Contract already frozen; do not overwrite it.')
target.write_text(json.dumps(contract,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'FROZEN','directions':len(directions),'contract_sha256':hashlib.sha256(target.read_bytes()).hexdigest()}))
