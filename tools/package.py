#!/usr/bin/env python3
"""Build an inspected, reproducible OCI Atlas ZIP and SHA-256 checksum."""

from __future__ import annotations

import hashlib
from pathlib import Path
import sys
import zipfile

from check import PLUGIN, REPO, check_repository, expected_files, inspect_archive


def main() -> int:
    summary = check_repository()
    output = REPO / "dist"
    output.mkdir(exist_ok=True)
    archive = output / f"{summary['name']}-{summary['version']}.zip"
    temporary = archive.with_suffix(".zip.tmp")
    try:
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED,
                             compresslevel=9) as zf:
            for relative in sorted(expected_files()):
                info = zipfile.ZipInfo("oci-atlas/" + relative, date_time=(1980, 1, 1, 0, 0, 0))
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                zf.writestr(info, (PLUGIN / relative).read_bytes(), compresslevel=9)
        inspect_archive(temporary)
        digest = hashlib.sha256(temporary.read_bytes()).hexdigest()
        temporary.replace(archive)
        checksum = archive.with_suffix(".zip.sha256")
        checksum.write_text(f"{digest}  {archive.name}\n", encoding="utf-8")
        print(f"Built {archive.relative_to(REPO)} ({archive.stat().st_size:,} bytes)")
        print(f"SHA-256 {digest}")
        return 0
    finally:
        temporary.unlink(missing_ok=True)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError, KeyError, TypeError, AttributeError, zipfile.BadZipFile) as exc:
        print(f"Packaging failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
