"""Identity-bound access to a relocatable, read-only reference scientific baseline."""
from pathlib import Path
from fractions import Fraction as Q
import hashlib, importlib.util, json, sys
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def save(p, value): Path(p).write_text(json.dumps(value, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def baseline(arg=None):
    candidate=Path(arg).resolve() if arg else HERE.parents[1]
    for root in [candidate,candidate/'science']:
        if (root/'experiments').is_dir() and (root/'baseline').is_dir():return root
    raise ValueError('Supply the science directory or complete evidence root.')

def identities(base):
    c = load(HERE/"contract.json")
    for name, digest in c["baseline_sha256"].items():
        assert sha(base/name) == digest, "baseline scientific input identity mismatch: "+name
    return c
def module(name, path):
    spec=importlib.util.spec_from_file_location(name, path)
    value=importlib.util.module_from_spec(spec);sys.modules[name]=value;spec.loader.exec_module(value)
    return value
def interval(I, S, bounds):
    lo,hi=map(Q,bounds);assert lo<=hi
    return I((lo.numerator*S)//lo.denominator,-((-hi.numerator*S)//hi.denominator),True)
def exact(x): return Q.from_float(float(x))
