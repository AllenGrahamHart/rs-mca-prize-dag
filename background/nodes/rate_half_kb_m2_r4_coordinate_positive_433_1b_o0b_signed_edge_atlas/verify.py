#!/usr/bin/env python3
"""Verify the positive 433-1b/O0b signed-edge atlas."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_signed_edge_atlas"
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1b_o0b_signed_edge_atlas.py"
)
SCRIPT_HASH = "1caaddce72bc76e142c9f720298932cffb426ccc66c4333c6d7a3c5d4218ea7f"
PARENTS = {
    "rate_half_kb_m2_r4_coordinate_positive_residual_loop_workboard",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
}
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_atlas():
    require(hashlib.sha256(SCRIPT.read_bytes()).hexdigest() == SCRIPT_HASH,
            "script custody")
    spec = importlib.util.spec_from_file_location("positive_433_1b_o0b", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    atlas = load_atlas()
    atlases, lanes, defects = atlas.verify()
    require({key: len(value) for key, value in atlases.items()} == {
        "S0": 2, "SBC": 4, "SDE": 2, "SDF": 2,
    }, "stratum orbit census")
    require(sum(sum(row[2] for row in value) for value in atlases.values()) == 224,
            "raw sign census")
    require(len(lanes) == 10 and all(len(rows) == 12 for rows in lanes.values()),
            "lane census")
    require({key: value["total"] for key, value in defects.items()} == {
        "S0": 1, "SBC": 3, "SDE": 3, "SDF": 3,
    }, "defect census")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED", f"parent {parent}")
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer evidence edge")
    statement = (NODE / "statement.md").read_text()
    require("224 active-sign assignments" in statement and
            "exactly ten target-gauge lanes" in statement,
            "statement census")
    require("does not assign source labels" in statement.lower(), "scope fence")
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_SIGNED_EDGE_ATLAS_VERIFY_PASS "
        "raw=224 strata=4 orbits=10 lanes=10 rows=12 defects=1,3,3,3"
    )


if __name__ == "__main__":
    main()
