"""Build the explicit V3.1 editorial source and small overlay; never publish."""
from pathlib import Path, PurePosixPath
import argparse, hashlib, json, os, shutil, sys, zipfile
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from verify_editorial import PARENT, VERSION, require, name, sha, read, record, parent_identities, verify
import verify_editorial as editorial_verifier
ARCHIVE = "Theodore-Ouyang-Heston-V3.1-Editorial-20261007.zip"
CI = """name: Verify editorial and inherited source identities
on:
  push:
    branches: [main]
  workflow_dispatch:
permissions:
  contents: read
jobs:
  editorial-source-identities:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: python -B verify_source.py
"""
def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

def prepare(parent, root, allowlist, output, delivery):
    parent, root = parent.resolve(), root.resolve(); cfg = read(root / name(allowlist))
    require(cfg["version"] == VERSION, "Allowlist version differs.")
    parent_source, science = parent_identities(parent)
    inherited_rows = parent_source["source_files"] + [record(parent, "SOURCE-MANIFEST.json")]
    specs = cfg["editorial_files"]; generated = {"verify_source.py", "verify_editorial.py", ".github/workflows/source.yml", "EDITORIAL-MANIFEST.json", "SOURCE-MANIFEST.json"}
    paths = [name(r["path"]) for r in specs]
    require(len(paths) == len(set(paths)) == len({n.casefold() for n in paths}), "Duplicate editorial output.")
    require(not generated.intersection(paths), "Explicit editorial output collides with a generated member.")
    require(all(not p.startswith("inherited-v3/") and not p.casefold().endswith((".npz", ".zip")) for p in paths), "Overlay includes inherited/large-bank objects.")
    required = {"README.md", "AUTHOR-CHRONOLOGY.md", "EDITORIAL-RESPONSE-ZH.md", "manuscript/merged-heston-en.md", "manuscript/merged-heston-zh.md",
                "paper/Theodore-Ouyang-Merged-Heston-EN.pdf", "paper/Theodore-Ouyang-Merged-Heston-ZH.pdf"}
    require(required <= set(paths), "Missing required editorial manuscript/delivery objects.")
    for r in specs:
        relative_source = name(r["source"])
        require(not relative_source.casefold().endswith((".npz", ".zip")), "Large archive/array cannot be renamed into the editorial layer.")
        record(root, relative_source)
        if r["path"] in required and r["path"].endswith(".pdf"):
            with (root / relative_source).open("rb") as stream:
                require(stream.read(5) == b"%PDF-", "Editorial PDF header is invalid.")
    target, stage = root / name(output), root / name(delivery)
    require(target.resolve().is_relative_to(root) and stage.resolve().is_relative_to(root), "Publication stage escapes root.")
    require(not target.exists() and not stage.exists(), "Use new immutable publication and delivery stages.")
    target.mkdir(); inherited = target / "inherited-v3"; inherited.mkdir()
    for row in inherited_rows:
        src = parent.joinpath(*PurePosixPath(row["path"]).parts)
        require(record(parent, row["path"]) == {k: row[k] for k in ("path", "bytes", "sha256")}, "Parent file changed.")
        dst = inherited.joinpath(*PurePosixPath(row["path"]).parts); dst.parent.mkdir(parents=True, exist_ok=True)
        os.link(src, dst)  # Fixed inherited bytes are never edited or rewritten.
    for r in specs:
        src = root.joinpath(*PurePosixPath(r["source"]).parts); dst = target.joinpath(*PurePosixPath(r["path"]).parts)
        dst.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(src, dst)
    shutil.copyfile(Path(editorial_verifier.__file__), target / "verify_editorial.py")
    (target / "verify_source.py").write_text('"""V3.1 editorial wrapper; retained V3 science is verified separately."""\nfrom verify_editorial import main\nif __name__ == "__main__": main()\n', encoding="utf-8", newline="\n")
    workflow = target / ".github/workflows/source.yml"; workflow.parent.mkdir(parents=True); workflow.write_text(CI, encoding="utf-8", newline="\n")
    overlay_paths = sorted(paths + ["verify_source.py", "verify_editorial.py", ".github/workflows/source.yml"])
    bridge = {"status": "SEALED_EDITORIAL_LAYER_INHERITING_FIXED_V3_SCIENCE", "version": VERSION, "parent": PARENT,
              "inherited_source_prefix": "inherited-v3", "inherited_source_objects": 472, "scientific_input_objects": len(science["files"]),
              "scientific_recomputation": False,
              "scope": "New editorial files are not covered by the old FRESH-ACCEPTANCE. Parent scientific inputs and retained acceptance remain unchanged.",
              "editorial_files": [record(target, p) for p in overlay_paths],
              "overlay_members": sorted(overlay_paths + ["EDITORIAL-MANIFEST.json", "SOURCE-MANIFEST.json"]),
              "overlay_reconstruction": "Overlay omits inherited-v3. Use the complete new source checkout, or place the exact parent source revision under inherited-v3. Science runs from the separately downloaded named V3 scientific archive."}
    write(target / "EDITORIAL-MANIFEST.json", bridge)
    all_paths = ["inherited-v3/" + r["path"] for r in inherited_rows] + overlay_paths + ["EDITORIAL-MANIFEST.json"]
    source = {"status": "SEALED_EDITORIAL_SOURCE_WITH_UNCHANGED_INHERITED_V3", "version": VERSION, "parent": PARENT,
              "editorial_manifest_sha256": sha(target / "EDITORIAL-MANIFEST.json"),
              "source_files": [record(target, p) for p in sorted(all_paths)], "manifest_self_reference": False}
    write(target / "SOURCE-MANIFEST.json", source)
    acceptance = verify(target); stage.mkdir(); write(stage / "EDITORIAL-ACCEPTANCE.json", acceptance)
    members = bridge["overlay_members"]
    archive = stage / ARCHIVE
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for path in members:
            entry = zipfile.ZipInfo(path, (1980, 1, 1, 0, 0, 0)); entry.compress_type = zipfile.ZIP_DEFLATED
            entry.create_system = 3; entry.external_attr = 0o100644 << 16
            with (target / path).open("rb") as src, z.open(entry, "w") as dst: shutil.copyfileobj(src, dst, 1024 * 1024)
    with zipfile.ZipFile(archive) as z:
        require(z.namelist() == members and z.testzip() is None, "Editorial overlay member order/CRC differs.")
        for path in members:
            require(hashlib.sha256(z.read(path)).hexdigest() == sha(target / path), "Editorial overlay identity differs.")
    for path in required:
        if path.endswith(".pdf"): shutil.copyfile(target / path, stage / PurePosixPath(path).name)
    asset_names = sorted([ARCHIVE, "Theodore-Ouyang-Merged-Heston-EN.pdf", "Theodore-Ouyang-Merged-Heston-ZH.pdf"])
    (stage / "SHA256SUMS.txt").write_text("".join(sha(stage / p) + "  " + p + "\n" for p in asset_names), encoding="utf-8", newline="\n")
    write(stage / "EDITORIAL-DELIVERY.json", {"status": "PASS_SMALL_EDITORIAL_OVERLAY_IDENTITIES", "version": VERSION,
          "assets": [record(stage, p) for p in asset_names], "overlay_members": len(members),
          "inherited_members_in_overlay": 0, "npz_members_in_overlay": 0, "scientific_recomputation": False, "parent": PARENT})
    # Recheck all parent identities after materialization and overlay reading.
    parent_identities(parent)
    print("PASS V3.1 editorial source and small overlay; unchanged 450 scientific identities; no scientific rerun.", flush=True)

def main():
    p = argparse.ArgumentParser(description=__doc__); p.add_argument("--parent", type=Path, required=True); p.add_argument("--root", type=Path, required=True)
    p.add_argument("--allowlist", default="editorial-allowlist.json"); p.add_argument("--output", default="publication-v31"); p.add_argument("--delivery", default="delivery-v31")
    a = p.parse_args()
    try: prepare(a.parent, a.root, a.allowlist, a.output, a.delivery)
    except (ValueError, KeyError, OSError, json.JSONDecodeError, zipfile.BadZipFile):
        print("FAIL editorial preparation; preserve the partial stage and inspect the explicit relative allowlist.", file=sys.stderr); raise SystemExit(1)
if __name__ == "__main__": main()
