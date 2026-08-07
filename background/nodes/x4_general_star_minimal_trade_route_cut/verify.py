#!/usr/bin/env python3
"""Exact prefix-bucket census for the general-to-minimal route cut."""

from collections import defaultdict
from itertools import combinations


P = 17
DOMAIN = tuple(range(1, P))
EXPECTED_MINIMAL = {1: 120, 2: 364, 3: 352, 4: 126, 5: 0, 6: 0, 7: 0, 8: 1}


def elementary(values):
    coeffs = [1]
    for value in values:
        coeffs.append(0)
        for degree in range(len(coeffs) - 1, 0, -1):
            coeffs[degree] = (
                coeffs[degree] + value * coeffs[degree - 1]
            ) % P
    return tuple(coeffs[1:])


def mask(values):
    return sum(1 << (value - 1) for value in values)


def disjoint_pair_count(width, depth):
    buckets = defaultdict(list)
    for support in combinations(DOMAIN, width):
        buckets[elementary(support)[:depth]].append(mask(support))
    return sum(
        1
        for bucket in buckets.values()
        for index, left in enumerate(bucket)
        for right in bucket[index + 1 :]
        if left & right == 0
    )


def dihedral_image(support, scale, invert):
    if invert:
        return {scale * pow(value, -1, P) % P for value in support}
    return {scale * value % P for value in support}


def main():
    left = (1, 2, 3)
    right = (4, 5, 14)
    left_e = elementary(left)
    right_e = elementary(right)
    assert left_e == (6, 11, 6)
    assert right_e == (6, 10, 8)
    assert left_e[0] == right_e[0] != 0
    assert left_e[1] != right_e[1]

    left_pair_sums = {(a + b) % P for a, b in combinations(left, 2)}
    right_pair_sums = {(a + b) % P for a, b in combinations(right, 2)}
    assert left_pair_sums == {3, 4, 5}
    assert right_pair_sums == {1, 2, 9}
    assert left_pair_sums.isdisjoint(right_pair_sums)
    assert all(
        dihedral_image(left, scale, invert) != set(right)
        for scale in DOMAIN
        for invert in (False, True)
    )

    general = disjoint_pair_count(3, 1)
    minimal = {width: disjoint_pair_count(width, width - 1) for width in range(1, 9)}
    assert general == 4576
    assert minimal == EXPECTED_MINIMAL
    assert sum(minimal.values()) == 963
    assert sum(minimal[width] for width in range(2, 9)) == 843
    assert general > sum(minimal.values())

    print("X4_GENERAL_STAR_MINIMAL_TRADE_ROUTE_CUT_PASS")
    print(f"general_order1_width3={general}")
    print("minimal_widths_1_to_8=" + ",".join(str(minimal[h]) for h in range(1, 9)))
    print(f"minimal_total={sum(minimal.values())}")
    print(f"minimal_total_widths_2_to_8={sum(minimal[h] for h in range(2, 9))}")
    print("witness=P(1,2,3),Q(4,5,14)")


if __name__ == "__main__":
    main()
