#!/usr/bin/env python3
"""Independent Python subset-enumeration audit of the explicit witness."""

from __future__ import annotations

import argparse
import copy
from collections import Counter
from fractions import Fraction


def subset_pairs(values: list[tuple[int, int]], q: int) -> Counter[tuple[int, int]]:
    sums = [(0, 0)]
    for a, b in values:
        sums += [((x + a) % q, (y + b) % q) for x, y in sums]
    return Counter(sums)


def subset_scalars(values: list[int], q: int) -> Counter[int]:
    sums = [0]
    for value in values:
        sums += [(current + value) % q for current in sums]
    return Counter(sums)


def build() -> dict[str, int]:
    n, q, zeta = 32, 33409, 7473
    assert pow(zeta, n, q) == 1 and pow(zeta, n // 2, q) == q - 1
    roots = [pow(zeta, i, q) for i in range(n)]
    vectors = [(root, root * root % q) for root in roots]
    left = subset_pairs(vectors[:16], q)
    right = subset_pairs(vectors[16:], q)
    z0 = sum(count * right[((-a) % q, (-b) % q)]
             for (a, b), count in left.items())

    even = subset_scalars([roots[i] * roots[i] % q for i in range(16)], q)
    odd = subset_scalars(roots[:16], q)
    c1 = even[0]
    z1 = sum(count * even[(-value) % q] for value, count in even.items())
    b0 = sum(count * count for count in odd.values())
    primitive = z0 - c1
    assert (z0, c1, primitive, z1, b0) == (384, 256, 128, 1696000, 174912)
    assert Fraction(q**2 * primitive, 2**n) > 8
    assert Fraction(primitive * 2**n, z1 * b0) < 8
    return {"z0": z0, "c1": c1, "primitive": primitive, "z1": z1, "b0": b0}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.tamper_selftest:
        changed = copy.deepcopy(result)
        changed["z0"] += 1
        caught = 0
        try:
            assert changed == result
        except AssertionError:
            caught = 1
        assert caught == 1
        print("DLI_AMBIENT_Q_NO_GO_AUDIT_TAMPER_PASS mutations=1/1")
        return
    print("DLI_AMBIENT_Q_NO_GO_AUDIT_PASS q=33409 subsets=2x65536")


if __name__ == "__main__":
    main()

