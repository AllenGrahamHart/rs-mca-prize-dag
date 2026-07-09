#!/usr/bin/env python3
"""Large-gap pilot for the h=3 same-fiber conic-chart rank target."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from f3_h3_conic_chart_degree_space_guard import conic_chart_rank
from f3_h3_exact_profile_bridge_budget import EXPECTED_ROWS
from f3_h3_exact_profile_rank_deficit_budget import rank_deficit_budget_summary


@dataclass(frozen=True)
class PilotCase:
    a_count: int
    b_count: int
    h_order: int
    expected_rank: int


CASES = (
    PilotCase(5, 4, 20, 293),
    PilotCase(5, 4, 24, 319),
    PilotCase(5, 4, 32, 320),
)


@dataclass(frozen=True)
class PilotRow:
    a_count: int
    b_count: int
    h_order: int
    rank: int
    target: int
    deficit: int
    h_over_a: Fraction


def pilot_rows() -> tuple[PilotRow, ...]:
    rows: list[PilotRow] = []
    for case in CASES:
        rank, degree_dim, coefficient_dim = conic_chart_rank(
            case.a_count, case.b_count, case.h_order
        )
        target = min(degree_dim, coefficient_dim)
        if rank != case.expected_rank:
            raise AssertionError((case, rank, target))
        rows.append(
            PilotRow(
                a_count=case.a_count,
                b_count=case.b_count,
                h_order=case.h_order,
                rank=rank,
                target=target,
                deficit=target - rank,
                h_over_a=Fraction(case.h_order, case.a_count),
            )
        )
    return tuple(rows)


def official_gap_summary() -> dict[str, int]:
    gaps = []
    for row in EXPECTED_ROWS:
        h = 2**row.s
        gaps.append((Fraction(h, row.a), row.s, h, row.a))
    gap, s, h, a = min(gaps)
    return {
        "official_rows": len(EXPECTED_ROWS),
        "min_gap_s": s,
        "min_gap_num": gap.numerator,
        "min_gap_den": gap.denominator,
        "min_gap_ppm": gap.numerator * 1_000_000 // gap.denominator,
        "min_gap_h": h,
        "min_gap_a": a,
    }


def largegap_pilot_summary() -> dict[str, int]:
    rows = pilot_rows()
    official = official_gap_summary()
    deficit = rank_deficit_budget_summary()
    expected = {
        (5, 4, 20): (293, 320, 27),
        (5, 4, 24): (319, 320, 1),
        (5, 4, 32): (320, 320, 0),
    }
    actual = {
        (row.a_count, row.b_count, row.h_order): (row.rank, row.target, row.deficit)
        for row in rows
    }
    if actual != expected:
        raise AssertionError(actual)
    if official["min_gap_s"] != 13:
        raise AssertionError(official)
    if deficit["min_allowed_deficit"] != 1847:
        raise AssertionError(deficit)
    return {
        "cases": len(rows),
        "max_pilot_deficit": max(row.deficit for row in rows),
        "min_pilot_deficit": min(row.deficit for row in rows),
        "full_cases": sum(1 for row in rows if row.deficit == 0),
        "official_min_gap_ppm": official["min_gap_ppm"],
        "official_min_gap_s": official["min_gap_s"],
        "official_min_gap_h": official["min_gap_h"],
        "official_min_gap_a": official["min_gap_a"],
        "allowed_deficit": deficit["min_allowed_deficit"],
    }


def main() -> None:
    summary = largegap_pilot_summary()
    print("h=3 conic-chart large-gap pilot")
    print("same toy chart as the conic degree-space guardrail")
    print(" A   B   H   H/A        rank  target  deficit")
    for row in pilot_rows():
        print(
            f"{row.a_count:2d} {row.b_count:3d} {row.h_order:3d} "
            f"{row.h_over_a.numerator}/{row.h_over_a.denominator:<7d} "
            f"{row.rank:6d} {row.target:7d} {row.deficit:8d}"
        )
    print(
        "official exact-profile gap: "
        f"min H/A occurs at s={summary['official_min_gap_s']} with "
        f"H={summary['official_min_gap_h']} A={summary['official_min_gap_a']} "
        f"ratio_ppm={summary['official_min_gap_ppm']}"
    )
    print(
        "summary: "
        f"cases={summary['cases']} "
        f"pilot_deficit={summary['min_pilot_deficit']}.."
        f"{summary['max_pilot_deficit']} "
        f"full_cases={summary['full_cases']} "
        f"allowed_deficit={summary['allowed_deficit']}"
    )
    print("H3_CONIC_CHART_LARGEGAP_PILOT_PASS")


if __name__ == "__main__":
    main()
