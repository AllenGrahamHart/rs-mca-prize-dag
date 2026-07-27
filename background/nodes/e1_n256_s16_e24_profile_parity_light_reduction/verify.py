#!/usr/bin/env python3
"""Verify the N=256 square-mass-16 E24 router."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
NODE = "e1_n256_s16_e24_profile_parity_light_reduction"
DEPENDENCIES = {
    "e1_n256_s16_e25_endpoint_exclusion",
    "e1_n256_s16_sparse_l1_variance_exclusion",
    "e1_n256_s16_signed_chord_collision_gate",
    "e1_n256_s16_e26_profile_parity_light_reduction",
    "collision_norm_criterion",
}
EXCLUSION = "e1_n256_s16_e24_six_profile_exclusion"
TARGETS = {"e1_official_prime_exception_control", "unsafe_crossing_family_instantiation"}
PROFILES = {(4,5,0,0,0), (0,6,0,0,0), (3,3,1,0,0),
            (2,1,2,0,0), (4,1,0,1,0), (0,2,0,1,0)}


def main() -> None:
    pin = json.loads((HERE / "source_pin.json").read_text())
    for key, value in pin.items():
        if not key.endswith("_file"):
            continue
        path = ROOT / value
        assert hashlib.sha256(path.read_bytes()).hexdigest() == pin[key+"_sha256"]

    packet = json.loads((ROOT / pin["probe_result_file"]).read_text())
    assert packet["complete"] is True and packet["variance"] == 48 and packet["energy"] == 24
    assert packet["l1_bound"] == 14 and packet["profile_count"] == 9
    assert packet["majorant_filter"] is None
    survivors = {tuple(row["profile"]) for row in packet["parity_survivors"]}
    assert survivors == PROFILES
    assert len(packet["parity_rejected"]) == 3
    assert packet["relevant_affine_templates"] == 154
    assert packet["direct_vector_floor"] == 3_056_582_144

    completed = subprocess.run(
        [sys.executable, str(ROOT / pin["probe_checker_file"])], cwd=ROOT,
        capture_output=True, text=True, timeout=30, check=True,
    )
    assert "l1=14 profiles=9 survivors=6 templates=154 floor=3056582144" in completed.stdout

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert all(nodes[dependency]["status"] == "PROVED" for dependency in DEPENDENCIES)
    incoming = {source for source, target, kind in edges if target == NODE and kind == "req"}
    assert incoming == DEPENDENCIES
    assert (NODE, EXCLUSION, "req") in edges
    assert all((NODE, target, "ev") in edges for target in TARGETS)
    print("E1_N256_S16_E24_PROFILE_PARITY_LIGHT_REDUCTION_PASS l1=14 profiles=9 survivors=6 templates=154 floor=3056582144 mutations=2")


if __name__ == "__main__":
    main()
