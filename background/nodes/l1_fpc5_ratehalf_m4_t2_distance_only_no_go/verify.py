#!/usr/bin/env python3
"""Exact arithmetic replay of the sharp distance-only Gilbert fence."""

from __future__ import annotations

import math


def entropy(value: float) -> float:
    if value in (0.0, 1.0):
        return 0.0
    return -value * math.log2(value) - (1.0 - value) * math.log2(1.0 - value)


def gilbert_lower_bound(length: int) -> tuple[int, int, int]:
    core = 5 * length + 5
    weight = 2 * length + 1
    terms = [
        math.comb(weight, index) * math.comb(core - weight, index)
        for index in range(length + 2)
    ]
    assert all(left <= right for left, right in zip(terms, terms[1:]))
    ball = sum(terms)
    total = math.comb(core, weight)
    lower = (total + ball - 1) // ball
    return lower, total, ball


def main() -> None:
    coefficient = (
        5 * entropy(2 / 5) - 2 * entropy(1 / 2) - 3 * entropy(1 / 3)
    )
    assert 0.0998 < coefficient < 0.1000

    rates = []
    for length in (8, 16, 32, 64, 128, 256, 512, 1024):
        lower, total, ball = gilbert_lower_bound(length)
        assert lower * ball >= total
        assert (lower - 1) * ball < total

        ell = length + 2
        core = 5 * ell - 5
        defect = 2 * ell - 3
        background = ell - 3
        s = ell - 3
        assert core == 5 * length + 5
        assert defect == 2 * length + 1
        assert background == length - 1
        assert (length - 1) + background == 2 * s
        rates.append(math.log2(lower) / length)

    assert rates[-1] > coefficient
    assert rates[-1] < coefficient + 0.01
    assert all(left > right for left, right in zip(rates, rates[1:]))

    official_ell = (2**40 + 4) // 5
    official_length = official_ell - 2
    assert official_length == 219902325554
    print(
        "L1_FPC5_DISTANCE_ONLY_NO_GO_PASS "
        f"entropy_exponent={coefficient:.10f} "
        f"L1024_rate={rates[-1]:.10f} official_L={official_length}"
    )


if __name__ == "__main__":
    main()
