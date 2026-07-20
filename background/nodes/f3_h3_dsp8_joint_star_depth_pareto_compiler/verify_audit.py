#!/usr/bin/env python3
"""Independent abstract-profile audit of the DSP8 Pareto ladder."""

from __future__ import annotations

from fractions import Fraction
from math import ceil


ROWS = {
    6: (Fraction(8, 11), Fraction(4), 2, 1),
    7: (Fraction(8, 11), Fraction(4), 2, 1),
    8: (Fraction(5, 9), Fraction(5, 4), 3, 2),
    9: (Fraction(5, 9), Fraction(5, 4), 3, 2),
    10: (Fraction(4, 9), Fraction(3, 4), 5, 3),
    11: (Fraction(4, 9), Fraction(3, 4), 5, 3),
    12: (Fraction(7, 18), Fraction(7, 12), 6, 4),
    13: (Fraction(7, 18), Fraction(7, 12), 6, 4),
    14: (Fraction(16, 47), Fraction(8, 17), 7, 5),
    15: (Fraction(16, 47), Fraction(8, 17), 7, 5),
    16: (Fraction(9, 29), Fraction(9, 22), 8, 6),
}


def floors(size: int) -> tuple[int, int]:
    free = (size * (size - 4) + 1) // 2 - 2 * size - 6
    antipodal = (size * (size - 2) + 1) // 2 - 4 * (size - 1) - 8
    return free, antipodal


def main() -> None:
    checked = 0
    endpoints = []
    for cutoff, (free_ratio, antipodal_ratio, free_degree, antipodal_degree) in ROWS.items():
        minimum = 7 + ceil(Fraction(cutoff + 1, 2))
        for excess in range(cutoff + 1, 513):
            size_minimum = 7 + (excess + 1) // 2
            for size in range(size_minimum, size_minimum + 96):
                free, antipodal = floors(size)
                assert excess <= free_ratio * free
                assert excess <= antipodal_ratio * antipodal
                assert ceil(Fraction(2 * free, size)) >= free_degree
                assert ceil(Fraction(2 * antipodal, size - 1)) >= antipodal_degree
                checked += 1

        free, antipodal = floors(minimum)
        endpoint_excess = 2 * (minimum - 7)
        assert Fraction(endpoint_excess, free) == free_ratio
        assert Fraction(endpoint_excess, antipodal) == antipodal_ratio
        endpoints.append((cutoff, minimum, free, antipodal))

    assert endpoints[-1] == (16, 16, 58, 44)
    print(
        "AUDIT_F3_H3_DSP8_JOINT_STAR_DEPTH_PARETO_COMPILER_PASS "
        f"profiles={checked} endpoints={len(endpoints)}"
    )


if __name__ == "__main__":
    main()
