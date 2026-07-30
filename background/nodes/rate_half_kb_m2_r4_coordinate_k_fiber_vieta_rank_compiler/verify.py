#!/usr/bin/env python3
"""Verify the coordinate K-fiber Vieta-rank compiler."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_k_fiber_vieta_rank_compiler"
PARENT = "rate_half_kb_m2_r4_coordinate_colored_quotient_resultant_compiler"
Q = 101


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def inv(value: int) -> int:
    return pow(value % Q, Q - 2, Q)


def evaluate_binary(coefficients: list[int], u: int, v: int) -> int:
    degree = len(coefficients) - 1
    return sum(coefficient * pow(u, index, Q) * pow(v, degree - index, Q)
               for index, coefficient in enumerate(coefficients)) % Q


def rank(matrix: list[list[int]]) -> int:
    work = [[entry % Q for entry in row] for row in matrix]
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next((row for row in range(pivot_row, len(work))
                      if work[row][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = inv(work[pivot_row][column])
        work[pivot_row] = [(entry * scale) % Q
                           for entry in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row or not work[row][column]:
                continue
            scale = work[row][column]
            work[row] = [
                (left - scale * right) % Q
                for left, right in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def positive_matrix(kappas: list[tuple[int, int]], products: list[int],
                    sums: list[int]) -> list[list[int]]:
    rows = []
    for (u, v), product, deck_sum in zip(kappas, products, sums):
        v2 = [v * v % Q, u * v % Q, u * u % Q]
        rows.append([(-product * value) % Q for value in v2]
                    + v2 + [0, 0])
        rows.append([(deck_sum * value) % Q for value in v2]
                    + [0, 0, 0, u * v * v % Q, u * u * v % Q])
    return rows


def negative_matrix(kappas: list[tuple[int, int]], products: list[int],
                    sums: list[int]) -> list[list[int]]:
    rows = []
    for (u, v), product, deck_sum in zip(kappas, products, sums):
        v1 = [v, u]
        v2 = [v * v % Q, u * v % Q, u * u % Q]
        rows.append([(-product * value) % Q for value in v1]
                    + v1 + [0, 0, 0])
        rows.append([(deck_sum * value) % Q for value in v1]
                    + [0, 0] + v2)
    return rows


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("10 x 8" in statement and "10 x 7" in statement,
            "matrix dimensions")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    require((PARENT, NODE_ID, "req") in edges, "parent")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer")

    positive_kappas = [(0, 1), (1, 0), (1, 1), (4, 1), (9, 1)]
    a2, a0, b1 = [3, 5, 7], [11, 13, 17], [19, 23]
    positive_products = []
    positive_sums = []
    for u, v in positive_kappas:
        lead = evaluate_binary(a2, u, v)
        require(lead != 0, "positive leading support")
        positive_products.append(
            evaluate_binary(a0, u, v) * inv(lead) % Q
        )
        positive_sums.append(
            -u * v * evaluate_binary(b1, u, v) * inv(lead) % Q
        )
    require(rank(positive_matrix(positive_kappas, positive_products,
                                 positive_sums)) <= 7,
            "positive kernel")
    positive_q_rows = [
        [deck_sum * v * v % Q, deck_sum * u * v % Q,
         deck_sum * u * u % Q, u * v * v % Q, u * u * v % Q]
        for (u, v), deck_sum in zip(positive_kappas, positive_sums)
    ]
    require(rank(positive_q_rows) <= 4, "positive determinant")

    negative_kappas = [(1, 1), (4, 1), (9, 1), (16, 1), (25, 1)]
    b2, b0, a1 = [3, 5], [7, 11], [13, 17, 19]
    negative_products = []
    negative_sums = []
    for u, v in negative_kappas:
        lead = evaluate_binary(b2, u, v)
        require(lead != 0, "negative leading support")
        negative_products.append(
            evaluate_binary(b0, u, v) * inv(lead) % Q
        )
        negative_sums.append(-evaluate_binary(a1, u, v) * inv(lead) % Q)
    require(rank(negative_matrix(negative_kappas, negative_products,
                                 negative_sums)) <= 6,
            "negative kernel")
    negative_p_rows = [
        [-product * v % Q, -product * u % Q, v, u]
        for (u, v), product in zip(negative_kappas, negative_products)
    ]
    negative_q_rows = [
        [deck_sum * v % Q, deck_sum * u % Q, v * v % Q,
         u * v % Q, u * u % Q]
        for (u, v), deck_sum in zip(negative_kappas, negative_sums)
    ]
    require(rank(negative_p_rows) <= 3, "negative product rank")
    require(rank(negative_q_rows) <= 4, "negative determinant")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_K_FIBER_VIETA_RANK_COMPILER_PASS "
        "fibers=5 positive_rows=10 negative_rows=10 ramified_positive=2"
    )


if __name__ == "__main__":
    main()
