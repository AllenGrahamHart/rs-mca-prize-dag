#!/usr/bin/env python3
"""Verify the E34 generic-template exclusion packet."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e34_generic_template_exclusion"
GENERIC = "e1_n256_s16_e34_generic_affine_weld_reduction"
CONDUCTOR = "e1_n256_proper_conductor_collision_exclusion"
E34 = "e1_n256_s16_e34_three_profile_reduction"
NORM = "collision_norm_criterion"
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
        "E1_E34_GENERIC_CENSUS_CHECK_PASS "
        "totals={'supports': 3801329, 'vectors': 243285056, "
        "'energy_34': 793742, 'profile_67': 505466, "
        "'full_conductor': 418464} maximum_m3=1770"
    )
    assert 1770 < 1947

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for node in (NODE, GENERIC, CONDUCTOR, E34, NORM):
        assert nodes[node]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    for dependency in (GENERIC, CONDUCTOR, E34, NORM):
        assert (dependency, NODE, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges

    print(
        "E1_N256_S16_E34_GENERIC_TEMPLATE_EXCLUSION_PASS "
        "vectors=243285056 full=418464 m3=1770 threshold=1947"
    )


if __name__ == "__main__":
    main()
