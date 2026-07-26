#!/usr/bin/env python3
"""Independent reflected-product replay at exact rational sample points."""

from __future__ import annotations

import math
from fractions import Fraction


def trim(a: list[Fraction]) -> list[Fraction]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    return trim(out)


def mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] += left * right
    return trim(out)


def scale(a: list[Fraction], c: Fraction | int) -> list[Fraction]:
    return trim([Fraction(c) * value for value in a])


def rising_value(s: int, r: int) -> Fraction:
    out = 1
    for j in range(r):
        out *= s + j
    return Fraction(out, math.factorial(r))


def substitute_reflection(poly: list[Fraction], center: int) -> list[Fraction]:
    out = [Fraction(0)]
    for k, coefficient in enumerate(poly):
        term = [
            coefficient * math.comb(k, j) * center ** (k - j) * (-1) ** j
            for j in range(k + 1)
        ]
        out = add(out, term)
    return out


def invariant_reduction(poly: list[Fraction], center: int) -> tuple[list[Fraction], list[Fraction]]:
    # W^k=A_k(U)W+B_k(U), with W^2=center*W+U.
    powers = [([Fraction(0)], [Fraction(1)]), ([Fraction(1)], [Fraction(0)])]
    for _ in range(2, len(poly)):
        a, b = powers[-1]
        powers.append((add(scale(a, center), b), [Fraction(0)] + a))
    aw = [Fraction(0)]
    constant = [Fraction(0)]
    for coefficient, (a, b) in zip(poly, powers):
        aw = add(aw, scale(a, coefficient))
        constant = add(constant, scale(b, coefficient))
    return aw, constant


def main() -> None:
    checks = 0
    for h in (7, 15):
        for s in (2, 5, 11):
            locator = [Fraction(0)] * (h + 1)
            for r in range(h + 1):
                locator[h - r] = rising_value(s, r)
            for center in (-2, 0, 1, 3):
                reflected = scale(substitute_reflection(locator, center), (-1) ** h)
                product = mul(locator, reflected)
                aw, invariant = invariant_reduction(product, center)
                assert aw == [Fraction(0)]
                assert len(invariant) == h + 1 and invariant[-1] == 1
                z = 1 - center
                for r in range(1, 4):
                    assert invariant[h - r] == rising_value(s, r) * z**r
                checks += 1

    mutations = 0
    h, s, center = 7, 11, 3
    locator = [Fraction(0)] * (h + 1)
    for r in range(h + 1):
        locator[h - r] = rising_value(s, r)
    reflected = scale(substitute_reflection(locator, center), (-1) ** h)
    _, invariant = invariant_reduction(mul(locator, reflected), center)
    mutations += invariant[h - 3] != -rising_value(s, 3) * (1 - center) ** 3
    assert mutations == 1

    print(
        "L1_MERSENNE_HNF_ORDER_ZERO_QUADRATIC_COLLISIONFREE_EXCLUSION_AUDIT_PASS "
        f"reflected_products={checks} coefficient_checks={3 * checks} mutations={mutations}"
    )


if __name__ == "__main__":
    main()
