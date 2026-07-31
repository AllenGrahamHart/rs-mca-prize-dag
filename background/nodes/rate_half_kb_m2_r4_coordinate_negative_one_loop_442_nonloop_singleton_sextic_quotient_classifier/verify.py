#!/usr/bin/env python3
"""Verify the nonloop-singleton sextic quotient classifier."""

import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_sextic_quotient_classifier"
PRIME = 2130706433
IOTA = 16711679


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def common_generators(epsilon_1, epsilon_2, b, c, r, t):
    x = r**2
    a_poly = x**2-6*x+1
    b_poly = (x+1)**2
    denominator = b*b_poly+a_poly
    c_numerator = b*(b*a_poly+b_poly)
    labels = (1, -1, x, t**2, -x)
    products = (-b**2, b, -b, c, -c)
    rows = [sp.Matrix([[-p, -p*s, 1, s]])
            for p, s in zip(products, labels)]
    product = sp.Matrix.vstack(rows[0], rows[1], rows[2], rows[3]).det()
    product_numerator = sp.together(
        product.subs(c, c_numerator/denominator)
    ).as_numer_denom()[0]
    roots = (1, epsilon_1*IOTA, r, t, epsilon_2*IOTA*r)
    q_values = tuple(root*edge_sum for root, edge_sum in zip(
        roots, (0, 1+b, 1-b, 1+c, 1-c)
    ))
    differences = tuple(products[0]-value for value in products)
    left, right, third = 1, 2, 3
    weld = (
        q_values[left]*differences[right]*differences[third]
        *(labels[third]-labels[right])
        + q_values[right]*differences[left]*differences[third]
        *(labels[left]-labels[third])
        + q_values[third]*differences[left]*differences[right]
        *(labels[right]-labels[left])
    )
    weld_numerator = sp.together(
        weld.subs(c, c_numerator/denominator)
    ).as_numer_denom()[0]
    cubic = (
        r**3+(2*epsilon_1*epsilon_2+epsilon_1*IOTA)*r**2
        +(-1-2*epsilon_2*IOTA)*r-epsilon_1*IOTA
    )
    return cubic, product_numerator, weld_numerator, denominator


def quotient_basis(generators, variables):
    return sp.groebner(
        generators, *variables, order="grevlex", method="f5b",
        modulus=PRIME,
    )


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("KB41Q-2" in statement and "KB41Q-4" in statement, "claim")
    require("does not assert" in statement and "nonclaim" in contract,
            "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_cubic_root_gate",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_degree12_gate",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    b, c, r, t = sp.symbols("b c r t")
    cubic_factors = (b**3-b**2-b-1, b**3+b**2+b-1)
    for epsilon_1 in (1, -1):
        for epsilon_2 in (1, -1):
            cubic, product, weld, _ = common_generators(
                epsilon_1, epsilon_2, b, c, r, t
            )
            for index, factor in enumerate(cubic_factors):
                basis = quotient_basis((cubic, factor, product, weld),
                                       (t, r, b))
                require(basis.is_zero_dimensional, "cubic dimension")
                require(basis.reduce(t**2+r**2)[1] == 0,
                        f"cubic collision {epsilon_1},{epsilon_2},{index}")

    # Representative sextic basis and denominator-unit replay.
    cubic, product, weld, denominator = common_generators(1, 1, b, c, r, t)
    sextic = b**6-2*b**5+7*b**4-8*b**3+7*b**2-2*b+1
    basis = quotient_basis((cubic, sextic, product, weld), (t, r, b))
    require(basis.is_zero_dimensional and len(basis.polys) == 6,
            "sextic basis")
    expected_leaders = {
        "t**0*r**1*b**2", "t**0*r**0*b**3", "t**2*r**0*b**0",
        "t**1*r**1*b**0", "t**0*r**2*b**0", "t**1*r**0*b**1",
    }
    require({str(poly.LM(order=basis.order)) for poly in basis.polys}
            == expected_leaders, "sextic leaders")

    monomials = (1, b, b**2, r, r*b, t)
    exponents = ((0, 0, 0), (0, 0, 1), (0, 0, 2),
                 (0, 1, 0), (0, 1, 1), (1, 0, 0))

    def vector(expression):
        remainder = sp.Poly(basis.reduce(expression)[1], t, r, b,
                            modulus=PRIME)
        terms = {power: int(value) % PRIME
                 for power, value in remainder.terms()}
        return [terms.get(power, 0) for power in exponents]

    matrix = sp.Matrix.hstack(*(
        sp.Matrix(vector(denominator*monomial)) for monomial in monomials
    ))
    require(int(matrix.det()) % PRIME == 2**19, "denominator determinant")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_SEXTIC_PASS "
        "cubic_rows=8 deleted=8 sextic_rank=6 denominator_norm=2^19"
    )


if __name__ == "__main__":
    main()
