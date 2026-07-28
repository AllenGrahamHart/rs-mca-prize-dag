#!/usr/bin/env python3
"""Independent checker for the complete E25 nine-profile census."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RESULT = HERE / "e25_nine_profile_census_result.json"
PRODUCTION_SOURCE = HERE / "e25_nine_profile_census.cpp"
AUDIT_SOURCE = HERE / "e25_nine_profile_census_audit.cpp"
DRIVER = HERE / "e25_nine_profile_census_modal.py"
REDUCTION = HERE / "e25_profile_parity_probe_result.json"
ATLAS = (
    ROOT
    / "background/nodes/e1_n256_s16_e27_profile_parity_light_reduction/notes"
    / "e27_profile_parity_probe_result.json"
)
PROFILES = (
    (5, 5, 0, 0, 0), (1, 6, 0, 0, 0), (4, 3, 1, 0, 0),
    (0, 4, 1, 0, 0), (3, 1, 2, 0, 0), (5, 1, 0, 1, 0),
    (1, 2, 0, 1, 0), (0, 0, 1, 1, 0), (0, 0, 0, 0, 1),
)


def strip_runtime(row: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in row.items() if key != "worker_seconds"}


def replay(vector: dict[str, object]) -> tuple[int, int, int]:
    profile_index = int(vector["profile"])
    positions = [int(value) for value in vector["positions"]]
    coefficients = [int(value) for value in vector["coefficients"]]
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
    assert max(magnitudes) <= 5
    profile = tuple(magnitudes.count(magnitude) for magnitude in range(1, 6))
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
    conductor = math.gcd(256, *positions)
    assert m3 == int(vector["m3"]) > 13
    assert conductor == int(vector["conductor"])
    return profile_index, conductor, m3


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    def extrema(key: str, profile: int, minimum: bool) -> int:
        values = [int(row[key][profile]) for row in rows if int(row[key][profile]) >= 0]
        return (min(values) if minimum else max(values)) if values else -1

    return {
        "vectors": sum(int(row["vectors"]) for row in rows),
        "profile_counts": [sum(int(row["profile_counts"][p]) for row in rows) for p in range(9)],
        "above_cutoff": [sum(int(row["above_cutoff"][p]) for row in rows) for p in range(9)],
        "full_above_cutoff": [sum(int(row["full_above_cutoff"][p]) for row in rows) for p in range(9)],
        "minimum_m3": [extrema("minimum_m3", p, True) for p in range(9)],
        "minimum_full_m3": [extrema("minimum_full_m3", p, True) for p in range(9)],
        "maximum_m3": [extrema("maximum_m3", p, False) for p in range(9)],
        "maximum_full_m3": [extrema("maximum_full_m3", p, False) for p in range(9)],
    }


def without_worker(summary: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in summary.items() if key != "worker_seconds"}


def main() -> None:
    packet = json.loads(RESULT.read_text())
    atlas = json.loads(ATLAS.read_text())
    assert packet["schema"] == "e1-e25-nine-profile-census-v1"
    assert packet["complete"] is packet["agreement"] is True
    assert packet["error"] is None and packet["mismatch_templates"] == []
    assert packet["completed_production"] == packet["completed_audit"] == packet["expected_each"] == 111
    assert hashlib.sha256(PRODUCTION_SOURCE.read_bytes()).hexdigest() == packet["source_sha256"]
    assert hashlib.sha256(AUDIT_SOURCE.read_bytes()).hexdigest() == packet["audit_source_sha256"]
    assert hashlib.sha256(DRIVER.read_bytes()).hexdigest() == packet["driver_sha256"]
    assert hashlib.sha256(REDUCTION.read_bytes()).hexdigest() == packet["reduction_sha256"]
    assert hashlib.sha256(ATLAS.read_bytes()).hexdigest() == packet["atlas_sha256"]

    representatives = atlas["light_geometry"]["orbit_representatives"]
    tasks = [[int(value) for value in row] for odd in ("1", "5") for row in representatives[odd]]
    production = sorted(packet["production"], key=lambda row: int(row["template"]))
    audit = sorted(packet["audit"], key=lambda row: int(row["template"]))
    assert len(production) == len(audit) == len(tasks) == 111
    matches = []
    for template, (left, right, light) in enumerate(zip(production, audit, tasks)):
        assert strip_runtime(left) == strip_runtime(right)
        assert int(left["template"]) == template and left["light"] == light
        assert left["complete"] is True
        assert int(left["supports"]) == math.comb(124, 3) == 310_124
        assert int(left["vectors"]) == 19_847_936
        assert len(left["matches"]) == sum(int(value) for value in left["above_cutoff"])
        for vector in left["matches"]:
            replay(vector)
            matches.append(vector)

    expected = summarize(production)
    assert without_worker(packet["production_summary"]) == expected
    assert without_worker(packet["audit_summary"]) == expected
    assert expected["vectors"] == 2_203_120_896
    assert len(matches) == sum(expected["above_cutoff"])
    assert sum(int(vector["conductor"]) == 1 for vector in matches) == sum(expected["full_above_cutoff"])
    print(
        "E25_NINE_PROFILE_CENSUS_CHECK_PASS "
        f"templates=111 vectors=2203120896 profile={sum(expected['profile_counts'])} "
        f"exceptions={len(matches)} full={sum(expected['full_above_cutoff'])}"
    )


if __name__ == "__main__":
    main()
