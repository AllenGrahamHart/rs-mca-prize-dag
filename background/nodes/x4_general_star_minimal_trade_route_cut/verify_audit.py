#!/usr/bin/env python3
"""Independent union-partition audit of the route-cut census."""

from itertools import combinations


MODULUS = 17
POINTS = tuple(range(1, MODULUS))
EXPECTED = (120, 364, 352, 126, 0, 0, 0, 1)


def prefix(support, depth):
    values = [1] + [0] * len(support)
    for point in support:
        for index in range(len(support), 0, -1):
            values[index] = (values[index] + point * values[index - 1]) % MODULUS
    return tuple(values[1 : depth + 1])


def complementary_records(width, depth):
    total = 0
    for union in combinations(POINTS, 2 * width):
        union_set = set(union)
        for left in combinations(union, width):
            right = tuple(sorted(union_set.difference(left)))
            if left >= right:
                continue
            if prefix(left, depth) == prefix(right, depth):
                total += 1
    return total


def main():
    witness_left = (1, 2, 3)
    witness_right = (4, 5, 14)
    assert prefix(witness_left, 1) == prefix(witness_right, 1) == (6,)
    assert prefix(witness_left, 2) != prefix(witness_right, 2)
    assert not any(
        prefix(left, 1) == prefix(right, 1)
        for left in combinations(witness_left, 2)
        for right in combinations(witness_right, 2)
    )

    general = complementary_records(3, 1)
    minimal = tuple(complementary_records(width, width - 1) for width in range(1, 9))
    assert general == 4576
    assert minimal == EXPECTED
    assert sum(minimal) == 963 < general

    print("X4_GENERAL_STAR_MINIMAL_TRADE_ROUTE_CUT_AUDIT_PASS")
    print(f"general={general} minimal_total={sum(minimal)}")


if __name__ == "__main__":
    main()
