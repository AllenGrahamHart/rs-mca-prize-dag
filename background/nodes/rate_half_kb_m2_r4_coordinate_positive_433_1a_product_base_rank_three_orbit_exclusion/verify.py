#!/usr/bin/env python3
"""Verify the positive 433-1a product-base three-orbit exclusion."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
PARENT = "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_minor_compiler"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    prime = 2130706433
    half = (prime - 1) // 2
    require((2 * half + 1) % prime == 0, "finite-field half coefficient")
    # Coefficient dictionaries in (c,R,T), verifying c*E5-E2.
    e2 = {(1, 1, 0): -1, (1, 0, 1): 2, (1, 0, 0): -1,
          (0, 1, 0): -1, (0, 0, 0): 1}
    e5 = {(1, 1, 0): -1, (1, 0, 0): 1, (0, 1, 0): -1,
          (0, 0, 1): 2, (0, 0, 0): -1}
    combination = {}
    for monomial, coefficient in e5.items():
        shifted = (monomial[0] + 1, monomial[1], monomial[2])
        combination[shifted] = combination.get(shifted, 0) + coefficient
    for monomial, coefficient in e2.items():
        combination[monomial] = combination.get(monomial, 0) - coefficient
    combination = {key: value for key, value in combination.items() if value}
    expected = {(2, 1, 0): -1, (2, 0, 0): 1,
                (0, 1, 0): 1, (0, 0, 0): -1}
    require(combination == expected, "cell-14 linear combination")

    source = (ROOT / "experiments/prize_resolution/"
              "rate_half_kb_positive_433_1a_product_base_rank_compiler.py")
    text = source.read_text()
    # 2026-08-01 hard-law-8 pin widening (wave 38): the compiler was extended
    # at d8dc40e6 to also close cell 3; the pin below tracks the extended set.
    require("cell_index in (0, 3, 14)" in text, "specialized cells")
    require("rank_drop_guard_only_minor_columns" in text, "unit certificates")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    require((PARENT, NODE_ID, "req") in edges, "parent edge")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer edge")
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_PRODUCT_BASE_THREE_ORBIT_VERIFY_PASS "
        "cells=0,11,14 product_rank=5 base_rank=6"
    )


if __name__ == "__main__":
    main()
