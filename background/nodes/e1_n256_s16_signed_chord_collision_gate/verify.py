#!/usr/bin/env python3
"""Verify the N=256 square-mass-16 signed-chord gate."""

from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_signed_chord_collision_gate"
PARENT = "e1_n256_s16_sparse_l1_variance_exclusion"
E1_TARGET = "e1_official_prime_exception_control"
UNIVERSAL_TARGET = "unsafe_crossing_family_instantiation"

EXPECTED_PIN = {
    "variance_parent_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/statement.md",
    "variance_parent_file_sha256": "54ad9ae4d64e6ab8d4dd7aaf3bc2998f54c78058756b5dc06ad969198b255aca",
}


def maximum_matching_weight(weights: tuple[int, ...]) -> int:
    if len(weights) < 2:
        return 0
    first = weights[0]
    best = maximum_matching_weight(weights[1:])
    for index in range(1, len(weights)):
        remainder = weights[1:index] + weights[index + 1 :]
        best = max(
            best,
            first * weights[index] + maximum_matching_weight(remainder),
        )
    return best


def chord_ledger(coefficients: dict[int, int]) -> tuple[int, int, int]:
    groups: dict[int, list[int]] = defaultdict(list)
    diameter_square_mass = 0
    for left, right in combinations(sorted(coefficients), 2):
        difference = right - left
        product = coefficients[left] * coefficients[right]
        if difference == 64:
            diameter_square_mass += product * product
        elif difference < 64:
            groups[difference].append(product)
        else:
            groups[128 - difference].append(-product)

    half_variance = sum(sum(weights) ** 2 for weights in groups.values())
    cross_sum = sum(
        sum(left * right for left, right in combinations(weights, 2))
        for weights in groups.values()
    )
    return half_variance, diameter_square_mass, cross_sum


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    source = ROOT / pin["variance_parent_file"]
    assert hashlib.sha256(source.read_bytes()).hexdigest() == pin[
        "variance_parent_file_sha256"
    ]

    profile_square_weights = (4, 4, 4, 1, 1, 1, 1)
    assert sum(profile_square_weights) == 16
    assert sum(weight * weight for weight in profile_square_weights) == 52
    assert (16**2 - 52) // 2 == 102
    assert maximum_matching_weight(profile_square_weights) == 21
    assert (41 - 102 + 21) // 2 == -20

    witness = {
        0: 2,
        16: -2,
        32: -1,
        48: 1,
        65: 1,
        80: -1,
        96: -2,
    }
    half_variance, diameter_square_mass, cross_sum = chord_ledger(witness)
    assert (half_variance, diameter_square_mass, cross_sum) == (18, 8, -38)
    assert half_variance == 102 - diameter_square_mass + 2 * cross_sum

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {entry["id"]: entry["status"] for entry in dag["nodes"]}
    statements = {entry["id"]: entry.get("statement", "") for entry in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[PARENT] == "PROVED"
    assert statuses[E1_TARGET] == "TARGET"
    assert statuses[UNIVERSAL_TARGET] == "TARGET"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, E1_TARGET, "ev") in edges
    assert (NODE, UNIVERSAL_TARGET, "ev") in edges
    assert "0<V<=82" in statements[NODE]
    assert "C<=-20" in statements[NODE]
    assert "circular Sidon" in statements[NODE]

    print(
        "E1_N256_S16_SIGNED_CHORD_COLLISION_GATE_PASS "
        "baseline=102 diameter_max=21 cross_max=-20 "
        "witness=18/8/-38"
    )


if __name__ == "__main__":
    main()
