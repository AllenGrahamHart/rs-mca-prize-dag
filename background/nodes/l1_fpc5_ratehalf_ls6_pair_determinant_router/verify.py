#!/usr/bin/env python3
"""Exact replay for the guarded LS6 pair cross determinant."""

from __future__ import annotations


MOD = 257


def trim(poly: list[int]) -> list[int]:
    out = [value % MOD for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    return trim([
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(size)
    ])


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([scalar * value for value in poly])


def mul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, x_value in enumerate(left):
        for j, y_value in enumerate(right):
            out[i + j] = (out[i + j] + x_value * y_value) % MOD
    return trim(out)


def divmod_poly(
    numerator: list[int], denominator: list[int]
) -> tuple[list[int], list[int]]:
    remainder = trim(numerator)
    denominator = trim(denominator)
    quotient = [0] * max(1, len(remainder) - len(denominator) + 1)
    inverse = pow(denominator[-1], -1, MOD)
    while remainder != [0] and len(remainder) >= len(denominator):
        shift = len(remainder) - len(denominator)
        coefficient = remainder[-1] * inverse % MOD
        quotient[shift] = coefficient
        for index, value in enumerate(denominator):
            remainder[index + shift] -= coefficient * value
        remainder = trim(remainder)
    return trim(quotient), remainder


def monic(poly: list[int]) -> list[int]:
    poly = trim(poly)
    return scale(poly, pow(poly[-1], -1, MOD))


def gcd_poly(left: list[int], right: list[int]) -> list[int]:
    left, right = trim(left), trim(right)
    while right != [0]:
        _, remainder = divmod_poly(left, right)
        left, right = right, remainder
    return monic(left)


def degree(poly: list[int]) -> int:
    return len(trim(poly)) - 1


def candidate(
    modulus: list[int], multiplier: list[int], quotient: list[int], tail: list[int]
) -> tuple[list[int], list[int]]:
    base, remainder = divmod_poly(mul(modulus, quotient), multiplier)
    locator = add(base, tail)
    value = add(scale(remainder, -1), mul(multiplier, tail))
    return locator, value


def main() -> None:
    ell, a, e = 7, 2, 4
    s, j = ell - a, 2 * ell - a
    l2 = [3, 1] + [0] * (ell - 2) + [1]
    l3 = [11, 2] + [0] * (ell - 2) + [1]
    modulus = mul(l2, l3)
    multiplier = [5, 6, 7, 8, 1]

    fixtures: list[tuple[list[int], list[int], list[int]]] = []
    for seed in range(1, 80):
        quotient = [13 + seed, 17 + 2 * seed, 1]
        tail = [19 + 3 * seed, 23 + 5 * seed]
        locator, value = candidate(modulus, multiplier, quotient, tail)
        if degree(locator) != j or locator[-1] != 1:
            continue
        if gcd_poly(locator, modulus) != [1]:
            continue
        if gcd_poly(locator, quotient) != [1]:
            continue
        if gcd_poly(locator, value) != [1]:
            continue
        fixtures.append((locator, quotient, value))
        if len(fixtures) == 2:
            break

    assert len(fixtures) == 2
    d1, q1, v1 = fixtures[0]
    d2, q2, v2 = fixtures[1]
    determinant = add(mul(d1, q2), scale(mul(d2, q1), -1))
    numerator = add(mul(d2, v1), scale(mul(d1, v2), -1))
    quotient_h, remainder_h = divmod_poly(numerator, modulus)

    assert determinant != [0]
    assert remainder_h == [0]
    assert quotient_h == determinant
    assert degree(determinant) <= ell - 2 * a
    assert degree(gcd_poly(d1, d2)) <= degree(determinant)
    assert degree(q1) == degree(q2) == e - a

    for ell_value, b_value, a_value in ((17, 9, 1), (23, 15, 2), (31, 27, 4)):
        locator_degree = 2 * ell_value - a_value
        core_size = 4 * ell_value + b_value - 2
        intersection = ell_value - 2 * a_value
        johnson = (
            ell_value * (4 * a_value - b_value + 2)
            + a_value * a_value
            + 2 * a_value * b_value
            - 4 * a_value
        )
        assert locator_degree * locator_degree - core_size * intersection == johnson
        assert johnson <= 0

    print("PASS: primitive LS6 pair determinant, intersection cap, and J identity")


if __name__ == "__main__":
    main()
