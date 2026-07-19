#!/usr/bin/env python3
"""Guardrail for the affine linear relation in h=3 conic charts."""

from __future__ import annotations

import sympy as sp

from f3_h3_conic_chart_degree_space_guard import CASES as DEGREE_SPACE_CASES
from f3_h3_conic_chart_official_ratio_deficit_pilot import CASES as PILOT_CASES
from f3_h3_rich_curve_rank_sample import P, conic_chart_curve


X = sp.symbols("X")


def pad(poly: tuple[int, ...], length: int) -> tuple[int, ...]:
    return poly + (0,) * (length - len(poly))


def relation_coefficients() -> tuple[int, ...]:
    curve, _ = conic_chart_curve()
    numerators = curve.ps
    denominator = curve.qs[0]
    max_length = max(len(poly) for poly in (*numerators, denominator))
    total = [0] * max_length
    for poly in numerators:
        for index, coefficient in enumerate(pad(poly, max_length)):
            total[index] = (total[index] + coefficient) % P
    a = 37
    for index, coefficient in enumerate(pad(denominator, max_length)):
        total[index] = (total[index] + a * coefficient) % P
    return tuple(total)


def poly_expr(poly: tuple[int, ...]) -> sp.Expr:
    return sum(coefficient * X**index for index, coefficient in enumerate(poly))


def gcd_degree(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    left_poly = sp.Poly(poly_expr(left), X, modulus=P)
    right_poly = sp.Poly(poly_expr(right), X, modulus=P)
    return sp.gcd(left_poly, right_poly).degree()


def linear_relation_guard_summary() -> dict[str, int]:
    curve, conic_b = conic_chart_curve()
    relation = relation_coefficients()
    if any(coefficient % P for coefficient in relation):
        raise AssertionError(relation)

    polys = (*curve.ps, curve.qs[0])
    pairwise_gcd_degrees = [
        gcd_degree(polys[i], polys[j])
        for i in range(len(polys))
        for j in range(i + 1, len(polys))
    ]
    if any(degree != 0 for degree in pairwise_gcd_degrees):
        raise AssertionError(pairwise_gcd_degrees)

    degree_deficits = []
    for row in DEGREE_SPACE_CASES:
        degree_dim = row.a_count + 6 * row.h_order * (row.b_count - 1)
        naive = min(degree_dim, row.a_count * row.b_count**3)
        degree_deficits.append(naive - row.expected_rank)
    pilot_deficits = [row.expected_naive - row.expected_rank for row in PILOT_CASES]
    if sum(1 for deficit in degree_deficits if deficit) != 4:
        raise AssertionError(degree_deficits)
    if sum(1 for deficit in pilot_deficits if deficit) != 4:
        raise AssertionError(pilot_deficits)
    return {
        "p": P,
        "a": 37,
        "b": conic_b,
        "polynomials": len(polys),
        "pairwise_gcd_checks": len(pairwise_gcd_degrees),
        "max_gcd_degree": max(pairwise_gcd_degrees),
        "degree_guard_failures": sum(1 for deficit in degree_deficits if deficit),
        "degree_guard_max_deficit": max(degree_deficits),
        "pilot_failures": sum(1 for deficit in pilot_deficits if deficit),
        "pilot_max_deficit": max(pilot_deficits),
    }


def main() -> None:
    summary = linear_relation_guard_summary()
    print("h=3 conic-chart linear-relation guard")
    print(
        f"p={summary['p']} a={summary['a']} b={summary['b']} "
        "relation: P_U + P_V + P_W + a Q = 0"
    )
    print(
        f"pairwise gcd checks={summary['pairwise_gcd_checks']} "
        f"max_gcd_degree={summary['max_gcd_degree']}"
    )
    print(
        "rank guardrails with deficits: "
        f"degree_space={summary['degree_guard_failures']} "
        f"(max_deficit={summary['degree_guard_max_deficit']}), "
        f"official_ratio_pilot={summary['pilot_failures']} "
        f"(max_deficit={summary['pilot_max_deficit']})"
    )
    print("Separated divisors alone do not prove conic-chart full rank.")
    print("H3_CONIC_CHART_LINEAR_RELATION_GUARD_PASS")


if __name__ == "__main__":
    main()
