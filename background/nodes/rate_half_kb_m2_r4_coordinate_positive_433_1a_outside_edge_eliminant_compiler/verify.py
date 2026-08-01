#!/usr/bin/env python3
"""Verify the positive 433-1a outside-edge eliminant compiler."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "outside_edge_eliminant_compiler"
)
PARENT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "quadratic_paired_product_resultant_interface"
)
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1a_outside_edge_eliminant.py"
)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    specification = importlib.util.spec_from_file_location("eliminant", SCRIPT)
    eliminant = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(eliminant)
    require(eliminant.verify() == {
        "generic_terms": 22,
        "generic_total_degree": 6,
        "linear_total_degree": 5,
    }, "eliminant shape")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "node status")
    edges = {
        (edge["from"], edge["to"], edge["kind"])
        for edge in dag["edges"]
    }
    require((PARENT, NODE_ID, "req") in edges, "dependency")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer")

    statement = (NODE / "statement.md").read_text()
    for marker in ("22 terms", "A=0,B!=0", "A=B=0", "bare resultant"):
        require(marker in statement, f"statement marker {marker}")
    print(
        "positive 433-1a outside-edge eliminant verified "
        "generic_terms=22 generic_degree=6 linear_degree=5"
    )


if __name__ == "__main__":
    main()
