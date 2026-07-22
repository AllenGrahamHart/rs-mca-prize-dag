#!/usr/bin/env python3
"""Exact check of the Bezout-remainder reconstruction formulas."""

from __future__ import annotations


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left: list[int], right: list[int], prime: int) -> list[int]:
    size = max(len(left), len(right))
    return trim([
        ((left[i] if i < len(left) else 0)
         + (right[i] if i < len(right) else 0)) % prime
        for i in range(size)
    ])


def scale(poly: list[int], scalar: int, prime: int) -> list[int]:
    return trim([scalar * value % prime for value in poly])


def mul(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return trim(out)


def divmod_poly(
    numerator: list[int], denominator: list[int], prime: int
) -> tuple[list[int], list[int]]:
    remainder = trim(numerator[:])
    quotient = [0] * max(1, len(remainder) - len(denominator) + 1)
    inverse = pow(denominator[-1], -1, prime)
    while remainder != [0] and len(remainder) >= len(denominator):
        degree = len(remainder) - len(denominator)
        coefficient = remainder[-1] * inverse % prime
        quotient[degree] = coefficient
        for index, value in enumerate(denominator):
            remainder[index + degree] = (
                remainder[index + degree] - coefficient * value
            ) % prime
        trim(remainder)
    return trim(quotient), remainder


def main() -> None:
    prime = 101
    f_0 = [2, 0, 0, 1]
    a_minus = [4, 3]
    l_p = add([1], scale(mul(f_0, a_minus, prime), -1, prime), prime)

    d_k = [9, 7, 2]
    r_k = [11, 5]
    c_k = add(mul(f_0, d_k, prime), r_k, prime)
    quotient, remainder = divmod_poly(c_k, f_0, prime)
    if quotient != d_k or remainder != r_k:
        raise AssertionError("Euclidean division fixture failed")

    rho_k = scale(remainder, -1, prime)
    s_k = add(quotient, mul(a_minus, remainder, prime), prime)
    unit_stage = add(
        add(c_k, mul(l_p, rho_k, prime), prime),
        scale(mul(f_0, s_k, prime), -1, prime),
        prime,
    )
    if unit_stage != [0]:
        raise AssertionError("reconstructed stage does not vanish")

    bad_c = add(c_k, [0, 0, 17], prime)
    _, bad_remainder = divmod_poly(bad_c, f_0, prime)
    if len(bad_remainder) - 1 < 2:
        raise AssertionError("non-affine remainder mutation was not detected")

    print(
        "RATE_HALF_QUOTIENT_UNIT_BEZOUT_REMAINDER_PASS "
        f"prime={prime} affine_degree={len(remainder)-1} "
        f"bad_degree={len(bad_remainder)-1}"
    )


if __name__ == "__main__":
    main()
