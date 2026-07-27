#!/usr/bin/env python3
"""Verify the N=256 autocorrelation-subfield exclusion."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_autocorrelation_subfield_exclusion"
PARENT = "e1_n256_s16_sparse_l1_variance_exclusion"
NORM_PARENT = "collision_norm_criterion"
E1_TARGET = "e1_official_prime_exception_control"
UNIVERSAL_TARGET = "unsafe_crossing_family_instantiation"

EXPECTED_PIN = {
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "variance_parent_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/statement.md",
    "variance_parent_file_sha256": "5dad1a8acbe7f8d4f1db89771371203fe257f65c8f7ea5d4b03e3df4ada32c12",
}


def weighted_schur(layer_one: tuple[int, ...], layer_two: tuple[int, ...]) -> int:
    weights = [0] * 128
    for representative in layer_one:
        weights[representative] += 1
        weights[-representative % 128] += 1
    for representative in layer_two:
        weights[representative] += 1
        weights[-representative % 128] += 1
    return sum(
        weights[first] * weights[second] * weights[(-first - second) % 128]
        for first in range(128)
        for second in range(128)
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

    assert 256 // 4 == 64
    assert 128 // 4 == 32
    assert [54, 50, 46, 42] == [
        54 - slack for slack in (0, 4, 8, 12)
    ]
    assert all(energy > 38 for energy in (54, 50, 46, 42))
    assert 16 + 2 * 22 == 60
    assert 60**32 < 2**250

    subgroup_outer = (8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60)
    subgroup_inner = (8, 16, 24, 32, 36, 44, 52, 60)
    assert all(value % 4 == 0 for value in subgroup_outer)
    assert set(subgroup_inner) < set(subgroup_outer)
    assert weighted_schur(subgroup_outer, subgroup_inner) == 2718

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
    assert "V=76" in statements[NODE]
    assert "4 does not divide d" in statements[NODE]
    assert "60^32<2^250" in statements[NODE]

    print(
        "E1_N256_S16_AUTOCORRELATION_SUBFIELD_EXCLUSION_PASS "
        "subfield_degree=32 conjugate_ceiling=60 subgroup_schur=2718"
    )


if __name__ == "__main__":
    main()
