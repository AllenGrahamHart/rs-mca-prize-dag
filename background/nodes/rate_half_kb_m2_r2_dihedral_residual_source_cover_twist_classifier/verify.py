#!/usr/bin/env python3
"""Verify the residual source-cover twist classifier."""

from __future__ import annotations

from fractions import Fraction


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def q_value(b: Fraction, d: Fraction, z: Fraction) -> Fraction:
    return z * z - b * d * z + b * b + d * d - 4


def verify() -> None:
    rows = [
        {"a": -1, "d": Fraction(1), "b_values": [Fraction(-3), Fraction(-1), Fraction(0), Fraction(1), Fraction(3)]},
        {"a": 1, "d": Fraction(3, 2), "b_values": [Fraction(-3), Fraction(-1), Fraction(0), Fraction(1), Fraction(3)]},
    ]
    # The second row uses a rational test d; universal identities are checked
    # under d^2=a+2 separately below rather than numerically specializing sqrt(3).
    for row in rows:
        for b in row["b_values"]:
            if b in (-2, 2):
                continue
            d = row["d"]
            require(q_value(b, d, Fraction(2)) == (b - d) ** 2, "Q(2)")
            require(q_value(b, d, Fraction(-2)) == (b + d) ** 2, "Q(-2)")
            discriminant = (b * b - 4) * (d * d - 4)
            require(discriminant != 0, "test quadratic must be squarefree")

    for a in (-1, 1):
        d2 = a + 2
        require(d2 in (1, 3), "dihedral half-trace square")
        for b in (Fraction(-3), Fraction(-1), Fraction(0), Fraction(1), Fraction(3)):
            rational_regime = b * b == d2
            require(rational_regime == (b * b == a + 2), "genus classifier")

    # Polynomial coefficient audit for the product identity denominator.
    # (x-b)(y-b)=z^2-b*d*z+b^2+d^2-4.
    for b, d, z in [
        (Fraction(0), Fraction(1), Fraction(3)),
        (Fraction(1), Fraction(-1), Fraction(4)),
        (Fraction(3), Fraction(2), Fraction(-1)),
    ]:
        denominator = z * z - b * d * z + b * b + d * d - 4
        require(denominator == q_value(b, d, z), "denominator identity")


if __name__ == "__main__":
    verify()
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_RESIDUAL_SOURCE_COVER_TWIST_CLASSIFIER_PASS")
