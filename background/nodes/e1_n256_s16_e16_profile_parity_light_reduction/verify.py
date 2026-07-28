#!/usr/bin/env python3
"""Verify the cutoff-free E16 profile/parity router."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
NODE = "e1_n256_s16_e16_profile_parity_light_reduction"
DEPENDENCIES = {
    "e1_n256_s16_e17_endpoint_exclusion",
    "e1_n256_s16_sparse_l1_variance_exclusion",
    "e1_n256_s16_signed_chord_collision_gate",
    "e1_n256_s16_e26_profile_parity_light_reduction",
    "collision_norm_criterion",
}
EXCLUSION = "e1_n256_s16_e16_four_profile_exclusion"
TARGETS = {"e1_official_prime_exception_control", "unsafe_crossing_family_instantiation"}
PROFILES = {
    (4, 3, 0, 0),
    (0, 4, 0, 0),
    (3, 1, 1, 0),
    (0, 0, 0, 1),
}


def main() -> None:
    pin = json.loads((HERE / "source_pin.json").read_text())
    for key, value in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / value).read_bytes()).hexdigest() == pin[
                key + "_sha256"
            ]
    packet = json.loads((ROOT / pin["probe_result_file"]).read_text())
    assert packet["complete"] and packet["variance"] == 32 and packet["energy"] == 16
    assert packet["l1_bound"] == 10 and packet["profile_count"] == 5
    assert packet["majorant_filter"] is None
    assert {tuple(row["profile"]) for row in packet["parity_survivors"]} == PROFILES
    assert len(packet["parity_rejected"]) == 1
    assert packet["relevant_affine_templates"] == 154
    assert packet["direct_vector_floor"] == 3_056_582_144
    run = subprocess.run(
        [sys.executable, str(ROOT / pin["probe_checker_file"])],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=30,
        check=True,
    )
    assert "l1=10 profiles=5 survivors=4 templates=154 floor=3056582144" in run.stdout
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert all(nodes[dependency]["status"] == "PROVED" for dependency in DEPENDENCIES)
    assert {source for source, target, kind in edges if target == NODE and kind == "req"} == DEPENDENCIES
    assert (NODE, EXCLUSION, "req") in edges
    assert all((NODE, target, "ev") in edges for target in TARGETS)
    print(
        "E1_N256_S16_E16_PROFILE_PARITY_LIGHT_REDUCTION_PASS "
        "l1=10 profiles=5 survivors=4 templates=154 floor=3056582144 mutations=1"
    )


if __name__ == "__main__":
    main()
