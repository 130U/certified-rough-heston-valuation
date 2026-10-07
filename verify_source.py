"""Check the published source identities; this does not execute science."""
from pathlib import Path, PurePosixPath
import hashlib, json, sys
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def check_name(s):
 p=PurePosixPath(s)
 assert not p.is_absolute() and ':' not in s and '\\' not in s
 assert all(q not in {'','.','..'} for q in s.split('/'))
 return ROOT.joinpath(*p.parts)
def main():
 data=json.loads((ROOT/'SOURCE-MANIFEST.json').read_text(encoding='utf-8'))
 rows=data.get('files',data.get('source_files'))
 assert isinstance(rows,list) and len({r['path'] for r in rows})==len(rows)
 for r in rows:
  p=check_name(r['path']);assert p.resolve().is_relative_to(ROOT.resolve())
  assert p.is_file() and p.stat().st_size==r['bytes'] and sha(p)==r['sha256'],r['path']
 print('PASS_PUBLICATION_SOURCE_IDENTITIES',len(rows))
if __name__=='__main__':main()
