#!/usr/bin/env python3
"""Replay checker for the h=6/7/8 bonus sweep status."""

from __future__ import annotations

import json
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
    if [row["p"] for row in h8_multi] != [1153, 3137, 12289]:
        raise AssertionError(h8_multi)
    for row in h8_multi:
        require_h8_full_certificate(row, row["p"])

    print(f"h=6/h=7 full zero rows verified: {full_count}")
    print("h=8 full anchored certificates verified: 3")
    print(f"h=8 partial zero slices remaining: {len(PARTIAL_H8_ROWS)}")
    print("H6_H8_BONUS_SWEEP_PASS")


if __name__ == "__main__":
    main()
