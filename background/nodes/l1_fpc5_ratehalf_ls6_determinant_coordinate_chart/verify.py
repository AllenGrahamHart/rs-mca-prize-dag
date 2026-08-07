#!/usr/bin/env python3
"""Exact replay for the LS6 determinant coordinate chart."""

from __future__ import annotations

from itertools import product


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


def sub(left: list[int], right: list[int]) -> list[int]:
    return add(left, scale(right, -1))


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


def inverse_mod(poly: list[int], modulus: list[int]) -> list[int]:
    old_r, current_r = trim(poly), trim(modulus)
    old_s, current_s = [1], [0]
    while current_r != [0]:
        quotient, remainder = divmod_poly(old_r, current_r)
        old_r, current_r = current_r, remainder
        old_s, current_s = current_s, sub(old_s, mul(quotient, current_s))
    assert len(old_r) == 1 and old_r[0] != 0
    inverse = scale(old_s, pow(old_r[0], -1, MOD))
    _, inverse = divmod_poly(inverse, modulus)
    assert divmod_poly(mul(poly, inverse), modulus)[1] == [1]
    return inverse


def degree(poly: list[int]) -> int:
    return len(trim(poly)) - 1


def derivative(poly: list[int]) -> list[int]:
    return trim([index * value for index, value in enumerate(poly)][1:] or [0])


def evaluate(poly: list[int], point: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * point + coefficient) % MOD
    return value


def roots(poly: list[int]) -> list[int]:
    return [point for point in range(MOD) if evaluate(poly, point) == 0]


def candidate(
    modulus: list[int], multiplier: list[int], quotient: list[int], tail: list[int]
) -> tuple[list[int], list[int]]:
    base, remainder = divmod_poly(mul(modulus, quotient), multiplier)
    locator = add(base, tail)
    value = add(scale(remainder, -1), mul(multiplier, tail))
    return locator, value


def chart_inverse(
    determinant: list[int],
    modulus: list[int],
    base_locator: list[int],
    base_quotient: list[int],
    base_value: list[int],
    quotient_inverse: list[int],
) -> tuple[list[int], list[int], list[int]]:
    residue = divmod_poly(
        scale(mul(determinant, quotient_inverse), -1), base_locator
    )[1]
    locator = add(base_locator, residue)
    quotient, quotient_remainder = divmod_poly(
        add(determinant, mul(locator, base_quotient)), base_locator
    )
    value, value_remainder = divmod_poly(
        sub(mul(locator, base_value), mul(modulus, determinant)), base_locator
    )
    assert quotient_remainder == [0]
    assert value_remainder == [0]
    return locator, quotient, value


def main() -> None:
    ell, a, e = 7, 2, 4
    s, j, h = ell - a, 2 * ell - a, ell - 2 * a
    l2 = [3, 1] + [0] * (ell - 2) + [1]
    l3 = [11, 2] + [0] * (ell - 2) + [1]
    modulus = mul(l2, l3)
    multiplier = [5, 6, 7, 8, 1]

    base = None
    for seed in range(1, 2001):
        quotient = [13 + seed, 17 + 2 * seed, 1]
        tail = [19 + 3 * seed, 23 + 5 * seed]
        locator, value = candidate(modulus, multiplier, quotient, tail)
        if degree(locator) != j or locator[-1] != 1:
            continue
        if gcd_poly(locator, modulus) != [1]:
            continue
        if gcd_poly(locator, quotient) != [1]:
            continue
        if gcd_poly(locator, derivative(locator)) != [1]:
            continue
        if not roots(locator):
            continue
        base = (locator, quotient, value)
        break
    assert base is not None
    d0, q0, v0 = base
    q0_inverse = inverse_mod(q0, d0)

    chart = []
    for coefficients in product(range(3), repeat=h + 1):
        determinant = trim(list(coefficients))
        locator, quotient, value = chart_inverse(
            determinant, modulus, d0, q0, v0, q0_inverse
        )
        assert degree(locator) == j and locator[-1] == 1
        assert degree(quotient) == e - a and quotient[-1] == q0[-1]
        assert degree(value) <= s
        assert mul(locator, multiplier) == add(mul(modulus, quotient), value)
        assert sub(mul(d0, quotient), mul(locator, q0)) == determinant

        for point in roots(d0):
            assert (evaluate(locator, point) == 0) == (
                evaluate(determinant, point) == 0
            )
        for point in roots(locator):
            primitive_at_point = evaluate(quotient, point) != 0
            if evaluate(d0, point) != 0:
                assert primitive_at_point == (evaluate(determinant, point) != 0)
            else:
                local_guard = (
                    evaluate(derivative(determinant), point)
                    + evaluate(derivative(locator), point) * evaluate(q0, point)
                ) % MOD
                assert primitive_at_point == (local_guard != 0)
        chart.append((determinant, locator, quotient))

    pair_checks = 0
    for h_left, d_left, q_left in chart[:12]:
        for h_right, d_right, q_right in chart[12:24]:
            cross = sub(mul(d_left, q_right), mul(d_right, q_left))
            numerator = sub(mul(d_left, h_right), mul(d_right, h_left))
            quotient, remainder = divmod_poly(numerator, d0)
            assert remainder == [0]
            assert quotient == cross
            assert degree(cross) <= h
            pair_checks += 1

    print(
        "PASS: LS6 determinant coordinate chart "
        f"coordinates={len(chart)} pair_checks={pair_checks} base_roots={len(roots(d0))}"
    )


if __name__ == "__main__":
    main()
