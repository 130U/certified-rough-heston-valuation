"""Read-only exact guards for explicitly supplied frozen candidate fields."""
from pathlib import Path
import argparse,hashlib,json
import numpy as np

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--fields",type=Path,nargs="+",required=True)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args();rows=[]
    for path in args.fields:
        before=digest(path);saved=np.load(path)
        t,u,A1,A2,LG=[saved[k] for k in ["t","u","A1","A2","LG"]]
        assert t.ndim==u.ndim==1 and t[0]==0 and t[-1]==.5 and np.all(np.diff(t)>0)
        assert np.array_equal(u,np.arange(len(u))/8)
        assert LG.shape==(len(t),len(u)) and A1.shape==u.shape==A2.shape
        assert np.all(LG[0]==0) and all(np.all(np.isfinite(a)) for a in [t,u,A1,A2,LG])
        assert digest(path)==before
        rows.append({"file":path.name,"sha256":before,"guards":"PASS",
            "time_nodes":len(t),"frequencies":len(u)})
    result={"status":"EXACT_FROZEN_FIELD_INPUT_GUARDS_PASS",
        "source_sha256":digest(Path(__file__)),"records":rows}
    args.output.write_text(json.dumps(result,indent=2)+"\n",encoding="utf8")
    print(json.dumps(result,indent=2))
if __name__=="__main__":main()
