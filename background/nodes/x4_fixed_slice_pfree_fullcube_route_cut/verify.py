#!/usr/bin/env python3
"""Exact replay of the fixed-slice syndrome containment and route-cut arithmetic."""

from collections import Counter
from itertools import combinations


def mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return out


def locator_prefix(subset, depth, p):
    poly = [1]
    for x in subset:
        poly = mul(poly, [(-x) % p, 1], p)
    degree = len(poly) - 1
    return tuple(poly[degree - i] for i in range(1, depth + 1))


def syndrome(subset, indices, p):
    return tuple(sum(pow(x, j, p) for x in subset) % p for j in indices)


def main():
    # Exact finite containment check at a nontrivial fixed slice.
    p, domain, weight, depth = 17, tuple(range(1, 17)), 8, 3
    indices = tuple(j for j in range(1, depth + 1) if j % p)
    prefix_to_syndrome = {}
    slice_syndromes = Counter()
    checked = 0
    for subset in combinations(domain, weight):
        z = locator_prefix(subset, depth, p)
        y = syndrome(subset, indices, p)
        if z in prefix_to_syndrome:
            assert prefix_to_syndrome[z] == y
        else:
            prefix_to_syndrome[z] = y
        slice_syndromes[y] += 1
        checked += 1
    assert checked == 12870

    cube_syndromes = Counter()
    for mask in range(1 << len(domain)):
        subset = tuple(domain[i] for i in range(len(domain)) if mask >> i & 1)
        cube_syndromes[syndrome(subset, indices, p)] += 1
    assert max(slice_syndromes.values()) <= max(cube_syndromes.values())

    # Load-bearing official integer inequalities.
    n = 1 << 41
    t_min = (n >> 8) - 2
    assert 2 * t_min * t_min > 641 * n
    assert 129 > 3 * 41

    print(
        "X4_FIXED_SLICE_PFREE_FULLCUBE_ROUTE_CUT_PASS "
        f"slice={checked} prefixes={len(prefix_to_syndrome)} cube={1 << len(domain)}"
    )


if __name__ == "__main__":
    main()
