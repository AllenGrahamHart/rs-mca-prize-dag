#!/usr/bin/env python3
"""Verify complete exclusion of O0b split cells 1 and 2."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SCRIPT = (ROOT / "experiments/prize_resolution" /
          "rate_half_kb_positive_433_1b_o0b_split_cells1_2_common_exclusion.py")
SCRIPT_SHA256 = "b1f6757006b34fa64cf275c16e158a612a91553f2e02ff141b9546cb9af487cf"
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_split_principal_common_system_adapter",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cells1_2_complete_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_s0_v4_label_quotient",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_repeated_outside_v4_quotient",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_split_cell0_complete_exclusion",
)
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    require(hashlib.sha256(SCRIPT.read_bytes()).hexdigest() == SCRIPT_SHA256,
            "transport compiler custody")
    spec = importlib.util.spec_from_file_location("cells1_2_exclusion", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    require(module.verify() == {
        "charts": 48,
        "raw_closed": 5040,
        "representatives_closed": 1416,
        "s0_profile": {2: 72, 4: 384},
        "repeated_profile": {2: 240, 4: 720},
        "owner_raw_remaining": 31920,
        "owner_representatives_remaining": 8952,
    }, "cells-1/2 exclusion result")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req"))
             for row in dag["edges"]}
    require(nodes[NODE.name]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED" and
                (parent, NODE.name, "req") in edges, "parent")
    require((NODE.name, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELLS1_2_VERIFY_PASS "
          "closed=5040/1416 owner=31920/8952")


if __name__ == "__main__":
    main()
