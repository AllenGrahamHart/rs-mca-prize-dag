#!/usr/bin/env python3
"""Exact arithmetic checks for the FPC5 support-shortening cap."""

from math import comb


def shortening_cap(length: int, weight: int, half_distance: int) -> tuple[int, int]:
    best = comb(length, weight)
    best_depth = -1
    numerator_choose = 1
    denominator_choose = 1
    for depth in range(weight + 1):
        residual = weight - depth
        if residual < half_distance:
            base = 1
        else:
            delta = residual * residual - (length - depth) * (
                residual - half_distance
            )
            if delta <= 0:
                base = None
            else:
                base = (length - depth) * half_distance // delta
        if base is not None:
            value = numerator_choose * base // denominator_choose
            if value < best:
                best = value
                best_depth = depth
        if depth < weight:
            numerator_choose = (
                numerator_choose * (length - depth) // (depth + 1)
            )
            denominator_choose = (
                denominator_choose * (weight - depth) // (depth + 1)
            )
    return best, best_depth


def main() -> None:
    # The rate-1/16, M=61 fixed-background strip.
    expected = {
        286: (10127, 4),
        287: (7396, 4),
        288: (5492, 3),
        289: (3723, 3),
        290: (2815, 3),
        291: (1839, 2),
        292: (1326, 2),
    }
    for defect, answer in expected.items():
        assert shortening_cap(511, 511 - defect, 125) == answer

    # The owner-free d=248 shell has H=375 and sigma=127.
    assert shortening_cap(511, 248, 127) == (5402, 4)

    # Complementing the support does not change the cap input.
    for defect in range(286, 293):
        weight = min(defect, 511 - defect)
        assert weight == 511 - defect

    print(
        "L1_FPC5_GRS_SHELL_CONSTANT_WEIGHT_SHORTENING_CAP_PASS "
        "checked_shells=8 max_depth=4"
    )


if __name__ == "__main__":
    main()
