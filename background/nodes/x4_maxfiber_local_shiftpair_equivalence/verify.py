#!/usr/bin/env python3
"""Exact replay of max-fiber/local-degree equality and prefix rigidity."""

from collections import defaultdict
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


def prefix(poly, depth):
    degree = len(poly) - 1
    return tuple(poly[degree - i] for i in range(1, depth + 1))


def degree(poly):
    for i in range(len(poly) - 1, -1, -1):
        if poly[i]:
            return i
    return -1


def main():
    p, domain, size, depth = 17, tuple(range(1, 17)), 8, 3
    fibers = defaultdict(list)
    locators = {}
    for subset in combinations(domain, size):
        poly = locator(subset, p)
        locators[subset] = poly
        fibers[prefix(poly, depth)].append(subset)

    maximum = max(map(len, fibers.values()))
    max_degree = max(len(fiber) - 1 for fiber in fibers.values())
    assert maximum == 1 + max_degree

    pairs = 0
    top_pairs = 0
    for fiber in fibers.values():
        for left, right in combinations(fiber, 2):
            e = len(set(left) - set(right))
            assert e >= depth + 1
            q_left, q_right = locators[left], locators[right]
            diff = [(a - b) % p for a, b in zip(q_left, q_right)]
            assert degree(diff) <= size - depth - 1
            if e == depth + 1:
                common = tuple(sorted(set(left) & set(right)))
                u = tuple(sorted(set(left) - set(right)))
                v = tuple(sorted(set(right) - set(left)))
                residual = [(a - b) % p for a, b in zip(locator(u, p), locator(v, p))]
                assert degree(residual) == 0
                assert degree(diff) == len(common)
                top_pairs += 1
            pairs += 1
    assert top_pairs > 0

    print(
        "X4_MAXFIBER_LOCAL_SHIFTPAIR_EQUIVALENCE_PASS "
        f"supports={len(locators)} fibers={len(fibers)} max={maximum} "
        f"pairs={pairs} top_pairs={top_pairs}"
    )


if __name__ == "__main__":
    main()
