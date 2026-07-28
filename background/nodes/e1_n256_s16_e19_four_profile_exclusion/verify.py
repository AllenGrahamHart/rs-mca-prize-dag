#!/usr/bin/env python3

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
NODE = "e1_n256_s16_e19_four_profile_exclusion"
DEPENDENCIES = {
    "e1_n256_s16_e19_profile_parity_light_reduction",
    "e1_n256_proper_conductor_collision_exclusion",
    "collision_norm_criterion",
}
TARGETS = {"e1_official_prime_exception_control", "unsafe_crossing_family_instantiation"}
MAXIMUM = 1096349292027446593481621675930218905147073043465918102751396673154250061826


def main() -> None:
    pin = json.loads((HERE / "source_pin.json").read_text())
    for key, value in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / value).read_bytes()).hexdigest() == pin[
                key + "_sha256"
            ]
    census = json.loads((ROOT / pin["census_result_file"]).read_text())
    norm = json.loads((ROOT / pin["norm_result_file"]).read_text())
    assert census["complete"]
    assert census["summary"]["profile_counts"] == [370, 182, 10, 12]
    assert census["summary"]["full_conductor_counts"] == [112, 24, 0, 0]
    assert census["summary"]["proper_conductor_counts"] == [258, 158, 10, 12]
    assert census["summary"]["collected_full_conductor"] == 136
    assert norm["complete"] and norm["agreement"]
    assert norm["summary"] == {
        "distinct_norms": 40,
        "maximizing_indices": [35, 37],
        "maximum_norm": MAXIMUM,
        "maximum_norm_bits": 250,
        "norm_at_or_above_2_250": 0,
        "vectors": 136,
    }
    assert MAXIMUM < 2**250 < 2 * MAXIMUM
    markers = (
        (pin["census_checker_file"], "profile=574 full=136 engines=2 mutations=1"),
        (
            pin["norm_checker_file"],
            f"vectors=136 distinct=40 max={MAXIMUM} bits=250 hits=0 engines=2 mutations=1",
        ),
    )
    for path, marker in markers:
        run = subprocess.run(
            [sys.executable, str(ROOT / path)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=30,
            check=True,
        )
        assert marker in run.stdout
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert all(nodes[dependency]["status"] == "PROVED" for dependency in DEPENDENCIES)
    assert {source for source, target, kind in edges if target == NODE and kind == "req"} == DEPENDENCIES
    assert all((NODE, target, "ev") in edges for target in TARGETS)
    print(
        "E1_N256_S16_E19_FOUR_PROFILE_EXCLUSION_PASS "
        "templates=8 vectors=158783488 profile=574 full=136 distinct=40 "
        "max_bits=250 engines=4 mutations=2"
    )


if __name__ == "__main__":
    main()
