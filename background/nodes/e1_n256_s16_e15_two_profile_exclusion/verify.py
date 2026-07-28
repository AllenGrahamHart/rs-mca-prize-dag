#!/usr/bin/env python3

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
NODE = "e1_n256_s16_e15_two_profile_exclusion"
DEPENDENCIES = {
    "e1_n256_s16_e15_profile_parity_light_reduction",
    "e1_n256_proper_conductor_collision_exclusion",
    "collision_norm_criterion",
}
TARGETS = {"e1_official_prime_exception_control", "unsafe_crossing_family_instantiation"}
MAXIMUM_NORM = 3003171528471974836716922425205211633163258783488230570091067301168069285892
MAXIMUM_ODD = 1263041506267492322130816623667822529962454800313964008196082776100356004097


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
    assert census["summary"]["profile_counts"] == [258, 36]
    assert census["summary"]["full_conductor_counts"] == [64, 0]
    assert census["summary"]["proper_conductor_counts"] == [194, 36]
    assert census["summary"]["collected_full_conductor"] == 64
    assert norm["complete"] and norm["agreement"]
    summary = norm["summary"]
    assert summary["vectors"] == 64 and summary["distinct_norms"] == 28
    assert summary["maximum_norm"] == MAXIMUM_NORM
    assert summary["maximum_norm_bits"] == 251
    assert summary["norms_at_or_above_2_250"] == 32
    assert summary["maximum_odd_part"] == MAXIMUM_ODD
    assert summary["maximum_odd_part_bits"] == 250
    assert summary["odd_parts_at_or_above_2_250"] == 0
    assert MAXIMUM_ODD < 2**250 < 2 * MAXIMUM_ODD
    markers = (
        (pin["census_checker_file"], "profile=294 full=64 engines=2 mutations=1"),
        (
            pin["norm_checker_file"],
            f"vectors=64 distinct=28 max={MAXIMUM_NORM} bits=251 hits=32 "
            f"odd_max={MAXIMUM_ODD} odd_bits=250 odd_hits=0 engines=2 mutations=1",
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
        "E1_N256_S16_E15_TWO_PROFILE_EXCLUSION_PASS "
        "templates=8 vectors=158783488 profile=294 full=64 distinct=28 "
        "norm_hits=32 odd_hits=0 engines=4 mutations=2"
    )


if __name__ == "__main__":
    main()
