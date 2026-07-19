#!/usr/bin/env python3
"""Verify the Modal radius-three x83 shell certificate JSON."""

from __future__ import annotations

import json
import math
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
NOTES = ROOT / "critical/nodes/u1_x4_direct_column_budget/notes"
CERT_ENV = os.environ.get(
    "F3_H8_RADIUS3_CERT",
    "f3_h8_n64_x83_radius3_shell_certificate.json",
)
OUT = Path(CERT_ENV)
if not OUT.is_absolute():
    OUT = NOTES / OUT


def main() -> None:
    cert = json.loads(OUT.read_text())
    expected_primes = [
        int(item)
        for item in os.environ.get("F3_H8_RADIUS3_EXPECTED_PRIMES", "262337").split(",")
        if item
    ]
    expected_chunk_pairs = int(os.environ.get("F3_H8_RADIUS3_EXPECTED_CHUNK_PAIRS", "20"))
    expected_jobs = len(expected_primes) * math.ceil(
        (7 * math.comb(16, 3)) / expected_chunk_pairs
    )
    expected_processed = len(expected_primes) * 7 * math.comb(16, 3) * math.comb(48, 3)
    expected = {
        "name": "h8_n64_x83_radius3_shell",
        "mode": "full",
        "radius": 3,
        "primes": expected_primes,
        "chunk_pairs": expected_chunk_pairs,
        "jobs_expected": expected_jobs,
        "jobs_completed": expected_jobs,
        "processed": expected_processed,
        "full_zero": 0,
        "complete": True,
        "errors": [],
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
    if sum(row.get("first_obstruction_zero", 0) for row in rows) != cert["first_obstruction_zero"]:
        raise AssertionError("first-zero mismatch")
    print("h=8 n64 x83 radius-three shell certificate verified")
    print("H8_N64_X83_RADIUS3_CERTIFICATE_PASS")


if __name__ == "__main__":
    main()
