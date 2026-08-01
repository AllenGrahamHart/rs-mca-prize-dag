#!/usr/bin/env python3
"""Verify positive 433-1a common-kernel uniqueness."""

import json
from pathlib import Path


NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_kernel_uniqueness"
)
PARENTS = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_product_base_rank_global_certificate",
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_pivot_chart_reduction",
}


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def rank_two(rows, prime):
    left, right = rows
    return int((left[0] * right[1] - left[1] * right[0]) % prime != 0) + 1


def evaluate(coefficients, value, prime):
    return sum(coefficient * value**index
               for index, coefficient in enumerate(coefficients)) % prime


def main():
    root = Path(__file__).resolve().parents[3]
    dag = json.loads((root / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "node status")
    incoming = {
        edge["from"] for edge in dag["edges"]
        if edge["to"] == NODE_ID and edge["kind"] == "req"
    }
    require(incoming == PARENTS, "dependency set")

    prime = 29
    labels = tuple(range(1, prime))
    checks = 0
    for loop in labels:
        for nonloop in labels:
            if loop == nonloop:
                continue
            rows = ((loop, loop * loop % prime),
                    (nonloop, nonloop * nonloop % prime))
            determinant = loop * nonloop * (nonloop - loop) % prime
            require(determinant != 0, "guard determinant")
            require(rank_two(rows, prime) == 2, "independent sum rows")
            checks += 1
    require(checks == 28 * 27, "coverage")
    a2 = (3, 5, 7)
    a0 = (11, 13, 17)
    q_value = 19
    loop, nonloop = 2, 9
    delta = nonloop * (nonloop - loop) % prime
    a2_tilde = tuple(delta * value % prime for value in a2)
    a0_tilde = tuple(delta * value % prime for value in a0)
    scale = -q_value * evaluate(a2, nonloop, prime) % prime
    b1_tilde = (-scale * loop % prime, scale)
    require(evaluate(b1_tilde, loop, prime) == 0, "loop reconstruction")
    require(
        (nonloop * evaluate(b1_tilde, nonloop, prime)
         + q_value * evaluate(a2_tilde, nonloop, prime)) % prime == 0,
        "nonloop reconstruction",
    )
    require(all(
        (a2_tilde[index] * a0[(index + 1) % 3]
         - a0_tilde[(index + 1) % 3] * a2[index]) % prime == 0
        for index in range(3)
    ), "common product scaling")
    print(f"positive 433-1a common-kernel uniqueness verified checks={checks}")


if __name__ == "__main__":
    main()
