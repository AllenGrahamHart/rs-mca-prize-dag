#!/usr/bin/env python3
"""Verify the cell-12 reciprocal matching-11/14 packet."""

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
    "rate_half_kb_positive_433_1b_cell12_xi3_pairing11_"
    "template_adapter_modal.py"
)
RESULT = EXP / (
    "rate_half_kb_positive_433_1b_cell12_xi3_pairing11_"
    "template_adapter_result.json"
)
TEMPLATE = EXP / (
    "rate_half_kb_positive_433_1b_cell4_xi3_pairing11_"
    "quadratic_resultant_signfree_modal.py"
)
TOWER = EXP / "rate_half_kb_positive_433_1b_cell12_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell12_compact_kernel_result.json"
ROOT_SCRIPT = EXP / (
    "rate_half_kb_positive_433_1b_cell12_xi3_pairing11_"
    "independent_roots_modal.py"
)
ROOT_RESULT = EXP / (
    "rate_half_kb_positive_433_1b_cell12_xi3_pairing11_"
    "independent_roots_result.json"
)
PINNED = {
    SCRIPT: "c1d3f153daac92734d5c58301d5e48eab0739069febda6ed9c76ab1e28d10d9c",
    RESULT: "6e229e8fc5585b21d1feff781e3bc2ce00ca9b1169553bd7370d0ec3369a76c6",
    TEMPLATE: "8f2fe8ca53863b2220ae60558b3f8d64269eec0f3952138679f2bc3a7069698b",
    ROOT_SCRIPT: "bf2ae15c7c6bc9298427adccc8cfcb401b562343c7e901c49f4cf34b601f2085",
    ROOT_RESULT: "a8ad5dca87941a6d22698430b12f52d3ad5e560f1335e9232b2e2106f84a45f4",
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
        == "rate-half-kb-positive-433-1b-cell12-xi3-pairing11-adapter-v1"
        and payload["field"] == 2130706433
        and payload["source_template_sha256"] == digest(TEMPLATE)
        and payload["source_tower_sha256"] == digest(TOWER)
        and payload["source_kernel_sha256"] == digest(KERNEL),
        "packet custody",
    )
    expected = set(itertools.product(
        itertools.product((-1, 1), repeat=2), (-1, 1)
    ))
    seen = set()
    all_lanes = []
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), row["sigma_c"])
        require(key in expected and key not in seen, "source-sign coverage")
        seen.add(key)
        row_census = {
            -1: (6, 12, 14, 0),
            1: (9, 15, 20, 4),
        }[row["sigma_c"]]
        require(
            row["status"] == "COMPLETE"
            and row["target_excluded"]
            and row["xi_index"] == 3
            and row["pairing_index"] == 11
            and row["remainder_degree"] == 1
            and row["witness_count"] == 0
            and not row["witnesses"]
            and (
                row["target_norm_root_count"], row["candidate_root_count"],
                row["source_point_count"], row["q_candidate_count"],
            ) == row_census
            and row["route_point_count"] == row["source_point_count"]
            and row["z_candidate_count"] == row["q_candidate_count"]
            and row["final_pair_solution_count"] == 0
            and not row["final_pair_solutions"]
            and not row["unresolved"],
            "complete branch terminal",
        )
        all_lanes.extend(lanes(row))
    require(seen == expected and len(payload["rows"]) == 8, "eight-row cover")
    require(
        sum(row["target_norm_root_count"] for row in payload["rows"]) == 60
        and sum(row["candidate_root_count"] for row in payload["rows"]) == 108
        and sum(row["source_point_count"] for row in payload["rows"]) == 136
        and sum(row["route_point_count"] for row in payload["rows"]) == 136
        and sum(row["z_candidate_count"] for row in payload["rows"]) == 16
        and sum(row["q_candidate_count"] for row in payload["rows"]) == 16,
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
            "CHECKED": 88,
            "MISSING_IMPOSSIBLE": 24,
            "TARGET_PRODUCT_BOUNDARY": 24,
        },
        "finite terminal partition",
    )
    boundary = collections.Counter(
        item["stage"]
        for row in payload["rows"] for item in row["boundary_rows"]
    )
    require(
        boundary == {"R_GUARD": 40, "T_GUARD": 32, "CELL12_B_LEADING": 8},
        "boundary terminal partition",
    )
    require(
        sum(len(row["target_boundary_rows"]) for row in payload["rows"]) == 24,
        "target-product boundary census",
    )
    manifest = json.loads((NODE / "node.json").read_text())
    require(
        manifest["node"]["id"] == NODE.name
        and manifest["node"]["status"] == "PROVED",
        "node manifest",
    )
    print("PASS cell-12 reciprocal pairing 11/14: rows=8 candidates=108 lanes=32")


if __name__ == "__main__":
    main()
