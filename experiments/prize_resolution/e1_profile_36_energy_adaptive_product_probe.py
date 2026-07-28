#!/usr/bin/env python3
"""Certify the exact product envelope with the integer-energy cap y <= 18+V."""

from __future__ import annotations

from fractions import Fraction
from math import isqrt

import modal


COUNT = 64
MEAN = Fraction(18)
GLOBAL_CAP = Fraction(144)
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
DENOMINATOR = 2**192
WINDOWS = {
    # cofactor: (first excluded variance, old endpoint, surviving boundary)
    256: (48, 60, 46),
    514: (24, 34, 22),
}
EXPECTED_PARITY_EXCLUSIONS = {
    (7, 3): False,
    (7, 7): False,
    (8, 4): False,
    (8, 8): False,
    (9, 1): True,
    (9, 5): False,
    (9, 9): False,
    (10, 2): True,
    (10, 6): False,
    (10, 10): False,
    (11, 3): True,
    (11, 7): True,
    (11, 11): False,
}

app = modal.App("e1-profile-36-energy-adaptive-product-certificate")
image = modal.Image.debian_slim()


def sqrt_interval(value: Fraction) -> tuple[Fraction, Fraction]:
    scaled_square = value.numerator * DENOMINATOR**2 // value.denominator
    floor = isqrt(scaled_square)
    lower = Fraction(floor, DENOMINATOR)
    if floor * floor * value.denominator == value.numerator * DENOMINATOR**2:
        return lower, lower
    return lower, Fraction(floor + 1, DENOMINATOR)


def product_intervals(
    variance: int,
    cap_override: int | None = None,
) -> list[tuple[int, int, Fraction, Fraction]]:
    cap = min(
        GLOBAL_CAP,
        Fraction(cap_override) if cap_override is not None else MEAN + variance,
    )
    rows = []
    total_sum = COUNT * MEAN
    total_square = COUNT * variance
    for capped_count in range(COUNT):
        residual_count = COUNT - capped_count
        residual_mean = (total_sum - capped_count * cap) / residual_count
        if residual_mean <= 0 or residual_mean > cap:
            continue
        residual_square = (
            total_square
            - capped_count * (cap - MEAN) ** 2
            - residual_count * (residual_mean - MEAN) ** 2
        )
        if residual_square < 0:
            continue
        residual_variance = residual_square / residual_count
        if residual_variance == 0:
            value = cap**capped_count * residual_mean**residual_count
            rows.append((capped_count, residual_count, value, value))
            continue
        for lower_count in range(1, residual_count):
            upper_count = residual_count - lower_count
            lower_delta_square = residual_variance * upper_count / lower_count
            upper_delta_square = residual_variance * lower_count / upper_count
            if lower_delta_square >= residual_mean**2:
                continue
            if upper_delta_square > (cap - residual_mean) ** 2:
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
            assert high_value[0] <= high_value[1] <= cap + Fraction(1, DENOMINATOR)
            rows.append(
                (
                    capped_count,
                    lower_count,
                    cap**capped_count
                    * low_value[0] ** lower_count
                    * high_value[0] ** upper_count,
                    cap**capped_count
                    * low_value[1] ** lower_count
                    * high_value[1] ** upper_count,
                )
            )
    assert rows
    return rows


def parity_l1_bounds(energy: int) -> dict[int, int]:
    bounds: dict[int, int] = {}
    for threes in range(energy // 9 + 1):
        for twos in range((energy - 9 * threes) // 4 + 1):
            ones = energy - 9 * threes - 4 * twos
            odd_weight = ones + threes
            l1_norm = ones + 2 * twos + 3 * threes
            bounds[odd_weight] = max(bounds.get(odd_weight, 0), l1_norm)
    # Exact multiplicity one makes the binary autocorrelation product nonzero.
    return {odd_weight: bound for odd_weight, bound in bounds.items() if odd_weight}


def compute() -> str:
    summaries = []
    comparisons = 0
    for cofactor, (onset, old_upper, boundary) in WINDOWS.items():
        target = cofactor * P_MIN
        for variance in range(onset, old_upper + 1, 2):
            rows = product_intervals(variance)
            assert all(product_upper < target for _, _, _, product_upper in rows)
            comparisons += len(rows)
        boundary_rows = product_intervals(boundary)
        assert any(
            product_lower > target for _, _, product_lower, _ in boundary_rows
        )
        comparisons += len(boundary_rows)
        summaries.append(
            f"m{cofactor}:survive<={boundary}:exclude={onset}..{old_upper}"
        )
    parity_l1 = {
        7: {3: 5, 7: 7},
        8: {4: 6, 8: 8},
        9: {1: 5, 5: 7, 9: 9},
        10: {2: 6, 6: 8, 10: 10},
        11: {3: 7, 7: 9, 11: 11},
    }
    assert {energy: parity_l1_bounds(energy) for energy in range(7, 12)} == parity_l1
    target = 514 * P_MIN
    strata = []
    for energy, q_rows in parity_l1.items():
        for odd_weight, l1_bound in q_rows.items():
            rows = product_intervals(2 * energy, 18 + 2 * l1_bound)
            excluded = all(product_upper < target for _, _, _, product_upper in rows)
            survives = any(product_lower > target for _, _, product_lower, _ in rows)
            assert excluded != survives
            assert excluded == EXPECTED_PARITY_EXCLUSIONS[(energy, odd_weight)]
            comparisons += len(rows)
            strata.append(
                f"E{energy}q{odd_weight}L{l1_bound}:"
                f"{'excluded' if excluded else 'survives'}"
            )
    return (
        "E1_PROFILE_36_ENERGY_ADAPTIVE_PRODUCT_CERTIFICATE_PASS "
        f"comparisons={comparisons} summaries={';'.join(summaries)} "
        f"strata={';'.join(strata)}"
    )


@app.function(image=image, cpu=1.0, memory=128, timeout=60, max_containers=1)
def probe() -> str:
    return compute()


@app.local_entrypoint()
def main() -> None:
    print(probe.remote())
