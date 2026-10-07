"""Verify an editorial source layer and its unchanged inherited V3 identities.

This entry verifies files and retained evidence. It does not rerun science.
"""
from pathlib import Path, PurePosixPath
import argparse, hashlib, json, re, subprocess, sys
sys.dont_write_bytecode = True

PARENT = {
    "source_revision": "027c42d89d6741ff00347074e559bf0faaf46797",
    "source_tree": "3f83b4c6554a20c8fb40bee3661774ddfa386a02",
    "release_tag": "v3.0.0-research-20261007",
    "source_manifest_sha256": "51a0c0529dfffafa038c2911a03b19cc2365a3179533737141e3fe7d5d688a29",
    "scientific_manifest_sha256": "788513e8a6a1cbe6e2a086dbb80d25b7da1864f7419b1f3bb7668ab1dc16639b",
    "fresh_acceptance_sha256": "1fa7d09c4fed6b87ad758ab04eb3439bb535d561bdc9fa29dbc4958b2c541d03",
    "delivery_manifest_sha256": "f35c7b8c7e64ff65a682ddd07db4eb04722145a18f9c7e3db5b6c50827f0343c",
    "science_archive_name": "Theodore-Ouyang-Heston-V3-Evidence-20261007.zip",
    "science_archive_bytes": 701213852,
    "science_archive_sha256": "f4c038b736ec01b3dd9c4e2dcff733665b5b7997f99ee26b64eb5cff0f2ab120",
}
VERSION = "v5.0.0-editorial-20261007"
PREDECESSOR = {'version': 'v3.1.0-editorial-20261007', 'source_revision': '09c73d2733ee44a1bdd93e49920f15ef9cd0334b'}

def require(ok, message):
    if not ok: raise ValueError(message)

def name(value):
    require(isinstance(value, str) and value and "\\" not in value, "Invalid relative member.")
    p = PurePosixPath(value)
    require(not p.is_absolute() and ":" not in value and
            all(x not in {"", ".", ".."} for x in value.split("/")), "Unsafe relative member.")
    return value

def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""): h.update(chunk)
    return h.hexdigest()

def read(path): return json.loads(path.read_text(encoding="utf-8"))
def identity(row): return {k: row[k] for k in ("path", "bytes", "sha256")}
def record(root, relative):
    relative = name(relative); p = root.joinpath(*PurePosixPath(relative).parts)
    require(p.resolve().is_relative_to(root.resolve()) and p.is_file(), "Missing/escaping member: " + relative)
    return {"path": relative, "bytes": p.stat().st_size, "sha256": sha(p)}

def parent_identities(root):
    checks = {"SOURCE-MANIFEST.json": "source_manifest_sha256", "SCIENTIFIC-MANIFEST.json": "scientific_manifest_sha256",
              "FRESH-ACCEPTANCE.json": "fresh_acceptance_sha256", "DELIVERY-MANIFEST.json": "delivery_manifest_sha256"}
    for path, key in checks.items(): require(sha(root / path) == PARENT[key], "Inherited parent identity differs: " + path)
    source, science = read(root / "SOURCE-MANIFEST.json"), read(root / "SCIENTIFIC-MANIFEST.json")
    require(len(source["source_files"]) == 471 and len(science["files"]) == 450, "Inherited object counts differ.")
    arrays = source["large_data_supplied_in_named_release_archive"]
    require(len(arrays) == 27, "Inherited release-only array count differs.")
    available = {r["path"]: identity(r) for r in source["source_files"] + arrays}
    require(all(available.get(r["path"]) == identity(r) for r in science["files"]), "Inherited scientific coverage differs.")
    return source, science


CORE_YEARS = {"underlying_research": 2023, "principal_article_writing": 2024, "github_upload": 2026}
CORE_STATEMENTS = {
    "en": ["underlying research was conducted in 2023", "principal articles were written in 2024", "materials were uploaded to GitHub in 2026"],
    "zh": ["基础研究开展于2023年", "主要文章撰写于2024年", "材料于2026年上传GitHub"],
}

def normalized(text): return re.sub(r"[\s*]", "", text).casefold()

