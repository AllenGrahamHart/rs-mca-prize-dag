#!/usr/bin/env python3
"""Six-A threshold target for the h=3 conic binary-form rank route."""

from __future__ import annotations

from f3_h3_conic_chart_degree_space_guard import conic_chart_rank
from f3_h3_exact_profile_bridge_budget import EXPECTED_ROWS
from f3_h3_exact_profile_rank_deficit_budget import rank_deficit_budget_summary


THRESHOLD_CASE = (5, 4, 30)
EXPECTED_THRESHOLD_RANK = 320


def official_sixa_summary() -> dict[str, int]:
    margins = []
    for row in EXPECTED_ROWS:
        h_order = 2**row.s
        margins.append((h_order - 6 * row.a, row.s, h_order, row.a, row.b))
    margin, s, h_order, a_count, b_count = min(margins)
    return {
        "rows": len(EXPECTED_ROWS),
        "min_margin": margin,
        "tight_s": s,
        "tight_h": h_order,
        "tight_a": a_count,
        "tight_b": b_count,
        "min_b": min(row.b for row in EXPECTED_ROWS),
        "max_b": max(row.b for row in EXPECTED_ROWS),
    }


def sixa_threshold_summary() -> dict[str, int]:
    a_count, b_count, h_order = THRESHOLD_CASE
    rank, degree_dim, coefficient_dim = conic_chart_rank(a_count, b_count, h_order)
    target = min(degree_dim, coefficient_dim)
    if rank != EXPECTED_THRESHOLD_RANK or rank != target:
        raise AssertionError((rank, target, THRESHOLD_CASE))

    official = official_sixa_summary()
    deficit = rank_deficit_budget_summary()
    if official["min_margin"] != 20:
        raise AssertionError(official)
    if official["min_b"] != 34:
        raise AssertionError(official)
    if deficit["min_allowed_deficit"] != 1847:
        raise AssertionError(deficit)

    return {
        "threshold_a": a_count,
        "threshold_b": b_count,
        "threshold_h": h_order,
        "threshold_rank": rank,
        "threshold_target": target,
        "threshold_deficit": target - rank,
        "official_rows": official["rows"],
        "official_min_h_minus_6a": official["min_margin"],
        "official_tight_s": official["tight_s"],
        "official_tight_h": official["tight_h"],
        "official_tight_a": official["tight_a"],
        "official_tight_b": official["tight_b"],
        "official_min_b": official["min_b"],
        "official_max_b": official["max_b"],
        "allowed_deficit": deficit["min_allowed_deficit"],
    }


def main() -> None:
    summary = sixa_threshold_summary()
    print("h=3 conic six-A threshold target")
    print(
        "threshold toy row: "
        f"A={summary['threshold_a']} B={summary['threshold_b']} "
        f"H={summary['threshold_h']} rank={summary['threshold_rank']} "
        f"target={summary['threshold_target']} "
        f"deficit={summary['threshold_deficit']}"
    )
    print(
        "official exact-profile rows: "
        f"rows={summary['official_rows']} "
        f"min(H-6A)={summary['official_min_h_minus_6a']} "
        f"tight_s={summary['official_tight_s']} "
        f"B={summary['official_min_b']}..{summary['official_max_b']}"
    )
    print(
        "sufficient theorem target: full conic binary-form rank whenever "
        "H >= 6A on the repaired same-fiber conic charts"
    )
    print(f"official fallback codimension allowance={summary['allowed_deficit']}")
    print("H3_CONIC_SIXA_THRESHOLD_TARGET_PASS")


if __name__ == "__main__":
    main()
