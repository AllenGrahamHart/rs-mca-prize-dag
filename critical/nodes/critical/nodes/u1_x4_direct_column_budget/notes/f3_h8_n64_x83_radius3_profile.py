#!/usr/bin/env python3
"""Verify the q3 radius-three x83 obstruction suffix profile."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
NOTES = ROOT / "critical/nodes/u1_x4_direct_column_budget/notes"
OUT = NOTES / "f3_h8_n64_x83_radius3_profile_q3.json"


def main() -> None:
    cert = json.loads(OUT.read_text())
    expected_processed = 7 * math.comb(16, 3) * math.comb(48, 3)
    expected_jobs = math.ceil((7 * math.comb(16, 3)) / 20)
    expected = {
        "name": "h8_n64_x83_radius3_shell",
        "mode": "full",
        "radius": 3,
        "primes": [262337],
        "chunk_pairs": 20,
        "jobs_expected": expected_jobs,
        "jobs_completed": expected_jobs,
        "processed": expected_processed,
        "first_obstruction_zero": 320,
        "full_zero": 0,
        "complete": True,
        "errors": [],
        "suffix_counts": [67800000, 320, 0, 0, 0, 0, 0, 0],
    }
    for key, value in expected.items():
        if cert.get(key) != value:
            raise AssertionError((key, cert.get(key), value))
    rows = cert.get("rows")
    if not isinstance(rows, list) or len(rows) != expected_jobs:
        raise AssertionError(("rows", len(rows) if isinstance(rows, list) else None))
    if any(not row.get("complete") for row in rows):
        raise AssertionError("incomplete shard")
    if any(row.get("full_zero") != 0 for row in rows):
        raise AssertionError("full-zero shard")
    if max(row.get("elapsed_sec", 999.0) for row in rows) >= 60:
        raise AssertionError("timeout-risk shard")
    if sum(row.get("processed", 0) for row in rows) != expected_processed:
        raise AssertionError("processed mismatch")
    suffix = [0] * 8
    for row in rows:
        row_suffix = row.get("suffix_counts")
        if not isinstance(row_suffix, list) or len(row_suffix) != 8:
            raise AssertionError(("row suffix", row_suffix))
        if sum(row_suffix) != row.get("processed"):
            raise AssertionError(("row suffix sum", row))
        if sum(row_suffix[1:]) != row.get("first_obstruction_zero"):
            raise AssertionError(("row first-zero sum", row))
        for index, count in enumerate(row_suffix):
            suffix[index] += count
    if suffix != expected["suffix_counts"]:
        raise AssertionError(("suffix aggregate", suffix))
    if cert.get("deep_examples") != []:
        raise AssertionError("unexpected depth >= 2 examples")
    print("h=8 n64 x83 radius-three q3 profile verified")
    print("H8_N64_X83_RADIUS3_PROFILE_PASS")


if __name__ == "__main__":
    main()
