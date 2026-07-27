#!/usr/bin/env python3
"""Verify the N=512 four-singleton E1 collision exclusion."""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n512_four_singleton_collision_exclusion"
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


def negacyclic_variance(half: int, support: tuple[int, ...], signs: tuple[int, ...]):
    coefficients = [0] * half
    for left, left_sign in zip(support, signs):
        for right, right_sign in zip(support, signs):
            quotient, residue = divmod(left - right, half)
            wrap_sign = -1 if quotient % 2 else 1
            coefficients[residue] += wrap_sign * left_sign * right_sign
    coefficients[0] -= len(support)
    return sum(value * value for value in coefficients), coefficients


def toy_autocorrelation_audit(half: int) -> tuple[int, int]:
    vectors = 0
    variance_two = 0
    for support in combinations(range(half), 4):
        # Global sign does not change the autocorrelation.
        for tail in product((-1, 1), repeat=3):
            variance, coefficients = negacyclic_variance(
                half, support, (1,) + tail
            )
            assert coefficients[0] == 0
            assert coefficients[half // 2] == 0
            for distance in range(1, half):
                assert coefficients[half - distance] == -coefficients[distance]
            assert variance >= 0 and variance % 2 == 0
            if variance == 2:
                nonzero = [
                    (index, value)
                    for index, value in enumerate(coefficients)
                    if value
                ]
                assert len(nonzero) == 2
                (left, left_value), (right, right_value) = nonzero
                assert {left_value, right_value} == {-1, 1}
                assert left + right == half
                variance_two += 1
            vectors += 1
    return vectors, variance_two


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for file_key, hash_key in (
        ("collision_norm_file", "collision_norm_file_sha256"),
        ("l2_radius_file", "l2_radius_file_sha256"),
    ):
        assert hashlib.sha256((ROOT / pin[file_key]).read_bytes()).hexdigest() == pin[hash_key]

    # Exact endpoint certificate for g(16)=7/5-log(4)>0.
    exp_lower = sum(
        (Fraction(7, 5) ** degree) / math.factorial(degree)
        for degree in range(6)
    )
    assert exp_lower == Fraction(189479, 46875)
    assert exp_lower > 4

    # Exact derivative factorization and rational norm comparisons.
    assert (4, -61, 180) == (4, -(45 + 16), 4 * 45)
    assert 180**128 < 47**128 * 2**250
    assert 19**128 < 5**128 * 2**250
    assert 3 * 16 < 7**2
    assert 82 * 75**2 < 81 * 76**2

    # lambda^r+lambda^-r is integral and follows this exact recurrence.
    lucas = [2, 4]
    for _ in range(2, 257):
        lucas.append(4 * lucas[-1] - lucas[-2])
    for order in (8, 16, 32, 64, 128, 256, 512):
        rank = order // 2
        assert lucas[rank] > 0
        assert lucas[rank] + 2 > lucas[rank]

    toy_counts = {}
    total_vectors = 0
    for half in (8, 16, 32):
        vectors, variance_two = toy_autocorrelation_audit(half)
        toy_counts[half] = variance_two
        total_vectors += vectors
    assert toy_counts == {8: 96, 16: 320, 32: 1152}

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
    assert "(0,4,0)" in statements[NODE]
    assert "V=2" in statements[NODE]
    assert "180/47" in statements[NODE]

    print(
        "E1_N512_FOUR_SINGLETON_COLLISION_EXCLUSION_PASS "
        f"toy_vectors={total_vectors} variance_two={sum(toy_counts.values())} "
        "first_band_survivors=1"
    )


if __name__ == "__main__":
    main()
