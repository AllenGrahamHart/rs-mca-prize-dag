#!/usr/bin/env python3
"""Exact subset-product DP for the M31 quotient-rotation specialization."""

from __future__ import annotations

from collections import Counter
from math import comb


EXPECTED = Counter(
    {
        8_287_155: 16,
        8_286_755: 8,
        8_286_751: 5,
        8_286_750: 3,
    }
)


def main() -> None:
    dp = [[0] * 32 for _ in range(18)]
    dp[0][0] = 1
    for exponent in range(1, 32):
        for size in range(min(17, exponent), 0, -1):
            for residue in range(32):
                dp[size][(residue + exponent) % 32] += dp[size - 1][residue]

    spectrum = dp[17]
    assert sum(spectrum) == comb(31, 17) == 265_182_525
    assert Counter(spectrum) == EXPECTED
    assert max(spectrum) == 8_287_155
    assert (comb(31, 17) + 31) // 32 == 8_286_954
    assert 16_777_215 - max(spectrum) == 8_490_060
    assert 16_777_215 - 2 * max(spectrum) == 202_905
    assert 2**20 + 2**16 + 1911 == 1_116_023
    print("M31_QUOTIENT_ROTATION_PRODUCT_SPECTRUM_PASS max=8287155")


if __name__ == "__main__":
    main()
