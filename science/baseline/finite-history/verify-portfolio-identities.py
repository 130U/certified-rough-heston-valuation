"""Release/current-receipt identity checks, independent of portfolio aggregation."""
from pathlib import Path
import hashlib,json,time
HERE=Path(__file__).resolve().parent;BASE=HERE.parent/'reference';OLD=HERE.parent/'continuous'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    started=0;contract=load(HERE/'portfolio-contract.json');base=load(HERE/'portfolio-results.json')
    tight=load(HERE/'portfolio-results-finite-history.json');ind=load(HERE/'finite-history-independent-verification.json')
    comparison=load(HERE/'portfolio-comparison.json');finite=load(HERE/'finite-history-results.json');replay=load(HERE/'portfolio-replay-receipt.json')
    manifest={r['path']:r['sha256'] for r in load(BASE/'code/MANIFEST.json')['artifacts']}
    assert base['contract_sha256']==tight['contract_sha256']==sha(HERE/'portfolio-contract.json')
    assert base['implementation_sha256']==sha(HERE/'portfolio-experiments-baseline.py'),'historical baseline implementation bytes changed'
    assert tight['implementation_sha256']==sha(HERE/'portfolio-experiments.py')
    assert ind['implementation_sha256']==sha(HERE/'verify-finite-history-independent.py')
    assert finite['implementation_sha256']==sha(HERE/'finite-history.py')
    assert base['prepared_coefficients']['exact_interval_cache_sha256']==tight['prepared_coefficients']['exact_interval_cache_sha256']
    for name,value in contract['source_sha256'].items():
        p=BASE/'code/frozen'/name;assert sha(p)==value==manifest['code/frozen/'+name]
    for name,value in ind['input_sha256'].items():
        candidates=[HERE/name,BASE/'code/frozen'/name,OLD/name]
        paths=[p for p in candidates if p.is_file()];assert len(paths)==1 and sha(paths[0])==value,'independent checker source receipt drifted: '+name
    for record in tight['records']:
        receipt=record['upgraded_node_receipt'];assert sha(HERE/receipt['file'])==receipt['sha256']==ind['input_sha256'][receipt['file']]
    for name,value in comparison['input_sha256'].items():assert sha(HERE/name)==value
    assert len(base['records'])==len(tight['records'])==comparison['matched_records']==84
    assert all(r['exit_code']==0 for r in replay['records']) and not replay['baseline_overwritten']
    assert [r['script'] for r in replay['records']]==['verify-finite-history-independent.py','portfolio-experiments.py','portfolio-report.py']
    assert {r['alpha']:r['primary_stopping_step'] for r in finite['results']}=={'13/25':82,'3/5':0,'9/10':0}
    files=['portfolio-contract.json','portfolio-results.json','portfolio-results-finite-history.json','portfolio-comparison.json','portfolio-research.md',
           'portfolio-replay-receipt.json','finite-history-independent-verification.json','optimal-upgrade-menu.json',
           'make_portfolio_contract.py','portfolio-experiments-baseline.py','portfolio-experiments.py','portfolio-report.py','verify-finite-history-independent.py','verify-portfolio-identities.py']
    output={'status':'PASS_PORTFOLIO_IDENTITY_AND_LATEST_RECEIPT_AUDIT','all_84_supplementary_receipts_match_current_node_files':True,
            'baseline_historical_implementation_and_coefficient_cache_preserved':True,'primary_stopping_steps_correct':True,
            'support_and_proof_boundary':'Arithmetic portfolio certificates conditional on upstream and finite-history analytic assumptions. Identity/read-back checks do not substitute for analytic proofs.',
            'artifact_sha256':{name:sha(HERE/name) for name in files},'new_replay_return_codes':[r['exit_code'] for r in replay['records']],
            }
    (HERE/'portfolio-verification.json').write_text(json.dumps(output,indent=2)+'\n');print(json.dumps(output,indent=2))
if __name__=='__main__':main()
