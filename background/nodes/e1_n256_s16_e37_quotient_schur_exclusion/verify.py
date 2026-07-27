#!/usr/bin/env python3
"""Verify the N=256 E=37 quotient-Schur exclusion."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e37_quotient_schur_exclusion"
E38_PARENT = "e1_n256_s16_e38_quotient_schur_exclusion"
VARIANCE_PARENT = "e1_n256_s16_sparse_l1_variance_exclusion"
NORM_PARENT = "collision_norm_criterion"
E1_TARGET = "e1_official_prime_exception_control"
UNIVERSAL_TARGET = "unsafe_crossing_family_instantiation"
EXPECTED_PIN = {
    "census_checker_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e37_mod16_quotient_census_check.py",
    "census_checker_file_sha256": "3f5bdb56a702f23b06afcc0575b8d18eef92d62144e5922beb0bb3d975b71567",
    "census_launcher_file": "background/nodes/e1_n256_s16_e37_quotient_schur_exclusion/verify_census_remote.py",
    "census_launcher_file_sha256": "75e7c8b926cfa4931b67a671ae0fe07658076462def2cbd37beab43d058fd913",
    "census_result_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e37_mod16_quotient_census_result.json",
    "census_result_file_sha256": "3801e1a3d58222c0fb50599800ed886f106d101f2c7129924eef0588ab516c91",
    "census_source_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e37_mod16_quotient_census.cpp",
    "census_source_file_sha256": "cfc9a7796666cc27b50077e9547e4f7896118824ff90e02ec2908bbcd1c9618a",
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "e38_parent_file": "background/nodes/e1_n256_s16_e38_quotient_schur_exclusion/statement.md",
    "e38_parent_file_sha256": "2f724a00648604f9f5f0bcdbe358d2b7a9e515b63b6193119698e0fc0e89bcc5",
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
        range(42), range(11), range(5), range(3), range(2), range(2)
    ):
        l1_norm = sum((index + 1) * count for index, count in enumerate(counts))
        energy = sum(
            (index + 1) ** 2 * count for index, count in enumerate(counts)
        )
        if energy == 37 and l1_norm <= 21 and sum(counts) <= 21:
            profiles.append((layer_triple_cap(counts), counts, l1_norm))
    return profiles


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for file_key, hash_key in (
        ("census_checker_file", "census_checker_file_sha256"),
        ("census_launcher_file", "census_launcher_file_sha256"),
        ("census_result_file", "census_result_file_sha256"),
        ("census_source_file", "census_source_file_sha256"),
        ("collision_norm_file", "collision_norm_file_sha256"),
        ("e38_parent_file", "e38_parent_file_sha256"),
        ("variance_parent_verify_file", "variance_parent_verify_file_sha256"),
    ):
        assert hashlib.sha256((ROOT / pin[file_key]).read_bytes()).hexdigest() == pin[
            hash_key
        ]

    checker = subprocess.run(
        ["python3", str(ROOT / pin["census_checker_file"])],
        check=True,
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert "allocations=19732753 bbb32=174" in checker.stdout
    assert "profile0_order128_inner4\": 2560" in checker.stdout
    assert "profile0_order128_not4\": 2576" in checker.stdout

    parent_path = ROOT / pin["variance_parent_verify_file"]
    spec = importlib.util.spec_from_file_location("e1_sparse_parent", parent_path)
    assert spec is not None and spec.loader is not None
    parent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(parent)
    slack_table = parent.relaxed_minimum_energy_by_slack(21)
    assert slack_table[15] == 41 > 37
    assert slack_table[19] == 37

    profiles = sorted(energy_profiles(), reverse=True)
    assert len(profiles) == 29
    assert profiles[:4] == [
        (2810, (5, 8, 0, 0, 0, 0), 21),
        (2630, (8, 5, 1, 0, 0, 0), 21),
        (2630, (1, 9, 0, 0, 0, 0), 19),
        (2474, (11, 2, 2, 0, 0, 0), 21),
    ]
    assert 2630 - 756 - 2 + 678 == 2550
    assert max(2576, 2560, 2372, 2168, 2550, 2474) == 2576 < 2592
    assert 16 + 2 * 21 == 58
    assert 58**32 < 2**250

    log_2_lower, log_2_upper = atanh_log_bounds(Fraction(2), 8)
    log_8_over_7_lower, log_8_over_7_upper = atanh_log_bounds(Fraction(8, 7), 8)
    log_64_over_57_lower, log_64_over_57_upper = atanh_log_bounds(
        Fraction(64, 57), 8
    )
    margin_2592_lower = (
        Fraction(-492_857, 2_544_224) * log_2_upper
        + Fraction(75_533, 79_507) * log_8_over_7_lower
        + Fraction(3_974, 79_507) * log_64_over_57_lower
        + Fraction(1_201, 737_751)
    )
    margin_2593_upper = (
        Fraction(-492_729, 2_544_224) * log_2_lower
        + Fraction(75_535, 79_507) * log_8_over_7_upper
        + Fraction(3_972, 79_507) * log_64_over_57_upper
        + Fraction(111, 70_262)
    )
    assert margin_2592_lower > 0
    assert margin_2593_upper < 0

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {entry["id"]: entry["status"] for entry in dag["nodes"]}
    statements = {entry["id"]: entry.get("statement", "") for entry in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[E38_PARENT] == "PROVED"
    assert statuses[VARIANCE_PARENT] == "PROVED"
    assert statuses[NORM_PARENT] == "PROVED"
    for dependency in (E38_PARENT, VARIANCE_PARENT, NORM_PARENT):
        assert (dependency, NODE, "req") in edges
    assert (NODE, E1_TARGET, "ev") in edges
    assert (NODE, UNIVERSAL_TARGET, "ev") in edges
    assert "M_3<=2576<2592" in statements[NODE]
    assert "V<=72" in statements[NODE]

    print(
        "E1_N256_S16_E37_QUOTIENT_SCHUR_EXCLUSION_PASS "
        "profiles=29 allocations=19732753 m3_cap=2576 residual_max=72"
    )


if __name__ == "__main__":
    main()
