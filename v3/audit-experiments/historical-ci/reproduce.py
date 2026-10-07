"""Verify a fixed scientific packet in a fresh copy, without host telemetry."""
from pathlib import Path
import argparse,hashlib,json,shutil,subprocess,sys,tempfile,re
ROOT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def verify(root):
    mf=root/'SCIENTIFIC-MANIFEST.json';data=json.loads(mf.read_text(encoding='utf-8'))
    for row in data['files']:
        p=root/row['path'];assert p.resolve().is_relative_to(root.resolve()),row['path']
        assert p.is_file() and p.stat().st_size==row['bytes'] and sha(p)==row['sha256'],row['path']
    return data
def main():
    p=argparse.ArgumentParser();p.add_argument('--full',action='store_true');p.add_argument('--manifest-only',action='store_true');a=p.parse_args()
    data=verify(ROOT)
    if a.manifest_only:print('PASS immutable scientific inputs',len(data['files']));return
    work=Path(tempfile.mkdtemp(prefix='verification-',dir=ROOT))
    assert work.resolve().is_relative_to(ROOT.resolve()) and work.resolve()!=ROOT.resolve()
    for row in data['files']:
        dest=work/row['path'];dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/row['path'],dest)
    shutil.copyfile(ROOT/'SCIENTIFIC-MANIFEST.json',work/'SCIENTIFIC-MANIFEST.json')
    # Cached reader results document previous checks. They must not replace a
    # fresh reconstruction in this acceptance copy.
    for n in [1024,2048]:
        for cache in (work/f'new-research/experiments/N{n}').glob('point-independent-*.json'):
            assert cache.resolve().is_relative_to(work.resolve());cache.unlink()
    steps=[('baseline/heston-frontier-20261007/run_frontier.py',['--full'] if a.full else []),
           ('new-research/theory/rho-direct-check.py',[]),
           ('new-research/theory/rho-direct-controls.py',[]),
           ('new-research/experiments/run_experiments.py',[])]
    record={'status':'RUNNING','tested_scientific_manifest_sha256':sha(ROOT/'SCIENTIFIC-MANIFEST.json'),
      'driver_sha256':sha(Path(__file__)),'full':a.full,'steps':[],
      'scope':'Fresh-copy complete saved-evidence reading, independent exact derivations, actual-output replay and deliberate corruptions. Full additionally runs the baseline fresh continuous-residual checks. All new residual banks were fully generated in the retained experiment; this command does not regenerate every field or residual derivative.',
      'independence':'Author-side complete acceptance in a fresh copy; separate readers share explicitly disclosed rigorous primitives. Not a claim of an external referee execution.'}
    dest=ROOT/'FRESH-ACCEPTANCE.json'
    for script,args in steps:
        result=subprocess.run([sys.executable,'-X','utf8','-B',str(work/script),*args],capture_output=True,text=True,encoding='utf-8')
        output=(result.stdout+result.stderr).replace(str(work),'<verification-copy>').replace(str(ROOT),'<evidence>')
        output=re.sub(r'[A-Za-z]:[\\/]Users[\\/][^\r\n"\']+','<local-path>',output)
        record['steps'].append({'script':script,'args':args,'source_sha256':sha(work/script),'returncode':result.returncode,'output':output})
        if result.returncode:
            record['status']='FAILED';dest.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8');print('FAIL',script);raise SystemExit(result.returncode)
        print('PASS',script,flush=True)
    verify(ROOT)
    record['status']='PASS_FRESH_COMPLETE_SCIENTIFIC_ACCEPTANCE';record['scientific_input_objects']=len(data['files'])
    dest.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8');print(record['status'])
if __name__=='__main__':main()
