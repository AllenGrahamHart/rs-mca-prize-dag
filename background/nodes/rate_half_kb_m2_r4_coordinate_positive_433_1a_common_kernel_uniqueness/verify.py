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
    print(f"positive 433-1a common-kernel uniqueness verified checks={checks}")


if __name__ == "__main__":
    main()
