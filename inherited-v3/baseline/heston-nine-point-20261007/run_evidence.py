"""One-command acceptance of the fixed, self-contained evidence bundle.

Run with --full to additionally regenerate every structural interval sign.
Run with --regenerate-continuous for a fresh full alpha=.52 time cover.
Frozen files are first hashed; executed outputs go into a separate work copy.
"""
from pathlib import Path
import argparse, hashlib, importlib.util, json, shutil, subprocess, sys, time
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser();p.add_argument('--full',action='store_true');p.add_argument('--regenerate-continuous',action='store_true');a=p.parse_args()
    start=0;manifest=ROOT/'BUNDLE-MANIFEST.json'
    if manifest.exists():
        entries=json.loads(manifest.read_text(encoding='utf-8'))['files']
        for row in entries:
            f=ROOT/row['path'];assert f.is_file() and f.stat().st_size==row['bytes'] and digest(f)==row['sha256'],row['path']
        print('PASS fixed bundle identities:',len(entries),flush=True)
    work=ROOT/'verification-work';work.mkdir(exist_ok=True)
    for stem in ['english-heston-release','bc-merged-20261007','heston-nine-point-20261007']:
        origin=ROOT/stem;target=work/stem
        assert target.resolve().is_relative_to(work.resolve())
        shutil.copytree(origin,target,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','.cache','paper','scripts','qa','bundle-v1','*.zip'))
    revision=work/'heston-nine-point-20261007';baseline=work/'english-heston-release'
    records=[]
    def receipt(status):
        return {'status':status,'tested_manifest_sha256':digest(manifest) if manifest.exists() else None,
                'full_structural_regeneration':a.full,'fresh_continuous_regeneration':a.regenerate_continuous,
                'records':records}
    def run(label,cmd):
        t=0;r=subprocess.run(cmd,cwd=revision,capture_output=True,text=True,encoding='utf-8')
        log=work/(label+'.log');log.write_text(r.stdout+r.stderr,encoding='utf-8')
        rec={'label':label,'return_code':r.returncode,'log':log.relative_to(ROOT).as_posix()}
        records.append(rec);print(json.dumps(rec),flush=True)
        (work/'execution-receipt.json').write_text(json.dumps(receipt('RUNNING' if r.returncode==0 else 'FAILED_SUBPROCESS'),indent=2)+'\n',encoding='utf-8')
        assert r.returncode==0,r.stderr or r.stdout
    py=[sys.executable,'-X','utf8','-B']
    run('frozen-inputs-and-model-inclusions',py+[str(baseline/'code/run.py'),'verify'])
    for script in ['verify_package.py','verify_input_bounds.py','verify_terminal.py','verify_field_receipt.py']:
        run('classical-'+script[:-3],py+[str(baseline/'code/classical'/script)])
    for script in ['startup_independent.py','adversarial_checks.py']:
        run(script[:-3],py+[str(work/'bc-merged-20261007'/script)])
    if a.full:run('all-211241-structural-signs',py+[str(work/'bc-merged-20261007/full_structure_verify.py')])
    if a.regenerate_continuous:run('fresh-all-513-time-residuals',py+[str(revision/'retain-time-envelopes.py')])
    for script in ['finite-history.py','verify-finite-history-independent.py','check-time-envelope.py','time-local-propagation.py']:
        run(script[:-3],py+[str(revision/script)])
    for script in ['literature-ledger-readback.py','independent-time-local.py']:
        run(script[:-3],py+[str(revision/script)])
    saved_baseline=revision/'portfolio-results-frozen.json'
    shutil.copyfile(revision/'portfolio-results.json',saved_baseline)
    run('portfolio-baseline',py+[str(revision/'portfolio-experiments-baseline.py')])
    def mathematical(value):
        if isinstance(value,list):return [mathematical(v) for v in value]
        if isinstance(value,dict):return {k:mathematical(v) for k,v in value.items() if k not in ['python']}
        return value
    assert mathematical(json.loads(saved_baseline.read_text(encoding='utf-8')))==mathematical(json.loads((revision/'portfolio-results.json').read_text(encoding='utf-8'))),'replayed baseline mathematical endpoints changed'
    run('portfolio-finite-history',py+[str(revision/'portfolio-experiments.py'),'--finite-history'])
    run('portfolio-report',py+[str(revision/'portfolio-report.py')])
    replay_records=[]
    for label,script in [('verify-finite-history-independent','verify-finite-history-independent.py'),('portfolio-finite-history','portfolio-experiments.py'),('portfolio-report','portfolio-report.py')]:
        rec=next(x for x in records if x['label']==label)
        replay_records.append({'script':script,'exit_code':rec['return_code'],'log':rec['log']})
    (revision/'portfolio-replay-receipt.json').write_text(json.dumps({'status':'PASS_DEPENDENCY_ORDER_REPLAY_ALL_RETURN_CODES_ZERO','baseline_overwritten':False,
        'scope':'Frozen bundle baseline bytes preserved; separately regenerated work-copy mathematics exactly compared with the saved baseline, omitting timings and interpreter-version metadata.',
        'records':replay_records},indent=2)+'\n',encoding='utf-8')
    run('portfolio-identities',py+[str(revision/'verify-portfolio-identities.py')])
    if manifest.exists():
        for row in entries:
            f=ROOT/row['path'];assert f.stat().st_size==row['bytes'] and digest(f)==row['sha256'],'frozen bundle changed: '+row['path']
    out={'status':'PASS_EXECUTED_FIXED_EVIDENCE_BUNDLE','tested_manifest_sha256':digest(manifest) if manifest.exists() else None,'full_structural_regeneration':a.full,
         'fresh_continuous_regeneration':a.regenerate_continuous,'records':records,
         'scope':'Saved model inclusions, all startup bounds, semantic negative controls, finite-history independent arithmetic, complete time-envelope identity/cover, time-local propagation, all systematic portfolios. Optional switches regenerate structural signs and all alpha=.52 continuous residuals. Other candidates retain their released continuous-time certificates.'}
    (work/'execution-receipt.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':out['status']},indent=2),flush=True)
if __name__=='__main__':main()
