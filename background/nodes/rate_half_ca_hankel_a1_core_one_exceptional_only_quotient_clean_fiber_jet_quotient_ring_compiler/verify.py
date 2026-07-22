#!/usr/bin/env python3
"""Exact quotient-ring checks for clean-fiber jet compilation."""

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
    lead_inverse = pow(denominator[-1], -1, prime)
    while remainder != [0] and len(remainder) >= len(denominator):
        shift = len(remainder) - len(denominator)
        coefficient = remainder[-1] * lead_inverse % prime
        quotient[shift] = coefficient
        for index, value in enumerate(denominator):
            remainder[index + shift] = (
                remainder[index + shift] - coefficient * value
            ) % prime
        trim(remainder)
    return trim(quotient), remainder


def reduce(poly: list[int], modulus: list[int], prime: int) -> list[int]:
    return divmod_poly(poly, modulus, prime)[1]


def inverse(poly: list[int], modulus: list[int], prime: int) -> list[int]:
    old_r, r = modulus[:], poly[:]
    old_t, t = [0], [1]
    while r != [0]:
        quotient, remainder = divmod_poly(old_r, r, prime)
        old_r, r = r, remainder
        old_t, t = t, add(old_t, scale(mul(quotient, t, prime), -1, prime), prime)
    if len(old_r) != 1 or old_r[0] == 0:
        raise AssertionError("nonunit quotient-ring denominator")
    return reduce(scale(old_t, pow(old_r[0], -1, prime), prime), modulus, prime)


def qmul(left: list[int], right: list[int], modulus: list[int], prime: int) -> list[int]:
    return reduce(mul(left, right, prime), modulus, prime)


def qpow(base: list[int], exponent: int, modulus: list[int], prime: int) -> list[int]:
    out = [1]
    power = base
    while exponent:
        if exponent & 1:
            out = qmul(out, power, modulus, prime)
        power = qmul(power, power, modulus, prime)
        exponent //= 2
    return out


def derivative(poly: list[int], prime: int) -> list[int]:
    return trim([index * poly[index] % prime for index in range(1, len(poly))])


def main() -> None:
    prime = 101
    order = 5
    rank = 5
    exponent = order + rank - 3
    f = [-1 % prime, 0, 0, 0, 0, 1]  # Y^5-1
    y = [0, 1]

    if qpow(y, exponent, f, prime) != qpow(y, rank - 3, f, prime):
        raise AssertionError("official exponent reduction failed")

    e_0 = 7
    f_t = [1]
    f_y = derivative(f, prime)
    velocity = scale(inverse(f_y, f, prime), -1, prime)
    f_yy = derivative(f_y, prime)
    acceleration = scale(
        qmul(qmul(f_yy, velocity, f, prime), velocity, f, prime),
        -1,
        prime,
    )
    acceleration = qmul(acceleration, inverse(f_y, f, prime), f, prime)

    w = scale(qpow(y, 2, f, prime), -e_0, prime)
    compiled_w = scale(
        qmul(qpow(y, 2, f, prime), inverse(f_t, f, prime), f, prime),
        -e_0,
        prime,
    )
    if compiled_w != w:
        raise AssertionError("first-jet quotient representative failed")

    r_prime = f_y
    r_second = f_yy
    curvature = add(
        qmul(qmul(r_second, velocity, f, prime), velocity, f, prime),
        qmul(r_prime, acceleration, f, prime),
        prime,
    )
    rhs_motion = scale(qmul(y, velocity, f, prime), 2 * e_0 * 2, prime)
    total_numerator = add(
        rhs_motion,
        scale(qmul(curvature, w, f, prime), -1, prime),
        prime,
    )
    total_denominator = scale(qmul(r_prime, velocity, f, prime), 2, prime)
    total_w = qmul(total_numerator, inverse(total_denominator, f, prime), f, prime)
    partial_w = add(
        total_w,
        scale(qmul(derivative(w, prime), velocity, f, prime), -1, prime),
        prime,
    )
    if partial_w != [0]:
        raise AssertionError("second-jet quotient representative failed")

    print(
        "RATE_HALF_QUOTIENT_CLEAN_FIBER_JET_RING_PASS "
        f"prime={prime} order={order} rank={rank} value_degree={len(w)-1}"
    )


if __name__ == "__main__":
    main()
