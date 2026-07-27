#!/usr/bin/env python3
"""Verify the N=256 E=34 three-profile reduction."""

from __future__ import annotations

import hashlib
import json
import math
import subprocess
from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e34_three_profile_reduction"
E35_PARENT = "e1_n256_s16_e35_quotient_schur_exclusion"
E36_PARENT = "e1_n256_s16_e36_quotient_schur_exclusion"
VARIANCE_PARENT = "e1_n256_s16_sparse_l1_variance_exclusion"
NORM_PARENT = "collision_norm_criterion"
E1_TARGET = "e1_official_prime_exception_control"
UNIVERSAL_TARGET = "unsafe_crossing_family_instantiation"


def atanh_log_bounds(value: Fraction, terms: int) -> tuple[Fraction, Fraction]:
    parameter = (value - 1) / (value + 1)
    lower = 2 * sum(
        parameter ** (2 * index + 1) / (2 * index + 1)
        for index in range(terms)
    )
    degree = 2 * terms + 1
    remainder = 2 * parameter**degree / (degree * (1 - parameter * parameter))
    return lower, lower + remainder


def layer_triple_cap(counts: tuple[int, ...]) -> int:
    sizes = [
        2 * sum(counts[level:])
        for level in range(len(counts))
        if sum(counts[level:])
    ]
    return sum(
        min(
            first * second - min(first, second),
            first * third - min(first, third),
            second * third - min(second, third),
        )
        for first, second, third in product(sizes, repeat=3)
    )


def energy_profiles() -> list[tuple[int, tuple[int, ...], int]]:
    profiles = []
    for counts in product(
        range(35), range(9), range(4), range(3), range(2), range(2)
    ):
        energy = sum((index + 1) ** 2 * count for index, count in enumerate(counts))
        l1_norm = sum((index + 1) * count for index, count in enumerate(counts))
        if energy == 34 and l1_norm <= 20 and sum(counts) <= 20:
            profiles.append((layer_triple_cap(counts), counts, l1_norm))
    return profiles


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    for key, path in pin.items():
        if not key.endswith("_file"):
            continue
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[
            key + "_sha256"
        ]

    nested = subprocess.run(
        ["python3", str(ROOT / pin["nested_checker_file"]), "--survivors"],
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert "tested=42413558" in nested.stdout
    assert '"profile4_order128": 1880' in nested.stdout
    assert '"profile4_order64": 1828' in nested.stdout
    assert '"profile5_order128": 1922' in nested.stdout
    assert '"profile5_order64": 1922' in nested.stdout

    coupled = subprocess.run(
        ["python3", str(ROOT / pin["coupled_checker_file"])],
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert '"order128_best_outside_four": 1942' in coupled.stdout
    assert '"order64_best_refined": 1942' in coupled.stdout
    assert "support_tested=7927920 support_max=1536" in coupled.stdout

    profiles = sorted(energy_profiles(), reverse=True)
    assert len(profiles) == 24
    assert profiles[:7] == [
        (2428, (6, 7, 0, 0, 0, 0), 20),
        (2264, (9, 4, 1, 0, 0, 0), 20),
        (2252, (2, 8, 0, 0, 0, 0), 18),
        (2124, (12, 1, 2, 0, 0, 0), 20),
        (2084, (5, 5, 1, 0, 0, 0), 18),
        (1956, (14, 1, 0, 1, 0, 0), 20),
        (1940, (8, 2, 2, 0, 0, 0), 18),
    ]
    assert max(1940, 1880, 1828, 1922, 1942, 1536) == 1942 < 1947
    assert math.comb(15, 8) == 6435
    assert math.comb(55, 2) - math.comb(23, 2) == 1232
    assert 6435 * 1232 == 7_927_920
    assert 56**32 < 2**250

    log_2_lower, log_2_upper = atanh_log_bounds(Fraction(2), 8)
    log_8_over_7_lower, log_8_over_7_upper = atanh_log_bounds(Fraction(8, 7), 8)
    log_64_over_57_lower, log_64_over_57_upper = atanh_log_bounds(
        Fraction(64, 57), 8
    )
    margin_1947_lower = (
        Fraction(-530_489, 2_544_224) * log_2_upper
        + Fraction(74_945, 79_507) * log_8_over_7_lower
        + Fraction(4_562, 79_507) * log_64_over_57_lower
        + Fraction(17_729, 1_475_502)
    )
    margin_1948_upper = (
        Fraction(-530_361, 2_544_224) * log_2_lower
        + Fraction(74_947, 79_507) * log_8_over_7_upper
        + Fraction(4_560, 79_507) * log_64_over_57_upper
        + Fraction(2_943, 245_917)
    )
    assert margin_1947_lower > 0
    assert margin_1948_upper < 0

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {entry["id"]: entry["status"] for entry in dag["nodes"]}
    statements = {entry["id"]: entry.get("statement", "") for entry in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    for dependency in (E35_PARENT, E36_PARENT, VARIANCE_PARENT, NORM_PARENT):
        assert statuses[dependency] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, E1_TARGET, "ev") in edges
    assert (NODE, UNIVERSAL_TARGET, "ev") in edges
    assert "(6,7),(9,4,1),(12,1,2)" in statements[NODE]
    assert "M_3<=1942<1947" in statements[NODE]

    print(
        "E1_N256_S16_E34_THREE_PROFILE_REDUCTION_PASS "
        "profiles=24 quotient=42413558 refined=809474 "
        "supports=7927920 m3_cap=1942 residual=3"
    )


if __name__ == "__main__":
    main()
