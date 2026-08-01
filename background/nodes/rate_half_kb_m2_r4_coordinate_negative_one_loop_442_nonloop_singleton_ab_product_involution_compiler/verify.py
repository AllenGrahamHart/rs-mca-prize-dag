#!/usr/bin/env python3
"""Verify the cells [3,6] product involution and forced outside mate."""

import importlib.util
import itertools
import json
from pathlib import Path
import warnings

import sympy as sp
from sympy.utilities.exceptions import SymPyDeprecationWarning


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_"
    "nonloop_singleton_ab_product_involution_compiler"
)
PARENT_PATH = ROOT / (
    "background/nodes/"
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_"
    "nonloop_singleton_ab_finite_classifier/verify.py"
)
SPEC = importlib.util.spec_from_file_location("parent", PARENT_PATH)
PARENT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PARENT)
PRIME = PARENT.PRIME


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    warnings.filterwarnings("ignore", category=SymPyDeprecationWarning)
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("KB41BI-5" in statement and "Phi(Y,Z)" in statement, "claim")
    require("does not enumerate" in statement and "nonclaim" in contract,
            "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_ab_finite_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_paired_product_involution_gate",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_complete_edge_skeleton_classifier",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    b, c, y, z = sp.symbols("b c y z")
    row_1 = sp.Matrix([b**3, b**2+b, -1])
    row_2 = sp.Matrix([-c**2, 0, -1])
    gamma = b*(b+1)
    alpha = -(b**3+c**2)
    beta = -b*(b+1)*c**2
    coefficients = row_1.cross(row_2)
    require(all(sp.expand(left+right) == 0 for left, right in zip(
        coefficients, (gamma, alpha, beta)
    )), "pair-row cross product")

    phi = gamma*y*z-alpha*(y+z)-beta
    require(sp.expand(phi.subs({y: -b**2, z: -b})) == 0,
            "first common pair")
    require(sp.expand(phi.subs({y: c, z: -c})) == 0,
            "second common pair")
    determinant = sp.factor(alpha**2+gamma*beta)
    require(determinant == (b-c)*(b+c)*(b**2-c)*(b**2+c),
            "nonsingularity factor")

    mate = sp.factor((alpha*b+beta)/(gamma*b-alpha))
    unsimplified = -b*(b**3+b*c**2+2*c**2)/(2*b**3+b**2+c**2)
    require(sp.simplify(mate-unsimplified) == 0, "unsimplified mate")
    require(sp.simplify(phi.subs({y: b, z: mate})) == 0,
            "mate involution equation")

    c_square = (5*b+6)/4
    b_modulus = sp.Poly(2*b**2+3*b+2, b)
    denominator = sp.rem(
        sp.Poly((gamma*b-alpha).subs(c**2, c_square), b), b_modulus
    ).as_expr()
    require(sp.expand(denominator-(9*b+14)/4) == 0,
            "mate denominator reduction")
    expected_mate = (18-5*b)/22
    comparison = sp.together(
        mate.subs(c**2, c_square)-expected_mate
    ).as_numer_denom()[0]
    require(sp.rem(sp.Poly(comparison, b), b_modulus).is_zero,
            "simplified mate")
    require(sp.resultant(2*b**2+3*b+2, 9*b+14, b) == 176,
            "denominator resultant")
    require(sp.resultant(2*b**2+3*b+2, 18-5*b, b) == 968,
            "nonzero mate resultant")
    require(sp.resultant(2*b**2+3*b+2, 18-27*b, b) == 3564,
            "nonfixed mate resultant")

    packets = []
    for epsilon_1, epsilon_2 in itertools.product((1, -1), repeat=2):
        packets.extend(PARENT.compile_row(epsilon_1, epsilon_2))
    require(len(packets) == 16, "parent packet count")
    for _, b_root, _, c_root in packets:
        require((4*c_root*c_root-5*b_root-6) % PRIME == 0,
                "common c-square relation")
        denominator_value = (
            2*b_root**3+b_root**2+c_root**2
        ) % PRIME
        require(denominator_value != 0, "finite mate")
        mate_value = (
            -b_root*(b_root**3+b_root*c_root**2+2*c_root**2)
            *pow(denominator_value, -1, PRIME)
        ) % PRIME
        expected_value = (
            (18-5*b_root)*pow(22, -1, PRIME)
        ) % PRIME
        require(mate_value == expected_value, "packet mate")
        common_products = {
            -(b_root**2) % PRIME, -b_root % PRIME,
            c_root, -c_root % PRIME, b_root,
        }
        require(mate_value != 0 and mate_value not in common_products,
                "mate guards")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_AB_INVOLUTION_PASS "
        "common_pairs=2 packets=16 forced_mates=2 outside_pairs=3"
    )


if __name__ == "__main__":
    main()
