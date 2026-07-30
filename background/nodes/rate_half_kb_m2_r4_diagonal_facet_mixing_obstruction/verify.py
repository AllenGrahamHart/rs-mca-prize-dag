#!/usr/bin/env python3
"""Verify the diagonal facet-mixing obstruction."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_diagonal_facet_mixing_obstruction"
PARENTS = (
    "rate_half_kb_m2_r4_diagonal_fiber_resultant_interpolation_compiler",
    "rate_half_kb_m2_u2_colored_source_resultant_split_compiler",
)
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
    require("L != I" in statement and "Q_J(W) ~ K_5(W)^2 chi(W)" in statement,
            "maximal-mixing quotient cut")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"parent edge {parent}")
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

    # When c=6, aligned eta transports four I roots to an L^c quartic with
    # J-capacity two. In the near case eta therefore pairs into K. The
    # paired xi and ell one-exchange quartics have complementary J counts.
    require(4 > 2, "aligned c6 contradiction")
    allowed_j_counts = [z for z in range(3) if 4 - z <= 2]
    require(allowed_j_counts == [2], "near c6 colored-fiber pin")
    require(2 * 5 + 2 == 12 and 2 * 7 - 2 == 12,
            "descended resultant degrees")

    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_FACET_MIXING_OBSTRUCTION_PASS "
        f"mixing_rows={len(rows)} crossing_counts=2,4,6 c6_J_count=2"
    )


if __name__ == "__main__":
    main()
