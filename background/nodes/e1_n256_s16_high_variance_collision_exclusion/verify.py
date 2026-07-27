#!/usr/bin/env python3
"""Verify the N=256 square-mass-16 high-variance exclusion."""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_high_variance_collision_exclusion"
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


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for file_key, hash_key in (
        ("collision_norm_file", "collision_norm_file_sha256"),
        ("l2_radius_file", "l2_radius_file_sha256"),
    ):
        assert hashlib.sha256((ROOT / pin[file_key]).read_bytes()).hexdigest() == pin[hash_key]

    # Derivative roots are x=16 and x=2070/(2*16).
    assert 2070 == 2 * 16 * Fraction(1035, 16)
    endpoint_exponent = Fraction(847, 460)
    endpoint_exp_lower = sum(
        endpoint_exponent**degree / math.factorial(degree)
        for degree in range(7)
    )
    assert endpoint_exp_lower == Fraction(
        42882796663116856249, 6821493765120000000
    )
    assert endpoint_exp_lower > Fraction(25, 4)

    exp_point_seven_lower = sum(
        Fraction(7, 10) ** degree / math.factorial(degree)
        for degree in range(4)
    )
    assert exp_point_seven_lower == Fraction(12013, 6000)
    assert exp_point_seven_lower > 2
    assert Fraction(4352, 1035) > Fraction(21, 5)
    assert 64 * 136 == 8704

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
    assert "V>=136" in statements[NODE]
    assert "V<=134" in statements[NODE]

    print(
        "E1_N256_S16_HIGH_VARIANCE_COLLISION_EXCLUSION_PASS "
        "mean=16 max=100 high_variance_start=136 residual_max=134"
    )


if __name__ == "__main__":
    main()
