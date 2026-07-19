#!/usr/bin/env python3
"""Audit the distance-six residual arithmetic across the high tail."""

from __future__ import annotations

import math


def main() -> None:
    checked = 0
    for excess in range(15, 100_000):
        small = 7 + math.ceil(excess / 2)
        weight = math.ceil(small * (small - 2) / 2)
        distance_four = 2 * (small - 1)
        distance_six = weight - 2 * distance_four
        assert 21 * excess <= 8 * distance_six
        checked += 1
    print(f"AUDIT_F3_H3_HIGH_EXCESS_DISTANCE_SIX_MOMENT_PASS excesses={checked}")


if __name__ == "__main__":
    main()
