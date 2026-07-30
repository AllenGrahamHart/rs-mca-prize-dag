#!/usr/bin/env python3
"""Verify the universal component-color profile cut."""

from itertools import product
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_u2_universal_component_color_profile_cut"
PARENT_ID = "rate_half_kb_m2_u2_universal_source_facet_census"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("0<=c_j<=2" in statement, "colored-degree cap")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    require((PARENT_ID, NODE_ID, "req") in edges, "parent edge")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer edge")

    profiles = sorted({
        tuple(sorted(4 - deficit for deficit in deficits))
        for deficits in product(range(3), repeat=6)
        if sum(deficits) == 4
    })
    expected = [
        (2, 2, 4, 4, 4, 4),
        (2, 3, 3, 4, 4, 4),
        (3, 3, 3, 3, 4, 4),
    ]
    require(profiles == expected, "three exact profiles")
    require(all(min(profile) >= 2 for profile in profiles),
            "every J label occurs")
    print(
        "RATE_HALF_KB_M2_U2_UNIVERSAL_COMPONENT_COLOR_PROFILE_CUT_PASS "
        f"profiles={len(profiles)}"
    )


if __name__ == "__main__":
    main()
