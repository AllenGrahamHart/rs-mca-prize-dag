#!/usr/bin/env python3
"""Verify the N=256 E=38 quotient-Schur exclusion."""

from __future__ import annotations

import hashlib
import json
import subprocess
from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e38_quotient_schur_exclusion"
VARIANCE_PARENT = "e1_n256_s16_sparse_l1_variance_exclusion"
SUBFIELD_PARENT = "e1_n256_s16_autocorrelation_subfield_exclusion"
NORM_PARENT = "collision_norm_criterion"
E1_TARGET = "e1_official_prime_exception_control"
UNIVERSAL_TARGET = "unsafe_crossing_family_instantiation"
EXPECTED_PIN = {
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "census_checker_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e38_mod16_quotient_census_check.py",
    "census_checker_file_sha256": "43390ae9c162410a51a1580d873f7de230fbe278804409715972ab5c3a4be110",
    "census_launcher_file": "background/nodes/e1_n256_s16_e38_quotient_schur_exclusion/verify_census_remote.py",
    "census_launcher_file_sha256": "38019632af3a1f1be3bfce3d5715b85c0650ee2fcf1573356ea24982aa6b69ec",
    "census_result_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e38_mod16_quotient_census_result.json",
    "census_result_file_sha256": "afc13704508a4592f1fbdbd7d3573302b8a8b2118cf736591dc29f1ae5dfbe7a",
    "census_source_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e38_mod16_quotient_census.cpp",
    "census_source_file_sha256": "48bfb6b3fa250ba4798d78cdc531f1e6fdd1c29a2c5a05f6f756cd88152453c5",
    "subfield_parent_file": "background/nodes/e1_n256_s16_autocorrelation_subfield_exclusion/statement.md",
    "subfield_parent_file_sha256": "4f33a2ada08bd29de1152f502a7678868b31f0829a3903dfa530e973cd5331de",
    "variance_parent_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/statement.md",
    "variance_parent_file_sha256": "5dad1a8acbe7f8d4f1db89771371203fe257f65c8f7ea5d4b03e3df4ada32c12",
    "variance_parent_verify_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/verify.py",
    "variance_parent_verify_file_sha256": "57b7a0f2d8590bda9234f4fb5bc0a573afd56200436458121767489fc5091f8e",
}


def atanh_log_bounds(value: Fraction, terms: int) -> tuple[Fraction, Fraction]:
    assert value > 1
    parameter = (value - 1) / (value + 1)
    lower = 2 * sum(
        parameter ** (2 * index + 1) / (2 * index + 1)
        for index in range(terms)
    )
    degree = 2 * terms + 1
    remainder = (
        2
        * parameter**degree
        / (degree * (1 - parameter * parameter))
    )
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
        range(43), range(11), range(5), range(3), range(2), range(2)
    ):
        l1_norm = sum((index + 1) * count for index, count in enumerate(counts))
        energy = sum(
            (index + 1) ** 2 * count for index, count in enumerate(counts)
        )
        if energy == 38 and l1_norm <= 22 and sum(counts) <= 21:
            profiles.append((layer_triple_cap(counts), counts, l1_norm))
    return profiles


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for file_key, hash_key in (
        ("collision_norm_file", "collision_norm_file_sha256"),
        ("census_checker_file", "census_checker_file_sha256"),
        ("census_launcher_file", "census_launcher_file_sha256"),
        ("census_result_file", "census_result_file_sha256"),
        ("census_source_file", "census_source_file_sha256"),
        ("subfield_parent_file", "subfield_parent_file_sha256"),
        ("variance_parent_file", "variance_parent_file_sha256"),
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
    assert "allocations=43153083" in checker.stdout
    packet = json.loads((ROOT / pin["census_result_file"]).read_text())
    maxima = {
        key: value["best"]["best"] for key, value in packet["summaries"].items()
    }
    assert maxima == {
        "profile0_order128": 2782,
        "profile0_order64": 2760,
        "profile1_order128": 2580,
        "profile1_order64": 2422,
        "profile2_order128": 840,
        "profile2_order64": 840,
    }

    profiles = sorted(energy_profiles(), reverse=True)
    assert len(profiles) == 32
    assert profiles[:4] == [
        (3012, (6, 8, 0, 0, 0, 0), 22),
        (2828, (9, 5, 1, 0, 0, 0), 22),
        (2820, (2, 9, 0, 0, 0, 0), 20),
        (2668, (12, 2, 2, 0, 0, 0), 22),
    ]
    assert 2828 - 870 - 2 + 840 == 2796
    assert max(2782, 2760, 2580, 2422, 2796, 2668) == 2796 < 2806

    log_2_lower, log_2_upper = atanh_log_bounds(Fraction(2), 8)
    log_8_over_7_lower, _ = atanh_log_bounds(Fraction(8, 7), 8)
    log_64_over_57_lower, _ = atanh_log_bounds(Fraction(64, 57), 8)
    _, log_57_over_14_upper = atanh_log_bounds(Fraction(57, 14), 8)
    cubic_coefficient_lower = (
        Fraction(71, 1_475_502)
        - Fraction(2, 79_507) * log_57_over_14_upper
    )
    assert cubic_coefficient_lower > 0
    margin_at_2806 = (
        Fraction(-480_441, 2_544_224) * log_2_upper
        + Fraction(75_727, 79_507) * log_8_over_7_lower
        + Fraction(3_780, 79_507) * log_64_over_57_lower
        - Fraction(1_318, 737_751)
    )
    assert log_2_lower < log_2_upper
    assert margin_at_2806 > 0

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {entry["id"]: entry["status"] for entry in dag["nodes"]}
    statements = {entry["id"]: entry.get("statement", "") for entry in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[VARIANCE_PARENT] == "PROVED"
    assert statuses[SUBFIELD_PARENT] == "PROVED"
    assert statuses[NORM_PARENT] == "PROVED"
    assert statuses[E1_TARGET] == "TARGET"
    assert statuses[UNIVERSAL_TARGET] == "TARGET"
    for dependency in (VARIANCE_PARENT, SUBFIELD_PARENT, NORM_PARENT):
        assert (dependency, NODE, "req") in edges
    assert (NODE, E1_TARGET, "ev") in edges
    assert (NODE, UNIVERSAL_TARGET, "ev") in edges
    assert "M_3<=2796<2806" in statements[NODE]
    assert "V<=74" in statements[NODE]

    print(
        "E1_N256_S16_E38_QUOTIENT_SCHUR_EXCLUSION_PASS "
        "profiles=32 allocations=43153083 m3_cap=2796 residual_max=74"
    )


if __name__ == "__main__":
    main()
