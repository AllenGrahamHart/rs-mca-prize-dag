#!/usr/bin/env python3
"""Verify the complete negative one-loop 442 composition."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_"
    "complete_exclusion"
)
ATLAS_PATH = ROOT / (
    "critical/nodes/rate_half_band_closure/notes/"
    "kb_one_loop_442_common_atlas.py"
)
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_aligned_loop_q_exclusion",
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_crossed_pair_exclusion",
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_ab_s1_product_exclusion",
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_mixed_pair_exclusion",
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s0_forced_internal_guarded_product_exclusion",
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_opposite_pair_exclusion",
)
ORBITS = (
    (0,),
    (1, 2),
    (3, 6),
    (4, 5, 7, 8),
    (9, 10, 12, 13),
    (11, 14),
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("atlas", ATLAS_PATH)
    atlas = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(atlas)
    cells = atlas.cells()
    covered = [cell for orbit in ORBITS for cell in orbit]
    require(len(cells) == 15, "atlas cell count")
    require(len(covered) == len(set(covered)) == 15, "disjoint orbit cover")
    require(set(covered) == set(range(len(cells))), "complete orbit cover")

    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("KB41C-1" in statement and "no complete" in statement, "claim")
    require("does not treat" in statement and "nonclaim" in contract, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED", f"parent {parent}")
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print(
        "RATE_HALF_KB_ONE_LOOP_442_COMPLETE_PASS "
        "cells=15 orbits=6 uncovered=0 status=empty"
    )


if __name__ == "__main__":
    main()
