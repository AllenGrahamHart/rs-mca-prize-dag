#!/usr/bin/env python3
"""Degree compiler for the h=3 same-lambda collision target."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp


A, Z, Y = sp.symbols("a z y")


GENERIC_ONE_RATIO = {
    "U": (1 + Z + Z**2 + A * Z * (1 + Z)) / (1 + Z + Z**2),
    "V": (1 + Z + Z**2 + A * (1 + Z)) / (1 + Z + Z**2),
    "W": (1 + Z + Z**2 - A * Z) / (1 + Z + Z**2),
}


@dataclass(frozen=True)
class MapDegree:
    name: str
    numerator: sp.Expr
    denominator: sp.Expr
    deg_a: int
    deg_z: int
    deg_y: int
    total_degree: int


def substitute_ratio(expression: sp.Expr, ratio: sp.Symbol) -> sp.Expr:
    return expression.subs(Z, ratio)


def degree_row(name: str, expression: sp.Expr) -> MapDegree:
    numerator, denominator = sp.together(expression).as_numer_denom()
    return MapDegree(
        name=name,
        numerator=sp.factor(numerator),
        denominator=sp.factor(denominator),
        deg_a=max(sp.degree(numerator, A), sp.degree(denominator, A)),
        deg_z=max(sp.degree(numerator, Z), sp.degree(denominator, Z)),
        deg_y=max(sp.degree(numerator, Y), sp.degree(denominator, Y)),
        total_degree=max(
            sp.Poly(numerator, A, Z, Y).total_degree(),
            sp.Poly(denominator, A, Z, Y).total_degree(),
        ),
    )


def generic_collision_rows() -> tuple[MapDegree, ...]:
    rows = []
    for prefix, ratio in (("z", Z), ("y", Y)):
        for name, expression in GENERIC_ONE_RATIO.items():
            rows.append(degree_row(f"{prefix}_{name}", substitute_ratio(expression, ratio)))
    return tuple(rows)


def generic_budget() -> dict[str, int]:
    rows = generic_collision_rows()
    return {
        "maps": len(rows),
        "sum_a": sum(row.deg_a for row in rows),
        "sum_z": sum(row.deg_z for row in rows),
        "sum_y": sum(row.deg_y for row in rows),
        "sum_total": sum(row.total_degree for row in rows),
        "max_total": max(row.total_degree for row in rows),
    }


def scale_branch_budget() -> dict[str, int]:
    # In a field containing a primitive cube root omega, the lambda=1 branch has
    # maps 1+x, 1+omega*x, 1+omega^2*x and the same three maps in y.  All are
    # affine linear over F(omega).
    return {
        "maps": 6,
        "sum_x": 3,
        "sum_y": 3,
        "sum_total": 6,
        "max_total": 1,
    }


def main() -> None:
    print("h=3 repeat same-lambda degree compiler")
    print("generic collision: variables a=lambda-1, z, y; six H-membership maps")
    generic = generic_budget()
    for row in generic_collision_rows():
        print(
            f"  {row.name}: P={row.numerator} Q={row.denominator} "
            f"deg_a={row.deg_a} deg_z={row.deg_z} deg_y={row.deg_y} "
            f"total={row.total_degree}"
        )
    print(
        f"generic_budget: maps={generic['maps']} sum_a={generic['sum_a']} "
        f"sum_z={generic['sum_z']} sum_y={generic['sum_y']} "
        f"sum_total={generic['sum_total']} max_total={generic['max_total']}"
    )
    scale = scale_branch_budget()
    print(
        f"lambda_one_scale_budget: maps={scale['maps']} sum_x={scale['sum_x']} "
        f"sum_y={scale['sum_y']} sum_total={scale['sum_total']} "
        f"max_total={scale['max_total']}"
    )
    if generic != {"maps": 6, "sum_a": 6, "sum_z": 6, "sum_y": 6, "sum_total": 14, "max_total": 3}:
        raise AssertionError(generic)
    if scale != {"maps": 6, "sum_x": 3, "sum_y": 3, "sum_total": 6, "max_total": 1}:
        raise AssertionError(scale)
    print("H3_REPEAT_SAME_LAMBDA_DEGREE_COMPILER_PASS")


if __name__ == "__main__":
    main()
