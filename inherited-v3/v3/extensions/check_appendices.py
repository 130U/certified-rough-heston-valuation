"""Check only the new insertion drafts; no environment or execution measurements."""
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
checks = []

def check(condition, name):
    checks.append({"check": name, "pass": bool(condition)})
    if not condition:
        raise AssertionError(name)

drafts = {}
for letter, count in (("f", 30), ("g", 17)):
    for lang in ("en", "zh"):
        name = f"appendix-{letter}-{lang}.md"
        drafts[name] = (HERE / name).read_text(encoding="utf-8")
    en, zh = (drafts[f"appendix-{letter}-{lang}.md"] for lang in ("en", "zh"))
    get_blocks = lambda value: [re.sub(r"\s+", "", x) for x in re.findall(r"\\\[(.*?)\\\]", value, re.S)]
    check(get_blocks(en) == get_blocks(zh), f"{letter.upper()} bilingual display formulas identical")
    get_inline = lambda value: Counter(re.sub(r"\s+", "", x) for x in re.findall(r"\\\((.*?)\\\)", value, re.S))
    check(get_inline(en) == get_inline(zh), f"{letter.upper()} bilingual inline formula multisets identical")
    expected = [f"{letter.upper()}{i:02d}" for i in range(1, count + 1)]
    for lang, value in (("en", en), ("zh", zh)):
        check(re.findall(r"\\tag\{([FG]\d+)\}", value) == expected, f"{letter.upper()} {lang} unique complete tag sequence")
        headings = re.findall(r"^### ([FG]\.\d+)\.", value, re.M)
        check(headings == [f"{letter.upper()}.{i}" for i in range(1, 9 if letter == "f" else 6)], f"{letter.upper()} {lang} complete section sequence")

deny = {
    "private absolute path": r"(?i)[A-Z]:[\\/]+Users[\\/]+[^\s]+",
    "personal email": r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}",
    "personal system specification": r"(?i)\b(?:Intel|AMD Ryzen|Windows\s+\d|RAM|Core Ultra|hard_memory_bytes|max_threads|perf_counter|wall.clock)\b",
    "execution duration": r"(?i)\b(?:elapsed|runtime|execution time|run time|wall time)\b|\d+(?:\.\d+)?\s*(?:milliseconds|seconds|GB)\b",
    "old manuscript localization": r"Appendix [CD]\.|附录\s*[CD][\.。]|directly in the main text|main text.s primal.dual witness",
    "large displayed rational": r"\d{30,}\s*/\s*\d{30,}",
}
for name, value in drafts.items():
    check(bool(re.search(r"^## (?:Appendix [FG]\.|附录 [FG]\.)", value, re.M)), f"{name}: manuscript appendix heading level")
    check(value.count(r"\(") == value.count(r"\)") and value.count(r"\(") > 0, f"{name}: balanced inline delimiters")
    prose = re.sub(r"\\\[.*?\\\]|\\\(.*?\\\)|\x60[^\x60]*\x60", "", value, flags=re.S)
    check(not re.search(r"\\[A-Za-z]+", prose), f"{name}: no raw TeX macro in prose")
    for category, pattern in deny.items():
        check(not re.search(pattern, value), f"{name}: no {category}")

result = {
    "status": "PASS_BILINGUAL_FORMULAS_LABELS_AND_NEW_PROSE_DISCLOSURE_CHECK",
    "scope": "Insertion drafts only; mathematical proofs and saved-reader scopes are reviewed separately.",
    "checks": checks,
    "drafts": [{"path": name, "sha256": hashlib.sha256((HERE / name).read_bytes()).hexdigest(), "inline_math_count": drafts[name].count(r"\("), "display_math_count": drafts[name].count(r"\[")} for name in drafts],
}
(HERE / "APPENDIX-CHECK.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "checks": len(checks), "draft_count": len(drafts)}))
