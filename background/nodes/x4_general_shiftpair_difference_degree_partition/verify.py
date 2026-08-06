#!/usr/bin/env python3
"""Small exact replay of the difference-degree partition.

The analytic proof is load-bearing.  This exhaustive finite-field replay is
only a convention and mutation guard.
"""

from itertools import combinations


def mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return out


def locator(roots, p):
    out = [1]
    for root in roots:
        out = mul(out, [(-root) % p, 1], p)
    return out


def degree(poly, p):
    for i in range(len(poly) - 1, -1, -1):
        if poly[i] % p:
            return i
    return -1


def prefix(support, depth, p):
    poly = locator(support, p)
    e = len(support)
    return tuple(poly[e - j] for j in range(1, depth + 1))


def replay(p, domain, size, depth):
    supports = list(combinations(domain, size))
    checked = 0
    saw_constant = False
    saw_nonconstant = False
    for left, right in combinations(supports, 2):
        if prefix(left, depth, p) != prefix(right, depth, p):
            continue
        common = set(left) & set(right)
        lhs = tuple(x for x in left if x not in common)
        rhs = tuple(x for x in right if x not in common)
        assert len(lhs) == len(rhs)
        e = len(lhs)
        lp = locator(lhs, p)
        lq = locator(rhs, p)
        diff = [(lp[i] - lq[i]) % p for i in range(e + 1)]
        d = degree(diff, p)
        assert 0 <= d <= e - depth - 1
        minimal = all(lp[e - j] == lq[e - j] for j in range(1, e))
        assert (d == 0) == minimal
        if e == depth + 1:
            assert d == 0
        saw_constant |= d == 0
        saw_nonconstant |= d >= 1
        checked += 1
    return checked, saw_constant, saw_nonconstant


def main():
    total = 0
    constant = False
    nonconstant = False
    for args in [
        (7, tuple(range(1, 7)), 3, 1),
        (11, tuple(range(1, 11)), 4, 1),
        (13, tuple(range(1, 13)), 5, 2),
    ]:
        checked, saw_c, saw_nc = replay(*args)
        total += checked
        constant |= saw_c
        nonconstant |= saw_nc
    assert total > 0
    assert constant
    assert nonconstant
    print(
        "x4_general_shiftpair_difference_degree_partition: PASS "
        f"pairs={total} constant={constant} nonconstant={nonconstant}"
    )


if __name__ == "__main__":
    main()
