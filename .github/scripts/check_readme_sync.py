"""Check that README.md (Chinese) and README.en.md (English) list the same entries.

For every section that contains entries, both files must have the same entries
in the same order, with the same link and equivalent tags.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

TAGS = {
    "免费": "Free",
    "免费增值": "Freemium",
    "付费": "Paid",
    "API": "API",
    "中国": "China",
    "香港": "Hong Kong",
    "美国": "US",
    "全球": "Global",
    "加密货币": "Crypto",
}

# Entries that intentionally link to a localized site in each language.
LOCALIZED_LINKS = {
    ("https://cn.investing.com", "https://www.investing.com"),
    ("https://data.worldbank.org.cn", "https://data.worldbank.org"),
}

ENTRY_RE = re.compile(r"^- \[[^\]]+\]\((https?://[^)\s]+)\)")
TAG_LINE_RE = re.compile(r"^  - ((?:`[^`]+`\s*)+)$")


def parse(path):
    """Return a list of sections, each a list of (link, tags) entries."""
    sections = []
    current = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            current = {"title": line[3:].strip(), "entries": []}
            sections.append(current)
            continue
        if current is None:
            continue
        match = ENTRY_RE.match(line)
        if match:
            current["entries"].append({"link": match.group(1), "tags": []})
            continue
        match = TAG_LINE_RE.match(line)
        if match and current["entries"]:
            current["entries"][-1]["tags"] = re.findall(r"`([^`]+)`", match.group(1))
    return [s for s in sections if s["entries"]]


def main():
    zh = parse(ROOT / "README.md")
    en = parse(ROOT / "README.en.md")
    errors = []

    if len(zh) != len(en):
        errors.append(f"Section count differs: README.md has {len(zh)}, README.en.md has {len(en)}")

    for zh_sec, en_sec in zip(zh, en):
        where = f"[{zh_sec['title']} / {en_sec['title']}]"
        if len(zh_sec["entries"]) != len(en_sec["entries"]):
            errors.append(
                f"{where} entry count differs: {len(zh_sec['entries'])} vs {len(en_sec['entries'])}"
            )
        for i, (z, e) in enumerate(zip(zh_sec["entries"], en_sec["entries"]), 1):
            if z["link"] != e["link"] and (z["link"], e["link"]) not in LOCALIZED_LINKS:
                errors.append(f"{where} entry {i} link differs: {z['link']} vs {e['link']}")
            unknown = [t for t in z["tags"] if t not in TAGS]
            if unknown:
                errors.append(f"{where} entry {i} has unknown tags in README.md: {unknown}")
            expected = [TAGS.get(t, t) for t in z["tags"]]
            if expected != e["tags"]:
                errors.append(f"{where} entry {i} tags differ: {z['tags']} vs {e['tags']}")

    if errors:
        print("README.md and README.en.md are out of sync:")
        for error in errors:
            print(f"  - {error}")
        return 1

    total = sum(len(s["entries"]) for s in zh)
    print(f"OK: {len(zh)} sections, {total} entries in sync")
    return 0


if __name__ == "__main__":
    sys.exit(main())
