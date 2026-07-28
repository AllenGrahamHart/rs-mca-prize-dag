#!/usr/bin/env python3
"""Verify the cutoff-free E17 profile/parity router."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
NODE = "e1_n256_s16_e17_profile_parity_light_reduction"
DEPENDENCIES = {
    "e1_n256_s16_e18_endpoint_exclusion",
    "e1_n256_s16_sparse_l1_variance_exclusion",
    "e1_n256_s16_signed_chord_collision_gate",
    "e1_n256_s16_e27_profile_parity_light_reduction",
    "collision_norm_criterion",
}
EXCLUSION = "e1_n256_s16_e17_five_profile_exclusion"
TARGETS = {"e1_official_prime_exception_control", "unsafe_crossing_family_instantiation"}
PROFILES = {
    (5, 3, 0, 0),
    (1, 4, 0, 0),
    (4, 1, 1, 0),
    (0, 2, 1, 0),
    (1, 0, 0, 1),
}


def main() -> None:
    pin = json.loads((HERE / "source_pin.json").read_text())
    for key, value in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / value).read_bytes()).hexdigest() == pin[
                key + "_sha256"
            ]
    packet = json.loads((ROOT / pin["probe_result_file"]).read_text())
    assert packet["complete"] and packet["variance"] == 34 and packet["energy"] == 17
    assert packet["l1_bound"] == 11 and packet["profile_count"] == 6
    assert packet["majorant_filter"] is None
    assert {tuple(row["profile"]) for row in packet["parity_survivors"]} == PROFILES
    assert len(packet["parity_rejected"]) == 1
    assert packet["relevant_affine_templates"] == 111
    assert packet["direct_vector_floor"] == 2_203_120_896
    run = subprocess.run(
        [sys.executable, str(ROOT / pin["probe_checker_file"])],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=30,
        check=True,
    )
    assert "l1=11 profiles=6 survivors=5 templates=111 floor=2203120896" in run.stdout
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert all(nodes[dependency]["status"] == "PROVED" for dependency in DEPENDENCIES)
    assert {source for source, target, kind in edges if target == NODE and kind == "req"} == DEPENDENCIES
    assert (NODE, EXCLUSION, "req") in edges
    assert all((NODE, target, "ev") in edges for target in TARGETS)
    print(
        "E1_N256_S16_E17_PROFILE_PARITY_LIGHT_REDUCTION_PASS "
        "l1=11 profiles=6 survivors=5 templates=111 floor=2203120896 mutations=1"
    )


if __name__ == "__main__":
    main()
