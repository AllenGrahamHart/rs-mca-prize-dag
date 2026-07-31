#!/usr/bin/env python3
"""Verify the crossed-pair one-loop 442 exclusion."""

import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_crossed_pair_exclusion"
PRIME = 2130706433
IOTA = 16711679


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("entire matching orbit" in statement and "is empty" in statement,
            "claim")
    require("does not delete the aligned-pair" in statement and "nonclaim" in contract,
            "scope")
    require(IOTA*IOTA % PRIME == PRIME-1, "deployed fourth root")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_product_q_weld",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    b, c, r, t = sp.symbols("b c r t")
    z = IOTA
    equations = (
        -b**2*r**2*t**2+3*b**2*r**2-3*b**2*t**2+b**2
        +b*c*r**2*t**2+b*c*r**2-b*c*t**2-b*c+b*r**2*t**2
        +b*r**2-b*t**2-b-c*r**2*t**2+3*c*r**2-3*c*t**2+c,
        -b**2*r**4+3*b**2*r**2*t**2-3*b**2*r**2+b**2*t**2
        +b*c*r**4+b*c*r**2*t**2-b*c*r**2-b*c*t**2-b*r**4
        -b*r**2*t**2+b*r**2+b*t**2+c*r**4-3*c*r**2*t**2
        +3*c*r**2-c*t**2,
        z*b**2*r+z*b**2+b*c*r-b*c+b*r-b+z*c*r+z*c,
        -z*b**2*r-z*b**2+b*c*r-b*c-b*r+b+z*c*r+z*c,
    )
    basis = sp.groebner(equations, t, r, c, b, order="grevlex",
                        method="f5b", modulus=PRIME)
    p_value = b*(b*r+b-z*r+z)
    q_value = c*(b*(r-1)+z*(r+1))
    require(basis.reduce(p_value)[1] == 0, "first ideal consequence")
    require(basis.reduce(q_value)[1] == 0, "second ideal consequence")

    normalized_p = sp.expand(p_value/b)
    normalized_q = sp.expand(q_value/c)
    resultant = sp.Poly(sp.resultant(normalized_p, normalized_q, r),
                        b, modulus=PRIME).monic()
    expected = sp.Poly(b**2-1, b, modulus=PRIME).monic()
    require(resultant == expected, "guard resultant")
    require(PRIME % 2 != 0, "odd characteristic")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_CROSSED_PASS "
        "matching_orbits_deleted=1 cells=2 sign_classes=4"
    )


if __name__ == "__main__":
    main()
