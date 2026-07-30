#!/usr/bin/env python3
"""Verify the source-row interpolation compiler."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_source_row_interpolation_compiler"
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
        for degree in range(9)
    ]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("45 x 12" in statement and "full support" in statement, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    for parent in (
        "rate_half_kb_m2_v4_outer_recurrence_router",
        "rate_half_kb_q6_u2_complete_source_conic_exclusion",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    labels = list(range(N))
    parity = parity_check(labels)
    coefficients = [
        [(13 * a + 17 * b + 7 * a * b + 5) % Q for a in range(3)]
        for b in range(5)
    ]
    scales = [(19 * i + 3) % Q or 1 for i in labels]
    rows = []
    for i, value in enumerate(labels):
        rows.append([
            sum(coefficients[b][a] * pow(value, a, Q) for a in range(3))
            * inv(scales[i]) % Q
            for b in range(5)
        ])

    matrix = []
    for b in range(5):
        for check in parity:
            matrix.append([check[i] * rows[i][b] % Q for i in range(N)])
    require(len(matrix) == 45 and all(len(row) == 12 for row in matrix),
            "matrix dimensions")
    require(all(sum(row[i] * scales[i] for i in range(N)) % Q == 0
                for row in matrix), "full-support kernel")
    require(all(scales), "kernel support")
    print(
        "RATE_HALF_KB_M2_R4_SOURCE_ROW_INTERPOLATION_COMPILER_PASS "
        "rows=45 cols=12"
    )


if __name__ == "__main__":
    main()
