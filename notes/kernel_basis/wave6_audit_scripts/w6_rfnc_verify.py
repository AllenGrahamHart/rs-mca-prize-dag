#!/usr/bin/env python3
"""Replay the finite coefficient checks in the rich-fiber norm cutoff."""

from __future__ import annotations

import collections
import itertools


def vector(order: int, left: int, right: int) -> dict[int, int]:
    half = order // 2
    out: collections.Counter[int] = collections.Counter()
    for exponent, coefficient in (
        ((left + right) % order, 1),
        (left, -1),
        (right, -1),
    ):
        if exponent >= half:
            exponent -= half
            coefficient = -coefficient
        out[exponent] += coefficient
    return {key: value for key, value in out.items() if value}


def norm_squared(row: dict[int, int]) -> int:
    return sum(value * value for value in row.values())


def main() -> None:
    checked = 0
    parity_checked = 0
    for order in (4, 8, 16, 32, 64, 128, 256):
        half = order // 2
        rows = []
        for left, right in itertools.combinations_with_replacement(range(1, order), 2):
            row = vector(order, left, right)
            square = norm_squared(row)
            assert square <= 9
            assert (square == 9) == (left == right == half)
            if square > 3:
                assert left == right or left == half or right == half
            assert sum(row.values()) % 2 == 1
            rows.append(row)
            checked += 1
        if order <= 32:
            for left, right in itertools.combinations(rows, 2):
                keys = left.keys() | right.keys()
                distance = sum((left.get(key, 0) - right.get(key, 0)) ** 2 for key in keys)
                assert distance % 2 == 0
                parity_checked += 1

    # Ten representations leave at least seven nonexceptional vectors.
    low_count = 7
    maximum_low_norm_sum = low_count * 3
    pair_count = low_count * (low_count - 1) // 2
    assert maximum_low_norm_sum == 21
    assert pair_count * 8 > low_count * maximum_low_norm_sum

    # The same centroid argument does not justify replacing 6 by 4.
    assert pair_count * 6 <= low_count * maximum_low_norm_sum

    for product_count in range(19, 200):
        fixed = product_count % 2
        orbit_count = (product_count + fixed) // 2
        assert orbit_count >= 10

    for exponent in range(2, 42):
        order = 1 << exponent
        assert (order // 2) // 2 == order // 4

    print(
        "H3_RICH_FIBER_NORM_CUTOFF_PASS "
        f"vectors={checked} parity_pairs={parity_checked} "
        "cutoff=19 parseval=6 exponent=n/4"
    )


if __name__ == "__main__":
    main()
