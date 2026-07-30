#!/usr/bin/env python3
"""Verify the saturated (1,1,2) internal-star reconstruction."""

import json
from fractions import Fraction as F
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction"
PARENTS = {
    "rate_half_kb_m2_r4_diagonal_c2_112_ramified_complete_source_repair",
    "rate_half_kb_m2_r4_diagonal_c2_112_saturated_defect_classifier",
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


def evaluation(epsilon, W):
    if epsilon == 1:
        return [
            [1, W, W * W, 0, 0],
            [0, 0, 0, 1 + W * W, W],
            [W * W, W, 1, 0, 0],
        ]
    return [
        [1, W, W * W, 0],
        [0, 0, 0, 1 - W * W],
        [-W * W, -W, -1, 0],
    ]


def compose(left, right):
    return [[sum(value * right[k][column]
                 for k, value in enumerate(row))
             for column in range(len(right[0]))] for row in left]


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("at most eight projective source-deck pairs" in statement,
            "candidate bound")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    require(all((parent, NODE_ID, "req") in edges for parent in PARENTS),
            "dependencies")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    w, z = F(2), F(3)
    line_quotient = [[-3, 1, 0], [-2, 0, 1]]
    for epsilon, source_dimension, image_dimension in ((1, 3, 3), (-1, 2, 2)):
        at_w = evaluation(epsilon, w)
        at_z = evaluation(epsilon, z)
        source_cut = compose(line_quotient, at_w)
        require(len(at_w[0]) - rank(source_cut) == source_dimension,
                "forced-line source dimension")
        require(rank(source_cut + at_z) == len(at_w[0]),
                "internal evaluation injective")
        require(image_dimension == source_dimension, "image dimension")

    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_C2_112_SOURCE_LINE_INTERNAL_STAR_RECONSTRUCTION_PASS "
        "positive_map=3x3_isomorphism negative_map=2_plane candidates_per_packet<=8"
    )


if __name__ == "__main__":
    main()
