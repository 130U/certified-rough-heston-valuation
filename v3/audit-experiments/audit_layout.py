"""Resolve a fixed V2 snapshot using portable canonical evidence paths."""
from pathlib import Path
import argparse
HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(add_help=False);parser.add_argument('--baseline');arguments,_=parser.parse_known_args()
def valid(p):return (p/'baseline').is_dir() and (p/'new-research/experiments').is_dir()
candidates=[]
if arguments.baseline:
 supplied=Path(arguments.baseline).resolve();candidates=[supplied,supplied/'evidence-v2',supplied.parent if supplied.name=='baseline' else supplied]
else:
 for parent in HERE.parents:
  candidates.extend([parent,parent/'evidence-v2',parent/'research/heston-major-revision-20261007/evidence-v2'])
PACKET=next((p for p in candidates if valid(p)),None)
if PACKET is None:raise SystemExit('Fixed baseline snapshot unavailable: pass --baseline with the V2 evidence root or packet root.')
BASE=PACKET/'baseline';EXP=PACKET/'new-research/experiments'
def canonical(p):
 p=p.resolve()
 if p.is_relative_to(BASE.resolve()):return 'baseline/'+p.relative_to(BASE).as_posix()
 if p.is_relative_to(EXP.resolve()):return 'new-research/experiments/'+p.relative_to(EXP).as_posix()
 if p.is_relative_to(HERE):return 'v3/audit-experiments/'+p.relative_to(HERE).as_posix()
 if p.is_relative_to(PACKET.resolve()):return 'packet-root/'+p.relative_to(PACKET).as_posix()
 raise ValueError('Evidence source is outside the identified snapshot.')
def resolve(name):
 if name.startswith('baseline/'):return BASE/name[len('baseline/'):]
 if name.startswith('new-research/experiments/'):return EXP/name[len('new-research/experiments/'):]
 if name.startswith('v3/audit-experiments/'):return HERE/name[len('v3/audit-experiments/'):]
 if name.startswith('packet-root/'):return PACKET/name[len('packet-root/'):]
 raise ValueError('Unrecognized canonical scientific source prefix.')
