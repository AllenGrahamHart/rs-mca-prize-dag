#!/usr/bin/env python3
"""Official-row separation guard for the h=3 private-linear route."""

from __future__ import annotations

from f3_h3_private_linear_lowrow_budget import EXPECTED_ROWS


def separation_summary() -> dict[str, int]:
    min_pass_margin = None
    min_next_margin = None
    min_cap_margin = None
    for row in EXPECTED_ROWS:
        h_order = 1 << row.s
        pass_margin = h_order - max(row.a, row.d, row.b - 1)
        next_margin = h_order - max(row.next_a, row.next_d, row.next_b - 1)
        cap_margin = h_order - (row.next_b_cap - 1)
        if pass_margin <= 0 or next_margin <= 0 or cap_margin <= 0:
            raise AssertionError((row, pass_margin, next_margin, cap_margin))
        min_pass_margin = (
            pass_margin if min_pass_margin is None else min(min_pass_margin, pass_margin)
        )
        min_next_margin = (
            next_margin if min_next_margin is None else min(min_next_margin, next_margin)
        )
        min_cap_margin = (
            cap_margin if min_cap_margin is None else min(min_cap_margin, cap_margin)
        )
    return {
        "rows": len(EXPECTED_ROWS),
        "first_s": EXPECTED_ROWS[0].s,
        "last_s": EXPECTED_ROWS[-1].s,
        "min_pass_margin": int(min_pass_margin),
        "min_next_margin": int(min_next_margin),
        "min_cap_margin": int(min_cap_margin),
        "max_pass_b": max(row.b for row in EXPECTED_ROWS),
        "max_next_b": max(row.next_b for row in EXPECTED_ROWS),
        "max_next_b_cap": max(row.next_b_cap for row in EXPECTED_ROWS),
    }


def main() -> None:
    summary = separation_summary()
    expected = {
        "rows": 29,
        "first_s": 13,
        "last_s": 41,
        "min_pass_margin": 7904,
        "min_next_margin": 7911,
        "min_cap_margin": 8099,
        "max_pass_b": 41284,
        "max_next_b": 41284,
        "max_next_b_cap": 61931,
    }
    if summary != expected:
        raise AssertionError(summary)

    print("h=3 private-linear official separation guard")
    print(
        f"official rows: s={summary['first_s']}..{summary['last_s']} "
        f"count={summary['rows']}"
    )
    print(
        "min H-max(A,D,B-1) margins: "
        f"passing={summary['min_pass_margin']} "
        f"next_failure={summary['min_next_margin']}"
    )
    print(f"min H-(next_B_cap-1) margin: {summary['min_cap_margin']}")
    print(
        "max B values: "
        f"passing={summary['max_pass_b']} "
        f"next={summary['max_next_b']} "
        f"next_cap={summary['max_next_b_cap']}"
    )
    print("every official private-linear box lies in the separated regime max(A,D,B-1)<H")
    print("H3_PRIVATE_LINEAR_OFFICIAL_SEPARATION_GUARD_PASS")


if __name__ == "__main__":
    main()
