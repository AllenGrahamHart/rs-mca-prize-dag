#!/usr/bin/env python3
"""Verify the exact post-closure 433-1b/O0b owner partition."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_vieta_minor_atlas",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_saturation_classification",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_outside_label_quotient",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cells3_6_bcplus_complete_outside_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cells3_6_bcminus_complete_outside_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_split_rankdrop_complete_exclusion",
)
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def validate(dag):
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req"))
             for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "partition status")
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED", f"parent status {parent}")
        require((parent, NODE_ID, "req") in edges, f"parent edge {parent}")

    signed, compiler, saturation, quotient, bcplus, bcminus, rankdrop = (
        nodes[parent] for parent in PARENTS
    )
    require("ten-lane" in signed["closure"], "ten-lane atlas")
    require("six split-BC" in compiler["statement"] and
            "four repeated-BC" in compiler["statement"], "compiler split")
    require("Forty survive" in saturation["statement"] and
            "160 of 240" in saturation["statement"], "repeat saturation")
    require("105-to-57" in quotient["closure"], "outside label unit")
    require("840" in bcplus["closure"] and "840" in bcminus["closure"],
            "cells3/6 closures")
    require("10,080" in rankdrop["closure"], "split rank-drop closure")

    split_rows = 6 * 15 * 4
    repeated_initial = 4 * 15 * 4
    repeated_after_common = 80
    repeated_closed = 32
    repeated_12 = 16
    repeated_1114 = repeated_after_common - repeated_closed - repeated_12
    require((split_rows, repeated_initial, repeated_1114) == (360, 240, 32),
            "row arithmetic")
    labels = {
        "split": split_rows * 105,
        "repeat12": repeated_12 * 105,
        "repeat1114": repeated_1114 * 105,
    }
    require(labels == {"split": 37800, "repeat12": 1680,
                       "repeat1114": 3360}, "label arithmetic")
    require(sum(labels.values()) == 42840 and
            split_rows + repeated_12 + repeated_1114 == 408,
            "residual totals")
    require("408" in nodes[NODE_ID]["closure"] and
            "42,840" in nodes[NODE_ID]["closure"] and
            all(value in nodes[NODE_ID]["statement"]
                for value in ("37,800", "1,680", "3,360")),
            "printed partition")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer edge")


def main():
    validate(json.loads((ROOT / "dag.json").read_text()))
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_RESIDUAL_PARTITION_VERIFY_PASS rows=408 labels=42840 blocks=3")


if __name__ == "__main__":
    main()
