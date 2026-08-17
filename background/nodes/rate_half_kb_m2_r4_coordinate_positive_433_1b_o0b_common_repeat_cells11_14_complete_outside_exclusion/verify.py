#!/usr/bin/env python3
"""Verify complete repeated-BC cells 11-14 outside exclusion."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell11_complete_outside_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cells11_14_duplicate_role_transport",
)
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def validate(cells=(11, 14), rows_per_cell=16, labels_per_row=105):
    require(tuple(cells) == (11, 14) and len(set(cells)) == 2, "cell owners")
    require(rows_per_cell == 16 and labels_per_row == 105, "owner sizes")
    per_cell = rows_per_cell * labels_per_row
    total = len(cells) * per_cell
    require(per_cell == 1680 and total == 3360, "owner arithmetic")
    return total


def main():
    total = validate()
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req")) for row in dag["edges"]}
    require(nodes[NODE.name]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED"
                and (parent, NODE.name, "req") in edges, "parent")
    require((NODE.name, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_CELLS11_14_COMPLETE_VERIFY_PASS "
          f"raw_labels={total}")


if __name__ == "__main__":
    main()
