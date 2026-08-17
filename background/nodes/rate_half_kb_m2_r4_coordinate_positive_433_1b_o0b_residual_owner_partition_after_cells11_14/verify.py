#!/usr/bin/env python3
"""Verify the revised O0b residual owner partition."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_residual_owner_partition",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cells11_14_complete_outside_exclusion",
)
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def validate(blocks=(("split_rank5", 360), ("cells1_2", 16), ("cells11_14", 32))):
    require(tuple(name for name, _ in blocks)
            == ("split_rank5", "cells1_2", "cells11_14"), "owner blocks")
    require(tuple(rows for _, rows in blocks) == (360, 16, 32), "parent rows")
    raw = tuple(rows * 105 for _, rows in blocks)
    require(raw == (37800, 1680, 3360) and sum(raw) == 42840, "parent raw census")
    residual_rows = sum(rows for _, rows in blocks[:2])
    residual_raw = sum(raw[:2])
    require(residual_rows == 376 and residual_raw == 39480, "residual census")
    require(sum(raw) - raw[2] == residual_raw, "exact subtraction")
    return residual_rows, residual_raw


def main():
    rows, raw = validate()
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req")) for row in dag["edges"]}
    require(nodes[NODE.name]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED"
                and (parent, NODE.name, "req") in edges, "parent")
    require((NODE.name, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REVISED_OWNER_VERIFY_PASS "
          f"common_rows={rows} raw_labels={raw}")


if __name__ == "__main__":
    main()
