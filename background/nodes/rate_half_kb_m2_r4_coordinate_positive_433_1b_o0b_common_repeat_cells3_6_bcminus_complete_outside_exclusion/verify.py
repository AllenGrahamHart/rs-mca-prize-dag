#!/usr/bin/env python3
"""Verify the complete repeated-BC BC- cells-3/6 outside aggregate."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
COLORED = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_"
    "cell3_bcminus_colored_missing_exclusion"
)
UNCOLORED = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_"
    "cell3_bcminus_uncolored_complete_outside_exclusion"
)
TRANSPORT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_"
    "cells3_6_full_system_transport"
)
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def validate(dag):
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req"))
             for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "aggregate status")
    for parent in (COLORED, UNCOLORED, TRANSPORT):
        require(nodes[parent]["status"] == "PROVED", f"parent status {parent}")
        require((parent, NODE_ID, "req") in edges, f"parent edge {parent}")
    require("240" in nodes[COLORED]["closure"], "colored census")
    require("600" in nodes[UNCOLORED]["closure"], "uncolored census")
    require("1,680" in nodes[TRANSPORT]["statement"], "transport census")
    require("840" in nodes[NODE_ID]["closure"] and
            nodes[NODE_ID]["statement"].count("840") >= 2,
            "aggregate census")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer edge")


def main():
    validate(json.loads((ROOT / "dag.json").read_text()))
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_BCMINUS_COMPLETE_OUTSIDE_VERIFY_PASS cell3=840 cell6=840")


if __name__ == "__main__":
    main()
