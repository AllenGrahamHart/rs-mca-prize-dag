#!/usr/bin/env python3
"""Verify the N=256 E=36 quotient-Schur exclusion."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e36_quotient_schur_exclusion"
E37_PARENT = "e1_n256_s16_e37_quotient_schur_exclusion"
VARIANCE_PARENT = "e1_n256_s16_sparse_l1_variance_exclusion"
NORM_PARENT = "collision_norm_criterion"
E1_TARGET = "e1_official_prime_exception_control"
UNIVERSAL_TARGET = "unsafe_crossing_family_instantiation"
EXPECTED_PIN = {
    "bbb_checker_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e36_bbb64_census_check.py",
    "bbb_checker_file_sha256": "8c82f08e5ad97962db2e9d8f2949c551a7b9fd43a02d3fdd5df49eb1cb3364c4",
    "bbb_launcher_file": "background/nodes/e1_n256_s16_e36_quotient_schur_exclusion/verify_bbb64_remote.py",
    "bbb_launcher_file_sha256": "2a627f4ceea60511cd7a255d151f3dcdb71df675ae56599acf2a14b157fdc0aa",
    "bbb_result_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e36_bbb64_census_result.json",
    "bbb_result_file_sha256": "197a007e584dc126717f51ad809433f01656f91319918fe2942c60960d5a9820",
    "bbb_source_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e36_bbb64_census.cpp",
    "bbb_source_file_sha256": "4443d96ac583105c8f96a7798503eff061c59cf6c7416a258dab0ab2f0c239ce",
    "census_checker_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e36_mod16_quotient_census_check.py",
    "census_checker_file_sha256": "789b65b3adfeac8b00d57d02714a176dc905e118cb60c0bc58b6c7154a40ee86",
    "census_launcher_file": "background/nodes/e1_n256_s16_e36_quotient_schur_exclusion/verify_census_remote.py",
    "census_launcher_file_sha256": "a60fd646e4855dba2bcb37e95a0219973301caa042463c527e31852ed5644c87",
    "census_result_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e36_mod16_quotient_census_result.json",
    "census_result_file_sha256": "123abe42baefc23d3dd3c46eeafa113c0eab09fc4cae6a66bf7139943ce97f67",
    "census_source_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e36_mod16_quotient_census.cpp",
    "census_source_file_sha256": "c3791fa8c6fc0919f07bd87098dec0438c57a87b6f308108ae8cc6151fe7b390",
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "e37_parent_file": "background/nodes/e1_n256_s16_e37_quotient_schur_exclusion/statement.md",
    "e37_parent_file_sha256": "fb44fe2f6460c9ef668419892b909fdb5e5396d522c164e0ab95da6eec8a272e",
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
        range(41), range(11), range(5), range(3), range(2), range(2)
    ):
        l1_norm = sum((index + 1) * count for index, count in enumerate(counts))
        energy = sum(
            (index + 1) ** 2 * count for index, count in enumerate(counts)
        )
        if energy == 36 and l1_norm <= 20 and sum(counts) <= 20:
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
    assert "allocations=8144380 bbb32=174" in census_checker.stdout
    assert '"profile0_order128_inner2": 2344' in census_checker.stdout
    assert '"profile0_order128_outside_inner2": 2208' in census_checker.stdout
    assert '"profile0_order64_inner2": 2332' in census_checker.stdout
    assert '"profile1_order128_outside_inner2": 2000' in census_checker.stdout
    assert '"profile1_order64_inner2": 1924' in census_checker.stdout

    bbb_checker = subprocess.run(
        ["python3", str(ROOT / pin["bbb_checker_file"])],
        check=True,
        capture_output=True,
        text=True,
        timeout=15,
    )
    assert "sets=7888725 maximum=174" in bbb_checker.stdout

    parent_path = ROOT / pin["variance_parent_verify_file"]
    spec = importlib.util.spec_from_file_location("e1_sparse_parent", parent_path)
    assert spec is not None and spec.loader is not None
    parent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(parent)
    slack_table = parent.relaxed_minimum_energy_by_slack(22)
    assert slack_table[18] == 40 > 36
    assert slack_table[22] == 36

    profiles = sorted(energy_profiles(), reverse=True)
    assert len(profiles) == 26
    assert profiles[:4] == [
        (2616, (4, 8, 0, 0, 0, 0), 20),
        (2448, (0, 9, 0, 0, 0, 0), 18),
        (2440, (7, 5, 1, 0, 0, 0), 20),
        (2288, (10, 2, 2, 0, 0, 0), 20),
    ]
    assert 2440 - 650 - 2 + 556 == 2344
    assert max(2208, 2344, 2332, 2000, 1924, 2344, 2288) == 2344 < 2377
    assert 16 + 2 * 20 == 56
    assert 56**32 < 2**250

    log_2_lower, log_2_upper = atanh_log_bounds(Fraction(2), 8)
    log_8_over_7_lower, log_8_over_7_upper = atanh_log_bounds(Fraction(8, 7), 8)
    log_64_over_57_lower, log_64_over_57_upper = atanh_log_bounds(
        Fraction(64, 57), 8
    )
    margin_2377_lower = (
        Fraction(-505_401, 2_544_224) * log_2_upper
        + Fraction(75_337, 79_507) * log_8_over_7_lower
        + Fraction(4_170, 79_507) * log_64_over_57_lower
        + Fraction(1_073, 210_786)
    )
    margin_2378_upper = (
        Fraction(-505_273, 2_544_224) * log_2_lower
        + Fraction(75_339, 79_507) * log_8_over_7_upper
        + Fraction(4_168, 79_507) * log_64_over_57_upper
        + Fraction(1_240, 245_917)
    )
    assert margin_2377_lower > 0
    assert margin_2378_upper < 0

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {entry["id"]: entry["status"] for entry in dag["nodes"]}
    statements = {entry["id"]: entry.get("statement", "") for entry in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[E37_PARENT] == "PROVED"
    assert statuses[VARIANCE_PARENT] == "PROVED"
    assert statuses[NORM_PARENT] == "PROVED"
    for dependency in (E37_PARENT, VARIANCE_PARENT, NORM_PARENT):
        assert (dependency, NODE, "req") in edges
    assert (NODE, E1_TARGET, "ev") in edges
    assert (NODE, UNIVERSAL_TARGET, "ev") in edges
    assert "M_3<=2344<2377" in statements[NODE]
    assert "V<=70" in statements[NODE]

    print(
        "E1_N256_S16_E36_QUOTIENT_SCHUR_EXCLUSION_PASS "
        "profiles=26 allocations=8144380 bbb64_sets=7888725 "
        "m3_cap=2344 residual_max=70"
    )


if __name__ == "__main__":
    main()
