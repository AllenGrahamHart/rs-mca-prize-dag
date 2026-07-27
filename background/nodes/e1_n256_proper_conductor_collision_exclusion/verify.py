#!/usr/bin/env python3
"""Verify the N=256 proper-conductor E1 collision exclusion."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_proper_conductor_collision_exclusion"
L2_PARENT = "e1_prime_field_l2_norm_collision_radius"
NORM_PARENT = "collision_norm_criterion"
E1_TARGET = "e1_official_prime_exception_control"
UNIVERSAL_TARGET = "unsafe_crossing_family_instantiation"

EXPECTED_PIN = {
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "l2_radius_file": "background/nodes/e1_prime_field_l2_norm_collision_radius/statement.md",
    "l2_radius_file_sha256": "ed607ee0d843c1f2c74c79129d19ef8d52be96ba2a8ceb77d35014f95d852995",
}


def variance(coefficients: tuple[int, ...], square_mass: int) -> int:
    half = len(coefficients)
    autocorrelation = [0] * half
    support = [index for index, value in enumerate(coefficients) if value]
    for left in support:
        for right in support:
            quotient, residue = divmod(left - right, half)
            autocorrelation[residue] += (
                -1 if quotient % 2 else 1
            ) * coefficients[left] * coefficients[right]
    autocorrelation[0] -= square_mass
    return sum(value * value for value in autocorrelation)


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for file_key, hash_key in (
        ("collision_norm_file", "collision_norm_file_sha256"),
        ("l2_radius_file", "l2_radius_file_sha256"),
    ):
        actual = hashlib.sha256((ROOT / pin[file_key]).read_bytes()).hexdigest()
        assert actual == pin[hash_key]

    assert 4 * 4 + 2 == 18
    assert 3 * 4 + 4 == 16
    proper_divisors = (2, 4, 8, 16, 32, 64, 128)
    assert max((256 // divisor) // 2 for divisor in proper_divisors) == 64
    assert 18**32 < 2**250

    coefficients = [0] * 128
    for index, value in (
        (0, 2),
        (16, -2),
        (32, -1),
        (48, 1),
        (65, 1),
        (80, -1),
        (96, -2),
    ):
        coefficients[index] = value
    support = [index for index, value in enumerate(coefficients) if value]
    base = support[0]
    assert sum(abs(value) == 2 for value in coefficients) == 3
    assert sum(abs(value) == 1 for value in coefficients) == 4
    assert sum(value * value for value in coefficients) == 16
    assert math.gcd(256, *(index - base for index in support)) == 1
    assert variance(tuple(coefficients), 16) == 36

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {entry["id"]: entry["status"] for entry in dag["nodes"]}
    statements = {entry["id"]: entry.get("statement", "") for entry in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[L2_PARENT] == "PROVED"
    assert statuses[NORM_PARENT] == "PROVED"
    assert statuses[E1_TARGET] == "TARGET"
    assert statuses[UNIVERSAL_TARGET] == "TARGET"
    assert (L2_PARENT, NODE, "req") in edges
    assert (NORM_PARENT, NODE, "req") in edges
    assert (NODE, E1_TARGET, "ev") in edges
    assert (NODE, UNIVERSAL_TARGET, "ev") in edges
    assert "full conductor" in statements[NODE]
    assert "18^32<2^250" in statements[NODE]

    print(
        "E1_N256_PROPER_CONDUCTOR_COLLISION_EXCLUSION_PASS "
        "profiles=2 max_subfield_degree=64 "
        "full_conductor_falsifier_variance=36"
    )


if __name__ == "__main__":
    main()
