#!/usr/bin/env python3
"""Verify the N=256 E=27 profile/parity/light reduction."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e27_profile_parity_light_reduction"
DEPENDENCIES = {
    "e1_n256_s16_e28_endpoint_exclusion",
    "e1_n256_s16_sparse_l1_variance_exclusion",
    "e1_n256_s16_signed_chord_collision_gate",
    "collision_norm_criterion",
}
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
UNITS = tuple(range(1, 128, 2))
EXPECTED_SURVIVORS = [
    (3, 6, 0, 0, 0),
    (2, 4, 1, 0, 0),
    (1, 2, 2, 0, 0),
    (3, 2, 0, 1, 0),
    (0, 0, 3, 0, 0),
    (2, 0, 1, 1, 0),
]


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


def energy_profiles() -> list[dict[str, object]]:
    answer = []
    for counts in product(range(28), range(8), range(4), range(2), range(2)):
        energy = sum((index + 1) ** 2 * count for index, count in enumerate(counts))
        l1_norm = sum((index + 1) * count for index, count in enumerate(counts))
        if energy == 27 and l1_norm <= 15:
            answer.append({
                "cap": layer_cap(counts),
                "profile": list(counts),
                "l1": l1_norm,
                "odd_classes": sum(counts[0::2]),
            })
    return sorted(answer, key=lambda row: (int(row["cap"]), row["profile"]), reverse=True)


def distance(left: int, right: int) -> int:
    difference = (left - right) % 128
    return min(difference, 128 - difference)


def canonical(support: tuple[int, ...]) -> tuple[int, ...]:
    return min(
        tuple(sorted((unit * (value - anchor)) % 128 for value in support))
        for anchor in support
        for unit in UNITS
    )


def light_ledger() -> tuple[Counter[int], dict[int, set[tuple[int, ...]]], dict[int, Counter[tuple[int, ...]]], Counter[int]]:
    counts: Counter[int] = Counter()
    orbits: defaultdict[int, set[tuple[int, ...]]] = defaultdict(set)
    partitions: defaultdict[int, Counter[tuple[int, ...]]] = defaultdict(Counter)
    shared: Counter[int] = Counter()
    for rest in combinations(range(1, 128), 3):
        support = (0,) + rest
        chords = [(distance(left, right), left, right) for left, right in combinations(support, 2)]
        if sum(chord == 64 for chord, _, _ in chords) != 1:
            continue
        multiplicities = Counter(chord for chord, _, _ in chords if chord != 64)
        odd = sum(count % 2 for count in multiplicities.values())
        counts[odd] += 1
        orbits[odd].add(canonical(support))
        partitions[odd][tuple(sorted(multiplicities.values(), reverse=True))] += 1
        repeated = [chord for chord, count in multiplicities.items() if count == 2]
        if len(repeated) == 1:
            edges = [(left, right) for chord, left, right in chords if chord == repeated[0]]
            shared[odd] += bool(set(edges[0]) & set(edges[1]))
    return counts, dict(orbits), dict(partitions), shared


def matching_ledgers() -> set[int]:
    weights = (2, 2, 2, 1, 1, 1, 1)
    answer: set[int] = set()

    def visit(available: tuple[int, ...], edges: tuple[tuple[int, int], ...]) -> None:
        if not available:
            if sum(weights[left] == weights[right] == 1 for left, right in edges) == 1:
                answer.add(sum((weights[left] * weights[right]) ** 2 for left, right in edges))
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
    required_files = {
        "probe_source_file",
        "probe_result_file",
        "independent_check_file",
        "endpoint_file",
        "variance_parent_verify_file",
        "signed_chord_file",
        "collision_norm_file",
    }
    assert {key for key in pin if key.endswith("_file")} == required_files
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]

    parent_path = ROOT / pin["variance_parent_verify_file"]
    spec = importlib.util.spec_from_file_location("variance_parent_e27", parent_path)
    assert spec is not None and spec.loader is not None
    parent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(parent)
    slack = parent.relaxed_minimum_energy_by_slack(40)
    trace = [[l1, 27 + 66 - 4 * l1, slack[27 + 66 - 4 * l1]] for l1 in range(23, 14, -1)]
    assert trace == [
        [23, 1, None], [22, 5, 55], [21, 9, 51], [20, 13, 47],
        [19, 17, 43], [18, 21, 39], [17, 25, 35], [16, 29, 31], [15, 33, 27],
    ]

    packet = json.loads((ROOT / pin["probe_result_file"]).read_text())
    assert packet["schema"] == "e1-e27-profile-parity-probe-v1" and packet["complete"] is True
    assert packet["source_sha256"] == pin["probe_source_file_sha256"]
    assert packet["slack_trace"] == trace and int(packet["l1_bound"]) == 15
    profiles = energy_profiles()
    assert len(profiles) == 12 and packet["profiles"] == profiles

    hermite = (
        (Fraction(48735, 79507), Fraction(30772, 79507), Fraction(-3445, 1849)),
        (Fraction(4788, 79507), Fraction(-4788, 79507), Fraction(301253, 1475502)),
        (Fraction(-213, 79507), Fraction(213, 79507), Fraction(-4243, 737751)),
        (Fraction(2, 79507), Fraction(-2, 79507), Fraction(71, 1475502)),
    )
    forms = []
    for moment in (443, 444):
        raw = (1, 16, 310, 6688 + moment)
        forms.append(tuple(sum(raw[index] * hermite[index][column] for index in range(4)) for column in range(3)))
    assert forms == [
        (Fraction(73575, 79507), Fraction(5932, 79507), Fraction(-17807, 491834)),
        (Fraction(73577, 79507), Fraction(5930, 79507), Fraction(-26675, 737751)),
    ]
    l2, u2 = atanh_log_bounds(Fraction(2))
    l87, u87 = atanh_log_bounds(Fraction(8, 7))
    l6457, u6457 = atanh_log_bounds(Fraction(64, 57))
    assert Fraction(-618169, 2544224) * u2 + forms[0][0] * l87 + forms[0][1] * l6457 - forms[0][2] > 0
    assert Fraction(-618041, 2544224) * l2 + forms[1][0] * u87 + forms[1][1] * u6457 - forms[1][2] < 0
    assert int(packet["cubic_cutoff"]) == 443

    above = [row for row in profiles if int(row["cap"]) > 443]
    survivors = [row for row in above if int(row["odd_classes"]) <= 5]
    assert len(above) == 11 and [tuple(row["profile"]) for row in survivors] == EXPECTED_SURVIVORS
    assert packet["above_cutoff"] == above and packet["parity_survivors"] == survivors

    counts, orbits, partitions, shared = light_ledger()
    assert counts == Counter({1: 264, 3: 960, 5: 14_400})
    assert {odd: len(values) for odd, values in orbits.items()} == {1: 11, 3: 8, 5: 100}
    assert partitions == {
        1: Counter({(2, 2, 1): 264}),
        3: Counter({(2, 1, 1, 1): 960}),
        5: Counter({(1, 1, 1, 1, 1): 14_400}),
    }
    assert shared == Counter({3: 960})
    printed = packet["light_geometry"]["orbit_representatives"]
    assert {odd: [list(value) for value in sorted(orbits[odd])] for odd in (1, 3, 5)} == {
        odd: printed[str(odd)] for odd in (1, 3, 5)
    }
    assert matching_ledgers() == {1, 5, 9, 17, 21}
    assert packet["diameter_ledgers"] == [[1, -37], [5, -35], [9, -33], [17, -29], [21, -27]]

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    incoming = {source for source, target, kind in edges if target == NODE and kind == "req"}
    assert incoming == DEPENDENCIES
    assert all(nodes[dependency]["status"] == "PROVED" for dependency in DEPENDENCIES)
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "M_3=443" in nodes[NODE]["statement"] and "eight" in nodes[NODE]["statement"]

    print("E1_N256_S16_E27_PROFILE_PARITY_LIGHT_REDUCTION_PASS profiles=12 above=11 survivors=6 supports=15624 orbits=119 router=8 ledgers=5")


if __name__ == "__main__":
    main()
