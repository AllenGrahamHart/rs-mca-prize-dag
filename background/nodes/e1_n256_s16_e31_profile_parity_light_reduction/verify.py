#!/usr/bin/env python3
"""Verify the N=256 E=31 profile/parity/light reduction."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e31_profile_parity_light_reduction"
DEPENDENCIES = (
    "e1_n256_s16_e32_endpoint_exclusion",
    "e1_n256_s16_sparse_l1_variance_exclusion",
    "e1_n256_s16_signed_chord_collision_gate",
    "collision_norm_criterion",
)
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")

EXPECTED_PIN = {
    "classifier_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e31_three_odd_light_orbit_classifier.py",
    "classifier_file_sha256": "c46d38885814ae21420c7e4ddc20e9588f45fb4a0bf08cbf4349978ab8f5ff92",
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "endpoint_file": "background/nodes/e1_n256_s16_e32_endpoint_exclusion/statement.md",
    "endpoint_file_sha256": "b6b8c1a986f9f64d64bed2fb056f8bcc64e5e8d86e3ef93bdd7cd6bcc40a9cd8",
    "independent_check_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e31_three_odd_light_orbit_check.py",
    "independent_check_file_sha256": "2412075b185a0900c1c5fa32986b08205bbfa5ae08e7b2993db76805d7b12588",
    "orbit_result_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e31_three_odd_light_orbit_result.json",
    "orbit_result_file_sha256": "dfa93a27a628267ec21ec3684ae8e567cce0f25bd836e31e4b55ae71ecce2ca6",
    "signed_chord_file": "background/nodes/e1_n256_s16_signed_chord_collision_gate/statement.md",
    "signed_chord_file_sha256": "926f9c94a0b5dd0830b7e37fafcd96f570dd93802de16061c802546e466e3157",
    "variance_parent_verify_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/verify.py",
    "variance_parent_verify_file_sha256": "57b7a0f2d8590bda9234f4fb5bc0a573afd56200436458121767489fc5091f8e",
}

EXPECTED_REPRESENTATIVES = (
    (0, 1, 2, 64),
    (0, 1, 32, 64),
    (0, 2, 4, 64),
    (0, 2, 32, 64),
    (0, 4, 8, 64),
    (0, 4, 32, 64),
    (0, 8, 16, 64),
    (0, 8, 32, 64),
)
UNITS = tuple(range(1, 128, 2))


def atanh_log_bounds(value: Fraction, terms: int = 8) -> tuple[Fraction, Fraction]:
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
    for counts in product(range(32), range(8), range(4), range(2), range(2)):
        energy = sum((index + 1) ** 2 * count for index, count in enumerate(counts))
        l1_norm = sum((index + 1) * count for index, count in enumerate(counts))
        if energy == 31 and l1_norm <= 17:
            answer.append((layer_cap(counts), counts, l1_norm, sum(counts[0::2])))
    return sorted(answer, reverse=True)


def distance(left: int, right: int) -> int:
    difference = (left - right) % 128
    return min(difference, 128 - difference)


def canonical(support: tuple[int, ...]) -> tuple[int, ...]:
    return min(
        tuple(sorted((unit * (value - anchor)) % 128 for value in support))
        for anchor in support
        for unit in UNITS
    )


def direct_light_orbits() -> tuple[int, dict[tuple[int, ...], int]]:
    orbit_counts: defaultdict[tuple[int, ...], int] = defaultdict(int)
    normalized = 0
    for rest in combinations(range(1, 128), 3):
        support = (0,) + rest
        counts = Counter(distance(left, right) for left, right in combinations(support, 2))
        if counts[64] != 1:
            continue
        odd = sum(count % 2 for chord, count in counts.items() if chord != 64)
        if odd != 3:
            continue
        partition = tuple(sorted((count for chord, count in counts.items() if chord != 64), reverse=True))
        assert partition == (2, 1, 1, 1)
        normalized += 1
        orbit_counts[canonical(support)] += 1
    return normalized, dict(orbit_counts)


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]

    parent_path = ROOT / pin["variance_parent_verify_file"]
    spec = importlib.util.spec_from_file_location("variance_parent_e31", parent_path)
    assert spec is not None and spec.loader is not None
    parent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(parent)
    slack_table = parent.relaxed_minimum_energy_by_slack(29)
    slack_trace = tuple(
        (l1_norm, 31 + 66 - 4 * l1_norm, slack_table[31 + 66 - 4 * l1_norm])
        for l1_norm in range(24, 16, -1)
    )
    assert slack_trace == (
        (24, 1, None), (23, 5, 55), (22, 9, 51), (21, 13, 47),
        (20, 17, 43), (19, 21, 39), (18, 25, 35), (17, 29, 31),
    )

    profiles = energy_profiles()
    assert len(profiles) == 15
    assert profiles[:8] == [
        (1906, (3, 7, 0, 0, 0), 17, 3),
        (1754, (6, 4, 1, 0, 0), 17, 7),
        (1626, (9, 1, 2, 0, 0), 17, 11),
        (1610, (2, 5, 1, 0, 0), 15, 3),
        (1478, (5, 2, 2, 0, 0), 15, 7),
        (1470, (11, 1, 0, 1, 0), 17, 11),
        (1362, (1, 3, 2, 0, 0), 13, 3),
        (1314, (7, 2, 0, 1, 0), 15, 7),
    ]

    hermite = (
        (Fraction(48735, 79507), Fraction(30772, 79507), Fraction(-3445, 1849)),
        (Fraction(4788, 79507), Fraction(-4788, 79507), Fraction(301253, 1475502)),
        (Fraction(-213, 79507), Fraction(213, 79507), Fraction(-4243, 737751)),
        (Fraction(2, 79507), Fraction(-2, 79507), Fraction(71, 1475502)),
    )
    forms = [
        add_forms(
            hermite[0],
            scale_form(Fraction(16), hermite[1]),
            scale_form(Fraction(16**2 + 62), hermite[2]),
            scale_form(Fraction(16**3 + 3 * 16 * 62 + moment), hermite[3]),
        )
        for moment in (1302, 1303)
    ]
    assert forms == [
        (Fraction(74357, 79507), Fraction(5150, 79507), Fraction(-16528, 737751)),
        (Fraction(74359, 79507), Fraction(5148, 79507), Fraction(-10995, 491834)),
    ]

    log_2_lower, log_2_upper = atanh_log_bounds(Fraction(2))
    log_8_over_7_lower, log_8_over_7_upper = atanh_log_bounds(Fraction(8, 7))
    log_64_over_57_lower, log_64_over_57_upper = atanh_log_bounds(Fraction(64, 57))
    assert (
        Fraction(-568121, 2544224) * log_2_upper
        + Fraction(74357, 79507) * log_8_over_7_lower
        + Fraction(5150, 79507) * log_64_over_57_lower
        + Fraction(16528, 737751)
    ) > 0
    assert (
        Fraction(-567993, 2544224) * log_2_lower
        + Fraction(74359, 79507) * log_8_over_7_upper
        + Fraction(5148, 79507) * log_64_over_57_upper
        + Fraction(10995, 491834)
    ) < 0

    above_threshold = [profile for profile in profiles if profile[0] > 1302]
    assert len(above_threshold) == 8
    survivors = [profile for profile in above_threshold if profile[3] <= 5]
    assert [profile[1] for profile in survivors] == [
        (3, 7, 0, 0, 0), (2, 5, 1, 0, 0), (1, 3, 2, 0, 0),
    ]

    diameter_ledgers = set()
    for heavy_heavy in range(2):
        for heavy_light in range(3):
            if heavy_light > min(3 - 2 * heavy_heavy, 2):
                continue
            square_mass = 1 + 4 * heavy_light + 16 * heavy_heavy
            diameter_ledgers.add((square_mass, (square_mass - 71) // 2))
    assert diameter_ledgers == {(1, -35), (5, -33), (9, -31), (17, -27), (21, -25)}

    normalized, orbit_counts = direct_light_orbits()
    assert normalized == 960
    assert tuple(sorted(orbit_counts)) == EXPECTED_REPRESENTATIVES
    assert Counter(orbit_counts.values()) == Counter({32: 2, 64: 2, 128: 2, 256: 2})
    packet = json.loads((ROOT / pin["orbit_result_file"]).read_text())
    assert packet["normalized_supports"] == normalized
    assert packet["orbits"] == len(orbit_counts) == 8
    assert tuple(tuple(row["representative"]) for row in packet["rows"]) == EXPECTED_REPRESENTATIVES

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    incoming = {source for source, target, kind in edges if target == NODE and kind == "req"}
    assert incoming == set(DEPENDENCIES)
    assert all(nodes[dependency]["status"] == "PROVED" for dependency in DEPENDENCIES)
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "M_3=1302" in nodes[NODE]["statement"]
    assert "960 normalized supports" in nodes[NODE]["statement"]

    print(
        "E1_N256_S16_E31_PROFILE_PARITY_LIGHT_REDUCTION_PASS "
        "profiles=15 above=8 survivors=3 supports=960 orbits=8 ledgers=5"
    )


if __name__ == "__main__":
    main()
