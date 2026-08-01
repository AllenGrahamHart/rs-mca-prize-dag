#!/usr/bin/env python3
"""Check branch completeness and DAG wiring for the BC-singleton classifier."""

import importlib.util
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_"
    "bc_singleton_finite_classifier"
)
ATLAS = ROOT / (
    "experiments/prize_resolution/rate_half_kb_zero_loop_433_common_atlas.py"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("atlas", ATLAS)
    atlas = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(atlas)
    for cell in (12, 13, 14):
        (t, r, c, b), equations, _, _ = atlas.compile_cell(cell, 1, 1)
        if cell == 12:
            expected = (-b + c*r**2) * (b*r**2 - c)
        elif cell == 13:
            expected = (
                b*(r - 1)**2 - c*(r + 1)**2
            ) * (
                b*(r + 1)**2 - c*(r - 1)**2
            )
        else:
            expected = (
                b*(r - 1)**2 + c*(r + 1)**2
            ) * (
                b*(r + 1)**2 + c*(r - 1)**2
            )
        actual_poly = sp.Poly(equations[0], t, r, c, b, modulus=atlas.PRIME).monic()
        expected_poly = sp.Poly(expected, t, r, c, b, modulus=atlas.PRIME).monic()
        require(actual_poly == expected_poly, f"cell {cell} branch factorization")

    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("exactly 64 packets" in statement, "full atlas census")
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate",
        "rate_half_kb_m2_r4_coordinate_negative_zero_loop_product_q_weld",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_BC_SINGLETON_CHECK_PASS "
        "cells=12,13,14 product_branches=6 full_common_atlas=64"
    )


if __name__ == "__main__":
    main()
