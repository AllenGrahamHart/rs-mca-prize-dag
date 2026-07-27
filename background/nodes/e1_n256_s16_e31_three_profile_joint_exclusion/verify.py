#!/usr/bin/env python3
"""Verify the complete E31 three-profile joint exclusion."""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e31_three_profile_joint_exclusion"
DEPENDENCIES = {
    "e1_n256_s16_e31_profile_parity_light_reduction",
    "collision_norm_criterion",
    "e1_n256_proper_conductor_collision_exclusion",
}
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
PROFILES = {
    "profile_37": (3, 7, 0),
    "profile_251": (2, 5, 1),
    "profile_132": (1, 3, 2),
}
EXPECTED_SUMMARY = {
    "profile_37": {
        "count": 7204,
        "full_conductor": 3856,
        "maximum_m3": 1380,
        "maximum_full_conductor_m3": 1206,
    },
    "profile_251": {
        "count": 1590,
        "full_conductor": 472,
        "maximum_m3": 1068,
        "maximum_full_conductor_m3": 1062,
    },
    "profile_132": {
        "count": 388,
        "full_conductor": 84,
        "maximum_m3": 1122,
        "maximum_full_conductor_m3": 714,
    },
}
EXPECTED_PIN = {
    "audit_driver_file": "background/nodes/e1_n256_s16_e31_profile_parity_light_reduction/notes/e31_three_profile_joint_census_audit_modal.py",
    "audit_driver_file_sha256": "4d406a26abaf97ca5d0e9a6ed76f666cb33a593f67a65504a2359250ea05cd7d",
    "audit_result_file": "background/nodes/e1_n256_s16_e31_profile_parity_light_reduction/notes/e31_three_profile_joint_census_audit_result.json",
    "audit_result_file_sha256": "7ac6775735fac05a913b2ab369b5bc041905fdfe3c3f748a6dfa33ffdd068d49",
    "audit_source_file": "background/nodes/e1_n256_s16_e31_profile_parity_light_reduction/notes/e31_three_profile_joint_census_audit.cpp",
    "audit_source_file_sha256": "f547379a5da430f59f5d223eaa92311f849c9007d2990e5c8813e48a06fc86d6",
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "orbit_result_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e31_three_odd_light_orbit_result.json",
    "orbit_result_file_sha256": "dfa93a27a628267ec21ec3684ae8e567cce0f25bd836e31e4b55ae71ecce2ca6",
    "production_driver_file": "background/nodes/e1_n256_s16_e31_profile_parity_light_reduction/notes/e31_three_profile_joint_census_modal.py",
    "production_driver_file_sha256": "028caa53d581574feb233f6042d8bc1219371457f1080487a41de78813bddeba",
    "production_result_file": "background/nodes/e1_n256_s16_e31_profile_parity_light_reduction/notes/e31_three_profile_joint_census_result.json",
    "production_result_file_sha256": "df2edcac66e1affa2602cbe2539964e9ef5375d31e1e8f44e270fdadf42ebfe1",
    "production_source_file": "background/nodes/e1_n256_s16_e31_profile_parity_light_reduction/notes/e31_three_profile_joint_census.cpp",
    "production_source_file_sha256": "86fd65d6293cda0ab223ccd57f1f1a5e7082b041a07c724ad1a21c399ab9329b",
    "proper_conductor_file": "background/nodes/e1_n256_proper_conductor_collision_exclusion/statement.md",
    "proper_conductor_file_sha256": "4319261b9d388351f2980fd4f849d7fae4876a6e5db167c74467ea957a055d73",
    "reduction_file": "background/nodes/e1_n256_s16_e31_profile_parity_light_reduction/statement.md",
    "reduction_file_sha256": "3927e37cfeb01a2d327a777ec3df3cd7a5bbadc15934a3b346620982eac05f50",
}


def folded_half(positions: tuple[int, ...], coefficients: tuple[int, ...]) -> list[int]:
    half = [0] * 64
    for left, right in combinations(range(7), 2):
        low, high = sorted((positions[left], positions[right]))
        difference = high - low
        if difference == 64:
            continue
        orientation = 1 if difference < 64 else -1
        chord = difference if difference < 64 else 128 - difference
        half[chord] += orientation * coefficients[left] * coefficients[right]
    return half


