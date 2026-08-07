#!/usr/bin/env python3
"""Exact replay of the fixed-H translated-divisor witness over F_17."""

from math import gcd


P = 17
N = 16
DOMAIN = tuple(pow(3, i, P) for i in range(N))
BASE = (0, 1, 3, 8, 15)
NEIGHBOURS = (
    (0, 1, 2, 7, 13),
    (1, 4, 8, 9, 11),
    (2, 3, 4, 6, 15),
)


def mul(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % P
    return out


def locator(indices):
    out = [1]
    for i in indices:
        out = mul(out, [(-DOMAIN[i]) % P, 1])
    return out


def divide_exact(numerator, denominator):
    out = numerator[:]
    quotient = [0] * (len(numerator) - len(denominator) + 1)
    for shift in range(len(quotient) - 1, -1, -1):
        coefficient = out[len(denominator) - 1 + shift]
        quotient[shift] = coefficient
        for i, value in enumerate(denominator):
            out[i + shift] = (out[i + shift] - coefficient * value) % P
    assert all(value == 0 for value in out)
    return quotient


def coefficient_scale(poly):
    degree = len(poly) - 1
    scale = gcd(N, degree)
    for j in range(1, degree + 1):
        if poly[degree - j]:
            scale = gcd(scale, j)
    return scale


def main():
    base_locator = locator(BASE)
    complement = tuple(i for i in range(N) if i not in BASE)
    complement_locator = locator(complement)
    assert base_locator == [10, 11, 9, 5, 15, 1]

    pairs = []
    for neighbour in NEIGHBOURS:
        core = set(BASE) & set(neighbour)
        left = tuple(sorted(set(neighbour) - core))
        right = tuple(sorted(set(BASE) - core))
        a = locator(left)
        b = locator(right)
        difference = [(x - y) % P for x, y in zip(a, b)]

        assert len(left) == len(right) == 3
        assert difference == [10, 6, 0, 0]
        assert locator(neighbour)[-2] == base_locator[-2]
        divide_exact(base_locator, b)
        divide_exact(complement_locator, a)
        assert gcd(coefficient_scale(a), coefficient_scale(b)) == 1
        pairs.append((tuple(a), tuple(b)))

    assert len(set(pairs)) == 3
    print(
        "X4_LINEAR_TRANSLATED_DIVISOR_INTERFACE_PASS "
        "field=17 base=5 multiplicity=3 difference=6X+10"
    )


if __name__ == "__main__":
    main()
