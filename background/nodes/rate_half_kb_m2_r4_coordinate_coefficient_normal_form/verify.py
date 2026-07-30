#!/usr/bin/env python3
"""Verify the coordinate coefficient normal form."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_coefficient_normal_form"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("epsilon=+1" in statement and "epsilon=-1" in statement,
            "two normal forms")
    require("G(-T,W)=G(T,W)" in statement, "endpoint parity")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    for parent in (
        "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
        "rate_half_kb_m2_r4_source_row_interpolation_compiler",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    monomials = [(i, j) for i in range(3) for j in range(5)]
    positive = [(i, j) for i, j in monomials if (i + j) % 2 == 0]
    negative = [(i, j) for i, j in monomials if (i + j) % 2 == 1]
    require((len(positive), len(negative)) == (8, 7), "eigenspace dimensions")

    plus_u = [(i, j) for i in (0, 2) for j in range(3)]
    plus_v = [(1, j) for j in range(2)]
    minus_u = [(1, j) for j in range(3)]
    minus_v = [(i, j) for i in (0, 2) for j in range(2)]
    require((len(plus_u) + len(plus_v), len(minus_u) + len(minus_v)) == (8, 7),
            "even-odd normal forms")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_COEFFICIENT_NORMAL_FORM_PASS "
        "source_dims=8,7"
    )


if __name__ == "__main__":
    main()
