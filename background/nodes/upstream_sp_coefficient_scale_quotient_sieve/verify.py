#!/usr/bin/env python3
"""Exact independent replay of the SP coefficient-scale quotient sieve."""

from itertools import combinations
from math import gcd


P = 17
N = 8
GEN = 3
DOMAIN = tuple(pow(GEN, 2 * i, P) for i in range(N))


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % P
    return out


def locator(exponents):
    out = [1]
    for i in exponents:
        out = mul(out, [(-DOMAIN[i]) % P, 1])
    return out


def poly_degree(poly):
    for i in range(len(poly) - 1, -1, -1):
        if poly[i] % P:
            return i
    return -1


def coefficient_scale(poly, n):
    e = len(poly) - 1
    indices = [j for j in range(1, e + 1) if poly[e - j] % P]
    value = gcd(n, e)
    for j in indices:
        value = gcd(value, j)
    return value


def invariant_at_scale(exponents, c, n):
    support = set(exponents)
    step = n // c
    return {(i + step) % n for i in support} == support


def maximal_orbit_scale(exponents, n):
    return max(c for c in divisors(n) if invariant_at_scale(exponents, c, n))


def common_prefix_depth(a, b):
    e = len(a) - 1
    depth = 0
    for j in range(1, e + 1):
        if a[e - j] != b[e - j]:
            break
        depth += 1
    return depth


def compressed(poly, c):
    assert (len(poly) - 1) % c == 0
    assert all(x % P == 0 for i, x in enumerate(poly) if i % c)
    return [poly[i] for i in range(0, len(poly), c)]


def main():
    subset_checks = 0
    for size in range(N + 1):
        for support in combinations(range(N), size):
            poly = locator(support)
            scale = coefficient_scale(poly, N)
            assert scale == maximal_orbit_scale(support, N)
            for c in divisors(N):
                invariant = invariant_at_scale(support, c, N)
                gap_form = size % c == 0 and all(
                    poly[size - j] == 0
                    for j in range(1, size + 1)
                    if j % c
                )
                assert invariant == gap_form == (scale % c == 0)
            subset_checks += 1

    pair_checks = 0
    quotient_pairs = 0
    nonconstant_quotient_pairs = 0
    for size in range(1, N // 2 + 1):
        supports = list(combinations(range(N), size))
        for left, right in combinations(supports, 2):
            if set(left) & set(right):
                continue
            a = locator(left)
            b = locator(right)
            t = common_prefix_depth(a, b)
            diff = [(x - y) % P for x, y in zip(a, b)]
            d = poly_degree(diff)
            assert 0 <= d <= size - t - 1
            c = gcd(coefficient_scale(a, N), coefficient_scale(b, N))
            if c > 1:
                ac = compressed(a, c)
                bc = compressed(b, c)
                dc = poly_degree([(x - y) % P for x, y in zip(ac, bc)])
                tc = (t + c) // c - 1
                assert d == c * dc
                assert dc <= size // c - tc - 1
                assert gcd(
                    coefficient_scale(ac, N // c),
                    coefficient_scale(bc, N // c),
                ) == 1
                assert c == gcd(
                    maximal_orbit_scale(left, N),
                    maximal_orbit_scale(right, N),
                )
                assert gcd(N, size, d) % c == 0
                quotient_pairs += 1
                nonconstant_quotient_pairs += d >= 1
            pair_checks += 1

    assert subset_checks == 2**N
    assert quotient_pairs > 0
    assert nonconstant_quotient_pairs > 0
    print(
        "UPSTREAM_SP_COEFFICIENT_SCALE_QUOTIENT_SIEVE_PASS "
        f"subsets={subset_checks} pairs={pair_checks} "
        f"quotient_pairs={quotient_pairs} nonconstant={nonconstant_quotient_pairs}"
    )


if __name__ == "__main__":
    main()
