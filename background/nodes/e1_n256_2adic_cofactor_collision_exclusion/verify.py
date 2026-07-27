#!/usr/bin/env python3
"""Verify the N=256 2-adic cofactor collision exclusion."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_2adic_cofactor_collision_exclusion"
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


def multiplicity_at_one(exponents: tuple[int, ...]) -> int:
    for degree in range(128):
        hasse_value = sum(
            math.comb(exponent, degree) for exponent in exponents
        )
        if hasse_value % 2:
            return degree
    raise AssertionError("nonzero degree-below-128 polynomial vanished to order 128")


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for file_key, hash_key in (
        ("collision_norm_file", "collision_norm_file_sha256"),
        ("l2_radius_file", "l2_radius_file_sha256"),
    ):
        actual = hashlib.sha256((ROOT / pin[file_key]).read_bytes()).hexdigest()
        assert actual == pin[hash_key]

    assert 16**64 == 2**256
    assert 18**64 < 2**267
    assert max(
        (integer & -integer).bit_length() - 1 for integer in range(1, 64)
    ) == 5
    assert max(
        (integer & -integer).bit_length() - 1
        for integer in range(1, 2**17)
    ) == 16

    for separation in range(1, 128):
        expected = separation & -separation
        assert multiplicity_at_one((0, separation)) == expected
        assert (expected <= 16) == (separation % 32 != 0)

    assert multiplicity_at_one((32, 48, 65, 80)) == 1
    assert multiplicity_at_one((0, 8, 16, 24)) == 24

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
    assert "mu<=5" in statements[NODE]
    assert "not divisible by 32" in statements[NODE]

    print(
        "E1_N256_2ADIC_COFACTOR_COLLISION_EXCLUSION_PASS "
        "s16_mu_max=5 s18_mu_max=16 gap_modulus=32"
    )


if __name__ == "__main__":
    main()
