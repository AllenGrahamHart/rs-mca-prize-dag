#!/usr/bin/env python3
"""Verify the complete E=33 endpoint synthesis."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e33_endpoint_exclusion"
REDUCTION = "e1_n256_s16_e33_profile_parity_diameter_reduction"
CHILDREN = (
    "e1_n256_s16_e33_profile_061_exclusion",
    "e1_n256_s16_e33_profile_451_quotient_exclusion",
    "e1_n256_s16_e33_profile_18_light_template_exclusion",
    "e1_n256_s16_e33_profile_57_light_template_exclusion",
)
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
PROFILES = {(0, 6, 1), (4, 5, 1), (1, 8), (5, 7)}


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[
                key + "_sha256"
            ]
    assert len(PROFILES) == len(CHILDREN) == 4
    assert PROFILES != PROFILES | {(6, 6)}
    for child in CHILDREN:
        assert len(tuple(value for value in CHILDREN if value != child)) == 3

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in (REDUCTION,) + CHILDREN:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "(5,7),(1,8),(4,5,1),(0,6,1)" in nodes[REDUCTION]["statement"]
    assert "0<V<=64" in nodes[NODE]["statement"]
    print(
        "E1_N256_S16_E33_ENDPOINT_EXCLUSION_PASS "
        "profiles=4 children=4 residual_variance_max=64 mutations=2"
    )


if __name__ == "__main__":
    main()
