#!/usr/bin/env python3
"""Verify the E25 profile/parity/light reduction packet."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e25_profile_parity_light_reduction"
ENDPOINT = "e1_n256_s16_e25_endpoint_exclusion"
DEPENDENCIES = {
    "e1_n256_s16_e26_endpoint_exclusion",
    "e1_n256_s16_sparse_l1_variance_exclusion",
    "e1_n256_s16_signed_chord_collision_gate",
    "e1_n256_s16_e27_profile_parity_light_reduction",
    "collision_norm_criterion",
}
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
PROFILES = [
    [5, 5, 0, 0, 0], [8, 2, 1, 0, 0], [1, 6, 0, 0, 0],
    [4, 3, 1, 0, 0], [7, 0, 2, 0, 0], [0, 4, 1, 0, 0],
    [3, 1, 2, 0, 0], [9, 0, 0, 1, 0], [5, 1, 0, 1, 0],
    [1, 2, 0, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 1],
]
CAPS = [1310, 1190, 1178, 1054, 954, 950, 846, 830, 714, 630, 506, 250]
ODD = [5, 9, 1, 5, 9, 1, 5, 9, 5, 1, 1, 1]
SURVIVORS = {
    (5, 5, 0, 0, 0), (1, 6, 0, 0, 0), (4, 3, 1, 0, 0),
    (0, 4, 1, 0, 0), (3, 1, 2, 0, 0), (5, 1, 0, 1, 0),
    (1, 2, 0, 1, 0), (0, 0, 1, 1, 0), (0, 0, 0, 0, 1),
}


def load_pin() -> dict[str, str]:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]
    return pin


def main() -> None:
    pin = load_pin()
    packet = json.loads((ROOT / pin["probe_result_file"]).read_text())
    assert packet["schema"] == "e1-e25-profile-parity-route-probe-v1"
    assert packet["complete"] is True and packet["variance"] == 50 and packet["energy"] == 25
    assert packet["source_sha256"] == pin["probe_source_file_sha256"]
    assert packet["atlas_sha256"] == pin["atlas_result_file_sha256"]
    assert packet["l1_bound"] == 15
    assert packet["slack_trace"] == [
        [22, 3, 53], [21, 7, 49], [20, 11, 45], [19, 15, 41],
        [18, 19, 37], [17, 23, 33], [16, 27, 29], [15, 31, 25],
        [14, 35, 21], [13, 39, 17], [12, 43, 13], [11, 47, 9],
    ]
    assert packet["profile_count"] == len(packet["profiles"]) == 12
    assert [row["profile"] for row in packet["profiles"]] == PROFILES
    assert [row["cap"] for row in packet["profiles"]] == CAPS
    assert [row["odd_classes"] for row in packet["profiles"]] == ODD
    assert packet["cubic_cutoff"] == 13
    assert [row["moment"] for row in packet["cubic_boundary"]] == [13, 14]
    assert [row["certified_sign"] for row in packet["cubic_boundary"]] == [1, -1]
    assert {tuple(row["profile"]) for row in packet["parity_survivors"]} == SURVIVORS
    assert {key: len(value) for key, value in packet["survivors_by_odd_count"].items()} == {
        "1": 5, "3": 0, "5": 4,
    }
    assert packet["atlas_input"] == {
        "orbit_counts": {"1": 11, "3": 8, "5": 100},
        "support_counts": {"1": 264, "3": 960, "5": 14_400},
    }
    assert packet["relevant_affine_templates"] == 111
    assert packet["direct_vector_floor"] == 2_203_120_896
    assert packet["diameter_ledgers"] == [[1, -38], [5, -36], [9, -34], [17, -30], [21, -28]]

    checked = subprocess.run(
        [sys.executable, str(ROOT / pin["probe_checker_file"])],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    assert "E25_PROFILE_PARITY_PROBE_CHECK_PASS" in checked.stdout

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    incoming = {source for source, target, kind in edges if target == NODE and kind == "req"}
    assert incoming == DEPENDENCIES
    assert all(nodes[dependency]["status"] == "PROVED" for dependency in DEPENDENCIES)
    assert (NODE, "e1_n256_s16_e25_nine_profile_exclusion", "req") in edges
    assert (NODE, ENDPOINT, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "M_3=13" in nodes[NODE]["statement"]
    assert "2,203,120,896" in nodes[NODE]["statement"]
    print("E1_N256_S16_E25_PROFILE_PARITY_LIGHT_REDUCTION_PASS profiles=12 survivors=9 templates=111 floor=2203120896")


if __name__ == "__main__":
    main()
