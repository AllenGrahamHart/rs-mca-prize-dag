#!/usr/bin/env python3
"""Verify the E30 profile-(5,4,1) exclusion packet."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e30_profile_541_exclusion"
PROFILE = "e1_n256_s16_e30_profile_parity_light_reduction"
CONDUCTOR = "e1_n256_proper_conductor_collision_exclusion"
NORM = "collision_norm_criterion"
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
STAGES = (
    "e1_n256_s16_e30_profile_541_relaxation_certificate",
    "e1_n256_s16_e30_profile_541_actual_census_certificate",
    "e1_n256_s16_e30_profile_541_primitive_norm_certificate",
)
MAXIMUM_NORM = 147314768947604483837877250659211387932426327951806688176613401078756416516
EXPECTED_PIN = {
    "actual_audit_driver_file": "background/nodes/e1_n256_s16_e30_profile_541_exclusion/notes/e30_profile541_exceptional_actual_audit_modal.py",
    "actual_audit_driver_file_sha256": "013f10765d96086029843a9e0b59d44c9154c7b6c9dff34625fd80a0808885d7",
    "actual_audit_result_file": "background/nodes/e1_n256_s16_e30_profile_541_exclusion/notes/e30_profile541_exceptional_actual_audit_result.json",
    "actual_audit_result_file_sha256": "557baddc97ea4df7605283bab3dc12a5f3c193da991f33203959f3313b625f19",
    "actual_audit_source_file": "background/nodes/e1_n256_s16_e30_profile_541_exclusion/notes/e30_profile541_exceptional_actual_audit.cpp",
    "actual_audit_source_file_sha256": "1c95e6c3dd98c71ad30a00a46dbe2425547eef09aa4392655ef33bd69c9a019c",
    "actual_driver_file": "background/nodes/e1_n256_s16_e30_profile_541_exclusion/notes/e30_profile541_exceptional_actual_modal.py",
    "actual_driver_file_sha256": "fdab49053b30ffded08dbf02b180d913e5164fa71e8f91b5f4fb6dd3a3c831ca",
    "actual_result_file": "background/nodes/e1_n256_s16_e30_profile_541_exclusion/notes/e30_profile541_exceptional_actual_result.json",
    "actual_result_file_sha256": "7f591ad710e4010e6a9ebc1893ff7ad7ff318299d90ce9b36786d486c2f7c8e9",
    "actual_source_file": "background/nodes/e1_n256_s16_e30_profile_541_exclusion/notes/e30_profile541_exceptional_actual_census.cpp",
    "actual_source_file_sha256": "049a9f35ea392f6dea548d710fdd80d2db4eb2346ddebf1607913b5507e2acd6",
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "conductor_file": "background/nodes/e1_n256_proper_conductor_collision_exclusion/statement.md",
    "conductor_file_sha256": "4319261b9d388351f2980fd4f849d7fae4876a6e5db167c74467ea957a055d73",
    "norm_driver_file": "background/nodes/e1_n256_s16_e30_profile_541_exclusion/notes/e30_profile541_exceptional_norm_modal.py",
    "norm_driver_file_sha256": "faf428d56bbe7305ea068629296e25103e0f1688e6d75bbdba57adfb1abd02b0",
    "norm_result_file": "background/nodes/e1_n256_s16_e30_profile_541_exclusion/notes/e30_profile541_exceptional_norm_result.json",
    "norm_result_file_sha256": "9c6a208ac0cb9e26c41d60a53b74495b93f89de79972258bbd8b9e906317f44b",
    "orbit_driver_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_six_odd_mask_orbits_modal.py",
    "orbit_driver_file_sha256": "d583d6de5bf84ee47d6ce4a9444d1c6bbac9f287c4f3b07ef41032c9eed71023",
    "orbit_result_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_six_odd_mask_orbits_result.json",
    "orbit_result_file_sha256": "661ef642bdfafe5f0f261057877d2ad41b46a36b86e4167d8cb682b317e5b001",
    "orbit_source_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_six_odd_mask_orbits.cpp",
    "orbit_source_file_sha256": "3f7c4464655e91fe3c4f89aacff778ed34268f557381155be5ee24a8fdc4dfe2",
    "profile_reduction_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/statement.md",
    "profile_reduction_file_sha256": "7d988ae69d03e78167eea76ca9746782b35627bb9fde645a187a121ee291aef4",
    "relaxation_audit_driver_file": "background/nodes/e1_n256_s16_e30_profile_541_exclusion/notes/e30_profile541_odd_difference_relaxation_audit_modal.py",
    "relaxation_audit_driver_file_sha256": "d9805c26679f999182dc783b412beda551053bc516e5a38d7caa50da514ae62a",
    "relaxation_audit_result_file": "background/nodes/e1_n256_s16_e30_profile_541_exclusion/notes/e30_profile541_odd_difference_relaxation_audit_result.json",
    "relaxation_audit_result_file_sha256": "9a75bb5b51d95a1280979ce4c9180cd19614cf7c278f6764f97de504dda053e4",
    "relaxation_audit_source_file": "background/nodes/e1_n256_s16_e30_profile_541_exclusion/notes/e30_profile541_odd_difference_relaxation_audit.cpp",
    "relaxation_audit_source_file_sha256": "bfd7f6a5ab7c907ec180f56fa8e77ba00da74b1f324b34fc5b88f9c45f53bb08",
    "relaxation_driver_file": "background/nodes/e1_n256_s16_e30_profile_541_exclusion/notes/e30_profile541_odd_difference_relaxation_modal.py",
    "relaxation_driver_file_sha256": "0fce2ee7c78a3636c26fb56bef781966a0e288e4ebdc6a7b54488d30018565e7",
    "relaxation_result_file": "background/nodes/e1_n256_s16_e30_profile_541_exclusion/notes/e30_profile541_odd_difference_relaxation_result.json",
    "relaxation_result_file_sha256": "d2c75cb89bbe4645ac82bd9ce8ccbe526872f1423fb54579ba97e8488b5cade9",
    "relaxation_source_file": "background/nodes/e1_n256_s16_e30_profile_541_exclusion/notes/e30_profile541_odd_difference_relaxation.cpp",
    "relaxation_source_file_sha256": "b43b1ffde26ce9f1b961172e5c26a826f2f785b8b0b986f3530cbac1c37251f5",
}


def replay_vector(vector: dict[str, object]) -> tuple[int, int]:
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
    assert tuple(magnitudes.count(value) for value in (1, 2, 3)) == (5, 4, 1)
    weights = [0] * 128
    for difference, magnitude in enumerate(magnitudes, start=1):
        weights[difference] = weights[128 - difference] = magnitude
    support = [index for index, value in enumerate(weights) if value]
    m3 = sum(
        weights[left] * weights[right] * weights[(-left - right) % 128]
        for left in support
        for right in support
    )
    assert m3 == int(vector["m3"]) > 1087
    conductor = math.gcd(256, *positions)
    assert conductor == int(vector["conductor"])
    return conductor, m3


def check_orbits(packet: dict[str, object]) -> dict[int, list[list[int]]]:
    assert packet["schema"] == "e1-e30-six-odd-mask-orbits-v1"
    assert packet["complete"] is True
    assert packet["completed_shards"] == packet["expected_shards"] == 4
    assert packet["source_sha256"] == EXPECTED_PIN["orbit_source_file_sha256"]
    assert packet["summary"]["normalized_six_odd_supports"] == 280_720
    assert packet["summary"]["distinct_odd_masks"] == 1_234
    assert packet["summary"]["affine_light_orbits"] == 1_234
    assert packet["summary"]["orbits_per_mask_histogram"] == {"1": 1_234}
    rows = {int(row["odd_mask"]): row["orbits"] for row in packet["rows"]}
    assert len(rows) == 1_234 and all(len(orbits) == 1 for orbits in rows.values())
    return rows


def check_relaxations(production: dict[str, object], audit: dict[str, object]) -> set[int]:
    assert production["schema"] == "e1-e30-profile541-odd-difference-relaxation-v1"
    assert audit["schema"] == "e1-e30-profile541-odd-difference-relaxation-audit-v1"
    assert production["complete"] is audit["complete"] is True
    assert production["completed_shards"] == production["expected_shards"] == 64
    assert audit["completed_shards"] == audit["expected_shards"] == 64
    assert production["source_sha256"] == EXPECTED_PIN["relaxation_source_file_sha256"]
    assert audit["source_sha256"] == EXPECTED_PIN["relaxation_audit_source_file_sha256"]
    assert audit["production_sha256"] == EXPECTED_PIN["relaxation_result_file_sha256"]
    first = {int(row["shard"]): row for row in production["rows"]}
    second = {int(row["shard"]): row for row in audit["rows"]}
    assert set(first) == set(second) == set(range(64))
    shared = (
        "shards", "normalized_six_odd_supports", "distinct_odd_masks",
        "tested_masks", "assignments", "above_threshold", "above_histogram",
        "threshold", "maximum_m3", "witness", "exceptional",
    )
    for shard in range(64):
        assert all(first[shard][key] == second[shard][key] for key in shared)
        assert int(first[shard]["normalized_six_odd_supports"]) == 280_720
        assert int(first[shard]["distinct_odd_masks"]) == 1_234
    assert production["summary"]["assignments"] == audit["summary"]["assignments"] == 2_924_654_040
    assert production["summary"]["above_threshold"] == audit["summary"]["above_threshold"] == 1_456
    assert production["summary"]["maximum_m3"] == audit["summary"]["maximum_m3"] == 1_278
    exceptional = production["summary"]["exceptional"]
    assert len(exceptional) == 1_456
    assert 1_234 * 6 * math.comb(57, 4) == 2_924_654_040
    return {int(row["odd_mask"]) for row in exceptional}


def check_actual(
    production: dict[str, object],
    audit: dict[str, object],
    tasks: list[list[int]],
) -> list[dict[str, object]]:
    assert production["schema"] == "e1-e30-profile541-exceptional-actual-v1"
    assert audit["schema"] == "e1-e30-profile541-exceptional-actual-audit-v1"
    assert production["complete"] is audit["complete"] is audit["agreement"] is True
    assert production["completed_templates"] == production["expected_templates"] == 321
    assert audit["completed_templates"] == audit["expected_templates"] == 321
    assert production["source_sha256"] == EXPECTED_PIN["actual_source_file_sha256"]
    assert audit["source_sha256"] == EXPECTED_PIN["actual_audit_source_file_sha256"]
    assert audit["production_sha256"] == EXPECTED_PIN["actual_result_file_sha256"]
    assert production["relaxation_sha256"] == audit["relaxation_sha256"] == EXPECTED_PIN["relaxation_result_file_sha256"]
    assert production["orbits_sha256"] == audit["orbits_sha256"] == EXPECTED_PIN["orbit_result_file_sha256"]
    first = sorted(production["rows"], key=lambda row: int(row["template"]))
    second = sorted(audit["rows"], key=lambda row: int(row["template"]))
    assert len(first) == len(second) == len(tasks) == 321
    matches = []
    for template, (left, right, light) in enumerate(zip(first, second, tasks)):
        for key in (
            "template", "light", "supports", "vectors", "profile_count",
            "above_cutoff", "full_above_cutoff", "maximum_m3",
            "maximum_full_m3", "matches",
        ):
            assert left[key] == right[key]
        assert int(left["template"]) == template and left["light"] == light
        assert int(left["supports"]) == 310_124
        assert int(left["vectors"]) == 19_847_936
        assert int(left["above_cutoff"]) == len(left["matches"])
        for vector in left["matches"]:
            replay_vector(vector)
            matches.append(vector)
    assert sum(int(row["profile_count"]) for row in first) == 45_846
    assert len(matches) == sum(int(row["above_cutoff"]) for row in first) == 440
    assert sum(int(row["full_above_cutoff"]) for row in first) == 86
    assert sum(int(row["vectors"]) for row in first) == 6_371_187_456
    for packet in (production, audit):
        summary = packet["summary"]
        assert int(summary["vectors"]) == 6_371_187_456
        assert int(summary["profile_count"]) == 45_846
        assert int(summary["above_cutoff"]) == 440
        assert int(summary["full_above_cutoff"]) == 86
        assert int(summary["maximum_m3"]) == int(summary["maximum_full_m3"]) == 1_278
    return [vector for vector in matches if int(vector["conductor"]) == 1]


def check_norms(packet: dict[str, object], vectors: list[dict[str, object]]) -> None:
    assert packet["schema"] == "e1-e30-profile541-exceptional-norm-v1"
    assert packet["complete"] is packet["agreement"] is True
    assert packet["actual_sha256"] == EXPECTED_PIN["actual_result_file_sha256"]
    assert packet["vectors"] == vectors and len(vectors) == 86
    assert packet["flint_norms"] == packet["pari_norms"]
    assert len(packet["flint_norms"]) == 86
    assert packet["summary"] == {
        "distinct_norms": 42,
        "maximizing_indices": [38, 39],
        "maximum_norm": MAXIMUM_NORM,
        "maximum_norm_bits": 247,
        "norm_at_or_above_2_250": 0,
        "vectors": 86,
    }
    assert max(int(value) for value in packet["flint_norms"]) == MAXIMUM_NORM
    assert 12 * MAXIMUM_NORM < 2**250 < 13 * MAXIMUM_NORM


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]
    orbits_packet = json.loads((ROOT / pin["orbit_result_file"]).read_text())
    orbits = check_orbits(orbits_packet)
    relaxation = json.loads((ROOT / pin["relaxation_result_file"]).read_text())
    relaxation_audit = json.loads((ROOT / pin["relaxation_audit_result_file"]).read_text())
    exceptional_masks = check_relaxations(relaxation, relaxation_audit)
    assert len(exceptional_masks) == 321
    tasks = [orbits[mask][0] for mask in sorted(exceptional_masks)]
    actual = json.loads((ROOT / pin["actual_result_file"]).read_text())
    actual_audit = json.loads((ROOT / pin["actual_audit_result_file"]).read_text())
    vectors = check_actual(actual, actual_audit, tasks)
    norms = json.loads((ROOT / pin["norm_result_file"]).read_text())
    check_norms(norms, vectors)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[PROFILE]["status"] == "PROVED"
    for dependency in (*STAGES, CONDUCTOR, NORM):
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "2,924,654,040" in nodes[NODE]["statement"]
    assert "12*N_max<2^250" in nodes[NODE]["statement"]

    print(
        "E1_N256_S16_E30_PROFILE_541_EXCLUSION_PASS "
        "masks=1234 assignments=2924654040 exceptions=1456 templates=321 "
        "vectors=6371187456 actual=440 full=86 max_bits=247 engines=6"
    )


if __name__ == "__main__":
    main()
