#!/usr/bin/env python3
"""Exact polynomial replay for the high-multiplier LS6 Pade reduction."""

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


def extended_gcd(
    left: list[int], right: list[int]
) -> tuple[list[int], list[int], list[int]]:
    old_r, r = trim(left), trim(right)
    old_s, s = [1], [0]
    old_t, t = [0], [1]
    while r != [0]:
        quotient, remainder = divmod_poly(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, add(old_s, scale(mul(quotient, s), -1))
        old_t, t = t, add(old_t, scale(mul(quotient, t), -1))
    leading_inverse = pow(old_r[-1], -1, MOD)
    return (
        scale(old_r, leading_inverse),
        scale(old_s, leading_inverse),
        scale(old_t, leading_inverse),
    )


def inverse_mod(poly: list[int], modulus: list[int]) -> list[int]:
    divisor, coefficient, _ = extended_gcd(poly, modulus)
    assert divisor == [1]
    _, remainder = divmod_poly(coefficient, modulus)
    return remainder


def degree(poly: list[int]) -> int:
    return len(trim(poly)) - 1


def find_guarded_high_example() -> tuple[int, int, int]:
    ell, a = 5, 1
    s, j, e = ell - a, 2 * ell - a, 6
    for seed in range(1, 40):
        modulus = [3 + seed, 2, 5, 0, 7, 1, 0, 3, 0, 0, 1]
        multiplier = [11 + seed, 4, 9, 2, 0, 6, 1]
        if gcd_poly(multiplier, modulus) != [1]:
            continue
        for free in range(MOD):
            quotient = [free, 3, 8, 1, 5, 1]
            candidate, remainder = divmod_poly(mul(modulus, quotient), multiplier)
            if degree(remainder) > s:
                continue
            if degree(candidate) != j or candidate[-1] != 1:
                continue
            if gcd_poly(candidate, modulus) != [1]:
                continue
            if gcd_poly(candidate, quotient) != [1]:
                continue
            value = scale(remainder, -1)
            assert mul(candidate, multiplier) == add(mul(modulus, quotient), value)
            inverse = inverse_mod(multiplier, modulus)
            _, reconstructed = divmod_poly(mul(inverse, value), modulus)
            assert reconstructed == candidate
            assert degree(inverse) >= ell + a
            return degree(candidate), degree(quotient), degree(inverse)
    raise AssertionError("failed to find the deterministic guarded high example")


def check_inverse_gate_falsifier() -> None:
    ell, a = 7, 2
    s = ell - a
    modulus = [1] + [0] * (2 * ell - 1) + [1]
    multiplier = [0] * ell + [1]
    inverse = [0] * ell + [-1]
    product = mul(multiplier, inverse)
    _, inverse_check = divmod_poly(product, modulus)
    assert inverse_check == [1]
    assert degree(inverse) == ell < ell + a

    quotient = [3 + index for index in range(s)] + [1]
    candidate, remainder = divmod_poly(mul(modulus, quotient), multiplier)
    value = scale(remainder, -1)
    assert degree(remainder) == s
    assert gcd_poly(candidate, quotient) != [1]
    assert mul(candidate, multiplier) == add(mul(modulus, quotient), value)


def main() -> None:
    candidate_degree, quotient_degree, inverse_degree = find_guarded_high_example()
    check_inverse_gate_falsifier()
    print(
        "PASS: high-multiplier quotient coordinates, guard transport, and inverse gate",
        f"degrees=({candidate_degree},{quotient_degree},{inverse_degree})",
    )


if __name__ == "__main__":
    main()
