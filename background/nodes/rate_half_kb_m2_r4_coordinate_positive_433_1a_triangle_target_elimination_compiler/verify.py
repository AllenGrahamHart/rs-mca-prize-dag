#!/usr/bin/env python3
"""Verify the positive 433-1a triangle target-elimination compiler."""

import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "triangle_target_elimination_compiler"
)
PARENT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "quadratic_paired_product_resultant_interface"
)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    b, c, d, e, f = sp.symbols("b c d e f", nonzero=True)
    x = e * f

    y_a = d * e
    z_a = -d * f
    type_a = sp.factor(
        (d + e) ** 2 + y_a * (z_a - x) ** 2 / (x * z_a)
    )
    require(type_a == 0, "template A sum identity")
    require(sp.expand((c * f) * (b * e) - b * c * x) == 0,
            "template A product chain")
    require(sp.expand(b * (d * e) * (c * f)
                      - c * (d * f) * (b * e)) == 0,
            "template A cross relation")

    y_b = d * e
    z_b = c * f
    type_b = sp.factor(
        (d + e) ** 2 * c**2 * x**2 * z_b**2
        - (y_b * z_b**2 + c**2 * x**2) ** 2
    )
    require(type_b == 0, "template B sum identity")
    require(sp.expand(b * (d * e) * (c * f)
                      - c * (d * f) * (b * e)) == 0,
            "template B cross relation")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "node status")
    edges = {
        (edge["from"], edge["to"], edge["kind"])
        for edge in dag["edges"]
    }
    require((PARENT, NODE_ID, "req") in edges, "dependency")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer")
    print("positive 433-1a triangle target elimination verified")


if __name__ == "__main__":
    main()
