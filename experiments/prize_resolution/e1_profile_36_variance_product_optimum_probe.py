#!/usr/bin/env python3
"""Probe the sharp fixed-mean/fixed-variance product envelope for S=18."""

from __future__ import annotations

import math


COUNT = 64
MEAN = 18.0
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128


def maximum_log_ratio(variance: int) -> tuple[float, int, float, float]:
    best = (-math.inf, -1, 0.0, 0.0)
    for lower_count in range(1, COUNT):
        upper_count = COUNT - lower_count
        lower = MEAN - math.sqrt(variance * upper_count / lower_count)
        if lower <= 0:
            continue
        upper = MEAN + math.sqrt(variance * lower_count / upper_count)
        score = (
            lower_count * math.log(lower / MEAN)
            + upper_count * math.log(upper / MEAN)
        )
        if score > best[0]:
            best = (score, lower_count, lower, upper)
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
    for variance in range(2, 38, 2):
        score, lower_count, lower, upper = maximum_log_ratio(variance)
        print(
            f"V={variance} max_log_ratio={score:.15f} "
            f"lower_count={lower_count} lower={lower:.12f} upper={upper:.12f}"
        )
    print("E1_PROFILE_36_VARIANCE_PRODUCT_OPTIMUM_PROBE_DONE")


if __name__ == "__main__":
    main()
