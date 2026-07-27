#!/usr/bin/env python3
"""Verify the E27 six-profile joint exclusion packet."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e27_six_profile_joint_exclusion"
ENDPOINT = "e1_n256_s16_e27_endpoint_exclusion"
REDUCTION = "e1_n256_s16_e27_profile_parity_light_reduction"
CONDUCTOR = "e1_n256_proper_conductor_collision_exclusion"
NORM = "collision_norm_criterion"
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
PROFILES = (
    (3, 6, 0, 0, 0),
    (2, 4, 1, 0, 0),
    (1, 2, 2, 0, 0),
    (3, 2, 0, 1, 0),
    (0, 0, 3, 0, 0),
    (2, 0, 1, 1, 0),
)
MAXIMUM_NORM = 172876856486553232403068097247779856553359362267270754177943490636016856066
EXPECTED_SUMMARY = {
    "vectors": 158_783_488,
    "profile_counts": [2_344, 752, 272, 666, 4, 86],
    "above_cutoff": [1_388, 338, 128, 146, 0, 0],
    "full_above_cutoff": [328, 68, 8, 0, 0, 0],
    "maximum_m3": [1_020, 1_074, 738, 648, 162, 408],
    "maximum_full_m3": [912, 678, 480, 390, -1, 198],
}


def strip_runtime(row: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in row.items() if key != "worker_seconds"}


def load_pin() -> dict[str, str]:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    required_files = {
        "reduction_statement_file",
        "reduction_result_file",
        "production_source_file",
        "production_driver_file",
        "production_result_file",
        "audit_source_file",
        "audit_driver_file",
        "audit_result_file",
        "norm_driver_file",
        "norm_result_file",
        "conductor_statement_file",
        "collision_norm_file",
    }
    assert {key for key in pin if key.endswith("_file")} == required_files
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]
    return pin


def replay_vector(vector: dict[str, object]) -> tuple[int, int, int]:
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
    profile = tuple(magnitudes.count(magnitude) for magnitude in range(1, 6))
    assert max(magnitudes) <= 5 and profile == PROFILES[profile_index]
    weights = [0] * 128
    for difference, magnitude in enumerate(magnitudes, start=1):
        weights[difference] = weights[128 - difference] = magnitude
    support = [index for index, value in enumerate(weights) if value]
    m3 = sum(
        weights[left] * weights[right] * weights[(-left - right) % 128]
        for left in support
        for right in support
    )
    assert m3 == int(vector["m3"]) > 443
    conductor = math.gcd(256, *positions)
    assert conductor == int(vector["conductor"])
    return profile_index, conductor, m3


def check_censuses(pin: dict[str, str]) -> list[dict[str, object]]:
    reduction = json.loads((ROOT / pin["reduction_result_file"]).read_text())
    assert reduction["schema"] == "e1-e27-profile-parity-probe-v1" and reduction["complete"] is True
    geometry = reduction["light_geometry"]["orbit_representatives"]
    tasks = list(geometry["3"])
    assert len(tasks) == 8

    production = json.loads((ROOT / pin["production_result_file"]).read_text())
    audit = json.loads((ROOT / pin["audit_result_file"]).read_text())
    assert production["schema"] == "e1-e27-six-profile-joint-census-v1"
    assert audit["schema"] == "e1-e27-six-profile-joint-census-audit-v1"
    assert production["complete"] is audit["complete"] is audit["agreement"] is True
    assert production["source_sha256"] == pin["production_source_file_sha256"]
    assert production["reduction_sha256"] == pin["reduction_result_file_sha256"]
    assert audit["source_sha256"] == pin["audit_source_file_sha256"]
    assert audit["production_sha256"] == pin["production_result_file_sha256"]
    assert audit["mismatch_templates"] == []

    first = sorted(production["rows"], key=lambda row: int(row["template"]))
    second = sorted(audit["rows"], key=lambda row: int(row["template"]))
    assert len(first) == len(second) == len(tasks) == 8
    matches: list[dict[str, object]] = []
    for template, (left, right, light) in enumerate(zip(first, second, tasks)):
        assert strip_runtime(left) == strip_runtime(right)
        assert int(left["template"]) == template and left["light"] == light
        assert int(left["supports"]) == math.comb(124, 3) == 310_124
        assert int(left["vectors"]) == 19_847_936
        assert sum(int(value) for value in left["above_cutoff"]) == len(left["matches"])
        for vector in left["matches"]:
            replay_vector(vector)
            matches.append(vector)
    for packet in (production, audit):
        for key, value in EXPECTED_SUMMARY.items():
            assert packet["summary"][key] == value
    assert len(matches) == 2_000
    primitive = [vector for vector in matches if int(vector["conductor"]) == 1]
    assert len(primitive) == 404
    return primitive


def check_norms(pin: dict[str, str], vectors: list[dict[str, object]]) -> None:
    packet = json.loads((ROOT / pin["norm_result_file"]).read_text())
    assert packet["schema"] == "e1-e27-six-profile-exceptional-norm-v1"
    assert packet["complete"] is packet["agreement"] is True
    assert packet["production_sha256"] == pin["production_result_file_sha256"]
    assert packet["audit_sha256"] == pin["audit_result_file_sha256"]
    assert packet["vectors"] == vectors and len(vectors) == 404
    assert packet["flint_norms"] == packet["pari_norms"] and len(packet["flint_norms"]) == 404
    assert packet["summary"] == {
        "distinct_norms": 144,
        "maximizing_indices": [124, 125],
        "maximum_norm": MAXIMUM_NORM,
        "maximum_norm_bits": 247,
        "norm_at_or_above_2_250": 0,
        "vectors": 404,
    }
    assert 10 * MAXIMUM_NORM < 2**250 < 11 * MAXIMUM_NORM


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
    assert (NODE, ENDPOINT, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "158,783,488" in nodes[NODE]["statement"]
    assert "10*N_max<2^250<11*N_max" in nodes[NODE]["statement"]

    print("E1_N256_S16_E27_SIX_PROFILE_JOINT_EXCLUSION_PASS templates=8 vectors=158783488 profile=4124 exceptions=2000 full=404 max_bits=247 engines=4")


if __name__ == "__main__":
    main()
