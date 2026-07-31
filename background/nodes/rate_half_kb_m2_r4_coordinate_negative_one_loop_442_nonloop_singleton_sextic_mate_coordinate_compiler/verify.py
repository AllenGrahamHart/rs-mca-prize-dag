#!/usr/bin/env python3
"""Verify representative sextic c and mate coordinates."""

import importlib.util
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_sextic_mate_coordinate_compiler"
PARENT_PATH = ROOT / "background/nodes/rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_sextic_quotient_classifier/verify.py"
SPEC = importlib.util.spec_from_file_location("parent", PARENT_PATH)
PARENT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PARENT)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def quotient_data(epsilon_1, epsilon_2):
    b, c, r, t = sp.symbols("b c r t")
    cubic, product, weld, denominator = PARENT.common_generators(
        epsilon_1, epsilon_2, b, c, r, t
    )
    sextic = b**6-2*b**5+7*b**4-8*b**3+7*b**2-2*b+1
    basis = PARENT.quotient_basis(
        (cubic, sextic, product, weld), (t, r, b)
    )
    monomials = (1, b, b**2, r, r*b, t)
    exponents = ((0, 0, 0), (0, 0, 1), (0, 0, 2),
                 (0, 1, 0), (0, 1, 1), (1, 0, 0))

    def vector(expression):
        remainder = sp.Poly(basis.reduce(expression)[1], t, r, b,
                            modulus=PARENT.PRIME)
        terms = {power: int(value) % PARENT.PRIME
                 for power, value in remainder.terms()}
        return sp.Matrix([terms.get(power, 0) for power in exponents])

    def polynomial(coordinates):
        return sum(
            int(coordinates[index]) % PARENT.PRIME*monomial
            for index, monomial in enumerate(monomials)
        )

    def multiplication_matrix(expression):
        return sp.Matrix.hstack(*(
            vector(expression*monomial) for monomial in monomials
        )).applyfunc(lambda value: int(value) % PARENT.PRIME)

    return b, r, t, denominator, vector, polynomial, multiplication_matrix


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("KB41M-2" in statement and "KB41M-3" in statement, "claim")
    require("does not evaluate" in statement and "nonclaim" in contract,
            "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_sextic_quotient_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_explicit_involution_compiler",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    b, r, t, d_c, vector, polynomial, matrix = quotient_data(1, 1)
    x = r**2
    a_poly = x**2-6*x+1
    b_poly = (x+1)**2
    c_numerator = b*(b*a_poly+b_poly)
    c_coordinates = matrix(d_c).inv_mod(PARENT.PRIME)*vector(c_numerator)
    c_coordinates %= PARENT.PRIME

    inverse_2 = pow(2, -1, PARENT.PRIME)
    inverse_4 = pow(4, -1, PARENT.PRIME)
    expected_c = sp.Matrix((
        -1, 1, -inverse_2,
        (PARENT.IOTA-1)*inverse_4, 0,
        (1-PARENT.IOTA)*inverse_4,
    )).applyfunc(lambda value: int(value) % PARENT.PRIME)
    require(c_coordinates == expected_c, "c coordinates")
    c_value = polynomial(c_coordinates)

    d_m = b**3-b**2*c_value+3*b*c_value+c_value**2
    d_m_matrix = matrix(d_m)
    require(int(d_m_matrix.det()) % PARENT.PRIME == 652,
            "mate denominator norm")
    mate_numerator = -b*(b**3+3*b**2*c_value-b*c_value+c_value**2)
    mate_coordinates = (
        d_m_matrix.inv_mod(PARENT.PRIME)*vector(mate_numerator)
    ) % PARENT.PRIME
    gaussian = (
        (50, -54), (87, 54), (-126, -54),
        (30, 12), (-54, 54), (12, 30),
    )
    inverse_163 = pow(163, -1, PARENT.PRIME)
    expected_mate = sp.Matrix(tuple(
        (real+imaginary*PARENT.IOTA)*inverse_163 % PARENT.PRIME
        for real, imaginary in gaussian
    ))
    require(mate_coordinates == expected_mate, "mate coordinates")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_MATE_PASS "
        "representative_rank=6 c_norm=2^19 mate_norm=652"
    )


if __name__ == "__main__":
    main()
