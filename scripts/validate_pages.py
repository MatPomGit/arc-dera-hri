"""Fail-closed whitelist for the public DERA-HRI MkDocs site.

No network or publication. Static checks do not replace review of final Pages visibility.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
POLICY = "config/pages-policy.json"
ALLOWED_EXT = {".md", ".css", ".png", ".jpg", ".jpeg", ".svg", ".webp", ".avif"}
FORBIDDEN_CONTENT = (
    re.compile(r"\bAGENTS\.md\b|\bCONTRIBUTING(?:\.md)?\b", re.I),
    re.compile(r"\b(?:TODO|FIXME|REPLACE(?:_[A-Z0-9_]+)?|NOT_RUN|NOT_VERIFIED)\b", re.I),
    re.compile(r"(?i)(?:dla agenta\s*:|agent\s*:\s*(?:wykonaj|dodaj|popraw|zmień)|"
               r"agent workflow|agent instructions|system prompt|developer instructions|"
               r"procedura autonomicznych agentów|zasady pracy agentów|"
               r"uwagi? redakcyjne|notatka dla autora|how to contribute)"),
    re.compile(r"(?i)(?:\.\./docs/|/docs/development/|/\.github/|/secrets/)"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
)
BLOCKED_CONFIG = (
    re.compile(r"(?m)^\s*(?:hooks|watch|exclude_docs|plugins\.|extra_javascript):"),
    re.compile(r"(?m)^\s*-\s*(?:include-markdown|macros|gen-files|literate-nav):"),
)


def safe_file(value: object) -> bool:
    if not isinstance(value, str) or not value or "\\" in value or "\x00" in value:
        return False
    path = PurePosixPath(value)
    return (not path.is_absolute() and not any(x in {"..", "."} or x.startswith(".")
                for x in path.parts)
            and path.suffix.lower() in ALLOWED_EXT
            and not any(x.lower() in {"docs", "development", "private", "research"}
                        for x in path.parts))


def check_pages(root: Path = ROOT, built: Path | None = None) -> list[str]:
    root = Path(root).resolve()
    issues: list[str] = []
    try:
        data = json.loads((root / POLICY).read_text(encoding="utf-8"))
    except (ValueError, UnicodeError, OSError):
        return ["PAGES POLICY: unreadable or invalid JSON"]
    if not isinstance(data, dict) or type(data.get("schema_version")) is not int or data["schema_version"] != 1:
        return ["PAGES POLICY: unsupported version"]
    allowed = data.get("public_files")
    if not isinstance(allowed, list) or not allowed or not all(safe_file(x) for x in allowed):
        return ["PAGES POLICY: invalid public_files"]
    if len(allowed) != len(set(allowed)) or "index.md" not in allowed:
        issues.append("PAGES POLICY: duplicate or missing index.md")
    if (data.get("source_dir"), data.get("output_dir")) != ("pages", "site"):
        issues.append("PAGES POLICY: invalid source/output boundary")
    try:
        config = (root / "mkdocs.yml").read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return ["PAGES CONFIG: cannot read mkdocs.yml"]
    for key, expected in (("docs_dir", "pages"), ("site_dir", "site")):
        matches = re.findall(r"(?m)^" + re.escape(key) + r":\s*(\S+)\s*$", config)
        if matches != [expected]:
            issues.append(f"PAGES CONFIG: {key} must equal {expected} exactly")
    if any(p.search(config) for p in BLOCKED_CONFIG):
        issues.append("PAGES CONFIG: unreviewed import/hook settings")
    navfiles = re.findall(r"(?m)^\s*-\s+[^:\n]+:\s*([-\w/]+\.md)\s*$", config)
    if not navfiles or any(n not in allowed for n in navfiles) or "index.md" not in navfiles:
        issues.append("PAGES CONFIG: navigation uses unapproved files")
    src = root / "pages"
    if not src.is_dir() or src.is_symlink():
        return sorted(set(issues + ["PAGES SOURCE: missing or symlink"]))
    present: set[str] = set()
    for item in sorted(src.rglob("*")):
        rel = item.relative_to(src).as_posix()
        if item.is_symlink():
            issues.append("PAGES SYMLINK: " + rel)
            continue
        if item.is_dir():
            continue
        if rel not in allowed or not safe_file(rel):
            issues.append("PAGES UNAPPROVED FILE: " + rel)
            continue
        present.add(rel)
        try:
            text = item.read_text(encoding="utf-8") if item.suffix in {".md", ".css", ".svg"} else ""
        except (OSError, UnicodeError):
            issues.append("PAGES UNREADABLE: " + rel)
            continue
        if any(p.search(text) for p in FORBIDDEN_CONTENT):
            issues.append("PAGES AGENT OR EDITORIAL CONTENT: " + rel)
    for rel in allowed:
        if rel not in present:
            issues.append("PAGES MISSING: " + rel)
    if built is not None:
        output = built if built.is_absolute() else root / built
        if not output.is_dir() or output.is_symlink():
            issues.append("PAGES BUILD: missing output")
        else:
            for item in sorted(output.rglob("*")):
                if item.is_symlink():
                    issues.append("PAGES BUILD SYMLINK: " + item.relative_to(output).as_posix())
                if item.is_file() and item.suffix.lower() in {".html", ".json", ".md"}:
                    content = item.read_text(encoding="utf-8", errors="replace")
                    if any(p.search(content) for p in FORBIDDEN_CONTENT):
                        issues.append("PAGES BUILD CONTENT: " + item.relative_to(output).as_posix())
                rel = item.relative_to(output).as_posix()
                if rel.startswith(("development/", "docs/", ".github/", "research/")):
                    issues.append("PAGES BUILD PATH: " + rel)
    return sorted(set(issues))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--built", type=Path)
    args = parser.parse_args()
    issues = check_pages(args.root, args.built)
    for issue in issues:
        print("FAIL:", issue)
    print("PASS: DERA public Pages" if not issues else "FAIL: DERA public Pages")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
