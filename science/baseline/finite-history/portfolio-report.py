"""Exact scenario read-back, summary and claim audit for the fixed 28 portfolios."""
from fractions import Fraction as Q
from pathlib import Path
from decimal import Decimal,localcontext,ROUND_CEILING
import hashlib,json,statistics,time
HERE=Path(__file__).resolve().parent
KEYS=['symmetric_marginal','best_signed_marginal','shared_Fourier','legal_directional_intersection']
def load(p):return json.loads((HERE/p).read_text())
def sha(p):return hashlib.sha256((HERE/p).read_bytes()).hexdigest()
def decimal_up(x,places=9):
    x=Q(x)
    with localcontext() as c:
        c.prec=120;c.rounding=ROUND_CEILING
        return str((Decimal(x.numerator)/Decimal(x.denominator)).quantize(Decimal(1).scaleb(-places),rounding=ROUND_CEILING))
def timing(values):return {'minimum':min(values),'median':statistics.median(values),'maximum':max(values),'total':sum(values)}
def main():
    started=0;contract=load('portfolio-contract.json');old=load('portfolio-results.json');new=load('portfolio-results-finite-history.json')
    scale=Q(contract['discount_D'])*Q(contract['forward_F']);direction={d['id']:d for d in contract['directions']}
    base={(r['alpha'],r['direction_id']):r for r in old['records']};tight={(r['alpha'],r['direction_id']):r for r in new['records']}
    assert len(base)==len(tight)==84 and base.keys()==tight.keys()
    comparisons=[];scenarios=[]
    for name,data in [('baseline',old),('finite_history',new)]:
        assert data['contract_sha256']==sha('portfolio-contract.json')
        for r in data['records']:
            w=list(map(Q,r['weights']));assert r['weights']==direction[r['direction_id']]['weights']
            c=Q(r['signed_center']);rad=Q(r['full_joint_radius']);assert list(map(Q,r['joint_error_interval']))==[c-rad,c+rad]
            assert Q(r['absolute_error_bounds_normalized']['shared_Fourier'])==abs(c)+rad
            boxes={k:list(map(Q,r[k])) for k in ['joint_error_interval','best_signed_marginal_error_interval','payoff_error_interval','legal_directional_intersection_error_interval']}
            expected=[max(boxes[k][0] for k in ['joint_error_interval','best_signed_marginal_error_interval','payoff_error_interval']),
                      min(boxes[k][1] for k in ['joint_error_interval','best_signed_marginal_error_interval','payoff_error_interval'])]
            assert expected==boxes['legal_directional_intersection_error_interval'] and expected[0]<=expected[1]
            assert Q(r['absolute_error_bounds_normalized']['best_signed_marginal'])==max(map(abs,boxes['best_signed_marginal_error_interval']))
            assert Q(r['absolute_error_bounds_normalized']['legal_directional_intersection'])==max(map(abs,expected))
            assert Q(r['absolute_error_bounds_normalized']['best_signed_marginal'])<=Q(r['absolute_error_bounds_normalized']['symmetric_marginal'])
            for key in KEYS:
                assert Q(r['absolute_error_bounds_index_points'][key])==scale*Q(r['absolute_error_bounds_normalized'][key])
                for decision in r['decisions']:
                    assert (decision['result'][key]=='CERTIFIED')==(Q(r['absolute_error_bounds_index_points'][key])<=Q(decision['budget_index_points']))
            assert Q(r['reduction_fraction_joint_vs_best_signed'])==1-Q(r['absolute_error_bounds_normalized']['shared_Fourier'])/Q(r['absolute_error_bounds_normalized']['best_signed_marginal'])
        scenarios.append({'scenario':name,
                          'candidate_diagnostics':data.get('candidate_diagnostics',[]),'summary':data['summary'],
                          
                          'intersection_strict_improvements':sum(r['intersection_strictly_improves_joint'] for r in data['records']),
                          'all_joint_intervals_nested_in_signed_marginal':all(r['joint_interval_inside_marginal'] for r in data['records'])})
    for key,a in base.items():
        b=tight[key];assert a['signed_center']==b['signed_center'] and a['weights']==b['weights']
        for component in ['analytic_strip_grid','true_infinite_tail','reference_arithmetic','omitted_finite_nodes']:
            assert a['radius_account'][component]==b['radius_account'][component]
        assert Q(b['full_joint_radius'])<=Q(a['full_joint_radius'])
        A=list(map(Q,a['best_signed_marginal_error_interval']));B=list(map(Q,b['best_signed_marginal_error_interval']));assert A[0]<=B[0]<=B[1]<=A[1]
        comparisons.append({'alpha':key[0],'direction_id':key[1],'kind':a['kind'],'unchanged_signed_center':a['signed_center'],
                            'baseline_index_point_bounds':a['absolute_error_bounds_index_points'],
                            'finite_history_index_point_bounds':b['absolute_error_bounds_index_points'],
                            'baseline_decisions':a['decisions'],'finite_history_decisions':b['decisions']})
    summary={'status':'PASS_EXACT_PORTFOLIO_SCENARIO_READBACK','matched_records':84,'scenarios':scenarios,'comparisons':comparisons,
             'input_sha256':{p:sha(p) for p in ['portfolio-contract.json','portfolio-results.json','portfolio-results-finite-history.json']},
             'proof_boundary':'Endpoint, scale, decisions, intersection, unchanged centre/remainder and scenario-monotonicity checks. Does not independently regenerate every trigonometric coefficient or prove the upstream/finitary analytic hypotheses.'}
    (HERE/'portfolio-comparison.json').write_text(json.dumps(summary,indent=2)+'\n')
    (HERE/'portfolio-research.md').write_text('Scientific portfolio account; exact results are retained in portfolio-comparison.json.\n',encoding='utf-8')
    print(json.dumps({'status':summary['status'],'matched_records':84},indent=2))
if __name__=='__main__':main()
