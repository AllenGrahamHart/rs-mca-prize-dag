#!/usr/bin/env python3
"""Certify parity-adaptive product chambers for cofactor 32."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path
import re

import modal


COUNT = 64
MEAN = Fraction(18)
GLOBAL_CAP = Fraction(144)
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
DENOMINATOR = 2**192
COFACTOR = 32
CHORD_WEIGHTS = set(range(3, 16))
MAX_CLASSES = 36
OUTPUT = Path(
    "experiments/prize_resolution/e1_profile_36_mu5_m32_parity_product_result.json"
)
HEADER = Path(
    "experiments/prize_resolution/e1_profile_36_mu5_m32_product_live.hpp"
)

app = modal.App("e1-profile-36-mu5-m32-parity-product")
image = modal.Image.debian_slim()


def sqrt_interval(value: Fraction) -> tuple[Fraction, Fraction]:
    scaled_square = value.numerator * DENOMINATOR**2 // value.denominator
    floor = isqrt(scaled_square)
    lower = Fraction(floor, DENOMINATOR)
    if floor * floor * value.denominator == value.numerator * DENOMINATOR**2:
        return lower, lower
    return lower, Fraction(floor + 1, DENOMINATOR)


def product_intervals(variance: int, cap_override: int) -> list[tuple[Fraction, Fraction]]:
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
            rows.append((
                cap**capped_count
                * (residual_mean - lower_delta[1]) ** lower_count
                * (residual_mean + upper_delta[0]) ** upper_count,
                cap**capped_count
                * (residual_mean - lower_delta[0]) ** lower_count
                * (residual_mean + upper_delta[1]) ** upper_count,
            ))
    assert rows
    return rows


def parity_l1_values(energy: int) -> dict[int, set[int]]:
    values: dict[int, set[int]] = {}

    def visit(magnitude: int, remaining: int, q: int, l1: int, classes: int) -> None:
        if magnitude == 1:
            count = remaining
            odd_weight = q + count
            if classes + count <= MAX_CLASSES and odd_weight in CHORD_WEIGHTS:
                values.setdefault(odd_weight, set()).add(l1 + count)
            return
        square = magnitude * magnitude
        for count in range(min(remaining // square, MAX_CLASSES - classes) + 1):
            visit(
                magnitude - 1,
                remaining - count * square,
                q + (count if magnitude % 2 else 0),
                l1 + count * magnitude,
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
    for energy in range(2, 86):
        for odd_weight, l1_values in sorted(parity_l1_values(energy).items()):
            for l1_norm in sorted(l1_values):
                key = (energy, l1_norm)
                if key not in cache:
                    rows = product_intervals(2 * energy, 18 + 2 * l1_norm)
                    is_excluded = all(upper < target for _, upper in rows)
                    survives = any(lower > target for lower, _ in rows)
                    status = "excluded" if is_excluded else "live" if survives else "ambiguous"
                    cache[key] = (status, len(rows))
                    comparisons += len(rows)
                record = (energy, odd_weight, l1_norm)
                {"live": live, "excluded": excluded, "ambiguous": ambiguous}[
                    cache[key][0]
                ].append(record)
    assert not ambiguous
    live_counts = {
        energy: sum(row[0] == energy for row in live)
        for energy in sorted({row[0] for row in live})
    }
    minimum_live_l1 = {
        energy: min(l1 for row_energy, _, l1 in live if row_energy == energy)
        for energy in live_counts
    }
    q_frontiers = {
        q: max(energy for energy, odd_weight, _ in live if odd_weight == q)
        for q in sorted({row[1] for row in live})
    }
    q_radii = {
        q: max((energy - q) // 4 for energy, odd_weight, _ in live if odd_weight == q)
        for q in q_frontiers
    }
    return {
        "schema": "e1-profile-36-mu5-m32-parity-product-v1",
        "complete": True,
        "cofactor": COFACTOR,
        "energy_range": [2, 85],
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
        "max_live_energy": max(live_counts),
    }


@app.function(image=image, cpu=1.0, memory=256, timeout=180, max_containers=1)
def probe() -> dict[str, object]:
    return compute()


@app.local_entrypoint()
def main() -> None:
    result = probe.remote()
    cases = []
    for record in result["live"]:
        match = re.fullmatch(r"E(\d+)q(\d+)L(\d+)", record)
        assert match
        energy, odd_weight, l1_norm = map(int, match.groups())
        cases.append(f"        case {(energy << 16) | (odd_weight << 8) | l1_norm}:\n")
    header = (
        "#pragma once\n\n"
        "inline bool m32_product_live(int energy, int odd_weight, int l1_norm) {\n"
        "    switch ((energy << 16) | (odd_weight << 8) | l1_norm) {\n"
        + "".join(cases)
        + "            return true;\n"
        "        default:\n"
        "            return false;\n"
        "    }\n"
        "}\n"
    )
    HEADER.write_text(header)
    result["source_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result["header_sha256"] = hashlib.sha256(HEADER.read_bytes()).hexdigest()
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "E1_PROFILE_36_MU5_M32_PARITY_PRODUCT_PASS "
        f"records={result['records']} comparisons={result['comparisons']} "
        f"live={len(result['live'])} excluded={len(result['excluded'])} "
        f"max_live_E={result['max_live_energy']} "
        f"q_frontiers={result['q_frontiers']} q_radii={result['q_radii']} "
        f"header={HEADER} output={OUTPUT}"
    )


if __name__ == "__main__":
    main()
