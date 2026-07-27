#!/usr/bin/env python3
"""Verify the N=256 square-mass-16 V=50 endpoint exclusion."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e25_endpoint_exclusion"
REDUCTION = "e1_n256_s16_e25_profile_parity_light_reduction"
EXCLUSION = "e1_n256_s16_e25_nine_profile_exclusion"
DEPENDENCIES = {REDUCTION, EXCLUSION}
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
PROFILES = {
    "(5,5)", "(1,6)", "(4,3,1)", "(0,4,1)", "(3,1,2)",
    "(5,1,0,1)", "(1,2,0,1)", "(0,0,1,1)", "(0,0,0,0,1)",
}


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert {key for key in pin if key.endswith("_file")} == {
        "reduction_statement_file", "joint_exclusion_file"
    }
    texts: dict[str, str] = {}
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]
            texts[key] = (ROOT / path).read_text()
    assert all(profile in texts["reduction_statement_file"] for profile in PROFILES)
    assert all(profile in texts["joint_exclusion_file"] for profile in PROFILES)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert all(nodes[dependency]["status"] == "PROVED" for dependency in DEPENDENCIES)
    incoming = {source for source, target, kind in edges if target == NODE and kind == "req"}
    assert incoming == DEPENDENCIES
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "0<V<=48" in nodes[NODE]["statement"]
    assert all(profile in nodes[NODE]["statement"] for profile in PROFILES)
    print("E1_N256_S16_E25_ENDPOINT_EXCLUSION_PASS profiles=9 exclusions=9 frontier=48 mutations=4")


if __name__ == "__main__":
    main()
