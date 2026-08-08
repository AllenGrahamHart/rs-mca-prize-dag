#!/usr/bin/env python3
"""Verify complete role-cell-4 coverage across both product-rank branches."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
RANKDROP = "rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_complete_exclusion"
PARTS = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_parallel_de_complete_exclusion": {(xi, pairing) for xi in (0, 1, 2) for pairing in range(15)},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi3_xi4_complete_exclusion": {(xi, pairing) for xi in (3, 4) for pairing in range(15)},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi5_xi6_endpoint_compatibility_exclusion": {(xi, pairing) for xi in (5, 6) for pairing in range(15)},
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    manifest = json.loads((NODE / "node.json").read_text())
    dependencies = {row["from"] for row in manifest["requires"]}
    require(dependencies == {RANKDROP, *PARTS}, "exact four-parent manifest")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "proved complete cell")
    for parent in dependencies:
        require(nodes[parent]["status"] == "PROVED", f"proved {parent}")
        require((parent, NODE_ID, "req") in edges, f"required {parent}")
    require("product-rank-drop complete exclusion" in nodes[RANKDROP]["title"].lower(),
            "rank-drop parent scope")

    covered = set()
    part_sizes = []
    for parent, labels in PARTS.items():
        require(covered.isdisjoint(labels), f"disjoint {parent}")
        covered.update(labels)
        part_sizes.append(len(labels) * 16)
    expected = {(xi, pairing) for xi in range(7) for pairing in range(15)}
    require(covered == expected and len(covered) == 105, "exact 105-label cover")
    require(sorted(part_sizes) == [480, 480, 720], "supplier multiplicities")
    require(len(covered) * 4 * 4 == 1680, "principal raw census")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "band evidence edge")
    print("cell=4 complete rankdrop=empty labels=105 raw_systems=1680 overlap=0")


if __name__ == "__main__":
    main()
