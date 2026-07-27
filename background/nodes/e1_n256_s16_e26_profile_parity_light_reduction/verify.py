#!/usr/bin/env python3
"""Verify the N=256 E=26 profile/parity/light reduction."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e26_profile_parity_light_reduction"
DEPENDENCIES = {
    "e1_n256_s16_e27_endpoint_exclusion",
    "e1_n256_s16_sparse_l1_variance_exclusion",
    "e1_n256_s16_signed_chord_collision_gate",
    "e1_n256_s16_e30_profile_parity_light_reduction",
    "collision_norm_criterion",
}
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
SURVIVORS = [
    (6, 5, 0, 0, 0), (2, 6, 0, 0, 0), (5, 3, 1, 0, 0),
    (1, 4, 1, 0, 0), (4, 1, 2, 0, 0), (0, 2, 2, 0, 0),
    (6, 1, 0, 1, 0), (2, 2, 0, 1, 0), (1, 0, 1, 1, 0),
    (1, 0, 0, 0, 1),
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


def profiles() -> list[dict[str, object]]:
    rows = []
    for counts in product(range(27), range(8), range(4), range(2), range(2)):
        energy = sum((index + 1) ** 2 * count for index, count in enumerate(counts))
        l1_norm = sum((index + 1) * count for index, count in enumerate(counts))
        if energy == 26 and l1_norm <= 16:
            rows.append({
                "cap": layer_cap(counts),
                "profile": list(counts),
                "l1": l1_norm,
                "odd_classes": sum(counts[0::2]),
            })
    return sorted(rows, key=lambda row: (int(row["cap"]), row["profile"]), reverse=True)


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    required = {
        "probe_source_file", "probe_result_file", "independent_check_file",
        "endpoint_file", "two_odd_atlas_file", "six_odd_atlas_file",
        "variance_parent_verify_file", "signed_chord_file", "collision_norm_file",
    }
    assert {key for key in pin if key.endswith("_file")} == required
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]

    parent_path = ROOT / pin["variance_parent_verify_file"]
    spec = importlib.util.spec_from_file_location("variance_parent_e26", parent_path)
    assert spec is not None and spec.loader is not None
    parent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(parent)
    slack = parent.relaxed_minimum_energy_by_slack(48)
    trace = [[l1, 26 + 66 - 4 * l1, slack[26 + 66 - 4 * l1]] for l1 in range(23, 11, -1)]
    assert trace == [
        [23, 0, 54], [22, 4, 50], [21, 8, 46], [20, 12, 42],
        [19, 16, 38], [18, 20, 34], [17, 24, 30], [16, 28, 26],
        [15, 32, 22], [14, 36, 18], [13, 40, 14], [12, 44, 10],
    ]

    packet = json.loads((ROOT / pin["probe_result_file"]).read_text())
    assert packet["schema"] == "e1-e26-profile-parity-route-probe-v1" and packet["complete"] is True
    assert packet["source_sha256"] == pin["probe_source_file_sha256"]
    assert packet["slack_trace"] == trace and packet["l1_bound"] == 16
    exact_profiles = profiles()
    assert len(exact_profiles) == 13 and packet["profiles"] == exact_profiles

    hermite = (
        (Fraction(48735, 79507), Fraction(30772, 79507), Fraction(-3445, 1849)),
        (Fraction(4788, 79507), Fraction(-4788, 79507), Fraction(301253, 1475502)),
        (Fraction(-213, 79507), Fraction(213, 79507), Fraction(-4243, 737751)),
        (Fraction(2, 79507), Fraction(-2, 79507), Fraction(71, 1475502)),
    )
    forms = []
    for moment in (228, 229):
        raw = (1, 16, 308, 6592 + moment)
        forms.append(tuple(sum(raw[index] * hermite[index][column] for index in range(4)) for column in range(3)))
    assert forms == [
        (Fraction(73379, 79507), Fraction(6128, 79507), Fraction(-9755, 245917)),
        (Fraction(73381, 79507), Fraction(6126, 79507), Fraction(-58459, 1475502)),
    ]
    l2, u2 = atanh_log_bounds(Fraction(2))
    l87, u87 = atanh_log_bounds(Fraction(8, 7))
    l6457, u6457 = atanh_log_bounds(Fraction(64, 57))
    assert Fraction(-630713, 2544224) * u2 + forms[0][0] * l87 + forms[0][1] * l6457 - forms[0][2] > 0
    assert Fraction(-630585, 2544224) * l2 + forms[1][0] * u87 + forms[1][1] * u6457 - forms[1][2] < 0
    assert packet["cubic_cutoff"] == 228 and packet["above_cutoff"] == exact_profiles
    survivors = [row for row in exact_profiles if int(row["odd_classes"]) <= 6]
    assert [tuple(row["profile"]) for row in survivors] == SURVIVORS
    assert packet["parity_survivors"] == survivors

    two = json.loads((ROOT / pin["two_odd_atlas_file"]).read_text())
    six = json.loads((ROOT / pin["six_odd_atlas_file"]).read_text())
    assert two["complete"] is six["complete"] is True
    assert (two["normalized_two_odd_supports"], two["two_odd_orbits"]) == (8168, 87)
    assert (six["summary"]["normalized_six_odd_supports"], six["summary"]["affine_light_orbits"]) == (280720, 1234)
    assert packet["relevant_affine_templates"] == 1321
    assert packet["direct_vector_floor"] == 26_219_123_456

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    incoming = {source for source, target, kind in edges if target == NODE and kind == "req"}
    assert incoming == DEPENDENCIES
    assert all(nodes[dependency]["status"] == "PROVED" for dependency in DEPENDENCIES)
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "M_3=228" in nodes[NODE]["statement"] and "26,219,123,456" in nodes[NODE]["statement"]
    print("E1_N256_S16_E26_PROFILE_PARITY_LIGHT_REDUCTION_PASS profiles=13 survivors=10 two=8168/87 six=280720/1234 floor=26219123456")


if __name__ == "__main__":
    main()
