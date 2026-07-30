#!/usr/bin/env python3
"""Independent Ramanujan-sum replay of the 32 product classes."""

from __future__ import annotations

from collections import Counter
from math import comb


def ramanujan_power_two(order: int, residue: int) -> int:
    assert order >= 2 and order & (order - 1) == 0
    if residue % order == 0:
        return order // 2
    if residue % (order // 2) == 0:
        return -(order // 2)
    return 0


def class_size(residue: int) -> int:
    correction = (
        -6435 * ramanujan_power_two(2, residue)
        - 35 * ramanujan_power_two(4, residue)
        - 3 * ramanujan_power_two(8, residue)
        + ramanujan_power_two(16, residue)
        - ramanujan_power_two(32, residue)
    )
    numerator = comb(31, 17) + correction
    assert numerator % 32 == 0
    return numerator // 32


def main() -> None:
    spectrum = [class_size(residue) for residue in range(32)]
    assert Counter(spectrum) == Counter(
        {8_287_155: 16, 8_286_755: 8, 8_286_751: 5, 8_286_750: 3}
    )
    assert sum(spectrum) == 265_182_525
    assert max(spectrum) == 8_287_155
    print("M31_QUOTIENT_ROTATION_PRODUCT_SPECTRUM_AUDIT_PASS")


if __name__ == "__main__":
    main()
