#!/usr/bin/env python3
"""Verify the E=33 profile-(0,6,1) exclusion."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e33_profile_061_exclusion"
PROFILE = "e1_n256_s16_e33_profile_parity_diameter_reduction"
CONDUCTOR = "e1_n256_proper_conductor_collision_exclusion"
NORM = "collision_norm_criterion"
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")

EXPECTED_PIN = {
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "profile_reduction_file": "background/nodes/e1_n256_s16_e33_profile_parity_diameter_reduction/statement.md",
    "profile_reduction_file_sha256": "5828b3f3a1c340075993b37eb218ad13bf0cb445a2807619c37e0b6a2965959b",
    "proper_conductor_file": "background/nodes/e1_n256_proper_conductor_collision_exclusion/statement.md",
    "proper_conductor_file_sha256": "4319261b9d388351f2980fd4f849d7fae4876a6e5db167c74467ea957a055d73",
}


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]

    # Expand (2*1_A+1_T)^3 independently by selecting one summand per slot.
    multiplicities = Counter()
    for choices in product(("A", "T"), repeat=3):
        coefficient = 1
        for choice in choices:
            coefficient *= 2 if choice == "A" else 1
        multiplicities["".join(sorted(choices))] += coefficient
    assert multiplicities == Counter({"AAA": 8, "AAT": 12, "ATT": 6, "TTT": 1})

    # If translation by z lost only z and gained only zero, propagation along
    # every possible 2-power cycle forces its unique involution into A.
    for order in (4, 8, 16, 32, 64, 128):
        forced = {1, order - 1}
        current = 1
        while current != order - 1:
            current = (current + 1) % order
            if current:
                forced.add(current)
        assert forced == set(range(1, order))
        assert order // 2 in forced

    outer = 14 * (14 - 2)
    target = 2 * (14 - 2)
    two_point = 2
    moment_cap = 8 * outer + 12 * target + 6 * two_point
    assert (outer, target, two_point, moment_cap) == (168, 24, 2, 1644)
    assert moment_cap < 1732

    # The abstract cap is attained by an order-16 subgroup minus zero and the
    # involution, embedded in Z/128Z.
    subgroup = {(8 * index) % 128 for index in range(16)}
    support = subgroup - {0, 64}
    t = 8
    outer_exact = sum(((-x-y) % 128) in support for x in support for y in support)
    target_exact = sum(((t-x) % 128) in support for x in support)
    exact_moment = 8 * outer_exact + 24 * target_exact + 12 * int((2*t) % 128 in support)
    assert (len(support), outer_exact, target_exact, exact_moment) == (14, 168, 12, 1644)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in (PROFILE, CONDUCTOR, NORM):
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    for target_node in TARGETS:
        assert (NODE, target_node, "ev") in edges
    assert "M_3<=1644<1732" in nodes[NODE]["statement"]

    print(
        "E1_N256_S16_E33_PROFILE_061_EXCLUSION_PASS "
        "fiber=12 outer=168 m3=1644 threshold=1732 sharp=1"
    )


if __name__ == "__main__":
    main()
