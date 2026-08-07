#!/usr/bin/env python3
"""Exact small replay for the locator-prefix scope theorem."""

from collections import Counter
from itertools import combinations


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


def value(poly, x, p):
    out = 0
    for coefficient in reversed(poly):
        out = (out * x + coefficient) % p
    return out


def prefix(poly, depth):
    degree = len(poly) - 1
    return tuple(poly[degree - i] for i in range(1, depth + 1))


def check_f17_mode():
    counts = Counter(sum(subset) % 17 for subset in combinations(range(1, 17), 9))
    assert sum(counts.values()) == 11440
    assert counts[0] == 672
    assert {counts[s] for s in range(1, 17)} == {673}


def check_prefix_bijection():
    p, domain, agreement, depth = 11, tuple(range(1, 11)), 5, 2
    dimension = agreement - depth
    fibers = {}
    for subset in combinations(domain, agreement):
        q_subset = locator(subset, p)
        fibers.setdefault(prefix(q_subset, depth), []).append((subset, q_subset))

    checked = 0
    for z, members in fibers.items():
        u = [0] * (agreement + 1)
        u[agreement] = 1
        for i, coefficient in enumerate(z, 1):
            u[agreement - i] = coefficient
        seen = set()
        for subset, q_subset in members:
            candidate = [(a - b) % p for a, b in zip(u, q_subset)]
            assert all(x == 0 for x in candidate[dimension:])
            agreements = tuple(x for x in domain if value(candidate, x, p) == value(u, x, p))
            assert agreements == subset
            seen.add(tuple(candidate[:dimension]))
            checked += 1
        assert len(seen) == len(members)
    assert checked == 252


if __name__ == "__main__":
    check_f17_mode()
    check_prefix_bijection()
    print("X4_LOCATOR_PREFIX_CONSUMER_SCOPE_PASS checks=11692")
