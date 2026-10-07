"""Verify source identity and the retained receipt; do not rerun science."""
from pathlib import Path, PurePosixPath
import hashlib,json,sys

ROOT=Path(__file__).resolve().parent
def fail(ok,message):
    if not ok: raise ValueError(message)
def name(value):
    fail(isinstance(value,str) and value and "\\" not in value and ":" not in value,
         "Invalid relative member name.")
    p=PurePosixPath(value)
    fail(not p.is_absolute() and all(x not in {"",".",".."} for x in value.split("/")),
         "Unsafe member name.")
    return value
def sha(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1048576),b""):h.update(b)
    return h.hexdigest()
def read(n):return json.loads((ROOT/n).read_text(encoding="utf-8"))
def identity(r):return {k:r[k] for k in ("path","bytes","sha256")}
def main():
    data=read("SOURCE-MANIFEST.json")
    rows=data["source_files"]
    arrays=data["large_data_supplied_in_named_release_archive"]
    names=[name(r["path"]) for r in rows+arrays]
    fail(len(names)==len(set(names))==len({n.casefold() for n in names}),"Duplicate source/array identity.")
    for r in rows:
        p=ROOT.joinpath(*PurePosixPath(r["path"]).parts)
        fail(p.resolve().is_relative_to(ROOT) and p.is_file(),"Source missing or escapes root: "+r["path"])
        fail(p.stat().st_size==r["bytes"] and sha(p)==r["sha256"],"Source identity changed: "+r["path"])
    fail(len(arrays)==data["expected_release_array_objects"],"Release array count changed.")
    fail(all(r["path"].casefold().endswith(".npz") for r in arrays),"Non-array release-only object.")
    fail(all(not (ROOT/r["path"]).exists() for r in arrays),"Release-only array is in source checkout.")
    science=read("SCIENTIFIC-MANIFEST.json")
    science_sha=sha(ROOT/"SCIENTIFIC-MANIFEST.json")
    fail(science_sha==data["scientific_manifest_sha256"],"Scientific manifest binding changed.")
    delivery=read("DELIVERY-MANIFEST.json")
    fail(sha(ROOT/"DELIVERY-MANIFEST.json")==data["delivery_manifest_sha256"],"Delivery manifest binding changed.")
    fail(delivery["scientific_manifest_sha256"]==science_sha,"Delivery/science binding changed.")
    available={r["path"]:identity(r) for r in rows+arrays}
    for r in science["files"]:
        fail(available.get(r["path"])==identity(r),"Scientific object coverage changed: "+r["path"])
    for r in delivery["files"]:
        fail(available.get(r["path"])==identity(r),"Delivery object coverage changed: "+r["path"])
    receipt=read("FRESH-ACCEPTANCE.json")
    fail(receipt.get("status")=="PASS_FRESH_COMPLETE_SCIENTIFIC_ACCEPTANCE","Retained fresh acceptance is not PASS.")
    fail(receipt.get("tested_scientific_manifest_sha256")==science_sha,"Retained receipt tested different science.")
    fail(sha(ROOT/"FRESH-ACCEPTANCE.json")==delivery["fresh_receipt_sha256"],"Retained receipt identity changed.")
    fixed={r["path"]:r for r in science["files"]}
    fail(receipt.get("driver_sha256")==fixed.get("reproduce.py",{}).get("sha256"),"Retained driver binding changed.")
    fail(receipt.get("scientific_input_objects")==len(fixed),"Retained scientific count changed.")
    steps=receipt.get("steps",[])
    fail(bool(steps),"Retained receipt has no execution records.")
    for step in steps:
        fail(step.get("returncode")==0,"Retained receipt records a failed step.")
        script=name(step.get("script",""))
        fail(script in fixed and step.get("source_sha256")==fixed[script]["sha256"],"Retained step source binding changed.")
    print("PASS source SHA/size identities, delivery coverage and retained fresh tested-science binding. "
          "CI does not rerun scientific arithmetic or continuous residual generation. "
          "Large arrays require the named evidence release archive.")
if __name__=="__main__":
    try:main()
    except (ValueError,KeyError,OSError,json.JSONDecodeError) as e:
        print("FAIL source identity: "+str(e).replace(str(ROOT),"<source-root>"),file=sys.stderr)
        raise SystemExit(1)
