#!/usr/bin/env python3
"""Independent audit of the E34 nonquarter-diameter weld reduction."""

from __future__ import annotations

import math
from itertools import combinations


def distance(left: int, right: int) -> int:
    delta = (right - left) % 128
    return min(delta, 128 - delta)


def main() -> None:
    total = 0
    for t in range(1, 32):
        heavy = (0, 64, t)
        first = {
            value
            for value in range(128)
            if value not in heavy and any(distance(value, h) == t for h in heavy)
        }
        second = {
            value
            for value in range(128)
            if value not in heavy and any(distance(value, h) == 64 - t for h in heavy)
        }
        assert len(first) == len(second) == 4
        common = first & second
        left_only = first - second
        right_only = second - first
        assert len(common) == 3 and len(left_only) == len(right_only) == 1

        special = sorted(first | second)
        counted = 0
        hostile_left = hostile_right = False
        for size in range(5):
            for chosen in combinations(special, size):
                light = set(chosen)
                if light & first and light & second:
                    counted += math.comb(120, 4 - size)
                if light == left_only:
                    hostile_left = not bool(light & second)
                if light == right_only:
                    hostile_right = not bool(light & first)
        assert hostile_left and hostile_right
        assert counted == 915125
        total += counted * 4 * 16

    assert total == 1815608000
    print(
        "E1_N256_S16_E34_NONQUARTER_DIAMETER_WELD_REDUCTION_AUDIT_PASS "
        "forms=31 mutations=2 vectors=1815608000"
    )


if __name__ == "__main__":
    main()
