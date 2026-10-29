#!/usr/bin/env python3
"""Validate the content catalog and render its navigation and source metadata."""

from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit


REPO = Path(__file__).resolve().parents[1]
PLUGIN = REPO / "plugins" / "oci-atlas"
SKILL_PATH = Path("skills/oci-atlas")
KINDS = ("access", "decision", "domain", "service", "troubleshooting", "recipe")
START = "<!-- atlas:catalog:start -->"
END = "<!-- atlas:catalog:end -->"


def demand(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def load_catalog(root: Path = PLUGIN) -> list[dict]:
    data = json.loads((root / SKILL_PATH / "catalog.json").read_text(encoding="utf-8"))
    demand(isinstance(data, dict) and data.get("schema_version") == 1,
           "Catalog must use schema_version 1")
    entries = data.get("entries")
    demand(isinstance(entries, list) and bool(entries), "Catalog entries are missing")
    ids, paths = set(), set()
    for entry in entries:
        demand(isinstance(entry, dict), "Catalog entries must be objects")
        name = entry.get("id")
        demand(isinstance(name, str) and bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)),
               "Invalid catalog id")
        demand(name not in ids, f"Duplicate catalog id: {name}")
        ids.add(name)
        path = entry.get("path")
        demand(path == f"references/{name}.md" and path not in paths,
               f"Invalid or duplicate catalog path: {name}")
        paths.add(path)
        demand(entry.get("kind") in KINDS, f"Invalid kind: {name}")
        for key in ("title", "summary"):
            value = entry.get(key)
            demand(isinstance(value, str) and bool(value.strip())
                   and not any(c in value for c in "\n\r|[]"), f"Invalid {key}: {name}")
        aliases = entry.get("aliases")
        demand(isinstance(aliases, list) and bool(aliases)
               and all(isinstance(v, str) and bool(v.strip())
                       and not any(c in v for c in "\n\r|[]") for v in aliases)
               and len(set(aliases)) == len(aliases), f"Invalid aliases: {name}")
        reviewed = entry.get("reviewed")
        demand(isinstance(reviewed, str) and bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", reviewed)),
               f"Invalid review date: {name}")
        demand(date.fromisoformat(reviewed) <= date.today(), f"Future review date: {name}")
        sources = entry.get("sources")
        demand(isinstance(sources, list) and bool(sources), f"Missing sources: {name}")
        hosts, urls = set(), set()
        for source in sources:
            demand(isinstance(source, dict), f"Invalid source: {name}")
            title, url = source.get("title"), source.get("url")
            demand(isinstance(title, str) and bool(title.strip())
                   and not any(c in title for c in "\n\r[]"), f"Invalid source title: {name}")
            demand(isinstance(url, str) and not any(c.isspace() or c in "()" for c in url),
                   f"Invalid source URL: {name}")
            parsed = urlsplit(url)
            demand(parsed.scheme == "https" and bool(parsed.hostname)
                   and parsed.username is None and parsed.password is None
                   and url not in urls, f"Unsafe or duplicate source URL: {name}")
            hosts.add(parsed.hostname)
            urls.add(url)
        demand("docs.oracle.com" in hosts, f"Missing Oracle documentation: {name}")
    return entries


def expected_files(root: Path = PLUGIN) -> set[str]:
    base = {"plugin.json", "README.md", "NOTICE.md", "LICENSE.txt", "assets/atlas.svg",
            "skills/oci-atlas/SKILL.md", "skills/oci-atlas/catalog.json"}
    return base | {(SKILL_PATH / entry["path"]).as_posix() for entry in load_catalog(root)}


def render_skill(text: str, entries: list[dict]) -> str:
    demand(text.count(START) == text.count(END) == 1, "Missing/duplicate catalog markers")
    before, rest = text.split(START)
    _, after = rest.split(END)
    rows = ["| Request | Read |", "| --- | --- |"]
    for entry in entries:
        rows.append(f"| {entry['summary']} | [{entry['title']}]({entry['path']}) |")
    return before + START + "\n\n" + "\n".join(rows) + "\n\n" + END + after


def render_guide(text: str, entry: dict) -> str:
    demand(bool(re.match(r"^# [^\n]+\n", text)), f"Missing guide title: {entry['id']}")
    text = "# " + entry["title"] + "\n" + text.split("\n", 1)[1]
    text, count = re.subn(r"^Reviewed: \d{4}-\d{2}-\d{2}", "Reviewed: " + entry["reviewed"],
                          text, count=1, flags=re.MULTILINE)
    demand(count == 1 and text.count("\n## Sources\n") == 1,
           f"Missing review date or unique Sources section: {entry['id']}")
    body, _ = text.split("\n## Sources\n")
    sources = "\n".join(f"- [{s['title']}]({s['url']})" for s in entry["sources"])
    return body + "\n## Sources\n\n" + sources + "\n"


def render_index(entries: list[dict]) -> str:
    lines = ["# OCI Atlas content catalog", "",
             "Generated from the [catalog](../plugins/oci-atlas/skills/oci-atlas/catalog.json). "
             "Edit catalog metadata and guide bodies, then run `python3 tools/catalog.py --write`.", "",
             "The entry skill routes directly to these references; the agent need not load this entire index.", ""]
    for kind in KINDS:
        lines.extend([f"## {kind.capitalize()}", "", "| Guide | Search terms | Reviewed |",
                      "| --- | --- | --- |"])
        for entry in entries:
            if entry["kind"] == kind:
                link = "../plugins/oci-atlas/skills/oci-atlas/" + entry["path"]
                lines.append(f"| [{entry['title']}]({link}) | {', '.join(entry['aliases'])} | {entry['reviewed']} |")
        lines.append("")
    return "\n".join(lines)


def generated_files(root: Path = PLUGIN, repo: Path | None = REPO) -> dict[Path, str]:
    entries = load_catalog(root)
    skill = root / SKILL_PATH / "SKILL.md"
    result = {skill: render_skill(skill.read_text(encoding="utf-8"), entries)}
    for entry in entries:
        guide = root / SKILL_PATH / entry["path"]
        result[guide] = render_guide(guide.read_text(encoding="utf-8"), entry)
    if repo is not None:
        result[repo / "docs/CONTENT.md"] = render_index(entries)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Render metadata and navigation")
    parser.add_argument("--check", action="store_true", help="Check generated content (default)")
    args = parser.parse_args()
    demand(not (args.write and args.check), "Choose --write or --check")
    outputs = generated_files()
    for path, text in outputs.items():
        if args.write:
            path.write_text(text, encoding="utf-8")
        else:
            demand(path.exists() and path.read_text(encoding="utf-8") == text,
                   f"Stale generated content: {path.relative_to(REPO)}; run tools/catalog.py --write")
    print(f"Catalog {'rendered' if args.write else 'checked'}: {len(load_catalog())} references")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(f"Catalog failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
