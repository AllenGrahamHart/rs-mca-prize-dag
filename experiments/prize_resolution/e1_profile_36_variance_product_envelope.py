#!/usr/bin/env python3
"""Certify the sharp S=18 product envelope at the two short cofactors."""

from __future__ import annotations

from fractions import Fraction
from math import isqrt


COUNT = 64
MEAN = 18
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
COFACTOR = 1024
DENOMINATOR = 2**192


def sqrt_interval(value: Fraction) -> tuple[Fraction, Fraction]:
    scaled_square = value.numerator * DENOMINATOR**2 // value.denominator
    floor = isqrt(scaled_square)
    lower = Fraction(floor, DENOMINATOR)
    if floor * floor * value.denominator == value.numerator * DENOMINATOR**2:
        return lower, lower
    return lower, Fraction(floor + 1, DENOMINATOR)


def product_interval(variance: int, lower_count: int) -> tuple[Fraction, Fraction]:
    upper_count = COUNT - lower_count
    lower_delta_bounds = sqrt_interval(
        Fraction(variance * upper_count, lower_count)
    )
    upper_delta_bounds = sqrt_interval(
        Fraction(variance * lower_count, upper_count)
    )

    lower_value_lower = Fraction(MEAN) - lower_delta_bounds[1]
    lower_value_upper = Fraction(MEAN) - lower_delta_bounds[0]
    upper_value_lower = Fraction(MEAN) + upper_delta_bounds[0]
    upper_value_upper = Fraction(MEAN) + upper_delta_bounds[1]
    assert 0 < lower_value_lower <= lower_value_upper
    assert upper_value_lower <= upper_value_upper
    return (
        lower_value_lower**lower_count * upper_value_lower**upper_count,
        lower_value_upper**lower_count * upper_value_upper**upper_count,
    )


def main() -> None:
    target = COFACTOR * P_MIN
    comparisons = 0
    closest_margin: Fraction | None = None
    closest_case: tuple[int, int] | None = None
    for variance in range(14, 36, 2):
        for lower_count in range(1, COUNT):
            lower_delta_square = Fraction(
                variance * (COUNT - lower_count), lower_count
            )
            if lower_delta_square >= MEAN**2:
                continue
            _, product_upper = product_interval(variance, lower_count)
            assert product_upper < target
            margin = Fraction(target, 1) / product_upper
            if closest_margin is None or margin < closest_margin:
                closest_margin = margin
                closest_case = (variance, lower_count)
            comparisons += 1

    boundary_lower, _ = product_interval(12, 63)
    assert boundary_lower > target
    assert closest_margin is not None and closest_case is not None
    print(
        "E1_PROFILE_36_VARIANCE_PRODUCT_ENVELOPE_PASS "
        f"comparisons={comparisons} variance_range=14..34 "
        f"cofactor={COFACTOR} closest_case={closest_case} "
        f"closest_margin_gt_one={closest_margin > 1} "
        "boundary_V12_survives=true"
    )


if __name__ == "__main__":
    main()
