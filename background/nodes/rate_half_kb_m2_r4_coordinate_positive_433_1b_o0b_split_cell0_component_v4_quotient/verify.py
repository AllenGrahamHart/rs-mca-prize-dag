#!/usr/bin/env python3
"""Verify the O0b split cell-0 component quotient."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SCRIPT = (ROOT / "experiments/prize_resolution" /
          "rate_half_kb_positive_433_1b_o0b_split_cell0_component_quotient.py")
SCRIPT_SHA256 = "7b47abccdf701daff94e0191fe23f9d7847ffd9e3f0c9a7d0958a40bada50a13"
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_split_cell0_common_component_classification",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_s0_v4_label_quotient",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_repeated_outside_v4_quotient",
)
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    require(hashlib.sha256(SCRIPT.read_bytes()).hexdigest() == SCRIPT_SHA256,
            "quotient compiler custody")
    spec = importlib.util.spec_from_file_location("component_quotient", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    require(module.verify() == {
        "raw_cases": 2520,
        "s0_profile": {2: 36, 4: 192},
        "repeated_profile": {2: 120, 4: 360},
        "representative_count": 708,
        "representatives_sha256":
            "23d7e403e420307b5466ffaf6d2af59d0cf9a4a93766b4d0bcf68231aba1a741",
        "component_rows": 4,
    }, "component quotient result")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req"))
             for row in dag["edges"]}
    require(nodes[NODE.name]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED" and
                (parent, NODE.name, "req") in edges, "parent")
    require((NODE.name, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELL0_COMPONENT_VERIFY_PASS "
          "raw=2520 reps=708 profile=2:156,4:552")


if __name__ == "__main__":
    main()
