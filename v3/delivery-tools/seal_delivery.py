"""Seal an explicit allowlist without editing its scientific inputs or publishing.

All stored source references are relative to --root. ZIP member metadata are fixed.
See README.md for the allowlist schema and intended execution boundaries.
"""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json
import shutil
import sys
import zipfile


ARCHIVE_NAME = "Theodore-Ouyang-Heston-V3-Evidence-20261007.zip"
PDF_NAMES = (
    "Theodore-Ouyang-Merged-Heston-EN.pdf",
    "Theodore-Ouyang-Merged-Heston-ZH.pdf",
)
FRESH_STATUS = "PASS_FRESH_COMPLETE_SCIENTIFIC_ACCEPTANCE"
FORBIDDEN = {".git", ".cache", "__pycache__", "cache", "caches", "tmp", "temp"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def relative_name(value):
    require(isinstance(value, str) and value and "\\" not in value,
            "Use nonempty forward-slash relative names.")
    p = PurePosixPath(value)
    require(not p.is_absolute() and ":" not in value and not any(
        part in {"", ".", ".."} for part in value.split("/")),
        "Unsafe relative name: " + value)
    require(all(part.casefold() not in FORBIDDEN and not part.casefold().startswith(
        ("verification-", "frontier-verification-work-", "temporary-")) for part in p.parts),
        "Temporary/cache/verification member is forbidden: " + value)
    require(not value.casefold().endswith((".pyc", ".pyo", ".tmp", ".temp", ".partial")),
            "Temporary file suffix is forbidden: " + value)
    return value


def source_file(root, value):
    relative_name(value)
    p = root.joinpath(*PurePosixPath(value).parts)
    require(p.resolve().is_relative_to(root), "Source escapes <ROOT>: " + value)
    require(p.is_file(), "Missing source: " + value)
    return p


def digest_file(p):
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def json_file(p):
    return json.loads(p.read_text(encoding="utf-8"))


def write_json(p, value):
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def receipt_check(receipt, science_sha, science_rows):
    require(receipt.get("status") == FRESH_STATUS, "Fresh acceptance is not a complete PASS.")
    require(receipt.get("tested_scientific_manifest_sha256") == science_sha,
            "Fresh acceptance does not bind the supplied scientific manifest.")
    identities = {r["path"]: r for r in science_rows}
    require(receipt.get("driver_sha256") == identities.get("reproduce.py", {}).get("sha256"),
            "Fresh acceptance driver identity differs from fixed science.")
    steps = receipt.get("steps")
    require(isinstance(steps, list) and steps, "Fresh acceptance has no executed steps.")
    for step in steps:
        require(step.get("returncode") == 0, "Fresh acceptance contains a failed step.")
        script = relative_name(step.get("script", ""))
        require(script in identities and step.get("source_sha256") == identities[script]["sha256"],
                "Fresh step source identity differs from fixed science: " + script)
    require(receipt.get("scientific_input_objects") == len(science_rows),
            "Fresh acceptance scientific object count differs.")


def seal(root, allow_path, output):
    root = root.resolve()
    cfg = json_file(source_file(root, allow_path))
    science_source = relative_name(cfg.get("scientific_manifest", "evidence-v3/SCIENTIFIC-MANIFEST.json"))
    science_path = source_file(root, science_source)
    science = json_file(science_path)
    science_rows = science["files"]
    require(isinstance(science_rows, list) and science_rows, "Scientific allowlist is empty.")
    science_prefix = str(PurePosixPath(science_source).parent)
    rows = {}
    case_names = set()

    def add(source, member, expected=None):
        source, member = relative_name(source), relative_name(member)
        require(member not in rows and member.casefold() not in case_names,
                "Duplicate or case-colliding member: " + member)
        p = source_file(root, source)
        row = {"path": member, "bytes": p.stat().st_size, "sha256": digest_file(p), "source": source}
        if expected is not None:
            require(expected.get("path") == member and expected.get("bytes") == row["bytes"]
                    and expected.get("sha256") == row["sha256"],
                    "Fixed scientific identity changed: " + member)
        rows[member] = row
        case_names.add(member.casefold())

    for old in science_rows:
        name = relative_name(old["path"])
        add(str(PurePosixPath(science_prefix) / name), name, old)
    add(science_source, "SCIENTIFIC-MANIFEST.json")
    for extra in cfg.get("extra_files", []):
        require(set(extra) == {"source", "path"}, "An extra entry must contain exactly source and path.")
        add(extra["source"], extra["path"])

    fresh_spec = cfg["fresh_receipt"]
    require(set(fresh_spec) == {"source", "path"} and fresh_spec["path"] == "FRESH-ACCEPTANCE.json",
            "fresh_receipt must have source and path=FRESH-ACCEPTANCE.json.")
    add(fresh_spec["source"], fresh_spec["path"])
    fresh = json_file(source_file(root, fresh_spec["source"]))
    science_sha = digest_file(science_path)
    receipt_check(fresh, science_sha, science_rows)

    pdf_specs = cfg["pdf_assets"]
    require(isinstance(pdf_specs, list) and len(pdf_specs) == 2,
            "Exactly two PDF assets must be explicitly listed.")
    require({r.get("name") for r in pdf_specs} == set(PDF_NAMES),
            "Use the two consistent final PDF asset names.")
    for spec in pdf_specs:
        require(set(spec) == {"source", "name"}, "A PDF asset must contain exactly source and name.")
        require(source_file(root, spec["source"]).read_bytes()[:5] == b"%PDF-", "Invalid PDF header.")
        add(spec["source"], "paper/" + spec["name"])
    require({r["path"] for r in rows.values() if r["path"].casefold().endswith(".pdf")}
            >= {"paper/" + n for n in PDF_NAMES}, "Missing final PDF members.")
    for name in PDF_NAMES:
        require(sum(PurePosixPath(n).name == name for n in rows) == 1,
                "Final PDF appears under more than one member path: " + name)

    expected_arrays = cfg.get("expected_release_arrays", 27)
    arrays = [r for r in rows.values() if r["path"].casefold().endswith(".npz")]
    require(len(arrays) == expected_arrays, "Unexpected release-array object count.")
    require("DELIVERY-MANIFEST.json" not in rows, "Delivery manifest must not list itself.")
    output_name = relative_name(output)
    target = root.joinpath(*PurePosixPath(output_name).parts)
    require(target.resolve().is_relative_to(root), "Output escapes <ROOT>.")
    require(not target.exists(), "Output directory already exists; use a new delivery stage.")
    require(not any(source_file(root, r["source"]).resolve().is_relative_to(target.resolve())
                    for r in rows.values()), "Output must be separate from all inputs.")

    ordered = sorted(rows.values(), key=lambda r: r["path"])
    manifest = {
        "status": "SEALED_EXPLICIT_V3_DELIVERY",
        "version": cfg.get("version", "v3.0.0-research-20261007"),
        "scientific_manifest_sha256": science_sha,
        "fresh_receipt_sha256": rows["FRESH-ACCEPTANCE.json"]["sha256"],
        "source_reference": "Every source is a path relative to <ROOT>; no source filesystem metadata is retained.",
        "files": ordered,
        "release_array_objects": len(arrays),
        "assets": [*PDF_NAMES, ARCHIVE_NAME, "SHA256SUMS.txt"],
        "verification_scope": "ZIP CRC, exact member set, sizes and SHA256; retained fresh acceptance identity. No scientific recomputation is performed by this sealer.",
    }
    target.mkdir()
    mf = target / "DELIVERY-MANIFEST.json"
    write_json(mf, manifest)
    for name in PDF_NAMES:
        source = rows["paper/" + name]
        shutil.copyfile(source_file(root, source["source"]), target / name)
        require(digest_file(target / name) == source["sha256"], "Copied PDF identity changed.")
    archive = target / ARCHIVE_NAME
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for row in ordered + [{"path": "DELIVERY-MANIFEST.json", "source": None}]:
            entry = zipfile.ZipInfo(row["path"], (1980, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            p = mf if row["source"] is None else source_file(root, row["source"])
            with p.open("rb") as src, z.open(entry, "w") as dst:
                shutil.copyfileobj(src, dst, 1024 * 1024)
    with zipfile.ZipFile(archive) as z:
        expected = [r["path"] for r in ordered] + ["DELIVERY-MANIFEST.json"]
        require(z.namelist() == expected, "Archive member list/order changed.")
        require(z.testzip() is None, "Archive CRC verification failed.")
        require(z.read("DELIVERY-MANIFEST.json") == mf.read_bytes(), "Archive manifest bytes changed.")
        for row in ordered:
            h = hashlib.sha256()
            with z.open(row["path"]) as f:
                for chunk in iter(lambda: f.read(1024 * 1024), b""):
                    h.update(chunk)
            info = z.getinfo(row["path"])
            require(info.file_size == row["bytes"] and h.hexdigest() == row["sha256"],
                    "Archive member identity changed: " + row["path"])
            require(info.date_time == (1980, 1, 1, 0, 0, 0), "Archive member date is not fixed.")
        # Recheck original fixed objects after all reads, preventing an unnoticed input race.
        for row in ordered:
            p = source_file(root, row["source"])
            require(p.stat().st_size == row["bytes"] and digest_file(p) == row["sha256"],
                    "Source changed during sealing: " + row["path"])
    sums = "".join(digest_file(target / n) + "  " + n + "\n" for n in [*PDF_NAMES, ARCHIVE_NAME])
    (target / "SHA256SUMS.txt").write_text(sums, encoding="utf-8", newline="\n")
    print("PASS sealed delivery: exact member identities, CRC and fixed ZIP dates;", len(ordered), "members.")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, required=True)
    p.add_argument("--allowlist", required=True, help="JSON path relative to <ROOT>")
    p.add_argument("--output", default="delivery-v3", help="New output directory relative to <ROOT>")
    a = p.parse_args()
    try:
        seal(a.root, a.allowlist, a.output)
    except (ValueError, KeyError, OSError, json.JSONDecodeError, zipfile.BadZipFile) as e:
        message = str(e).replace(str(a.root.resolve()), "<ROOT>")
        print("FAIL delivery: " + message, file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
