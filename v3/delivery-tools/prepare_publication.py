"""Prepare a new source tree from a sealed delivery allowlist; never run Git.

The retained fresh receipt is checked for identity, not rerun by source CI.
Scientific arrays remain identified as named-release-only objects.
"""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json
import shutil
import subprocess
import sys

from seal_delivery import (FRESH_STATUS, digest_file, json_file, receipt_check,
                           relative_name, require, source_file, write_json)


VERIFY_SOURCE = r'''"""Verify source identity and the retained receipt; do not rerun science."""
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
'''

WORKFLOW = '''name: Verify sealed source identities
on:
  push:
    branches: [main]
  workflow_dispatch:
permissions:
  contents: read
jobs:
  source-identity:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Check identities and retained fresh acceptance binding
        run: python verify_source.py
'''


def prepare(root, delivery_name, output):
    root = root.resolve()
    delivery_path = source_file(root, delivery_name)
    delivery = json_file(delivery_path)
    require(delivery.get("status") == "SEALED_EXPLICIT_V3_DELIVERY", "Delivery is not a sealed explicit manifest.")
    rows = delivery["files"]
    require(isinstance(rows, list) and rows, "Delivery file list is empty.")
    names = [relative_name(r["path"]) for r in rows]
    require(len(names) == len(set(names)) == len({n.casefold() for n in names}), "Duplicate delivery members.")
    protected = {"SOURCE-MANIFEST.json", "DELIVERY-MANIFEST.json", "verify_source.py",
                 ".github/workflows/source.yml", ".gitignore", ".gitattributes"}
    require(not protected.intersection(names), "Delivery conflicts with generated source-control objects.")
    by_name = {r["path"]: r for r in rows}
    for row in rows:
        p = source_file(root, row["source"])
        require(p.stat().st_size == row["bytes"] and digest_file(p) == row["sha256"],
                "Delivery source identity changed: " + row["path"])
    require({"SCIENTIFIC-MANIFEST.json", "FRESH-ACCEPTANCE.json"} <= set(names), "Delivery lacks binding objects.")
    sci = json_file(source_file(root, by_name["SCIENTIFIC-MANIFEST.json"]["source"]))
    science_sha = by_name["SCIENTIFIC-MANIFEST.json"]["sha256"]
    require(science_sha == delivery["scientific_manifest_sha256"], "Delivery science hash differs.")
    receipt = json_file(source_file(root, by_name["FRESH-ACCEPTANCE.json"]["source"]))
    receipt_check(receipt, science_sha, sci["files"])
    require(by_name["FRESH-ACCEPTANCE.json"]["sha256"] == delivery["fresh_receipt_sha256"],
            "Delivery fresh receipt hash differs.")
    actual = {r["path"]: {k: r[k] for k in ("path", "bytes", "sha256")} for r in rows}
    for r in sci["files"]:
        require(actual.get(r["path"]) == {k: r[k] for k in ("path", "bytes", "sha256")},
                "Delivery does not cover science: " + r["path"])
    bank = [actual[n] for n in names if n.casefold().endswith(".npz")]
    require(len(bank) == delivery["release_array_objects"], "Release-array count differs.")
    target = root.joinpath(*PurePosixPath(relative_name(output)).parts)
    require(target.resolve().is_relative_to(root) and not target.exists(), "Use a new source output stage.")
    require(not any(source_file(root, r["source"]).resolve().is_relative_to(target.resolve())
                    for r in rows), "Source output must be separate from inputs.")
    target.mkdir()
    keep = []
    for row in rows:
        if row["path"].casefold().endswith(".npz"):
            continue
        p = target.joinpath(*PurePosixPath(row["path"]).parts)
        p.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source_file(root, row["source"]), p)
        keep.append(actual[row["path"]])
    shutil.copyfile(delivery_path, target / "DELIVERY-MANIFEST.json")
    generated = {
        "verify_source.py": VERIFY_SOURCE,
        ".github/workflows/source.yml": WORKFLOW,
        ".gitignore": "__pycache__/\n.cache/\nverification-*/\nfrontier-verification-work-*/\n",
        ".gitattributes": "* -text\n",
    }
    for name, text in generated.items():
        p = target.joinpath(*PurePosixPath(name).parts)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8", newline="\n")
    for name in ["DELIVERY-MANIFEST.json", *generated]:
        p = target / name
        keep.append({"path": name, "bytes": p.stat().st_size, "sha256": digest_file(p)})
    keep.sort(key=lambda r: r["path"])
    bank.sort(key=lambda r: r["path"])
    manifest = {
        "status": "SEALED_SOURCE_IDENTITY_WITH_RELEASE_ONLY_ARRAYS",
        "version": delivery["version"],
        "scientific_manifest_sha256": science_sha,
        "delivery_manifest_sha256": digest_file(delivery_path),
        "source_files": keep,
        "large_data_supplied_in_named_release_archive": bank,
        "expected_release_array_objects": len(bank),
        "release_archive": "Theodore-Ouyang-Heston-V3-Evidence-20261007.zip",
        "ci_scope": "SHA256/size, science/delivery coverage, retained FRESH tested-science and driver/step bindings only. No scientific rerun.",
    }
    write_json(target / "SOURCE-MANIFEST.json", manifest)
    run = subprocess.run([sys.executable, "-B", str(target / "verify_source.py")],
                         capture_output=True, text=True, encoding="utf-8")
    require(run.returncode == 0, "Generated source verifier did not accept the copied fixed identities.")
    require(not any(p.is_file() and p.suffix.casefold() == ".npz" for p in target.rglob("*")),
            "Source publication contains a release-only array.")
    print("PASS prepared source identities;", len(keep), "source objects and", len(bank), "release-only arrays. No Git or publication action.")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, required=True)
    p.add_argument("--delivery", default="delivery-v3/DELIVERY-MANIFEST.json", help="Relative to <ROOT>")
    p.add_argument("--output", default="publication-v3", help="New directory relative to <ROOT>")
    a = p.parse_args()
    try:
        prepare(a.root, a.delivery, a.output)
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as e:
        print("FAIL source preparation: " + str(e).replace(str(a.root.resolve()), "<ROOT>"), file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
