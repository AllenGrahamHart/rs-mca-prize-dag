#!/usr/bin/env python3
"""Verify the E=33 profile-(1,8) light-template exclusion."""

from __future__ import annotations

import hashlib
import json
import math
import subprocess
import tempfile
from collections import Counter
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e33_profile_18_light_template_exclusion"
PROFILE = "e1_n256_s16_e33_profile_parity_diameter_reduction"
NORM = "collision_norm_criterion"
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
EXPECTED = {
    0: (112, 112, 912, 912),
    1: (560, 448, 1200, 1200),
    2: (856, 64, 1284, 696),
    3: (592, 0, 1248, -1),
    4: (0, 0, -1, -1),
    5: (3280, 3280, 864, 864),
    6: (2992, 1760, 864, 864),
    7: (3504, 2624, 1284, 864),
    8: (3824, 2048, 1356, 192),
    9: (704, 0, 1296, -1),
    10: (720, 256, 1188, 1164),
}
TEMPLATES = (
    frozenset((0, 1, 64, 127)),
    frozenset((0, 2, 64, 126)),
    frozenset((0, 4, 64, 124)),
    frozenset((0, 8, 64, 120)),
    frozenset((0, 16, 64, 112)),
    frozenset((0, 1, 63, 64)),
    frozenset((0, 2, 62, 64)),
    frozenset((0, 4, 60, 64)),
    frozenset((0, 8, 56, 64)),
    frozenset((0, 16, 48, 64)),
    frozenset((0, 16, 32, 64)),
)
EXPECTED_PIN = {
    "audit_census_file": "background/nodes/e1_n256_s16_e33_profile_parity_diameter_reduction/notes/e33_profile18_light_template_audit.cpp",
    "audit_census_file_sha256": "855dc2a15f30a64650285b8ebd61631b3476b65424d8c42548832be5f9f74ad5",
    "census_file": "background/nodes/e1_n256_s16_e33_profile_parity_diameter_reduction/notes/e33_profile18_light_template_census.cpp",
    "census_file_sha256": "d38f971d9343dc3a3186ea86f32f7eed65700816d9be047ec7ab6032850e74dd",
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "launcher_file": "background/nodes/e1_n256_s16_e33_profile_parity_diameter_reduction/notes/e33_profile18_light_template_census_modal.py",
    "launcher_file_sha256": "e2a3ad44936650f60803d763164344af405f586bbc6f0b9622267c2215ff5d13",
    "profile_reduction_file": "background/nodes/e1_n256_s16_e33_profile_parity_diameter_reduction/statement.md",
    "profile_reduction_file_sha256": "5828b3f3a1c340075993b37eb218ad13bf0cb445a2807619c37e0b6a2965959b",
    "result_file": "background/nodes/e1_n256_s16_e33_profile_parity_diameter_reduction/notes/e33_profile18_light_template_census_result.json",
    "result_file_sha256": "19a9d8509f6acf55cb667a90b207a94cf46376262569840f75dd5ad6f55111ec",
}


def distance(left: int, right: int) -> int:
    difference = (left - right) % 128
    return min(difference, 128 - difference)


def light_orbit(
    templates: tuple[frozenset[int], ...] = TEMPLATES,
) -> set[frozenset[int]]:
    return {
        frozenset((unit * value + translation) % 128 for value in template)
        for template in templates
        for unit in range(1, 128, 2)
        for translation in range(128)
    }


def check_light_classification() -> None:
    orbit = light_orbit()
    assert frozenset((0, 1, 63, 64)) not in light_orbit(TEMPLATES[:5] + TEMPLATES[10:])
    normalized = 0
    for x, y in combinations((value for value in range(128) if value not in (0, 64)), 2):
        support = frozenset((0, 64, x, y))
        diameter_count = sum(
            distance(left, right) == 64 for left, right in combinations(support, 2)
        )
        classes = Counter(
            distance(left, right)
            for left, right in combinations(support, 2)
            if distance(left, right) != 64
        )
        if diameter_count != 1 or sum(value % 2 for value in classes.values()) != 1:
            continue
        normalized += 1
        assert support in orbit
    assert normalized == 132


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
    conductor = math.gcd(256, *positions)
    return half, m3, conductor


