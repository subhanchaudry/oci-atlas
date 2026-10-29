#!/usr/bin/env python3
"""Lightweight, offline checks for this knowledge package. Standard library only."""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import tempfile
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET
import zipfile

from catalog import expected_files, generated_files, load_catalog


REPO = Path(__file__).resolve().parents[1]
PLUGIN = REPO / "plugins" / "oci-atlas"
PLUGIN_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
LINK = re.compile(r"\[[^\]\n]*\]\(([^)\s]+)\)")
SECRETS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |ENCRYPTED )?PRIVATE KEY-----"),
    re.compile(r"\bsk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{24,}\b"),
    re.compile(r"\bocid1\.[a-z0-9_]+\.[a-z0-9-]+\.[a-z0-9.-]*[a-z0-9]{40,}\b"),
)


class InvalidPackage(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise InvalidPackage(message)


def load_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(value, dict), f"{path.name}: expected JSON object")
    return value


def frontmatter(text: str) -> dict[str, str]:
    """Parse our deliberate YAML subset: keys with JSON-quoted string values.

    JSON string scalars are valid YAML; restricting authoring here keeps checks
    dependency-free without pretending to implement a general YAML parser.
    """
    lines = text.splitlines()
    require(bool(lines) and lines[0] == "---", "Skill frontmatter is missing")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise InvalidPackage("Skill frontmatter is not closed") from exc
    result = {}
    for line in lines[1:end]:
        key, sep, scalar = line.partition(":")
        require(bool(sep) and key in {"name", "description", "license"},
                "Frontmatter supports name, description and license only")
        require(key not in result, f"Duplicate frontmatter key: {key}")
        value = json.loads(scalar.strip())
        require(isinstance(value, str) and bool(value.strip()), f"Invalid {key}")
        result[key] = value
    return result


def local_links(path: Path, boundary: Path) -> None:
    for target in LINK.findall(path.read_text(encoding="utf-8")):
        parsed = urlsplit(target)
        if parsed.scheme:
            require(parsed.scheme == "https" and bool(parsed.hostname)
                    and parsed.username is None and parsed.password is None,
                    f"Unsupported external link in {path.name}: {target}")
            continue
        if not parsed.path:
            continue
        require(not parsed.netloc, f"Invalid local link in {path.name}")
        resolved = (path.parent / unquote(parsed.path)).resolve()
        require(resolved.is_relative_to(boundary.resolve()),
                f"Link escapes its package: {path.name}: {target}")
        require(resolved.is_file(), f"Broken local link in {path.name}: {target}")


