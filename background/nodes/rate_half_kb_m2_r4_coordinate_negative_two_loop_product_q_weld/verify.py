#!/usr/bin/env python3
"""Verify the negative two-loop product-to-q weld."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_two_loop_product_q_weld"
P = 29
K = (1, 28, 4, 25, 9)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def evaluate(poly: tuple[int, ...], value: int) -> int:
    return sum(coefficient * pow(value, degree, P) for degree, coefficient in enumerate(poly)) % P


def rank_mod(rows: list[list[int]]) -> int:
    matrix = [[value % P for value in row] for row in rows]
    pivot_row = 0
    for column in range(len(matrix[0])):
        pivot = next((row for row in range(pivot_row, len(matrix)) if matrix[row][column]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        inverse = pow(matrix[pivot_row][column], -1, P)
        matrix[pivot_row] = [value * inverse % P for value in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row == pivot_row:
                continue
            scale = matrix[row][column]
            if scale:
                matrix[row] = [
                    (left - scale * right) % P
                    for left, right in zip(matrix[row], matrix[pivot_row])
                ]
        pivot_row += 1
    return pivot_row


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("(KBNW-2)" in statement and "necessary and sufficient" in statement, "claim")
    require("p_r-p_s=Delta(r-s)/(D(r)D(s))" in proof, "difference identity")
    require("nonclaim" in contract and "does not prove" in statement, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_loop_stratified_q_compiler",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    # Synthesize an exact two-loop packet over F_29.
    numerator = (2, 3)
    denominator = (1, 2)
    products = [
        evaluate(numerator, value) * pow(evaluate(denominator, value), -1, P) % P
        for value in K
    ]
    require(len(set(products)) == 5, "injective products")
    product_rows = [
        [-product, -product * value, 1, value]
        for value, product in zip(K, products)
    ]
    require(rank_mod(product_rows) == 3, "rank-three product map")
    require(all(evaluate(denominator, value) for value in K), "leading support")

    loop_a, loop_b = K[:2]
    nonloops = K[2:]
    scalar = 7

    def locator(value: int) -> int:
        return (value - loop_a) * (value - loop_b) % P

    q_values = {
        value: -scalar * locator(value) * pow(evaluate(denominator, value), -1, P) % P
        for value in nonloops
    }

    def weld(i: int, j: int, q: dict[int, int]) -> int:
        h = loop_a
        left = q[i] * locator(j) * (h - i) * (products[0] - products[K.index(j)])
        right = q[j] * locator(i) * (h - j) * (products[0] - products[K.index(i)])
        return (left - right) % P

    residuals = [weld(nonloops[0], value, q_values) for value in nonloops[1:]]
    require(residuals == [0, 0], "two welds")
    recovered = {
        -q_values[value] * evaluate(denominator, value) * pow(locator(value), -1, P) % P
        for value in nonloops
    }
    require(recovered == {scalar}, "common scalar")
    mutated = dict(q_values)
    mutated[nonloops[-1]] = (mutated[nonloops[-1]] + 1) % P
    mutation = weld(nonloops[0], nonloops[-1], mutated)
    require(mutation != 0, "mutation")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_WELD_PASS "
        f"product_rank=3 welds=0,0 scalar={scalar} mutation={mutation}"
    )


if __name__ == "__main__":
    main()
