#!/usr/bin/env python3
"""Verify the E30 two-odd profile exclusion packet."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e30_two_odd_profile_exclusion"
PROFILE = "e1_n256_s16_e30_profile_parity_light_reduction"
CONDUCTOR = "e1_n256_proper_conductor_collision_exclusion"
NORM = "collision_norm_criterion"
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
MAXIMUM_NORM = 255193811126065252065353356643030254729479452452701245894186298519499407392
EXPECTED_SUMMARY = {
    "profile_151": {
        "count": 7_722,
        "full_conductor": 3_572,
        "maximum_full_conductor_m3": 1_068,
        "maximum_m3": 1_344,
    },
    "profile_27": {
        "count": 44_302,
        "full_conductor": 28_114,
        "maximum_full_conductor_m3": 1_320,
        "maximum_m3": 1_320,
    },
}
EXPECTED_PIN = {
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "conductor_file": "background/nodes/e1_n256_proper_conductor_collision_exclusion/statement.md",
    "conductor_file_sha256": "4319261b9d388351f2980fd4f849d7fae4876a6e5db167c74467ea957a055d73",
    "joint_audit_driver_file": "background/nodes/e1_n256_s16_e30_two_odd_profile_exclusion/notes/e30_two_odd_joint_census_audit_modal.py",
    "joint_audit_driver_file_sha256": "a968771cd0f21bbf16f77607da519d994d359826782655ce7dd7becc99224ab9",
    "joint_audit_result_file": "background/nodes/e1_n256_s16_e30_two_odd_profile_exclusion/notes/e30_two_odd_joint_census_audit_result.json",
    "joint_audit_result_file_sha256": "d93386a90cc24bee6333ce8bb566b0967083ba71ccc8d53adba2d49899222712",
    "joint_audit_source_file": "background/nodes/e1_n256_s16_e30_two_odd_profile_exclusion/notes/e30_two_odd_joint_census_audit.cpp",
    "joint_audit_source_file_sha256": "1e98f61dc91e5d9f4b8944c81d493841dcfd9ae81f941f30577a9f0151708136",
    "joint_driver_file": "background/nodes/e1_n256_s16_e30_two_odd_profile_exclusion/notes/e30_two_odd_joint_census_modal.py",
    "joint_driver_file_sha256": "46648ccd4563d1f4a5e3ae8d914e3a95757449520ef388da973ae120e833c1d7",
    "joint_result_file": "background/nodes/e1_n256_s16_e30_two_odd_profile_exclusion/notes/e30_two_odd_joint_census_result.json",
    "joint_result_file_sha256": "02e67a1fd5245b08333d1abfc107695086de708288e73328ee345223a5af646e",
    "joint_source_file": "background/nodes/e1_n256_s16_e30_two_odd_profile_exclusion/notes/e30_two_odd_joint_census.cpp",
    "joint_source_file_sha256": "1ffd87c70e16f87015d0c173290dd43376db61a0703bfe51ee3f46522162eedc",
    "norm_audit_driver_file": "background/nodes/e1_n256_s16_e30_two_odd_profile_exclusion/notes/e30_profile27_exact_norm_audit_modal.py",
    "norm_audit_driver_file_sha256": "1a8984397b52010c7a3742e5bee573175b025255f7d43fa8c6f197df0aa53976",
    "norm_audit_result_file": "background/nodes/e1_n256_s16_e30_two_odd_profile_exclusion/notes/e30_profile27_exact_norm_audit_result.json",
    "norm_audit_result_file_sha256": "f2d73b7ae4d47f323ee6ca4604a609ed2c2985d7a0796e26db56707d77e22270",
    "norm_audit_source_file": "background/nodes/e1_n256_s16_e30_two_odd_profile_exclusion/notes/e30_profile27_exact_norm_audit.cpp",
    "norm_audit_source_file_sha256": "ad247a0ea53198ac6881318703aa1d594631003269f0e7a14781179f619ff38c",
    "norm_driver_file": "background/nodes/e1_n256_s16_e30_two_odd_profile_exclusion/notes/e30_profile27_exact_norm_census_modal.py",
    "norm_driver_file_sha256": "57311712ce9a4a153aff2080ed0844baa64218cd3b2850ed6fbd56dfaa03feaa",
    "norm_result_file": "background/nodes/e1_n256_s16_e30_two_odd_profile_exclusion/notes/e30_profile27_exact_norm_census_result.json",
    "norm_result_file_sha256": "73d32a8d8c1d2480cdabbb365ee6ab30601cd8bd2eee82b52cf5608052e521ee",
    "norm_source_file": "background/nodes/e1_n256_s16_e30_two_odd_profile_exclusion/notes/e30_profile27_exact_norm_census.cpp",
    "norm_source_file_sha256": "e635219beb9cb09a5fa3ee59c86930fd4de1aa01054869f80269e816bd0a7993",
    "orbit_result_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_two_six_odd_light_orbit_result.json",
    "orbit_result_file_sha256": "6ba7acb9e680f115b7c6121615748b00fa68a6adee005bb750094fea73ce5759",
    "profile_reduction_file": "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/statement.md",
    "profile_reduction_file_sha256": "7d988ae69d03e78167eea76ca9746782b35627bb9fde645a187a121ee291aef4",
}


def replay_witness(witness: dict[str, object], profile: tuple[int, int, int]) -> None:
    positions = tuple(int(value) for value in witness["positions"])
    coefficients = tuple(int(value) for value in witness["coefficients"])
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
    assert tuple(magnitudes.count(value) for value in (1, 2, 3)) == profile
    assert max(magnitudes, default=0) <= 3
    if "m3" in witness:
        weights = [0] * 128
        support = []
        for difference in range(1, 64):
            magnitude = abs(product[difference])
            if magnitude:
                weights[difference] = weights[128 - difference] = magnitude
                support.extend((difference, 128 - difference))
        third_moment = sum(
            weights[left] * weights[right] * weights[(-left - right) % 128]
            for left in support
            for right in support
        )
        assert int(witness["m3"]) == third_moment


def check_joint_packets(production: dict[str, object], audit: dict[str, object]) -> None:
    assert production["schema"] == "e1-e30-two-odd-joint-census-v1"
    assert audit["schema"] == "e1-e30-two-odd-joint-census-audit-v1"
    assert production["complete"] is audit["complete"] is audit["agreement"] is True
    assert production["expected_templates"] == production["completed_templates"] == 87
    assert audit["expected_templates"] == audit["completed_templates"] == 87
    assert production["source_sha256"] == EXPECTED_PIN["joint_source_file_sha256"]
    assert audit["source_sha256"] == EXPECTED_PIN["joint_audit_source_file_sha256"]
    assert audit["production_sha256"] == EXPECTED_PIN["joint_result_file_sha256"]
    assert production["orbits_sha256"] == audit["orbits_sha256"] == EXPECTED_PIN["orbit_result_file_sha256"]
    assert production["summary"] == audit["summary"] == EXPECTED_SUMMARY

    first = {int(row["template"]): row for row in production["rows"]}
    second = {int(row["template"]): row for row in audit["rows"]}
    assert set(first) == set(second) == set(range(87))
    for template in range(87):
        left = first[template]
        right = second[template]
        for key in ("complete", "light", "supports", "vectors"):
            assert left[key] == right[key]
        for profile_key, profile in (("profile_27", (2, 7, 0)), ("profile_151", (1, 5, 1))):
            for key in ("count", "full_conductor", "maximum_m3", "maximum_full_conductor_m3"):
                assert left[profile_key][key] == right[profile_key][key]
            if int(left[profile_key]["count"]):
                replay_witness(left[profile_key]["witness"], profile)
                assert int(left[profile_key]["witness"]["m3"]) == int(left[profile_key]["maximum_m3"])
            if int(left[profile_key]["full_conductor"]):
                witness = left[profile_key]["full_conductor_witness"]
                replay_witness(witness, profile)
                assert math.gcd(256, *(int(value) for value in witness["positions"])) == 1
                assert int(witness["m3"]) == int(left[profile_key]["maximum_full_conductor_m3"])
    assert sum(int(row["vectors"]) for row in first.values()) == 1_726_770_432


def check_norm_packets(
    production: dict[str, object],
    audit: dict[str, object],
    joint: dict[str, object],
) -> None:
    assert production["schema"] == "e1-e30-profile27-exact-norm-census-v1"
    assert audit["schema"] == "e1-e30-profile27-exact-norm-audit-v1"
    assert production["complete"] is audit["complete"] is audit["agreement"] is True
    assert production["expected_templates"] == production["completed_templates"] == 87
    assert audit["expected_templates"] == audit["completed_templates"] == 87
    assert production["source_sha256"] == EXPECTED_PIN["norm_source_file_sha256"]
    assert audit["source_sha256"] == EXPECTED_PIN["norm_audit_source_file_sha256"]
    assert audit["production_sha256"] == EXPECTED_PIN["norm_result_file_sha256"]
    assert production["orbits_sha256"] == audit["orbits_sha256"] == EXPECTED_PIN["orbit_result_file_sha256"]

    first = {int(row["template"]): row for row in production["rows"]}
    second = {int(row["template"]): row for row in audit["rows"]}
    joint_rows = {int(row["template"]): row for row in joint["rows"]}
    assert set(first) == set(second) == set(joint_rows) == set(range(87))
    for template in range(87):
        left = first[template]
        right = second[template]
        for key in (
            "complete",
            "light",
            "full_conductor_profile_27",
            "norm_at_or_above_2_250",
            "maximum_norm",
            "maximum_norm_bits",
            "maximum_witness",
        ):
            assert left[key] == right[key]
        assert int(left["full_conductor_profile_27"]) == int(
            joint_rows[template]["profile_27"]["full_conductor"]
        )
        assert int(left["norm_at_or_above_2_250"]) == 0
        if int(left["full_conductor_profile_27"]):
            witness = left["maximum_witness"]
            replay_witness(witness, (2, 7, 0))
            assert math.gcd(256, *(int(value) for value in witness["positions"])) == 1
            assert int(witness["norm"]) == int(left["maximum_norm"])

    expected_norm_summary = {
        "full_conductor_profile_27": 28_114,
        "maximum_norm": MAXIMUM_NORM,
        "maximum_norm_bits": 248,
        "norm_at_or_above_2_250": 0,
    }
    for packet in (production, audit):
        assert all(int(packet["summary"][key]) == value for key, value in expected_norm_summary.items())
    maximizing = [row for row in first.values() if int(row["maximum_norm"]) == MAXIMUM_NORM]
    assert len(maximizing) == 1 and int(maximizing[0]["template"]) == 30
    assert maximizing[0]["light"] == [0, 1, 20, 109]
    witness = maximizing[0]["maximum_witness"]
    assert witness["positions"] == [7, 39, 103, 0, 1, 20, 109]
    assert witness["coefficients"] == [2, -2, -2, -1, 1, 1, 1]


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]

    joint = json.loads((ROOT / pin["joint_result_file"]).read_text())
    joint_audit = json.loads((ROOT / pin["joint_audit_result_file"]).read_text())
    check_joint_packets(joint, joint_audit)
    norms = json.loads((ROOT / pin["norm_result_file"]).read_text())
    norms_audit = json.loads((ROOT / pin["norm_audit_result_file"]).read_text())
    check_norm_packets(norms, norms_audit, joint)
    assert 7 * MAXIMUM_NORM < 2**250 < 8 * MAXIMUM_NORM

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in (PROFILE, CONDUCTOR, NORM):
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "28,114" in nodes[NODE]["statement"]
    assert "7*N_max<2^250" in nodes[NODE]["statement"]

    print(
        "E1_N256_S16_E30_TWO_ODD_PROFILE_EXCLUSION_PASS "
        "templates=87 vectors=1726770432 full27=28114 full151=3572 "
        "max_bits=248 above=0 engines=4"
    )


if __name__ == "__main__":
    main()
