#!/usr/bin/env python3
"""Certify the bounded sharp product windows for all residual cofactors."""

from __future__ import annotations

from fractions import Fraction
from math import isqrt


COUNT = 64
MEAN = Fraction(18)
CAP = Fraction(144)
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
DENOMINATOR = 2**192

# cofactor: (first excluded variance, old inclusive upper endpoint)
WINDOWS = {
    2: (286, 350),
    4: (268, 314),
    8: (256, 278),
    16: (218, 244),
    32: (172, 208),
    64: (132, 174),
    256: (62, 104),
    512: (36, 68),
    514: (36, 68),
}
EXPECTED_CLOSEST = {
    2: (286, 1, 62),
    4: (268, 1, 62),
    8: (256, 1, 62),
    16: (218, 0, 63),
    32: (172, 0, 63),
    64: (132, 0, 63),
    256: (62, 0, 63),
    512: (36, 0, 63),
    514: (36, 0, 63),
}


def sqrt_interval(value: Fraction) -> tuple[Fraction, Fraction]:
    scaled_square = value.numerator * DENOMINATOR**2 // value.denominator
    floor = isqrt(scaled_square)
    lower = Fraction(floor, DENOMINATOR)
    if floor * floor * value.denominator == value.numerator * DENOMINATOR**2:
        return lower, lower
    return lower, Fraction(floor + 1, DENOMINATOR)


def product_intervals(
    variance: int,
) -> list[tuple[int, int, Fraction, Fraction]]:
    rows = []
    total_sum = COUNT * MEAN
    total_square = COUNT * variance
    for capped_count in range(8):
        residual_count = COUNT - capped_count
        residual_mean = (total_sum - capped_count * CAP) / residual_count
        residual_square = (
            total_square
            - capped_count * (CAP - MEAN) ** 2
            - residual_count * (residual_mean - MEAN) ** 2
        )
        if residual_square < 0:
            continue
        residual_variance = residual_square / residual_count
        if residual_variance == 0:
            value = CAP**capped_count * residual_mean**residual_count
            rows.append((capped_count, residual_count, value, value))
            continue
        for lower_count in range(1, residual_count):
            upper_count = residual_count - lower_count
            lower_delta_square = residual_variance * upper_count / lower_count
            upper_delta_square = residual_variance * lower_count / upper_count
            if lower_delta_square >= residual_mean**2:
                continue
            if upper_delta_square > (CAP - residual_mean) ** 2:
                continue
            lower_delta = sqrt_interval(lower_delta_square)
            upper_delta = sqrt_interval(upper_delta_square)
            low_value = (
                residual_mean - lower_delta[1],
                residual_mean - lower_delta[0],
            )
            high_value = (
                residual_mean + upper_delta[0],
                residual_mean + upper_delta[1],
            )
            assert 0 < low_value[0] <= low_value[1]
            assert high_value[0] <= high_value[1] <= CAP + Fraction(1, DENOMINATOR)
            rows.append(
                (
                    capped_count,
                    lower_count,
                    CAP**capped_count
                    * low_value[0] ** lower_count
                    * high_value[0] ** upper_count,
                    CAP**capped_count
                    * low_value[1] ** lower_count
                    * high_value[1] ** upper_count,
                )
            )
    assert rows
    return rows


def main() -> None:
    total_comparisons = 0
    summaries = []
    for cofactor, (onset, old_upper) in WINDOWS.items():
        target = cofactor * P_MIN
        closest: tuple[Fraction, int, int, int] | None = None
        comparisons = 0
        for variance in range(onset, old_upper + 1, 2):
            for capped_count, lower_count, _, product_upper in product_intervals(variance):
                assert product_upper < target
                margin = Fraction(target, 1) / product_upper
                row = (margin, variance, capped_count, lower_count)
                if closest is None or row < closest:
                    closest = row
                comparisons += 1
        assert closest is not None
        assert closest[1:] == EXPECTED_CLOSEST[cofactor]

        boundary = onset - 2
        boundary_survives = any(
            product_lower > target
            for _, _, product_lower, _ in product_intervals(boundary)
        )
        assert boundary_survives
        total_comparisons += comparisons
        summaries.append(
            f"m{cofactor}:V{boundary}:comparisons{comparisons}:"
            f"closest{closest[1]}/{closest[2]}/{closest[3]}"
        )

    print(
        "E1_PROFILE_36_BOUNDED_VARIANCE_PRODUCT_ENVELOPE_PASS "
        f"cofactors={len(WINDOWS)} comparisons={total_comparisons} "
        f"summaries={';'.join(summaries)}"
    )


if __name__ == "__main__":
    main()
