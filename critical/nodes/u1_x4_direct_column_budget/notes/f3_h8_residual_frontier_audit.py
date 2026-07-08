#!/usr/bin/env python3
"""Audit the h=8 residual frontier for F3/T4.

This verifier is a bookkeeping/audit layer over existing certificates.  It
does not launch a new h=8 search.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
NOTES = ROOT / "critical/nodes/u1_x4_direct_column_budget/notes"

H8_N32_PRIMES = [1153, 3137, 12289, 40961, 61441, 65537]
PARTIAL_H8_N64 = {
    "boundary_n64_h8_p193": 193,
    "q3_n64_h8": 262337,
}


def load_json(name: str):
    return json.loads((NOTES / name).read_text())


def require_h8_n32_rows() -> int:
    rows = load_json("f3_h8_n32_multirow_certificate.json")
    if [row.get("p") for row in rows] != H8_N32_PRIMES:
        raise AssertionError(rows)
    for row in rows:
        expected = {
            "n": 32,
            "h": 8,
            "W": 32,
            "hashed": 2629575,
            "probed": 7888725,
            "anchored_toral_trades": 3,
            "anchored_nontoral_trades": 0,
            "partial": False,
            "complete": True,
            "direct_n3_exceeded": False,
        }
        for key, value in expected.items():
            if row.get(key) != value:
                raise AssertionError((key, row.get(key), value, row))
        if (row["p"] - 1) % 32 != 0:
            raise AssertionError(row)
    return sum(row["probed"] for row in rows)


def require_partial_h8_n64_rows() -> None:
    rows = {row["name"]: row for row in load_json("f3a1_results.json")}
    for name, p in PARTIAL_H8_N64.items():
        row = rows[name]
        expected = {
            "name": name,
            "n": 64,
            "h": 8,
            "p": p,
            "anchored_nontoral_trades": 0,
            "direct_n3_budget": 64**3,
            "direct_n3_exceeded": False,
            "partial": True,
        }
        for key, value in expected.items():
            if row.get(key) != value:
                raise AssertionError((key, row.get(key), value, row))
        slice_row = row.get("row")
        if not isinstance(slice_row, dict) or slice_row.get("W") != 48:
            raise AssertionError(row)


def require_radius3_certificate(name: str, p: int, expected_first_zero: int) -> int:
    cert = load_json(name)
    expected_jobs = math.ceil((7 * math.comb(16, 3)) / 20)
    expected_processed = 7 * math.comb(16, 3) * math.comb(48, 3)
    expected = {
        "name": "h8_n64_x83_radius3_shell",
        "mode": "full",
        "radius": 3,
        "primes": [p],
        "chunk_pairs": 20,
        "jobs_expected": expected_jobs,
        "jobs_completed": expected_jobs,
        "processed": expected_processed,
        "first_obstruction_zero": expected_first_zero,
        "full_zero": 0,
        "complete": True,
        "errors": [],
    }
    for key, value in expected.items():
        if cert.get(key) != value:
            raise AssertionError((name, key, cert.get(key), value))
    rows = cert.get("rows")
    if not isinstance(rows, list) or len(rows) != expected_jobs:
        raise AssertionError((name, rows))
    if sum(row.get("processed", 0) for row in rows) != expected_processed:
        raise AssertionError(name)
    if sum(row.get("first_obstruction_zero", 0) for row in rows) != expected_first_zero:
        raise AssertionError(name)
    if any(not row.get("complete") or row.get("full_zero") != 0 for row in rows):
        raise AssertionError(name)
    if max(row.get("elapsed_sec", 999.0) for row in rows) >= 60:
        raise AssertionError(("timeout-risk shard", name))
    return expected_processed


def require_q3_profile() -> None:
    cert = load_json("f3_h8_n64_x83_radius3_profile_q3.json")
    suffix = [67800000, 320, 0, 0, 0, 0, 0, 0]
    if cert.get("suffix_counts") != suffix:
        raise AssertionError(cert.get("suffix_counts"))
    if cert.get("deep_examples") != []:
        raise AssertionError("unexpected q3 deep examples")
    if cert.get("full_zero") != 0 or cert.get("complete") is not True:
        raise AssertionError(cert)
    rows_suffix = [0] * len(suffix)
    for row in cert["rows"]:
        row_suffix = row.get("suffix_counts")
        if not isinstance(row_suffix, list) or len(row_suffix) != len(suffix):
            raise AssertionError(row)
        if sum(row_suffix) != row.get("processed"):
            raise AssertionError(row)
        for index, count in enumerate(row_suffix):
            rows_suffix[index] += count
    if rows_suffix != suffix:
        raise AssertionError(rows_suffix)


def main() -> None:
    n32_probes = require_h8_n32_rows()
    require_partial_h8_n64_rows()
    p4289_processed = require_radius3_certificate(
        "f3_h8_n64_x83_radius3_shell_certificate_p4289.json", 4289, 16048
    )
    q3_processed = require_radius3_certificate(
        "f3_h8_n64_x83_radius3_shell_certificate.json", 262337, 320
    )
    require_q3_profile()

    blind_left_records = math.comb(63, 7)
    blind_left_gib = blind_left_records * 32 / (1024**3)
    blind_right_records = math.comb(63, 8)

    print("h=8 residual frontier audit")
    print(f"n=32 complete certified primes: {len(H8_N32_PRIMES)}")
    print(f"n=32 right-side probes: {n32_probes}")
    print(f"n=64 partial rows remaining: {len(PARTIAL_H8_N64)}")
    print(f"radius-three p=4289 processed: {p4289_processed}, full_zero=0")
    print(f"radius-three p=262337 processed: {q3_processed}, full_zero=0")
    print("q3 suffix profile: [67800000, 320, 0, 0, 0, 0, 0, 0]")
    print(f"blind n64 h8 left records: {blind_left_records} (~{blind_left_gib:.2f} GiB at 32 bytes)")
    print(f"blind n64 h8 right records: {blind_right_records}")
    print("H8_RESIDUAL_FRONTIER_AUDIT_PASS")


if __name__ == "__main__":
    main()
