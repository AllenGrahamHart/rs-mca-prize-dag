#!/usr/bin/env python3
"""Verify the N=256 square-mass-16 V=60 endpoint exclusion."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e30_endpoint_exclusion"
REDUCTION = "e1_n256_s16_e30_profile_parity_light_reduction"
DEPENDENCIES = {
    REDUCTION,
    "e1_n256_s16_e30_three_profile_quotient_exclusion",
    "e1_n256_s16_e30_two_odd_profile_exclusion",
    "e1_n256_s16_e30_profile_422_exclusion",
    "e1_n256_s16_e30_profile_541_exclusion",
    "e1_n256_s16_e30_profile_66_exclusion",
}
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
PROFILES = {
    "(6,6)", "(2,7)", "(5,4,1)", "(1,5,1)",
    "(4,2,2)", "(0,3,2)", "(6,2,0,1)", "(3,0,3)",
}


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    texts: dict[str, str] = {}
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]
            texts[key] = (ROOT / path).read_text()
    assert all(profile in texts["profile_reduction_file"] for profile in PROFILES)

    groups = [
        ({"(0,3,2)", "(6,2,0,1)", "(3,0,3)"}, texts["quotient_exclusion_file"]),
        ({"(2,7)", "(1,5,1)"}, texts["two_odd_exclusion_file"]),
        ({"(4,2,2)"}, texts["profile_422_file"]),
        ({"(5,4,1)"}, texts["profile_541_file"]),
        ({"(6,6)"}, texts["profile_66_file"]),
    ]
    covered: list[str] = []
    for profiles, text in groups:
        assert all(profile in text for profile in profiles)
        covered.extend(profiles)
    assert set(covered) == PROFILES and len(covered) == len(PROFILES)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert all(nodes[dependency]["status"] == "PROVED" for dependency in DEPENDENCIES)
    incoming = {source for source, target, kind in edges if target == NODE and kind == "req"}
    assert incoming == DEPENDENCIES
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "0<V<=58" in nodes[NODE]["statement"]
    assert all(profile in nodes[NODE]["statement"] for profile in PROFILES)

    print("E1_N256_S16_E30_ENDPOINT_EXCLUSION_PASS profiles=8 exclusions=8 frontier=58 mutations=3")


if __name__ == "__main__":
    main()
