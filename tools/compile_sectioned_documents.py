#!/usr/bin/env python3
"""Build or check generated roadmap and compute-ledger views."""

from __future__ import annotations

import argparse
from pathlib import Path

from sectioned_document import (
    ROOT,
    SectionedDocumentError,
    compiled_text,
    load_manifest,
    write_document,
)


MANIFESTS = (
    ROOT / "notes" / "roadmap" / "document.json",
    ROOT / "notes" / "compute_requests" / "document.json",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    errors = []
    for manifest in MANIFESTS:
        try:
            document = load_manifest(manifest, ROOT)
            expected = compiled_text(manifest, ROOT)
        except (SectionedDocumentError, ValueError) as error:
            errors.append(str(error))
            continue
        output = document["output"]
        if args.write:
            write_document(manifest, ROOT)
            print(
                f"SECTIONED_DOCUMENT_COMPILED {output.relative_to(ROOT)} "
                f"sections={len(document['sections'])} bytes={len(expected.encode())}"
            )
        elif not output.is_file() or output.read_text() != expected:
            errors.append(
                f"{output.relative_to(ROOT)} is stale; run "
                "python3 tools/compile_sectioned_documents.py --write"
            )
        else:
            print(
                f"SECTIONED_DOCUMENT_PASS {output.relative_to(ROOT)} "
                f"sections={len(document['sections'])} bytes={len(expected.encode())}"
            )
    if errors:
        print("SECTIONED_DOCUMENT_FAIL")
        for error in errors:
            print(f"  - {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
