#!/usr/bin/env python3
"""Verify the O0b split cell-0 common-component classification."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SCRIPT = (ROOT / "experiments/prize_resolution" /
          "rate_half_kb_positive_433_1b_o0b_split_cell0_common_classification.py")
SCRIPT_SHA256 = "2e2aa2117ba3427e011b23d656db374552a5a4d60a24905f46d557d35be80323"
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_split_principal_common_system_adapter",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell0_complete_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_s0_v4_label_quotient",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_repeated_outside_v4_quotient",
)
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    require(hashlib.sha256(SCRIPT.read_bytes()).hexdigest() == SCRIPT_SHA256,
            "classifier custody")
    spec = importlib.util.spec_from_file_location("cell0_common", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    require(module.verify() == {
        "mixed_charts": 12,
        "equal_charts": 12,
        "component_rows": 4,
        "mixed_raw_closed": 1260,
        "mixed_orbits_closed": 354,
        "s0_profile": {2: 18, 4: 96},
        "repeated_profile": {2: 60, 4: 180},
        "owner_raw_remaining": 38220,
        "owner_orbits_remaining": 10722,
        "equal_raw_remaining": 1260,
        "equal_component_orbits": 708,
    }, "cell-0 classification result")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req"))
             for row in dag["edges"]}
    require(nodes[NODE.name]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED" and
                (parent, NODE.name, "req") in edges, "parent")
    require((NODE.name, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELL0_COMMON_VERIFY_PASS "
          "closed=1260/354 owner=38220/10722 components=708")


if __name__ == "__main__":
    main()
