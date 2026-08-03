#!/usr/bin/env python3
"""Verify exact compatibility views and bounded semantic source shards."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

from compile_sectioned_documents import MANIFESTS
from sectioned_document import (
    ROOT,
    SectionedDocumentError,
    compiled_text,
    load_manifest,
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def mutation_tests():
    with tempfile.TemporaryDirectory() as raw:
        root = Path(raw)
        first = root / "parts/first.md"
        second = root / "parts/second.md"
        first.parent.mkdir()
        first.write_text("first\n")
        second.write_text("second\n")
        manifest = root / "document.json"
        baseline = {
            "schema": "sectioned-document-v1",
            "output": "combined.md",
            "sections": ["parts/first.md", "parts/second.md"],
        }
        manifest.write_text(json.dumps(baseline))
        require(compiled_text(manifest, root) == "first\nsecond\n",
                "fixture compilation")
        caught = 0

        duplicate = json.loads(json.dumps(baseline))
        duplicate["sections"][1] = duplicate["sections"][0]
        manifest.write_text(json.dumps(duplicate))
        try:
            load_manifest(manifest, root)
        except SectionedDocumentError:
            caught += 1

        escape = json.loads(json.dumps(baseline))
        escape["sections"][0] = "../escape.md"
        manifest.write_text(json.dumps(escape))
        try:
            load_manifest(manifest, root)
        except SectionedDocumentError:
            caught += 1

        manifest.write_text(json.dumps(baseline))
        output = root / "combined.md"
        output.write_text("stale\n")
        caught += output.read_text() != compiled_text(manifest, root)
        require(caught == 3, f"section mutations caught {caught}/3")
    return caught


def main():
    total_sections = 0
    for manifest in MANIFESTS:
        document = load_manifest(manifest, ROOT)
        expected = compiled_text(manifest, ROOT)
        output = document["output"]
        require(output.read_text() == expected,
                f"stale compatibility document {output}")
        line_counts = [
            section.read_text().count("\n")
            for section in document["sections"]
        ]
        require(max(line_counts) < 9000,
                f"oversized source shard in {manifest}")
        require(all(count > 0 for count in line_counts),
                f"empty source shard in {manifest}")
        total_sections += len(line_counts)
    for path in (
        ROOT / "notes/roadmap/INDEX.md",
        ROOT / "notes/roadmap/LIST.md",
        ROOT / "notes/roadmap/MCA.md",
        ROOT / "notes/roadmap/RATE_HALF.md",
        ROOT / "notes/roadmap/SHARED_UPSTREAM.md",
        ROOT / "notes/compute_requests/INDEX.md",
    ):
        require(path.is_file(), f"missing navigation index {path}")
    caught = mutation_tests()
    print(
        f"SECTIONED_DOCUMENT_PASS documents={len(MANIFESTS)} "
        f"sections={total_sections} mutations={caught}/3"
    )


if __name__ == "__main__":
    main()
