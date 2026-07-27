#!/usr/bin/env python3
"""Verify the E30 profile-(6,6) exclusion packet."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e30_profile_66_exclusion"
ENDPOINT = "e1_n256_s16_e30_endpoint_exclusion"
PROFILE = "e1_n256_s16_e30_profile_parity_light_reduction"
CONDUCTOR = "e1_n256_proper_conductor_collision_exclusion"
NORM = "collision_norm_criterion"
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
MAXIMUM_NORM = 384340001363476246612319029755636117549080229904040014178244445877664108548


def load_pin() -> dict[str, str]:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]
    return pin


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
    assert magnitudes.count(1) == magnitudes.count(2) == 6
    assert all(value <= 2 for value in magnitudes)
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


def check_relaxations(pin: dict[str, str]) -> list[list[int]]:
    orbits = json.loads((ROOT / pin["orbit_result_file"]).read_text())
    assert orbits["schema"] == "e1-e30-six-odd-mask-orbits-v1" and orbits["complete"] is True
    assert orbits["summary"]["affine_light_orbits"] == 1234
    assert orbits["summary"]["distinct_odd_masks"] == 1234
    assert orbits["summary"]["normalized_six_odd_supports"] == 280720
    assert orbits["summary"]["orbits_per_mask_histogram"] == {"1": 1234}
    atlas = [(int(row["odd_mask"]), row["orbits"][0]) for row in orbits["rows"]]
    assert len(atlas) == 1234 and all(len(row["orbits"]) == 1 for row in orbits["rows"])

    production = json.loads((ROOT / pin["relaxation_result_file"]).read_text())
    audit = json.loads((ROOT / pin["relaxation_audit_result_file"]).read_text())
    assert production["schema"] == "e1-e30-profile66-odd-difference-scan-v1"
    assert audit["schema"] == "e1-e30-profile66-odd-difference-scan-audit-v1"
    assert production["complete"] is audit["complete"] is True
    assert production["source_sha256"] == pin["relaxation_source_file_sha256"]
    assert audit["source_sha256"] == pin["relaxation_audit_source_file_sha256"]
    assert audit["production_sha256"] == pin["relaxation_result_file_sha256"]
    first = sorted(production["rows"], key=lambda row: int(row["index"]))
    second = sorted(audit["rows"], key=lambda row: int(row["index"]))
    assert len(first) == len(second) == 1234
    shared = (
        "index", "odd_mask", "light", "odd_classes", "assignments",
        "above_threshold", "above_histogram", "threshold", "maximum_m3",
        "maximum_even_classes",
    )
    for index, (left, right, (mask, light)) in enumerate(zip(first, second, atlas)):
        assert all(left[key] == right[key] for key in shared)
        assert int(left["index"]) == index and int(left["odd_mask"]) == mask
        assert left["light"] == light and len(left["odd_classes"]) == 6
        assert int(left["assignments"]) == math.comb(57, 6) == 36_288_252
    assert sum(int(row["assignments"]) for row in first) == 44_779_702_968
    assert sum(int(row["above_threshold"]) for row in first) == 33_737
    assert sum(int(row["above_threshold"]) > 0 for row in first) == 1_191
    assert max(int(row["maximum_m3"]) for row in first) == 1_542
    assert production["summary"]["above_threshold"] == audit["summary"]["above_threshold"] == 33_737
    return [row["light"] for row in first if int(row["above_threshold"]) > 0]


def check_actual(pin: dict[str, str], tasks: list[list[int]]) -> list[dict[str, object]]:
    production = json.loads((ROOT / pin["actual_result_file"]).read_text())
    audit = json.loads((ROOT / pin["actual_audit_result_file"]).read_text())
    assert production["schema"] == "e1-e30-profile66-exceptional-actual-v1"
    assert audit["schema"] == "e1-e30-profile66-exceptional-actual-audit-v1"
    assert production["complete"] is audit["complete"] is True
    assert production["source_sha256"] == pin["actual_source_file_sha256"]
    assert audit["source_sha256"] == pin["actual_audit_source_file_sha256"]
    assert audit["production_sha256"] == pin["actual_result_file_sha256"]
    assert production["relaxation_sha256"] == audit["relaxation_sha256"] == pin["relaxation_result_file_sha256"]
    first = sorted(production["rows"], key=lambda row: int(row["template"]))
    second = sorted(audit["rows"], key=lambda row: int(row["template"]))
    assert len(first) == len(second) == len(tasks) == 1_191
    matches: list[dict[str, object]] = []
    shared = (
        "template", "light", "supports", "vectors", "profile_count",
        "above_cutoff", "full_above_cutoff", "maximum_m3",
        "maximum_full_m3", "matches",
    )
    for template, (left, right, light) in enumerate(zip(first, second, tasks)):
        assert all(left[key] == right[key] for key in shared)
        assert int(left["template"]) == template and left["light"] == light
        assert int(left["supports"]) == 310_124
        assert int(left["vectors"]) == 19_847_936
        assert int(left["above_cutoff"]) == len(left["matches"])
        for vector in left["matches"]:
            replay_vector(vector)
            matches.append(vector)
    expected = {
        "vectors": 23_638_891_776,
        "profile_count": 240_672,
        "above_cutoff": 6_244,
        "full_above_cutoff": 1_232,
        "maximum_m3": 1_530,
        "maximum_full_m3": 1_338,
    }
    for packet in (production, audit):
        assert all(int(packet["summary"][key]) == value for key, value in expected.items())
    assert len(matches) == 6_244
    primitive = [vector for vector in matches if int(vector["conductor"]) == 1]
    assert len(primitive) == 1_232
    return primitive


def check_norms(pin: dict[str, str], vectors: list[dict[str, object]]) -> None:
    packet = json.loads((ROOT / pin["norm_result_file"]).read_text())
    assert packet["schema"] == "e1-e30-profile66-exceptional-norm-v1"
    assert packet["complete"] is packet["agreement"] is True
    assert packet["actual_sha256"] == pin["actual_result_file_sha256"]
    assert packet["vectors"] == vectors and len(vectors) == 1_232
    assert packet["flint_norms"] == packet["pari_norms"] and len(packet["flint_norms"]) == 1_232
    assert packet["summary"] == {
        "distinct_norms": 575,
        "maximizing_indices": [1077, 1078],
        "maximum_norm": MAXIMUM_NORM,
        "maximum_norm_bits": 248,
        "norm_at_or_above_2_250": 0,
        "vectors": 1232,
    }
    assert 4 * MAXIMUM_NORM < 2**250 < 5 * MAXIMUM_NORM


def main() -> None:
    pin = load_pin()
    tasks = check_relaxations(pin)
    vectors = check_actual(pin, tasks)
    check_norms(pin, vectors)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in (PROFILE, CONDUCTOR, NORM):
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, ENDPOINT, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "44,779,702,968" in nodes[NODE]["statement"]
    assert "4*N_max<2^250" in nodes[NODE]["statement"]

    print(
        "E1_N256_S16_E30_PROFILE_66_EXCLUSION_PASS "
        "masks=1234 assignments=44779702968 exceptions=33737 templates=1191 "
        "vectors=23638891776 actual=6244 full=1232 max_bits=248 engines=6"
    )


if __name__ == "__main__":
    main()
