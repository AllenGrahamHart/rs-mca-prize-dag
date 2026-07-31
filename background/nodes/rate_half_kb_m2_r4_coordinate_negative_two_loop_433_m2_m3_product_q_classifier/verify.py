#!/usr/bin/env python3
"""Verify the 433 M2/M3 product-q classifier."""

import itertools
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_m2_m3_product_q_classifier"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def maximal_minors(labels, products):
    rows = [[-p, -p*k, 1, k] for k, p in zip(labels, products)]
    return rows, [sp.expand(sp.det(sp.Matrix([rows[i] for i in indices])))
                  for indices in itertools.combinations(range(5), 4)]


def cofactor_vector(rows, indices):
    matrix = sp.Matrix([rows[i] for i in indices])
    return [sp.expand((-1)**j * matrix[:, [i for i in range(4) if i != j]].det())
            for j in range(4)]


def dot(left, right):
    return sp.expand(sum(x*y for x, y in zip(left, right)))


def modp(value, prime):
    return int(value) % prime


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("aggregate geometric cap 48" in contract, "claim")
    require("maximal-cofactor" in proof and "nonclaim" in contract, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_product_q_weld",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_product_minor_cell_cut",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_constrained_product_q_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_m1_product_q_exclusion",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    m, b, c, z = sp.symbols("m b c z")
    u = m**4 + 6*m**2 + 1
    v = (m**2 - 1)**2
    p6 = m**6 + 2*m**5 + 7*m**4 - 4*m**3 + 7*m**2 + 2*m + 1
    a = 2*m**5 + 3*m**4 + 12*m**3 - 14*m**2 + 18*m + 3
    d = 2*m**5 + 5*m**4 + 16*m**3 - 2*m**2 + 6*m + 5
    e = a - 8
    p4 = m**4 + m**3 + 4*m**2 + m + 1
    p4_prime = m**4 + 2*m**3 + 10*m**2 + 2*m + 1
    products = (-1, -c**2, b, -b, b*c)

    witnesses = {-1: (41, 11, 10, 39), 1: (41, 11, 4, 21)}
    for epsilon in (-1, 1):
        cell = "M2" if epsilon == -1 else "M3"
        labels = ((-1, m, 1, m**2, -m**2) if epsilon == -1
                  else (-m**2, m, 1, m**2, -1))
        rows, minors = maximal_minors(labels, products)
        cofactors = cofactor_vector(rows, (0, 2, 3))

        sign = 1 if epsilon == -1 else -1
        e1 = sp.expand(u*(b*c+1) + sign*v*(b+c))
        e2 = sp.expand((m+1)**2*(b**2-c**2) + sign*(m-1)**2*b*(1-c**2))
        q = sp.expand((4*m**2 if epsilon == -1 else (m**2+1)**2)*(c**2+b)**2
                      + c**2*(1+b)**2*v)
        c_factor = m*(m-1) if epsilon == 1 else m-1
        require(sp.expand(dot(rows[1], cofactors)-c_factor*e2) == 0,
                f"{cell} C cofactor")
        require(sp.expand(dot(rows[4], cofactors)+b*e1) == 0,
                f"{cell} BC cofactor")
        base = sp.Matrix([rows[i] for i in (0, 2, 3)])
        base_minors = [sp.expand(base[:, columns].det())
                       for columns in itertools.combinations(range(4), 3)]
        rank_guard = m*b*(b-1)*(b+1)*(m-1)*(m+1)*(m**2+1)
        rank_drop = sp.groebner((*base_minors, z*rank_guard-1), z, b, m,
                                order="lex")
        require(len(rank_drop.polys) == 1 and rank_drop.polys[0].as_expr() == 1,
                f"{cell} guarded base rank")

        ideal = sp.groebner((e1, e2, q), c, b, m, order="lex")
        require(ideal.domain == sp.ZZ, f"{cell} ideal domain")
        if epsilon == -1:
            eliminant = m**2*(b+1)*(m**2+1)**3*u**2*p4*p6
            branches = ((u, b*(b+1)), (p4, (b+1)**2))
        else:
            eliminant = m*(b+1)*(m**2+1)**3*(m**4+1)*u**2*p4_prime*p6
            branches = ((m**4+1, (b-1)*(b+1)), (u, b*(b+1)),
                        (p4_prime, (b+1)**2))
        require(ideal.reduce(sp.expand(eliminant))[1] == 0, f"{cell} eliminant")
        for branch, collision in branches:
            branch_ideal = sp.groebner((e1, e2, q, branch), c, b, m, order="lex")
            require(branch_ideal.domain == sp.ZZ, f"{cell} branch domain")
            require(branch_ideal.reduce(collision)[1] == 0, f"{cell} branch collision")

        b_poly = 4*b**2 + epsilon*a*b + 4
        c_poly = 8*c + b*d + epsilon*e
        p6_ideal = sp.groebner((e1, e2, q, p6), c, b, m, order="lex")
        require(p6_ideal.reduce(sp.expand((b+1)*b_poly))[1] == 0,
                f"{cell} quadratic necessity")
        require(p6_ideal.reduce(sp.expand((b+1)*c_poly))[1] == 0,
                f"{cell} locator necessity")
        converse = sp.groebner((p6, b_poly, c_poly), c, b, m, order="lex")
        require(converse.domain == sp.ZZ, f"{cell} converse domain")
        require(all(converse.reduce(value)[1] == 0 for value in (*minors, q)),
                f"{cell} full converse")

        prime, mw, bw, cw = witnesses[epsilon]
        substitution = {m: mw, b: bw, c: cw}
        label_values = [modp(sp.sympify(value).subs(substitution), prime) for value in labels]
        product_values = [modp(sp.sympify(value).subs(substitution), prime) for value in products]
        require(len(set(label_values)) == 5, f"{cell} witness labels")
        require(len(set(product_values)) == 5, f"{cell} witness products")
        require(all(modp(poly.subs(substitution), prime) == 0
                    for poly in (p6, b_poly, c_poly, q, *minors)),
                f"{cell} witness equations")
        witness_base = sp.Matrix([[sp.sympify(entry).subs(substitution) for entry in rows[i]]
                                  for i in (0, 2, 3)])
        witness_three_minors = [witness_base[:, columns].det()
                                for columns in itertools.combinations(range(4), 3)]
        require(any(modp(value, prime) != 0 for value in witness_three_minors),
                f"{cell} witness rank")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_433_M2_M3_PASS "
        "cells=M2,M3 shared=P6 per_cell_cap=12 aggregate_433_cap=48"
    )


if __name__ == "__main__":
    main()
