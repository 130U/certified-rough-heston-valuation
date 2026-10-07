"""Record the portable code and proof-map byte identities; no scientific rerun."""
from pathlib import Path
import hashlib,json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):h.update(block)
    return h.hexdigest()

files=[p for p in HERE.rglob('*') if p.is_file() and p.name!='MANIFEST.json'
       and '__pycache__' not in p.parts and p.suffix!='.pyc']
files.append(ROOT/'docs'/'proof-map.md')
records=[{'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':digest(p)}
         for p in sorted(files)]
assert all(r['bytes']<100*1024*1024 for r in records)
out={'status':'PORTABLE_CODE_AND_FROZEN_INPUT_MANIFEST',
     'hash':'sha256','artifacts':records,
     'scope':'Own-code and frozen release bytes plus the proof map; manuscript/PDF identity is recorded by the top-level release process.'}
(HERE/'MANIFEST.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'files':len(records),'bytes':sum(r['bytes'] for r in records),
                  'maximum_file_bytes':max(r['bytes'] for r in records)},indent=2))
