#!/usr/bin/env python3
"""Replay checker for the h=6/7/8 bonus sweep status."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
NOTES = ROOT / "critical/nodes/u1_x4_direct_column_budget/notes"


FULL_ZERO_ROWS = {
    "f3a1_results.json": (
        "boundary_n32_h6_p1153_FULL",
        "boundary_n32_h7_p1153_FULL",
        "boundary_n32_h6_p3137",
        "boundary_n32_h7_p3137",
        "boundary_n32_h6_p12289",
    ),
    "f3a2_results.json": (
        "smooth_n32_h6_p40961",
        "smooth_n32_h7_p40961",
        "smooth_n32_h6_p61441",
        "smooth_n32_h7_p61441",
        "smooth_n32_h6_p65537",
        "smooth_n32_h7_p65537",
    ),
}

PARTIAL_H8_ROWS = ("boundary_n64_h8_p193", "q3_n64_h8")


def load_rows(filename: str) -> dict[str, dict]:
    rows = json.loads((NOTES / filename).read_text())
    return {row["name"]: row for row in rows}


def require_zero_full(row: dict) -> None:
    if row.get("partial"):
        raise AssertionError(("expected full", row))
    if row.get("anchored_nontoral_trades") != 0:
        raise AssertionError(("expected zero", row))
    if row.get("direct_n3_exceeded"):
        raise AssertionError(("n3 alarm", row))


def require_zero_partial(row: dict) -> None:
    if not row.get("partial"):
        raise AssertionError(("expected partial", row))
    if row.get("anchored_nontoral_trades") != 0:
        raise AssertionError(("expected zero in checked slice", row))
    if row.get("direct_n3_exceeded"):
        raise AssertionError(("n3 alarm", row))


def require_h8_full_certificate(row: dict, p: int = 1153) -> None:
    expected = {
        "n": 32,
        "h": 8,
        "p": p,
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


def require_h6_n64_certificate(row: dict) -> None:
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
        "partial": False,
        "complete": True,
        "direct_n3_exceeded": False,
    }
    for key, value in expected.items():
        if row.get(key) != value:
            raise AssertionError((key, row.get(key), value, row))
    rows = row.get("rows")
    if not isinstance(rows, list) or len(rows) != 16:
        raise AssertionError(row)
    if [item.get("shard") for item in rows] != list(range(16)):
        raise AssertionError(rows)
    if sum(item.get("probed", 0) for item in rows) != row["probed"]:
        raise AssertionError(row)


def require_h6_n64_extra_certificate(rows: list[dict]) -> None:
    expected_primes = [4481, 4673, 4801, 4993, 5441, 5569]
    expected_nontoral = {
        4481: 0,
        4673: 0,
        4801: 0,
        4993: 6,
        5441: 0,
        5569: 0,
    }
    if [row.get("p") for row in rows] != expected_primes:
        raise AssertionError(rows)
    for row in rows:
        p = row["p"]
        expected = {
            "name": f"boundary_n64_h6_p{p}_SHARDED_CPP",
            "n": 64,
            "h": 6,
            "W": 64,
            "shards": 16,
            "shards_completed": 16,
            "hashed_per_shard": 7028847,
            "probed": 67945521,
            "anchored_toral_trades": 0,
            "anchored_nontoral_trades": expected_nontoral[p],
            "partial": False,
            "complete": True,
            "direct_n3_exceeded": False,
        }
        for key, value in expected.items():
            if row.get(key) != value:
                raise AssertionError((p, key, row.get(key), value, row))
        shards = row.get("rows")
        if not isinstance(shards, list) or len(shards) != 16:
            raise AssertionError((p, shards))
        if [item.get("shard") for item in shards] != list(range(16)):
            raise AssertionError((p, shards))
        if sum(item.get("probed", 0) for item in shards) != row["probed"]:
            raise AssertionError((p, row))
        witness_count = len(row.get("witnesses", []))
        if witness_count != expected_nontoral[p]:
            raise AssertionError((p, witness_count, row))


def require_h7_n64_certificate(row: dict) -> None:
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
        "partial": False,
        "complete": True,
        "direct_n3_exceeded": False,
    }
    for key, value in expected.items():
        if row.get(key) != value:
            raise AssertionError((key, row.get(key), value, row))
    rows = row.get("rows")
    if not isinstance(rows, list) or len(rows) != 16:
        raise AssertionError(row)
    if [item.get("right_shard") for item in rows] != list(range(16)):
        raise AssertionError(rows)
    if sum(item.get("probed", 0) for item in rows) != row["probed"]:
        raise AssertionError(row)


def require_h8_radius3_certificate(
    cert: dict, expected_primes: list[int], expected_first_zero: int
) -> None:
    expected_jobs = len(expected_primes) * math.ceil((7 * math.comb(16, 3)) / 20)
    expected_processed = len(expected_primes) * 7 * math.comb(16, 3) * math.comb(48, 3)
    expected = {
        "name": "h8_n64_x83_radius3_shell",
        "mode": "full",
        "radius": 3,
        "primes": expected_primes,
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
            raise AssertionError((key, cert.get(key), value, cert))
    rows = cert.get("rows")
    if not isinstance(rows, list) or len(rows) != expected_jobs:
        raise AssertionError(("radius3 rows", rows))
    if any(not row.get("complete") for row in rows):
        raise AssertionError("incomplete radius3 shard")
    if any(row.get("full_zero") != 0 for row in rows):
        raise AssertionError("radius3 full-zero shard")
    if sum(row.get("processed", 0) for row in rows) != expected_processed:
        raise AssertionError("radius3 processed mismatch")
    if sum(row.get("first_obstruction_zero", 0) for row in rows) != expected_first_zero:
        raise AssertionError("radius3 first-obstruction mismatch")
    if max(row.get("elapsed_sec", 999.0) for row in rows) >= 60:
        raise AssertionError("radius3 timeout-risk shard")


def require_h8_radius3_profile(cert: dict) -> None:
    require_h8_radius3_certificate(cert, [262337], 320)
    expected_suffix = [67800000, 320, 0, 0, 0, 0, 0, 0]
    if cert.get("suffix_counts") != expected_suffix:
        raise AssertionError(("radius3 profile suffix", cert.get("suffix_counts")))
    if cert.get("deep_examples") != []:
        raise AssertionError("radius3 profile has depth >= 2 examples")
    suffix = [0] * 8
    for row in cert["rows"]:
        row_suffix = row.get("suffix_counts")
        if not isinstance(row_suffix, list) or len(row_suffix) != 8:
            raise AssertionError(("radius3 row suffix", row_suffix))
        if sum(row_suffix) != row.get("processed"):
            raise AssertionError(("radius3 row suffix sum", row))
        if sum(row_suffix[1:]) != row.get("first_obstruction_zero"):
            raise AssertionError(("radius3 row first zero", row))
        for index, count in enumerate(row_suffix):
            suffix[index] += count
    if suffix != expected_suffix:
        raise AssertionError(("radius3 profile row aggregate", suffix))


def main() -> None:
    loaded = {filename: load_rows(filename) for filename in FULL_ZERO_ROWS}
    full_count = 0
    for filename, names in FULL_ZERO_ROWS.items():
        rows = loaded[filename]
        for name in names:
            require_zero_full(rows[name])
            full_count += 1

    a1 = loaded["f3a1_results.json"]
    for name in PARTIAL_H8_ROWS:
        require_zero_partial(a1[name])
    h8_full = json.loads((NOTES / "f3_h8_n32_full_certificate.json").read_text())
    require_h8_full_certificate(h8_full, 1153)
    h8_multi = json.loads((NOTES / "f3_h8_n32_multirow_certificate.json").read_text())
    if [row["p"] for row in h8_multi] != [1153, 3137, 12289, 40961, 61441, 65537]:
        raise AssertionError(h8_multi)
    for row in h8_multi:
        require_h8_full_certificate(row, row["p"])
    h6_n64 = json.loads((NOTES / "f3_h6_n64_boundary_certificate.json").read_text())
    require_h6_n64_certificate(h6_n64)
    h6_n64_extra = json.loads(
        (NOTES / "f3_h6_n64_extra_primes_certificate.json").read_text()
    )
    require_h6_n64_extra_certificate(h6_n64_extra)
    h7_n64 = json.loads((NOTES / "f3_h7_n64_boundary_certificate.json").read_text())
    require_h7_n64_certificate(h7_n64)
    h8_radius3 = json.loads(
        (NOTES / "f3_h8_n64_x83_radius3_shell_certificate.json").read_text()
    )
    require_h8_radius3_certificate(h8_radius3, [262337], 320)
    h8_radius3_p4289 = json.loads(
        (NOTES / "f3_h8_n64_x83_radius3_shell_certificate_p4289.json").read_text()
    )
    require_h8_radius3_certificate(h8_radius3_p4289, [4289], 16048)
    h8_radius3_profile = json.loads(
        (NOTES / "f3_h8_n64_x83_radius3_profile_q3.json").read_text()
    )
    require_h8_radius3_profile(h8_radius3_profile)

    print(f"h=6/h=7 full zero rows verified: {full_count}")
    print("h=6 n64 full anchored certificates verified: 1")
    print("h=6 n64 extra full anchored sweeps verified: 6 (p4993 has 6 nontoral, below n^3)")
    print("h=7 n64 full anchored certificates verified: 1")
    print("h=8 full anchored certificates verified: 6")
    print("h=8 n64 x83 radius-three shell certificates verified: 2")
    print("h=8 n64 x83 radius-three q3 suffix profile verified: 1")
    print(f"h=8 partial zero slices remaining: {len(PARTIAL_H8_ROWS)}")
    print("H6_H8_BONUS_SWEEP_PASS")


if __name__ == "__main__":
    main()
