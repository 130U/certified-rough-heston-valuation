"""Lossless adapter for a completed continuous-time, point-alpha residual proof.

It never replaces a rigorous bound by the diagnostic scan or convenience float.
The adapted status means continuous PHYSICAL TIME at fixed alpha/frequency
nodes. It does not certify a continuous alpha/frequency box.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json
import numpy as np

BASE=Path(__file__).resolve().parent
H=F(1,8)

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",type=Path,required=True)
    p.add_argument("--executed-source",type=Path,required=True)
    p.add_argument("--field",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    p.add_argument("--input-guards",type=Path,default=BASE/"frozen-field-input-validation.json")
    args=p.parse_args()
    rawbytes=args.input.read_bytes();raw=json.loads(rawbytes)
    if raw.get("status")!="OUTWARD_BINARY64_INTERVAL_POINT_RESIDUAL_CERTIFICATE":
        raise ValueError("only the completed outward residual proof is accepted")
    if raw.get("source_sha256")!=digest(args.executed_source):
        raise ValueError("executed source hash does not match completed result")
    if raw.get("field_sha256")!=digest(args.field):
        raise ValueError("frozen field hash differs from the actual source")
    if raw.get("residual_definition")!="physical Gbar-nu*F(Hhat), Hhat=I^alpha Gbar":
        raise ValueError("unknown residual object")
    if F(raw["alpha_exact"])!=F(raw["beta_exact"]):
        raise ValueError("this executed version requires point alpha=beta")
    if F(raw["T_exact"])!=F(1,2) or F(raw["nu_exact"])!=F(2897,10000):
        raise ValueError("frozen T/nu differs")
    guards_path=args.input_guards
    guards=json.loads(guards_path.read_bytes())
    if guards.get("status")!="EXACT_FROZEN_FIELD_INPUT_GUARDS_PASS":
        raise ValueError("frozen input guards have not passed")
    matching=[r for r in guards["records"] if r["sha256"]==raw["field_sha256"] and r["guards"]=="PASS"]
    if len(matching)!=1:raise ValueError("actual field lacks unique passed guards")
    saved=np.load(args.field);t=saved["t"];u=saved["u"]
    if not all(np.all(np.isfinite(saved[k])) for k in ["t","u","A1","A2","LG"]):
        raise ValueError("nonfinite frozen component")
    if t[0]!=0 or t[-1]!=.5 or not np.all(np.diff(t)>0) or not np.all(saved["LG"][0]==0):
        raise ValueError("field hypotheses fail")
    split=raw["split"]
    if not isinstance(split,int) or split<1:raise ValueError("positive integer subdivision needed")
    if raw["certified_closed_subintervals"]!=1+(len(t)-2)*split:
        raise ValueError("closed physical-time interval count does not cover the grid")
    for j in range(1,len(t)-1):
        edges=np.linspace(t[j],t[j+1],split+1);edges[0]=t[j];edges[-1]=t[j+1]
        if not np.all(np.diff(edges)>0):raise ValueError("subdivision loses ordered coverage")
    nodes=[F.from_float(v) for v in raw["u"]]
    values=raw["delta_physical_upper_exact_dyadics"]
    if len(nodes)!=len(values) or len(nodes)<2:raise ValueError("bound/node count differs")
    if nodes!=[i*H for i in range(len(nodes))]:
        raise ValueError("frequency cover must have exact h=1/8 without gaps")
    if [F.from_float(float(v)) for v in u[:len(nodes)]]!=nodes:
        raise ValueError("residual nodes differ from frozen field")
    bounds=[]
    first_hp=raw.get("first_cell_Re_H_div_talpha_upper_exact_dyadics")
    later_hp=raw.get("later_cells_Re_H_upper_exact_dyadics")
    if (first_hp is None)!=(later_hp is None):
        raise ValueError("both first-cell and later-cell real-part evidence required")
    if first_hp is not None and (len(first_hp)!=len(nodes) or len(later_hp)!=len(nodes)):
        raise ValueError("real-part bound/node count differs")
    for index,(node,value) in enumerate(zip(nodes,values)):
        if not isinstance(value,str) or F(value)<0:raise ValueError("nonnegative exact upper bound required")
        record={"u":str(node),"delta_physical_upper":value}
        if first_hp is not None:
            if not isinstance(first_hp[index],str) or not isinstance(later_hp[index],str):
                raise ValueError("real-part evidence must be exact rational strings")
            # The first record bounds Re(Hhat)/t^alpha, NOT Hhat itself.
            # If it is nonpositive then the complete first cell, including
            # zero, has Re(Hhat)<=0. A positive bracket is not a direct H bound.
            if F(first_hp[index])<=0:
                record["approx_halfplane_upper"]=str(max(F(0),F(later_hp[index])))
                record["halfplane_source"]="first-cell normalized bracket<=0 and later all-cell exact upper; include Hhat(0)=0"
        bounds.append(record)
    proof=BASE/"field-residual-proof.md"
    helper_evidence=[]
    if "combined_derivative_source_sha256" in raw:
        helper=BASE/"combined-field-derivative.py"
        if raw["combined_derivative_source_sha256"]!=digest(helper):
            raise ValueError("combined derivative helper differs from executed result")
        helper_evidence=[{"path":str(helper),"sha256":digest(helper)}]
    out={"status":"EXACT_CONTINUOUS_RESIDUAL_CERTIFICATE",
        "scope":"all physical t in [0,1/2], one point alpha, fixed dyadic Fourier nodes only",
        "field_sha256":raw["field_sha256"],"T":raw["T_exact"],"nu":raw["nu_exact"],
        "rho":"-1489/2000","kappa":"0","alpha_lower":raw["alpha_exact"],
        "alpha_upper":raw["alpha_exact"],"frequency_step":"1/8",
        "residual_definition":"D_C_t_alpha_Hhat_minus_nu_F","cover":bounds,
        "proof_evidence":[{"path":str(proof),"sha256":digest(proof)},
            {"path":str(args.executed_source),"sha256":digest(args.executed_source)},
            {"path":str(args.input),"sha256":hashlib.sha256(rawbytes).hexdigest()},
            {"path":str(guards_path),"sha256":digest(guards_path)}]+helper_evidence,
        "source_sha256":digest(Path(__file__)),
        "adapter_changes_only_schema_not_bounds":True,
        "uses_scan_or_convenience_float":False}
    if digest(args.field)!=raw["field_sha256"]:raise ValueError("field changed during adapter")
    args.output.write_text(json.dumps(out,indent=2)+"\n",encoding="utf8")
    print(json.dumps({"status":out["status"],"nodes":len(bounds),"scope":out["scope"]},indent=2))

if __name__=="__main__":main()
