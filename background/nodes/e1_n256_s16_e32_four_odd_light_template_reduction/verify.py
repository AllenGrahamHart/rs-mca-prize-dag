#!/usr/bin/env python3
"""Verify the E32 common four-odd light-template reduction."""

from __future__ import annotations

import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e32_four_odd_light_template_reduction"
PROFILE = "e1_n256_s16_e32_profile_parity_diameter_reduction"
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
EXPECTED_PIN = {
    "audit_classifier_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_four_odd_light_orbit_check.py",
    "audit_classifier_file_sha256": "4cfa16da91b32258f7a9f69c546d132c9692fbf7d53de01ccb47857e4ed537c8",
    "classifier_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_four_odd_light_orbit_classifier.py",
    "classifier_file_sha256": "39f0822ff8be654b245476521301497efa5c24487fbb584d68dcc0651117aa2c",
    "profile_reduction_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/statement.md",
    "profile_reduction_file_sha256": "2c775ba148a35987157c2ce170dbc18b4a338f194cd990b304904e8726ed4edd",
    "result_file": "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_four_odd_light_orbit_result.json",
    "result_file_sha256": "daaf781348f8b691c959c6172e900a6791b00904a6131c60c16f7d98eeec7e98",
}


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]

    primary = subprocess.run(
        ["python3", str(ROOT / pin["classifier_file"])],
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    audit = subprocess.run(
        ["python3", str(ROOT / pin["audit_classifier_file"])],
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert "normalized=28800 orbits=148" in primary.stdout
    assert "gap_supports=28800 orbits=148" in audit.stdout
    assert hashlib.sha256((ROOT / pin["result_file"]).read_bytes()).hexdigest() == pin[
        "result_file_sha256"
    ]

    packet = json.loads((ROOT / pin["result_file"]).read_text())
    assert packet["schema"] == "e1-e32-four-odd-light-orbits-v1"
    assert packet["complete"] is True
    assert int(packet["normalized_supports"]) == 28_800
    assert int(packet["orbits"]) == 148
    assert packet["normalized_orbit_size_histogram"] == {
        "32": 4, "64": 16, "128": 40, "256": 88,
    }
    assert packet["repeated_shape_histogram"] == {"wedge": 148}
    assert sum(int(row["normalized_count"]) for row in packet["rows"]) == 28_800
    assert Counter(int(row["normalized_count"]) for row in packet["rows"]) == Counter(
        {32: 4, 64: 16, 128: 40, 256: 88}
    )
    assert all(row["repeated_shape"] == "wedge" for row in packet["rows"])
    assert 4 * 32 + 16 * 64 + 40 * 128 + 88 * 256 == 28_800

    diameter_ledgers = {
        4 * heavy_light + 16 * heavy_heavy
        for heavy_heavy in range(2)
        for heavy_light in range(4)
        if heavy_light <= 3 - 2 * heavy_heavy
    }
    assert diameter_ledgers == {0, 4, 8, 12, 16, 20}
    assert {(diameter, (diameter - 70) // 2) for diameter in diameter_ledgers} == {
        (0, -35), (4, -33), (8, -31), (12, -29), (16, -27), (20, -25),
    }

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[PROFILE]["status"] == "PROVED"
    assert (PROFILE, NODE, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "28,800" in nodes[NODE]["statement"] and "148" in nodes[NODE]["statement"]

    print(
        "E1_N256_S16_E32_FOUR_ODD_LIGHT_TEMPLATE_REDUCTION_PASS "
        "supports=28800 orbits=148 wedges=148 diameters=6 mutations=1"
    )


if __name__ == "__main__":
    main()
