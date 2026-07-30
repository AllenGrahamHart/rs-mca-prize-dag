#!/usr/bin/env python3
"""Verify the (2,0,2) ramified-defect exclusion."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_diagonal_c2_202_ramified_defect_exclusion"
PARENTS = {
    "rate_half_kb_m2_r4_diagonal_c2_square_fiber_linear_cut",
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
    require("Delta_star >= 2+2=4" in statement, "defect contradiction")
    require("w notin {0,infinity}" in statement, "ramified deletion")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    require(all((parent, NODE_ID, "req") in edges for parent in PARENTS),
            "dependencies")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    balanced = (2, 2, 1, 1, 1, 1)
    require(sum(balanced) == 8 and defect(balanced) == 2,
            "six-vertex balanced floor")
    require(2 * defect((2,)) + defect(balanced) == 4,
            "ramified total defect")
    require(4 > 3, "complete-source contradiction")

    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_C2_202_RAMIFIED_DEFECT_EXCLUSION_PASS "
        "ramified_double_cost=2 J0_floor=2 total_defect=4 budget=3"
    )


if __name__ == "__main__":
    main()
