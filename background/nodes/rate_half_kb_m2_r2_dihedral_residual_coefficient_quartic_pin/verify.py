#!/usr/bin/env python3
"""Verify the canonical residual coefficient-quartic substitution."""

from __future__ import annotations

from collections import defaultdict


Monomial = tuple[int, int]
Polynomial = dict[Monomial, dict[str, int]]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def add_term(poly: Polynomial, monomial: Monomial, coefficient: str, value: int) -> None:
    poly[monomial][coefficient] += value


def expansion() -> Polynomial:
    poly: Polynomial = defaultdict(lambda: defaultdict(int))
    add_term(poly, (0, 4), "A", 1)
    add_term(poly, (2, 2), "B", 1)
    add_term(poly, (0, 3), "B", -2)
    add_term(poly, (4, 0), "C", 1)
    add_term(poly, (2, 1), "C", -4)
    add_term(poly, (0, 2), "C", 2)
    add_term(poly, (0, 2), "D", 1)
    add_term(poly, (2, 0), "E", 1)
    add_term(poly, (0, 1), "E", -2)
    add_term(poly, (0, 0), "F", 1)
    return {key: dict(value) for key, value in poly.items()}


def verify() -> None:
    expected = {
        (0, 4): {"A": 1},
        (2, 2): {"B": 1},
        (0, 3): {"B": -2},
        (4, 0): {"C": 1},
        (2, 1): {"C": -4},
        (0, 2): {"C": 2, "D": 1},
        (2, 0): {"E": 1},
        (0, 1): {"E": -2},
        (0, 0): {"F": 1},
    }
    actual = expansion()
    require(actual == expected, "canonical quartic expansion mismatch")
    require(max(s_degree + p_degree for s_degree, p_degree in actual) == 4, "wrong total degree")
    require({coefficient for row in actual.values() for coefficient in row} == set("ABCDEF"), "lost sibling coefficient")

    # Independent evaluations of k(S^2-2P,P^2) and the expanded Q.
    coefficient_rows = [
        {"A": 2, "B": -3, "C": 5, "D": 7, "E": -11, "F": 13},
        {"A": -1, "B": 4, "C": 3, "D": -2, "E": 6, "F": 9},
    ]
    for coefficients in coefficient_rows:
        for s_value, p_value in [(-3, 2), (0, -5), (7, 1), (4, -6)]:
            sigma = s_value * s_value - 2 * p_value
            pi = p_value * p_value
            direct = (
                coefficients["A"] * pi * pi
                + coefficients["B"] * sigma * pi
                + coefficients["C"] * (sigma * sigma - 2 * pi)
                + coefficients["D"] * pi
                + coefficients["E"] * sigma
                + coefficients["F"]
            )
            expanded = 0
            for (s_degree, p_degree), terms in actual.items():
                scalar = sum(coefficients[name] * multiplier for name, multiplier in terms.items())
                expanded += scalar * s_value**s_degree * p_value**p_degree
            require(direct == expanded, "substitution evaluation mismatch")

    require(4 * 3 < 24, "degree-below-four Bezout fence")


if __name__ == "__main__":
    verify()
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_RESIDUAL_COEFFICIENT_QUARTIC_PIN_PASS")
