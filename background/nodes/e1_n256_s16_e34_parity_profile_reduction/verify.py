#!/usr/bin/env python3
"""Verify the N=256 E=34 parity-profile reduction."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e34_parity_profile_reduction"
THREE_PROFILE = "e1_n256_s16_e34_three_profile_reduction"
SIGNED_CHORD = "e1_n256_s16_signed_chord_collision_gate"
E1_TARGET = "e1_official_prime_exception_control"
UNIVERSAL_TARGET = "unsafe_crossing_family_instantiation"

EXPECTED_PIN = {
    "signed_chord_file": "background/nodes/e1_n256_s16_signed_chord_collision_gate/statement.md",
    "signed_chord_file_sha256": "926f9c94a0b5dd0830b7e37fafcd96f570dd93802de16061c802546e466e3157",
    "three_profile_file": "background/nodes/e1_n256_s16_e34_three_profile_reduction/statement.md",
    "three_profile_file_sha256": "cd30b1ff438af39161421c577883ffc59278a316d71c28f11a85d8c9fd4c9f0c",
}


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for file_key, hash_key in (
        ("signed_chord_file", "signed_chord_file_sha256"),
        ("three_profile_file", "three_profile_file_sha256"),
    ):
        assert hashlib.sha256((ROOT / pin[file_key]).read_bytes()).hexdigest() == pin[hash_key]

    coefficient_magnitudes = (2, 2, 2, 1, 1, 1, 1)
    chord_magnitudes = Counter(
        left * right for left, right in combinations(coefficient_magnitudes, 2)
    )
    assert chord_magnitudes == Counter({2: 12, 1: 6, 4: 3})
    unit_supply = chord_magnitudes[1]

    profiles = ((6, 7, 0), (9, 4, 1), (12, 1, 2))
    assert all(
        sum((index + 1) * count for index, count in enumerate(profile)) == 20
        and sum((index + 1) ** 2 * count for index, count in enumerate(profile)) == 34
        for profile in profiles
    )
    odd_counts = tuple(profile[0] + profile[2] for profile in profiles)
    assert odd_counts == (6, 10, 14)
    survivors = tuple(profile for profile in profiles if profile[0] + profile[2] <= unit_supply)
    assert survivors == ((6, 7, 0),)

    diameter_ledgers = set()
    for diameter_4 in range(2):
        for diameter_2 in range(4):
            if 2 * diameter_4 + diameter_2 > 3:
                continue
            diameter_square_mass = 16 * diameter_4 + 4 * diameter_2
            cross_sum = (34 - 102 + diameter_square_mass) // 2
            diameter_ledgers.add((diameter_square_mass, cross_sum))
    assert diameter_ledgers == {
        (0, -34),
        (4, -32),
        (8, -30),
        (12, -28),
        (16, -26),
        (20, -24),
    }

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[THREE_PROFILE]["status"] == "PROVED"
    assert nodes[SIGNED_CHORD]["status"] == "PROVED"
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    assert (THREE_PROFILE, NODE, "req") in edges
    assert (SIGNED_CHORD, NODE, "req") in edges
    assert (NODE, E1_TARGET, "ev") in edges
    assert (NODE, UNIVERSAL_TARGET, "ev") in edges

    print(
        "E1_N256_S16_E34_PARITY_PROFILE_REDUCTION_PASS "
        f"unit_chords={unit_supply} odd_counts={odd_counts} diameter_ledgers={len(diameter_ledgers)}"
    )


if __name__ == "__main__":
    main()
