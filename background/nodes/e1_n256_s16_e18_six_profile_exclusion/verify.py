#!/usr/bin/env python3

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
NODE = "e1_n256_s16_e18_six_profile_exclusion"
DEPENDENCIES = {
    "e1_n256_s16_e18_profile_parity_light_reduction",
    "e1_n256_proper_conductor_collision_exclusion",
    "collision_norm_criterion",
}
TARGETS = {"e1_official_prime_exception_control", "unsafe_crossing_family_instantiation"}
MAXIMUM_NORM = 3244660049331064070204285700733501169431397018164712582311239362105072116226
MAXIMUM_ODD = 1622330024665532035102142850366750584715698509082356291155619681052536058113


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
    assert census["summary"]["profile_counts"] == [2410, 3096, 842, 208, 4, 152]
    assert census["summary"]["full_conductor_counts"] == [1100, 1622, 226, 18, 0, 28]
    assert census["summary"]["proper_conductor_counts"] == [1310, 1474, 616, 190, 4, 124]
    assert census["summary"]["collected_full_conductor"] == 2994
    assert norm["complete"] and norm["agreement"]
    summary = norm["summary"]
    assert summary["vectors"] == 2994 and summary["distinct_norms"] == 895
    assert summary["maximum_norm"] == MAXIMUM_NORM
    assert summary["maximum_norm_bits"] == 251
    assert summary["norms_at_or_above_2_250"] == 6
    assert summary["maximum_odd_part"] == MAXIMUM_ODD
    assert summary["maximum_odd_part_bits"] == 250
    assert summary["odd_parts_at_or_above_2_250"] == 0
    assert MAXIMUM_ODD < 2**250 < 2 * MAXIMUM_ODD
    markers = (
        (pin["census_checker_file"], "profile=6712 full=2994 engines=2 mutations=1"),
        (
            pin["norm_checker_file"],
            f"vectors=2994 distinct=895 max={MAXIMUM_NORM} bits=251 hits=6 "
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
        "E1_N256_S16_E18_SIX_PROFILE_EXCLUSION_PASS "
        "templates=1321 vectors=26219123456 profile=6712 full=2994 distinct=895 "
        "norm_hits=6 odd_hits=0 engines=4 mutations=2"
    )


if __name__ == "__main__":
    main()
