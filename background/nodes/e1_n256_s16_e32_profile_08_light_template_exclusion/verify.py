#!/usr/bin/env python3
"""Verify the E=32 profile-(0,8) light-template exclusion."""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e32_profile_08_light_template_exclusion"
PROFILE = "e1_n256_s16_e32_profile_parity_diameter_reduction"
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
TEMPLATES = tuple(
    frozenset((0, 64, step, 64 + step)) for step in (1, 2, 4, 8, 16, 32)
)
EXPECTED_PIN = {
    "audit_census_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_profile08_light_template_audit.cpp",
    "audit_census_file_sha256": "7913b7b94f4d40750f49ad5b4407c08e1755c086986f4c807628889a0c0a48f0",
    "audit_launcher_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_profile08_light_template_audit_modal.py",
    "audit_launcher_file_sha256": "29a9fce58106450f6d6777f44a5383d1fd89e756e9abfb06d0a986d91c799527",
    "audit_result_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_profile08_light_template_audit_result.json",
    "audit_result_file_sha256": "a2d9e792c3342c46d8aa3c6ad551145de82ddb58b199b6af6e5e3036c1888705",
    "census_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_profile08_light_template_census.cpp",
    "census_file_sha256": "f088b99e9c7b2b68259752bfbe8a8de946ec147d0f7817d775769fbe35ff021d",
    "launcher_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_profile08_light_template_census_modal.py",
    "launcher_file_sha256": "64795a8d2d2ffbe4a92325423c9d9859d1e938f37bf9483a98f388b5b7212851",
    "profile_reduction_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/statement.md",
    "profile_reduction_file_sha256": "2c775ba148a35987157c2ce170dbc18b4a338f194cd990b304904e8726ed4edd",
    "result_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_profile08_light_template_census_result.json",
    "result_file_sha256": "5e77f01f4c2888f79d50a14c881d7caf5a262dad56c58e4befad1d022f6bf2dd",
}


def distance(left: int, right: int) -> int:
    difference = (left - right) % 128
    return min(difference, 128 - difference)


def light_orbit(templates: tuple[frozenset[int], ...] = TEMPLATES) -> set[frozenset[int]]:
    return {
        frozenset((unit * value + translation) % 128 for value in template)
        for template in templates
        for unit in range(1, 128, 2)
        for translation in range(128)
    }


def check_light_classification() -> None:
    orbit = light_orbit()
    assert TEMPLATES[-1] not in light_orbit(TEMPLATES[:-1])
    normalized = 0
    for rest in combinations(range(1, 128), 3):
        support = frozenset((0,) + rest)
        classes = Counter(
            distance(left, right) for left, right in combinations(support, 2)
        )
        diameter_count = classes[64]
        if diameter_count not in (0, 2):
            continue
        if any(count % 2 for chord, count in classes.items() if chord != 64):
            continue
        normalized += 1
        assert diameter_count == 2
        assert support in orbit
    assert normalized == 63


def check_production(packet: dict[str, object], source: Path) -> None:
    assert packet["schema"] == "e1-e32-profile08-light-template-v1"
    assert packet["complete"] is True and int(packet["shards"]) == 8
    assert packet["source_sha256"] == hashlib.sha256(source.read_bytes()).hexdigest()
    rows = packet["rows"]
    assert isinstance(rows, list) and len(rows) == 48
    for template in range(6):
        selected = [row for row in rows if int(row["template"]) == template]
        assert {int(row["shard"]) for row in selected} == set(range(8))
        assert all(bool(row["complete"]) and int(row["shards"]) == 8 for row in selected)
        assert sum(int(row["supports"]) for row in selected) == math.comb(124, 3)
        assert sum(int(row["vectors"]) for row in selected) == math.comb(124, 3) * 64
        assert sum(int(row["supports"]) for row in selected[:-1]) < math.comb(124, 3)
        assert all(
            int(row[key]) == expected
            for row in selected
            for key, expected in (
                ("profile_08", 0),
                ("full_conductor", 0),
                ("maximum_m3", -1),
                ("maximum_full_conductor_m3", -1),
            )
        )
        summary = packet["summary"][str(template)]
        assert int(summary["supports"]) == math.comb(124, 3)
        assert int(summary["vectors"]) == math.comb(124, 3) * 64
        assert all(
            int(summary[key]) == expected
            for key, expected in (
                ("profile_08", 0),
                ("full_conductor", 0),
                ("maximum_m3", -1),
                ("maximum_full_conductor_m3", -1),
            )
        )


def check_audit(packet: dict[str, object], source: Path) -> None:
    assert packet["schema"] == "e1-e32-profile08-light-template-audit-v1"
    assert packet["complete"] is True
    assert packet["source_sha256"] == hashlib.sha256(source.read_bytes()).hexdigest()
    rows = packet["rows"]
    assert isinstance(rows, list) and {int(row["template"]) for row in rows} == set(range(6))
    for row in rows:
        assert bool(row["complete"])
        assert int(row["supports"]) == math.comb(124, 3)
        assert int(row["vectors"]) == math.comb(124, 3) * 64
        assert int(row["profile_08"]) == int(row["full_conductor"]) == 0
        assert int(row["maximum_m3"]) == int(row["maximum_full_conductor_m3"]) == -1


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]

    check_light_classification()
    check_production(
        json.loads((ROOT / pin["result_file"]).read_text()),
        ROOT / pin["census_file"],
    )
    check_audit(
        json.loads((ROOT / pin["audit_result_file"]).read_text()),
        ROOT / pin["audit_census_file"],
    )
    assert 6 * math.comb(124, 3) * 64 == 119_087_616

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[PROFILE]["status"] == "PROVED"
    assert (PROFILE, NODE, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "119,087,616" in nodes[NODE]["statement"]

    print(
        "E1_N256_S16_E32_PROFILE_08_LIGHT_TEMPLATE_EXCLUSION_PASS "
        "normalized=63 templates=6 vectors=119087616 retained=0 mutations=3"
    )


if __name__ == "__main__":
    main()
