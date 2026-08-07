#!/usr/bin/env python3
"""Arithmetic replay for sharp FPC5 pure quotient absence."""

from __future__ import annotations

import math


def divisors_power_two(exponent: int) -> list[int]:
    return [2**power for power in range(1, exponent + 1)]


def main() -> None:
    rows = 0
    scales = 0
    for exponent in range(4, 41, 4):
        k = 2**exponent
        ell = (k + 4) // 5
        n = 2 * k
        j = 2 * ell - 3
        assert 5 * ell == k + 4
        assert j % 2 == 1
        for scale in divisors_power_two(exponent + 1):
            assert n % scale == 0
            assert j % scale != 0
            scales += 1
        assert math.gcd(n, j) == 1
        rows += 1

    official_k = 2**40
    official_ell = (official_k + 4) // 5
    official_j = 2 * official_ell - 3
    assert official_ell == 219902325556
    assert official_j == 439804651109
    print(
        "L1_FPC5_SHARP_DYADIC_QUOTIENT_ABSENCE_PASS "
        f"rows={rows} scales={scales} official_j={official_j}"
    )


if __name__ == "__main__":
    main()
