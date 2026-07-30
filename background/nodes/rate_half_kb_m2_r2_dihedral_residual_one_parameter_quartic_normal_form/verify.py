#!/usr/bin/env python3
"""Verify the residual one-parameter coefficient-quartic normal form."""

from __future__ import annotations

from fractions import Fraction


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def coefficients(a: int, b: Fraction) -> dict[str, Fraction]:
    return {
        "A": (a - 2) * (a - b * b + 2),
        "B": -(a - 2) * (2 * a - b * b - 2 * b + 4),
        "C": (a - b) ** 2,
        "D": 4 * a * a - a * b * b - 4 * a * b - 4 * a + 16 * b - 16,
        "E": -2 * (a - 2) * (a - b),
        "F": (a - 2) ** 2,
    }


def old_coordinate(new: Fraction, b: Fraction) -> Fraction:
    return (b * new - 2) / (new - 1)


def sibling_old(a: int, x: Fraction, y: Fraction) -> Fraction:
    return x * x + y * y - a * x * y + a * a - 4


def sibling_new(row: dict[str, Fraction], x: Fraction, y: Fraction) -> Fraction:
    sigma = x + y
    pi = x * y
    return (
        row["A"] * pi * pi
        + row["B"] * sigma * pi
        + row["C"] * (sigma * sigma - 2 * pi)
        + row["D"] * pi
        + row["E"] * sigma
        + row["F"]
    )


def quartic(row: dict[str, Fraction], s_value: Fraction, p_value: Fraction) -> Fraction:
    return (
        row["A"] * p_value**4
        + row["B"] * s_value**2 * p_value**2
        - 2 * row["B"] * p_value**3
        + row["C"] * s_value**4
        - 4 * row["C"] * s_value**2 * p_value
        + (2 * row["C"] + row["D"]) * p_value**2
        + row["E"] * s_value**2
        - 2 * row["E"] * p_value
        + row["F"]
    )


def verify() -> None:
    require({-1, 1} == {2 * (-1) + 1, 2 * 0 + 1}, "a-value replay")
    for a in (-1, 1):
        for b in (Fraction(-3), Fraction(-1), Fraction(0), Fraction(1), Fraction(3)):
            require(b not in (2, -2), "bad test parameter")
            row = coefficients(a, b)
            require(set(row) == set("ABCDEF"), "coefficient key loss")
            for x, y in [
                (Fraction(0), Fraction(3)),
                (Fraction(-2), Fraction(4)),
                (Fraction(5), Fraction(-3)),
            ]:
                require(x != 1 and y != 1, "test hits target pole")
                cleared_old = (x - 1) ** 2 * (y - 1) ** 2 * sibling_old(
                    a,
                    old_coordinate(x, b),
                    old_coordinate(y, b),
                )
                require(cleared_old == sibling_new(row, x, y), "sibling transform mismatch")

            for t, u in [(Fraction(2), Fraction(3)), (Fraction(-1), Fraction(4))]:
                s_value = t + u
                p_value = t * u
                require(
                    quartic(row, s_value, p_value) == sibling_new(row, t * t, u * u),
                    "canonical quartic substitution mismatch",
                )

            alpha = row["B"] ** 2 - 4 * row["A"] * row["C"]
            beta = 8 * row["C"] ** 2 + 2 * row["B"] * row["E"] - 4 * row["C"] * row["D"]
            gamma = row["E"] ** 2 - 4 * row["C"] * row["F"]
            require(alpha == (a - 2) * (a + 2) * (b - 2) ** 3 * (b + 2), "alpha invariant")
            require(beta == -4 * (a + 2) * (a - b) * (b - 2) ** 3, "beta invariant")
            require(gamma == 0, "aligned-branch discriminant")


if __name__ == "__main__":
    verify()
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_RESIDUAL_ONE_PARAMETER_QUARTIC_NORMAL_FORM_PASS")
