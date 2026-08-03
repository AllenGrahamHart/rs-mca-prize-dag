#!/usr/bin/env python3
"""Mutation-test the streaming sharded-result implementation."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

from sharded_result import (
    ShardedResultError,
    ShardedResultWriter,
    iter_records,
    verify,
)


ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    with tempfile.TemporaryDirectory() as raw:
        directory = Path(raw) / "result"
        records = [{"case": value, "square": value * value}
                   for value in range(7)]
        with ShardedResultWriter(
            directory,
            metadata={"claim": "test-only"},
            shard_records=3,
        ) as writer:
            for record in records:
                writer.add(record)
        manifest = directory / "manifest.json"
        counts = verify(manifest)
        require(counts["shards"] == 3 and counts["records"] == 7,
                "writer partition")
        require(list(iter_records(manifest)) == records, "stream replay")

        first = directory / "shards/part-00000.jsonl"
        original = first.read_bytes()
        first.write_bytes(original + b"{}\n")
        try:
            verify(manifest)
        except ShardedResultError:
            pass
        else:
            raise RuntimeError("shard mutation was not detected")
        first.write_bytes(original)

        payload = json.loads(manifest.read_text())
        payload["shards"][0]["path"] = "../escape.jsonl"
        manifest.write_text(json.dumps(payload))
        try:
            verify(manifest)
        except ShardedResultError:
            pass
        else:
            raise RuntimeError("path escape was not detected")

    document = ROOT / "notes/SHARDED_RESULT_CONVENTION.md"
    text = document.read_text()
    for anchor in (
        "Rows are evidence, not DAG nodes",
        "partial-result survival",
        "manifest.json",
        "verify_sharded_result_convention.py",
    ):
        require(anchor in text, f"missing convention anchor {anchor}")
    print("SHARDED_RESULT_CONVENTION_PASS shards=3 records=7 mutations=2/2")


if __name__ == "__main__":
    main()
