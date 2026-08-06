#!/usr/bin/env python3
"""Degree compiler for h=3 slope-hit mixed generic/scale branches."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp


A, Z, X = sp.symbols("a z x")
B, Y = sp.symbols("b y")
C0, C1, C2 = sp.symbols("c0 c1 c2")


@dataclass(frozen=True)
class DegreeRow:
    name: str
    variable_degrees: tuple[int, ...]
    total_degree: int


def norm(t: sp.Expr) -> sp.Expr:
    return 1 + t + t**2


def inv_num(alpha: sp.Expr, t: sp.Expr) -> sp.Expr:
    return -alpha**3 * t**2 * (1 + t) ** 2


def generic_membership_maps(alpha: sp.Expr, t: sp.Expr, prefix: str) -> dict[str, sp.Expr]:
    n = norm(t)
    return {
        f"{prefix}_U": (n + alpha * t * (1 + t)) / n,
        f"{prefix}_V": (n + alpha * (1 + t)) / n,
        f"{prefix}_W": (n - alpha * t) / n,
    }


def scale_membership_maps(scale: sp.Expr, prefix: str) -> dict[str, sp.Expr]:
    # The primitive-cube coefficients are constants over the coefficient field.
    return {
        f"{prefix}_0": 1 + scale,
        f"{prefix}_1": 1 + C1 * scale,
        f"{prefix}_2": 1 + C2 * scale,
    }


def degree_row(name: str, expression: sp.Expr, variables: tuple[sp.Symbol, ...]) -> DegreeRow:
    numerator, denominator = sp.together(expression).as_numer_denom()
    variable_degrees = tuple(
        max(sp.degree(numerator, variable), sp.degree(denominator, variable))
        for variable in variables
    )
    total_degree = max(
        sp.Poly(numerator, *variables).total_degree(),
        sp.Poly(denominator, *variables).total_degree(),
    )
    return DegreeRow(name, variable_degrees, total_degree)


def sum_rows(rows: tuple[DegreeRow, ...]) -> tuple[int, ...]:
    if not rows:
        return ()
    return tuple(sum(row.variable_degrees[index] for row in rows) for index in range(len(rows[0].variable_degrees))) + (
        sum(row.total_degree for row in rows),
    )


def generic_source_scale_target_membership_rows() -> tuple[DegreeRow, ...]:
    variables = (A, Z, X)
    maps = {}
    maps.update(generic_membership_maps(A, Z, "src"))
    maps.update(scale_membership_maps(X, "tgt"))
    return tuple(degree_row(name, expression, variables) for name, expression in maps.items())


def scale_source_generic_target_membership_rows() -> tuple[DegreeRow, ...]:
    variables = (X, B, Y)
    maps = {}
    maps.update(scale_membership_maps(X, "src"))
    maps.update(generic_membership_maps(B, Y, "tgt"))
    return tuple(degree_row(name, expression, variables) for name, expression in maps.items())


def generic_source_slope_nums(alpha: sp.Expr, t: sp.Expr) -> dict[str, sp.Expr]:
    n = norm(t)
    return {
        "Q0": n**2 - alpha**2 * t**2 * (1 + t) ** 2,
        "Q1": n**2 - alpha**2 * (1 + t) ** 2,
        "Q2": n**2 - alpha**2 * t**2,
    }


def generic_source_scale_target_factors() -> dict[str, sp.Expr]:
    n = norm(Z)
    delta = A
    rho_num = delta * n**3 + inv_num(A, Z) - X**3 * n**3
    return {
        name: sp.factor(rho_num - slope_num * delta * n)
        for name, slope_num in generic_source_slope_nums(A, Z).items()
    }


def scale_source_generic_target_factors() -> dict[str, sp.Expr]:
    m = norm(Y)
    target_num = inv_num(B, Y)
    return {
        f"Q{index}": sp.factor((X**3 - coeff * B * X**2) * m**3 - target_num)
        for index, coeff in enumerate((C0, C1, C2))
    }


def polynomial_degree_rows(
    factors: dict[str, sp.Expr], variables: tuple[sp.Symbol, ...]
) -> tuple[DegreeRow, ...]:
    return tuple(
        DegreeRow(
            name=name,
            variable_degrees=tuple(sp.degree(polynomial, variable) for variable in variables),
            total_degree=sp.Poly(polynomial, *variables).total_degree(),
        )
        for name, polynomial in factors.items()
    )


def print_rows(label: str, variable_names: tuple[str, ...], rows: tuple[DegreeRow, ...]) -> tuple[int, ...]:
    sums = sum_rows(rows)
    degree_bits = " ".join(f"S_{name}={value}" for name, value in zip(variable_names, sums[:-1]))
    print(f"{label}: rows={len(rows)} {degree_bits} S_total={sums[-1]}")
    for row in rows:
        row_bits = " ".join(
            f"deg_{name}={value}" for name, value in zip(variable_names, row.variable_degrees)
        )
        print(f"  {row.name}: {row_bits} total={row.total_degree}")
    return sums


def main() -> None:
    print("h=3 repeat slope mixed degree compiler")

    gs_membership = generic_source_scale_target_membership_rows()
    gs_sums = print_rows(
        "generic_source_scale_target_membership",
        ("a", "z", "x"),
        gs_membership,
    )
    gs_factor_rows = polynomial_degree_rows(generic_source_scale_target_factors(), (A, Z, X))
    gs_factor_sums = print_rows(
        "generic_source_scale_target_hit_factors",
        ("a", "z", "x"),
        gs_factor_rows,
    )

    sg_membership = scale_source_generic_target_membership_rows()
    sg_sums = print_rows(
        "scale_source_generic_target_membership",
        ("x", "b", "y"),
        sg_membership,
    )
    sg_factor_rows = polynomial_degree_rows(scale_source_generic_target_factors(), (X, B, Y))
    sg_factor_sums = print_rows(
        "scale_source_generic_target_hit_factors",
        ("x", "b", "y"),
        sg_factor_rows,
    )

    if gs_sums != (3, 6, 3, 10):
        raise AssertionError(("generic-source scale-target membership", gs_sums))
    if sg_sums != (3, 3, 6, 10):
        raise AssertionError(("scale-source generic-target membership", sg_sums))
    if {row.variable_degrees + (row.total_degree,) for row in gs_factor_rows} != {(3, 6, 3, 9)}:
        raise AssertionError(gs_factor_rows)
    if {row.variable_degrees + (row.total_degree,) for row in sg_factor_rows} != {(3, 3, 6, 9)}:
        raise AssertionError(sg_factor_rows)
    if gs_factor_sums != (9, 18, 9, 27):
        raise AssertionError(("generic-source scale-target factors", gs_factor_sums))
    if sg_factor_sums != (9, 9, 18, 27):
        raise AssertionError(("scale-source generic-target factors", sg_factor_sums))

    print("mixed_slope_miss_product_bound: membership S_total=10, hit-product total<=27")
    print("H3_REPEAT_SLOPE_MIXED_DEGREE_COMPILER_PASS")


if __name__ == "__main__":
    main()
