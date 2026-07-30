#!/usr/bin/env python3
"""Verify the ramified complete-source coefficient repair."""

import json
from fractions import Fraction as F
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_diagonal_c2_112_ramified_complete_source_repair"
PARENTS = {
    "rate_half_kb_m2_r4_diagonal_c2_112_source_line_odd_part_incidence_gate",
    "rate_half_kb_m2_r4_source_row_interpolation_compiler",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def rank(matrix):
    work = [[F(value) for value in row] for row in matrix]
    pivot = 0
    for column in range(len(work[0])):
        row = next((index for index in range(pivot, len(work))
                    if work[index][column]), None)
        if row is None:
            continue
        work[pivot], work[row] = work[row], work[pivot]
        scale = work[pivot][column]
        work[pivot] = [value / scale for value in work[pivot]]
        for index in range(len(work)):
            if index == pivot or not work[index][column]:
                continue
            scale = work[index][column]
            work[index] = [left - scale * right
                           for left, right in zip(work[index], work[pivot])]
        pivot += 1
    return pivot


def compose(left, right):
    return [[sum(a * right[k][j] for k, a in enumerate(row))
             for j in range(len(right[0]))] for row in left]


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("V(T,0) in <q> minus {0}" in statement, "ramified odd cut")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    require(all((parent, NODE_ID, "req") in edges for parent in PARENTS),
            "dependencies")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    quotient = [[3, -2, 0], [1, 0, -2]]
    for epsilon, variables, expected_dimension in ((1, 8, 4), (-1, 7, 3)):
        u = [[F(0)] * variables for _ in range(3)]
        v = [[F(0)] * variables for _ in range(3)]
        u[0][0] = 1
        u[1][3] = 1
        u[2][2] = epsilon
        offset = 5 if epsilon == 1 else 4
        v[0][offset] = 1
        v[1][offset + 2] = 1
        v[2][offset + 1] = epsilon
        cuts = compose(quotient, u) + compose(quotient, v)
        require(rank(cuts) == 4, "ramified total rank")
        require(variables - rank(cuts) == expected_dimension,
                "ramified repaired dimension")

    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_C2_112_RAMIFIED_COMPLETE_SOURCE_REPAIR_PASS "
        "row_orders=2,2 total_rank=4 dimensions=4/3 odd_part=nonzero"
    )


if __name__ == "__main__":
    main()
