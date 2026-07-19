#!/usr/bin/env python3
"""Audit the exact high-tail composition on deterministic integer profiles."""

from __future__ import annotations

import math
import random


def minimum_weight(excess: int) -> int:
    small = 7 + math.ceil(excess / 2)
    return math.ceil(small * (small - 4) / 2)


def main() -> None:
    rng = random.Random(0x33_83)
    checked = 0
    for n in (32, 64, 128):
        budget = 300 * n * n - 238 * (n - 1) * (n - 2)
        for _ in range(1000):
            moment = 0
            high_excess = 0
            for excess in range(15, 80):
                quotient_weight = rng.randrange(4)
                edge_weight = minimum_weight(excess)
                assert 83 * excess <= 16 * edge_weight
                moment += edge_weight * quotient_weight
                high_excess += excess * quotient_weight
            assert 83 * high_excess <= 16 * moment
            if 272 * moment <= 83 * budget:
                assert 17 * high_excess <= budget
            checked += 1
    print(f"AUDIT_F3_H3_HIGH_EXCESS_LOW_DISTANCE_MOMENT_PASS profiles={checked}")


if __name__ == "__main__":
    main()
