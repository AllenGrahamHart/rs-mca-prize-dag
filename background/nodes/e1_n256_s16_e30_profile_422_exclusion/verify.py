#!/usr/bin/env python3
"""Verify the E30 profile-(4,2,2) exclusion packet."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e30_profile_422_exclusion"
PROFILE = "e1_n256_s16_e30_profile_parity_light_reduction"
CONDUCTOR = "e1_n256_proper_conductor_collision_exclusion"
NORM = "collision_norm_criterion"
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
MAXIMUM_NORM = 4039047355553663302249733085042470588482730556495866201164489362016333826
EXCEPTIONAL = [
    {
        "even_classes": [3, 4],
        "light": [0, 1, 6, 8],
        "m3": 1146,
        "odd_classes": [1, 2, 5, 6, 7, 8],
        "odd_mask": 243,
        "promoted_to_three": [1, 2],
    },
    {
        "even_classes": [6, 8],
        "light": [0, 2, 12, 16],
        "m3": 1146,
        "odd_classes": [2, 4, 10, 12, 14, 16],
        "odd_mask": 43530,
        "promoted_to_three": [2, 4],
    },
    {
        "even_classes": [12, 16],
        "light": [0, 4, 24, 32],
        "m3": 1146,
        "odd_classes": [4, 8, 20, 24, 28, 32],
        "odd_mask": 2290614408,
        "promoted_to_three": [4, 8],
    },
]
EXPECTED_PIN = {
    "actual_audit_source_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_profile422_exceptional_actual_audit.cpp",
    "actual_audit_source_file_sha256": "7653641953cc2b6d7e0a2d43cb0db38b59d32f7352328198311a946a295424c9",
    "actual_driver_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_profile422_exceptional_actual_modal.py",
    "actual_driver_file_sha256": "5149cb343e335b1919bdd00596bd52ac682a2cb54e0aebf69e3b4d04761f6c75",
    "actual_production_source_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_profile422_exceptional_actual_census.cpp",
    "actual_production_source_file_sha256": "a9ec3e5def3fc685dd34fb4e41b5f909fffd2384203cf90e321b1d40b69feb1a",
    "actual_result_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_profile422_exceptional_actual_result.json",
    "actual_result_file_sha256": "f79ac5f852463cf89f37b5fed2929d082664cce58be45b0b8e659059087d4bb5",
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "conductor_file": "background/nodes/e1_n256_proper_conductor_collision_exclusion/statement.md",
    "conductor_file_sha256": "4319261b9d388351f2980fd4f849d7fae4876a6e5db167c74467ea957a055d73",
    "norm_driver_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_profile422_exceptional_norm_modal.py",
    "norm_driver_file_sha256": "5ab83368ef26c4994d4d48392b577bf5d58ef0b131ce64884ffb29befd114ede",
    "norm_result_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_profile422_exceptional_norm_result.json",
    "norm_result_file_sha256": "2bf121d2f359b0a39fd07c22259a06069ada017542e06960a1c3a018c4a14f3b",
    "profile_reduction_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/statement.md",
    "profile_reduction_file_sha256": "7d988ae69d03e78167eea76ca9746782b35627bb9fde645a187a121ee291aef4",
    "relaxation_audit_driver_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_profile422_odd_difference_relaxation_audit_modal.py",
    "relaxation_audit_driver_file_sha256": "97f24e92a3e2e34ab6d8abae554622861e6e85a538071e5bef6c365294c9e4b2",
    "relaxation_audit_result_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_profile422_odd_difference_relaxation_audit_result.json",
    "relaxation_audit_result_file_sha256": "6d6accd48705887225810791d10788a333a10031761ff2f8f196186fe15ab20a",
    "relaxation_audit_source_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_profile422_odd_difference_relaxation_audit.cpp",
    "relaxation_audit_source_file_sha256": "407f7f04b2fc304c4dd7fa1724c82ac977d412b45ac7d461d5a486bb1cf4e664",
    "relaxation_driver_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_profile422_odd_difference_relaxation_modal.py",
    "relaxation_driver_file_sha256": "5d04f0ac7695266b6cfcb211f9ac862a6b3bc17dea83b2839b1b8ed5fec6a63f",
    "relaxation_result_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_profile422_odd_difference_relaxation_result.json",
    "relaxation_result_file_sha256": "9ec8c7757b38d92b17ed9adeadf71083a62a4eb2aa29074fa4051df5a7028ae8",
    "relaxation_source_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_profile422_odd_difference_relaxation.cpp",
    "relaxation_source_file_sha256": "93dae1d933f50288ea7a389253fd54311799f2e989921eb5a730c1e98199dd41",
}


def replay_vector(vector: dict[str, object], template: int) -> int:
    positions = tuple(int(value) for value in vector["positions"])
    coefficients = tuple(int(value) for value in vector["coefficients"])
    assert len(positions) == len(coefficients) == 7 and len(set(positions)) == 7
    assert sorted(abs(value) for value in coefficients) == [1, 1, 1, 1, 2, 2, 2]
    product = [0] * 128
    for left, left_value in zip(positions, coefficients):
        for right, right_value in zip(positions, coefficients):
            quotient, residue = divmod(left - right, 128)
            product[residue] += (-1 if quotient % 2 else 1) * left_value * right_value
    assert product[0] == 16
    assert all(product[128 - difference] == -product[difference] for difference in range(1, 64))
    magnitudes = [abs(product[difference]) for difference in range(1, 64)]
    assert tuple(magnitudes.count(value) for value in (1, 2, 3)) == (4, 2, 2)
    expected = {distance: 1 for distance in EXCEPTIONAL[template]["odd_classes"]}
    expected.update({distance: 3 for distance in EXCEPTIONAL[template]["promoted_to_three"]})
    expected.update({distance: 2 for distance in EXCEPTIONAL[template]["even_classes"]})
    assert all(magnitudes[distance - 1] == expected.get(distance, 0) for distance in range(1, 64))
    weights = [0] * 128
    for difference, magnitude in enumerate(magnitudes, start=1):
        weights[difference] = weights[128 - difference] = magnitude
    m3 = sum(
        weights[left] * weights[right] * weights[(-left - right) % 128]
        for left in range(128)
        for right in range(128)
        if weights[left] and weights[right]
    )
    assert m3 == 1146
    return math.gcd(256, *positions)


def check_relaxations(production: dict[str, object], audit: dict[str, object]) -> None:
    assert production["schema"] == "e1-e30-profile422-odd-difference-relaxation-v1"
    assert audit["schema"] == "e1-e30-profile422-odd-difference-relaxation-audit-v1"
    assert production["complete"] is audit["complete"] is True
    assert production["completed_shards"] == production["expected_shards"] == 4
    assert audit["completed_shards"] == audit["expected_shards"] == 4
    assert production["source_sha256"] == EXPECTED_PIN["relaxation_source_file_sha256"]
    assert audit["source_sha256"] == EXPECTED_PIN["relaxation_audit_source_file_sha256"]
    assert audit["production_sha256"] == EXPECTED_PIN["relaxation_result_file_sha256"]
    first = {int(row["shard"]): row for row in production["rows"]}
    second = {int(row["shard"]): row for row in audit["rows"]}
    assert set(first) == set(second) == set(range(4))
    expected_masks = [309, 309, 308, 308]
    expected_assignments = [7_397_460, 7_397_460, 7_373_520, 7_373_520]
    expected_maxima = [1050, 1062, 1050, 1146]
    for shard in range(4):
        left = first[shard]
        right = second[shard]
        for key in (
            "shards",
            "normalized_six_odd_supports",
            "distinct_odd_masks",
            "tested_masks",
            "assignments",
            "above_threshold",
            "above_histogram",
            "threshold",
            "maximum_m3",
            "witness",
            "exceptional",
        ):
            assert left[key] == right[key]
        assert int(left["normalized_six_odd_supports"]) == 280_720
        assert int(left["distinct_odd_masks"]) == 1_234
        assert int(left["tested_masks"]) == expected_masks[shard]
        assert int(left["assignments"]) == expected_assignments[shard]
        assert int(left["maximum_m3"]) == expected_maxima[shard]
        assert int(left["above_threshold"]) == (3 if shard == 3 else 0)
    assert production["summary"]["assignments"] == audit["summary"]["assignments"] == 29_541_960
    assert production["summary"]["above_threshold"] == audit["summary"]["above_threshold"] == 3
    assert production["summary"]["maximum_m3"] == audit["summary"]["maximum_m3"] == 1146
    assert production["summary"]["exceptional"] == EXCEPTIONAL
    assert 1_234 * math.comb(6, 2) * math.comb(57, 2) == 29_541_960
    orbit_rows = [row for row in production["rows"] if row["exceptional_light_orbits"]]
    assert len(orbit_rows) == 1
    assert orbit_rows[0]["exceptional_light_orbits"] == [
        {"odd_mask": row["odd_mask"], "orbits": [row["light"]]} for row in EXCEPTIONAL
    ]


def check_actual(packet: dict[str, object]) -> list[dict[str, object]]:
    assert packet["schema"] == "e1-e30-profile422-exceptional-actual-v1"
    assert packet["complete"] is packet["agreement"] is True
    assert packet["completed_production"] == packet["completed_audit"] == packet["expected_each"] == 3
    assert packet["production_source_sha256"] == EXPECTED_PIN["actual_production_source_file_sha256"]
    assert packet["audit_source_sha256"] == EXPECTED_PIN["actual_audit_source_file_sha256"]
    assert packet["relaxation_sha256"] == EXPECTED_PIN["relaxation_result_file_sha256"]
    first = sorted(packet["production"], key=lambda row: int(row["template"]))
    second = sorted(packet["audit"], key=lambda row: int(row["template"]))
    assert len(first) == len(second) == 3
    for template, (left, right) in enumerate(zip(first, second)):
        for key in ("template", "light", "supports", "vectors", "count", "full_conductor", "witness", "matches"):
            assert left[key] == right[key]
        assert int(left["template"]) == template
        assert left["light"] == EXCEPTIONAL[template]["light"]
        assert int(left["supports"]) == 310_124
        assert int(left["vectors"]) == 19_847_936
        assert int(left["count"]) == len(left["matches"]) == 2
        conductors = [replay_vector(vector, template) for vector in left["matches"]]
        expected_conductor = 1 if template == 0 else 2**template
        assert conductors == [expected_conductor, expected_conductor]
        assert int(left["full_conductor"]) == (2 if template == 0 else 0)
    summary = packet["summary"]
    assert int(summary["vectors_per_engine"]) == 59_543_808
    assert int(summary["count"]) == 6
    assert int(summary["full_conductor"]) == 2
    return first[0]["matches"]


def check_norms(packet: dict[str, object], primitive: list[dict[str, object]]) -> None:
    assert packet["schema"] == "e1-e30-profile422-exceptional-norm-v1"
    assert packet["complete"] is packet["agreement"] is True
    assert packet["actual_sha256"] == EXPECTED_PIN["actual_result_file_sha256"]
    assert packet["vectors"] == primitive
    assert packet["flint_norms"] == packet["pari_norms"] == [MAXIMUM_NORM, MAXIMUM_NORM]
    assert packet["summary"] == {
        "maximum_norm": MAXIMUM_NORM,
        "maximum_norm_bits": 242,
        "norm_at_or_above_2_250": 0,
    }
    first = dict(zip(primitive[0]["positions"], primitive[0]["coefficients"]))
    second = dict(zip(primitive[1]["positions"], primitive[1]["coefficients"]))
    assert all(second.get(exponent, 0) == (-1) ** exponent * first.get(exponent, 0) for exponent in range(128))
    assert 447 * MAXIMUM_NORM < 2**250 < 448 * MAXIMUM_NORM


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]
    production = json.loads((ROOT / pin["relaxation_result_file"]).read_text())
    audit = json.loads((ROOT / pin["relaxation_audit_result_file"]).read_text())
    check_relaxations(production, audit)
    actual = json.loads((ROOT / pin["actual_result_file"]).read_text())
    primitive = check_actual(actual)
    norms = json.loads((ROOT / pin["norm_result_file"]).read_text())
    check_norms(norms, primitive)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in (PROFILE, CONDUCTOR, NORM):
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "29,541,960" in nodes[NODE]["statement"]
    assert "447*N_max<2^250" in nodes[NODE]["statement"]

    print(
        "E1_N256_S16_E30_PROFILE_422_EXCLUSION_PASS "
        "masks=1234 assignments=29541960 exceptions=3 actual=6 full=2 "
        "max_bits=242 engines=6"
    )


if __name__ == "__main__":
    main()
