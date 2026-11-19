"""Retain the initial dependency ledger's exact bytes for protocol audit.

The later execution ledger excludes an unused clock-reporting solver routine.
Scientific grid, arithmetic routines used by experiments, and workload remain
unchanged. This script reconstructs that earlier HASH LEDGER, not old source
containing unused reporting calls, so no personal run data is introduced.
"""
from pathlib import Path
import hashlib,json,re
HERE=Path(__file__).resolve().parent
source=HERE.parent/'baseline/reference/code/src/solver-diagnostic.py'
blob=source.read_bytes();text=blob.decode('utf-8').split('\ndef main():')[0]
text=re.sub(r', time\b|,time\b','',text);text=re.sub(r'\btime,\s*','',text)
text=re.sub(r';?started=time\.monotonic\(\)','',text)
text=re.sub(r"\s*if start%\(block\*16\)==0:print\([^\n]+\)", '', text)
text=re.sub(r"'seconds':time\.monotonic\(\)-started,",'',text)
ledger=json.loads((HERE/'dependency-provenance.json').read_text(encoding='utf-8'))
for r in ledger['records']:
    if r['name']=='solver-diagnostic.py':r['new_sha256']=hashlib.sha256(text.encode()).hexdigest()
payload=(json.dumps(ledger,indent=2)+'\n').replace('\n','\r\n').encode('utf-8')
expected=json.loads((HERE/'nearby-contract.json').read_text(encoding='utf-8'))['dependency_ledger_sha256']
assert hashlib.sha256(payload).hexdigest()==expected
(HERE/'dependency-provenance-initial.json').write_bytes(payload)
print('PASS exact initial ledger recovered without restoring unused clock routine')
