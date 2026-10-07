"""Read-only integrity, portability, and document-link checks for this supplement."""
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
manifest = json.loads((HERE / "MANIFEST.json").read_text())
assert manifest["scope"] == "Classical supplement only; independent of the rough-Heston evidence manifest."
for name, expected in manifest["files"].items():
    if name == 'manuscript/merged-heston-en.md':
        path = next((p / name for p in [ROOT, *ROOT.parents] if (p / name).is_file()), None)
        assert path is not None, name
    else:
        path = ROOT / name
    assert path.is_file(), name
    assert hashlib.sha256(path.read_bytes()).hexdigest() == expected, name
    text = path.read_text(encoding="utf-8-sig")
    assert not re.search(r"[\u3400-\u9fff]", text), name
    assert not re.search(r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]", text), name
    if path.suffix == ".json":
        json.loads(text)
    if path.suffix == ".md":
        for target in re.findall(r"(?<![A-Za-z0-9\\])\[[^\]\n]+\]\(([^)]+)\)", text):
            assert not target.startswith(("file:", "C:")), target
            if not re.match(r"[a-z]+://", target):
                target_file = target.split("#")[0]
                assert any((base / target_file).resolve().is_file() for base in [path.parent, path.parent.parent]), target
print(json.dumps({
    "status": "PASS_CLASSICAL_PACKAGE_INTEGRITY",
    "checked_files": len(manifest["files"]),
    "private_absolute_paths": 0,
    "CJK_characters": 0,
    "all_document_links_resolve": True,
    "scope": manifest["scope"],
}))