def third_moment(half: list[int]) -> int:
    weight = [0] * 128
    support = []
    for difference in range(1, 64):
        magnitude = abs(half[difference])
        if magnitude:
            weight[difference] = weight[128 - difference] = magnitude
            support.extend((difference, 128 - difference))
    return sum(
        weight[left] * weight[right] * weight[(-left - right) % 128]
        for left in support
        for right in support
    )


def replay_witness(profile: str, witness: dict[str, object], full: bool) -> None:
    positions = tuple(map(int, witness["positions"]))  # type: ignore[arg-type]
    coefficients = tuple(map(int, witness["coefficients"]))  # type: ignore[arg-type]
    assert len(set(positions)) == len(positions) == 7
    assert coefficients[0] == 2
    assert all(abs(value) == 2 for value in coefficients[:3])
    assert all(abs(value) == 1 for value in coefficients[3:])
    half = folded_half(positions, coefficients)
    counts = Counter(abs(value) for value in half[1:] if value)
    expected = PROFILES[profile]
    assert tuple(counts[index] for index in (1, 2, 3)) == expected
    assert not any(magnitude > 3 for magnitude in counts)
    assert sum(value * value for value in half) == 31
    assert third_moment(half) == int(witness["m3"])
    conductor = math.gcd(256, *positions)
    if full:
        assert conductor == 1


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]

    production = json.loads((ROOT / pin["production_result_file"]).read_text())
    audit = json.loads((ROOT / pin["audit_result_file"]).read_text())
    orbits = json.loads((ROOT / pin["orbit_result_file"]).read_text())
    assert production["schema"] == "e1-e31-three-profile-joint-census-v1"
    assert audit["schema"] == "e1-e31-three-profile-joint-census-audit-v1"
    assert production["complete"] is audit["complete"] is audit["agreement"] is True
    assert production["completed_templates"] == production["expected_templates"] == 8
    assert audit["completed_templates"] == audit["expected_templates"] == 8
    assert production["summary"] == audit["summary"] == EXPECTED_SUMMARY
    assert production["orbits_sha256"] == audit["orbits_sha256"] == pin["orbit_result_file_sha256"]
    assert audit["production_sha256"] == pin["production_result_file_sha256"]
    assert production["source_sha256"] == pin["production_source_file_sha256"]
    assert audit["source_sha256"] == pin["audit_source_file_sha256"]

    expected_lights = [row["representative"] for row in orbits["rows"]]
    assert len(expected_lights) == 8
    expected_supports = math.comb(124, 3)
    expected_vectors = expected_supports * 64
    for engine in (production, audit):
        assert [row["template"] for row in engine["rows"]] == list(range(8))
        assert [row["light"] for row in engine["rows"]] == expected_lights
        assert all(row["supports"] == expected_supports for row in engine["rows"])
        assert all(row["vectors"] == expected_vectors for row in engine["rows"])
        assert sum(row["vectors"] for row in engine["rows"]) == 158_783_488

    for production_row, audit_row in zip(production["rows"], audit["rows"]):
        for profile in PROFILES:
            for field in (
                "count", "full_conductor", "maximum_m3", "maximum_full_conductor_m3"
            ):
                assert production_row[profile][field] == audit_row[profile][field]
            if production_row[profile]["count"]:
                replay_witness(profile, production_row[profile]["witness"], False)
            if production_row[profile]["full_conductor"]:
                replay_witness(profile, production_row[profile]["full_conductor_witness"], True)

    assert EXPECTED_SUMMARY["profile_251"]["maximum_m3"] < 1302
    assert EXPECTED_SUMMARY["profile_132"]["maximum_m3"] < 1302
    assert EXPECTED_SUMMARY["profile_37"]["maximum_full_conductor_m3"] < 1302
    assert EXPECTED_SUMMARY["profile_37"]["maximum_m3"] > 1302
    assert EXPECTED_SUMMARY["profile_37"]["count"] - EXPECTED_SUMMARY["profile_37"]["full_conductor"] == 3348

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    incoming = {source for source, target, kind in edges if target == NODE and kind == "req"}
    assert incoming == DEPENDENCIES
    assert all(nodes[dependency]["status"] == "PROVED" for dependency in DEPENDENCIES)
    for target in TARGETS:
        assert (NODE, target, "ev") in edges

    print(
        "E1_N256_S16_E31_THREE_PROFILE_JOINT_EXCLUSION_PASS "
        "templates=8 supports=2480992 vectors=158783488 profiles=3 engines=2"
    )


if __name__ == "__main__":
    main()
