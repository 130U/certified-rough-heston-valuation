from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
excluded={'AUDIT-MANIFEST.json','independent-audit.json','snapshot-identity-bridge.json','audit-execution.json'}
rows=[]
for p in sorted(HERE.rglob('*')):
 if not p.is_file() or p.name in excluded or '__pycache__' in p.parts:continue
 rows.append({'path':p.relative_to(HERE).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'evidence_bytes':p.stat().st_size})
(HERE/'AUDIT-MANIFEST.json').write_text(json.dumps({'status':'FIXED_SECONDARY_AUDIT_ARTIFACTS','files':rows},indent=2)+'\n',encoding='utf-8')
print('PASS frozen secondary audit manifest',len(rows),'objects')
