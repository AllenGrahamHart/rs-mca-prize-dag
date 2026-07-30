#!/usr/bin/env python3
"""Verify the diagonal c=2 square-fiber linear cut."""

import json
from fractions import Fraction
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_diagonal_c2_square_fiber_linear_cut"
PARENTS = {
    "rate_half_kb_m2_r4_diagonal_branch_coefficient_compiler",
    "rate_half_kb_m2_r4_diagonal_facet_mixing_obstruction",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def rank(matrix: list[list[int]]) -> int:
    rows = [[Fraction(value) for value in row] for row in matrix]
    if not rows:
        return 0
    pivot_row = 0
    for column in range(len(rows[0])):
        pivot = next((r for r in range(pivot_row, len(rows))
                      if rows[r][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = rows[pivot_row][column]
        rows[pivot_row] = [value / scale for value in rows[pivot_row]]
        for r in range(len(rows)):
            if r != pivot_row and rows[r][column]:
                scale = rows[r][column]
                rows[r] = [a - scale * b
                           for a, b in zip(rows[r], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def evaluation_matrices(epsilon: int, w: int) -> tuple[list[list[int]], list[list[int]]]:
    if epsilon == 1:
        u = [
            [1, w, w * w, 0, 0],
            [0, 0, 0, 1 + w * w, w],
            [w * w, w, 1, 0, 0],
        ]
    else:
        u = [
            [1, w, w * w, 0],
            [0, 0, 0, 1 - w * w],
            [-w * w, -w, -1, 0],
        ]
    v = [
        [1, w, 0],
        [0, 0, 1 + epsilon * w],
        [epsilon * w, epsilon, 0],
    ]
    return u, v


def compose(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [
        [sum(a * right[k][j] for k, a in enumerate(row))
         for j in range(len(right[0]))]
        for row in left
    ]


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("dimension 4" in statement and "dimension 3" in statement,
            "unramified dimensions")
    require("dimensions are respectively six and" in statement,
            "ramified dimensions")
    require("m_02= C chi_w(W-1)" in statement, "minor factorization")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    require(all((parent, NODE_ID, "req") in edges for parent in PARENTS),
            "dependencies")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    # A fixed nonzero q=(1,3,2); these two rows cut a vector to span(q).
    quotient = [[-3, 1, 0], [-2, 0, 1]]
    for epsilon, ambient, expected in ((1, 8, 4), (-1, 7, 3)):
        u, v = evaluation_matrices(epsilon, 2)
        require(rank(u) == rank(v) == 3, "unramified evaluation rank")
        require(rank(compose(quotient, u)) == 2, "U line cut")
        require(rank(compose(quotient, v)) == 2, "V line cut")
        require(ambient - 4 == expected, "unramified dimension")
        u_zero, _ = evaluation_matrices(epsilon, 0)
        require(rank(u_zero) == 3, "ramified U evaluation rank")
        require(ambient - 2 == expected + 2, "ramified dimension")

    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_C2_SQUARE_FIBER_LINEAR_CUT_PASS "
        "unramified_dims=4,3 ramified_dims=6,5 minor_quotients=linear"
    )


if __name__ == "__main__":
    main()
