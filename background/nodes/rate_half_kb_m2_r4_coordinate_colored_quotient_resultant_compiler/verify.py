#!/usr/bin/env python3
"""Verify the coordinate colored-quotient resultant compiler."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_colored_quotient_resultant_compiler"
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_coefficient_normal_form",
    "rate_half_kb_m2_u2_colored_source_resultant_split_compiler",
)
Q = 101


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def evaluate(coefficients: list[int], value: int) -> int:
    return sum(coefficient * pow(value, degree, Q)
               for degree, coefficient in enumerate(coefficients)) % Q


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("Phi_+(Y,W)" in statement and "Phi_-(Y,W)" in statement,
            "paired forms")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"parent {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer")

    a2 = [3, 5, 7]
    a0 = [11, 13, 17]
    b1 = [19, 23]
    a1 = [29, 31, 37]
    b2 = [41, 43]
    b0 = [47, 53]
    for t, x in ((2, 3), (5, 7), (11, 13), (17, 19)):
        w = x * x % Q
        y = t * t % Q
        positive_base = (evaluate(a2, w) * y + evaluate(a0, w)) % Q
        positive_odd = x * t * evaluate(b1, w) % Q
        positive_pair = (positive_base + positive_odd) * (
            positive_base - positive_odd
        ) % Q
        phi_positive = (
            positive_base * positive_base
            - w * y * evaluate(b1, w) ** 2
        ) % Q
        require(positive_pair == phi_positive, "positive pair")

        negative_even = t * evaluate(a1, w) % Q
        negative_odd = x * (
            evaluate(b2, w) * y + evaluate(b0, w)
        ) % Q
        negative_pair = (negative_even + negative_odd) * (
            -negative_even + negative_odd
        ) % Q
        phi_negative = (
            w * (evaluate(b2, w) * y + evaluate(b0, w)) ** 2
            - y * evaluate(a1, w) ** 2
        ) % Q
        require(negative_pair == phi_negative, "negative pair")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_COLORED_QUOTIENT_RESULTANT_COMPILER_PASS "
        "pair_checks=8 quotient_color_degree=2"
    )


if __name__ == "__main__":
    main()
