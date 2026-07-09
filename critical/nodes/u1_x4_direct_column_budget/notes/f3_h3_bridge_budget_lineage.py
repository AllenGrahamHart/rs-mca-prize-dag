#!/usr/bin/env python3
"""Replay the h=3 bridge-budget lineage from diagonal to non-diagonal boxes."""

from __future__ import annotations

from f3_h3_bridge_budget_compiler import EXPECTED_BUDGETS as DIAGONAL_BUDGETS
from f3_h3_nondiagonal_highrow_budget import EXPECTED_ROWS as HIGH_ROWS
from f3_h3_nondiagonal_lowrow_budget import EXPECTED_ROWS as LOW_ROWS


def budget_lineage_summary() -> dict[str, int]:
    rows = (*LOW_ROWS, *HIGH_ROWS)
    if [row.s for row in rows] != list(range(13, 42)):
        raise AssertionError([row.s for row in rows])
    mismatches = [
        (row.s, row.old_z, DIAGONAL_BUDGETS[row.s])
        for row in rows
        if row.old_z != DIAGONAL_BUDGETS[row.s]
    ]
    if mismatches:
        raise AssertionError(mismatches)
    gains = [row.z - row.old_z for row in rows]
    if any(gain <= 0 for gain in gains):
        raise AssertionError(gains)
    return {
        "rows": len(rows),
        "first_s": rows[0].s,
        "last_s": rows[-1].s,
        "diagonal_min": min(row.old_z for row in rows),
        "diagonal_max": max(row.old_z for row in rows),
        "nondiagonal_min": min(row.z for row in rows),
        "nondiagonal_max": max(row.z for row in rows),
        "diagonal_total": sum(row.old_z for row in rows),
        "nondiagonal_total": sum(row.z for row in rows),
        "gain_min": min(gains),
        "gain_max": max(gains),
        "gain_total": sum(gains),
        "first_gain": gains[0],
        "last_gain": gains[-1],
    }


def main() -> None:
    summary = budget_lineage_summary()
    print("h=3 bridge-budget lineage")
    print(
        f"official_rows=s={summary['first_s']}..{summary['last_s']} "
        f"count={summary['rows']}"
    )
    print(
        "diagonal legacy budget: "
        f"Z={summary['diagonal_min']}..{summary['diagonal_max']} "
        f"total={summary['diagonal_total']}"
    )
    print(
        "active non-diagonal budget: "
        f"Z={summary['nondiagonal_min']}..{summary['nondiagonal_max']} "
        f"total={summary['nondiagonal_total']}"
    )
    print(
        "improvement: "
        f"min_gain={summary['gain_min']} max_gain={summary['gain_max']} "
        f"total_gain={summary['gain_total']} "
        f"first_gain={summary['first_gain']} last_gain={summary['last_gain']}"
    )
    print("active bridge target uses the non-diagonal Z_budget table")
    print("H3_BRIDGE_BUDGET_LINEAGE_PASS")


if __name__ == "__main__":
    main()
