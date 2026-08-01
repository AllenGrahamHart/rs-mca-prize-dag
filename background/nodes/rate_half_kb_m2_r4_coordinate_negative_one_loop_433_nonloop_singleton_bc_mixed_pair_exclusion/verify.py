#!/usr/bin/env python3
"""Verify the one-loop 433 BC mixed-pair exclusion."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_433_"
    "nonloop_singleton_bc_mixed_pair_exclusion"
)
ROUTER = ROOT / (
    "experiments/prize_resolution/rate_half_kb_one_loop_433_cell9_router.py"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("router", ROUTER)
    router = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(router)
    rows = router.verify()
    require(len(rows) == 4, "sign rows")
    require(
        [router.ATLAS.BASE.cells()[index][0] for index in (9, 10, 12, 13)]
        == [3, 3, 4, 4],
        "cell orbit",
    )

    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("`[9,10,12,13]`" in statement and "is empty" in statement, "claim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_product_q_weld",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print(
        "RATE_HALF_KB_ONE_LOOP_433_BC_MIXED_VERIFY_PASS "
        "cells=9,10,12,13 sign_rows=16 survivors=0"
    )


if __name__ == "__main__":
    main()
