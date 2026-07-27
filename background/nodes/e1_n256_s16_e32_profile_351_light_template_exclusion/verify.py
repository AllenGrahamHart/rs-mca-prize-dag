#!/usr/bin/env python3
"""Verify the E32 profile-(3,5,1) light-template exclusion."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e32_profile_351_light_template_exclusion"
PROFILE = "e1_n256_s16_e32_profile_parity_diameter_reduction"
ROUTER = "e1_n256_s16_e32_four_odd_light_template_reduction"
NORM = "collision_norm_criterion"
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
EXPECTED_PIN = {
    "audit_census_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_four_odd_joint_census_audit.cpp",
    "audit_census_file_sha256": "15ee63254b0703496c83b4b575958fad0ec6b85e15f4518006f7715f900a8951",
    "audit_launcher_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_four_odd_joint_census_audit_modal.py",
    "audit_launcher_file_sha256": "e2d882c1054bd7b135251ab7fdc9e1049f3ece76ff54c2b1d21d5fa3e8389c52",
    "audit_result_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_four_odd_joint_census_audit_result.json",
    "audit_result_file_sha256": "cf56979139c8d0f600bd611252e0c503367ed2f1a64f2a2cf965210d2a97b168",
    "census_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_four_odd_joint_census.cpp",
    "census_file_sha256": "df5d49d1550311533926955ef58417cd7e50cd629bb2035945fee893bafe5fa4",
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "launcher_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_four_odd_joint_census_modal.py",
    "launcher_file_sha256": "4a5eb85dd8806aeb922fc1682a42ae2008e141b0dc51356c171c13f73f920f05",
    "orbit_result_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_four_odd_light_orbit_result.json",
    "orbit_result_file_sha256": "daaf781348f8b691c959c6172e900a6791b00904a6131c60c16f7d98eeec7e98",
    "profile_reduction_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/statement.md",
    "profile_reduction_file_sha256": "2c775ba148a35987157c2ce170dbc18b4a338f194cd990b304904e8726ed4edd",
    "result_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_four_odd_joint_census_result.json",
    "result_file_sha256": "237ed17fbbf36897409cc0f16dc4599dc8dd3c852c2e622f9f077a6b73ee25ab",
    "router_file": "background/nodes/e1_n256_s16_e32_four_odd_light_template_reduction/statement.md",
    "router_file_sha256": "cbb8fdb70f3c2bf9e099d53e01483a3ba83fdd371a5058bf16f5e8a00b28ba8c",
}
EXPECTED_SUMMARY = {
    "profile_351": {
        "count": 29_238,
        "full_conductor": 15_440,
        "maximum_m3": 1_392,
        "maximum_full_conductor_m3": 1_392,
    },
    "profile_47": {
        "count": 87_818,
        "full_conductor": 60_148,
        "maximum_m3": 1_584,
        "maximum_full_conductor_m3": 1_524,
    },
}


def witness_data(witness: dict[str, object]) -> tuple[tuple[int, int, int], int, int]:
    positions = tuple(int(value) for value in witness["positions"])
    coefficients = tuple(int(value) for value in witness["coefficients"])
    assert len(positions) == len(coefficients) == 7
    assert len(set(positions)) == 7
    assert sorted(abs(value) for value in coefficients) == [1, 1, 1, 1, 2, 2, 2]

    product = [0] * 128
    for left, left_value in zip(positions, coefficients):
        for right, right_value in zip(positions, coefficients):
            quotient, residue = divmod(left - right, 128)
            product[residue] += (-1 if quotient % 2 else 1) * left_value * right_value
    assert product[0] == 16
    assert all(product[128 - difference] == -product[difference] for difference in range(1, 64))

    magnitudes = [abs(product[difference]) for difference in range(1, 64)]
    assert max(magnitudes) <= 3
    profile = tuple(magnitudes.count(value) for value in (1, 2, 3))
    weight = [0] * 128
    for difference in range(1, 64):
        weight[difference] = magnitudes[difference - 1]
        weight[128 - difference] = magnitudes[difference - 1]
    m3 = sum(
        weight[left] * weight[right] * weight[(-left - right) % 128]
        for left in range(128)
        for right in range(128)
        if weight[left] and weight[right]
    )
    conductor = math.gcd(256, *positions)
    return profile, m3, conductor


def normalized_summary(packet: dict[str, object]) -> dict[str, dict[str, int]]:
    return {
        profile: {key: int(value) for key, value in packet["summary"][profile].items()}
        for profile in EXPECTED_SUMMARY
    }


def check_packets(production: dict[str, object], audit: dict[str, object]) -> None:
    assert production["schema"] == "e1-e32-four-odd-joint-census-v1"
    assert audit["schema"] == "e1-e32-four-odd-joint-census-audit-v1"
    assert production["complete"] is audit["complete"] is True
    assert production["orbits_sha256"] == audit["orbits_sha256"] == EXPECTED_PIN["orbit_result_file_sha256"]
    assert production["source_sha256"] == EXPECTED_PIN["census_file_sha256"]
    assert audit["source_sha256"] == EXPECTED_PIN["audit_census_file_sha256"]
    assert normalized_summary(production) == normalized_summary(audit) == EXPECTED_SUMMARY

    production_rows = {int(row["template"]): row for row in production["rows"]}
    audit_rows = {int(row["template"]): row for row in audit["rows"]}
    assert set(production_rows) == set(audit_rows) == set(range(148))
    expected_supports = math.comb(124, 3)
    expected_vectors = expected_supports * 64
    ledger_keys = (
        "count", "full_conductor", "maximum_m3", "maximum_full_conductor_m3"
    )
    for template in range(148):
        first = production_rows[template]
        second = audit_rows[template]
        assert first["light"] == second["light"]
        assert int(first["supports"]) == int(second["supports"]) == expected_supports
        assert int(first["vectors"]) == int(second["vectors"]) == expected_vectors
        for profile, expected_profile in (("profile_47", (4, 7, 0)), ("profile_351", (3, 5, 1))):
            assert all(int(first[profile][key]) == int(second[profile][key]) for key in ledger_keys)
            if int(first[profile]["count"]):
                observed_profile, m3, _ = witness_data(first[profile]["witness"])
                assert observed_profile == expected_profile
                assert m3 == int(first[profile]["maximum_m3"])
            if int(first[profile]["full_conductor"]):
                observed_profile, m3, conductor = witness_data(first[profile]["full_conductor_witness"])
                assert observed_profile == expected_profile and conductor == 1
                assert m3 == int(first[profile]["maximum_full_conductor_m3"])
    assert 148 * expected_vectors == 2_937_494_528


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]

    production = json.loads((ROOT / pin["result_file"]).read_text())
    audit = json.loads((ROOT / pin["audit_result_file"]).read_text())
    check_packets(production, audit)
    assert EXPECTED_SUMMARY["profile_351"]["maximum_m3"] < 1517

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in (PROFILE, ROUTER, NORM):
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "2,937,494,528" in nodes[NODE]["statement"]
    assert "M_3=1392<1517" in nodes[NODE]["statement"]

    print(
        "E1_N256_S16_E32_PROFILE_351_LIGHT_TEMPLATE_EXCLUSION_PASS "
        "templates=148 vectors=2937494528 retained=29238 full=15440 m3=1392 mutations=4"
    )


if __name__ == "__main__":
    main()
