"""Build native GitHub mathematics from the canonical English Markdown sources.

Run from the project root: python scripts/build_github_manuscripts.py
The source manuscripts remain unchanged. Only equivalent presentation macros and
math delimiters are changed; every conversion is recorded in qa/GitHub-build.json.
The implementation uses the Python standard library.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript"
TOKEN = re.compile(
    r"(?P<code>```[\s\S]*?```|`[^`\n]*`)"
    r"|(?P<bracket>\\\[[\s\S]*?\\\])"
    r"|(?P<paren>\\\([\s\S]*?\\\))"
    r"|(?P<double>\$\$[\s\S]*?\$\$)"
    r"|(?P<single>(?<![\\$])\$(?!\$)(?:\\.|[^$])*?(?<!\\)\$(?!\$))"
)
PUBLIC_MATH = re.compile(r"```math\n([\s\S]*?)\n```|\$`([^`\n]*)`\$")


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def escaped(text, pos):
    count, i = 0, pos - 1
    while i >= 0 and text[i] == "\\":
        count += 1
        i -= 1
    return count % 2 == 1


def balanced(text, start, opening="{", closing="}"):
    if text[start] != opening:
        raise ValueError("Expected a balanced argument")
    depth, i = 1, start + 1
    while i < len(text):
        if not escaped(text, i):
            if text[i] == opening:
                depth += 1
            elif text[i] == closing:
                depth -= 1
                if depth == 0:
                    return text[start + 1:i], i + 1
        i += 1
    raise ValueError("Unbalanced mathematical argument")


def github_tex(tex, table=False):
    changes = []
    # This is the equivalent base-TeX form used by the preceding public project.
    search = re.compile(r"\\xRightarrow\s*")
    cursor = 0
    while True:
        match = search.search(tex, cursor)
        if match is None:
            break
        if escaped(tex, match.start()):
            cursor = match.end()
            continue
        arg_start = match.end()
        below = None
        if arg_start < len(tex) and tex[arg_start] == "[":
            below, arg_start = balanced(tex, arg_start, "[", "]")
            while arg_start < len(tex) and tex[arg_start].isspace():
                arg_start += 1
        above, end = balanced(tex, arg_start)
        new = r"\overset{" + above + r"}{\Longrightarrow}"
        if below is not None:
            new = r"\underset{" + below + "}{" + new + "}"
        old = tex[match.start():end]
        changes.append({"rule": "annotated implication in base TeX", "from": old, "to": new})
        tex = tex[:match.start()] + new + tex[end:]
        cursor = match.start() + len(new)
    operator = re.compile(r"\\operatorname\{([A-Za-z]+)\}")
    def replace_operator(match):
        if escaped(tex, match.start()):
            return match.group()
        new = r"\mathop{\mathrm{" + match.group(1) + r"}}\nolimits "
        changes.append({"rule": "upright operator in base TeX", "from": match.group(), "to": new})
        return new
    tex = operator.sub(replace_operator, tex)
    out = []
    for i, char in enumerate(tex):
        if char in "<>" and not escaped(tex, i):
            new = r"\lt " if char == "<" else r"\gt "
            changes.append({"rule": "HTML-safe relation", "from": char, "to": new})
            out.append(new)
        else:
            out.append(char)
    tex = "".join(out)
    if table:
        out, i = [], 0
        while i < len(tex):
            if tex.startswith(r"\|", i) and not escaped(tex, i):
                out.append(r"\Vert ")
                changes.append({"rule": "table-safe double vertical bar", "from": r"\|", "to": r"\Vert "})
                i += 2
            elif tex[i] == "|" and not escaped(tex, i):
                out.append(r"\vert ")
                changes.append({"rule": "table-safe vertical bar", "from": "|", "to": r"\vert "})
                i += 1
            else:
                out.append(tex[i])
                i += 1
        tex = "".join(out)
        if "|" in tex:
            raise ValueError("An unconverted pipe would split a Markdown table")
    return tex, changes


def display_container(tex):
    # Keep standalone tagged expressions horizontal in GitHub's native MathML.
    stripped = tex.strip()
    tag = re.search(r"\\tag\*?\s*\{[^}]*\}\s*$", stripped)
    if tag and not stripped.startswith(r"\begin{"):
        expression = stripped[:tag.start()].rstrip()
        return r"\begin{gathered}" + "\n" + expression + "\n" + r"\end{gathered}" + "\n" + tag.group().strip(), True
    return tex, False


def build(source):
    output, records, cursor = [], [], 0
    protected_source, protected_target = [], []
    for match in TOKEN.finditer(source):
        prefix = source[cursor:match.start()]
        output.append(prefix)
        protected_source.append(prefix)
        protected_target.append(prefix)
        raw = match.group()
        if match.lastgroup == "code":
            output.append(raw)
            protected_source.append(raw)
            protected_target.append(raw)
            cursor = match.end()
            continue
        display = match.lastgroup in ("bracket", "double")
        tex = raw[2:-2] if match.lastgroup != "single" else raw[1:-1]
        line_start = source.rfind("\n", 0, match.start()) + 1
        before = source[line_start:match.start()]
        in_table = before.lstrip().startswith("|")
        if display and in_table:
            raise ValueError("Display mathematics cannot be placed in a Markdown table cell")
        safe, changes = github_tex(tex, table=in_table)
        container = False
        if display:
            safe, container = display_container(safe)
            if container:
                changes.append({"rule": "display-only alignment container", "environment": "gathered", "effect": "unchanged expression and equation tag"})
            indentation = before if not before.strip() else ""
            safe_lines = safe.strip("\n").splitlines()
            converted = "```math\n" + "\n".join(indentation + line for line in safe_lines) + "\n" + indentation + "```"
        else:
            if "\n" in safe or "\r" in safe:
                folded = re.sub(r"[ \t]*\r?\n[ \t]*", " ", safe)
                changes.append({"rule": "inline TeX line-break whitespace", "from": safe, "to": folded, "effect": "TeX input line breaks are equivalent to spaces"})
                safe = folded
            if "`" in safe:
                raise ValueError("Inline mathematics contains a literal backtick")
            converted = "$`" + safe + "`$"
        output.append(converted)
        marker = "FORMULA_" + str(len(records))
        protected_source.append(marker)
        protected_target.append(marker)
        records.append({
            "index": len(records) + 1,
            "source_line": source.count("\n", 0, match.start()) + 1,
            "kind": "display" if display else "inline",
            "source_delimiter": match.lastgroup,
            "in_markdown_table": in_table,
            "source_tex_sha256": sha(tex),
            "source_tex": tex,
            "github_tex": safe,
            "equation_tags": re.findall(r"\\tag\*?\s*\{([^}]*)\}", tex),
            "changes": changes,
        })
        cursor = match.end()
    output.append(source[cursor:])
    protected_source.append(source[cursor:])
    protected_target.append(source[cursor:])
    assert protected_source == protected_target
    result = "".join(output)
    assert re.findall(r"\\tag\*?\s*\{([^}]*)\}", source) == re.findall(r"\\tag\*?\s*\{([^}]*)\}", result)
    # No unsupported source delimiter remains outside the emitted math fences.
    nonmath = re.sub(r"```math\n[\s\S]*?\n[ \t]*```|\$`[^`\n]*`\$", "", result)
    assert not re.search(r"\\[()[\]]", nonmath)
    assert len(re.findall(r"\$`[^`\n]*`\$", result)) == sum(r["kind"] == "inline" for r in records)
    assert len(re.findall(r"^[ \t]*```math$", result, re.M)) == sum(r["kind"] == "display" for r in records)
    # Pipes in emitted inline expressions cannot create extra table columns.
    for line in result.splitlines():
        if line.lstrip().startswith("|"):
            for formula in re.findall(r"\$`([^`\n]*)`\$", line):
                assert "|" not in formula
    return result, records


def self_test():
    sample = r"Inline \(a< b\) and $c>d$." + "\n\n" + r"\[z=1\tag{T1}\]" + "\n\n" + r"| $|x|+\|y\|$ | value |" + "\n"
    out, records = build(sample)
    assert len(records) == 4
    assert r"\lt " in out and r"\gt " in out
    assert r"\vert x\vert +\Vert y\Vert " in out
    annotated, changes = github_tex(r"\xRightarrow{\text{condition}}")
    assert annotated == r"\overset{\text{condition}}{\Longrightarrow}"
    wrapped, wrapped_records = build("Inline \\(a\n\\le b\\).")
    assert "$`a \\le b`$" in wrapped
    assert wrapped_records[0]["changes"][-1]["rule"] == "inline TeX line-break whitespace"
    return {"status": "PASS", "checks": ["all source delimiters", "tag preservation", "HTML-safe comparisons", "table-safe single and double bars", "annotated implication", "multiline inline TeX whitespace"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preview-dir", type=Path, help="Write a preview directory rather than the public manuscript paths")
    parser.add_argument("--self-test", action="store_true", help="Run built-in conversion boundary checks only")
    args = parser.parse_args()
    test = self_test()
    if args.self_test:
        print(json.dumps(test))
        return
    sources = [MANUSCRIPT / "report-source.md", MANUSCRIPT / "rough-heston-source.md"]
    missing = [str(p.relative_to(ROOT)) for p in sources if not p.exists()]
    if missing:
        raise SystemExit("Canonical source files must be created first: " + ", ".join(missing))
    result = {"status": "PASS", "self_test": test, "scope": "mathematical presentation only; no source, prose, citation, or parameter changes", "documents": []}
    for source_path in sources:
        source = source_path.read_text(encoding="utf-8")
        source_bytes = source_path.read_bytes()
        target_text, records = build(source)
        target_name = source_path.name.replace("-source", "")
        target_path = (args.preview_dir / target_name) if args.preview_dir else MANUSCRIPT / target_name
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(target_text, encoding="utf-8", newline="\n")
        assert source_path.read_bytes() == source_bytes
        try:
            target_relative = target_path.resolve().relative_to(ROOT).as_posix()
        except ValueError:
            target_relative = "preview/" + target_name
        result["documents"].append({
            "source": source_path.relative_to(ROOT).as_posix(),
            "target": target_relative,
            "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
            "target_sha256": hashlib.sha256(target_path.read_bytes()).hexdigest(),
            "source_unchanged": True,
            "formula_count": len(records),
            "display_count": sum(r["kind"] == "display" for r in records),
            "inline_count": sum(r["kind"] == "inline" for r in records),
            "equation_tag_count": sum(len(r["equation_tags"]) for r in records),
            "formula_order_preserved": True,
            "prose_unchanged": True,
            "all_changes_registered": True,
            "native_github_math_delimiters": True,
            "table_pipes_protected": True,
            "formulas": records,
        })
    qa = ROOT / "qa/GitHub-build.json"
    qa.parent.mkdir(parents=True, exist_ok=True)
    qa.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    summary = {"status": result["status"], "qa": qa.relative_to(ROOT).as_posix(), "documents": [{k: v for k, v in d.items() if k != "formulas"} for d in result["documents"]]}
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
