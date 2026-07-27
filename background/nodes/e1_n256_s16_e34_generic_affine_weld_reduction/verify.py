#!/usr/bin/env python3
"""Verify the E34 generic affine-weld reduction."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e34_generic_affine_weld_reduction"
HEAVY = "e1_n256_s16_e34_heavy_chord_template_reduction"
PARITY = "e1_n256_s16_e34_parity_profile_reduction"
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    for key, value in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / value).read_bytes()).hexdigest() == pin[key + "_sha256"]

    checker = subprocess.run(
        ["python3", str(ROOT / pin["checker_file"])],
        capture_output=True,
        check=True,
        text=True,
        timeout=20,
    )
    assert checker.stdout.strip() == (
        "E1_E34_GENERIC_ORBIT_CHECK_PASS "
        "orbits=57 triples=325376 census_vectors=243285056"
    )

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for node in (NODE, HEAVY, PARITY):
        assert nodes[node]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    for dependency in (HEAVY, PARITY):
        assert (dependency, NODE, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges

    print(
        "E1_N256_S16_E34_GENERIC_AFFINE_WELD_REDUCTION_PASS "
        "orbits=57 triples=325376 census_vectors=243285056"
    )


if __name__ == "__main__":
    main()
