#!/usr/bin/env python3
"""Verify the positive loop-ramification gate and ten-orbit census."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_positive_loop_ramification_gate"
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_loop_skeleton_census.py"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("census", SCRIPT)
    census = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(census)
    result = census.verify()
    require(sum(len(rows) for rows in result.values()) == 10, "orbit count")
    require(sum(sum(size for _, size in rows) for rows in result.values()) == 13,
            "labeled count")
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
        "rate_half_kb_m2_r4_coordinate_k_fiber_vieta_rank_compiler",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    statement = (NODE / "statement.md").read_text()
    require("injectivity" in statement and
            "multiplicities three and four" in statement,
            "injectivity fence")
    require("does not delete a skeleton" in statement, "nonclaim")
    print(
        "RATE_HALF_KB_POSITIVE_LOOP_RAMIFICATION_VERIFY_PASS "
        "profiles=2 orbits=10 labeled=13"
    )


if __name__ == "__main__":
    main()
