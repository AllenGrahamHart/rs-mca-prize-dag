#!/usr/bin/env python3
"""Degree compiler for the generic loose nine-slope membership maps."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp


A, B, X = sp.symbols("a b X")

GENERIC_SLOPES = {
    "C_1": sp.Integer(1),
    "C_a": 1 / A,
    "C_b": 1 / B,
    "C_1a": -1 / (1 + A),
    "C_1b": -1 / (1 + B),
    "C_ab": -1 / (A + B),
    "L_a": 1 + 1 / A - 1 / (1 + A),
    "L_b": 1 + 1 / B - 1 / (1 + B),
    "L_ab": 1 / A + 1 / B - 1 / (A + B),
}


@dataclass(frozen=True)
class GenericMapDegree:
    name: str
    numerator: sp.Expr
    denominator: sp.Expr
    deg_a: int
    deg_b: int
    deg_x: int
    total_degree: int


def membership_map(slope: sp.Expr) -> tuple[sp.Expr, sp.Expr]:
    numerator, denominator = sp.together(1 + X * slope).as_numer_denom()
    if sp.degree(denominator, X) != 0:
        raise AssertionError((slope, denominator, "denominator depends on X"))
    if sp.degree(numerator, X) > 1:
        raise AssertionError((slope, numerator, "unexpected X degree"))
    return sp.factor(numerator), sp.factor(denominator)


def degree_row(name: str, slope: sp.Expr) -> GenericMapDegree:
    numerator, denominator = membership_map(slope)
    return GenericMapDegree(
        name=name,
        numerator=numerator,
        denominator=denominator,
        deg_a=max(sp.degree(numerator, A), sp.degree(denominator, A)),
        deg_b=max(sp.degree(numerator, B), sp.degree(denominator, B)),
        deg_x=sp.degree(numerator, X),
        total_degree=max(
            sp.Poly(numerator, A, B, X).total_degree(),
            sp.Poly(denominator, A, B, X).total_degree(),
        ),
    )


def generic_rows() -> tuple[GenericMapDegree, ...]:
    return tuple(degree_row(name, slope) for name, slope in GENERIC_SLOPES.items())


def cleared_degree_bounds(
    subgroup_order: int, aux_a: int, aux_b: int, aux_x: int, aux_y: int
) -> dict[str, int]:
    if min(subgroup_order, aux_a, aux_b, aux_x, aux_y) < 1:
        raise ValueError((subgroup_order, aux_a, aux_b, aux_x, aux_y))
    rows = generic_rows()
    y_power = subgroup_order * (aux_y - 1)
    return {
        "a_degree": (aux_a - 1) + y_power * sum(row.deg_a for row in rows),
        "b_degree": (aux_b - 1) + y_power * sum(row.deg_b for row in rows),
        "x_degree": (aux_x - 1) + y_power * len(rows),
        "total_degree": (aux_a - 1)
        + (aux_b - 1)
        + (aux_x - 1)
        + y_power * sum(row.total_degree for row in rows),
    }


def main() -> None:
    print("h=3 repeat loose generic degree compiler")
    rows = generic_rows()
    sum_a = sum(row.deg_a for row in rows)
    sum_b = sum(row.deg_b for row in rows)
    sum_total = sum(row.total_degree for row in rows)
    print(
        f"generic_maps={len(rows)} sum_a_degrees={sum_a} "
        f"sum_b_degrees={sum_b} sum_total_degrees={sum_total}"
    )
    for row in rows:
        print(
            f"  {row.name}: P={sp.factor(row.numerator)} Q={sp.factor(row.denominator)} "
            f"deg_a={row.deg_a} deg_b={row.deg_b} deg_x={row.deg_x} "
            f"total={row.total_degree}"
        )
    sample = cleared_degree_bounds(subgroup_order=32, aux_a=16, aux_b=16, aux_x=16, aux_y=4)
    print(
        f"sample_clear_n32_A16_B16_X16_Y4: "
        f"a_degree={sample['a_degree']} b_degree={sample['b_degree']} "
        f"x_degree={sample['x_degree']} total_degree={sample['total_degree']}"
    )
    print("degree formula: a <= A-1+7n(Y-1), b <= B-1+7n(Y-1)")
    print("x <= X-1+9n(Y-1), total <= A+B+X-3+15n(Y-1)")
    print("H3_REPEAT_LOOSE_GENERIC_DEGREE_COMPILER_PASS")


if __name__ == "__main__":
    main()
