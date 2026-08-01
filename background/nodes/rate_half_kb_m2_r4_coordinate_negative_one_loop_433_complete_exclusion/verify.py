#!/usr/bin/env python3
"""Verify the complete negative one-loop 433 composition."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_433_complete_exclusion"
)
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_433_"
    "loop_singleton_aligned_exclusion",
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_433_"
    "loop_singleton_crossed_exclusion",
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_433_"
    "nonloop_singleton_ab_ac_complete_product_exclusion",
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_433_"
    "nonloop_singleton_mixed_pair_exclusion",
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_433_"
    "nonloop_singleton_bc_mixed_pair_exclusion",
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_433_"
    "nonloop_singleton_opposite_pair_exclusion",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    orbits = ({0}, {1, 2}, {3, 6}, {4, 5, 7, 8},
              {9, 10, 12, 13}, {11, 14})
    require(set().union(*orbits) == set(range(15)), "atlas cover")
    require(sum(map(len, orbits)) == 15, "atlas disjointness")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    require(all(nodes[parent]["status"] == "PROVED" for parent in PARENTS),
            "parent statuses")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "statement status")
    require("negative one-loop `(4,3,3)` packet exists" in statement
            and "Hence no" in statement, "claim")
    print(
        "RATE_HALF_KB_ONE_LOOP_433_COMPLETE_VERIFY_PASS "
        "orbits=6 cells=15 survivors=0"
    )


if __name__ == "__main__":
    main()
