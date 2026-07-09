#!/usr/bin/env python3
"""J-invariant compiler for generic h=3 same-lambda ratio orbits."""

from __future__ import annotations

import sympy as sp

from f3_h3_repeat_same_lambda_orbit_domain import (
    Y,
    Z,
    generic_off_orbit_product,
    poly_degrees,
)


A = sp.symbols("a")


def norm(t: sp.Expr) -> sp.Expr:
    return 1 + t + t**2


def j_invariant(t: sp.Expr) -> sp.Expr:
    return norm(t) ** 3 / (t**2 * (1 + t) ** 2)


def reciprocal_product_formula(alpha: sp.Expr, ratio: sp.Expr) -> sp.Expr:
    return -j_invariant(ratio) / alpha**3


def j_difference_numerator() -> sp.Expr:
    numerator, _ = sp.together(j_invariant(Z) - j_invariant(Y)).as_numer_denom()
    return sp.factor(numerator)


def verify_j_separates_orbits() -> tuple[int, int, int]:
    numerator = j_difference_numerator()
    off_orbit = generic_off_orbit_product()
    if sp.expand(numerator + off_orbit) != 0:
        raise AssertionError((sp.factor(numerator), sp.factor(off_orbit)))
    degrees = poly_degrees(numerator)
    if degrees != (6, 6, 10):
        raise AssertionError((degrees, numerator))
    return degrees


def verify_reciprocal_product_formula() -> tuple[int, int, int]:
    ratio = Z
    root = norm(ratio) / (A * ratio * (1 + ratio))
    product = -ratio * (1 + ratio) * root**3
    formula = reciprocal_product_formula(A, ratio)
    numerator, denominator = sp.together(product - formula).as_numer_denom()
    if sp.expand(numerator) != 0:
        raise AssertionError((sp.factor(product), sp.factor(formula), denominator))
    numerator, denominator = sp.together(formula).as_numer_denom()
    degrees = (
        max(sp.degree(numerator, A), sp.degree(denominator, A)),
        max(sp.degree(numerator, Z), sp.degree(denominator, Z)),
        max(
            sp.Poly(numerator, A, Z).total_degree(),
            sp.Poly(denominator, A, Z).total_degree(),
        ),
    )
    if degrees != (3, 6, 7):
        raise AssertionError((degrees, formula))
    return degrees


def main() -> None:
    print("h=3 repeat same-lambda J-invariant")
    product_degrees = verify_reciprocal_product_formula()
    j_degrees = verify_j_separates_orbits()
    print("generic reciprocal product:")
    print("  R(a,z) = -J(z)/a^3")
    print("  J(z) = (1+z+z^2)^3 / (z^2(1+z)^2)")
    print(
        "  R_formula_degrees: "
        f"deg_a={product_degrees[0]} deg_z={product_degrees[1]} total={product_degrees[2]}"
    )
    print("orbit separation:")
    print("  numerator(J(z)-J(y)) = - generic_off_orbit_product(z,y)")
    print(
        "  off_orbit_degrees: "
        f"deg_z={j_degrees[0]} deg_y={j_degrees[1]} total={j_degrees[2]}"
    )
    print("H3_REPEAT_SAME_LAMBDA_J_INVARIANT_PASS")


if __name__ == "__main__":
    main()
