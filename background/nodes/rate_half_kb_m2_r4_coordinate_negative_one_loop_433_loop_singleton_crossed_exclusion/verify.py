#!/usr/bin/env python3
"""Verify the one-loop 433 crossed loop-singleton exclusion."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_433_"
    "loop_singleton_crossed_exclusion"
)
ROUTER = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_one_loop_433_cell12_q_router.py"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("router", ROUTER)
    router = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(router)
    router.verify()

    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("KB431X-2" in statement and "Cells `1,2` are empty" in statement,
            "claim")
    require("does not delete" in statement and "nonclaim" in contract,
            "scope")

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
        "RATE_HALF_KB_ONE_LOOP_433_CROSSED_VERIFY_PASS "
        "cells=1,2 sign_rows=8 q_survivors=0"
    )


if __name__ == "__main__":
    main()
