#!/usr/bin/env python3
"""Verify the universal m2 u2 source-facet census."""

import json
from itertools import product
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_u2_universal_source_facet_census"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("J-J: 10" in statement and "I-J: 4" in statement, "census")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    for parent in (
        "rate_half_kb_q6_s6_common_five_outgoing_fiber_pin",
        "rate_half_kb_m2_r4_source_row_interpolation_compiler",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    profiles = sorted({
        tuple(sorted(4 - deficit for deficit in deficits))
        for deficits in product(range(5), repeat=6)
        if sum(deficits) == 4
    })
    expected = [
        (0, 4, 4, 4, 4, 4),
        (1, 3, 4, 4, 4, 4),
        (2, 2, 4, 4, 4, 4),
        (2, 3, 3, 4, 4, 4),
        (3, 3, 3, 3, 4, 4),
    ]
    require(profiles == expected, "five exhaustive profiles")
    require(all(sum(profile) == 20 for profile in profiles), "K incidence sum")
    print(
        "RATE_HALF_KB_M2_U2_UNIVERSAL_SOURCE_FACET_CENSUS_PASS "
        f"profiles={len(profiles)}"
    )


if __name__ == "__main__":
    main()
