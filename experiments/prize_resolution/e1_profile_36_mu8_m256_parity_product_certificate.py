#!/usr/bin/env python3
"""Certify every parity-adaptive product chamber for cofactor 256."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from math import isqrt
from pathlib import Path

import modal


COUNT = 64
MEAN = Fraction(18)
GLOBAL_CAP = Fraction(144)
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
DENOMINATOR = 2**192
COFACTOR = 256
CHORD_WEIGHTS = {1, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
EXPECTED_LIVE = {
    "E3q3L3",
    "E5q1L3", "E5q5L5",
    "E6q6L6",
    "E7q3L5", "E7q7L7",
    "E8q8L8",
    "E9q1L3", "E9q1L5", "E9q5L7", "E9q9L9",
    "E10q6L8", "E10q10L10",
    "E11q3L5", "E11q3L7", "E11q7L9", "E11q11L11",
    "E12q8L10", "E12q12L12",
    "E13q1L7", "E13q5L7", "E13q5L9", "E13q9L11", "E13q13L13",
    "E14q6L8", "E14q6L10", "E14q10L12", "E14q14L14",
    "E15q3L9", "E15q7L9", "E15q7L11", "E15q11L13", "E15q15L15",
    "E16q8L10", "E16q8L12", "E16q12L14",
    "E17q5L11", "E17q9L11", "E17q9L13", "E17q13L15",
    "E18q10L14", "E18q14L16",
    "E19q11L15", "E19q15L17",
    "E20q12L16",
}
EXPECTED_EXCLUDED = {
    "E13q1L5", "E15q3L7",
    "E17q1L5", "E17q1L7", "E17q1L9", "E17q5L9",
    "E18q6L10", "E18q6L12", "E18q10L12",
    "E19q3L7", "E19q3L9", "E19q3L11", "E19q7L11", "E19q7L13",
    "E19q11L13",
    "E20q8L12", "E20q8L14", "E20q12L14",
    "E21q1L7", "E21q1L9", "E21q1L11", "E21q5L9", "E21q5L11",
    "E21q5L13", "E21q9L13", "E21q9L15", "E21q13L15", "E21q13L17",
    "E22q6L10", "E22q6L12", "E22q6L14", "E22q10L14", "E22q10L16",
    "E22q14L16", "E22q14L18",
    "E23q3L9", "E23q3L11", "E23q3L13", "E23q7L11", "E23q7L13",
    "E23q7L15", "E23q11L15", "E23q11L17", "E23q15L17", "E23q15L19",
}

app = modal.App("e1-profile-36-mu8-m256-parity-product-certificate")
image = modal.Image.debian_slim()


def sqrt_interval(value: Fraction) -> tuple[Fraction, Fraction]:
    scaled_square = value.numerator * DENOMINATOR**2 // value.denominator
    floor = isqrt(scaled_square)
    lower = Fraction(floor, DENOMINATOR)
    if floor * floor * value.denominator == value.numerator * DENOMINATOR**2:
        return lower, lower
    return lower, Fraction(floor + 1, DENOMINATOR)


def product_intervals(
    variance: int, cap_override: int
) -> list[tuple[Fraction, Fraction]]:
    cap = min(GLOBAL_CAP, Fraction(cap_override))
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
            rows.append((value, value))
            continue
        for lower_count in range(1, residual_count):
            upper_count = residual_count - lower_count
            lower_square = residual_variance * upper_count / lower_count
            upper_square = residual_variance * lower_count / upper_count
            if lower_square >= residual_mean**2:
                continue
            if upper_square > (cap - residual_mean) ** 2:
                continue
            lower_delta = sqrt_interval(lower_square)
            upper_delta = sqrt_interval(upper_square)
            low_value = (
                residual_mean - lower_delta[1],
                residual_mean - lower_delta[0],
            )
            high_value = (
                residual_mean + upper_delta[0],
                residual_mean + upper_delta[1],
            )
            rows.append(
                (
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


def parity_l1_values(energy: int) -> dict[int, set[int]]:
    values: dict[int, set[int]] = {}
    for fours in range(energy // 16 + 1):
        for threes in range((energy - 16 * fours) // 9 + 1):
            for twos in range((energy - 16 * fours - 9 * threes) // 4 + 1):
                ones = energy - 16 * fours - 9 * threes - 4 * twos
                odd_weight = ones + threes
                l1_norm = ones + 2 * twos + 3 * threes + 4 * fours
                if odd_weight in CHORD_WEIGHTS:
                    values.setdefault(odd_weight, set()).add(l1_norm)
    return values


def compute() -> dict[str, object]:
    target = COFACTOR * P_MIN
    comparisons = 0
    live = []
    excluded = []
    for energy in range(2, 24):
        for odd_weight, l1_values in sorted(parity_l1_values(energy).items()):
            for l1_norm in sorted(l1_values):
                rows = product_intervals(2 * energy, 18 + 2 * l1_norm)
                is_excluded = all(upper < target for _, upper in rows)
                survives = any(lower > target for lower, _ in rows)
                assert is_excluded != survives
                comparisons += len(rows)
                record = f"E{energy}q{odd_weight}L{l1_norm}"
                (excluded if is_excluded else live).append(record)
    assert comparisons == 27_176
    assert set(live) == EXPECTED_LIVE
    assert set(excluded) == EXPECTED_EXCLUDED
    assert len(live) == len(EXPECTED_LIVE) == 45
    assert len(excluded) == len(EXPECTED_EXCLUDED) == 45
    return {
        "schema": "e1-profile-36-mu8-m256-parity-product-v1",
        "comparisons": comparisons,
        "live": live,
        "excluded": excluded,
    }


@app.function(image=image, cpu=1.0, memory=128, timeout=60, max_containers=1)
def certify() -> dict[str, object]:
    return compute()


@app.local_entrypoint()
def main(
    output: str = (
        "experiments/prize_resolution/"
        "e1_profile_36_mu8_m256_parity_product_result.json"
    ),
) -> None:
    packet = certify.remote()
    packet["source_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    output_path = Path(output)
    output_path.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    print(
        "E1_PROFILE_36_MU8_M256_PARITY_PRODUCT_PASS "
        f"comparisons={packet['comparisons']} live={len(packet['live'])} "
        f"excluded={len(packet['excluded'])} output={output}"
    )


if __name__ == "__main__":
    main()
