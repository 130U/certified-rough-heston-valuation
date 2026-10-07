"""One-command portable secondary audit of fixed V2 evidence."""
from pathlib import Path
import argparse,hashlib,json,re,subprocess,sys
from audit_layout import HERE,PACKET
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--baseline');parser.add_argument('--manifest-only',action='store_true');a=parser.parse_args()
 manifest=HERE/'AUDIT-MANIFEST.json';rows=json.loads(manifest.read_text(encoding='utf-8'))['files']
 for r in rows:
  p=HERE/r['path'];assert p.resolve().is_relative_to(HERE);assert p.stat().st_size==r['evidence_bytes'] and sha(p)==r['sha256']
 if a.manifest_only:print('PASS secondary audit artifact identities',len(rows));return
 commands=['read_audit_independent.py','bridge_snapshot.py'];steps=[]
 for name in commands:
  p=subprocess.run([sys.executable,'-B',str(HERE/name),'--baseline',str(PACKET)],capture_output=True,text=True,encoding='utf-8')
  output=(p.stdout+p.stderr).replace(str(HERE),'<audit>').replace(str(PACKET),'<fixed-baseline>')
  output=re.sub(r'[A-Za-z]:[\\/]Users[\\/][^\r\n"\']+','<local-path>',output)
  steps.append({'script':name,'source_sha256':sha(HERE/name),'return_code':p.returncode,'output':output})
  if p.returncode:
   (HERE/'audit-execution.json').write_text(json.dumps({'status':'FAILED','steps':steps},indent=2)+'\n',encoding='utf-8');print('FAIL secondary audit',name);raise SystemExit(p.returncode)
 receipt={'status':'PASS_PORTABLE_INDEPENDENT_SECONDARY_AUDIT','audit_manifest_sha256':sha(manifest),'steps':steps,'scope':'Exact secondary ledgers, threshold counts, all40 pair-mode decisions and source-checked flag semantics; no original continuous derivative regeneration is claimed.'}
 (HERE/'audit-execution.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8');print(receipt['status'])
if __name__=='__main__':main()