def check_witness(witness: dict[str, object], template: int, full: bool) -> None:
    if int(witness["m3"]) < 0:
        return
    positions = tuple(map(int, witness["positions"]))
    coefficients = tuple(map(int, witness["coefficients"]))
    assert len(set(positions)) == len(positions) == 7
    assert tuple(map(abs, coefficients)) == (2, 2, 2, 1, 1, 1, 1)
    assert coefficients[0] == 2
    assert frozenset(positions[3:]) == TEMPLATES[template]
    half, m3, conductor = autocorrelation(positions, coefficients)
    assert sum(abs(value) == 1 for value in half[1:]) == 1
    assert sum(abs(value) == 2 for value in half[1:]) == 8
    assert all(abs(value) <= 2 for value in half[1:])
    assert m3 == int(witness["m3"])
    if full:
        assert conductor == 1


def summarize(rows: list[dict[str, object]]) -> dict[int, tuple[int, int, int, int]]:
    answer = {}
    for template in range(11):
        selected = [row for row in rows if int(row["template"]) == template]
        answer[template] = (
            sum(int(row["profile_18"]) for row in selected),
            sum(int(row["full_conductor"]) for row in selected),
            max(int(row["maximum_m3"]) for row in selected),
            max(int(row["maximum_full_conductor_m3"]) for row in selected),
        )
    return answer


def check_packet(packet: dict[str, object], source: Path) -> None:
    assert packet["schema"] == "e1-e33-profile18-light-template-v1"
    assert packet["complete"] is True and int(packet["shards"]) == 8
    assert packet["source_sha256"] == hashlib.sha256(source.read_bytes()).hexdigest()
    rows = packet["rows"]
    assert isinstance(rows, list) and len(rows) == 88
    for template in range(11):
        selected = [row for row in rows if int(row["template"]) == template]
        assert {int(row["shard"]) for row in selected} == set(range(8))
        assert all(bool(row["complete"]) and int(row["shards"]) == 8 for row in selected)
        assert sum(int(row["supports"]) for row in selected) == math.comb(124, 3)
        assert sum(int(row["vectors"]) for row in selected) == math.comb(124, 3) * 64
        assert all(int(row["vectors"]) == 64 * int(row["supports"]) for row in selected)
        assert sum(int(row["supports"]) for row in selected[:-1]) < math.comb(124, 3)
        for row in selected:
            check_witness(row["witness"], template, False)
            check_witness(row["full_conductor_witness"], template, True)
            if int(row["maximum_m3"]) >= 0:
                assert int(row["witness"]["m3"]) == int(row["maximum_m3"])
            if int(row["maximum_full_conductor_m3"]) >= 0:
                assert int(row["full_conductor_witness"]["m3"]) == int(
                    row["maximum_full_conductor_m3"]
                )
    assert summarize(rows) == EXPECTED
    for template, expected in EXPECTED.items():
        summary = packet["summary"][str(template)]
        assert (
            int(summary["profile_18"]),
            int(summary["full_conductor"]),
            int(summary["maximum_m3"]),
            int(summary["maximum_full_conductor_m3"]),
        ) == expected


def compile_binary(source: Path, directory: Path) -> Path:
    binary = directory / "e33_profile18_light_templates"
    subprocess.run(
        ["g++", "-O3", "-std=c++17", str(source), "-o", str(binary)],
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    return binary


def replay(binary: Path) -> list[dict[str, object]]:
    rows = []
    for template in range(11):
        completed = subprocess.run(
            [str(binary), str(template), "0", "1"],
            check=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
        rows.append(json.loads(completed.stdout))
    return rows


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[
                key + "_sha256"
            ]

    source = ROOT / pin["census_file"]
    packet = json.loads((ROOT / pin["result_file"]).read_text())
    check_packet(packet, source)
    check_light_classification()
    with tempfile.TemporaryDirectory() as temporary:
        rows = replay(compile_binary(source, Path(temporary)))
    assert summarize(rows) == EXPECTED
    assert all(int(row["supports"]) == math.comb(124, 3) for row in rows)
    assert sum(expected[0] for expected in EXPECTED.values()) == 17144
    assert max(expected[2] for expected in EXPECTED.values()) == 1356 < 1732
    assert max(expected[2] for expected in EXPECTED.values()) > 1355

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in (PROFILE, NORM):
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "218,327,296" in nodes[NODE]["statement"]
    print(
        "E1_N256_S16_E33_PROFILE_18_LIGHT_TEMPLATE_EXCLUSION_PASS "
        "light_supports=132 vectors=218327296 profile=17144 m3=1356 "
        "threshold=1732 mutations=3"
    )


if __name__ == "__main__":
    main()
