#!/usr/bin/env python3
"""Verify the N=256 E=30 profile/parity/light reduction."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e30_profile_parity_light_reduction"
DEPENDENCIES = {
    "e1_n256_s16_e31_endpoint_exclusion",
    "e1_n256_s16_sparse_l1_variance_exclusion",
    "e1_n256_s16_signed_chord_collision_gate",
    "collision_norm_criterion",
}
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
EXPECTED_PIN = {
    "classifier_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_two_six_odd_light_orbit_classifier.py",
    "classifier_file_sha256": "4d9a442a502be612fe2691c89a8c950b62ea7e7e0a87f3e24ec5c35b3b068c5f",
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "endpoint_file": "background/nodes/e1_n256_s16_e31_endpoint_exclusion/statement.md",
    "endpoint_file_sha256": "2b735476474994494974c969245af60601b2fe1f5c738474e46bea26f74ac262",
    "independent_check_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_two_six_odd_light_orbit_check.py",
    "independent_check_file_sha256": "20dac08416459193e2f4736db71fc1f7a11f18f20ef8be8f68f85660d5e31313",
    "orbit_result_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_two_six_odd_light_orbit_result.json",
    "orbit_result_file_sha256": "6ba7acb9e680f115b7c6121615748b00fa68a6adee005bb750094fea73ce5759",
    "signed_chord_file": "background/nodes/e1_n256_s16_signed_chord_collision_gate/statement.md",
    "signed_chord_file_sha256": "926f9c94a0b5dd0830b7e37fafcd96f570dd93802de16061c802546e466e3157",
    "variance_parent_verify_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/verify.py",
    "variance_parent_verify_file_sha256": "57b7a0f2d8590bda9234f4fb5bc0a573afd56200436458121767489fc5091f8e",
}
UNITS = tuple(range(1, 128, 2))


def atanh_log_bounds(value: Fraction, terms: int = 8) -> tuple[Fraction, Fraction]:
    parameter = (value - 1) / (value + 1)
    lower = 2 * sum(
        parameter ** (2 * index + 1) / (2 * index + 1)
        for index in range(terms)
    )
    degree = 2 * terms + 1
    return lower, lower + 2 * parameter**degree / (degree * (1 - parameter * parameter))


def layer_cap(counts: tuple[int, ...]) -> int:
    sizes = [2 * sum(counts[level:]) for level in range(len(counts)) if sum(counts[level:])]
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
    for counts in product(range(31), range(8), range(4), range(2), range(2)):
        energy = sum((index + 1) ** 2 * count for index, count in enumerate(counts))
        l1_norm = sum((index + 1) * count for index, count in enumerate(counts))
        if energy == 30 and l1_norm <= 18:
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


def direct_light_ledger() -> tuple[Counter[tuple[int, int]], dict[tuple[int, ...], int]]:
    signatures: Counter[tuple[int, int]] = Counter()
    two_odd_orbits: defaultdict[tuple[int, ...], int] = defaultdict(int)
    for rest in combinations(range(1, 128), 3):
        support = (0,) + rest
        counts = Counter(distance(left, right) for left, right in combinations(support, 2))
        diameter = counts[64]
        odd = sum(count % 2 for chord, count in counts.items() if chord != 64)
        signatures[(diameter, odd)] += 1
        if diameter == 0 and odd == 2:
            partition = tuple(sorted((count for chord, count in counts.items() if chord != 64), reverse=True))
            assert partition in ((2, 2, 1, 1), (3, 2, 1))
            two_odd_orbits[canonical(support)] += 1
        if diameter == 0 and odd == 6:
            assert all(count == 1 for chord, count in counts.items() if chord != 64)
    return signatures, dict(two_odd_orbits)


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]

    parent_path = ROOT / pin["variance_parent_verify_file"]
    spec = importlib.util.spec_from_file_location("variance_parent_e30", parent_path)
    assert spec is not None and spec.loader is not None
    parent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(parent)
    slack_table = parent.relaxed_minimum_energy_by_slack(24)
    slack_trace = tuple(
        (l1_norm, 30 + 66 - 4 * l1_norm, slack_table[30 + 66 - 4 * l1_norm])
        for l1_norm in range(24, 17, -1)
    )
    assert slack_trace == (
        (24, 0, 54), (23, 4, 50), (22, 8, 46), (21, 12, 42),
        (20, 16, 38), (19, 20, 34), (18, 24, 30),
    )

    profiles = energy_profiles()
    assert len(profiles) == 18
    assert profiles[:13] == [
        (1908, (6, 6, 0, 0, 0), 18, 6),
        (1764, (9, 3, 1, 0, 0), 18, 10),
        (1748, (2, 7, 0, 0, 0), 16, 2),
        (1644, (12, 0, 2, 0, 0), 18, 14),
        (1600, (5, 4, 1, 0, 0), 16, 6),
        (1500, (14, 0, 0, 1, 0), 18, 14),
        (1476, (8, 1, 2, 0, 0), 16, 10),
        (1468, (1, 5, 1, 0, 0), 14, 2),
        (1340, (4, 2, 2, 0, 0), 14, 6),
        (1324, (10, 1, 0, 1, 0), 16, 10),
        (1236, (0, 3, 2, 0, 0), 12, 2),
        (1180, (6, 2, 0, 1, 0), 14, 6),
        (1128, (3, 0, 3, 0, 0), 12, 6),
    ]

    hermite = (
        (Fraction(48735, 79507), Fraction(30772, 79507), Fraction(-3445, 1849)),
        (Fraction(4788, 79507), Fraction(-4788, 79507), Fraction(301253, 1475502)),
        (Fraction(-213, 79507), Fraction(213, 79507), Fraction(-4243, 737751)),
        (Fraction(2, 79507), Fraction(-2, 79507), Fraction(71, 1475502)),
    )
    forms = []
    for moment in (1087, 1088):
        raw = (1, 16, 16**2 + 60, 16**3 + 3 * 16 * 60 + moment)
        forms.append(tuple(sum(raw[index] * hermite[index][column] for index in range(4)) for column in range(3)))
    assert forms == [
        (Fraction(74161, 79507), Fraction(5346, 79507), Fraction(-38165, 1475502)),
        (Fraction(74163, 79507), Fraction(5344, 79507), Fraction(-907, 35131)),
    ]

    l2, u2 = atanh_log_bounds(Fraction(2))
    l87, u87 = atanh_log_bounds(Fraction(8, 7))
    l6457, u6457 = atanh_log_bounds(Fraction(64, 57))
    assert Fraction(-580665, 2544224) * u2 + forms[0][0] * l87 + forms[0][1] * l6457 - forms[0][2] > 0
    assert Fraction(-580537, 2544224) * l2 + forms[1][0] * u87 + forms[1][1] * u6457 - forms[1][2] < 0

    above = [profile for profile in profiles if profile[0] > 1087]
    assert len(above) == 13
    survivors = [profile for profile in above if profile[3] <= 6]
    assert [profile[1] for profile in survivors] == [
        (6, 6, 0, 0, 0), (2, 7, 0, 0, 0), (5, 4, 1, 0, 0),
        (1, 5, 1, 0, 0), (4, 2, 2, 0, 0), (0, 3, 2, 0, 0),
        (6, 2, 0, 1, 0), (3, 0, 3, 0, 0),
    ]

    diameter_ledgers = set()
    for heavy_heavy in range(2):
        for heavy_light in range(4):
            if heavy_light > min(3 - 2 * heavy_heavy, 4):
                continue
            square_mass = 4 * heavy_light + 16 * heavy_heavy
            diameter_ledgers.add((square_mass, (square_mass - 72) // 2))
    assert diameter_ledgers == {(0, -36), (4, -34), (8, -32), (12, -30), (16, -28), (20, -26)}

    signatures, two_odd_orbits = direct_light_ledger()
    assert signatures == Counter({
        (0, 2): 8168, (0, 4): 28800, (0, 6): 280720,
        (1, 1): 264, (1, 3): 960, (1, 5): 14400, (2, 0): 63,
    })
    assert len(two_odd_orbits) == 87
    assert sum(two_odd_orbits.values()) == 8168
    assert Counter(two_odd_orbits.values()) == Counter({8: 1, 16: 4, 32: 11, 64: 23, 128: 47, 256: 1})
    packet = json.loads((ROOT / pin["orbit_result_file"]).read_text())
    assert packet["normalized_two_odd_supports"] == 8168
    assert packet["normalized_six_odd_supports"] == 280720
    assert packet["two_odd_orbits"] == 87
    assert packet["six_odd_orbit_lower_bound"] == 1097

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    incoming = {source for source, target, kind in edges if target == NODE and kind == "req"}
    assert incoming == DEPENDENCIES
    assert all(nodes[dependency]["status"] == "PROVED" for dependency in DEPENDENCIES)
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "M_3=1087" in nodes[NODE]["statement"]
    assert "21,773,185,792" in nodes[NODE]["statement"]

    print(
        "E1_N256_S16_E30_PROFILE_PARITY_LIGHT_REDUCTION_PASS "
        "profiles=18 above=13 survivors=8 two=8168/87 six=280720/1097+ ledgers=6"
    )


if __name__ == "__main__":
    main()
