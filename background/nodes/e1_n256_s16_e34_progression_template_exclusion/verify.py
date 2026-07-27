#!/usr/bin/env python3
"""Verify the E34 progression-template exclusion packet."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e34_progression_template_exclusion"
PROGRESSION = "e1_n256_s16_e34_progression_weld_reduction"
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
    expected = (
        "E1_E34_PROGRESSION_CENSUS_CHECK_PASS "
        "representative_totals={'supports': 5979825, 'vectors': 191354400, "
        "'energy_34': 603832, 'profile_67': 404212, 'full_conductor': 329776} "
        "weighted_totals={'supports': 74149830, 'vectors': 2372794560, "
        "'energy_34': 5768472, 'profile_67': 3618496, 'full_conductor': 3131008} "
        "maximum_m3=1722"
    )
    assert checker.stdout.strip() == expected
    assert 1722 < 1947

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for node in (NODE, PROGRESSION, CONDUCTOR, E34, NORM):
        assert nodes[node]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    for dependency in (PROGRESSION, CONDUCTOR, E34, NORM):
        assert (dependency, NODE, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges

    print(
        "E1_N256_S16_E34_PROGRESSION_TEMPLATE_EXCLUSION_PASS "
        "representative_vectors=191354400 weighted_full=3131008 "
        "m3=1722 threshold=1947"
    )


if __name__ == "__main__":
    main()
