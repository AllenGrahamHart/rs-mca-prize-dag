#!/usr/bin/env python3
"""Verify the diagonal fiber-resultant interpolation compiler."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_diagonal_fiber_resultant_interpolation_compiler"
Q = 101
N = 12


def inv(value: int) -> int:
    return pow(value % Q, Q - 2, Q)


def parity_check(labels: list[int]) -> list[list[int]]:
    weights = []
    for i, value in enumerate(labels):
        denominator = 1
        for j, other in enumerate(labels):
            if i != j:
                denominator = denominator * (value - other) % Q
        weights.append(inv(denominator))
    return [
        [weights[i] * pow(labels[i], degree, Q) % Q for i in range(N)]
        for degree in range(7)
    ]


def mat_vec(matrix: list[list[int]], vector: list[int]) -> list[int]:
    return [sum(a * b for a, b in zip(row, vector)) % Q for row in matrix]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("35 x 12" in statement and "whole-quadratic-fiber" in statement,
            "scope markers")
    require("need not preserve the subfield" in proof, "no false star lift")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    for parent in (
        "rate_half_kb_m2_v4_outer_recurrence_router",
        "rate_half_kb_q6_s6_common_five_outgoing_fiber_pin",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    labels = list(range(N))
    parity = parity_check(labels)
    coefficients = [
        [(7 * a + 11 * b + 3 * a * b + 5) % Q for b in range(5)]
        for a in range(5)
    ]
    scales = [(13 * p + 9) % Q or 1 for p in range(N)]
    fibers = []
    for p, value in enumerate(labels):
        row = []
        for a in range(5):
            evaluation = sum(
                coefficients[a][b] * pow(value, b, Q) for b in range(5)
            ) % Q
            row.append(evaluation * inv(scales[p]) % Q)
        fibers.append(row)

    stacked = []
    for a in range(5):
        for check in parity:
            stacked.append([check[p] * fibers[p][a] % Q for p in range(N)])
    require(len(stacked) == 35 and all(len(row) == 12 for row in stacked),
            "matrix dimensions")
    require(mat_vec(stacked, scales) == [0] * 35, "full-support kernel")
    require(all(scales), "kernel support")
    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_FIBER_RESULTANT_INTERPOLATION_COMPILER_PASS "
        f"rows={len(stacked)} cols={len(stacked[0])}"
    )


if __name__ == "__main__":
    main()
