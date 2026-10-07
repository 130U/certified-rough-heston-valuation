"""Consolidate completed computational audit receipts without rerunning work."""
from pathlib import Path
import ast,hashlib,json,sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
def main():
    path=HERE/'verification.json';ledger=json.loads(path.read_text())
    fresh=HERE/'residual-spotcheck.json'
    if fresh.is_file():
        (HERE/'residual-fresh-subset.json').write_bytes(fresh.read_bytes())
    names=[('full_structure_sign_regeneration','full_structure_verify.py','full-structure-verification.json'),
           ('semantic_negative_controls','adversarial_checks.py','adversarial-checks.json'),
           ('independent_direct_startup','startup_independent.py','startup-independent.json'),
           ('fresh_continuous_residual_spotchecks','residual_spotcheck.py','residual-spotcheck.json'),
           ('new_shared_Fourier_support','shared_fourier_spread.py','shared-fourier-spread.json'),
           ('same_output_point_budget_decisions','spread_decisions.py','spread-decisions.json'),
           ('second_coefficient_assembly','verify_shared_fourier.py','shared-fourier-independent-verification.json')]
    original=[r for r in ledger['records'] if r['label'] not in {a for a,_,_ in names}|{'final_upstream_source_immutability'}]
    new=[]
    for label,script,receipt in names:
        source=(HERE/script).read_text(encoding='utf-8');ast.parse(source,filename=script)
        record={'label':label,'command':[ledger['python_executable'],'-B',str(HERE/script)],
                'current_script_sha256':hashlib.sha256((HERE/script).read_bytes()).hexdigest(),'receipt':receipt}
        if not (HERE/receipt).is_file():record.update({'status':'PENDING','return_code':None})
        else:
            result=json.loads((HERE/receipt).read_text(encoding='utf-8'))
            record.update({'status':'PASS' if result['status'].startswith('PASS') else result['status'],
                           'return_code':0 if result['status'].startswith('PASS') else result.get('return_code'),
                           'result':result,'wall_seconds':result.get('wall_seconds',result.get('seconds')),
                           'receipt_sha256':hashlib.sha256((HERE/receipt).read_bytes()).hexdigest()})
        new.append(record)
    immutability=HERE/'source-immutability-final.json'
    if immutability.is_file():
        imm=json.loads(immutability.read_text())
        new.append({'label':'final_upstream_source_immutability','command':'code/run.py::check_manifest()',
                    'status':'PASS' if imm['status'].startswith('PASS') else imm['status'],'return_code':0,
                    'receipt':immutability.name,'wall_seconds':imm['wall_seconds'],'result':imm})
    ledger['records']=original+new
    ledger['status']='PASS_ALL_COMPLETED_BC_COMPUTATIONAL_AUDITS' if all(r['status']=='PASS' for r in ledger['records']) else 'AUDIT_IN_PROGRESS'
    ledger['scope']='Full211241 structural leaf regeneration and cover; exact model/probability/objective replays; all1539 independently assembled startup bounds; whole-time2-node per-candidate continuous residual spotchecks; same-center complete shared-Fourier support and second coefficient assembly. No full513-node residual replay or classical coefficient-bank regeneration.'
    ledger['path_relocation_note']='The source-discovery helper was added mechanically after the full structural run and during the fresh residual replay. Original executed generator/field hashes in the receipts are unchanged. current_script_sha256 identifies the present portable wrapper, not a retroactively assigned historical execution hash. Fast shared/startup/second-assembly stages were replayed after this mechanical change.'
    path.write_text(json.dumps(ledger,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':ledger['status'],'records':len(ledger['records']),
                      'pending':[r['label'] for r in ledger['records'] if r['status']!='PASS']},indent=2))
if __name__=='__main__':main()