def chronology(root):
    data = read(root / "CHRONOLOGY.json")
    require(data["schema"] == "author-chronology-v1" and data["version"] == VERSION,
            "Chronology schema/version differs.")
    require(data["author"] == "Theodore Ouyang" and data["core_years"] == CORE_YEARS,
            "Research/writing/upload chronology differs.")
    require(data["core_statements"] == CORE_STATEMENTS, "Core chronology statements differ.")
    revision = data["merged_revision"]
    require(revision["year"] == 2026 and revision["retrospectively_attributed_to_2023_or_2024"] is False,
            "Merged revision chronology differs.")
    require(revision["scope"] == ["merged proof strengthening", "scientific code", "numerical experiments", "evidence assembly", "author-side verification"],
            "Merged revision scope differs.")
    edition = data["editorial_edition"]
    require(edition["date"] == "2026-10-07" and edition["scientific_recomputation"] is False,
            "Editorial date/scope differs.")
    require(data["dated_writing_is_not_a_date_for_all_merged_proofs_code_or_evidence"] is True,
            "Writing and later additions must remain distinct.")
    checked = []
    for path, language, section in [
        ("README.md", "en", None), ("README.md", "zh", None),
        ("AUTHOR-CHRONOLOGY.md", "en", None), ("AUTHOR-CHRONOLOGY.md", "zh", None),
        ("manuscript/merged-heston-en.md", "en", "## Appendix H."),
        ("manuscript/merged-heston-zh.md", "zh", "## 附录 H."),
    ]:
        text = (root / path).read_text(encoding="utf8")
        if section:
            require(section in text, "Missing chronology appendix: " + path)
            text = text.split(section, 1)[1].split("\n## ", 1)[0]
        compact = normalized(text)
        alternatives = [[statement] for statement in CORE_STATEMENTS[language]]
        if language == "zh":
            alternatives = [[a, b] for a, b in zip(CORE_STATEMENTS["zh"],
                ["2023年开展基础研究", "2024年主要撰写文章", "2026年将材料上传GitHub"])]
        require(all(any(normalized(statement) in compact for statement in candidates) for candidates in alternatives),
                "Core chronology text differs: " + path)
        if section:
            require("2026" in compact and ("proof" if language == "en" else "证明") in compact,
                    "Merged revision scope missing: " + path)
        checked.append({"path": path, "language": language})
    return {"status": "PASS_DISTINCT_RESEARCH_WRITING_UPLOAD_AND_REVISION_CHRONOLOGY",
            "core_years": CORE_YEARS, "merged_revision_year": 2026,
            "chronology_sha256": sha(root / "CHRONOLOGY.json"), "checked_texts": checked}

def verify(root):
    root = root.resolve(); source = read(root / "SOURCE-MANIFEST.json"); bridge = read(root / "EDITORIAL-MANIFEST.json")
    require(source["version"] == bridge["version"] == VERSION, "Editorial version differs.")
    require(bridge["parent"] == PARENT and source["parent"] == PARENT, "Fixed parent bridge differs.")
    require(bridge["preceding_editorial"] == source["preceding_editorial"] == PREDECESSOR, "Preceding editorial identity differs.")
    date_check = chronology(root)
    require(bridge["chronology_sha256"] == date_check["chronology_sha256"], "Chronology bridge identity differs.")
    require(bridge["scientific_recomputation"] is False, "This layer cannot claim a new scientific run.")
    require(bridge["scientific_input_objects"] == 450, "Frozen science count differs.")
    require(source["editorial_manifest_sha256"] == sha(root / "EDITORIAL-MANIFEST.json"), "Editorial bridge identity differs.")
    rows = source["source_files"]; names = [name(r["path"]) for r in rows]
    require("SOURCE-MANIFEST.json" not in names and len(names) == len(set(names)) == len({n.casefold() for n in names}),
            "Source manifest self-reference or duplicate.")
    require(all(record(root, r["path"]) == identity(r) for r in rows), "Editorial source SHA/size differs.")
    editorial = {r["path"]: identity(r) for r in bridge["editorial_files"]}
    require(len(editorial) == len(bridge["editorial_files"]), "Duplicate editorial identity.")
    new_rows = {r["path"]: identity(r) for r in rows if not r["path"].startswith("inherited-v3/") and r["path"] != "EDITORIAL-MANIFEST.json"}
    require(editorial == new_rows, "Editorial/source member coverage differs.")
    require(bridge["overlay_members"] == sorted(list(editorial) + ["EDITORIAL-MANIFEST.json", "SOURCE-MANIFEST.json"]),
            "Editorial overlay coverage differs.")
    inherited = root / "inherited-v3"; parent, science = parent_identities(inherited)
    expected = {"inherited-v3/" + r["path"]: identity(r) for r in parent["source_files"]}
    expected["inherited-v3/SOURCE-MANIFEST.json"] = record(inherited, "SOURCE-MANIFEST.json")
    actual = {r["path"]: r for r in rows if r["path"].startswith("inherited-v3/")}
    require(set(actual) == set(expected) and len(actual) == 472, "Inherited source member set differs.")
    for path, old in expected.items(): require(actual[path]["bytes"] == old["bytes"] and actual[path]["sha256"] == old["sha256"], "Inherited bytes differ: " + path)
    require(not any((inherited / r["path"]).exists() for r in parent["large_data_supplied_in_named_release_archive"]), "Large release array was materialized in inherited source.")
    run = subprocess.run([sys.executable, "-B", "verify_source.py"], cwd=inherited,
                         capture_output=True, text=True, encoding="utf-8")
    require(run.returncode == 0, "Original inherited V3 source verifier failed.")
    return {"status": "PASS_EDITORIAL_LAYER_AND_UNCHANGED_INHERITED_V3_IDENTITIES", "version": VERSION,
            "source_objects": len(rows), "inherited_source_objects": 472, "scientific_input_objects": len(science["files"]),
            "parent": PARENT, "preceding_editorial": PREDECESSOR, "chronology": date_check, "editorial_manifest_sha256": sha(root / "EDITORIAL-MANIFEST.json"),
            "source_manifest_sha256": sha(root / "SOURCE-MANIFEST.json"), "scientific_recomputation": False}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    try:
        result = verify(args.root)
        if args.receipt: args.receipt.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
        print(result["status"], flush=True)
    except (ValueError, KeyError, OSError, json.JSONDecodeError):
        print("FAIL editorial source identities; inspect fixed relative manifests.", file=sys.stderr)
        raise SystemExit(1)
if __name__ == "__main__": main()
