"""Fixed-input acceptance, with optional reconstruction in a separate tree.

Fresh generator timings change its receipt identity. The regeneration tree is
therefore never used as an input to the fixed transfer readers.
"""
from pathlib import Path
import argparse,hashlib,json,shutil,subprocess,sys,time
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--full',action='store_true');parser.add_argument('--regenerate-full',action='store_true');a=parser.parse_args()
    manifest=ROOT/'FRONTIER-MANIFEST.json';assert manifest.exists(),'Run from the extracted fixed supplement.'
    rows=json.loads(manifest.read_text(encoding='utf-8'))['files']
    for row in rows:
        p=ROOT/row['path'];assert p.resolve().is_relative_to(ROOT.resolve()),row['path']
        assert p.is_file() and p.stat().st_size==row['bytes'] and sha(p)==row['sha256'],row['path']
    def clone_manifest_tree(target):
        assert target.resolve().is_relative_to(ROOT.resolve()) and target.resolve()!=ROOT.resolve()
        target.mkdir()
        # Every clone begins from the immutable manifest objects, never another
        # working tree with rewritten results or runtime metadata.
        for row in rows:
            p=target/row['path'];assert p.resolve().is_relative_to(target.resolve()),row['path']
            p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/row['path'],p)
    token=str(time.time_ns())
    work=ROOT/('frontier-verification-work-'+token);clone_manifest_tree(work)
    regeneration_work=None;regeneration_copy_seconds=None;active_step=None
    records=[];start=time.perf_counter();py=[sys.executable,'-X','utf8','-B']
    receipt=ROOT/'frontier-execution-receipt.json'
    def save(status):
        r={'status':status,'tested_manifest_sha256':sha(manifest),'records':records,'active_step':active_step,
           'full':a.full,'regenerate_full':a.regenerate_full,'wall_seconds_including_subprocess_startup':time.perf_counter()-start,
           'scope':'Manifest checks and primary work-copy creation precede this phase timer. Subprocess times include fresh child interpreter startup. Optional regeneration-copy creation is included in the phase timer and reported separately. Fixed transfer readers use only the primary fixed-input tree.',
           'work_directory':work.name,'work_tree_scope':'Fixed manifest inputs; normal aggregation and complete readers. No fresh continuous reconstruction changes these inputs.',
           'regeneration_work_directory':regeneration_work.name if regeneration_work is not None else None,
           'regeneration_tree_scope':'Separate full manifest clone: fresh high-node residual generation and saved-bank/startup audit only. Its newly timed raw receipt is never supplied to fixed transfer readers.' if regeneration_work is not None else None,
           'regeneration_copy_seconds':regeneration_copy_seconds}
        receipt.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8');return r
    def run(label,cmd,cwd=None,tree=None,scope='fixed-input acceptance'):
        nonlocal active_step
        tree=work if tree is None else tree;cwd=tree/'heston-frontier-20261007' if cwd is None else cwd
        assert cwd.resolve().is_relative_to(tree.resolve())
        active_step={'label':label,'tree':tree.name,'scope':scope};save('RUNNING')
        t=time.perf_counter();p=subprocess.run(cmd,cwd=cwd,capture_output=True,text=True,encoding='utf-8')
        log=tree/(label+'.log');log.write_text(p.stdout+p.stderr,encoding='utf-8')
        records.append({'label':label,'return_code':p.returncode,'wall_seconds':time.perf_counter()-t,
                        'log':str(log.relative_to(ROOT)),'work_tree':tree.name,'scope':scope})
        active_step=None
        print(json.dumps(records[-1]),flush=True);save('RUNNING' if p.returncode==0 else 'FAILED')
        assert p.returncode==0,p.stderr or p.stdout
    command=py+[str(work/'heston-nine-point-20261007/run_evidence.py')]
    if a.full:command+=['--full']
    run('original-finite-history-full-acceptance',command,work)
    fresh=work/'heston-frontier-20261007'
    for name in ['omission-verify.py','omission-aggregate.py','independent-omission.py','independent-transfer.py','independent-transfer-supplement.py']:
        assert (fresh/name).exists(),name
        command=py+[str(fresh/name)]
        if name in ['independent-transfer.py','independent-transfer-supplement.py']:command+=['--full']
        run(name[:-3],command)
    if a.regenerate_full:
        # The complete fixed-input readers above must pass before expensive
        # optional reconstruction. Do not overwrite the raw high-node receipt
        # whose original SHA is pinned by the quarter-maturity evidence.
        regeneration_work=ROOT/('frontier-regeneration-work-'+token)
        assert regeneration_work.resolve()!=work.resolve()
        t=time.perf_counter();clone_manifest_tree(regeneration_work);regeneration_copy_seconds=time.perf_counter()-t
        regenerated=regeneration_work/'heston-frontier-20261007'
        run('optional-new-high-frequency-continuous-regeneration',py+[str(regenerated/'omission-run.py'),'--regenerate-full'],
            tree=regeneration_work,scope='isolated fresh high-node reconstruction; no fixed transfer inputs consumed')
        run('optional-fresh-high-frequency-bank-audit',py+[str(regenerated/'omission-verify.py')],
            tree=regeneration_work,scope='isolated fresh bank, all closed cells, startup and half-plane audit')
        # Verify the original raw sources in the fixed-input tree remained
        # untouched throughout optional generation and its fresh-bank audit.
        fixed_names=['heston-frontier-20261007/omission-residual-high.json',
                     'heston-frontier-20261007/omission-time-high.npz',
                     'heston-frontier-20261007/omission-full-execution.json']
        identities={row['path']:row for row in rows}
        for name in fixed_names:assert sha(work/name)==identities[name]['sha256'],('fixed-input identity changed',name)
    # Recheck the immutable archive objects after all work-copy mutations.
    for row in rows:assert sha(ROOT/row['path'])==row['sha256'],row['path']
    result=save('PASS_COMPLETE_FRONTIER_ACCEPTANCE')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
