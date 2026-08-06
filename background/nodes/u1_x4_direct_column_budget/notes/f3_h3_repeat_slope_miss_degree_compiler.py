#!/usr/bin/env python3
"""Degree compiler for the generic h=3 slope-miss target."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp


A, B, Z, Y = sp.symbols("a b z y")


def norm(t: sp.Expr) -> sp.Expr:
    return 1 + t + t**2


def inv_num(alpha: sp.Expr, t: sp.Expr) -> sp.Expr:
    return -alpha**3 * t**2 * (1 + t) ** 2


def membership_maps(alpha: sp.Expr, t: sp.Expr, prefix: str) -> dict[str, sp.Expr]:
    n = norm(t)
    return {
        f"{prefix}_U": (n + alpha * t * (1 + t)) / n,
        f"{prefix}_V": (n + alpha * (1 + t)) / n,
        f"{prefix}_W": (n - alpha * t) / n,
    }


@dataclass(frozen=True)
class DegreeRow:
    name: str
    deg_a: int
    deg_b: int
    deg_z: int
    deg_y: int
    total_degree: int


def degree_row(name: str, expression: sp.Expr) -> DegreeRow:
    numerator, denominator = sp.together(expression).as_numer_denom()
    return DegreeRow(
        name=name,
        deg_a=max(sp.degree(numerator, A), sp.degree(denominator, A)),
        deg_b=max(sp.degree(numerator, B), sp.degree(denominator, B)),
        deg_z=max(sp.degree(numerator, Z), sp.degree(denominator, Z)),
        deg_y=max(sp.degree(numerator, Y), sp.degree(denominator, Y)),
        total_degree=max(
            sp.Poly(numerator, A, B, Z, Y).total_degree(),
            sp.Poly(denominator, A, B, Z, Y).total_degree(),
        ),
    )


def membership_degree_rows() -> tuple[DegreeRow, ...]:
    maps = {}
    maps.update(membership_maps(A, Z, "src"))
    maps.update(membership_maps(B, Y, "tgt"))
    return tuple(degree_row(name, expression) for name, expression in maps.items())


def slope_hit_factors() -> dict[str, sp.Expr]:
    n = norm(Z)
    m = norm(Y)
    source_inv_num = inv_num(A, Z)
    target_inv_num = inv_num(B, Y)
    delta = A - B
    rho_clear = (delta * n**3 + source_inv_num) * m**3 - target_inv_num * n**3
    source_slope_nums = {
        "Q0": n**2 - A**2 * Z**2 * (1 + Z) ** 2,
        "Q1": n**2 - A**2 * (1 + Z) ** 2,
        "Q2": n**2 - A**2 * Z**2,
    }
    return {
        name: sp.factor(rho_clear - slope_num * delta * n * m**3)
        for name, slope_num in source_slope_nums.items()
    }


def polynomial_degree_row(name: str, polynomial: sp.Expr) -> DegreeRow:
    return DegreeRow(
        name=name,
        deg_a=sp.degree(polynomial, A),
        deg_b=sp.degree(polynomial, B),
        deg_z=sp.degree(polynomial, Z),
        deg_y=sp.degree(polynomial, Y),
        total_degree=sp.Poly(polynomial, A, B, Z, Y).total_degree(),
    )


def main() -> None:
    print("h=3 repeat slope-miss degree compiler")
    rows = membership_degree_rows()
    sums = {
        "a": sum(row.deg_a for row in rows),
        "b": sum(row.deg_b for row in rows),
        "z": sum(row.deg_z for row in rows),
        "y": sum(row.deg_y for row in rows),
        "total": sum(row.total_degree for row in rows),
    }
    print(
        f"generic_membership: maps={len(rows)} S_a={sums['a']} S_b={sums['b']} "
        f"S_z={sums['z']} S_y={sums['y']} S_total={sums['total']}"
    )
    for row in rows:
        print(
            f"  {row.name}: deg_a={row.deg_a} deg_b={row.deg_b} "
            f"deg_z={row.deg_z} deg_y={row.deg_y} total={row.total_degree}"
        )
    factors = slope_hit_factors()
    factor_rows = tuple(polynomial_degree_row(name, polynomial) for name, polynomial in factors.items())
    product_bounds = {
        "a": sum(row.deg_a for row in factor_rows),
        "b": sum(row.deg_b for row in factor_rows),
        "z": sum(row.deg_z for row in factor_rows),
        "y": sum(row.deg_y for row in factor_rows),
        "total": sum(row.total_degree for row in factor_rows),
    }
    for row in factor_rows:
        print(
            f"  {row.name}: deg_a={row.deg_a} deg_b={row.deg_b} "
            f"deg_z={row.deg_z} deg_y={row.deg_y} total={row.total_degree}"
        )
    print(
        f"slope_miss_product_bound: deg_a<={product_bounds['a']} "
        f"deg_b<={product_bounds['b']} deg_z<={product_bounds['z']} "
        f"deg_y<={product_bounds['y']} total<={product_bounds['total']}"
    )
    if sums != {"a": 3, "b": 3, "z": 6, "y": 6, "total": 14}:
        raise AssertionError(sums)
    expected_factors = {
        "Q0": (3, 3, 6, 6, 15),
        "Q1": (3, 3, 6, 6, 13),
        "Q2": (3, 3, 6, 6, 13),
    }
    actual = {
        row.name: (row.deg_a, row.deg_b, row.deg_z, row.deg_y, row.total_degree)
        for row in factor_rows
    }
    if actual != expected_factors:
        raise AssertionError(actual)
    print("H3_REPEAT_SLOPE_MISS_DEGREE_COMPILER_PASS")


if __name__ == "__main__":
    main()
