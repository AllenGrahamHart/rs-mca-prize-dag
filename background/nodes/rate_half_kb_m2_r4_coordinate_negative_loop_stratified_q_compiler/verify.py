#!/usr/bin/env python3
"""Verify the negative loop-stratified q compiler."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_loop_stratified_q_compiler"
P = 29
K = (1, 28, 4, 25, 9)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def determinant(matrix: list[list[int]]) -> int:
    if len(matrix) == 1:
        return matrix[0][0] % P
    return sum(
        (-1 if column % 2 else 1)
        * matrix[0][column]
        * determinant([row[:column] + row[column + 1:] for row in matrix[1:]])
        for column in range(len(matrix))
    ) % P


def poly_eval(poly: tuple[int, ...], value: int) -> int:
    return sum(coefficient * pow(value, degree, P) for degree, coefficient in enumerate(poly)) % P


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("(KBNQ-3)" in statement and "ell=2: 3 x 3" in statement, "claim")
    require("(3-ell)+2=5-ell" in proof, "dimension count")
    require("nonclaim" in contract and "do not exclude" in statement, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    for parent in (
        "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    # Exact two-loop survivor synthesized from A1=(W-1)(W+1), B2=1+2W.
    loops = K[:2]
    residual = K[2:]
    locator = (-1 % P, 0, 1)
    b2 = (1, 2)
    q_values = [
        -poly_eval(locator, value) * pow(poly_eval(b2, value), -1, P) % P
        for value in residual
    ]
    matrix = [
        [poly_eval(locator, value), q, q * value % P]
        for value, q in zip(residual, q_values)
    ]
    require(determinant(matrix) == 0, "two-loop determinant")
    require(all(poly_eval(b2, value) for value in K), "leading support")
    mutated = [row[:] for row in matrix]
    mutated[0][1] = (mutated[0][1] + 1) % P
    require(determinant(mutated) != 0, "mutation")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_LOOP_Q_PASS "
        f"sizes=5,4,3 two_loop_det=0 mutation={determinant(mutated)}"
    )


if __name__ == "__main__":
    main()
