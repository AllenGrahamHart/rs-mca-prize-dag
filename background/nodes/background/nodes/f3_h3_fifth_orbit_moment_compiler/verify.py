#!/usr/bin/env python3
"""Replay the sharp fifth product-orbit compiler for C36'."""

from __future__ import annotations

from fractions import Fraction
from math import comb


def main() -> None:
    equality_cases: list[tuple[int, int, int]] = []
    for product_count in range(0, 2000):
        for diagonal_count in range(0, min(2, product_count) + 1):
            if diagonal_count % 2 != product_count % 2:
                continue
            orbit_count = (product_count + diagonal_count) // 2
            lhs = max(product_count - 18, 0)
            rhs = Fraction(2, 231) * comb(orbit_count, 5)
            if lhs > rhs:
                raise AssertionError(
                    (product_count, diagonal_count, orbit_count, lhs, rhs)
                )
            if lhs and lhs == rhs:
                equality_cases.append((product_count, diagonal_count, orbit_count))

    if equality_cases != [(22, 0, 11)]:
        raise AssertionError(equality_cases)

    # Increasing the denominator makes the sharp coefficient too small.
    if Fraction(2, 232) * comb(11, 5) >= 22 - 18:
        raise AssertionError("sharp-coefficient mutation undetected")

    allowance = Fraction(34650, 17)
    if 17 * Fraction(2, 231) * allowance != 300:
        raise AssertionError("consumer arithmetic mismatch")

    print(
        "H3_FIFTH_ORBIT_MOMENT_COMPILER_PASS "
        "sharp=P22_D0_U11 allowance=34650n2/17"
    )


if __name__ == "__main__":
    main()
