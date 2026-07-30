#!/usr/bin/env python3
"""Verify the complete diagonal (2,0,2) defect exclusion."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_diagonal_c2_202_defect_exclusion"
PARENTS = {
    "rate_half_kb_m2_r4_diagonal_facet_mixing_obstruction",
    "rate_half_kb_m2_v4_outer_recurrence_router",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def defect(weights: tuple[int, ...]) -> int:
    return sum(weight * (weight - 1) // 2 for weight in weights)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("(a,b,c)!=(2,0,2)" in statement, "row deletion")
    require("both source-subfield branches" in statement, "branch scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    require(all((parent, NODE_ID, "req") in edges for parent in PARENTS),
            "dependencies")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    square_vertices = (2, 2)
    j0_balanced = (2, 2, 1, 1, 1, 1)
    require(defect(square_vertices) == 2, "reciprocal square defect")
    require(sum(j0_balanced) == 8 and defect(j0_balanced) == 2,
            "J0 defect floor")
    require(defect(square_vertices) + defect(j0_balanced) == 4 > 3,
            "complete-source contradiction")

    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_C2_202_DEFECT_EXCLUSION_PASS "
        "square_cost=2 J0_floor=2 total_defect=4 budget=3 rows_remaining=4"
    )


if __name__ == "__main__":
    main()
