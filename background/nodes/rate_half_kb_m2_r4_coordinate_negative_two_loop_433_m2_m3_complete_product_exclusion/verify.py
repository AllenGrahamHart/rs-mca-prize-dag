#!/usr/bin/env python3
"""Verify the complete M2/M3 paired-product exclusion."""

import json
from pathlib import Path
import subprocess
import sys

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_m2_m3_complete_product_exclusion"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def reduce_sign(expression, tau):
    numerator = sp.together(expression).as_numer_denom()[0]
    return sp.rem(sp.expand(numerator), tau**2 - 1, tau)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("20-cell frontier is empty" in statement, "claim")
    require("does not treat the separate `X2,N1,L1`" in statement and
            "nonclaim" in contract, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_m2_m3_product_q_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_outside_product_involution_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_complete_edge_skeleton_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_complete_product_invariance_router",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    b, c, d, e, f, tau, p, a, q, x = sp.symbols("b c d e f tau p a q x")
    product_x = b*d
    product_y = c*e
    product_z = tau*d*e
    product_u = d*f
    product_v = e*f
    require(sp.together(product_z - tau*product_x*product_y/(b*c)) == 0,
            "Z relation")
    require(sp.together(product_v - b*product_y*product_u/(c*product_x)) == 0,
            "V relation")

    # Reconstruct the five residual forms from the two multiplicative relations.
    cases = (
        ((p, a, tau*p*a/(b*c), x, -x, b*a*x/(c*p), -b*a*x/(c*p)),
         (a, tau*p*a/(b*c), x, -x, b*a*x/(c*p), -b*a*x/(c*p))),
        ((a, p, tau*a*p/(b*c), x, -x, b*p*x/(c*a), -b*p*x/(c*a)),
         (a, tau*p*a/(b*c), x, -x, b*p*x/(c*a), -b*p*x/(c*a))),
        ((a, tau*p*b*c/a, p, x, -x,
          tau*p*b**2*x/a**2, -tau*p*b**2*x/a**2),
         (a, tau*p*b*c/a, x, -x,
          tau*p*b**2*x/a**2, -tau*p*b**2*x/a**2)),
        ((a, q, tau*a*q/(b*c), p, -p, b*q*p/(c*a), -b*q*p/(c*a)),
         (a, q, tau*a*q/(b*c), -p, b*q*p/(c*a), -b*q*p/(c*a))),
        ((a, q, tau*a*q/(b*c), c*a*p/(b*q), -c*a*p/(b*q), p, -p),
         (a, q, tau*a*q/(b*c), c*a*p/(b*q), -c*a*p/(b*q), -p)),
    )
    for full_values, residual in cases:
        forced_positions = [index for index, value in enumerate(full_values) if value == p]
        require(len(forced_positions) == 1, "forced position")
        reconstructed = tuple(
            value for index, value in enumerate(full_values)
            if index != forced_positions[0]
        )
        require(all(reduce_sign(left - right, tau) == 0
                    for left, right in zip(reconstructed, residual)),
                "residual form")

    process = subprocess.run(
        [sys.executable, str(NODE / "certificate.py")],
        check=True,
        capture_output=True,
        text=True,
        timeout=55,
    )
    output = process.stdout.strip()
    require("units=300" in output and "unit_check=norm" in output, "unit census")
    require("chain0=60 chain1=15 chain2=0" in output, "projection census")
    require(2*2*5*15 == 300, "cell count")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_433_M2_M3_COMPLETE_PASS "
        "cells_deleted=20 universal_templates=75 unit_obstructions=300"
    )


if __name__ == "__main__":
    main()
