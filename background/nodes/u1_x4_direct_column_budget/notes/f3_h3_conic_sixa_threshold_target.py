#!/usr/bin/env python3
"""Six-A threshold target for the h=3 conic binary-form rank route."""

from __future__ import annotations

from f3_h3_conic_chart_degree_space_guard import conic_chart_rank
from f3_h3_exact_profile_bridge_budget import EXPECTED_ROWS
from f3_h3_exact_profile_rank_deficit_budget import rank_deficit_budget_summary


THRESHOLD_CASE = (5, 4, 30)
EXPECTED_THRESHOLD_RANK = 320
PASS_CASES = (
    (2, 4, 12, 128, 128, 0),
    (3, 4, 18, 192, 192, 0),
    (4, 4, 24, 256, 256, 0),
    (5, 4, 30, 320, 320, 0),
)
FAIL_CASES = (
    (3, 5, 18, 346, 375, 29),
    (4, 5, 24, 468, 500, 32),
    (3, 6, 18, 459, 543, 84),
)


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


def checked_rank_case(case: tuple[int, int, int, int, int, int]) -> tuple[int, int, int]:
    a_count, b_count, h_order, expected_rank, expected_target, expected_deficit = case
    rank, degree_dim, coefficient_dim = conic_chart_rank(a_count, b_count, h_order)
    target = min(degree_dim, coefficient_dim)
    deficit = target - rank
    if (rank, target, deficit) != (
        expected_rank,
        expected_target,
        expected_deficit,
    ):
        raise AssertionError((case, rank, target, deficit))
    return rank, target, deficit


def sixa_threshold_summary() -> dict[str, int]:
    for case in (*PASS_CASES, *FAIL_CASES):
        checked_rank_case(case)
    official = official_sixa_summary()
    deficit = rank_deficit_budget_summary()
    if official["min_margin"] != 20:
        raise AssertionError(official)
    if official["min_b"] != 34:
        raise AssertionError(official)
    if deficit["min_allowed_deficit"] != 1847:
        raise AssertionError(deficit)

    return {
        "threshold_a": THRESHOLD_CASE[0],
        "threshold_b": THRESHOLD_CASE[1],
        "threshold_h": THRESHOLD_CASE[2],
        "threshold_rank": EXPECTED_THRESHOLD_RANK,
        "threshold_target": EXPECTED_THRESHOLD_RANK,
        "threshold_deficit": 0,
        "pass_cases": len(PASS_CASES),
        "fail_cases": len(FAIL_CASES),
        "max_fail_deficit": max(case[-1] for case in FAIL_CASES),
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
        "guardrail: H >= 6A alone is not a sufficient theorem outside the "
        "official dense regime"
    )
    print(
        f"bounded checks: pass_cases={summary['pass_cases']} "
        f"fail_cases={summary['fail_cases']} "
        f"max_fail_deficit={summary['max_fail_deficit']}"
    )
    print(f"official fallback codimension allowance={summary['allowed_deficit']}")
    print("H3_CONIC_SIXA_THRESHOLD_TARGET_PASS")


if __name__ == "__main__":
    main()
