#!/usr/bin/env python3
"""Probe the sharp product envelope with the exact conjugate-square cap."""

from __future__ import annotations

import math


COUNT = 64
MEAN = 18.0
CAP = 144.0
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128


def maximum_log_ratio(variance: int) -> tuple[float, int, int, float, float]:
    best = (-math.inf, -1, -1, 0.0, 0.0)
    total_sum = COUNT * MEAN
    total_centered_square = COUNT * variance
    for capped_count in range(8):
        residual_count = COUNT - capped_count
        residual_mean = (total_sum - capped_count * CAP) / residual_count
        residual_centered_at_18 = (
            total_centered_square - capped_count * (CAP - MEAN) ** 2
        )
        residual_square = (
            residual_centered_at_18
            - residual_count * (residual_mean - MEAN) ** 2
        )
        if residual_square < -1e-9:
            continue
        residual_variance = max(0.0, residual_square / residual_count)
        if residual_variance == 0:
            score = (
                capped_count * math.log(CAP / MEAN)
                + residual_count * math.log(residual_mean / MEAN)
            )
            if score > best[0]:
                best = (score, capped_count, residual_count, residual_mean, residual_mean)
            continue
        for lower_count in range(1, residual_count):
            upper_count = residual_count - lower_count
            lower = residual_mean - math.sqrt(
                residual_variance * upper_count / lower_count
            )
            upper = residual_mean + math.sqrt(
                residual_variance * lower_count / upper_count
            )
            if lower <= 0 or upper > CAP + 1e-9:
                continue
            score = (
                capped_count * math.log(CAP / MEAN)
                + lower_count * math.log(lower / MEAN)
                + upper_count * math.log(upper / MEAN)
            )
            if score > best[0]:
                best = (score, capped_count, lower_count, lower, upper)
    return best


def main() -> None:
    denominator = 18**64
    for cofactor in (1024, 1028, 1538, 512, 514, 256, 64, 32, 16, 8, 4, 2):
        target_log_ratio = math.log(cofactor * P_MIN / denominator)
        onset = None
        row = None
        for variance in range(2, 352, 2):
            optimum = maximum_log_ratio(variance)
            if optimum[0] < target_log_ratio:
                onset = variance
                row = optimum
                break
        print(
            f"m={cofactor} target_log_ratio={target_log_ratio:.15f} "
            f"onset={onset} optimizer={row}"
        )
    print("E1_PROFILE_36_BOUNDED_VARIANCE_PRODUCT_OPTIMUM_PROBE_DONE")


if __name__ == "__main__":
    main()
