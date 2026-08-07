#!/usr/bin/env python3
"""Exact replay of prefix twist orbits and their moment contribution."""

from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, gcd


def mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return out


def locator(subset, p):
    out = [1]
    for x in subset:
        out = mul(out, [(-x) % p, 1], p)
    return out


def prefix(subset, depth, p):
    poly = locator(subset, p)
    degree = len(poly) - 1
    return tuple(poly[degree - i] for i in range(1, depth + 1))


def transform(z, scale, p):
    return tuple(value * pow(scale, i, p) % p for i, value in enumerate(z, 1))


def stabilizer_size(z, order):
    active = [i for i, value in enumerate(z, 1) if value]
    if not active:
        return order
    out = order
    for i in active:
        out = gcd(out, i)
    return out


def main():
    p, domain, size, depth = 17, tuple(range(1, 17)), 8, 3
    order = len(domain)
    fibers = Counter(prefix(subset, depth, p) for subset in combinations(domain, size))
    total = comb(order, size)
    assert total == sum(fibers.values()) == 12870

    orbit_checks = 0
    for z, count in fibers.items():
        orbit = {transform(z, scale, p) for scale in domain}
        expected = order // stabilizer_size(z, order)
        assert len(orbit) == expected
        assert {fibers[value] for value in orbit} == {count}
        orbit_checks += len(orbit)

    q = p**depth
    for moment in (2, 3, 4):
        gamma = Fraction(q ** (moment - 1) * sum(c**moment for c in fibers.values()), total**moment)
        for z, count in fibers.items():
            s_z = stabilizer_size(z, order)
            normalized = Fraction(q * count, total)
            forced = Fraction(order, s_z) * normalized**moment / q
            assert gamma >= forced

    print(
        "X4_PREFIX_TWIST_ORBIT_MOMENT_PASS "
        f"subsets={total} fibers={len(fibers)} orbit_checks={orbit_checks} moments=3"
    )


if __name__ == "__main__":
    main()
