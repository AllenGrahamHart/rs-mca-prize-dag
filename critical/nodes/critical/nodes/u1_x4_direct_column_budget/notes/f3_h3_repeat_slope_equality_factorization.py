#!/usr/bin/env python3
"""Equality-factorization compiler for h=3 repeat slope-hit numerators."""

from __future__ import annotations

import sympy as sp

from f3_h3_repeat_slope_miss_degree_compiler import (
    A,
    B,
    Y,
    Z,
    inv_num,
    norm,
    slope_hit_factors,
)
from f3_h3_repeat_slope_mixed_degree_compiler import (
    X,
    generic_source_scale_target_factors,
    scale_source_generic_target_factors,
)


C = sp.symbols("c")


def generic_increments(alpha: sp.Expr, t: sp.Expr) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    return (
        alpha * t * (1 + t),
        alpha * (1 + t),
        -alpha * t,
    )


def generic_equality_products() -> dict[str, sp.Expr]:
    n = norm(Z)
    m = norm(Y)
    source_increments = generic_increments(A, Z)
    target_increments = generic_increments(B, Y)
    return {
        f"Q{index}": sp.factor(
            sp.prod(source * m - target * n for target in target_increments)
        )
        for index, source in enumerate(source_increments)
    }


def mixed_equality_products() -> dict[str, sp.Expr]:
    n = norm(Z)
    source_increments = generic_increments(A, Z)
    return {
        f"Q{index}": sp.factor(source**3 - X**3 * n**3)
        for index, source in enumerate(source_increments)
    }


def scale_source_equality_product() -> sp.Expr:
    m = norm(Y)
    target_increments = generic_increments(B, Y)
    return sp.factor(sp.prod(C * X * m - target for target in target_increments))


def scale_source_model_factor() -> sp.Expr:
    m = norm(Y)
    # If the scale coordinate is 1+c*x and c^3=1, the matching hit factor is
    # labelled by c^2.  The square map permutes the primitive-cube labels.
    return sp.factor((X**3 - C**2 * B * X**2) * m**3 - inv_num(B, Y))


def total_degrees(rows: dict[str, sp.Expr], variables: tuple[sp.Symbol, ...]) -> dict[str, int]:
    return {name: sp.Poly(poly, *variables).total_degree() for name, poly in rows.items()}


def verify_generic_factorization() -> dict[str, int]:
    slope = slope_hit_factors()
    equality = generic_equality_products()
    signs: dict[str, int] = {}
    for name, slope_poly in slope.items():
        equality_poly = equality[name]
        if sp.expand(slope_poly - equality_poly) == 0:
            signs[name] = 1
        elif sp.expand(slope_poly + equality_poly) == 0:
            signs[name] = -1
        else:
            raise AssertionError((name, sp.factor(slope_poly), sp.factor(equality_poly)))
    degrees = total_degrees(equality, (A, B, Z, Y))
    if degrees != {"Q0": 15, "Q1": 13, "Q2": 13}:
        raise AssertionError(degrees)
    return degrees


def verify_mixed_factorization() -> dict[str, int]:
    slope = generic_source_scale_target_factors()
    equality = mixed_equality_products()
    signs: dict[str, int] = {}
    for name, slope_poly in slope.items():
        equality_poly = equality[name]
        if sp.expand(slope_poly - equality_poly) == 0:
            signs[name] = 1
        elif sp.expand(slope_poly + equality_poly) == 0:
            signs[name] = -1
        else:
            raise AssertionError((name, sp.factor(slope_poly), sp.factor(equality_poly)))
    degrees = total_degrees(equality, (A, Z, X))
    if degrees != {"Q0": 9, "Q1": 9, "Q2": 9}:
        raise AssertionError(degrees)
    return degrees


def verify_scale_source_mixed_factorization() -> dict[str, int]:
    product = scale_source_equality_product()
    model = scale_source_model_factor()
    remainder = sp.rem(sp.expand(product - model), C**3 - 1, C)
    if sp.expand(remainder) != 0:
        raise AssertionError((sp.factor(product), sp.factor(model), sp.factor(remainder)))
    degrees = total_degrees(scale_source_generic_target_factors(), (X, B, Y))
    if degrees != {"Q0": 9, "Q1": 9, "Q2": 9}:
        raise AssertionError(degrees)
    return degrees


def main() -> None:
    print("h=3 repeat slope equality factorization")
    generic_degrees = verify_generic_factorization()
    mixed_degrees = verify_mixed_factorization()
    reverse_mixed_degrees = verify_scale_source_mixed_factorization()
    print("generic-generic:")
    print("  Q_i = product_j (source_increment_i*M - target_increment_j*N)")
    for name in ("Q0", "Q1", "Q2"):
        print(f"  {name}: equality_product_total_degree={generic_degrees[name]}")
    print("mixed generic/scale:")
    print("  Q_i = source_increment_i^3 - x^3*N^3")
    for name in ("Q0", "Q1", "Q2"):
        print(f"  {name}: equality_product_total_degree={mixed_degrees[name]}")
    print("mixed scale/generic:")
    print("  for c^3=1, Q_{c^2} = product_j (c*x*M - target_increment_j)")
    for name in ("Q0", "Q1", "Q2"):
        print(f"  {name}: equality_product_total_degree={reverse_mixed_degrees[name]}")
    print("slope-hit numerators vanish exactly when source and target share a coordinate")
    print("H3_REPEAT_SLOPE_EQUALITY_FACTORIZATION_PASS")


if __name__ == "__main__":
    main()
