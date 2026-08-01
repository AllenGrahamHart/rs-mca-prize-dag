#!/usr/bin/env python3
"""Verify the positive residual loop workboard."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_positive_residual_loop_workboard"
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_residual_loop_workboard.py"
)
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_loop_ramification_gate",
    "rate_half_kb_m2_r4_coordinate_positive_ramified_loop_multiplicity_exclusion",
    "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("workboard", SCRIPT)
    workboard = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(workboard)
    common_rows, outside, routed = workboard.verify()
    live = [row for row in common_rows if row["reason"] == "live"]
    require(len(common_rows) == 10 and len(live) == 5, "common orbit counts")
    require(sum(row["orbit_size"] for row in live) == 7, "labeled common count")
    require(tuple(len(outside[h][1]) for h in (0, 1)) == (2, 4),
            "outside orbit counts")
    require(sum(len(routes) for _, routes in routed) == 13, "route count")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    statement = (NODE / "statement.md").read_text()
    require("thirteen representative route records remain" in statement,
            "route claim")
    require("does not assert that any route is" in statement, "scope fence")
    print(
        "RATE_HALF_KB_POSITIVE_RESIDUAL_LOOP_WORKBOARD_VERIFY_PASS "
        "common=10/5 labeled=7 outside_orbits=2,4 routes=13"
    )


if __name__ == "__main__":
    main()
