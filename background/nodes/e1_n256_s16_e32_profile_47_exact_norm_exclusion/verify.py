#!/usr/bin/env python3
"""Verify the E32 profile-(4,7) exact-norm exclusion."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e32_profile_47_exact_norm_exclusion"
PROFILE = "e1_n256_s16_e32_profile_parity_diameter_reduction"
ROUTER = "e1_n256_s16_e32_four_odd_light_template_reduction"
CONDUCTOR = "e1_n256_proper_conductor_collision_exclusion"
NORM = "collision_norm_criterion"
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
MAXIMUM_NORM = 119477984433218714943829098200259691143739376720677525742811917286342611458
EXPECTED_PIN = {
    "audit_census_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_profile47_exact_norm_audit.cpp",
    "audit_census_file_sha256": "8dbb18c81ce412f715c845a60374f9be79cd139b520b266078da3bb4a9bcb19e",
    "audit_launcher_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_profile47_exact_norm_audit_modal.py",
    "audit_launcher_file_sha256": "08c70df9e9b5e2203b50c41caeb0d003a3053fa05600a5221369d0816a5ce600",
    "audit_result_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_profile47_exact_norm_audit_result.json",
    "audit_result_file_sha256": "06b4061b3935417932f6e45e04b13fcb45a6ea37c55680cbb9f2da6001ea2385",
    "census_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_profile47_exact_norm_census.cpp",
    "census_file_sha256": "07dcc5290d5718272013ce57303b527f5eae32cf5cef133b970c3becaa102525",
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "conductor_file": "background/nodes/e1_n256_proper_conductor_collision_exclusion/statement.md",
    "conductor_file_sha256": "4319261b9d388351f2980fd4f849d7fae4876a6e5db167c74467ea957a055d73",
    "launcher_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_profile47_exact_norm_census_modal.py",
    "launcher_file_sha256": "7da3a88c68d9498615691b3218a198e1b45b992d8aaaabe6cf0719bfa099cbaa",
    "orbit_result_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_four_odd_light_orbit_result.json",
    "orbit_result_file_sha256": "daaf781348f8b691c959c6172e900a6791b00904a6131c60c16f7d98eeec7e98",
    "profile_reduction_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/statement.md",
    "profile_reduction_file_sha256": "2c775ba148a35987157c2ce170dbc18b4a338f194cd990b304904e8726ed4edd",
    "result_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_profile47_exact_norm_census_result.json",
    "result_file_sha256": "cad805abff33c55d80a765e7f83ad6f85fe530cbf9b39835b87798984d5cae93",
    "router_file": "background/nodes/e1_n256_s16_e32_four_odd_light_template_reduction/statement.md",
    "router_file_sha256": "cbb8fdb70f3c2bf9e099d53e01483a3ba83fdd371a5058bf16f5e8a00b28ba8c",
}


def check_witness(witness: dict[str, object]) -> None:
    positions = tuple(int(value) for value in witness["positions"])
    coefficients = tuple(int(value) for value in witness["coefficients"])
    assert len(positions) == len(coefficients) == 7 and len(set(positions)) == 7
    assert sorted(abs(value) for value in coefficients) == [1, 1, 1, 1, 2, 2, 2]
    assert math.gcd(256, *positions) == 1
    product = [0] * 128
    for left, left_value in zip(positions, coefficients):
        for right, right_value in zip(positions, coefficients):
            quotient, residue = divmod(left - right, 128)
            product[residue] += (-1 if quotient % 2 else 1) * left_value * right_value
    assert product[0] == 16
    assert all(product[128 - difference] == -product[difference] for difference in range(1, 64))
    magnitudes = [abs(product[difference]) for difference in range(1, 64)]
    assert (magnitudes.count(1), magnitudes.count(2), magnitudes.count(3)) == (4, 7, 0)
    assert max(magnitudes) == 2


def check_packets(production: dict[str, object], audit: dict[str, object]) -> None:
    assert production["schema"] == "e1-e32-profile47-exact-norm-census-v1"
    assert audit["schema"] == "e1-e32-profile47-exact-norm-audit-v1"
    assert production["complete"] is audit["complete"] is True
    assert production["selected_templates"] == audit["selected_templates"] == list(range(148))
    assert production["source_sha256"] == EXPECTED_PIN["census_file_sha256"]
    assert audit["source_sha256"] == EXPECTED_PIN["audit_census_file_sha256"]
    assert production["orbits_sha256"] == audit["orbits_sha256"] == EXPECTED_PIN["orbit_result_file_sha256"]

    first = {int(row["template"]): row for row in production["rows"]}
    second = {int(row["template"]): row for row in audit["rows"]}
    assert set(first) == set(second) == set(range(148))
    for template in range(148):
        left = first[template]
        right = second[template]
        assert left["light"] == right["light"]
        for key in (
            "full_conductor_profile_47",
            "norm_at_or_above_2_250",
            "maximum_norm",
            "maximum_norm_bits",
            "maximum_witness",
        ):
            assert left[key] == right[key]
        assert int(left["norm_at_or_above_2_250"]) == 0
        if int(left["full_conductor_profile_47"]):
            check_witness(left["maximum_witness"])
            assert int(left["maximum_witness"]["norm"]) == int(left["maximum_norm"])

    for packet in (production, audit):
        summary = packet["summary"]
        assert int(summary["full_conductor_profile_47"]) == 60_148
        assert int(summary["norm_at_or_above_2_250"]) == 0
        assert int(summary["maximum_norm"]) == MAXIMUM_NORM
        assert int(summary["maximum_norm_bits"]) == 247
    maximizing = [row for row in first.values() if int(row["maximum_norm"]) == MAXIMUM_NORM]
    assert len(maximizing) == 1 and int(maximizing[0]["template"]) == 7
    assert maximizing[0]["maximum_witness"]["positions"] == [5, 7, 9, 0, 1, 2, 12]
    assert maximizing[0]["maximum_witness"]["coefficients"] == [2, -2, -2, 1, 1, 1, 1]


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]

    production = json.loads((ROOT / pin["result_file"]).read_text())
    audit = json.loads((ROOT / pin["audit_result_file"]).read_text())
    check_packets(production, audit)
    assert 15 * MAXIMUM_NORM < 2**250 < 16 * MAXIMUM_NORM

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in (PROFILE, ROUTER, CONDUCTOR, NORM):
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "60,148" in nodes[NODE]["statement"]
    assert "15*N_max<2^250" in nodes[NODE]["statement"]

    print(
        "E1_N256_S16_E32_PROFILE_47_EXACT_NORM_EXCLUSION_PASS "
        "templates=148 full=60148 max_bits=247 above=0 engines=2 mutations=4"
    )


if __name__ == "__main__":
    main()
