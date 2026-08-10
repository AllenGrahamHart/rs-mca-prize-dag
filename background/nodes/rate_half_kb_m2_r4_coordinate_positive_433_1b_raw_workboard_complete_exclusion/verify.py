#!/usr/bin/env python3
"""Verify exact closure of the positive 433-1b raw workboard."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name

ROLE_GROUPS = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell0_complete_exclusion": {0},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cells1_2_complete_exclusion": {1, 2},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cells3_6_duplicate_role_complete_exclusion": {3, 6},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cells4_7_duplicate_role_complete_exclusion": {4, 7},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cells5_8_complete_exclusion": {5, 8},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cells9_10_complete_exclusion": {9, 10},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell11_complete_exclusion": {11},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cells12_13_complete_exclusion": {12, 13},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell14_fixed_a_rankone_allmixed_exclusion": {14},
}
STRUCTURAL = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_common_vieta_minor_compiler",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_complete_exclusion",
}
PARENTS = set(ROLE_GROUPS) | STRUCTURAL


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def validate(statuses, groups):
    require(set(statuses) == PARENTS, "exact parent status set")
    require(all(value == "PROVED" for value in statuses.values()),
            "all parents proved")
    require(set(groups) == set(ROLE_GROUPS), "exact role-owner set")
    cells = [cell for group in groups.values() for cell in group]
    require(len(cells) == 15, "15 role-cell incidences")
    require(set(cells) == set(range(15)), "exact role-cell cover")
    require(sorted(map(len, groups.values())) == [1, 1, 1, 2, 2, 2, 2, 2, 2],
            "nine owner-block sizes")
    require(15 * 105 == 1575 and 1575 * 16 == 25200,
            "raw label and signed-system totals")


def main():
    manifests = {
        identifier: json.loads(
            (ROOT / "background/nodes" / identifier / "node.json").read_text()
        )["node"]
        for identifier in PARENTS
    }
    validate(
        {identifier: manifest["status"] for identifier, manifest in manifests.items()},
        ROLE_GROUPS,
    )
    for identifier in PARENTS:
        require(manifests[identifier]["id"] == identifier,
                f"manifest identity {identifier}")
        require((ROOT / "background/nodes" / identifier / "verify.py").is_file(),
                f"verifier present {identifier}")

    own = json.loads((NODE / "node.json").read_text())
    require(own["node"]["status"] == "PROVED", "aggregate proved")
    require({row["from"] for row in own["requires"]} == PARENTS,
            "exact aggregate parents")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG aggregate status")
    for identifier in PARENTS:
        require((identifier, NODE_ID, "req") in edges,
                f"DAG parent edge {identifier}")
    require((NODE_ID, "rate_half_band_structural_surplus", "ev") in edges,
            "K3-arm evidence edge")
    print("PASS raw 433-1b workboard: cells=15 labels=1575 systems=25200")


if __name__ == "__main__":
    main()
