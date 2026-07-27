#!/usr/bin/env python3
"""Verify the E28 eight-profile joint exclusion packet."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e28_eight_profile_joint_exclusion"
ENDPOINT = "e1_n256_s16_e28_endpoint_exclusion"
REDUCTION = "e1_n256_s16_e28_profile_parity_light_reduction"
CONDUCTOR = "e1_n256_proper_conductor_collision_exclusion"
NORM = "collision_norm_criterion"
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
PROFILES = (
    (4,6,0,0,0), (0,7,0,0,0), (3,4,1,0,0), (2,2,2,0,0),
    (4,2,0,1,0), (1,0,3,0,0), (0,3,0,1,0), (3,0,1,1,0),
)
MAXIMUM_NORM = 296015175952529502165108365809577184284217843110959136601469787066321741314
EXPECTED = {
    "vectors": 3_056_582_144,
    "profile_counts": [28_458, 3_008, 12_458, 1_182, 1_984, 30, 1_360, 236],
    "above_cutoff": [9_936, 656, 1_500, 392, 152, 2, 0, 0],
    "full_above_cutoff": [3_838, 192, 330, 10, 2, 0, 0, 0],
    "maximum_m3": [1_200, 768, 1_020, 924, 804, 666, 480, 618],
    "maximum_full_m3": [1_200, 720, 1_020, 906, 696, -1, 240, 396],
}


def strip_runtime(row: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in row.items() if key != "worker_seconds"}


def load_pin() -> dict[str, str]:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    required = {
        "reduction_statement_file", "probe_result_file", "production_source_file",
        "production_driver_file", "production_result_file", "audit_source_file",
        "audit_driver_file", "audit_result_file", "norm_driver_file", "norm_result_file",
        "conductor_statement_file", "collision_norm_file",
    }
    assert {key for key in pin if key.endswith("_file")} == required
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]
    return pin


def replay(vector: dict[str, object]) -> tuple[int, int]:
    profile_index = int(vector["profile"])
    positions = tuple(int(value) for value in vector["positions"])
    coefficients = tuple(int(value) for value in vector["coefficients"])
    assert 0 <= profile_index < 8 and len(set(positions)) == len(positions) == 7
    assert sorted(abs(value) for value in coefficients) == [1,1,1,1,2,2,2]
    product = [0] * 128
    for left, left_value in zip(positions, coefficients):
        for right, right_value in zip(positions, coefficients):
            quotient, residue = divmod(left - right, 128)
            product[residue] += (-1 if quotient % 2 else 1) * left_value * right_value
    assert product[0] == 16
    assert all(product[128-difference] == -product[difference] for difference in range(1,64))
    magnitudes = [abs(product[difference]) for difference in range(1,64)]
    assert max(magnitudes) <= 5
    assert tuple(magnitudes.count(value) for value in range(1,6)) == PROFILES[profile_index]
    weights = [0] * 128
    for difference, magnitude in enumerate(magnitudes, start=1):
        weights[difference] = weights[128-difference] = magnitude
    support = [index for index, value in enumerate(weights) if value]
    m3 = sum(weights[a]*weights[b]*weights[(-a-b)%128] for a in support for b in support)
    assert m3 == int(vector["m3"]) > 658
    conductor = math.gcd(256, *positions)
    assert conductor == int(vector["conductor"])
    return conductor, m3


def check_censuses(pin: dict[str, str]) -> list[dict[str, object]]:
    probe = json.loads((ROOT / pin["probe_result_file"]).read_text())
    production = json.loads((ROOT / pin["production_result_file"]).read_text())
    audit = json.loads((ROOT / pin["audit_result_file"]).read_text())
    assert probe["complete"] is production["complete"] is audit["complete"] is True
    assert audit["agreement"] is True and audit["mismatch_templates"] == []
    assert production["schema"] == "e1-e28-eight-profile-joint-census-v1"
    assert audit["schema"] == "e1-e28-eight-profile-joint-census-audit-v1"
    assert production["source_sha256"] == pin["production_source_file_sha256"]
    assert production["probe_sha256"] == pin["probe_result_file_sha256"]
    assert audit["source_sha256"] == pin["audit_source_file_sha256"]
    assert audit["production_sha256"] == pin["production_result_file_sha256"]
    first = sorted(production["rows"], key=lambda row: int(row["template"]))
    second = sorted(audit["rows"], key=lambda row: int(row["template"]))
    assert len(first) == len(second) == 154
    matches: list[dict[str, object]] = []
    for template, (left, right) in enumerate(zip(first, second)):
        assert strip_runtime(left) == strip_runtime(right)
        assert int(left["template"]) == template
        assert int(left["supports"]) == math.comb(124,3) == 310_124
        assert int(left["vectors"]) == 19_847_936
        assert sum(int(value) for value in left["above_cutoff"]) == len(left["matches"])
        for vector in left["matches"]:
            replay(vector)
            matches.append(vector)
    for packet in (production, audit):
        for key, value in EXPECTED.items():
            assert packet["summary"][key] == value
    assert len(matches) == 12_638
    primitive = [vector for vector in matches if int(vector["conductor"]) == 1]
    assert len(primitive) == 4_372
    return primitive


def check_norms(pin: dict[str, str], vectors: list[dict[str, object]]) -> None:
    packet = json.loads((ROOT / pin["norm_result_file"]).read_text())
    assert packet["schema"] == "e1-e28-eight-profile-exceptional-norm-v1"
    assert packet["complete"] is packet["agreement"] is True
    assert packet["production_sha256"] == pin["production_result_file_sha256"]
    assert packet["audit_sha256"] == pin["audit_result_file_sha256"]
    assert packet["vectors"] == vectors and len(vectors) == 4_372
    assert packet["flint_norms"] == packet["pari_norms"] and len(packet["flint_norms"]) == 4_372
    assert packet["summary"] == {
        "distinct_norms": 1723, "maximizing_indices": [2326,2327],
        "maximum_norm": MAXIMUM_NORM, "maximum_norm_bits": 248,
        "norm_at_or_above_2_250": 0, "vectors": 4372,
    }
    assert 6 * MAXIMUM_NORM < 2**250 < 7 * MAXIMUM_NORM


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
        assert nodes[dependency]["status"] == "PROVED" and (dependency, NODE, "req") in edges
    assert (NODE, ENDPOINT, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "3,056,582,144" in nodes[NODE]["statement"]
    assert "6*N_max<2^250<7*N_max" in nodes[NODE]["statement"]

    print("E1_N256_S16_E28_EIGHT_PROFILE_JOINT_EXCLUSION_PASS templates=154 vectors=3056582144 profile=48716 exceptions=12638 full=4372 max_bits=248 engines=4")


if __name__ == "__main__":
    main()
