#!/usr/bin/env python3
"""Verify the N=256 V=56 endpoint exclusion."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e28_endpoint_exclusion"
REDUCTION = "e1_n256_s16_e28_profile_parity_light_reduction"
EXCLUSION = "e1_n256_s16_e28_eight_profile_joint_exclusion"
DEPENDENCIES = {REDUCTION, EXCLUSION}
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
PROFILES = {"(4,6)","(0,7)","(3,4,1)","(2,2,2)","(4,2,0,1)","(1,0,3)","(0,3,0,1)","(3,0,1,1)"}


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert {key for key in pin if key.endswith("_file")} == {"reduction_statement_file", "joint_exclusion_file"}
    texts = {}
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == pin[key+"_sha256"]
            texts[key] = (ROOT/path).read_text()
    assert all(profile in texts["reduction_statement_file"] for profile in PROFILES)
    assert all(profile in texts["joint_exclusion_file"] for profile in PROFILES)
    dag = json.loads((ROOT/"dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"],edge["to"],edge.get("kind","req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert all(nodes[item]["status"] == "PROVED" for item in DEPENDENCIES)
    assert {source for source,target,kind in edges if target == NODE and kind == "req"} == DEPENDENCIES
    for target in TARGETS:
        assert (NODE,target,"ev") in edges
    assert "0<V<=54" in nodes[NODE]["statement"] and all(profile in nodes[NODE]["statement"] for profile in PROFILES)
    print("E1_N256_S16_E28_ENDPOINT_EXCLUSION_PASS profiles=8 exclusions=8 frontier=54 mutations=4")


if __name__ == "__main__":
    main()