def check_package(root: Path) -> dict:
    require(root.is_dir(), f"Missing plugin directory: {root}")
    entries = list(root.rglob("*"))
    require(not any(p.is_symlink() for p in entries), "Plugin contains a symlink")
    actual = {p.relative_to(root).as_posix() for p in entries if p.is_file()}
    expected = expected_files(root)
    require(actual == expected,
            f"Unexpected/missing package files: extra={sorted(actual - expected)}, "
            f"missing={sorted(expected - actual)}")
    for path in (p for p in entries if p.is_file()):
        require(path.stat().st_size <= 1024 * 1024, f"Oversized file: {path.name}")
        text = path.read_text(encoding="utf-8")
        require(not any(pattern.search(text) for pattern in SECRETS),
                f"Possible secret or customer identifier in {path.name}; inspect locally")
        if path.suffix == ".md":
            local_links(path, root)

    manifest = load_json(root / "plugin.json")
    require(manifest.get("$schema") == PLUGIN_SCHEMA, "Wrong portable manifest schema")
    require(manifest.get("name") == "oci-atlas", "Plugin name must be oci-atlas")
    require(bool(re.fullmatch(r"0|[1-9]\d*", manifest.get("version", "").split(".")[0]))
            and bool(re.fullmatch(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)",
                                  manifest.get("version", ""))), "Use release SemVer x.y.z")
    require(manifest.get("license") == "UPL-1.0", "License must be UPL-1.0")
    require(isinstance(manifest.get("description"), str)
            and bool(manifest["description"].strip()), "Missing plugin description")
    require(not {"skills", "mcpServers", "apps", "interface"}.intersection(manifest),
            "Legacy fields must not be at the portable manifest root")
    ext = manifest.get("extensions", {}).get("com.openai", {})
    require(ext.get("onboardingSkill") == "./skills/oci-atlas/SKILL.md",
            "Onboarding must target the packaged skill")
    interface = ext.get("interface", {})
    require(interface.get("displayName") == "OCI Atlas", "Wrong display name")
    subtitle = interface.get("shortDescription")
    require(isinstance(subtitle, str) and 0 < len(subtitle) <= 30, "Invalid subtitle")
    require(interface.get("category") == "Developer Tools", "Wrong category")
    require(isinstance(interface.get("capabilities"), list)
            and all(isinstance(v, str) and bool(v) for v in interface["capabilities"]),
            "Capabilities must be a list of strings")
    prompts = interface.get("defaultPrompt")
    require(isinstance(prompts, list) and 1 <= len(prompts) <= 3
            and all(isinstance(p, str) and 0 < len(p) <= 128 and "\n" not in p
                    for p in prompts), "Invalid default prompts")
    for field in ("logo", "composerIcon"):
        value = interface.get(field)
        require(value == "./assets/atlas.svg", f"Invalid {field} path")
    svg = ET.parse(root / "assets/atlas.svg").getroot()
    require(svg.tag == "{http://www.w3.org/2000/svg}svg"
            and svg.attrib.get("viewBox") == "0 0 128 128", "Invalid square SVG icon")

    skill = root / "skills" / "oci-atlas" / "SKILL.md"
    text = skill.read_text(encoding="utf-8")
    meta = frontmatter(text)
    require(meta.get("name") == skill.parent.name, "Skill name/directory mismatch")
    require(0 < len(meta.get("description", "")) <= 1024, "Invalid skill description")
    require(meta.get("license") == "UPL-1.0", "Missing skill license")
    require(len(text.splitlines()) < 500, "Move detail out of the entry skill")
    routes = set(LINK.findall(text))
    catalog = load_catalog(root)
    for entry in catalog:
        require(entry["path"] in routes, f"Guide is not directly routed: {entry['id']}")
    for path, rendered in generated_files(root, repo=None).items():
        require(path.read_text(encoding="utf-8") == rendered,
                f"Stale catalog-generated content: {path.name}")
    counts = Counter(entry["kind"] for entry in catalog)

    return {"name": manifest["name"], "version": manifest["version"],
            "files": len(actual), "knowledge_areas": counts["domain"],
            "service_guides": counts["service"], "recipes": counts["recipe"],
            "troubleshooting_guides": counts["troubleshooting"],
            "references": len(catalog), "entry_lines": len(text.splitlines())}


def check_repository() -> dict:
    summary = check_package(PLUGIN)
    marketplace = load_json(REPO / ".agents" / "plugins" / "marketplace.json")
    require(marketplace.get("name") == "oci-atlas-marketplace", "Wrong marketplace name")
    require(marketplace.get("plugins") == [{"name": "oci-atlas", "source": {
        "source": "local", "path": "./plugins/oci-atlas"}}], "Wrong marketplace source")
    require((REPO / "LICENSE.txt").read_bytes() == (PLUGIN / "LICENSE.txt").read_bytes(),
            "Repository and package licenses differ")
    for path, rendered in generated_files().items():
        require(path.exists() and path.read_text(encoding="utf-8") == rendered,
                f"Stale generated content: {path.name}; run tools/catalog.py --write")
    for path in [*REPO.glob("*.md"), *(REPO / "docs").glob("*.md")]:
        local_links(path, REPO)
    return summary


def inspect_archive(archive: Path, compare_source: bool = True) -> dict:
    with zipfile.ZipFile(archive) as zf, tempfile.TemporaryDirectory(prefix="oci-atlas-check-") as tmp:
        names = zf.namelist()
        require(len(names) == len(set(names)), "Archive has duplicate members")
        require(set(names) == {"oci-atlas/" + p for p in expected_files()},
                "Archive does not contain exactly one complete plugin")
        for entry in zf.infolist():
            member = PurePosixPath(entry.filename)
            require(not member.is_absolute() and ".." not in member.parts
                    and "\\" not in entry.filename, "Unsafe archive path")
            require(not stat.S_ISLNK(entry.external_attr >> 16), "Archive contains a symlink")
            require(entry.file_size <= 1024 * 1024, "Oversized archive member")
            if compare_source:
                source = PLUGIN / Path(*member.parts[1:])
                require(zf.read(entry) == source.read_bytes(),
                        f"Archive differs from source: {entry.filename}")
        require(zf.testzip() is None, "Archive CRC failure")
        zf.extractall(tmp)
        return check_package(Path(tmp) / "oci-atlas")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, help="Also inspect a ZIP against current source")
    args = parser.parse_args()
    try:
        summary = check_repository()
        if args.archive:
            inspect_archive(args.archive)
            summary["archive"] = str(args.archive)
        print(json.dumps({"status": "passed", **summary}, indent=2))
        return 0
    except (InvalidPackage, ValueError, OSError, KeyError, TypeError, AttributeError,
            zipfile.BadZipFile, ET.ParseError) as exc:
        print(f"Check failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
