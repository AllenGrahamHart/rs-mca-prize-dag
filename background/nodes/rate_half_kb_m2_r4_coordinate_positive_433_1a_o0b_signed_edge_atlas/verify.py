#!/usr/bin/env python3
"""Verify the positive 433-1a/O0b signed-edge atlas."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_positive_433_1a_o0b_signed_edge_atlas"
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1a_o0b_signed_edge_atlas.py"
)
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_residual_loop_workboard",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("atlas", SCRIPT)
    atlas = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(atlas)
    orbits, lanes, defect = atlas.verify()
    require(len(orbits) == 2, "sign orbit count")
    require(tuple(row[2] for row in orbits) == (16, 16), "orbit sizes")
    require(set(lanes) == {-1, 1}, "cycle lanes")
    require(all(len(rows) == 12 for rows in lanes.values()), "row counts")
    require(defect["total"] == 3, "defect saturation")

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
    require("exactly two signed lanes" in statement, "claim")
    require("does not assign source fibers" in statement, "scope fence")
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_O0B_SIGNED_EDGE_ATLAS_VERIFY_PASS "
        "raw=32 orbits=2 sizes=16,16 lanes=2 rows=12 defect=3"
    )


if __name__ == "__main__":
    main()
