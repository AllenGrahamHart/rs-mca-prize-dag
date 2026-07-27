#!/usr/bin/env python3
"""Verify the E26 four-six-odd-profile exclusion packet."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e26_four_six_odd_profile_exclusion"
ENDPOINT = "e1_n256_s16_e26_endpoint_exclusion"
REDUCTION = "e1_n256_s16_e26_profile_parity_light_reduction"
CONDUCTOR = "e1_n256_proper_conductor_collision_exclusion"
NORM = "collision_norm_criterion"
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
PROFILES = (
    (6, 5, 0, 0),
    (5, 3, 1, 0),
    (4, 1, 2, 0),
    (6, 1, 0, 1),
)
MAXIMUM_NORM = 1139098407599461804511111865916270680930143333943822578584573946997885235216
PROFILE_MAXIMUM_NORMS = [
    514522447408508265710050094914745110851293119825043128038848015175225737248,
    MAXIMUM_NORM,
    607184693371193095509131406353754381037244320900017288437685057679154283524,
    188175792653561568256817788477665516320080335682584556336488275853045825538,
]
EXPECTED_SUMMARY = {
    "vectors": 24_492_353_024,
    "profile_counts": [51_562, 23_884, 1_614, 1_788],
    "above_cutoff": [48_918, 23_232, 1_590, 874],
    "full_above_cutoff": [32_096, 12_632, 408, 272],
    "maximum_m3": [1_074, 942, 870, 606],
    "maximum_full_m3": [1_062, 942, 690, 606],
}


def strip_runtime(row: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in row.items() if key != "worker_seconds"}


def summary_without_runtime(summary: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in summary.items() if key != "worker_seconds"}


def load_pin() -> dict[str, str]:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    required_files = {
        "reduction_statement_file",
        "atlas_file",
        "production_source_file",
        "audit_source_file",
        "census_driver_file",
        "census_result_file",
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


def replay_vector(vector: dict[str, object]) -> tuple[int, int]:
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
    assert max(magnitudes) <= 4
    profile = tuple(magnitudes.count(magnitude) for magnitude in range(1, 5))
    assert profile == PROFILES[profile_index]
    weights = [0] * 128
    for difference, magnitude in enumerate(magnitudes, start=1):
        weights[difference] = weights[128 - difference] = magnitude
    support = [index for index, value in enumerate(weights) if value]
    m3 = sum(
        weights[left] * weights[right] * weights[(-left - right) % 128]
        for left in support
        for right in support
    )
    assert m3 == int(vector["m3"]) > 228
    assert math.gcd(256, *positions) == 1
    return profile_index, m3


def check_censuses(pin: dict[str, str]) -> list[dict[str, object]]:
    atlas = json.loads((ROOT / pin["atlas_file"]).read_text())
    assert atlas["complete"] is True
    assert atlas["summary"]["affine_light_orbits"] == 1_234
    assert atlas["summary"]["orbits_per_mask_histogram"] == {"1": 1_234}
    tasks = [
        [int(value) for value in row["orbits"][0]]
        for row in sorted(atlas["rows"], key=lambda row: int(row["odd_mask"]))
    ]

    packet = json.loads((ROOT / pin["census_result_file"]).read_text())
    assert packet["schema"] == "e1-e26-four-six-odd-profile-census-v1"
    assert packet["complete"] is packet["agreement"] is True
    assert packet["error"] is None and packet["mismatch_templates"] == []
    assert packet["completed_production"] == packet["completed_audit"] == packet["expected_each"] == 1_234
    assert packet["source_sha256"] == pin["production_source_file_sha256"]
    assert packet["audit_source_sha256"] == pin["audit_source_file_sha256"]
    assert packet["atlas_sha256"] == pin["atlas_file_sha256"]
    assert summary_without_runtime(packet["production_summary"]) == EXPECTED_SUMMARY
    assert summary_without_runtime(packet["audit_summary"]) == EXPECTED_SUMMARY

    production = sorted(packet["production"], key=lambda row: int(row["template"]))
    audit = sorted(packet["audit"], key=lambda row: int(row["template"]))
    assert len(production) == len(audit) == len(tasks) == 1_234
    vectors: list[dict[str, object]] = []
    for template, (left, right, light) in enumerate(zip(production, audit, tasks)):
        assert strip_runtime(left) == strip_runtime(right)
        assert int(left["template"]) == template and left["light"] == light
        assert left["complete"] is True
        assert int(left["supports"]) == math.comb(124, 3) == 310_124
        assert int(left["vectors"]) == 19_847_936
        assert sum(int(value) for value in left["full_above_cutoff"]) == len(left["matches"])
        for vector in left["matches"]:
            replay_vector(vector)
            vectors.append(vector)
    assert len(vectors) == 45_408
    assert sum(EXPECTED_SUMMARY["above_cutoff"]) - len(vectors) == 29_206
    return vectors


def flatten_norm_rows(rows: list[dict[str, object]]) -> list[int]:
    assert len(rows) == 46
    result: list[int] = []
    for batch, row in enumerate(sorted(rows, key=lambda item: int(item["batch"]))):
        assert int(row["batch"]) == batch
        expected = 408 if batch == 45 else 1_000
        assert len(row["norms"]) == expected
        result.extend(int(value) for value in row["norms"])
    return result


def check_norms(pin: dict[str, str], vectors: list[dict[str, object]]) -> None:
    packet = json.loads((ROOT / pin["norm_result_file"]).read_text())
    assert packet["schema"] == "e1-e26-four-six-odd-profile-norm-v1"
    assert packet["complete"] is packet["agreement"] is True
    assert packet["error"] is None
    assert packet["source_sha256"] == pin["norm_driver_file_sha256"]
    assert packet["census_sha256"] == pin["census_result_file_sha256"]
    assert packet["vectors"] == len(vectors) == 45_408
    assert packet["batch_size"] == 1_000
    assert packet["expected_batches"] == packet["completed_flint"] == packet["completed_pari"] == 46
    flint_norms = flatten_norm_rows(packet["flint"])
    pari_norms = flatten_norm_rows(packet["pari"])
    assert flint_norms == pari_norms and len(flint_norms) == len(vectors)
    summary = packet["summary"]
    assert summary["vectors"] == 45_408
    assert summary["distinct_norms"] == 20_636
    assert summary["maximum_norm"] == max(flint_norms) == MAXIMUM_NORM
    assert summary["maximum_norm_bits"] == MAXIMUM_NORM.bit_length() == 250
    assert summary["norms_at_or_above_2_250"] == 0
    assert summary["eligible_distinct_odd_parts"] == 0
    assert summary["prime_eligible_odd_parts"] == 0
    assert summary["candidate_vectors"] == 0
    assert summary["candidate_indices"] == [] and packet["candidate_records"] == []
    profile_maxima = [
        max(norm for norm, vector in zip(flint_norms, vectors) if int(vector["profile"]) == profile)
        for profile in range(4)
    ]
    assert profile_maxima == summary["profile_maximum_norms"] == PROFILE_MAXIMUM_NORMS
    assert [value.bit_length() for value in profile_maxima] == summary["profile_maximum_bits"] == [249, 250, 249, 247]
    assert MAXIMUM_NORM < 2**250 < 2 * MAXIMUM_NORM


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
    assert "24,492,353,024" in nodes[NODE]["statement"]
    assert "N_max<2^250<2*N_max" in nodes[NODE]["statement"]

    print("E1_N256_S16_E26_FOUR_SIX_ODD_PROFILE_EXCLUSION_PASS templates=1234 vectors=24492353024 profile=78848 exceptions=74614 full=45408 max_bits=250 engines=4")


if __name__ == "__main__":
    main()
