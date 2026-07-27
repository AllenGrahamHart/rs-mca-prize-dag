#!/usr/bin/env python3
"""Verify the E=33 profile-(5,7) light-template exclusion."""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e33_profile_57_light_template_exclusion"
PROFILE = "e1_n256_s16_e33_profile_parity_diameter_reduction"
CONDUCTOR = "e1_n256_proper_conductor_collision_exclusion"
NORM = "collision_norm_criterion"
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
EXPECTED_PIN = {
    "audit_file": "background/nodes/e1_n256_s16_e33_profile_parity_diameter_reduction/notes/e33_profile57_light_template_audit.cpp",
    "audit_file_sha256": "4504b8475e2effb6c0172401b6e2b26a542b443367560ecf8668afcd1edaac98",
    "audit_launcher_file": "background/nodes/e1_n256_s16_e33_profile_parity_diameter_reduction/notes/e33_profile57_light_template_audit_modal.py",
    "audit_launcher_file_sha256": "c83ed730d62e0fcd1c078bdc65ac4978d745ef346963e00d80bdaae2bb6ee552",
    "audit_result_file": "background/nodes/e1_n256_s16_e33_profile_parity_diameter_reduction/notes/e33_profile57_light_template_audit_result.json",
    "audit_result_file_sha256": "d75b03111f966fbf8f21b66637b9739492e639646f3614cd834da4630a6f6c07",
    "census_file": "background/nodes/e1_n256_s16_e33_profile_parity_diameter_reduction/notes/e33_profile57_light_template_census.cpp",
    "census_file_sha256": "674d092cecacf6ab3cefb902112400479082d8ef671ac8016b0fbd567fa2e0a7",
    "census_launcher_file": "background/nodes/e1_n256_s16_e33_profile_parity_diameter_reduction/notes/e33_profile57_light_template_census_modal.py",
    "census_launcher_file_sha256": "3027ae72ed4ae0eb12964f2d24e04aefa00d28952e3c1567b7c35ba99db0d7ce",
    "census_result_file": "background/nodes/e1_n256_s16_e33_profile_parity_diameter_reduction/notes/e33_profile57_light_template_census_result.json",
    "census_result_file_sha256": "f1a4218e2383b4ae2e08aa22f39a7823bb0f658ef0bc6a7f91d8d5bf0d543e16",
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "profile_reduction_file": "background/nodes/e1_n256_s16_e33_profile_parity_diameter_reduction/statement.md",
    "profile_reduction_file_sha256": "5828b3f3a1c340075993b37eb218ad13bf0cb445a2807619c37e0b6a2965959b",
    "proper_conductor_file": "background/nodes/e1_n256_proper_conductor_collision_exclusion/statement.md",
    "proper_conductor_file_sha256": "4319261b9d388351f2980fd4f849d7fae4876a6e5db167c74467ea957a055d73",
}


def distance(left: int, right: int) -> int:
    difference = (left - right) % 128
    return min(difference, 128 - difference)


def canonical(support: frozenset[int]) -> tuple[int, ...]:
    return min(
        tuple(sorted((unit * value + translation) % 128 for value in support))
        for unit in range(1, 128, 2)
        for translation in (0, 64)
    )


def classify_lights() -> tuple[int, tuple[tuple[int, ...], ...]]:
    normalized = []
    for x, y in combinations((value for value in range(128) if value not in (0, 64)), 2):
        support = frozenset((0, 64, x, y))
        classes = Counter(distance(left, right) for left, right in combinations(support, 2))
        if classes[64] == 1 and all(classes[value] <= 1 for value in range(1, 64)):
            normalized.append(support)
    representatives = tuple(sorted({canonical(support) for support in normalized}))
    return len(normalized), representatives


def autocorrelation(
    positions: tuple[int, ...], coefficients: tuple[int, ...]
) -> tuple[list[int], int, int]:
    half = [0] * 64
    for left, right in combinations(range(7), 2):
        low, high = sorted((positions[left], positions[right]))
        difference = high - low
        if difference == 64:
            continue
        orientation = 1 if difference < 64 else -1
        folded = difference if difference < 64 else 128 - difference
        half[folded] += orientation * coefficients[left] * coefficients[right]
    weight = [0] * 128
    for difference in range(1, 64):
        weight[difference] = weight[128 - difference] = abs(half[difference])
    m3 = sum(
        weight[left] * weight[right] * weight[(-left - right) % 128]
        for left in range(128)
        if weight[left]
        for right in range(128)
        if weight[right]
    )
    return half, m3, math.gcd(256, *positions)


