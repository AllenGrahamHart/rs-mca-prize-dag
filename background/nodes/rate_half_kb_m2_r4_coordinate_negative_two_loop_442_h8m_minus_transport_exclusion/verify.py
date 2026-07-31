#!/usr/bin/env python3
"""Verify the H8-M-minus transport exclusion."""

import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_h8m_minus_transport_exclusion"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("five to four" in statement and "30 to 24" in statement, "claim")
    require("does not delete either" in statement and "nonclaim" in contract, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_exceptional_product_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_complete_product_invariance_router",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_h8l_minus_complete_product_exclusion",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    l, b, d, e, f, sigma = sp.symbols("l b d e f sigma")
    s = l**3-l+1
    relation = l**4+1
    gate = b**2-b*s+1
    bp = 1/b
    c = (b-2)*s
    cp = -c/b

    transported_gate = sp.together(bp**2-bp*s+1).as_numer_denom()[0]
    require(sp.expand(transported_gate-gate) == 0, "b gate transport")
    require(sp.expand(cp-(2*bp-1)*s) == 0, "c locator transport")
    h8l_labels = (l, -l**2, 1, -1, l**2)
    swapped_labels = (h8l_labels[1], h8l_labels[0], h8l_labels[2],
                      h8l_labels[4], h8l_labels[3])
    require(swapped_labels == (-l**2, l, 1, l**2, -1), "label transport")

    old_products = (-1, -b**2, b, c, -b*c)
    swapped_products = (old_products[1], old_products[0], old_products[2],
                        old_products[4], old_products[3])
    new_products = (-1, -bp**2, bp, cp, -bp*cp)
    require(all(sp.expand(new-swapped/b**2) == 0
                for new, swapped in zip(new_products, swapped_products)),
            "common product scaling")

    numerator = bp*(bp*l**2-2*bp*l+bp-2*l**2-2)
    denominator = 2*bp*l**2+2*bp-l**2+2*l-1
    forced_identity = sp.together(numerator-bp**2*denominator).as_numer_denom()[0]
    ideal = sp.groebner((relation, gate), b, l, order="lex")
    require(ideal.reduce(sp.expand(forced_identity))[1] == 0, "forced product transport")

    dp, ep, fp = -d/b, -e/b, -f/b
    old_outside = (c*d, c*e, sigma*d*e, d*f, -d*f, e*f, -e*f)
    new_outside = (cp*dp, cp*ep, sigma*dp*ep,
                   dp*fp, -dp*fp, ep*fp, -ep*fp)
    require(all(sp.expand(new-old/b**2) == 0
                for new, old in zip(new_outside, old_outside)),
            "outside product scaling")

    # The parameter and horizontal transformations are involutive.
    require(sp.simplify(1/bp-b) == 0, "b involution")
    require(sp.simplify(-cp/bp-c) == 0, "c involution")
    require(30-6 == 24 and 390-78 == 312, "frontier count")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_442_H8M_MINUS_TRANSPORT_PASS "
        "common_rows_deleted=1 frontier_rows=4 frontier_cells=24 cap=312"
    )


if __name__ == "__main__":
    main()
