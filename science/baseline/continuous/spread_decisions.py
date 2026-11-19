"""Exact point-budget decisions, including honest uncertified outcomes."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib,json,sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
from audit_paths import release_root
FROZEN=release_root(HERE)/'code'/'frozen'
def main():
    contract=json.loads((HERE/'spread-decision-contract.json').read_text())
    joint=json.loads((HERE/'shared-fourier-spread.json').read_text())
    pade=json.loads((FROZEN/'frozen-pade-numeric-output.json').read_text())
    scale=Q(contract['DF']);budgets=[Q(contract['primary_absolute_implementation_budget_index_points'])]+list(map(Q,contract['additional_sensitivity_budgets_index_points']))
    rows=[]
    for result in joint['results']:
        alpha=Q(result['alpha']);price=json.loads((FROZEN/result['source']).read_text())
        fast={r['row_id']:Q(r['normalized_call_exact_dyadic']) for c in pade['cover'] if Q(c['alpha'])==alpha for r in c['rows']}
        selected=[r for r in price['rows'] if r['K'] in ['4400','4500']]
        symmetric=sum((max(abs(Q(v)-fast[r['row_id']]) for v in r['true_normalized_price']) for r in selected),Q(0))
        bounds={'symmetric_marginal':symmetric,'best_signed_marginal':Q(result['best_signed_marginal_absolute_error_upper']),
                'shared_fourier_joint':Q(result['joint_actual_fast_absolute_error_upper'])}
        rows.append({'alpha':str(alpha),'error_bounds_normalized_exact':{k:str(v) for k,v in bounds.items()},
            'error_bounds_index_points_exact':{k:str(v*scale) for k,v in bounds.items()},
            'error_bounds_index_points_display':{k:format(float(v*scale),'.12g') for k,v in bounds.items()},
            'decisions':[{'budget_index_points':str(b),'results':{k:('CERTIFIED_AT_BUDGET' if v*scale<=b else 'NOT_CERTIFIED_AT_BUDGET') for k,v in bounds.items()}} for b in budgets]})
    result={'status':'PASS_EXACT_FULL_ERROR_DECISION_COMPARISON','contract_sha256':hashlib.sha256((HERE/'spread-decision-contract.json').read_bytes()).hexdigest(),
            'primary_budget_index_points':str(budgets[0]),'DF':str(scale),'results':rows,
            'interpretation':contract['interpretation'],'timing_boundary':'Contract fixed before root read new joint results, after child computation had occurred. Not prospective preregistration before computation.'}
    (HERE/'spread-decisions.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
