#!/usr/bin/env python3
"""Exact replay of the inverse source-ratio representation and degree gate."""

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


def shifted(poly: list[int], scalar: int) -> list[int]:
    return add(poly, [-scalar])


def main() -> None:
    ell = 7
    lambda_value = 19
    lambda_factor = (pow(lambda_value, -1, MOD) - 1) % MOD
    checks = 0

    fixtures = (
        (
            [5, 2, 0, 1, 4, 0, 3, 1],
            [9, 1, 7, 0, 0, 5, 2, 1],
            [13, 4, 1, 0, 6, 3, 0, 1],
        ),
        (
            [11, 6, 2, 0, 5, 1, 4, 1],
            [3, 8, 0, 7, 1, 0, 2, 1],
            [17, 1, 5, 2, 0, 4, 6, 1],
        ),
    )

    for l1, l2, l3 in fixtures:
        inverse_l2_mod_l3 = inverse_mod(l2, l3)
        _, ratio = divmod_poly(mul(l1, inverse_l2_mod_l3), l3)
        a_poly = scale(ratio, lambda_factor)
        f_poly = add(l1, mul(l2, a_poly))
        modulus = mul(l2, l3)

        _, residue_l2 = divmod_poly(f_poly, l2)
        _, residue_l3 = divmod_poly(f_poly, l3)
        _, l1_l2 = divmod_poly(l1, l2)
        _, scaled_l1_l3 = divmod_poly(scale(l1, pow(lambda_value, -1, MOD)), l3)
        assert residue_l2 == l1_l2
        assert residue_l3 == scaled_l1_l3

        inverse = inverse_mod(f_poly, modulus)
        _, identity = divmod_poly(mul(inverse, f_poly), modulus)
        assert identity == [1]
        if degree(ratio) >= 1:
            assert degree(f_poly) == ell + degree(ratio)
        checks += 1

    p_poly = [7, 3] + [0] * (ell - 2) + [1]
    z1, z2, z3 = 5, 29, 71
    l1, l2, l3 = shifted(p_poly, z1), shifted(p_poly, z2), shifted(p_poly, z3)
    _, ratio = divmod_poly(mul(l1, inverse_mod(l2, l3)), l3)
    expected = (z3 - z1) * pow(z3 - z2, -1, MOD) % MOD
    assert ratio == [expected]
    a_poly = scale(ratio, lambda_factor)
    f_poly = add(l1, mul(l2, a_poly))
    assert degree(f_poly) <= ell < ell + 1
    checks += 1

    assert checks == 3
    print("PASS: inverse source-ratio form, degree gate, and common-pencil failure")


if __name__ == "__main__":
    main()
