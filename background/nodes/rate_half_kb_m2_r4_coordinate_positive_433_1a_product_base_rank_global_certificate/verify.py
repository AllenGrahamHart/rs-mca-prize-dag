#!/usr/bin/env python3
"""Verify the positive 433-1a global product-base rank certificate."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_minor_compiler",
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_product_base_rank_five_orbit_exclusion",
)
RESULT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1a_product_base_rank_singular_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    payload = json.loads(RESULT.read_text())
    require(payload["field"] == 2130706433, "deployed field")
    require(set(payload["cells"]) == {"1", "9", "12"}, "certificate cells")
    for cell, row in payload["cells"].items():
        require(row["singular_output"] == ["UNIT", "1", "1"],
                f"unit output {cell}")
        require(len(row["program_sha256"]) == 64, f"program hash {cell}")
        require(len(row["equation_sha256"]) == 6, f"equation hashes {cell}")

    source = (ROOT / "experiments/prize_resolution/"
              "rate_half_kb_positive_433_1a_product_base_rank_singular_modal.py")
    text = source.read_text()
    require("z*({guard})-1" in text, "inverse localization")
    require("reduce(1,G)==0" in text, "unit test")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"parent {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer edge")
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_PRODUCT_BASE_GLOBAL_VERIFY_PASS "
        "cells=15 product_rank=5 base_rank=6 singular_units=3"
    )


if __name__ == "__main__":
    main()
