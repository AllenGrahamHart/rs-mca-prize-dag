#!/usr/bin/env python3
"""Verify the cell-12 reciprocal-linear pairings 1-2 packet."""

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
    "rate_half_kb_positive_433_1b_cell12_xi3_pairings1_2_"
    "template_adapter_modal.py"
)
RESULT = EXP / (
    "rate_half_kb_positive_433_1b_cell12_xi3_pairings1_2_"
    "template_adapter_result.json"
)
TEMPLATE = EXP / (
    "rate_half_kb_positive_433_1b_cell4_xi3_pairings1_2_"
    "reciprocal_linear_modal.py"
)
TOWER = EXP / "rate_half_kb_positive_433_1b_cell12_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell12_compact_kernel_result.json"
PINNED = {
    SCRIPT: "33617b237da8b16f0070dc33109bbd97b75d6170331e922c847e7955eaccbf41",
    RESULT: "bbe8fcc924f4dab01d5806e42baad0de6963bda4eb918c1462c01fa638cc0587",
    TEMPLATE: "6175e9472f571b752273395050247db907e9bbb68065c7c0c8bdd0933e4ac2aa",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def lanes(row):
    for finite in row["finite_rows"]:
        for z_row in finite.get("z_rows", []):
            yield from z_row.get("lanes", [])


def main():
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"hash drift: {path.name}")
    ast.parse(SCRIPT.read_text())
    payload = json.loads(RESULT.read_text())
    require(
        payload["schema"] == (
            "rate-half-kb-positive-433-1b-cell12-xi3-pairings1-2-adapter-v1"
        )
        and payload["field"] == 2130706433
        and payload["source_template_sha256"] == digest(TEMPLATE)
        and payload["source_tower_sha256"] == digest(TOWER)
        and payload["source_kernel_sha256"] == digest(KERNEL),
        "packet custody",
    )
    signs = tuple(itertools.product((-1, 1), repeat=2))
    expected = {
        (*epsilon, branch, 0, 1)
        for epsilon in signs for branch in range(3)
    } | {
        (*epsilon, branch, sigma_c, 2)
        for epsilon in signs for branch in range(3) for sigma_c in (-1, 1)
    }
    seen = set()
    all_lanes = []
    for row in payload["rows"]:
        key = (
            *row["epsilon"], row["branch_index"],
            row["sigma_c_anchor"], row["pairing_index"],
        )
        require(key in expected and key not in seen, "branch coverage")
        seen.add(key)
        require(
            row["status"] == "COMPLETE"
            and row["target_excluded"]
            and row["xi_index"] == 3
            and row["pairing_index"] in (1, 2)
            and row["remainder_degree"] == 1
            and row["witness_count"] == 0
            and not row["witnesses"]
            and row["final_pair_solution_count"] == 0
            and not row["final_pair_solutions"]
            and not row["unresolved"],
            "complete branch terminal",
        )
        all_lanes.extend(lanes(row))
    require(seen == expected and len(payload["rows"]) == 36, "36-row cover")
    require(
        sum(row["target_norm_root_count"] for row in payload["rows"]) == 244
        and sum(row["candidate_root_count"] for row in payload["rows"]) == 620
        and sum(row["source_point_count"] for row in payload["rows"]) == 1040
        and sum(row["route_point_count"] for row in payload["rows"]) == 1040
        and sum(row["z_candidate_count"] for row in payload["rows"]) == 80,
        "exact census totals",
    )
    require(
        len(all_lanes) == 192
        and all(
            item["status"] == "THIRD_PAIR_NONZERO"
            and item["final_pair_cut"] % 2130706433
            for item in all_lanes
        ),
        "192 final lanes",
    )
    statuses = collections.Counter(
        item["status"]
        for row in payload["rows"] for item in row["finite_rows"]
    )
    require(
        statuses == {
            "CHECKED": 776,
            "MISSING_IMPOSSIBLE": 108,
            "TARGET_PRODUCT_BOUNDARY": 108,
            "EMPTY_Q_BRANCH": 48,
        },
        "finite terminal partition",
    )
    boundary = collections.Counter(
        item["stage"]
        for row in payload["rows"] for item in row["boundary_rows"]
    )
    require(
        boundary == {"R_GUARD": 180, "T_GUARD": 144, "CELL12_B_LEADING": 36},
        "boundary terminal partition",
    )
    manifest = json.loads((NODE / "node.json").read_text())
    require(
        manifest["node"]["id"] == NODE.name
        and manifest["node"]["status"] == "PROVED",
        "node manifest",
    )
    print("PASS cell-12 reciprocal pairings 1-2: rows=36 candidates=620 lanes=192")


if __name__ == "__main__":
    main()
