"""Resolve the identified scientific packet using relative paths."""
from pathlib import Path
import argparse
HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(add_help=False);parser.add_argument('--baseline');arguments,_=parser.parse_known_args()
def valid(p):return (p/'baseline').is_dir() and (p/'experiments').is_dir()
candidates=[]
if arguments.baseline:
 supplied=Path(arguments.baseline).resolve();candidates=[supplied,supplied/'science']
else:candidates=list(HERE.parents)
PACKET=next((p for p in candidates if valid(p)),None)
if PACKET is None:raise SystemExit('Scientific packet unavailable: pass --baseline science.')
BASE=PACKET/'baseline';EXP=PACKET/'experiments'
def canonical(p):
 p=p.resolve()
 if p.is_relative_to(BASE.resolve()):return 'baseline/'+p.relative_to(BASE).as_posix()
 if p.is_relative_to(EXP.resolve()):return 'experiments/'+p.relative_to(EXP).as_posix()
 if p.is_relative_to(HERE):return 'analysis/audit/'+p.relative_to(HERE).as_posix()
 if p.is_relative_to(PACKET.resolve()):return 'packet-root/'+p.relative_to(PACKET).as_posix()
 raise ValueError('Source outside the identified scientific packet.')
def resolve(name):
 if name.startswith('baseline/'):return BASE/name[len('baseline/'):]
 if name.startswith('experiments/'):return EXP/name[len('experiments/'):]
 if name.startswith('analysis/audit/'):return HERE/name[len('analysis/audit/'):]
 if name.startswith('packet-root/'):return PACKET/name[len('packet-root/'):]
 raise ValueError('Unrecognized canonical source prefix.')
