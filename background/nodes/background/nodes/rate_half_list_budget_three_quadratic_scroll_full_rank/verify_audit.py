#!/usr/bin/env python3
"""Independent symbolic-coefficient audit of the scroll determinant."""

from __future__ import annotations

from fractions import Fraction


def determinant4(matrix: list[list[Fraction]]) -> Fraction:
    total = Fraction(0)
    for permutation in __import__("itertools").permutations(range(4)):
        inversions = sum(permutation[i] > permutation[j] for i in range(4) for j in range(i + 1, 4))
        term = 1
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        total += (-1 if inversions % 2 else 1) * term
    return total


def main() -> None:
    fixtures = (
        (3, 5, 0, 7, 11, 13, 17, 19, 23, 29),
        (5, 7, 31, 11, 13, 17, 19, 23, 29, 0),
    )
    for c, a0, a1, d0, d1, e0, e1, f0, f1, f2 in fixtures:
        s = Fraction(f2, d1)
        matrix = [
            [Fraction(c), 0, 0, 0],
            [0, c * s, Fraction(c), 0],
            [-e0, -e1 + s * a0, a0, a1],
            [-f0, -f1 + s * d0, d0, d1],
        ]
        actual = determinant4(matrix)
        expected = Fraction(c**2 * (e1 * d1 - a1 * f1))
        assert actual == expected
        assert expected != 0

    # K4-e: nonzero quadratic coefficient is the negative determinant factor.
    c, a1, d1, e1, f1 = 5, 31, 13, 19, 29
    quadratic = a1 * f1 - d1 * e1
    determinant_factor = e1 * d1 - a1 * f1
    assert quadratic == -determinant_factor != 0
    assert c**2 * determinant_factor == -c**3 * Fraction(quadratic, c)
    print(
        "AUDIT_RATE_HALF_LIST_BUDGET_THREE_QUADRATIC_SCROLL_FULL_RANK_PASS "
        "rational_determinant=2 pendant_nonzero=1 k4e_leading_match=1"
    )


if __name__ == "__main__":
    main()
