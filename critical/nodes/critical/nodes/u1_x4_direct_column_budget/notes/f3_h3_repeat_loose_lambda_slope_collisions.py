#!/usr/bin/env python3
"""Lambda-slope collision table for normalized h=3 loose systems."""

from __future__ import annotations

from itertools import combinations, product

import sympy as sp

from f3_h3_repeat_loose_affine_slope_compiler import coordinate_slopes, lambda_slopes
from f3_h3_repeat_loose_normalized_system import normalized_reciprocal_multipliers


A, B = sp.symbols("a b")

COORDINATE_EXPRESSIONS = {
    "1": sp.Integer(1),
    "1/a": 1 / A,
    "1/b": 1 / B,
    "-1/(1+a)": -1 / (1 + A),
    "-1/(1+b)": -1 / (1 + B),
    "-1/(a+b)": -1 / (A + B),
}

LAMBDA_EXPRESSIONS = {
    "L_a": 1 + 1 / A - 1 / (1 + A),
    "L_b": 1 + 1 / B - 1 / (1 + B),
    "L_ab": 1 / A + 1 / B - 1 / (A + B),
}

EXPECTED_LAMBDA_COORDINATE = {
    ("L_a", "1"): sp.Integer(1),
    ("L_a", "1/a"): A,
    ("L_a", "1/b"): A**2 * B - A**2 + A * B - A + B,
    ("L_a", "-1/(1+a)"): A + 1,
    ("L_a", "-1/(1+b)"): A**2 * B + 2 * A**2 + A * B + 2 * A + B + 1,
    ("L_a", "-1/(a+b)"): A**3 + A**2 * B + 2 * A**2 + A * B + 2 * A + B,
    ("L_b", "1"): sp.Integer(1),
    ("L_b", "1/a"): A * B**2 + A * B + A - B**2 - B,
    ("L_b", "1/b"): B,
    ("L_b", "-1/(1+a)"): A * B**2 + A * B + A + 2 * B**2 + 2 * B + 1,
    ("L_b", "-1/(1+b)"): B + 1,
    ("L_b", "-1/(a+b)"): A * B**2 + A * B + A + B**3 + 2 * B**2 + 2 * B,
    ("L_ab", "1"): -A**2 * B + A**2 - A * B**2 + A * B + B**2,
    ("L_ab", "1/a"): A,
    ("L_ab", "1/b"): B,
    ("L_ab", "-1/(1+a)"): A**3 + 2 * A**2 * B + A**2 + 2 * A * B**2 + A * B + B**2,
    ("L_ab", "-1/(1+b)"): 2 * A**2 * B + A**2 + 2 * A * B**2 + A * B + B**3 + B**2,
    ("L_ab", "-1/(a+b)"): A + B,
}

EXPECTED_LAMBDA_LAMBDA = {
    ("L_a", "L_b"): -(A - B) * (A + B + 1),
    ("L_a", "L_ab"): A * (B - 1) * (A + B + 1),
    ("L_b", "L_ab"): B * (A - 1) * (A + B + 1),
}

NONTRIVIAL_LAMBDA_COORDINATE = {
    ("L_a", "1/b"),
    ("L_a", "-1/(1+b)"),
    ("L_a", "-1/(a+b)"),
    ("L_b", "1/a"),
    ("L_b", "-1/(1+a)"),
    ("L_b", "-1/(a+b)"),
    ("L_ab", "1"),
    ("L_ab", "-1/(1+a)"),
    ("L_ab", "-1/(1+b)"),
}


def numerator(lhs: sp.Expr, rhs: sp.Expr) -> sp.Expr:
    num, _ = sp.together(lhs - rhs).as_numer_denom()
    return sp.factor(num)


def check_symbolic_tables() -> None:
    for key, expected in EXPECTED_LAMBDA_COORDINATE.items():
        lambda_name, coordinate_name = key
        actual = numerator(LAMBDA_EXPRESSIONS[lambda_name], COORDINATE_EXPRESSIONS[coordinate_name])
        if sp.factor(actual - expected) != 0:
            raise AssertionError((key, actual, expected))
    for key, expected in EXPECTED_LAMBDA_LAMBDA.items():
        left, right = key
        actual = numerator(LAMBDA_EXPRESSIONS[left], LAMBDA_EXPRESSIONS[right])
        if sp.factor(actual - expected) != 0:
            raise AssertionError((key, actual, expected))


def eval_poly(poly: sp.Expr, a_value: int, b_value: int, p: int) -> int:
    return int(poly.subs({A: a_value, B: b_value})) % p


def check_finite_fields() -> None:
    lambda_order = tuple(LAMBDA_EXPRESSIONS)
    coordinate_order = tuple(COORDINATE_EXPRESSIONS)
    for p in (5, 7, 11, 13, 17, 97):
        for a_value, b_value in product(range(p), repeat=2):
            q_values = normalized_reciprocal_multipliers(a_value, b_value, p)
            if not all(q_values):
                continue
            if len(set(q_values)) != 6:
                continue
            if (1 + a_value + b_value) % p == 0:
                continue
            c_values = coordinate_slopes(a_value, b_value, p)
            l_values = lambda_slopes(a_value, b_value, p)
            if len(set(l_values)) != 3:
                raise AssertionError((p, a_value, b_value, "lambda-lambda collision", l_values))
            for i, lambda_name in enumerate(lambda_order):
                for j, coordinate_name in enumerate(coordinate_order):
                    key = (lambda_name, coordinate_name)
                    collision = l_values[i] == c_values[j]
                    polynomial_zero = eval_poly(EXPECTED_LAMBDA_COORDINATE[key], a_value, b_value, p) == 0
                    if collision != polynomial_zero:
                        raise AssertionError((p, a_value, b_value, key, l_values[i], c_values[j]))


def main() -> None:
    print("h=3 repeat loose lambda-slope collision table")
    print("lambda slopes:")
    for name, expression in LAMBDA_EXPRESSIONS.items():
        print(f"{name} = {sp.factor(expression)}")
    check_symbolic_tables()
    print("symbolic lambda-coordinate and lambda-lambda tables verified")
    print("nontrivial lambda-coordinate collision divisors:")
    for key in sorted(NONTRIVIAL_LAMBDA_COORDINATE):
        print(f"{key[0]} = {key[1]} iff {sp.factor(EXPECTED_LAMBDA_COORDINATE[key])} = 0")
    print("lambda-lambda collisions factor through excluded loose-system conditions:")
    for key, expression in EXPECTED_LAMBDA_LAMBDA.items():
        print(f"{key[0]} = {key[1]} iff {sp.factor(expression)} = 0")
    check_finite_fields()
    print("finite collision guardrails verified over p=5,7,11,13,17,97")
    print("H3_REPEAT_LOOSE_LAMBDA_SLOPE_COLLISIONS_PASS")


if __name__ == "__main__":
    main()
