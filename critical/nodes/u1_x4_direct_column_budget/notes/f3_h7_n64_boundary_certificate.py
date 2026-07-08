#!/usr/bin/env python3
"""Verify the h=7 n=64 p4289 rank-sharded certificate JSON."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
NOTES = ROOT / "critical/nodes/u1_x4_direct_column_budget/notes"
OUT = NOTES / "f3_h7_n64_boundary_certificate.json"


def main() -> None:
    row = json.loads(OUT.read_text())
    expected = {
        "name": "boundary_n64_h7_p4289_RANK_SHARDED_CPP",
        "n": 64,
        "h": 7,
        "p": 4289,
        "W": 64,
        "shards": 16,
        "shards_completed": 16,
        "left_records_per_shard": 67945521,
        "probed": 553270671,
        "anchored_toral_trades": 0,
        "anchored_nontoral_trades": 0,
        "direct_n3_budget": 262144,
        "direct_n3_exceeded": False,
        "partial": False,
        "complete": True,
    }
    for key, value in expected.items():
        if row.get(key) != value:
            raise AssertionError((key, row.get(key), value, row))
    shards = row.get("rows")
    if not isinstance(shards, list) or len(shards) != 16:
        raise AssertionError(row)
    if [item.get("right_shard") for item in shards] != list(range(16)):
        raise AssertionError(shards)
    if sum(item.get("probed", 0) for item in shards) != row["probed"]:
        raise AssertionError(row)
    if not all(item.get("complete") and not item.get("partial") for item in shards):
        raise AssertionError(shards)
    if not all(item.get("phase") == "complete_one_right_shard" for item in shards):
        raise AssertionError(shards)
    if max(item.get("elapsed_sec", 999) for item in shards) >= 60:
        raise AssertionError(shards)
    print("h=7 n64 p4289 rank-sharded certificate verified")
    print("H7_N64_BOUNDARY_CERTIFICATE_JSON_PASS")


if __name__ == "__main__":
    main()
