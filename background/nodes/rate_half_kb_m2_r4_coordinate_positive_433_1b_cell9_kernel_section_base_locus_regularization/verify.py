#!/usr/bin/env python3
"""Verify the cell-9 section-base pointwise regularization."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell9_kernel_null_residual_modal.py"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell9_kernel_null_residual_result.json"
REPLAY = EXP / "rate_half_kb_positive_433_1b_cell9_endpoint_replay_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell9_compact_kernel_result.json"
PINNED = {
    SCRIPT: "812198b5149cb90649464144e7b7b8f6e2f9cc3ba5e0fb5b91f7bfaf14b58a0d",
    RESULT: "4197b0413cfae562589351850cf937c5a0aaca9dc021e30d8ff360bebdb64993",
}
PRIME = 2130706433
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_endpoint_compatibility_decomposition",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_global_five_relation_common_locus",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_global_common_kernel",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def point_key(row):
    point = row["point"]
    return (tuple(row["epsilon"]), row["point_index"],
            tuple(point[name] for name in ("r", "t", "b", "c")))


def main():
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"hash drift: {path.name}")
    payload = json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell9-kernel-null-residual-v1"
            and payload["field"] == PRIME
            and payload["source_replay_sha256"] == digest(REPLAY)
            and payload["source_kernel_sha256"] == digest(KERNEL),
            "payload custody")
    signs = tuple(itertools.product((-1, 1), repeat=2))
    expected = {
        (source, point, lane)
        for source in signs for point in range(2) for lane in signs
    }
    seen = set()
    source_data = {}
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), row["point_index"], tuple(row["sigma"]))
        require(key in expected and key not in seen, "row coverage")
        seen.add(key)
        require(row["status"] == "COMPLETE" and row["common_rank"] == 7
                and row["section_is_zero"]
                and row["section_values"] == [0] * 8
                and row["kernel_dots"] == [0] * 10
                and row["missing_mode"] == "REGULARIZED_CONSTRAINED"
                and len(row["missing_values"]) == 3
                and row["missing_values"][0] != 0
                and row["point"]["guard_nonzero"], "regularization ledger")
        value = (point_key(row), tuple(row["missing_values"]))
        source_key = key[:2]
        previous = source_data.setdefault(source_key, value)
        require(previous == value, "target-lane source drift")
    require(seen == expected and len(source_data) == 8,
            "regularization Cartesian cover")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE.name in nodes and nodes[NODE.name]["status"] == "PROVED",
            "DAG node")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    require(all((parent, NODE.name, "req") in edges for parent in PARENTS),
            "DAG parents")
    print("cell=9 section_base_points=8 common_rank=7 constrained=8")


if __name__ == "__main__":
    main()
