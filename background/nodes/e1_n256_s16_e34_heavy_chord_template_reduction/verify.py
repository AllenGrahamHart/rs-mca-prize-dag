#!/usr/bin/env python3
"""Verify the E34 heavy-chord template reduction."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e34_heavy_chord_template_reduction"
PARITY = "e1_n256_s16_e34_parity_profile_reduction"
SIGNED = "e1_n256_s16_signed_chord_collision_gate"
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")

EXPECTED_PIN = {
    "parity_profile_file": "background/nodes/e1_n256_s16_e34_parity_profile_reduction/statement.md",
    "parity_profile_file_sha256": "90a546f51956446dbc188ed467c700a51ab505a081e9e5731877076412ce19fe",
    "signed_chord_file": "background/nodes/e1_n256_s16_signed_chord_collision_gate/statement.md",
    "signed_chord_file_sha256": "926f9c94a0b5dd0830b7e37fafcd96f570dd93802de16061c802546e466e3157",
}


def distance(left: int, right: int) -> int:
    delta = (right - left) % 128
    return min(delta, 128 - delta)


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for file_key, hash_key in (
        ("parity_profile_file", "parity_profile_file_sha256"),
        ("signed_chord_file", "signed_chord_file_sha256"),
    ):
        assert hashlib.sha256((ROOT / pin[file_key]).read_bytes()).hexdigest() == pin[hash_key]

    # A singleton magnitude-four chord plus at most one unit chord cannot
    # produce one of the residual magnitudes 0, 1, 2.
    singleton_outputs = {
        abs(4 * heavy_sign + unit)
        for heavy_sign in (-1, 1)
        for unit in (-1, 0, 1)
    }
    assert singleton_outputs == {3, 4, 5}
    pair_outputs = {
        (first, second, unit, abs(4 * first + 4 * second + unit))
        for first, second, unit in product((-1, 1), (-1, 1), (-1, 0, 1))
    }
    assert all(
        first == -second
        for first, second, _, output in pair_outputs
        if output <= 2
    )

    cases = Counter()
    for heavy in combinations(range(128), 3):
        lengths = [distance(left, right) for left, right in combinations(heavy, 2)]
        diameter_count = lengths.count(64)
        assert diameter_count <= 1
        non_diameter = [value for value in lengths if value != 64]
        distinct = len(set(non_diameter))
        if diameter_count:
            assert len(non_diameter) == 2
            if distinct == 1:
                assert non_diameter == [32, 32]
                cases["quarter"] += 1
            else:
                assert distinct == 2
                cases["diameter"] += 1
        else:
            assert distinct in (2, 3)
            cases["progression" if distinct == 2 else "generic"] += 1
    assert sum(cases.values()) == 341376
    assert all(cases[name] > 0 for name in ("quarter", "diameter", "progression", "generic"))

    # Exact distance-32 sign ledger in the normalized quarter template.
    with_missing_quarter = {
        abs(4 * s1 * (s0 + s2) + 2 * light * (s2 - s0))
        for s0, s1, s2, light in product((-1, 1), repeat=4)
    }
    assert with_missing_quarter == {4, 8}
    without_missing_quarter = {
        (s0, s2, unit, abs(4 * s1 * (s0 + s2) + unit))
        for s0, s1, s2 in product((-1, 1), repeat=3)
        for unit in (-1, 0, 1)
    }
    assert all(
        s2 == -s0
        for s0, s2, _, output in without_missing_quarter
        if output <= 2
    )

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[PARITY]["status"] == "PROVED"
    assert nodes[SIGNED]["status"] == "PROVED"
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    assert (PARITY, NODE, "req") in edges
    assert (SIGNED, NODE, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges

    print(
        "E1_N256_S16_E34_HEAVY_CHORD_TEMPLATE_REDUCTION_PASS "
        f"triples={sum(cases.values())} cases={dict(sorted(cases.items()))}"
    )


if __name__ == "__main__":
    main()
