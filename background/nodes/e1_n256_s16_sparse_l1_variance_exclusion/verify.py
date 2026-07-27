#!/usr/bin/env python3
"""Verify the N=256 square-mass-16 sparse-L1 variance exclusion."""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_sparse_l1_variance_exclusion"
PARENT = "e1_n256_s16_high_variance_collision_exclusion"
NORM_PARENT = "collision_norm_criterion"
E1_TARGET = "e1_official_prime_exception_control"
UNIVERSAL_TARGET = "unsafe_crossing_family_instantiation"

EXPECTED_PIN = {
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "variance_parent_file": "background/nodes/e1_n256_s16_high_variance_collision_exclusion/statement.md",
    "variance_parent_file_sha256": "9ff382e14946f9797e29859e118893a239a2e0b6a452ddb38978bd42360cbfa0",
}

ROWS = (
    (112, 112, 56, 32, 80, 1714),
    (114, 118, 59, 33, 82, 1749),
    (120, 124, 62, 34, 84, 1785),
    (126, 130, 65, 35, 86, 1820),
    (132, 134, 67, 36, 88, 1855),
)


def integer_l1_maxima(max_energy: int) -> dict[int, int]:
    states = {(0, 0): 0}
    for count in range(21):
        for (energy, state_count), l1_norm in tuple(states.items()):
            if state_count != count:
                continue
            for value in range(1, math.isqrt(max_energy - energy) + 1):
                key = (energy + value * value, count + 1)
                states[key] = max(states.get(key, -1), l1_norm + value)
    return {
        energy: max(states.get((energy, count), -1) for count in range(22))
        for energy in range(max_energy + 1)
    }


def taylor(argument: Fraction, degree: int) -> Fraction:
    return sum(
        argument**index / math.factorial(index)
        for index in range(degree + 1)
    )


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for file_key, hash_key in (
        ("collision_norm_file", "collision_norm_file_sha256"),
        ("variance_parent_file", "variance_parent_file_sha256"),
    ):
        actual = hashlib.sha256((ROOT / pin[file_key]).read_bytes()).hexdigest()
        assert actual == pin[hash_key]

    maxima = integer_l1_maxima(67)
    expected = {
        56: 32,
        57: 33,
        58: 32,
        59: 33,
        60: 34,
        61: 33,
        62: 34,
        63: 35,
        64: 34,
        65: 35,
        66: 36,
        67: 35,
    }
    assert {energy: maxima[energy] for energy in expected} == expected

    excluded = []
    for lower_v, upper_v, upper_energy, upper_l1, bound, denominator in ROWS:
        assert all(
            maxima[energy] <= upper_l1
            for energy in range(lower_v // 2, upper_energy + 1)
        )
        assert bound == 16 + 2 * upper_l1
        assert 16 < Fraction(denominator, 32) < bound

        endpoint_exponent = (
            Fraction(bound - 16, 16)
            - Fraction((bound - 16) ** 2, denominator)
        )
        assert taylor(endpoint_exponent, 12) > Fraction(bound, 16)

        six_bit_exponent = Fraction(32 * lower_v, 3 * denominator)
        assert taylor(six_bit_exponent, 9) > 2
        excluded.extend(range(lower_v, upper_v + 1, 2))

    assert excluded == list(range(112, 136, 2))

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {entry["id"]: entry["status"] for entry in dag["nodes"]}
    statements = {entry["id"]: entry.get("statement", "") for entry in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[PARENT] == "PROVED"
    assert statuses[NORM_PARENT] == "PROVED"
    assert statuses[E1_TARGET] == "TARGET"
    assert statuses[UNIVERSAL_TARGET] == "TARGET"
    assert (PARENT, NODE, "req") in edges
    assert (NORM_PARENT, NODE, "req") in edges
    assert (NODE, E1_TARGET, "ev") in edges
    assert (NODE, UNIVERSAL_TARGET, "ev") in edges
    assert "112<=V<=134" in statements[NODE]
    assert "V<=110" in statements[NODE]

    print(
        "E1_N256_S16_SPARSE_L1_VARIANCE_EXCLUSION_PASS "
        "excluded=12 residual_max=110 majorants=5"
    )


if __name__ == "__main__":
    main()
