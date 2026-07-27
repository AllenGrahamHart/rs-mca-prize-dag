#!/usr/bin/env python3
"""Verify the E1 folded-L2 norm radius and its DAG contract."""

from __future__ import annotations

import cmath
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_prime_field_l2_norm_collision_radius"
PRIME_PARENT = "e1_pair_feasible_prime_field_reduction"
NORM_PARENT = "collision_norm_criterion"
E1_TARGET = "e1_official_prime_exception_control"
UNIVERSAL_TARGET = "unsafe_crossing_family_instantiation"

EXPECTED_PIN = {
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "prime_field_file": "background/nodes/e1_pair_feasible_prime_field_reduction/statement.md",
    "prime_field_file_sha256": "f7b5ea3463c6b9101b854191a498015fedc89d1bf4a5a0c28b2b2f8b71157e7b",
}


def coefficient_profiles(swap_distance: int):
    for opposite_pairs in range(swap_distance + 1):
        for same_sign_pairs in range(swap_distance + 1):
            singles = 2 * swap_distance - 2 * opposite_pairs - 2 * same_sign_pairs
            if singles < 0:
                continue
            yield opposite_pairs, singles, same_sign_pairs


def check_orthogonality(order: int) -> int:
    half = order // 2
    root = cmath.exp(2j * cmath.pi / order)
    checks = 0
    for left in range(half):
        for right in range(half):
            total = sum(root ** (odd * (left - right)) for odd in range(1, order, 2))
            expected = half if left == right else 0
            assert abs(total - expected) < 1e-8
            checks += 1
    return checks


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for file_key, hash_key in (
        ("collision_norm_file", "collision_norm_file_sha256"),
        ("prime_field_file", "prime_field_file_sha256"),
    ):
        assert hashlib.sha256((ROOT / pin[file_key]).read_bytes()).hexdigest() == pin[hash_key]

    profile_checks = 0
    for swap_distance in range(1, 9):
        for opposite_pairs, singles, same_sign_pairs in coefficient_profiles(swap_distance):
            assert singles % 2 == 0
            square_sum = 4 * opposite_pairs + singles
            assert square_sum <= 4 * swap_distance
            if singles == 0 and same_sign_pairs == 0:
                assert opposite_pairs == swap_distance
            else:
                assert square_sum <= 4 * swap_distance - 2
            profile_checks += 1

    assert 14**64 < 1 << 250
    assert 4**64 < 1 << 250
    assert 2**128 < 1 << 250
    prize_budget = 317494674775468773183020924238786383963
    assert prize_budget << 128 > 1 << 250

    orthogonality_checks = sum(check_orthogonality(order) for order in (8, 16, 32))

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {entry["id"]: entry["status"] for entry in dag["nodes"]}
    statements = {entry["id"]: entry.get("statement", "") for entry in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[PRIME_PARENT] == "PROVED"
    assert statuses[NORM_PARENT] == "PROVED"
    assert statuses[E1_TARGET] == "TARGET"
    assert statuses[UNIVERSAL_TARGET] == "TARGET"
    assert (PRIME_PARENT, NODE, "req") in edges
    assert (NORM_PARENT, NODE, "req") in edges
    assert (NODE, E1_TARGET, "ev") in edges
    assert (NODE, UNIVERSAL_TARGET, "ev") in edges
    assert "s<=4" in statements[NODE]
    assert "s=1" in statements[NODE]

    print(
        "E1_PRIME_FIELD_L2_NORM_COLLISION_RADIUS_PASS "
        f"profile_checks={profile_checks} orthogonality_checks={orthogonality_checks}"
    )


if __name__ == "__main__":
    main()
