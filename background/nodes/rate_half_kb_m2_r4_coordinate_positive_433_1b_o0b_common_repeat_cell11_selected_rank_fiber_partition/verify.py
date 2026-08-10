#!/usr/bin/env python3
"""Verify the repeated-BC cell-11 selected-rank fiber partition."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
PREFIX = "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_"
FILES = {
    "launcher": (PREFIX + "rank_fiber_modal.py", "ea39704acf28b5e4208e3bd1cdae5bee92046ca8315afe0ba434305d07454215"),
    "result": (PREFIX + "rank_fiber_result.json", "25a2f3fc08a68bf4a586df6926ba4558bf1e5751b2486302be096155f856ffc5"),
}
SOURCE_SHA256 = "a9c3f10fc7e368f88599bce085598d641d0a73352a1f7d54e06abcd9b4aabbf7"
PARENT = "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell11_curve_projection_atlas"
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"
MINOR_HASH = {
    -1: "565aa4fb6fb918dfd2cad221ba290a17c8e148890f31c52996b2a3759c8bd9ef",
    1: "e3570ad8e5401672b4212af63f2c30d9b454f178335c51e21289b211a693ee99",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def validate(payload):
    require(payload["schema"] == "rate-half-kb-positive-433-1b-o0b-common-repeat-cell11-rank-fiber-v1", "schema")
    require(payload["source_sha256"] == SOURCE_SHA256, "source")
    require(payload["status_counts"] == {"COMPLETE": 8}, "completion")
    expected = set(itertools.product((-1, 1), (-1, 1), (-1, 1)))
    actual = set()
    degrees = {-1: [], 1: []}
    for row in payload["rows"]:
        key = (*row["epsilon"], row["bc_sign"])
        require(key in expected and key not in actual, "case")
        actual.add(key)
        sign = row["bc_sign"]
        sign_product = row["epsilon"][0] * row["epsilon"][1]
        require(row["status"] == "COMPLETE" and not row["stderr"], "row completion")
        require(row["full_dimension"] == 1 and row["full_basis_size"] == (21 if sign == -1 else 17), "common geometry")
        require(row["t_relation"] == f"t={sign_product}*r^2" and row["t_relation_remainder"] == "0", "t relation")
        require(row["selected_rank_minor_sha256"] == MINOR_HASH[sign], "minor identity")
        require(row["selected_rank_minor_remainder"] not in ("", "0") and len(row["selected_rank_minor_remainder_sha256"]) == 64, "minor nonvanishing")
        require(row["selected_rank_fiber_dimension"] == 0 and row["selected_rank_fiber_basis_size"] == 8, "fiber dimension")
        require(row["selected_rank_fiber_vdim"] == (4 if sign == -1 else 6), "fiber degree")
        degrees[sign].append(row["selected_rank_fiber_vdim"])
    require(actual == expected and degrees == {-1: [4] * 4, 1: [6] * 4}, "coverage")


def main():
    for filename, digest in FILES.values():
        require(hashlib.sha256((EXPERIMENTS / filename).read_bytes()).hexdigest() == digest, f"file custody {filename}")
    validate(json.loads((EXPERIMENTS / FILES["result"][0]).read_text()))
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req")) for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    require(nodes[PARENT]["status"] == "PROVED" and (PARENT, NODE_ID, "req") in edges, "parent")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_CELL11_SELECTED_RANK_FIBER_VERIFY_PASS rows=8 boundary_degree=40")


if __name__ == "__main__":
    main()
