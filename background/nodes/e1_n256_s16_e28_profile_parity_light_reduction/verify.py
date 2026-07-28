#!/usr/bin/env python3
"""Verify the N=256 E=28 profile/parity/light reduction."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e28_profile_parity_light_reduction"
DEPENDENCIES = {
    "e1_n256_s16_e29_endpoint_exclusion",
    "e1_n256_s16_sparse_l1_variance_exclusion",
    "e1_n256_s16_signed_chord_collision_gate",
    "e1_n256_s16_e32_profile_parity_diameter_reduction",
    "collision_norm_criterion",
}
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
EXPECTED_SURVIVORS = [
    (4, 6, 0, 0, 0), (0, 7, 0, 0, 0), (3, 4, 1, 0, 0),
    (2, 2, 2, 0, 0), (4, 2, 0, 1, 0), (1, 0, 3, 0, 0),
    (0, 3, 0, 1, 0), (3, 0, 1, 1, 0),
]


def atanh_log_bounds(value: Fraction, terms: int = 8) -> tuple[Fraction, Fraction]:
    parameter = (value - 1) / (value + 1)
    lower = 2 * sum(parameter ** (2 * index + 1) / (2 * index + 1) for index in range(terms))
    degree = 2 * terms + 1
    return lower, lower + 2 * parameter**degree / (degree * (1 - parameter * parameter))


def layer_cap(counts: tuple[int, ...]) -> int:
    sizes = [2 * sum(counts[level:]) for level in range(len(counts)) if sum(counts[level:])]
    return sum(
        min(a * b - min(a, b), a * c - min(a, c), b * c - min(b, c))
        for a, b, c in product(sizes, repeat=3)
    )


def energy_profiles() -> list[dict[str, object]]:
    answer = []
    for counts in product(range(29), range(8), range(4), range(2), range(2)):
        energy = sum((index + 1) ** 2 * count for index, count in enumerate(counts))
        l1_norm = sum((index + 1) * count for index, count in enumerate(counts))
        if energy == 28 and l1_norm <= 16:
            answer.append({
                "cap": layer_cap(counts), "profile": list(counts), "l1": l1_norm,
                "odd_classes": sum(counts[0::2]),
            })
    return sorted(answer, key=lambda row: (int(row["cap"]), row["profile"]), reverse=True)


def distance(left: int, right: int) -> int:
    difference = (left - right) % 128
    return min(difference, 128 - difference)


def canonical(support: tuple[int, ...]) -> tuple[int, ...]:
    return min(
        tuple(sorted((unit * (value - anchor)) % 128 for value in support))
        for anchor in support for unit in range(1, 128, 2)
    )


def light_ledger() -> tuple[Counter[tuple[int, int]], set[tuple[int, ...]]]:
    signatures: Counter[tuple[int, int]] = Counter()
    zero_orbits: set[tuple[int, ...]] = set()
    for rest in combinations(range(1, 128), 3):
        support = (0,) + rest
        counts = Counter(distance(left, right) for left, right in combinations(support, 2))
        diameter = counts[64]
        odd = sum(count % 2 for chord, count in counts.items() if chord != 64)
        signatures[(diameter, odd)] += 1
        if (diameter, odd) == (2, 0):
            zero_orbits.add(canonical(support))
    return signatures, zero_orbits


def matching_ledgers(light_diameters: int) -> set[int]:
    weights = (2, 2, 2, 1, 1, 1, 1)
    answer: set[int] = set()

    def visit(available: tuple[int, ...], edges: tuple[tuple[int, int], ...]) -> None:
        if not available:
            if sum(weights[a] == weights[b] == 1 for a, b in edges) == light_diameters:
                answer.add(sum((weights[a] * weights[b]) ** 2 for a, b in edges))
            return
        first = available[0]
        visit(available[1:], edges)
        for offset, second in enumerate(available[1:]):
            remainder = available[1 : offset + 1] + available[offset + 2 :]
            visit(remainder, edges + ((first, second),))

    visit(tuple(range(7)), ())
    return answer


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    required = {
        "probe_source_file", "probe_result_file", "endpoint_file",
        "variance_parent_verify_file", "signed_chord_file", "collision_norm_file",
        "four_atlas_owner_file", "four_atlas_result_file",
    }
    assert {key for key in pin if key.endswith("_file")} == required
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]

    spec = importlib.util.spec_from_file_location("variance_parent_e28", ROOT / pin["variance_parent_verify_file"])
    assert spec is not None and spec.loader is not None
    parent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(parent)
    slack = parent.relaxed_minimum_energy_by_slack(40)
    trace = [[l1, 28 + 66 - 4 * l1, slack[28 + 66 - 4 * l1]] for l1 in range(23, 14, -1)]
    assert trace == [
        [23, 2, 56], [22, 6, 52], [21, 10, 48], [20, 14, 44], [19, 18, 40],
        [18, 22, 36], [17, 26, 32], [16, 30, 28], [15, 34, 24],
    ]

    packet = json.loads((ROOT / pin["probe_result_file"]).read_text())
    assert packet["schema"] == "e1-e28-profile-parity-route-probe-v1" and packet["complete"] is True
    assert packet["source_sha256"] == pin["probe_source_file_sha256"]
    assert packet["slack_trace"] == trace and int(packet["l1_bound"]) == 16
    profiles = energy_profiles()
    assert len(profiles) == 14 and packet["profiles"] == profiles

    hermite = (
        (Fraction(48735, 79507), Fraction(30772, 79507), Fraction(-3445, 1849)),
        (Fraction(4788, 79507), Fraction(-4788, 79507), Fraction(301253, 1475502)),
        (Fraction(-213, 79507), Fraction(213, 79507), Fraction(-4243, 737751)),
        (Fraction(2, 79507), Fraction(-2, 79507), Fraction(71, 1475502)),
    )
    forms = []
    for moment in (658, 659):
        raw = (1, 16, 312, 6784 + moment)
        forms.append(tuple(sum(raw[index] * hermite[index][column] for index in range(4)) for column in range(3)))
    assert forms == [
        (Fraction(73771, 79507), Fraction(5736, 79507), Fraction(-8052, 245917)),
        (Fraction(73773, 79507), Fraction(5734, 79507), Fraction(-2539, 77658)),
    ]
    l2, u2 = atanh_log_bounds(Fraction(2))
    l87, u87 = atanh_log_bounds(Fraction(8, 7))
    l6457, u6457 = atanh_log_bounds(Fraction(64, 57))
    assert Fraction(-605625, 2544224) * u2 + forms[0][0] * l87 + forms[0][1] * l6457 - forms[0][2] > 0
    assert Fraction(-605497, 2544224) * l2 + forms[1][0] * u87 + forms[1][1] * u6457 - forms[1][2] < 0
    assert int(packet["cubic_cutoff"]) == 658
    above = [row for row in profiles if int(row["cap"]) > 658]
    survivors = [row for row in above if int(row["odd_classes"]) <= 6]
    assert len(above) == 13 and [tuple(row["profile"]) for row in survivors] == EXPECTED_SURVIVORS
    assert packet["above_cutoff"] == above and packet["parity_survivors"] == survivors

    signatures, zero_orbits = light_ledger()
    assert signatures == Counter({
        (0, 2): 8168, (0, 4): 28800, (0, 6): 280720,
        (1, 1): 264, (1, 3): 960, (1, 5): 14400, (2, 0): 63,
    })
    assert [list(value) for value in sorted(zero_orbits)] == packet["light_geometry"]["zero_odd_orbits"]
    four = json.loads((ROOT / pin["four_atlas_result_file"]).read_text())
    assert four["complete"] is True and four["normalized_supports"] == 28800 and four["orbits"] == 148
    assert packet["atlas_sha256"]["4"] == pin["four_atlas_result_file_sha256"]
    assert packet["relevant_affine_templates"] == 154 and packet["direct_vector_floor"] == 3_056_582_144
    assert matching_ledgers(0) == {0, 4, 8, 12, 16, 20}
    assert matching_ledgers(2) == {2, 18}

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    incoming = {source for source, target, kind in edges if target == NODE and kind == "req"}
    assert incoming == DEPENDENCIES and all(nodes[item]["status"] == "PROVED" for item in DEPENDENCIES)
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "M_3=658" in nodes[NODE]["statement"] and "154" in nodes[NODE]["statement"]

    print("E1_N256_S16_E28_PROFILE_PARITY_LIGHT_REDUCTION_PASS profiles=14 above=13 survivors=8 zero=63/6 four=28800/148 router=154 ledgers=8")


if __name__ == "__main__":
    main()
