#!/usr/bin/env python3
"""Verify the disjoint 45-label parallel-DE cell-4 assembly."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
BLOCKS = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_de_firstpair_complete_exclusion": {0, 1, 2},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_de_pairing3_6_complete_exclusion": {3, 6},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_de_pairing4_9_complete_exclusion": {4, 9},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_de_pairing5_12_complete_exclusion": {5, 12},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_de_pairing7_10_complete_exclusion": {7, 10},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_de_pairing8_13_complete_exclusion": {8, 13},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_de_pairing11_14_complete_exclusion": {11, 14},
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    manifest = json.loads((NODE / "node.json").read_text())
    dependencies = {row["from"] for row in manifest["requires"]}
    require(dependencies == set(BLOCKS), "exact seven-parent manifest")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "proved assembly")

    covered = set()
    for parent, pairings in BLOCKS.items():
        require(nodes[parent]["status"] == "PROVED", f"proved {parent}")
        require((parent, NODE_ID, "req") in edges, f"required {parent}")
        parent_labels = {(xi, pairing) for xi in range(3) for pairing in pairings}
        require(covered.isdisjoint(parent_labels), f"disjoint {parent}")
        covered.update(parent_labels)

    expected = {(xi, pairing) for xi in range(3) for pairing in range(15)}
    require(covered == expected and len(covered) == 45, "exact 45-label cover")
    require(len(covered) * 4 * 4 == 720, "raw-case multiplicity")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "band evidence edge")
    print("cell=4 parallel_DE labels=45 matchings=15 raw_cases=720 overlap=0")


if __name__ == "__main__":
    main()
