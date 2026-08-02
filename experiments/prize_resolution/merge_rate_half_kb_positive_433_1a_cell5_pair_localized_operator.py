#!/usr/bin/env python3
"""Merge complete localized-operator shards into one coverage packet."""

import argparse
import hashlib
import json
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputs", nargs="+", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    return parser.parse_args()


def main():
    args = parse_args()
    shards = []
    sources = []
    for path in args.inputs:
        raw = path.read_bytes()
        sources.append(
            {"path": path.name, "sha256": hashlib.sha256(raw).hexdigest()}
        )
        shards.extend(json.loads(raw))
    complete = [item for item in shards if item["status"] == "COMPLETE"]
    chosen = {}
    for shard in complete:
        for column in range(shard["start"], shard["stop"] + 1):
            chosen[column] = shard
    if set(chosen) != set(range(1, 25)):
        raise SystemExit(f"incomplete column coverage: {sorted(chosen)}")
    selected = []
    seen_shards = set()
    for column in range(1, 25):
        shard = chosen[column]
        identity = (shard["program_sha256"], shard["start"], shard["stop"])
        if identity not in seen_shards:
            selected.append(shard)
            seen_shards.add(identity)
    expected = {
        "alpha": 2,
        "beta": 3,
        "basis_sha256": (
            "8fd93095924f616770e49257ae45f255a8859f43c4f87100859cadfc8cc77ed6"
        ),
        "square_packet_sha256": (
            "c10acad4d6e6971fb978498f49a1a8306326b81f23c6cdf3c06cb318ba6f61d3"
        ),
    }
    for shard in selected:
        for key, value in expected.items():
            if shard[key] != value:
                raise SystemExit(f"{key} mismatch")
        if shard["returncode"] != 0 or "LOCALIZED_OPERATOR_SHARD_COMPLETE" not in shard["stdout"]:
            raise SystemExit("invalid completion marker")
    entries = {}
    for column in range(1, 25):
        shard = chosen[column]
        for entry in shard["entries"]:
            if entry["column"] != column:
                continue
            key = (entry["kind"], entry["row"], entry["column"])
            entries[key] = entry
    coordinate_keys = {
        ("C", row, column)
        for row in range(1, 25)
        for column in range(1, 25)
    }
    if not coordinate_keys <= set(entries):
        raise SystemExit("coordinate coverage mismatch")
    for column in range(1, 25):
        if not any(key[0] == "W" and key[2] == column for key in entries):
            raise SystemExit(f"empty target column {column}")
    payload = {
        "schema": "rate-half-kb-positive-433-1a-cell5-localized-operator-v1",
        **expected,
        "column_coverage": list(range(1, 25)),
        "sources": sources,
        "shards": [
            {key: value for key, value in shard.items() if key != "entries"}
            for shard in selected
        ],
        "entries": [entries[key] for key in sorted(entries)],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_CELL5_LOCALIZED_OPERATOR_MERGE_PASS "
        f"shards={len(selected)} entries={len(entries)}"
    )


if __name__ == "__main__":
    main()
