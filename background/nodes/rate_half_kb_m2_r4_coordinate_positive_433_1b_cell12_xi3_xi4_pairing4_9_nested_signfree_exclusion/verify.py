#!/usr/bin/env python3
"""Verify the cell-12 reciprocal matching-4/9 packet."""

import ast
import collections
import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
SCRIPT = EXP / (
    "rate_half_kb_positive_433_1b_cell12_xi3_pairing4_"
    "template_adapter_modal.py"
)
RESULT = EXP / (
    "rate_half_kb_positive_433_1b_cell12_xi3_pairing4_"
    "template_adapter_result.json"
)
TEMPLATE = EXP / (
    "rate_half_kb_positive_433_1b_cell4_xi3_pairing4_"
    "nested_signfree_modal.py"
)
TOWER = EXP / "rate_half_kb_positive_433_1b_cell12_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell12_compact_kernel_result.json"
ROOT_SCRIPT = EXP / (
    "rate_half_kb_positive_433_1b_cell12_xi3_pairing4_"
    "independent_roots_modal.py"
)
ROOT_RESULT = EXP / (
    "rate_half_kb_positive_433_1b_cell12_xi3_pairing4_"
    "independent_roots_result.json"
)
PINNED = {
    SCRIPT: "2ac5d9ed71f83f1a0da5d1f5875ac2c73fbd608bf4dea0d511cc39393beccda7",
    RESULT: "29540cf0d63cfdd9a961b5c9bd31e5f63e7de5328e385d22911b0c36c158303e",
    TEMPLATE: "0992beedc8d85e1d7e510d40dadccd72d01e8b38325d9e6fe56c741ab50711fd",
    ROOT_SCRIPT: "06e6f9b2e32e3daa1665332ff4740935c91f73e483fc9f84e3e7b0f4056aa383",
    ROOT_RESULT: "db66fcb66d5b849fbda9f9eff8157b568f4063c594f1b1a63e8ea7e1668b7829",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def lanes(row):
    for finite in row["finite_rows"]:
        for z_row in finite.get("z_rows", []):
            for q_row in z_row.get("q_rows", []):
                yield from q_row.get("lanes", [])


def main():
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"hash drift: {path.name}")
    ast.parse(SCRIPT.read_text())
    payload = json.loads(RESULT.read_text())
    require(
        payload["schema"]
        == "rate-half-kb-positive-433-1b-cell12-xi3-pairing4-adapter-v1"
        and payload["field"] == 2130706433
        and payload["source_template_sha256"] == digest(TEMPLATE)
        and payload["source_tower_sha256"] == digest(TOWER)
        and payload["source_kernel_sha256"] == digest(KERNEL),
        "packet custody",
    )
    expected = set(itertools.product((-1, 1), repeat=2))
    seen = set()
    all_lanes = []
    for row in payload["rows"]:
        key = tuple(row["epsilon"])
        require(key in expected and key not in seen, "source-sign coverage")
        seen.add(key)
        require(
            row["status"] == "COMPLETE"
            and row["target_excluded"]
            and row["xi_index"] == 3
            and row["pairing_index"] == 4
            and row["remainder_degree"] == 1
            and row["witness_count"] == 0
            and not row["witnesses"]
            and row["q_candidate_count"] == 2
            and row["final_pair_solution_count"] == 0
            and not row["final_pair_solutions"]
            and not row["unresolved"],
            "complete branch terminal",
        )
        all_lanes.extend(lanes(row))
    require(seen == expected and len(payload["rows"]) == 4, "four-row cover")
    require(
        sum(row["target_norm_root_count"] for row in payload["rows"]) == 32
        and sum(row["candidate_root_count"] for row in payload["rows"]) == 72
        and sum(row["source_point_count"] for row in payload["rows"]) == 120
        and sum(row["route_point_count"] for row in payload["rows"]) == 120
        and sum(row["z_candidate_count"] for row in payload["rows"]) == 8
        and sum(row["q_candidate_count"] for row in payload["rows"]) == 8,
        "exact census totals",
    )
    require(
        len(all_lanes) == 32
        and all(
            lane["status"] == "THIRD_PAIR_NONZERO"
            and lane["final_pair_cut"] % 2130706433
            for lane in all_lanes
        ),
        "32 final lanes",
    )
    statuses = collections.Counter(
        item["status"]
        for row in payload["rows"] for item in row["finite_rows"]
    )
    require(
        statuses == {
            "CHECKED": 96,
            "MISSING_IMPOSSIBLE": 12,
            "TARGET_PRODUCT_BOUNDARY": 12,
        },
        "finite terminal partition",
    )
    boundary = collections.Counter(
        item["stage"]
        for row in payload["rows"] for item in row["boundary_rows"]
    )
    require(
        boundary == {"R_GUARD": 20, "T_GUARD": 16, "CELL12_B_LEADING": 4},
        "boundary terminal partition",
    )
    require(
        sum(len(row["target_boundary_rows"]) for row in payload["rows"]) == 12,
        "target-product boundary census",
    )
    manifest = json.loads((NODE / "node.json").read_text())
    require(
        manifest["node"]["id"] == NODE.name
        and manifest["node"]["status"] == "PROVED",
        "node manifest",
    )
    print("PASS cell-12 reciprocal pairing 4/9: rows=4 candidates=72 lanes=32")


if __name__ == "__main__":
    main()
