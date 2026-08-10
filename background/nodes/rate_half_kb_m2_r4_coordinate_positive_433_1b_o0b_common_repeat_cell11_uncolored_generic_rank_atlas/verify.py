#!/usr/bin/env python3
"""Verify the repeated-BC cell-11 uncolored generic-rank atlas."""

from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
PARENT = "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell11_common_kernel_reconstruction"
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"
CORE_SHA256 = "336aace4780acce09d9cb53cc969635d16a038af0a5379338a746e086758aac7"
TOWER_SHA256 = "e80940956518b958dafe74eb34e8ce4f00ce729e78646203bb0724057e6f7899"
FILES = {
    "launcher": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_uncolored_generic_rank_modal.py",
        "d6995ccc293a30c3277c108a42dcbcbe1c7afa7eece40cd263a1cfd9cc9cb786",
    ),
    "plus": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_uncolored_generic_rank_bcplus_result.json",
        "8f7e84f601514685dbb0079ec8f5b9851e5e051602dd815d06a82e0c34c8d1ec",
    ),
    "minus": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_uncolored_generic_rank_bcminus_result.json",
        "bae6700ba440c027ff97c40188f5fa6d33b82ad38183fffc3c70222ae84518c3",
    ),
}
MISSING = ("DE+", "DF+", "EF")
DEGREE_COUNTS = {
    (0, 4, 4): 48,
    (2, 2, 4): 176,
    (2, 4, 2): 64,
    (4, 0, 4): 24,
    (4, 2, 2): 48,
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load(label):
    return json.loads((EXPERIMENTS / FILES[label][0]).read_text())


def validate(payload, bc_sign):
    require(payload["schema"].endswith("cell11-uncolored-generic-rank-v1"), "schema")
    require(payload["core_sha256"] == CORE_SHA256, "core custody")
    require(payload["tower_sha256"] == TOWER_SHA256, "tower custody")
    require(payload["bc_sign_filter"] == bc_sign and payload["complete_atlas"],
            "shard scope")
    require(payload["case_count"] == 360 and
            payload["status_counts"] == {"GENERIC_UNIT": 360}, "status census")
    require(len(payload["guard_atlas"]) == (15 if bc_sign == 1 else 27),
            "guard atlas")
    expected = set(itertools.product(
        (-1, 1), (-1, 1), MISSING, (-1, 1), range(15)
    ))
    actual = set()
    degree_counts = Counter()
    rank_counts = Counter()
    for row in payload["rows"]:
        key = (*row["epsilon"], row["missing_record"], row["sigma_o"],
               row["pairing_index"])
        require(key in expected and key not in actual, "formal coverage")
        actual.add(key)
        require(row["bc_sign"] == bc_sign and row["status"] == "GENERIC_UNIT",
                "row scope")
        require(row["base_degree"] == (4 if bc_sign == 1 else 6), "base degree")
        require(row["selected"] == row["pair_rows"][-1], "selected pair")
        selected = row["selected"]
        require(selected["witness_x"] == 2 and
                selected["construction_guards_nonzero"], "guarded specialization")
        require(0 < selected["witness_determinant"] < 2130706433,
                "nonzero determinant")
        require(selected["last_rank"] == selected["size"], "full rank")
        require(set(row["guard_hashes"]) <= set(payload["guard_atlas"]),
                "guard references")
        require(len(row["matching"]) == 3 and
                sorted(value for pair in row["matching"] for value in pair)
                == sorted(row["residual_records"]), "matching partition")
        degree_counts[tuple(row["equation_degrees"])] += 1
        rank_counts[selected["size"]] += 1
    require(actual == expected, "complete formal product")
    require(dict(degree_counts) == DEGREE_COUNTS, "degree histogram")
    expected_ranks = {64: 248, 96: 112} if bc_sign == 1 else {96: 248, 144: 112}
    require(dict(rank_counts) == expected_ranks, "rank histogram")


def main():
    for filename, expected in FILES.values():
        actual = hashlib.sha256((EXPERIMENTS / filename).read_bytes()).hexdigest()
        require(actual == expected, f"file custody {filename}")
    validate(load("plus"), 1)
    validate(load("minus"), -1)
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req")) for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    require(nodes[PARENT]["status"] == "PROVED" and (PARENT, NODE_ID, "req") in edges,
            "parent")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_CELL11_GENERIC_RANK_VERIFY_PASS cases=720 witness_x=2 ranks=64,96,144")


if __name__ == "__main__":
    main()
