#!/usr/bin/env python3
"""Verify the complete E24 six-profile exclusion."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
NODE = "e1_n256_s16_e24_six_profile_exclusion"
DEPENDENCIES = {
    "e1_n256_s16_e24_profile_parity_light_reduction",
    "e1_n256_proper_conductor_collision_exclusion",
    "collision_norm_criterion",
}
TARGETS = {"e1_official_prime_exception_control", "unsafe_crossing_family_instantiation"}
MAXIMUM = 934000596876556404040131946795508791323292938762264172037712523409677324304


def main() -> None:
    pin = json.loads((HERE / "source_pin.json").read_text())
    for key, value in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / value).read_bytes()).hexdigest() == pin[key+"_sha256"]

    count = json.loads((ROOT / pin["count_result_file"]).read_text())
    collect = json.loads((ROOT / pin["collect_result_file"]).read_text())
    norm = json.loads((ROOT / pin["norm_result_file"]).read_text())
    assert count["complete"] is True and collect["complete"] is True
    assert count["summary"]["profile_counts"] == [10878, 0, 2780, 306, 452, 0]
    assert count["summary"]["full_conductor_counts"] == [5870, 0, 836, 30, 98, 0]
    assert count["summary"]["proper_conductor_counts"] == [5008, 0, 1944, 276, 354, 0]
    assert collect["summary"]["collected_full_conductor"] == 6834
    assert norm["complete"] is True and norm["agreement"] is True
    assert norm["summary"] == {
        "distinct_norms": 2684,
        "maximizing_indices": [4086, 4087, 4176, 4177],
        "maximum_norm": MAXIMUM,
        "maximum_norm_bits": 250,
        "norm_at_or_above_2_250": 0,
        "vectors": 6834,
    }
    assert MAXIMUM < 2**250 < 2*MAXIMUM

    markers = (
        (pin["count_checker_file"], "profile=14416 full=6834 engines=2 mutations=1"),
        (pin["collect_checker_file"], "profile=14416 full=6834 engines=2 mutations=1"),
        (pin["norm_checker_file"], f"vectors=6834 distinct=2684 max={MAXIMUM} bits=250 hits=0 engines=2 mutations=2"),
    )
    for path, marker in markers:
        completed = subprocess.run(
            [sys.executable, str(ROOT / path)], cwd=ROOT, capture_output=True,
            text=True, timeout=30, check=True,
        )
        assert marker in completed.stdout

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert all(nodes[dependency]["status"] == "PROVED" for dependency in DEPENDENCIES)
    incoming = {source for source, target, kind in edges if target == NODE and kind == "req"}
    assert incoming == DEPENDENCIES
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    print("E1_N256_S16_E24_SIX_PROFILE_EXCLUSION_PASS templates=154 vectors=3056582144 profile=14416 full=6834 distinct=2684 max_bits=250 engines=4 mutations=4")


if __name__ == "__main__":
    main()
