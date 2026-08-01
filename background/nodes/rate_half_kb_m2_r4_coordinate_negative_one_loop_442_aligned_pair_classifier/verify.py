#!/usr/bin/env python3
"""Verify the aligned-pair one-loop 442 classifier."""

import itertools
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_aligned_pair_classifier"
PRIME = 2130706433
IOTA = 16711679


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def equations(b, c, r, t):
    z = IOTA
    return (
        b**2*r**2*t**2-b**2+b*c*r**2-b*c*t**2+b*r**2-b*t**2+c*r**2*t**2-c,
        -b**2*r**2*t**2-b**2+b*c*r**2+b*c*t**2-b*r**2-b*t**2+c*r**2*t**2+c,
        b**2*r**2-z*b**2+(z-1)*b*c*r+(z-1)*b*r+c*r**2-z*c,
        -b**2*r**2-z*b**2+(z+1)*b*c*r-(z+1)*b*r+c*r**2+z*c,
    )


def unit_mod(polynomial, modulus, variable):
    numerator = sp.together(polynomial).as_numer_denom()[0]
    return sp.gcd(
        sp.Poly(numerator, variable, modulus=PRIME),
        sp.Poly(modulus, variable, modulus=PRIME),
    ).degree() == 0


def all_guards(labels, products, b, c):
    guards = [b, c, b-1, b+1, c-1, c+1, b-c, b+c]
    guards.extend(labels[left]-labels[right]
                  for left, right in itertools.combinations(range(5), 2))
    guards.extend(products[left]-products[right]
                  for left, right in itertools.combinations(range(5), 2))
    return guards


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("following guarded families" in statement and "KB41A-3" in statement,
            "claim")
    require("does not delete either family" in statement and "nonclaim" in contract,
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

    b, c, r, t, u, v, w = sp.symbols("b c r t u v w")
    defining = equations(b, c, r, t)
    q_poly = b**2+b*c+c**2
    basis = sp.groebner(defining, t, r, c, b, order="grevlex",
                        method="f5b", modulus=PRIME)
    first_route = (b-1)*(b+1)*(b-c)*q_poly
    require(basis.reduce(first_route)[1] == 0, "cube factor route")

    cube_basis = sp.groebner((*defining, q_poly), t, r, c, b,
                             order="grevlex", method="f5b", modulus=PRIME)
    require(cube_basis.reduce((b*r-c)*(b+t**2))[1] == 0, "branch split")

    family_a = sp.groebner(
        (*defining, q_poly, b*r-c, u*b-1), u, t, r, c, b,
        order="grevlex", method="f5b", modulus=PRIME,
    )
    for value, name in ((b-IOTA*r, "A/b"), (r**2+r+1, "A/r"),
                        (t**2-c, "A/t")):
        require(family_a.reduce(value)[1] == 0, name)

    family_b = sp.groebner(
        (*defining, q_poly, b+t**2, u*b-1, v*(b**2-1)-1, w*(r-1)-1),
        u, v, w, t, r, c, b, order="grevlex", method="f5b", modulus=PRIME,
    )
    for value, name in ((b*r+IOTA, "B/r"), (b*c+1, "B/c"),
                        (IOTA*b**2+b-IOTA, "B/b"), (t**2+b, "B/t")):
        require(family_b.reduce(value)[1] == 0, name)

    # Converse and unit guards in the two one-variable quotient algebras.
    modulus_a = r**2+r+1
    values_a = {b: IOTA*r, c: IOTA*r**2, t**2: IOTA*r**2}
    for expression in defining:
        reduced = sp.rem(sp.Poly(sp.expand(expression.subs(values_a)), r,
                                 modulus=PRIME),
                         sp.Poly(modulus_a, r, modulus=PRIME)).as_expr()
        require(reduced == 0, "A converse")
    labels_a = (IOTA*r**2, 1, -1, r**2, -r**2)
    products_a = (-(IOTA*r)**2, IOTA*r, -IOTA*r, IOTA*r**2, -IOTA*r**2)
    require(all(unit_mod(value, modulus_a, r)
                for value in all_guards(labels_a, products_a, IOTA*r, IOTA*r**2)),
            "A guards")

    modulus_b = IOTA*b**2+b-IOTA
    c_b = -1/b
    r_b = -IOTA/b
    values_b = {c: c_b, r: r_b, t**2: -b}
    for expression in defining:
        require(unit_mod(1, modulus_b, b), "B denominator")
        numerator = sp.together(expression.subs(values_b)).as_numer_denom()[0]
        remainder = sp.rem(sp.Poly(numerator, b, modulus=PRIME),
                           sp.Poly(modulus_b, b, modulus=PRIME)).as_expr()
        require(remainder == 0, "B converse")
    labels_b = (-b, 1, -1, r_b**2, -r_b**2)
    products_b = (-b**2, b, -b, c_b, -c_b)
    require(all(unit_mod(value, modulus_b, b)
                for value in all_guards(labels_b, products_b, b, c_b)),
            "B guards")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_ALIGNED_PASS "
        "matching_orbit=1 families=2 sign_classes=4"
    )


if __name__ == "__main__":
    main()
