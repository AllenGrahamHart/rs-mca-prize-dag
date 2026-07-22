#!/usr/bin/env python3
"""Exhaust the fixed-root and scalar-free nu=2 tests on small analogues."""

from __future__ import annotations


EXPECTED = {
    7: (1, 0, 0),
    31: (65, 3, 0),
    127: (1281, 19, 0),
}


def multiply(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        if left:
            for j, right in enumerate(b):
                out[i + j] = (out[i + j] + left * right) % p
    return out


def linear_power(root: int, exponent: int, p: int) -> list[int]:
    out = [1]
    for _ in range(exponent):
        out = multiply(out, [-root % p, 1], p)
    return out


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def evaluate(poly: list[int], point: int, p: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * point + coefficient) % p
    return value


def remainder(dividend: list[int], divisor: list[int], p: int) -> list[int]:
    dividend = trim(dividend[:])
    divisor = trim(divisor[:])
    inverse_leader = pow(divisor[-1], -1, p)
    while len(dividend) >= len(divisor):
        offset = len(dividend) - len(divisor)
        scale = dividend[-1] * inverse_leader % p
        for index, value in enumerate(divisor):
            dividend[offset + index] = (
                dividend[offset + index] - scale * value
            ) % p
        trim(dividend)
    return dividend


def data(p: int, exponents: tuple[int, int, int]) -> tuple[tuple[int, ...], int]:
    e1, e2, e3 = exponents
    differences = ((e2 - e3) % p, (e3 - e1) % p, (e1 - e2) % p)
    assert all(differences)
    w = 1
    for difference, exponent in zip(differences, exponents):
        w = w * pow(difference, exponent, p) % p
    return differences, w


def sign_passes(
    p: int,
    exponents: tuple[int, int, int],
    differences: tuple[int, ...],
    w: int,
    sign: int,
) -> bool:
    product = 1
    for difference, exponent in zip(differences, exponents):
        product = product * pow(
            (3 * w - 4 * sign * difference) % p, exponent, p
        ) % p
    return (product + w) % p == 0


def scalar_free_inner(
    p: int,
    exponents: tuple[int, int, int],
    differences: tuple[int, ...],
    w: int,
) -> list[int]:
    inverse_four = pow(4, -1, p)
    inner = [1]
    for difference, exponent in zip(differences, exponents):
        root = 3 * w * inverse_four * pow(difference, -1, p) % p
        inner = multiply(inner, linear_power(root, exponent, p), p)
    inner[0] = (inner[0] + 3 * inverse_four) % p
    assert len(inner) == p + 1 and inner[-1] == 1 and inner[0] == 0
    return inner


def divides_domain(p: int, inner: list[int]) -> bool:
    square = multiply(inner, inner, p)
    cubic = multiply(square, inner, p)
    outer = cubic + [0] * max(0, len(inner) - len(cubic))
    for index, value in enumerate(inner):
        outer[index] = (outer[index] - 2 * value) % p
    outer[0] = (outer[0] + 1) % p
    trim(outer)
    n = 4 * (p + 1)
    domain = [p] + [0] * (n - 1) + [1]
    return remainder(domain, outer, p) == [0]


def census(p: int) -> tuple[int, int, int]:
    triples = sign_hits = divisibility_hits = 0
    for e1 in range(1, p):
        for e2 in range(e1 + 1, p):
            e3 = p - e1 - e2
            if e3 <= e2:
                continue
            exponents = (e1, e2, e3)
            differences, w = data(p, exponents)
            triples += 1
            signs = [
                sign
                for sign in (1, -1)
                if sign_passes(p, exponents, differences, w, sign)
            ]
            assert len(signs) <= 1
            if not signs:
                continue
            sign_hits += 1
            inner = scalar_free_inner(p, exponents, differences, w)
            assert evaluate(inner, signs[0], p) == 1
            if divides_domain(p, inner):
                divisibility_hits += 1
    return triples, sign_hits, divisibility_hits


def main() -> None:
    for p, expected in EXPECTED.items():
        observed = census(p)
        assert observed == expected, (p, observed, expected)
        print(
            f"p={p} triples={observed[0]} "
            f"sign_hits={observed[1]} divisibility_hits={observed[2]}"
        )
    print("L1_M4_H3_NU2_SCALAR_FREE_ANALOGS_PASS")


if __name__ == "__main__":
    main()
