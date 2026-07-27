#!/usr/bin/env python3
"""Verify the N=256 E=33 profile/parity/diameter reduction."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e33_profile_parity_diameter_reduction"
E34 = "e1_n256_s16_e34_endpoint_exclusion"
VARIANCE = "e1_n256_s16_sparse_l1_variance_exclusion"
SIGNED = "e1_n256_s16_signed_chord_collision_gate"
NORM = "collision_norm_criterion"
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")

EXPECTED_PIN = {
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "e34_endpoint_file": "background/nodes/e1_n256_s16_e34_endpoint_exclusion/statement.md",
    "e34_endpoint_file_sha256": "ec89d4a47312cf14a607b12ba89014c7747639f8273a32317c6be3baa618a4e7",
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
    for counts in product(range(34), range(9), range(4), range(3), range(2), range(2)):
        energy = sum((index + 1) ** 2 * count for index, count in enumerate(counts))
        l1_norm = sum((index + 1) * count for index, count in enumerate(counts))
        if energy == 33 and l1_norm <= 19 and sum(counts) <= 19:
            odd_count = sum(counts[0::2])
            answer.append((layer_cap(counts), counts, l1_norm, odd_count))
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
    slack_table = parent.relaxed_minimum_energy_by_slack(23)
    slack_trace = tuple(
        (l1_norm, 33 + 66 - 4 * l1_norm, slack_table[33 + 66 - 4 * l1_norm])
        for l1_norm in range(24, 18, -1)
    )
    assert slack_trace == (
        (24, 3, 53), (23, 7, 49), (22, 11, 45),
        (21, 15, 41), (20, 19, 37), (19, 23, 33),
    )

    profiles = energy_profiles()
    assert len(profiles) == 21
    assert profiles[:9] == [
        (2246, (5, 7, 0, 0, 0, 0), 19, 5),
        (2086, (8, 4, 1, 0, 0, 0), 19, 9),
        (2082, (1, 8, 0, 0, 0, 0), 17, 1),
        (1950, (11, 1, 2, 0, 0, 0), 19, 13),
        (1918, (4, 5, 1, 0, 0, 0), 17, 5),
        (1786, (13, 1, 0, 1, 0, 0), 19, 13),
        (1782, (0, 6, 1, 0, 0, 0), 15, 1),
        (1778, (7, 2, 2, 0, 0, 0), 17, 9),
        (1638, (3, 3, 2, 0, 0, 0), 15, 5),
    ]

    hermite = (
        (Fraction(48735,79507), Fraction(30772,79507), Fraction(-3445,1849)),
        (Fraction(4788,79507), Fraction(-4788,79507), Fraction(301253,1475502)),
        (Fraction(-213,79507), Fraction(213,79507), Fraction(-4243,737751)),
        (Fraction(2,79507), Fraction(-2,79507), Fraction(71,1475502)),
    )
    expected_forms = []
    for moment in (1732, 1733):
        expected_forms.append(add_forms(
            hermite[0],
            scale_form(Fraction(16), hermite[1]),
            scale_form(Fraction(16**2 + 66), hermite[2]),
            scale_form(Fraction(16**3 + 3 * 16 * 66 + moment), hermite[3]),
        ))
    assert expected_forms == [
        (Fraction(74749,79507), Fraction(4758,79507), Fraction(-601,38829)),
        (Fraction(74751,79507), Fraction(4756,79507), Fraction(-7589,491834)),
    ]
    log_2_lower, log_2_upper = atanh_log_bounds(Fraction(2), 8)
    log_8_over_7_lower, log_8_over_7_upper = atanh_log_bounds(Fraction(8,7), 8)
    log_64_over_57_lower, log_64_over_57_upper = atanh_log_bounds(Fraction(64,57), 8)
    margin_1732_lower = (
        Fraction(-543033,2544224) * log_2_upper
        + Fraction(74749,79507) * log_8_over_7_lower
        + Fraction(4758,79507) * log_64_over_57_lower
        + Fraction(601,38829)
    )
    margin_1733_upper = (
        Fraction(-542905,2544224) * log_2_lower
        + Fraction(74751,79507) * log_8_over_7_upper
        + Fraction(4756,79507) * log_64_over_57_upper
        + Fraction(7589,491834)
    )
    assert margin_1732_lower > 0
    assert margin_1733_upper < 0

    above_threshold = [profile for profile in profiles if profile[0] > 1732]
    survivors = [profile for profile in above_threshold if profile[3] <= 5]
    assert [profile[1] for profile in survivors] == [
        (5, 7, 0, 0, 0, 0),
        (1, 8, 0, 0, 0, 0),
        (4, 5, 1, 0, 0, 0),
        (0, 6, 1, 0, 0, 0),
    ]

    coefficient_magnitudes = (2, 2, 2, 1, 1, 1, 1)
    unit_chords = sum(
        left * right == 1 for left, right in combinations(coefficient_magnitudes, 2)
    )
    assert unit_chords == 6
    diameter_ledgers = {
        (1 + 4 * diameter_2 + 16 * diameter_4,
         (33 - 102 + 1 + 4 * diameter_2 + 16 * diameter_4) // 2)
        for diameter_4 in range(2)
        for diameter_2 in range(3)
        if diameter_2 <= 2 - diameter_4
    }
    assert diameter_ledgers == {(1,-34), (5,-32), (9,-30), (17,-26), (21,-24)}

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in (E34, VARIANCE, SIGNED, NORM):
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "(5,7),(1,8),(4,5,1),(0,6,1)" in nodes[NODE]["statement"]
    assert "M_3=1732" in nodes[NODE]["statement"]

    print(
        "E1_N256_S16_E33_PROFILE_PARITY_DIAMETER_REDUCTION_PASS "
        "profiles=21 above=8 survivors=4 threshold=1732 diameter_ledgers=5"
    )


if __name__ == "__main__":
    main()
