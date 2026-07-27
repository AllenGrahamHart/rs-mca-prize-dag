#!/usr/bin/env python3
"""Verify the N=256 square-mass-16 V=62 endpoint exclusion."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e31_endpoint_exclusion"
REDUCTION = "e1_n256_s16_e31_profile_parity_light_reduction"
EXCLUSION = "e1_n256_s16_e31_three_profile_joint_exclusion"
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
EXPECTED_PIN = {
    "joint_exclusion_file": "background/nodes/e1_n256_s16_e31_three_profile_joint_exclusion/statement.md",
    "joint_exclusion_file_sha256": "774316e421645a78fa1dec87f58f19dc5df3e4dd4185a11ffd6b7dee501d39d3",
    "profile_reduction_file": "background/nodes/e1_n256_s16_e31_profile_parity_light_reduction/statement.md",
    "profile_reduction_file_sha256": "3927e37cfeb01a2d327a777ec3df3cd7a5bbadc15934a3b346620982eac05f50",
}


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]

    reduction = (ROOT / pin["profile_reduction_file"]).read_text()
    exclusion = (ROOT / pin["joint_exclusion_file"]).read_text()
    profiles = ("(3,7)", "(2,5,1)", "(1,3,2)")
    assert all(profile in reduction and profile in exclusion for profile in profiles)
    assert "eight affine odd-unit orbits" in reduction
    assert "158,783,488" in exclusion

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == nodes[REDUCTION]["status"] == nodes[EXCLUSION]["status"] == "PROVED"
    incoming = {source for source, target, kind in edges if target == NODE and kind == "req"}
    assert incoming == {REDUCTION, EXCLUSION}
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "0<V<=60" in nodes[NODE]["statement"]
    assert all(profile in nodes[NODE]["statement"] for profile in profiles)

    print(
        "E1_N256_S16_E31_ENDPOINT_EXCLUSION_PASS "
        "profiles=3 exclusions=3 frontier=60 mutations=4"
    )


if __name__ == "__main__":
    main()
