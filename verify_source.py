"""Check the published source identities; this does not execute science."""
from pathlib import Path, PurePosixPath
import argparse, hashlib, json, os, sys
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
 parser=argparse.ArgumentParser();parser.add_argument('--strict',action='store_true',help='Also reject unlisted publication files');args=parser.parse_args()
 data=json.loads((ROOT/'SOURCE-MANIFEST.json').read_text(encoding='utf-8'))
 rows=data.get('files',data.get('source_files'))
 assert isinstance(rows,list) and len({r['path'] for r in rows})==len(rows)
 for r in rows:
  p=check_name(r['path']);assert p.resolve().is_relative_to(ROOT.resolve())
  assert p.is_file() and p.stat().st_size==r['bytes'] and sha(p)==r['sha256'],r['path']
 if args.strict:
  ignored={'.git','.cache','qa','node_modules','__pycache__','.venv'}
  actual=set()
  for parent,dirs,files in os.walk(ROOT):
   dirs[:]=[name for name in dirs if name not in ignored and not name.startswith('scientific-check-')]
   actual.update((Path(parent)/name).relative_to(ROOT).as_posix() for name in files)
  expected={r['path'] for r in rows}|{'SOURCE-MANIFEST.json'}
  assert actual==expected,{'unlisted':sorted(actual-expected),'missing':sorted(expected-actual)}
  print('PASS_EXACT_PUBLICATION_INVENTORY',len(actual))
 print('PASS_PUBLICATION_SOURCE_IDENTITIES',len(rows))
if __name__=='__main__':main()
