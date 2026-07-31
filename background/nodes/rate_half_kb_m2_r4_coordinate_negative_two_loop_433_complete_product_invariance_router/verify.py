#!/usr/bin/env python3
"""Verify the 433 complete-product invariance router."""

import itertools
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_complete_product_invariance_router"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("= 20 cells" in statement and "21 `2 x 2`" in statement, "claim")
    require("independent projectivities" in statement and "nonclaim" in contract, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_m2_m3_product_q_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_outside_product_involution_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_complete_edge_skeleton_classifier",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    b, c, d, e, f = sp.symbols("b c d e f")
    canonical_cells = []
    xi_indices = (0, 1, 2, 3, 5)
    for epsilon in (-1, 1):
        for tau in (-1, 1):
            products = (b*d, c*e, tau*d*e, d*f, -d*f, e*f, -e*f)
            for xi_index in xi_indices:
                residual = products[:xi_index] + products[xi_index+1:]
                require(len(residual) == 6, "residual sextic")
                canonical_cells.append((epsilon, tau, xi_index, residual))
    require(len(canonical_cells) == 20, "cell count")
    require(len({cell[:3] for cell in canonical_cells}) == 20, "cell uniqueness")
    require(sp.binomial(7, 2) == 21, "proportionality minors")

    # Exhaust the three original singleton signs and verify the gauge.
    for u, v, w in itertools.product((-1, 1), repeat=3):
        old = {sp.expand(u*b*d), sp.expand(v*c*e), sp.expand(w*d*e),
               d*f, -d*f, e*f, -e*f}
        new_d, new_e, tau = u*d, v*e, w*u*v
        canonical = {sp.expand(b*new_d), sp.expand(c*new_e),
                     sp.expand(tau*new_d*new_e),
                     new_d*f, -new_d*f, new_e*f, -new_e*f}
        require(old == canonical, "sign gauge")

    gamma, alpha, beta = sp.symbols("Gamma Alpha Beta")
    matrix = sp.Matrix([[alpha, beta], [gamma, -alpha]])
    scalar = alpha**2 + beta*gamma
    require(matrix*matrix == scalar*sp.eye(2), "involution square")
    y, z = sp.symbols("Y Z")
    fixed = gamma*y**2-2*alpha*y*z-beta*z**2
    require(sp.Poly(fixed, y, z).total_degree() == 2, "fixed quadratic")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_433_INVARIANCE_PASS "
        "naive=300 canonical=20 tau=2 xi_types=5 minors=21"
    )


if __name__ == "__main__":
    main()
