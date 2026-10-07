"""Read identified saved banks and reconstruct downstream certificates."""
from pathlib import Path, PurePosixPath
import argparse, hashlib, json, shutil, subprocess, sys, tempfile
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def verify():
 m=json.loads((ROOT/'SCIENTIFIC-MANIFEST.json').read_text(encoding='utf-8'))
 for r in m['files']:
  n=PurePosixPath(r['path']);assert not n.is_absolute() and ':' not in r['path'] and '\\' not in r['path']
  assert all(s not in {'','.','..'} for s in r['path'].split('/'))
  p=ROOT.joinpath(*n.parts);assert p.resolve().is_relative_to(ROOT.resolve()) and p.is_file(),r['path']
  assert p.stat().st_size==r['bytes'] and sha(p)==r['sha256'],r['path']
 return m
def main():
 p=argparse.ArgumentParser();p.add_argument('--full',action='store_true');p.add_argument('--manifest-only',action='store_true');a=p.parse_args()
 m=verify()
 if a.manifest_only:print('PASS_SCIENTIFIC_INPUT_IDENTITIES',len(m['files']));return
 work=Path(tempfile.mkdtemp(prefix='scientific-check-',dir=ROOT))
 assert work.resolve().is_relative_to(ROOT.resolve()) and work!=ROOT
 for r in m['files']:
  dst=work/r['path'];dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/r['path'],dst)
 science=work/'science'
 for n in [1024,2048]:
  for cache in (science/f'experiments/N{n}').glob('point-independent-*.json'):
   assert cache.resolve().is_relative_to(work.resolve());cache.unlink()
 steps=[('baseline/frontier/run_frontier.py',['--full'] if a.full else []),('theory/rho-direct-check.py',[]),('theory/rho-direct-controls.py',[]),('experiments/run_experiments.py',[]),('analysis/kernel/independent.py',['--baseline',str(science)]),('analysis/audit/read_audit_independent.py',['--baseline',str(science)]),('analysis/verify_extensions.py',[])]
 record={'status':'RUNNING','scientific_manifest_sha256':sha(ROOT/'SCIENTIFIC-MANIFEST.json'),'full_structural_signs':a.full,'continuous_derivatives_regenerated':False,'scope':'Saved-bank reading and exact downstream reconstruction. Full additionally recomputes the original structural-sign cover. Continuous derivative generators and strict arithmetic theory remain identified shared dependencies.','steps':[]}
 receipt=ROOT/'SCIENTIFIC-REPLAY.json'
 for name,args in steps:
  run=subprocess.run([sys.executable,'-X','utf8','-B',str(science/name),*args],capture_output=True,text=True,encoding='utf-8')
  text=(run.stdout+run.stderr).replace(str(work),'<working-copy>').replace(str(ROOT),'<evidence>')
  row={'script':'science/'+name,'returncode':run.returncode,'output':text};record['steps'].append(row)
  if run.returncode:
   record['status']='FAILED';receipt.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8');print('FAIL',name,flush=True);print(text);raise SystemExit(run.returncode)
  print('PASS',name,flush=True)
  receipt.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
 verify();record['status']='PASS_SAVED_BANK_AND_DOWNSTREAM_RECONSTRUCTION';record['scientific_input_objects']=len(m['files'])
 receipt.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8');print(record['status'],flush=True)
if __name__=='__main__':main()
