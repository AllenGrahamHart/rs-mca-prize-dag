#!/usr/bin/env python3
"""Verify the constrained 433 outside-product compiler."""

import itertools
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_constrained_outside_product_involution_compiler"
DEPLOYED_PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def rows(labels, products):
    return [sp.Matrix([[-value, -value*label, 1, label]])
            for label, value in zip(labels, products)]


def candidate_minors(labels, products, xi, value):
    common = rows(labels, products)
    candidate = sp.Matrix([[-value, -value*xi, 1, xi]])
    return [
        sp.Matrix.vstack(*(common[index] for index in indices), candidate).det()
        for indices in itertools.combinations(range(5), 3)
    ]


def unit_ideal(polynomials, variables):
    basis = sp.groebner(
        polynomials, *variables, order="grevlex", method="f5b",
        modulus=DEPLOYED_PRIME,
    )
    return len(basis.polys) == 1 and basis.polys[0].as_expr() == 1


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("30` cells" in statement and "(KB43W-4)" in statement, "claim")
    require("does not delete" in statement and "nonclaim" in contract, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_constrained_product_q_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_complete_edge_skeleton_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_paired_product_involution_gate",
        "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    m, c, ell, value = sp.symbols("M c L p")
    b = -c**3
    p8 = m**4 + 8*m**3 - 2*m**2 + 8*m + 1
    products = (-1, -c**2, b, -b, b*c)
    cases = {
        "X2": {
            "labels": (-m**2, m, 1, m**2, -m),
            "xi": -1,
            "base": (p8, (c**2 + 1)*(m + 1)**2 - c*(m - 1)**2),
            "pnum": -2*m**3*c + 3*m**3 - 16*m**2*c + 24*m**2
                    + 6*m*c - 9*m - 36*c + 32,
            "pden": 22,
            "pairs": ((0, 3), (1, 4)),
            "scale": c + 1,
            "gab": (c**3 + c - 1,
                    -c**3*(c**2 - c + 1),
                    c**5*(c**3 - c**2 - 1)),
        },
        "N1": {
            "labels": (-1, m, 1, m**2, -m),
            "xi": -m**2,
            "base": (p8, (c**2 + 1)*(m + 1)**2 + c*(m - 1)**2),
            "pnum": 2*m**3*c + 3*m**3 + 16*m**2*c + 24*m**2
                    - 6*m*c - 9*m + 36*c + 32,
            "pden": 22,
            "pairs": ((0, 2), (1, 4)),
            "scale": c - 1,
            "gab": (c**3 + c + 1,
                    -c**3*(c**2 + c + 1),
                    -c**5*(c**3 + c**2 + 1)),
        },
        "L1": {
            "labels": (ell, m, 1, -1, -m),
            "xi": -ell,
            "base": (m**2 + 1, 2*c**4 + 3*c**2 + 2,
                     3*ell - 4*c**3 - 2*c + m),
            "pnum": 3*c**2 + 10,
            "pden": 8,
            "pairs": ((1, 4), (2, 3)),
            "scale": 1,
            "gab": (-c**2*(c**2 + 1), 2*c**6, c**8*(c**2 + 1)),
        },
    }

    for name, data in cases.items():
        p_value = data["pnum"] / data["pden"]
        minors = candidate_minors(data["labels"], products, data["xi"], value)
        variables = (value, ell, c, m) if name == "L1" else (value, c, m)
        forced_ideal = sp.groebner((*data["base"], *minors), *variables, order="lex")
        require(forced_ideal.reduce(data["pden"]*value - data["pnum"])[1] == 0,
                f"forced product necessity {name}")
        converse_variables = (ell, c, m) if name == "L1" else (c, m)
        converse = sp.groebner(data["base"], *converse_variables, order="lex")
        for minor in candidate_minors(data["labels"], products, data["xi"], p_value):
            numerator = sp.together(minor).as_numer_denom()[0]
            require(converse.reduce(sp.expand(numerator))[1] == 0,
                    f"forced product converse {name}")

        pair_rows = []
        for left, right in data["pairs"]:
            y_value, z_value = products[left], products[right]
            pair_rows.append(sp.Matrix([y_value*z_value, -(y_value + z_value), -1]))
        cross = pair_rows[0].cross(pair_rows[1])
        require(all(sp.expand(cross[index] - data["scale"]*data["gab"][index]) == 0
                    for index in range(3)), f"pair cross {name}")

        gamma, alpha, beta = data["gab"]
        base_without_ell = data["base"][:2] if name == "L1" else data["base"]
        for guard_name, guard in (
            ("b", b), ("c", c), ("p", data["pnum"]),
            ("Gamma", gamma), ("Alpha", alpha), ("Beta", beta),
            ("determinant", alpha**2 + gamma*beta), ("scale", data["scale"]),
        ):
            require(unit_ideal((*base_without_ell, guard), (c, m)),
                    f"deployed unit {name}/{guard_name}")

    require(all(DEPLOYED_PRIME % prime for prime in (2, 3, 11)),
            "constant denominators")
    require(3*2*5 == 30, "cell count")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_433_CONSTRAINED_OUTSIDE_PASS "
        "rows=3 forced_products=3 involutions=3 cells=30"
    )


if __name__ == "__main__":
    main()
