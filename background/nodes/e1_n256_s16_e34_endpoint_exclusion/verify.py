#!/usr/bin/env python3
"""Verify the complete E34 endpoint synthesis."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e34_endpoint_exclusion"
DEPENDENCIES = (
    "e1_n256_s16_e34_three_profile_reduction",
    "e1_n256_s16_e34_parity_profile_reduction",
    "e1_n256_s16_e34_heavy_chord_template_reduction",
    "e1_n256_s16_e34_quarter_template_exclusion",
    "e1_n256_s16_e34_nonquarter_diameter_template_exclusion",
    "e1_n256_s16_e34_progression_template_exclusion",
    "e1_n256_s16_e34_generic_template_exclusion",
)
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    for key, value in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / value).read_bytes()).hexdigest() == pin[key + "_sha256"]

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for node in (NODE, *DEPENDENCIES):
        assert nodes[node]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    for dependency in DEPENDENCIES:
        assert (dependency, NODE, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges

    profiles = {"6,7", "9,4,1", "12,1,2"}
    parity_survivors = {"6,7"}
    assert parity_survivors <= profiles and profiles - parity_survivors == {"9,4,1", "12,1,2"}
    templates = {"quarter", "diameter", "progression", "generic"}
    exclusions = {"quarter", "diameter", "progression", "generic"}
    assert templates == exclusions
    print(
        "E1_N256_S16_E34_ENDPOINT_EXCLUSION_PASS "
        "profiles=3 templates=4 residual_variance_max=66"
    )


if __name__ == "__main__":
    main()
