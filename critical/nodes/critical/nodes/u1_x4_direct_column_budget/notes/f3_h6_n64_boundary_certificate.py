#!/usr/bin/env python3
"""Verify the Modal-produced n=64,h=6 anchored boundary certificate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
OUT = (
    ROOT
    / "critical/nodes/u1_x4_direct_column_budget/notes"
    / "f3_h6_n64_boundary_certificate.json"
)


def main() -> None:
    row = json.loads(OUT.read_text())
    expected = {
        "name": "boundary_n64_h6_p4289_SHARDED_CPP",
        "n": 64,
        "h": 6,
        "p": 4289,
        "W": 64,
        "shards": 16,
        "shards_completed": 16,
        "hashed_per_shard": 7028847,
        "probed": 67945521,
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
    rows = row.get("rows")
    if not isinstance(rows, list) or len(rows) != 16:
        raise AssertionError(("rows", rows))
    if [item.get("shard") for item in rows] != list(range(16)):
        raise AssertionError([item.get("shard") for item in rows])
    for item in rows:
        if item.get("anchored_nontoral_trades") != 0:
            raise AssertionError(("shard nontoral", item))
        if item.get("direct_n3_exceeded"):
            raise AssertionError(("shard n3 alarm", item))
    print(json.dumps({k: v for k, v in row.items() if k != "rows"}, sort_keys=True))
    print("H6_N64_BOUNDARY_CERTIFICATE_JSON_PASS")


if __name__ == "__main__":
    main()
