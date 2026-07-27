#!/usr/bin/env python3
"""Verify the N=256 E=32 profile/parity/diameter reduction."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e32_profile_parity_diameter_reduction"
E33 = "e1_n256_s16_e33_endpoint_exclusion"
VARIANCE = "e1_n256_s16_sparse_l1_variance_exclusion"
SIGNED = "e1_n256_s16_signed_chord_collision_gate"
NORM = "collision_norm_criterion"
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")

EXPECTED_PIN = {
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "e33_endpoint_file": "background/nodes/e1_n256_s16_e33_endpoint_exclusion/statement.md",
    "e33_endpoint_file_sha256": "5b778a73533ea32385d1beb61f74e3acd40a6e5c402d8e4b1a1ffb3dc1129c65",
    "signed_chord_file": "background/nodes/e1_n256_s16_signed_chord_collision_gate/statement.md",
    "signed_chord_file_sha256": "926f9c94a0b5dd0830b7e37fafcd96f570dd93802de16061c802546e466e3157",
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


def add_forms(*forms: tuple[Fraction, Fraction, Fraction]) -> tuple[Fraction, Fraction, Fraction]:
    return tuple(sum(form[index] for form in forms) for index in range(3))  # type: ignore[return-value]


def scale_form(scale: Fraction, form: tuple[Fraction, Fraction, Fraction]) -> tuple[Fraction, Fraction, Fraction]:
    return tuple(scale * value for value in form)  # type: ignore[return-value]


def layer_cap(counts: tuple[int, ...]) -> int:
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


def energy_profiles() -> list[tuple[int, tuple[int, ...], int, int]]:
    answer = []
    for counts in product(range(33), range(9), range(4), range(3), range(2), range(2)):
        energy = sum((index + 1) ** 2 * count for index, count in enumerate(counts))
        l1_norm = sum((index + 1) * count for index, count in enumerate(counts))
        if energy == 32 and l1_norm <= 18 and sum(counts) <= 18:
            answer.append((layer_cap(counts), counts, l1_norm, sum(counts[0::2])))
    return sorted(answer, reverse=True)


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]

    parent_path = ROOT / pin["variance_parent_verify_file"]
    spec = importlib.util.spec_from_file_location("variance_parent", parent_path)
    assert spec is not None and spec.loader is not None
    parent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(parent)
    slack_table = parent.relaxed_minimum_energy_by_slack(26)
    slack_trace = tuple(
        (l1_norm, 32 + 66 - 4 * l1_norm, slack_table[32 + 66 - 4 * l1_norm])
        for l1_norm in range(24, 17, -1)
    )
    assert slack_trace == (
        (24, 2, 56), (23, 6, 52), (22, 10, 48), (21, 14, 44),
        (20, 18, 40), (19, 22, 36), (18, 26, 32),
    )

    profiles = energy_profiles()
    assert len(profiles) == 18
    assert profiles[:8] == [
        (2072, (4, 7, 0, 0, 0, 0), 18, 4),
        (1920, (0, 8, 0, 0, 0, 0), 16, 0),
        (1916, (7, 4, 1, 0, 0, 0), 18, 8),
        (1784, (10, 1, 2, 0, 0, 0), 18, 12),
        (1760, (3, 5, 1, 0, 0, 0), 16, 4),
        (1624, (12, 1, 0, 1, 0, 0), 18, 12),
        (1624, (6, 2, 2, 0, 0, 0), 16, 8),
        (1496, (2, 3, 2, 0, 0, 0), 14, 4),
    ]

    hermite = (
        (Fraction(48735, 79507), Fraction(30772, 79507), Fraction(-3445, 1849)),
        (Fraction(4788, 79507), Fraction(-4788, 79507), Fraction(301253, 1475502)),
        (Fraction(-213, 79507), Fraction(213, 79507), Fraction(-4243, 737751)),
        (Fraction(2, 79507), Fraction(-2, 79507), Fraction(71, 1475502)),
    )
    expected_forms = []
    for moment in (1517, 1518):
        expected_forms.append(add_forms(
            hermite[0],
            scale_form(Fraction(16), hermite[1]),
            scale_form(Fraction(320), hermite[2]),
            scale_form(Fraction(7168 + moment), hermite[3]),
        ))
    assert expected_forms == [
        (Fraction(74553, 79507), Fraction(4954, 79507), Fraction(-27947, 1475502)),
        (Fraction(74555, 79507), Fraction(4952, 79507), Fraction(-4646, 245917)),
    ]

    log_2_lower, log_2_upper = atanh_log_bounds(Fraction(2), 8)
    log_8_over_7_lower, log_8_over_7_upper = atanh_log_bounds(Fraction(8, 7), 8)
    log_64_over_57_lower, log_64_over_57_upper = atanh_log_bounds(Fraction(64, 57), 8)
    assert (
        Fraction(-555577, 2544224) * log_2_upper
        + Fraction(74553, 79507) * log_8_over_7_lower
        + Fraction(4954, 79507) * log_64_over_57_lower
        + Fraction(27947, 1475502)
    ) > 0
    assert (
        Fraction(-555449, 2544224) * log_2_lower
        + Fraction(74555, 79507) * log_8_over_7_upper
        + Fraction(4952, 79507) * log_64_over_57_upper
        + Fraction(4646, 245917)
    ) < 0

    above_threshold = [profile for profile in profiles if profile[0] > 1517]
    assert len(above_threshold) == 7
    survivors = [profile for profile in above_threshold if profile[3] <= 6]
    assert [profile[1] for profile in survivors] == [
        (4, 7, 0, 0, 0, 0),
        (0, 8, 0, 0, 0, 0),
        (3, 5, 1, 0, 0, 0),
    ]

    diameter_ledgers = set()
    for light_light in (0, 2):
        for heavy_heavy in range(2):
            for heavy_light in range(4):
                if heavy_light > min(3 - 2 * heavy_heavy, 4 - 2 * light_light):
                    continue
                square_mass = light_light + 4 * heavy_light + 16 * heavy_heavy
                cross_sum = (32 - 102 + square_mass) // 2
                diameter_ledgers.add((square_mass, cross_sum, light_light))
    assert diameter_ledgers == {
        (0, -35, 0), (2, -34, 2), (4, -33, 0), (8, -31, 0),
        (12, -29, 0), (16, -27, 0), (18, -26, 2), (20, -25, 0),
    }

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in (E33, VARIANCE, SIGNED, NORM):
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "(4,7),(0,8),(3,5,1)" in nodes[NODE]["statement"]
    assert "M_3=1517" in nodes[NODE]["statement"]

    print(
        "E1_N256_S16_E32_PROFILE_PARITY_DIAMETER_REDUCTION_PASS "
        "profiles=18 above=7 survivors=3 threshold=1517 diameter_ledgers=8"
    )


if __name__ == "__main__":
    main()
