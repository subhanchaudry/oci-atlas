#!/usr/bin/env python3
"""Check a release tag against package metadata and extract its changelog notes."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys


REPO = Path(__file__).resolve().parents[1]


def release_notes(tag: str) -> str:
    if not re.fullmatch(r"v(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)", tag):
        raise ValueError("Release tags must use vX.Y.Z without a prerelease suffix")
    version = json.loads((REPO / "plugins/oci-atlas/plugin.json").read_text())["version"]
    if tag != "v" + version:
        raise ValueError("Release tag does not match plugin.json version")
    changelog = (REPO / "CHANGELOG.md").read_text(encoding="utf-8")
    headings = list(re.finditer(r"^## ([^\n]+)\n", changelog, re.MULTILINE))
    matches = [(i, m) for i, m in enumerate(headings)
               if m.group(1).startswith(version + " — ")]
    if len(matches) != 1:
        raise ValueError("Release requires exactly one dated changelog section")
    i, heading = matches[0]
    end = headings[i + 1].start() if i + 1 < len(headings) else len(changelog)
    body = changelog[heading.end():end].strip()
    if not body:
        raise ValueError("Release changelog section is empty")
    return (body + "\n\n"
            f"[Get started](https://github.com/subhanchaudry/oci-atlas/blob/{tag}/docs/GETTING-STARTED.md)"
            " · "
            f"[Installation and updates](https://github.com/subhanchaudry/oci-atlas/blob/{tag}/docs/INSTALL.md)"
            "\n\nDownload the plugin ZIP and its SHA-256 companion below. "
            "Source archives contain the complete repository.\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag", required=True)
    parser.add_argument("--notes-file", type=Path, required=True)
    args = parser.parse_args()
    notes = release_notes(args.tag)
    args.notes_file.write_text(notes, encoding="utf-8")
    print(f"Release metadata checked: {args.tag}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, KeyError, OSError) as exc:
        print(f"Release preparation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
