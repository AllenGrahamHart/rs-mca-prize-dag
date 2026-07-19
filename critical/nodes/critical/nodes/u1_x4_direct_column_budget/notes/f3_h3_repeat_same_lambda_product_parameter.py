#!/usr/bin/env python3
"""Product-parameter compiler for generic h=3 same-lambda edges."""

from __future__ import annotations

from itertools import permutations

import sympy as sp

from f3_h3_repeat_edge_cubic_gcd_form import edge_cubic_data
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_reciprocal_product_compiler import reciprocal_edge
from f3_h3_repeat_same_lambda_j_invariant import j_invariant, norm
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS


A, Z, T = sp.symbols("a z T")


def generic_coordinate_maps() -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    n = norm(Z)
    return (
        (n + A * Z * (1 + Z)) / n,
        (n + A * (1 + Z)) / n,
        (n - A * Z) / n,
    )


def product_parameter() -> sp.Expr:
    u, v, w = generic_coordinate_maps()
    return sp.factor(u * v * w)


def cubic_polynomial() -> sp.Expr:
    product = product_parameter()
    return sp.factor(T**3 - (A + 3) * T**2 + (2 * A + 3) * T - product)


def derivative_factorization() -> tuple[sp.Expr, sp.Expr]:
    numerator, denominator = sp.together(sp.diff(product_parameter(), Z)).as_numer_denom()
    return sp.factor(numerator), sp.factor(denominator)


def symbolic_summary() -> dict[str, int]:
    u, v, w = generic_coordinate_maps()
    if sp.factor(u + v + w - (A + 3)) != 0:
        raise AssertionError(sp.factor(u + v + w))
    if sp.factor(u * v + u * w + v * w - (2 * A + 3)) != 0:
        raise AssertionError(sp.factor(u * v + u * w + v * w))

    product = product_parameter()
    product_from_j = A + 1 - A**3 / j_invariant(Z)
    if sp.factor(sp.together(product - product_from_j)) != 0:
        raise AssertionError((sp.factor(product), sp.factor(product_from_j)))

    cubic = cubic_polynomial()
    for coordinate in (u, v, w):
        if sp.factor(sp.together(cubic.subs(T, coordinate))) != 0:
            raise AssertionError((coordinate, sp.factor(cubic.subs(T, coordinate))))

    numerator, denominator = derivative_factorization()
    expected_num = A**3 * Z * (Z - 1) * (Z + 1) * (Z + 2) * (2 * Z + 1)
    expected_den = norm(Z) ** 4
    if sp.expand(numerator - expected_num) != 0:
        raise AssertionError((sp.factor(numerator), expected_num))
    if sp.expand(denominator - expected_den) != 0:
        raise AssertionError((sp.factor(denominator), expected_den))

    return {
        "sum_constant": 3,
        "sum_a_coeff": 1,
        "pair_constant": 3,
        "pair_a_coeff": 2,
        "derivative_num_degree_z": sp.degree(numerator, Z),
        "derivative_den_degree_z": sp.degree(denominator, Z),
        "active_critical_points": 0,
    }


def product_value_mod(lam: int, z: int, p: int) -> int:
    a = (lam - 1) % p
    n = (1 + z + z * z) % p
    if n == 0:
        raise AssertionError((p, lam, z, "generic denominator"))
    return (lam - pow(a, 3, p) * pow(z, 2, p) * pow((1 + z) % p, 2, p) * pow(pow(n, 3, p), -1, p)) % p


def finite_guardrails() -> dict[str, int]:
    generic_checks = 0
    lambda_one_skips = 0
    rows = 0
    for p, n in (*WITNESS_ROWS, *CONTRAST_ROWS):
        rows += 1
        for edge, (lam, coord_product) in edge_cubic_data(p, n).items():
            rec_edge = reciprocal_edge(edge, p)
            if lam == 1:
                lambda_one_skips += len(tuple(permutations(rec_edge, 2)))
                continue
            for r, s in permutations(rec_edge, 2):
                z = s * pow(r, -1, p) % p
                if product_value_mod(lam, z, p) != coord_product:
                    raise AssertionError((p, n, edge, lam, coord_product, r, s, z))
                generic_checks += 1
    return {
        "rows": rows,
        "generic_checks": generic_checks,
        "lambda_one_skips": lambda_one_skips,
    }


def product_parameter_summary() -> dict[str, int]:
    symbolic = symbolic_summary()
    finite = finite_guardrails()
    if finite != {"rows": 7, "generic_checks": 174, "lambda_one_skips": 6}:
        raise AssertionError(finite)
    return {**symbolic, **finite}


def main() -> None:
    summary = product_parameter_summary()
    print("h=3 repeat same-lambda product parameter")
    print("generic edge coordinates have e1=a+3 and e2=2a+3")
    print("product m(z)=a+1-a^3/J(z), with J the complete S3 quotient invariant")
    numerator, denominator = derivative_factorization()
    print(f"m'(z) numerator = {numerator}")
    print(f"m'(z) denominator = {denominator}")
    print(
        "summary: "
        f"derivative_num_degree_z={summary['derivative_num_degree_z']} "
        f"derivative_den_degree_z={summary['derivative_den_degree_z']} "
        f"active_critical_points={summary['active_critical_points']} "
        f"finite_generic_checks={summary['generic_checks']} "
        f"lambda_one_skips={summary['lambda_one_skips']}"
    )
    print("H3_REPEAT_SAME_LAMBDA_PRODUCT_PARAMETER_PASS")


if __name__ == "__main__":
    main()
