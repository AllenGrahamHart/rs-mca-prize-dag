#!/usr/bin/env python3
"""Verify the cell-12 reciprocal-role pairing-0 packet."""

import ast
import collections
import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell12_xi3_pairing0_template_adapter_modal.py"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell12_xi3_pairing0_template_adapter_result.json"
TEMPLATE = EXP / "rate_half_kb_positive_433_1b_cell4_xi3_pairing0_reciprocal_square_modal.py"
TOWER = EXP / "rate_half_kb_positive_433_1b_cell12_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell12_compact_kernel_result.json"
PINNED = {
    SCRIPT: "0ba327c456d78c1b8d0da05255a1eaf3c1dadc4a84c01ee718b74e2c9f13e389",
    RESULT: "1aed6f7e6a5459a4ffdc5f246b76efe923bb6f5a40b3911b505aabf9a4a42c6b",
    TEMPLATE: "be6e74f8713af6f26fe183a00e5bc50d0a89aa1fdd53c1c636525165a2f5ae68",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def lanes(row):
    for finite in row["finite_rows"]:
        for y_row in finite.get("yd_rows", []):
            for d_row in y_row.get("d_rows", []):
                yield from d_row.get("lanes", [])


def main():
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"hash drift: {path.name}")
    ast.parse(SCRIPT.read_text())
    payload = json.loads(RESULT.read_text())
    require(payload["schema"] == "rate-half-kb-positive-433-1b-cell12-xi3-pairing0-adapter-v1"
            and payload["field"] == 2130706433
            and payload["source_template_sha256"] == digest(TEMPLATE)
            and payload["source_tower_sha256"] == digest(TOWER)
            and payload["source_kernel_sha256"] == digest(KERNEL),
            "packet custody")
    expected = set(itertools.product(
        itertools.product((-1, 1), repeat=2), range(3), (-1, 1)
    ))
    seen = set()
    all_lanes = []
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), row["branch_index"], row["sigma_o"])
        require(key in expected and key not in seen, "branch coverage")
        seen.add(key)
        require(row["status"] == "COMPLETE" and row["target_excluded"]
                and row["xi_index"] == 3 and row["pairing_index"] == 0
                and row["witness_count"] == 0 and not row["witnesses"]
                and row["final_pair_solution_count"] == 0
                and not row["final_pair_solutions"] and not row["unresolved"],
                "complete branch terminal")
        all_lanes.extend(lanes(row))
    require(seen == expected and len(payload["rows"]) == 24, "24-row cover")
    require(sum(row["candidate_root_count"] for row in payload["rows"]) == 340
            and sum(row["source_point_count"] for row in payload["rows"]) == 472
            and sum(row["route_point_count"] for row in payload["rows"]) == 472
            and sum(row["yd_candidate_count"] for row in payload["rows"]) == 96,
            "exact census totals")
    require(len(all_lanes) == 192
            and all(item["status"] == "THIRD_PAIR_NONZERO"
                    and item["final_pair_cut"] % 2130706433
                    for item in all_lanes), "192 final lanes")
    statuses = collections.Counter(
        item["status"] for row in payload["rows"] for item in row["finite_rows"]
    )
    require(statuses == {
        "CHECKED": 296, "EMPTY_Q_BRANCH": 32,
        "MISSING_IMPOSSIBLE": 72, "TARGET_PRODUCT_BOUNDARY": 72,
    }, "finite terminal partition")
    manifest = json.loads((NODE / "node.json").read_text())
    require(manifest["node"]["id"] == NODE.name
            and manifest["node"]["status"] == "PROVED", "node manifest")
    print("PASS cell-12 reciprocal pairing 0: rows=24 candidates=340 lanes=192")


if __name__ == "__main__":
    main()
