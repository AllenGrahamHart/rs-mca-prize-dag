#!/usr/bin/env python3
"""Verify the disjoint 30-label xi3/xi4 cell-4 assembly."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
BLOCKS = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi3_pairing0_reciprocal_square_exclusion": {(3, 0)},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi4_xi3_pairing0_transport_exclusion": {(4, 0)},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi3_pairings1_2_reciprocal_linear_exclusion": {(3, 1), (3, 2)},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi4_xi3_pairings1_2_transport_exclusion": {(4, 1), (4, 2)},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi3_xi4_pairing3_6_transport_exclusion": {(xi, pairing) for xi in (3, 4) for pairing in (3, 6)},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi3_xi4_pairing4_9_transport_exclusion": {(xi, pairing) for xi in (3, 4) for pairing in (4, 9)},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi3_xi4_pairing5_12_transport_exclusion": {(xi, pairing) for xi in (3, 4) for pairing in (5, 12)},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi3_xi4_pairing7_10_transport_exclusion": {(xi, pairing) for xi in (3, 4) for pairing in (7, 10)},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi3_xi4_pairing8_13_transport_exclusion": {(xi, pairing) for xi in (3, 4) for pairing in (8, 13)},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi3_xi4_pairing11_14_transport_exclusion": {(xi, pairing) for xi in (3, 4) for pairing in (11, 14)},
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    manifest = json.loads((NODE / "node.json").read_text())
    dependencies = {row["from"] for row in manifest["requires"]}
    require(dependencies == set(BLOCKS), "exact ten-parent manifest")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "proved assembly")

    covered = set()
    for parent, labels in BLOCKS.items():
        require(nodes[parent]["status"] == "PROVED", f"proved {parent}")
        require((parent, NODE_ID, "req") in edges, f"required {parent}")
        require(covered.isdisjoint(labels), f"disjoint {parent}")
        covered.update(labels)

    expected = {(xi, pairing) for xi in (3, 4) for pairing in range(15)}
    require(covered == expected and len(covered) == 30, "exact 30-label cover")
    require(len(covered) * 4 * 4 == 480, "raw-case multiplicity")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "band evidence edge")
    print("cell=4 xi=3,4 labels=30 matchings=15 raw_cases=480 overlap=0")


if __name__ == "__main__":
    main()
