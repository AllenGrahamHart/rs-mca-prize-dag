#!/usr/bin/env python3
"""Exact controls for the bounded-tail dihedral row-codegree theorem."""

from __future__ import annotations


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index in range(len(out)):
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


def evaluate(poly: list[int], value: int, prime: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * value + coefficient) % prime
    return out


def locator(roots: tuple[int, ...], prime: int) -> list[int]:
    out = [1]
    for root in roots:
        out = mul(out, [-root % prime, 1], prime)
    return out


def lagrange(index: int, points: tuple[int, ...], prime: int) -> list[int]:
    out = [1]
    denominator = 1
    pivot = points[index]
    for other, point in enumerate(points):
        if other == index:
            continue
        out = mul(out, [-point % prime, 1], prime)
        denominator = denominator * (pivot - point) % prime
    return scale(out, pow(denominator, -1, prime), prime)


def check_fixture(reciprocal: bool) -> tuple[int, int]:
    prime = 101
    e = 5
    tail = 2
    xis = (2, 3, 5, 7, 11)
    phi = scale(locator(xis, prime), pow(evaluate(locator(xis, prime), 0, prime), -1, prime), prime)
    ls = [lagrange(index, xis, prime) for index in range(e)]
    alpha = (13, 17, 19, 23, 29)
    b_poly = locator((31, 37, 41), prime)

    if reciprocal:
        c = 4
        good = (
            [c, -9 % prime, 1],
            [c, -12 % prime, 1],
            [c, -15 % prime, 1],
        )
        x = 6
        y = c * pow(x, -1, prime) % prime
    else:
        c = 0
        good = (
            [-9 % prime, 0, 1],
            [-16 % prime, 0, 1],
            [-25 % prime, 0, 1],
        )
        x = 8
        y = -x % prime
    tails = (
        locator((43, 47), prime),
        locator((53, 59), prime),
    )
    d_polys = good + tails
    need(all(evaluate(poly, x, prime) and evaluate(poly, y, prime) for poly in d_polys),
         "fixture outside orbit hit exceptional support")

    beta_x = evaluate(b_poly, x, prime)
    if reciprocal:
        beta_y = x * x * evaluate(b_poly, y, prime) * pow(c, -1, prime) % prime
    else:
        beta_y = evaluate(b_poly, y, prime)

    h_poly = scale(phi, beta_x - beta_y, prime)
    for index in range(e - tail, e):
        d_x = evaluate(d_polys[index], x, prime)
        if reciprocal:
            d_y = x * x * evaluate(d_polys[index], y, prime) * pow(c, -1, prime) % prime
        else:
            d_y = evaluate(d_polys[index], y, prime)
        coefficient = (
            beta_x
            * beta_y
            * alpha[index]
            * (pow(d_y, -1, prime) - pow(d_x, -1, prime))
        ) % prime
        h_poly = add(h_poly, scale(mul([0, 1], ls[index], prime), coefficient, prime), prime)

    i_good = locator(xis[: e - tail], prime)
    quotient, remainder = divmod_poly(h_poly, i_good, prime)
    need(remainder == [0], "good internal locator did not divide eliminant")
    need(len(quotient) - 1 <= tail, "tail quotient degree exceeded tail count")

    # Directly replay the common-root implication over the base field.
    q_x = phi[:]
    q_y = phi[:]
    for index, d_poly in enumerate(d_polys):
        d_x = evaluate(d_poly, x, prime)
        if reciprocal:
            d_y_hat = x * x * evaluate(d_poly, y, prime) * pow(c, -1, prime) % prime
        else:
            d_y_hat = evaluate(d_poly, y, prime)
        q_x = add(q_x, scale(mul([0, 1], ls[index], prime), beta_x * alpha[index] * pow(d_x, -1, prime), prime), prime)
        q_y = add(q_y, scale(mul([0, 1], ls[index], prime), beta_y * alpha[index] * pow(d_y_hat, -1, prime), prime), prime)

    common = [
        value
        for value in range(1, prime)
        if value not in xis
        and evaluate(q_x, value, prime) == 0
        and evaluate(q_y, value, prime) == 0
    ]
    need(all(evaluate(quotient, value, prime) == 0 for value in common),
         "common row root escaped tail quotient")
    need(len(common) <= tail, "fixture codegree exceeded tail count")
    return len(quotient) - 1, len(common)


def check_identity_orbits() -> tuple[int, int]:
    prime = 101
    b_poly = locator((3, 7, 11), prime)
    antipodal = {
        min(x, -x % prime)
        for x in range(1, prime)
        if evaluate(b_poly, x, prime) == evaluate(b_poly, -x % prime, prime)
    }
    c = 4
    reciprocal = {
        min(x, c * pow(x, -1, prime) % prime)
        for x in range(1, prime)
        if x != c * pow(x, -1, prime) % prime
        and evaluate(b_poly, x, prime)
        == x * x * evaluate(b_poly, c * pow(x, -1, prime) % prime, prime) * pow(c, -1, prime) % prime
    }
    need(len(antipodal) <= 1 and len(reciprocal) <= 1,
         "more than one identity orbit appeared")
    return len(antipodal), len(reciprocal)


def main() -> None:
    anti = check_fixture(False)
    reciprocal = check_fixture(True)
    identity = check_identity_orbits()
    print(
        "RATE_HALF_DISTANCE_THREE_BOUNDED_TAIL_ROW_CODEGREE_PASS "
        f"antipodal={anti} reciprocal={reciprocal} "
        f"identity_orbits={identity} official_tail_bound=40"
    )


if __name__ == "__main__":
    main()
