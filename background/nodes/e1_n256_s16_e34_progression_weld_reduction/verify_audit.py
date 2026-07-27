#!/usr/bin/env python3
"""Independent audit of the E34 progression-weld reduction."""

from __future__ import annotations

import math
from itertools import combinations, product


def distance(left: int, right: int) -> int:
    delta = (right - left) % 128
    return min(delta, 128 - delta)


def main() -> None:
    total = 0
    for t in range(1, 64):
        if t == 32:
            continue
        heavy = (0, t, (2 * t) % 128)
        assert len(set(heavy)) == 3
        repeated = {
            value
            for value in range(128)
            if value not in heavy and any(distance(value, h) == t for h in heavy)
        }
        outer = distance(heavy[0], heavy[2])
        weld = {
            value
            for value in range(128)
            if value not in heavy and any(distance(value, h) == outer for h in heavy)
        }
        assert len(repeated) == 2 and len(weld) == 4

        counted = 0
        ordered = sorted(weld)
        for size in range(5):
            for chosen in combinations(ordered, size):
                if chosen:
                    counted += math.comb(121, 4 - size)
        assert counted == 1195965
        total += counted * 2 * 16

    # A hostile third heavy-light contribution can reduce eight to one;
    # two contributions cannot reach the target alphabet.
    two = {
        abs(8 + 2 * sum(values) + unit)
        for values in product((-1, 0, 1), repeat=2)
        for unit in (-1, 0, 1)
    }
    three = {
        abs(8 + 2 * sum(values) + unit)
        for values in product((-1, 0, 1), repeat=3)
        for unit in (-1, 0, 1)
    }
    assert two.isdisjoint({0, 1, 2}) and 1 in three
    assert total == 2372794560

    orbit_sizes = {}
    for representative in (1, 2, 4, 8, 16):
        orbit = {
            min((unit * representative) % 128, (-unit * representative) % 128)
            for unit in range(1, 128, 2)
        }
        orbit.discard(0)
        orbit_sizes[representative] = len(orbit)
    assert orbit_sizes == {1: 32, 2: 16, 4: 8, 8: 4, 16: 2}
    assert sum(orbit_sizes.values()) == 62
    assert 5 * 1195965 * 2 * 16 == 191354400
    print(
        "E1_N256_S16_E34_PROGRESSION_WELD_REDUCTION_AUDIT_PASS "
        "forms=62 orbits=5 mutations=1 census_vectors=191354400"
    )


if __name__ == "__main__":
    main()
