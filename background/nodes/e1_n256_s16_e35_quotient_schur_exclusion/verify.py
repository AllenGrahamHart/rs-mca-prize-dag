#!/usr/bin/env python3
"""Verify the N=256 E=35 quotient-Schur exclusion."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e35_quotient_schur_exclusion"
E36_PARENT = "e1_n256_s16_e36_quotient_schur_exclusion"
VARIANCE_PARENT = "e1_n256_s16_sparse_l1_variance_exclusion"
NORM_PARENT = "collision_norm_criterion"
E1_TARGET = "e1_official_prime_exception_control"
UNIVERSAL_TARGET = "unsafe_crossing_family_instantiation"
EXPECTED_PIN = {
    "census_checker_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e35_mod16_quotient_census_check.py",
    "census_checker_file_sha256": "f5689ee7b9394fad1cfaac5f29f76158e7903c19f2caaac5ee0f54d5f9bc4f0a",
    "census_launcher_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/verify_e35_mod16_quotient_census_remote.py",
    "census_launcher_file_sha256": "3698c54883b36def2ede9a827daf4479ef17df7801990fe231a5e03b32d65a06",
    "census_result_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e35_mod16_quotient_census_result.json",
    "census_result_file_sha256": "32be5f7f2dde3088a9f9650a3d3013c8fddbb19e6e9d81f5b760cf50d45b3f39",
    "census_source_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e35_mod16_quotient_census.cpp",
    "census_source_file_sha256": "935f8e10d8698de7d397c8299ae763375d8d3f247862236d41513ebefb3fa739",
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "coupling_checker_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e35_high_outer_coupling_check.py",
    "coupling_checker_file_sha256": "5e22c630ea57a5440bd1c3bfcf5ef87da37321aca813eb8e12d54125238271a7",
    "e36_parent_file": "background/nodes/e1_n256_s16_e36_quotient_schur_exclusion/statement.md",
    "e36_parent_file_sha256": "ad17af846bba63cf7a2d1bd3f9f318696507d91a9cbcec50460872abc80559e7",
    "variance_parent_verify_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/verify.py",
    "variance_parent_verify_file_sha256": "57b7a0f2d8590bda9234f4fb5bc0a573afd56200436458121767489fc5091f8e",
}


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
        range(40), range(11), range(5), range(3), range(2), range(2)
    ):
        l1_norm = sum((index + 1) * count for index, count in enumerate(counts))
        energy = sum(
            (index + 1) ** 2 * count for index, count in enumerate(counts)
        )
        if energy == 35 and l1_norm <= 19 and sum(counts) <= 19:
            profiles.append((layer_triple_cap(counts), counts, l1_norm))
    return profiles


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for file_key, path in pin.items():
        if not file_key.endswith("_file"):
            continue
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[
            file_key + "_sha256"
        ]

    census_checker = subprocess.run(
        ["python3", str(ROOT / pin["census_checker_file"])],
        check=True,
        capture_output=True,
        text=True,
        timeout=15,
    )
    assert "allocations=2946287" in census_checker.stdout
    assert '"profile0_order128_inner2": 2152' in census_checker.stdout
    assert '"profile0_order128_outside_inner2": 2010' in census_checker.stdout
    assert '"profile0_order64_inner2": 2100' in census_checker.stdout
    assert '"profile1_order128_outside_inner2": 460' in census_checker.stdout
    assert '"profile1_order64_outside_inner2": 454' in census_checker.stdout

    coupling_checker = subprocess.run(
        ["python3", str(ROOT / pin["coupling_checker_file"])],
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert "high=4/0 nested=276 maximum=2054 global=2162" in (
        coupling_checker.stdout
    )

    parent_path = ROOT / pin["variance_parent_verify_file"]
    spec = importlib.util.spec_from_file_location("e1_sparse_parent", parent_path)
    assert spec is not None and spec.loader is not None
    parent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(parent)
    slack_table = parent.relaxed_minimum_energy_by_slack(25)
    assert slack_table[21] == 39 > 35
    assert slack_table[25] == 35

    profiles = sorted(energy_profiles(), reverse=True)
    assert len(profiles) == 21
    assert profiles[:4] == [
        (2430, (3, 8, 0, 0, 0, 0), 19),
        (2258, (6, 5, 1, 0, 0, 0), 19),
        (2110, (9, 2, 2, 0, 0, 0), 19),
        (2098, (2, 6, 1, 0, 0, 0), 17),
    ]
    assert 2258 - 552 - 2 == 1704
    assert 458 + 1704 == 2162
    assert 454 + 1704 == 2158
    assert max(2152, 2100, 2162, 2158, 2054, 2110) == 2162
    assert 16 + 2 * 19 == 54
    assert 54**32 < 2**250

    log_2_lower, log_2_upper = atanh_log_bounds(Fraction(2), 8)
    log_8_over_7_lower, log_8_over_7_upper = atanh_log_bounds(Fraction(8, 7), 8)
    log_64_over_57_lower, log_64_over_57_upper = atanh_log_bounds(
        Fraction(64, 57), 8
    )
    margin_2162_lower = (
        Fraction(-517_945, 2_544_224) * log_2_upper
        + Fraction(75_141, 79_507) * log_8_over_7_lower
        + Fraction(4_366, 79_507) * log_64_over_57_lower
        + Fraction(6_310, 737_751)
    )
    margin_2163_upper = (
        Fraction(-517_817, 2_544_224) * log_2_lower
        + Fraction(75_143, 79_507) * log_8_over_7_upper
        + Fraction(4_364, 79_507) * log_64_over_57_upper
        + Fraction(4_183, 491_834)
    )
    assert margin_2162_lower > 0
    assert margin_2163_upper < 0

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {entry["id"]: entry["status"] for entry in dag["nodes"]}
    statements = {entry["id"]: entry.get("statement", "") for entry in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[E36_PARENT] == "PROVED"
    assert statuses[VARIANCE_PARENT] == "PROVED"
    assert statuses[NORM_PARENT] == "PROVED"
    for dependency in (E36_PARENT, VARIANCE_PARENT, NORM_PARENT):
        assert (dependency, NODE, "req") in edges
    assert (NODE, E1_TARGET, "ev") in edges
    assert (NODE, UNIVERSAL_TARGET, "ev") in edges
    assert "M_3<=2162" in statements[NODE]
    assert "V<=68" in statements[NODE]

    print(
        "E1_N256_S16_E35_QUOTIENT_SCHUR_EXCLUSION_PASS "
        "profiles=21 allocations=2946287 high_outer=4 nested=276 "
        "m3_cap=2162 residual_max=68"
    )


if __name__ == "__main__":
    main()
