#!/usr/bin/env python3
"""Verify the aligned one-loop 442 loop-q exclusion."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_"
    "aligned_loop_q_exclusion"
)
EXPERIMENT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_one_loop_442_aligned_loop_q_exclusion.py"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location(
        "aligned_loop_q", EXPERIMENT
    )
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    module.verify()

    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("KB41Q-2" in statement and "KB41Q-3" in statement, "claim")
    require("does not by itself" in statement and "nonclaim" in contract,
            "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    parents = (
        "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_aligned_pair_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_aligned_outside_product_router",
    )
    for parent in parents:
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print(
        "RATE_HALF_KB_ONE_LOOP_442_ALIGNED_LOOP_Q_VERIFY_PASS "
        "families=2 branches=S1-DE,S1-DF,S2 survivors=0"
    )


if __name__ == "__main__":
    main()
