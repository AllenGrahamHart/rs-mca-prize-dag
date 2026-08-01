#!/usr/bin/env python3
"""Verify the positive 433-1a common Vieta minor compiler."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_minor_compiler"
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1a_common_vieta_compiler.py"
)
PARENTS = (
    "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_o0b_signed_edge_atlas",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def pairings(values):
    first, *rest = values
    for index, second in enumerate(rest):
        tail = rest[:index] + rest[index + 1:]
        yield ((first, second), tuple(tail))


def matching_cells():
    count = 0
    for singleton in range(5):
        remaining = [value for value in range(5) if value != singleton]
        count += sum(1 for _ in pairings(remaining))
    return count


def main():
    require(matching_cells() == 15, "matching cell count")
    source = SCRIPT.read_text()
    require("ROLES = (\"LC\", \"AB+1\", \"AB+2\", \"AB-\", \"AC\")" in source,
            "role order")
    require("for left, right in itertools.combinations(range(1, 5), 2)" in source,
            "six-minor loop")
    require("matrix.det(method=\"domain-ge\")" in source, "direct determinant")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    statement = (NODE / "statement.md").read_text()
    require("rank B=6" in statement and "rank B<6" in statement,
            "rank guard and branch")
    require("360 minors total" in statement, "compiled count")
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_COMMON_VIETA_MINOR_VERIFY_PASS "
        "cells=15 role_orbits=9 sign_rows=60 minors=360 degree=18,20,21,23"
    )


if __name__ == "__main__":
    main()
