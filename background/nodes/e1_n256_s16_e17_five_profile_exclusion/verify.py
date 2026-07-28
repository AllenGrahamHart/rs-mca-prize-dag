#!/usr/bin/env python3

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
NODE = "e1_n256_s16_e17_five_profile_exclusion"
DEPENDENCIES = {
    "e1_n256_s16_e17_profile_parity_light_reduction",
    "e1_n256_proper_conductor_collision_exclusion",
    "collision_norm_criterion",
}
TARGETS = {"e1_official_prime_exception_control", "unsafe_crossing_family_instantiation"}
MAXIMUM_NORM = 2816861446662266258222239103326104068711609833031798890850684996153986296836
MAXIMUM_ODD = 744372174442013450465816409476894770650462784978029532566873973061928116737


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
    assert census["summary"]["profile_counts"] == [608, 1152, 188, 92, 10]
    assert census["summary"]["full_conductor_counts"] == [196, 272, 20, 0, 0]
    assert census["summary"]["proper_conductor_counts"] == [412, 880, 168, 92, 10]
    assert census["summary"]["collected_full_conductor"] == 488
    assert norm["complete"] and norm["agreement"]
    summary = norm["summary"]
    assert summary["vectors"] == 488 and summary["distinct_norms"] == 108
    assert summary["maximum_norm"] == MAXIMUM_NORM
    assert summary["maximum_norm_bits"] == 251
    assert summary["norms_at_or_above_2_250"] == 16
    assert summary["maximum_odd_part"] == MAXIMUM_ODD
    assert summary["maximum_odd_part_bits"] == 249
    assert summary["odd_parts_at_or_above_2_250"] == 0
    assert 2 * MAXIMUM_ODD < 2**250 < 3 * MAXIMUM_ODD
    markers = (
        (pin["census_checker_file"], "profile=2050 full=488 engines=2 mutations=1"),
        (
            pin["norm_checker_file"],
            f"vectors=488 distinct=108 max={MAXIMUM_NORM} bits=251 hits=16 "
            f"odd_max={MAXIMUM_ODD} odd_bits=249 odd_hits=0 engines=2 mutations=1",
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
        "E1_N256_S16_E17_FIVE_PROFILE_EXCLUSION_PASS "
        "templates=111 vectors=2203120896 profile=2050 full=488 distinct=108 "
        "norm_hits=16 odd_hits=0 engines=4 mutations=2"
    )


if __name__ == "__main__":
    main()
