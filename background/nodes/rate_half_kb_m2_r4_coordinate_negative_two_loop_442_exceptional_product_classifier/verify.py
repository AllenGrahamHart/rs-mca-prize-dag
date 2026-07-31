#!/usr/bin/env python3
"""Verify the 442 exceptional common-K product classifier."""

import itertools
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_exceptional_product_classifier"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("(KB4P-3)" in statement and "(KB4P-5)" in statement, "six rows")
    require("at most twelve" in statement and "all five" in proof, "scope")
    require("nonclaim" in contract and "does not close" in statement, "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_antipodal_label_classifier",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    l, b, c = sp.symbols("l b c")
    cases = {
        ("H6", -1): ((l, -l**2, 1, -l, l**2), l**2 - l + 1,
                     4*b**2 + b + 4, 3*c + 2*b - 2),
        ("H6", 1): ((l, -l**2, 1, -l, l**2), l**2 - l + 1,
                    4*b**2 + 7*b + 4, c - 2*b - 2),
        ("H8L", -1): ((l, -l**2, 1, -1, l**2), l**4 + 1,
                      b**2 - b*l**3 + b*l - b + 1,
                      c - (b - 2)*(l**3 - l + 1)),
        ("H8L", 1): ((l, -l**2, 1, -1, l**2), l**4 + 1,
                     b**2 - 2*b*l**3 + 2*b*l - b + 1,
                     c + b*l**3 - b*l - b - 2),
        ("H8M", -1): ((-l**2, l, 1, l**2, -1), l**4 + 1,
                      b**2 - b*l**3 + b*l - b + 1,
                      c - (2*b - 1)*(l**3 - l + 1)),
        ("H8M", 1): ((-l**2, l, 1, l**2, -1), l**4 + 1,
                     b**2 - 2*b*l**3 + 2*b*l - b + 1,
                     c - 2*b + l**3 - l - 1),
    }

    for (name, tau), (labels, relation, b_gate, c_gate) in cases.items():
        products = (-1, -b**2, b, c, tau*b*c)
        rows = [[-p, -p*k, 1, k] for k, p in zip(labels, products)]
        minors = [
            sp.expand(sp.det(sp.Matrix([rows[index] for index in indices])))
            for indices in itertools.combinations(range(5), 4)
        ]
        ideal = sp.groebner((relation, b_gate, c_gate), c, b, l, order="lex")
        require(all(ideal.reduce(minor)[1] == 0 for minor in minors), f"converse {name}/{tau}")

        # The full determinant ideal contains the decisive quadratic after
        # removing the actual-packet factors b and b+/-1.
        determinant_ideal = sp.groebner((relation, *minors), c, b, l, order="lex")
        basis = [sp.factor(poly.as_expr()) for poly in determinant_ideal.polys]
        decisive = basis[-2]
        quotient = sp.cancel(decisive / b_gate)
        allowed_factors = sp.factor(b * (b + 1)**2) if tau == -1 else sp.factor(b * (b - 1) * (b + 1))
        require(sp.expand(quotient - allowed_factors) == 0, f"necessity {name}/{tau}")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_442_PRODUCT_PASS "
        "loci=3 signs=2 rows=6 max_packets=12 minors_per_row=5"
    )


if __name__ == "__main__":
    main()
