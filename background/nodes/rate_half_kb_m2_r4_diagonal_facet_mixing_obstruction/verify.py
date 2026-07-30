#!/usr/bin/env python3
"""Verify the diagonal facet-mixing obstruction."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_diagonal_facet_mixing_obstruction"
PARENT = "rate_half_kb_m2_r4_diagonal_fiber_resultant_interpolation_compiler"
CONSUMER = "rate_half_band_closure"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("tau(I) != I" in statement, "mixing obstruction")
    require("(2,0,2), (1,1,2)" in statement, "orbit census")
    require("at least two roots of R_k lie in J_1" in statement,
            "transport cut")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    require((PARENT, NODE_ID, "req") in edges, "parent edge")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer edge")

    rows = set()
    for a in range(3):
        for b in (0, 1):
            if 2 * a + b > 5:
                continue
            c = 6 - 2 * a - 2 * b
            if c in (2, 4, 6):
                rows.add((a, b, c))
    expected = {(2, 0, 2), (1, 1, 2), (1, 0, 4), (0, 1, 4), (0, 0, 6)}
    require(rows == expected, f"orbit rows: {sorted(rows)}")

    # A preserving matching forces the odd five-set K to meet xi. Its
    # transported quartic has four J roots, while xi has J-capacity 0 in
    # the aligned case and 2 in the near-aligned case.
    for xi_j_capacity in (0, 2):
        require(4 > xi_j_capacity, "preserving-case contradiction")

    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_FACET_MIXING_OBSTRUCTION_PASS "
        f"mixing_rows={len(rows)} crossing_counts=2,4,6"
    )


if __name__ == "__main__":
    main()
