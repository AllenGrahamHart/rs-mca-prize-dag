#!/usr/bin/env python3
"""Exact modular controls for triangular affine reconstruction."""

from __future__ import annotations


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left: list[int], right: list[int], prime: int) -> list[int]:
    size = max(len(left), len(right))
    out = [0] * size
    for index in range(size):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % prime
    return trim(out)


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
    while len(remainder) >= len(denominator) and remainder != [0]:
        degree = len(remainder) - len(denominator)
        coefficient = remainder[-1] * inverse % prime
        quotient[degree] = coefficient
        for index, value in enumerate(denominator):
            remainder[index + degree] = (
                remainder[index + degree] - coefficient * value
            ) % prime
        trim(remainder)
    return trim(quotient), trim(remainder)


def invert_mod(poly: list[int], modulus: list[int], prime: int) -> list[int]:
    old_r, r = modulus[:], poly[:]
    old_t, t = [0], [1]
    while r != [0]:
        quotient, remainder = divmod_poly(old_r, r, prime)
        old_r, r = r, remainder
        old_t, t = t, add(old_t, scale(mul(quotient, t, prime), -1, prime), prime)
    if len(old_r) != 1 or old_r[0] == 0:
        raise AssertionError("polynomial is not invertible modulo f_0")
    inverse_gcd = pow(old_r[0], -1, prime)
    _, reduced = divmod_poly(scale(old_t, inverse_gcd, prime), modulus, prime)
    return reduced


def reconstruct(
    c_base: list[int], multiplier: list[int], modulus: list[int], prime: int
) -> list[int]:
    inverse = invert_mod(multiplier, modulus, prime)
    _, residue = divmod_poly(scale(mul(c_base, inverse, prime), -1, prime), modulus, prime)
    return residue


def main() -> None:
    prime = 101
    f_0 = [2, 0, 0, 1]       # t^3+2
    l_0 = [1, 1]             # t+1
    p_cl = [1, 0, 1]         # t^2+1
    multiplier = mul(l_0, p_cl, prime)

    expected = ([7, 5], [13, 11])
    recovered: list[list[int]] = []
    for index, affine in enumerate(expected):
        multiple = [3 + index, 2]
        c_base = add(
            scale(mul(multiplier, affine, prime), -1, prime),
            mul(f_0, multiple, prime),
            prime,
        )
        residue = reconstruct(c_base, multiplier, f_0, prime)
        if residue != list(affine):
            raise AssertionError("affine correction was not reconstructed")
        recovered.append(residue)

    bad_target = [1, 2, 3]
    bad_base = scale(mul(multiplier, bad_target, prime), -1, prime)
    bad_residue = reconstruct(bad_base, multiplier, f_0, prime)
    if len(bad_residue) - 1 < 2:
        raise AssertionError("non-affine mutation was not rejected")
    print(
        "RATE_HALF_QUOTIENT_UNIT_TRIANGULAR_AFFINE_PASS "
        f"prime={prime} recovered={recovered} bad_degree={len(bad_residue) - 1}"
    )


if __name__ == "__main__":
    main()
