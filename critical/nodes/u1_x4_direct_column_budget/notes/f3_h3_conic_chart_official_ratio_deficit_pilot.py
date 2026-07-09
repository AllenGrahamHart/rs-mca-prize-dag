#!/usr/bin/env python3
"""Small official-ratio deficit pilot for h=3 conic-chart rank."""

from __future__ import annotations

from dataclasses import dataclass

from f3_h3_conic_chart_degree_space_guard import conic_chart_rank


@dataclass(frozen=True)
class PilotCase:
    a_count: int
    b_count: int
    h_order: int
    expected_rank: int
    expected_naive: int


CASES = (
    PilotCase(2, 4, 8, 118, 128),
    PilotCase(2, 6, 8, 214, 242),
    PilotCase(2, 8, 8, 310, 338),
    PilotCase(3, 4, 16, 192, 192),
    PilotCase(3, 6, 16, 414, 483),
    PilotCase(4, 4, 24, 256, 256),
)


def pilot_summary() -> dict[str, int]:
    deficits = []
    for case in CASES:
        rank, degree_dim, coefficient_dim = conic_chart_rank(
            case.a_count, case.b_count, case.h_order
        )
        naive = min(degree_dim, coefficient_dim)
        if (rank, naive) != (case.expected_rank, case.expected_naive):
            raise AssertionError((case, rank, naive))
        deficits.append(naive - rank)
    return {
        "cases": len(CASES),
        "max_deficit": max(deficits),
        "positive_deficit_cases": sum(1 for deficit in deficits if deficit),
        "full_cases": sum(1 for deficit in deficits if not deficit),
    }


def main() -> None:
    print("h=3 conic-chart official-ratio deficit pilot")
    print("same toy chart: p=769, a=37, b=706, base=(101,333)")
    print(" A   B   H   rank  min(AB^3,L+1)  deficit")
    for case in CASES:
        rank, degree_dim, coefficient_dim = conic_chart_rank(
            case.a_count, case.b_count, case.h_order
        )
        naive = min(degree_dim, coefficient_dim)
        print(
            f"{case.a_count:2d} {case.b_count:3d} {case.h_order:3d}"
            f" {rank:6d} {naive:14d} {naive - rank:8d}"
        )
    summary = pilot_summary()
    print(
        "summary: "
        f"cases={summary['cases']} "
        f"positive_deficit_cases={summary['positive_deficit_cases']} "
        f"full_cases={summary['full_cases']} "
        f"max_deficit={summary['max_deficit']}"
    )
    print("This is a small route-selection pilot, not a uniform rank theorem.")
    print("H3_CONIC_CHART_OFFICIAL_RATIO_DEFICIT_PILOT_PASS")


if __name__ == "__main__":
    main()
