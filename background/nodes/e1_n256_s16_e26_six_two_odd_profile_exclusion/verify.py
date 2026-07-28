#!/usr/bin/env python3
"""Verify the E26 six two-odd profile exclusion packet."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e26_six_two_odd_profile_exclusion"
REDUCTION = "e1_n256_s16_e26_profile_parity_light_reduction"
CONDUCTOR = "e1_n256_proper_conductor_collision_exclusion"
NORM = "collision_norm_criterion"
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
PROFILES = (
    (2, 6, 0, 0, 0), (1, 4, 1, 0, 0), (0, 2, 2, 0, 0),
    (2, 2, 0, 1, 0), (1, 0, 1, 1, 0), (1, 0, 0, 0, 1),
)
MAXIMUM_NORM = 902560312161452055740126650872074695232473707768299835426377069738129096704
EXPECTED_SUMMARY = {
    "vectors": 1_726_770_432,
    "profile_counts": [22_214, 2_148, 120, 2_754, 140, 4],
    "above_cutoff": [14_958, 1_744, 82, 798, 42, 0],
    "full_above_cutoff": [7_508, 438, 4, 106, 4, 0],
    "maximum_m3": [984, 840, 630, 600, 450, 0],
    "maximum_full_m3": [984, 702, 630, 420, 432, -1],
}


def strip_runtime(row: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in row.items() if key != "worker_seconds"}


def load_pin() -> dict[str, str]:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    required = {
        "reduction_statement_file", "reduction_result_file", "two_odd_atlas_file",
        "production_source_file", "production_driver_file", "production_result_file",
        "audit_source_file", "audit_driver_file", "audit_result_file",
        "norm_driver_file", "norm_result_file", "conductor_statement_file",
        "collision_norm_file",
    }
    assert {key for key in pin if key.endswith("_file")} == required
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]
    return pin


def replay(vector: dict[str, object]) -> tuple[int, int, int]:
    profile_index = int(vector["profile"])
    positions = tuple(int(value) for value in vector["positions"])
    coefficients = tuple(int(value) for value in vector["coefficients"])
    assert 0 <= profile_index < len(PROFILES)
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
    profile = tuple(magnitudes.count(value) for value in range(1, 6))
    assert max(magnitudes) <= 5 and profile == PROFILES[profile_index]
    weights = [0] * 128
    for difference, magnitude in enumerate(magnitudes, start=1):
        weights[difference] = weights[128 - difference] = magnitude
    support = [index for index, value in enumerate(weights) if value]
    m3 = sum(weights[left] * weights[right] * weights[(-left - right) % 128] for left in support for right in support)
    assert m3 == int(vector["m3"]) > 228
    conductor = math.gcd(256, *positions)
    assert conductor == int(vector["conductor"])
    return profile_index, conductor, m3


def check_censuses(pin: dict[str, str]) -> list[dict[str, object]]:
    reduction = json.loads((ROOT / pin["reduction_result_file"]).read_text())
    atlas = json.loads((ROOT / pin["two_odd_atlas_file"]).read_text())
    assert reduction["schema"] == "e1-e26-profile-parity-route-probe-v1" and reduction["complete"] is True
    tasks = [row["representative"] for row in atlas["rows"]]
    assert atlas["complete"] is True and len(tasks) == 87
    production = json.loads((ROOT / pin["production_result_file"]).read_text())
    audit = json.loads((ROOT / pin["audit_result_file"]).read_text())
    assert production["schema"] == "e1-e26-six-two-odd-profile-census-v1"
    assert audit["schema"] == "e1-e26-six-two-odd-profile-census-audit-v1"
    assert production["complete"] is audit["complete"] is audit["agreement"] is True
    assert production["source_sha256"] == pin["production_source_file_sha256"]
    assert production["reduction_sha256"] == pin["reduction_result_file_sha256"]
    assert production["atlas_sha256"] == pin["two_odd_atlas_file_sha256"]
    assert audit["source_sha256"] == pin["audit_source_file_sha256"]
    assert audit["production_sha256"] == pin["production_result_file_sha256"]
    assert audit["mismatch_templates"] == []
    first = sorted(production["rows"], key=lambda row: int(row["template"]))
    second = sorted(audit["rows"], key=lambda row: int(row["template"]))
    assert len(first) == len(second) == len(tasks) == 87
    matches: list[dict[str, object]] = []
    for template, (left, right, light) in enumerate(zip(first, second, tasks)):
        assert strip_runtime(left) == strip_runtime(right)
        assert int(left["template"]) == template and left["light"] == light
        assert int(left["supports"]) == math.comb(124, 3) == 310_124
        assert int(left["vectors"]) == 19_847_936
        assert sum(int(value) for value in left["above_cutoff"]) == len(left["matches"])
        for vector in left["matches"]:
            replay(vector)
            matches.append(vector)
    for packet in (production, audit):
        for key, value in EXPECTED_SUMMARY.items():
            assert packet["summary"][key] == value
    assert len(matches) == 17_624
    primitive = [vector for vector in matches if int(vector["conductor"]) == 1]
    assert len(primitive) == 8_060
    return primitive


def check_norms(pin: dict[str, str], vectors: list[dict[str, object]]) -> None:
    packet = json.loads((ROOT / pin["norm_result_file"]).read_text())
    assert packet["schema"] == "e1-e26-six-two-odd-profile-exceptional-norm-v1"
    assert packet["complete"] is packet["agreement"] is True
    assert packet["production_sha256"] == pin["production_result_file_sha256"]
    assert packet["audit_sha256"] == pin["audit_result_file_sha256"]
    assert packet["vectors"] == vectors and len(vectors) == 8_060
    assert packet["flint_norms"] == packet["pari_norms"] and len(packet["flint_norms"]) == 8_060
    assert packet["summary"] == {
        "distinct_norms": 1_442,
        "maximizing_indices": [5411, 5412, 5417, 5422, 5425, 5430, 5467, 5468],
        "maximum_norm": MAXIMUM_NORM,
        "maximum_norm_bits": 249,
        "norm_at_or_above_2_250": 0,
        "vectors": 8_060,
    }
    assert 2 * MAXIMUM_NORM < 2**250 < 3 * MAXIMUM_NORM


def main() -> None:
    pin = load_pin()
    vectors = check_censuses(pin)
    check_norms(pin, vectors)
    production_source = (ROOT / pin["production_source_file"]).read_text()
    audit_source = (ROOT / pin["audit_source_file"]).read_text()
    norm_driver = (ROOT / pin["norm_driver_file"]).read_text()
    assert "folded_class" in production_source and "reverse_exponent" not in production_source
    assert "reverse_exponent" in audit_source and "folded_class" not in audit_source
    assert "python-flint" in norm_driver and "polresultant" in norm_driver

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in (REDUCTION, CONDUCTOR, NORM):
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "1,726,770,432" in nodes[NODE]["statement"]
    assert "2*N_max<2^250<3*N_max" in nodes[NODE]["statement"]
    print("E1_N256_S16_E26_SIX_TWO_ODD_PROFILE_EXCLUSION_PASS templates=87 vectors=1726770432 profile=27380 exceptions=17624 full=8060 max_bits=249 engines=4")


if __name__ == "__main__":
    main()