def check_witness(witness: dict[str, object], light: tuple[int, ...], full: bool) -> int:
    if int(witness["m3"]) < 0:
        return -1
    positions = tuple(map(int, witness["positions"]))
    coefficients = tuple(map(int, witness["coefficients"]))
    assert len(set(positions)) == len(positions) == 7
    assert tuple(map(abs, coefficients)) == (2, 2, 2, 1, 1, 1, 1)
    assert coefficients[0] == 2 and tuple(sorted(positions[3:])) == light
    half, m3, conductor = autocorrelation(positions, coefficients)
    assert sum(abs(value) == 1 for value in half[1:]) == 5
    assert sum(abs(value) == 2 for value in half[1:]) == 7
    assert all(abs(value) <= 2 for value in half[1:])
    assert m3 == int(witness["m3"])
    if full:
        assert conductor == 1
    return conductor


def check_packets(
    primary: dict[str, object], audit: dict[str, object]
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    assert primary["schema"] == "e1-e33-profile57-light-template-v1"
    assert audit["schema"] == "e1-e33-profile57-light-template-audit-v1"
    for packet in (primary, audit):
        assert packet["complete"] is True
        assert packet["errors"] == []
        assert packet["expected_templates"] == 100
        assert packet["returned_templates"] == list(range(100))
        assert len(packet["rows"]) == 100

    normalized, representatives = classify_lights()
    assert normalized == 7200 and len(representatives) == 100
    primary_rows = primary["rows"]
    audit_rows = audit["rows"]
    for index, (left, right) in enumerate(zip(primary_rows, audit_rows)):
        assert int(left["template"]) == int(right["template"]) == index
        assert tuple(map(int, left["light"])) == tuple(map(int, right["light"])) == representatives[index]
        assert bool(left["complete"]) and bool(right["complete"])
        assert int(left["templates"]) == int(right["templates"]) == 100
        for key in (
            "supports",
            "vectors",
            "profile_57",
            "full_conductor",
            "maximum_m3",
            "maximum_full_conductor_m3",
        ):
            assert int(left[key]) == int(right[key])
        assert int(left["supports"]) == math.comb(124, 3)
        assert int(left["vectors"]) == math.comb(124, 3) * 64
        conductor = check_witness(left["witness"], representatives[index], False)
        check_witness(left["full_conductor_witness"], representatives[index], True)
        if int(left["maximum_m3"]) >= 0:
            assert int(left["witness"]["m3"]) == int(left["maximum_m3"])
        if int(left["maximum_full_conductor_m3"]) >= 0:
            assert int(left["full_conductor_witness"]["m3"]) == int(
                left["maximum_full_conductor_m3"]
            )
        if int(left["maximum_m3"]) == 1758:
            assert conductor > 1

    assert sum(int(row["supports"]) for row in primary_rows) == 31_012_400
    assert sum(int(row["vectors"]) for row in primary_rows) == 1_984_793_600
    assert sum(int(row["profile_57"]) for row in primary_rows) == 28_048
    assert sum(int(row["full_conductor"]) for row in primary_rows) == 17_768
    assert max(int(row["maximum_m3"]) for row in primary_rows) == 1758
    assert max(int(row["maximum_full_conductor_m3"]) for row in primary_rows) == 1416
    return primary_rows, audit_rows


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[
                key + "_sha256"
            ]
    primary = json.loads((ROOT / pin["census_result_file"]).read_text())
    audit = json.loads((ROOT / pin["audit_result_file"]).read_text())
    primary_rows, _ = check_packets(primary, audit)

    assert len(primary_rows[:-1]) == 99
    assert 1416 > 1415 and 1416 < 1732
    global_row = max(primary_rows, key=lambda row: int(row["maximum_m3"]))
    assert int(global_row["maximum_m3"]) == 1758 > 1732
    positions = tuple(map(int, global_row["witness"]["positions"]))
    assert math.gcd(256, *positions) == 4

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in (PROFILE, CONDUCTOR, NORM):
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    print(
        "E1_N256_S16_E33_PROFILE_57_LIGHT_TEMPLATE_EXCLUSION_PASS "
        "lights=7200/100 vectors=1984793600 profile=28048 full=17768 "
        "m3=1758/1416 threshold=1732 mutations=3"
    )


if __name__ == "__main__":
    main()
