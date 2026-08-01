#!/usr/bin/env python3
"""Verify the positive three-loop outside-edge eliminant compiler."""

import importlib.util
import json
import os
import subprocess
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_positive_three_loop_outside_edge_eliminant_compiler"
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_three_loop_outside_edge_eliminant.py"
)
PROBE = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_three_loop_small_prime_probe.py"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("eliminant", SCRIPT)
    eliminant = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(eliminant)
    result = eliminant.verify()
    require(result == {
        "generic_terms": 22,
        "generic_total_degree": 6,
        "linear_total_degree": 5,
    }, "eliminant shape")

    environment = dict(os.environ)
    environment.update(KB_PROBE_PRIME="13", KB_PROBE_SECONDS="10")
    replay = subprocess.run(
        ["python3", str(PROBE)],
        check=True,
        capture_output=True,
        text=True,
        env=environment,
        timeout=15,
    )
    require("prime=13 timed_out=0 survivors=0" in replay.stdout,
            "F13 route replay")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    for parent in (
        "rate_half_kb_m2_r4_coordinate_positive_three_loop_signed_outside_vieta_atlas",
        "rate_half_kb_m2_r4_coordinate_positive_three_loop_common_kernel_compiler",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    statement = (NODE / "statement.md").read_text()
    require("degree-drop branch is genuine" in statement, "branch claim")
    require("does not make a bare" in statement, "scope fence")
    print(
        "RATE_HALF_KB_POSITIVE_THREE_LOOP_EDGE_ELIMINANT_VERIFY_PASS "
        "generic_terms=22 generic_degree=6 linear_degree=5 f13_survivors=0"
    )


if __name__ == "__main__":
    main()
