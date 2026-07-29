#!/usr/bin/env python3
"""Probe parity-adaptive product exclusions for cofactor 64."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path

import modal


COUNT = 64
MEAN = Fraction(18)
GLOBAL_CAP = Fraction(144)
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
DENOMINATOR = 2**192
COFACTOR = 64
CHORD_WEIGHTS = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
MAX_CLASSES = 36
OUTPUT = Path(
    "experiments/prize_resolution/e1_profile_36_mu6_m64_parity_product_result.json"
)

app = modal.App("e1-profile-36-mu6-m64-parity-product-probe")
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
            rows.append(
                (
                    cap**capped_count
                    * (residual_mean - lower_delta[1]) ** lower_count
                    * (residual_mean + upper_delta[0]) ** upper_count,
                    cap**capped_count
                    * (residual_mean - lower_delta[0]) ** lower_count
                    * (residual_mean + upper_delta[1]) ** upper_count,
                )
            )
    assert rows
    return rows


def parity_l1_values(energy: int) -> dict[int, set[int]]:
    values: dict[int, set[int]] = {}

    def visit(
        magnitude: int,
        remaining: int,
        odd_weight: int,
        l1_norm: int,
        classes: int,
    ) -> None:
        if magnitude == 1:
            count = remaining
            q = odd_weight + count
            if classes + count <= MAX_CLASSES and q in CHORD_WEIGHTS:
                values.setdefault(q, set()).add(l1_norm + count)
            return
        square = magnitude * magnitude
        for count in range(min(remaining // square, MAX_CLASSES - classes) + 1):
            visit(
                magnitude - 1,
                remaining - count * square,
                odd_weight + (count if magnitude % 2 else 0),
                l1_norm + count * magnitude,
                classes + count,
            )

    visit(isqrt(energy), energy, 0, 0, 0)
    return values


def encode(record: tuple[int, int, int]) -> str:
    return f"E{record[0]}q{record[1]}L{record[2]}"


def compute() -> dict[str, object]:
    target = COFACTOR * P_MIN
    cache: dict[tuple[int, int], tuple[str, int]] = {}
    live: list[tuple[int, int, int]] = []
    excluded: list[tuple[int, int, int]] = []
    ambiguous: list[tuple[int, int, int]] = []
    comparisons = 0
    for energy in range(2, 66):
        for odd_weight, l1_values in sorted(parity_l1_values(energy).items()):
            for l1_norm in sorted(l1_values):
                key = (energy, l1_norm)
                if key not in cache:
                    rows = product_intervals(2 * energy, 18 + 2 * l1_norm)
                    is_excluded = all(upper < target for _, upper in rows)
                    survives = any(lower > target for lower, _ in rows)
                    status = (
                        "excluded" if is_excluded
                        else "live" if survives
                        else "ambiguous"
                    )
                    cache[key] = (status, len(rows))
                    comparisons += len(rows)
                status = cache[key][0]
                record = (energy, odd_weight, l1_norm)
                {"live": live, "excluded": excluded, "ambiguous": ambiguous}[status].append(record)
    assert not ambiguous
    live_counts = {
        energy: sum(row[0] == energy for row in live)
        for energy in sorted({row[0] for row in live})
    }
    minimum_live_l1 = {
        energy: min(l1_norm for row_energy, _, l1_norm in live if row_energy == energy)
        for energy in live_counts
    }
    q_frontiers = {
        odd_weight: max(energy for energy, q, _ in live if q == odd_weight)
        for odd_weight in sorted({row[1] for row in live})
    }
    q_radii = {
        odd_weight: max((energy - odd_weight) // 4 for energy, q, _ in live if q == odd_weight)
        for odd_weight in q_frontiers
    }
    max_live = max(live_counts)
    assert len(live) + len(excluded) == 1092
    assert len(cache) == 510 and comparisons == 128228
    assert len(live) == 255 and len(excluded) == 837 and max_live == 46
    assert q_frontiers == {
        2: 34, 3: 35, 4: 36, 5: 37, 6: 38, 7: 39, 8: 44,
        9: 45, 10: 42, 11: 43, 12: 44, 13: 45, 14: 46, 15: 43,
    }
    return {
        "schema": "e1-profile-36-mu6-m64-parity-product-v1",
        "complete": True,
        "cofactor": COFACTOR,
        "energy_range": [2, 65],
        "maximum_classes": MAX_CLASSES,
        "denominator_bits": 192,
        "records": len(live) + len(excluded),
        "cache_entries": len(cache),
        "comparisons": comparisons,
        "live": [encode(record) for record in live],
        "excluded": [encode(record) for record in excluded],
        "live_counts": live_counts,
        "minimum_live_l1": minimum_live_l1,
        "q_frontiers": q_frontiers,
        "q_radii": q_radii,
        "max_live_energy": max_live,
    }


@app.function(image=image, cpu=1.0, memory=256, timeout=120, max_containers=1)
def probe() -> dict[str, object]:
    return compute()


@app.local_entrypoint()
def main() -> None:
    result = probe.remote()
    source = Path(__file__)
    result["source_sha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "E1_PROFILE_36_MU6_M64_PARITY_PRODUCT_PASS "
        f"records={result['records']} comparisons={result['comparisons']} "
        f"live={len(result['live'])} excluded={len(result['excluded'])} "
        f"max_live_E={result['max_live_energy']} output={OUTPUT}"
    )


if __name__ == "__main__":
    main()
