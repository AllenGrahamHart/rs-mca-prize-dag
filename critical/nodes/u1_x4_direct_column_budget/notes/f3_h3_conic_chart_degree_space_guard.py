#!/usr/bin/env python3
"""Guardrail against overclaiming conic-chart degree-space fullness."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product

from f3_h3_rich_curve_rank_sample import (
    P,
    conic_chart_curve,
    monomial_x,
    mul,
    pow_poly,
    rank_columns,
)


@dataclass(frozen=True)
class RankCase:
    a_count: int
    b_count: int
    h_order: int
    expected_rank: int


CASES = (
    RankCase(5, 4, 32, 320),
    RankCase(5, 4, 16, 247),
    RankCase(5, 4, 8, 137),
    RankCase(5, 4, 4, 74),
    RankCase(5, 6, 4, 122),
    RankCase(12, 5, 4, 108),
    RankCase(16, 4, 8, 160),
)


def precompute_powers(curve, b_count: int, h_order: int) -> tuple[list[list[int]], list[list[int]]]:
    p_powers = [[1] for _ in range(3 * b_count)]
    q_powers = [[1] for _ in range(3 * b_count)]
    for index, (poly_p, poly_q) in enumerate(zip(curve.ps, curve.qs)):
        for b_exp in range(b_count):
            p_powers[index * b_count + b_exp] = pow_poly(list(poly_p), h_order * b_exp)
            q_powers[index * b_count + b_exp] = pow_poly(
                list(poly_q), h_order * (b_count - 1 - b_exp)
            )
    return p_powers, q_powers


def column_for_box(
    p_powers: list[list[int]],
    q_powers: list[list[int]],
    b_count: int,
    a_exp: int,
    bs: tuple[int, int, int],
    degree_cap: int,
) -> list[int]:
    polynomial = monomial_x(a_exp)
    for index, b_exp in enumerate(bs):
        polynomial = mul(polynomial, p_powers[index * b_count + b_exp])
        polynomial = mul(polynomial, q_powers[index * b_count + b_exp])
    if len(polynomial) > degree_cap + 1:
        raise AssertionError((len(polynomial) - 1, degree_cap))
    return polynomial + [0] * (degree_cap + 1 - len(polynomial))


def conic_chart_rank(a_count: int, b_count: int, h_order: int) -> tuple[int, int, int]:
    curve, _ = conic_chart_curve()
    degree_cap = (a_count - 1) + 6 * h_order * (b_count - 1)
    p_powers, q_powers = precompute_powers(curve, b_count, h_order)
    columns = []
    for a, bs in product(range(a_count), product(range(b_count), repeat=3)):
        columns.append(column_for_box(p_powers, q_powers, b_count, a, bs, degree_cap))
    return rank_columns(columns), degree_cap + 1, a_count * b_count**3


def degree_space_guard_summary() -> dict[str, int]:
    failures = 0
    successes = 0
    min_deficit = None
    max_deficit = 0
    for case in CASES:
        rank, degree_dim, coefficient_dim = conic_chart_rank(
            case.a_count, case.b_count, case.h_order
        )
        naive_fullness = min(degree_dim, coefficient_dim)
        if rank != case.expected_rank:
            raise AssertionError((case, rank, naive_fullness))
        deficit = naive_fullness - rank
        if deficit:
            failures += 1
            min_deficit = deficit if min_deficit is None else min(min_deficit, deficit)
            max_deficit = max(max_deficit, deficit)
        else:
            successes += 1
    if failures != 4 or successes != 3:
        raise AssertionError((failures, successes))
    return {
        "cases": len(CASES),
        "fullness_failures": failures,
        "fullness_successes": successes,
        "min_positive_deficit": min_deficit or 0,
        "max_deficit": max_deficit,
    }


def main() -> None:
    print("h=3 conic-chart degree-space guardrail")
    print("same toy chart: p=769, a=37, b=706, base=(101,333)")
    print(" A   B   H   rank  min(AB^3,L+1)  deficit  status")
    for case in CASES:
        rank, degree_dim, coefficient_dim = conic_chart_rank(
            case.a_count, case.b_count, case.h_order
        )
        naive_fullness = min(degree_dim, coefficient_dim)
        deficit = naive_fullness - rank
        status = "FULL" if deficit == 0 else "DEFICIT"
        print(
            f"{case.a_count:2d} {case.b_count:3d} {case.h_order:3d}"
            f" {rank:6d} {naive_fullness:14d} {deficit:8d} {status}"
        )
    summary = degree_space_guard_summary()
    print(
        "summary: "
        f"cases={summary['cases']} "
        f"fullness_failures={summary['fullness_failures']} "
        f"fullness_successes={summary['fullness_successes']} "
        f"deficit_range={summary['min_positive_deficit']}..{summary['max_deficit']}"
    )
    print("Do not state conic-chart RC-RANK as automatic degree-space fullness.")
    print("H3_CONIC_CHART_DEGREE_SPACE_GUARD_PASS")


if __name__ == "__main__":
    main()
