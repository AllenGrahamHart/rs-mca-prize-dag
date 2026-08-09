#!/usr/bin/env python3
"""Verify the cell-9 endpoint-role proof composition."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
COMPAT = EXP / "rate_half_kb_positive_433_1b_cell9_endpoint_replay_result.json"
GENERIC = EXP / "rate_half_kb_positive_433_1b_cell9_endpoint_residual_result.json"
BASE = EXP / "rate_half_kb_positive_433_1b_cell9_kernel_null_residual_result.json"
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_endpoint_compatibility_decomposition",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_endpoint_generic_complete_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_regularized_base_locus_complete_exclusion",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    compat = json.loads(COMPAT.read_text())
    require(len(compat["rows"]) == 8
            and all(row["generic_point_count"] == 4
                    and row["kernel_null_point_count"] == 2
                    for row in compat["rows"]), "source partition")
    generic = json.loads(GENERIC.read_text())
    require(len(generic["rows"]) == 32
            and sum(row["systems"] for row in generic["rows"]) == 1920
            and sum(row["unit_systems"] for row in generic["rows"]) == 1920,
            "generic exclusion")
    base = json.loads(BASE.read_text())
    endpoint_systems = [
        item
        for row in base["rows"]
        for item in row["rows"]
        if item["xi_index"] in (5, 6)
    ]
    require(len(endpoint_systems) == 960
            and all(item["unit"] for item in endpoint_systems),
            "base endpoint subset")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE.name in nodes and nodes[NODE.name]["status"] == "PROVED"
            and all(nodes[parent]["status"] == "PROVED" for parent in PARENTS),
            "DAG statuses")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    require(all((parent, NODE.name, "req") in edges for parent in PARENTS)
            and (NODE.name, "rate_half_band_closure", "ev") in edges,
            "DAG edges")
    print("cell=9 endpoint_labels=30 generic_unit=1920 base_endpoint_unit=960")


if __name__ == "__main__":
    main()
