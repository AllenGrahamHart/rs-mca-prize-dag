#!/usr/bin/env python3
"""Coordinate-slope distinctness for normalized h=3 loose systems."""

from __future__ import annotations

from itertools import combinations, product

from f3_h3_repeat_loose_affine_slope_compiler import coordinate_slopes
from f3_h3_repeat_loose_normalized_system import normalized_reciprocal_multipliers


AFFINE_FORMS = {
    "1": (1, 0, 0),
    "a": (0, 1, 0),
    "b": (0, 0, 1),
    "-(1+a)": (-1, -1, 0),
    "-(1+b)": (-1, 0, -1),
    "-(a+b)": (0, -1, -1),
}

EXPECTED_COLLISIONS = {
    ("1", "a"): (1, -1, 0),
    ("1", "b"): (1, 0, -1),
    ("1", "-(1+a)"): (2, 1, 0),
    ("1", "-(1+b)"): (2, 0, 1),
    ("1", "-(a+b)"): (1, 1, 1),
    ("a", "b"): (0, 1, -1),
    ("a", "-(1+a)"): (1, 2, 0),
    ("a", "-(1+b)"): (1, 1, 1),
    ("a", "-(a+b)"): (0, 2, 1),
    ("b", "-(1+a)"): (1, 1, 1),
    ("b", "-(1+b)"): (1, 0, 2),
    ("b", "-(a+b)"): (0, 1, 2),
    ("-(1+a)", "-(1+b)"): (0, -1, 1),
    ("-(1+a)", "-(a+b)"): (-1, 0, 1),
    ("-(1+b)", "-(a+b)"): (-1, 1, 0),
}


def subtract_forms(lhs: tuple[int, int, int], rhs: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(x - y for x, y in zip(lhs, rhs))


def eval_form(form: tuple[int, int, int], a: int, b: int, p: int) -> int:
    const, a_coeff, b_coeff = form
    return (const + a_coeff * a + b_coeff * b) % p


def check_symbolic_table() -> None:
    for left, right in combinations(AFFINE_FORMS, 2):
        actual = subtract_forms(AFFINE_FORMS[left], AFFINE_FORMS[right])
        expected = EXPECTED_COLLISIONS[(left, right)]
        if actual != expected:
            raise AssertionError((left, right, actual, expected))


def check_finite_fields() -> None:
    for p in (5, 7, 11, 13, 17, 97):
        for a, b in product(range(p), repeat=2):
            q_values = normalized_reciprocal_multipliers(a, b, p)
            table_distinct = True
            for left, right in combinations(AFFINE_FORMS, 2):
                if eval_form(EXPECTED_COLLISIONS[(left, right)], a, b, p) == 0:
                    table_distinct = False
            if table_distinct != (len(set(q_values)) == 6):
                raise AssertionError((p, a, b, q_values, table_distinct))
            if all(q % p for q in q_values):
                slopes = coordinate_slopes(a, b, p)
                if (len(set(slopes)) == 6) != (len(set(q_values)) == 6):
                    raise AssertionError((p, a, b, q_values, slopes))


def main() -> None:
    print("h=3 repeat loose coordinate-slope distinctness")
    print("coordinate slopes are inverses of the six reciprocal multipliers")
    check_symbolic_table()
    print("symbolic collision table verified")
    for (left, right), form in EXPECTED_COLLISIONS.items():
        print(f"{left} = {right} iff {form[0]} + {form[1]}*a + {form[2]}*b = 0")
    check_finite_fields()
    print("finite inversion guardrails verified over p=5,7,11,13,17,97")
    print("H3_REPEAT_LOOSE_COORDINATE_SLOPE_DISTINCTNESS_PASS")


if __name__ == "__main__":
    main()
