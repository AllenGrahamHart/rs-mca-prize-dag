#!/usr/bin/env python3
"""Verify the exact finite classifier for one-loop 442 cells [3,6]."""

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
    "nonloop_singleton_ab_finite_classifier"
)
ROUTER_PATH = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_one_loop_442_cell36_sparse_router.py"
)
SPEC = importlib.util.spec_from_file_location("router", ROUTER_PATH)
ROUTER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ROUTER)
PRIME = ROUTER.PRIME
IOTA = ROUTER.IOTA


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def monic(expression, variables):
    return sp.Poly(expression, *variables, modulus=PRIME).monic()


def exact_quotient(expression, divisor, variables):
    quotient, remainder = sp.div(
        sp.Poly(expression, *variables, modulus=PRIME),
        sp.Poly(divisor, *variables, modulus=PRIME),
    )
    require(remainder.is_zero, "nonexact guarded division")
    return quotient.as_expr()


def compile_row(epsilon_1, epsilon_2):
    (b, c, r, t), (p_left, p_right), (q_left, q_right) = ROUTER.equations(
        epsilon_1, epsilon_2
    )
    u_value = r**2*t**2 - 3*r**2 + 3*t**2 - 1
    v_value = (r**2 - 1)*(t**2 + 1)
    a_left = sp.diff(p_left, c)
    b_left = p_left.subs(c, 0)
    require(sp.Poly(p_left, c).degree() == 1, "product linear in c")
    require(sp.Poly(
        a_left*b*(b*u_value-v_value)+b_left*(b*v_value-u_value),
        b, r, t, modulus=PRIME,
    ).is_zero, "product c reconstruction")
    require(sp.expand(
        b*(b*v_value-u_value)+(b*u_value-v_value)
        -(b**2-1)*v_value
    ) == 0, "product denominator identity")
    c_value = b*(b*u_value-v_value)/(b*v_value-u_value)

    compatibility = ROUTER.primitive(
        sp.diff(p_left, c)*p_right.subs(c, 0)
        -sp.diff(p_right, c)*p_left.subs(c, 0),
        (b, r, t),
    )
    q_left_numerator = ROUTER.primitive(q_left.subs(c, c_value), (b, r, t))
    q_right_numerator = ROUTER.primitive(q_right.subs(c, c_value), (b, r, t))

    h_value = (
        r**2*t + epsilon_1*IOTA*r**2
        +2*epsilon_1*IOTA*r*t + 2*r + t + epsilon_1*IOTA
    )
    q_guard = (
        b*(b-1)*(b+1)*(r-t)*(r-epsilon_1*IOTA)*(t**2+1)
    )
    quotient = exact_quotient(q_left_numerator, q_guard, (b, r, t))
    require(monic(quotient, (b, r, t)) == monic(h_value, (b, r, t)),
            "guard-stripped linear t weld")

    a_value = r**2+2*epsilon_1*IOTA*r+1
    n_value = -epsilon_1*IOTA*r**2-2*r-epsilon_1*IOTA
    require(sp.gcd(
        sp.Poly(a_value, r, modulus=PRIME),
        sp.Poly(-n_value, r, modulus=PRIME),
    ).degree() == 0, "linear t denominator branch")
    t_value = n_value/a_value

    compatibility_routed = ROUTER.primitive(
        compatibility.subs(t, t_value), (b, r)
    )
    q_right_routed = ROUTER.primitive(
        q_right_numerator.subs(t, t_value), (b, r)
    )
    routed_gcd = sp.gcd(
        sp.Poly(compatibility_routed, b, r, modulus=PRIME),
        sp.Poly(q_right_routed, b, r, modulus=PRIME),
    ).monic()
    require(routed_gcd == monic(b*(r**4-1), (b, r)),
            "routed common guard")
    product_reduced = exact_quotient(
        compatibility_routed, routed_gcd.as_expr(), (b, r)
    )
    q_reduced = exact_quotient(
        q_right_routed, routed_gcd.as_expr(), (b, r)
    )
    resultant = sp.Poly(
        sp.resultant(product_reduced, q_reduced, b), r, modulus=PRIME
    ).monic()

    label_guard = sp.Poly(
        r*(r**4-1)*n_value*a_value
        *(n_value**2-a_value**2)*(n_value**2+a_value**2)
        *(n_value**2-r**2*a_value**2)
        *(n_value**2+r**2*a_value**2),
        r, modulus=PRIME,
    )
    candidate = sp.Poly(r**2+epsilon_2*IOTA, r, modulus=PRIME).monic()
    require(sp.gcd(candidate, label_guard).degree() == 0,
            "candidate meets routed label guard")
    saturated = resultant
    while True:
        common = sp.gcd(saturated, label_guard)
        if common.degree() == 0:
            break
        saturated = saturated.exquo(common)
    require(saturated.monic() == (candidate*candidate).monic(),
            "saturated b-resultant")

    candidate_factors = sp.factor_list(candidate.as_expr(), modulus=PRIME)[1]
    require(len(candidate_factors) == 2
            and all(sp.Poly(factor, r, modulus=PRIME).degree() == 1
                    for factor, _ in candidate_factors),
            "deployed candidate roots")
    expected_b = sp.Poly(2*b**2+3*b+2, b, modulus=PRIME).monic()
    b_factors = sp.factor_list(expected_b.as_expr(), modulus=PRIME)[1]
    require(len(b_factors) == 2
            and all(sp.Poly(factor, b, modulus=PRIME).degree() == 1
                    for factor, _ in b_factors),
            "deployed b roots")

    witnesses = []
    for r_factor, _ in candidate_factors:
        r_coeff, r_constant = sp.Poly(
            r_factor, r, modulus=PRIME
        ).all_coeffs()
        r_root = int(-r_constant*r_coeff**-1) % PRIME
        b_gcd = sp.gcd(
            sp.Poly(product_reduced.subs(r, r_root), b, modulus=PRIME),
            sp.Poly(q_reduced.subs(r, r_root), b, modulus=PRIME),
        ).monic()
        require(b_gcd == expected_b, "candidate b gcd")
        for b_factor, _ in b_factors:
            b_coeff, b_constant = sp.Poly(
                b_factor, b, modulus=PRIME
            ).all_coeffs()
            b_root = int(-b_constant*b_coeff**-1) % PRIME
            t_root = ROUTER.evaluate_mod(t_value, {r: r_root})
            c_root = ROUTER.evaluate_mod(
                c_value, {r: r_root, t: t_root, b: b_root}
            )
            substitutions = {r: r_root, b: b_root, t: t_root, c: c_root}
            require(all(
                ROUTER.evaluate_mod(equation, substitutions) == 0
                for equation in (p_left, p_right, q_left, q_right)
            ), "original common equations")
            labels = (1, t_root**2 % PRIME, PRIME-1,
                      r_root**2 % PRIME, -(r_root**2) % PRIME)
            products = (-(b_root**2) % PRIME, b_root, -b_root % PRIME,
                        c_root, -c_root % PRIME)
            require(0 not in labels and len(set(labels)) == 5,
                    "source-label guards")
            require(0 not in products and len(set(products)) == 5,
                    "common-product guards")
            witnesses.append((r_root, b_root, t_root, c_root))
    require(len(set(witnesses)) == 4, "four exact packets")
    return witnesses


def main():
    warnings.filterwarnings("ignore", category=SymPyDeprecationWarning)
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("KB41B-3" in statement and "exactly four" in statement, "claim")
    require("not deleted" in statement and "nonclaim" in contract, "scope")

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

    rows = {
        (epsilon_1, epsilon_2): compile_row(epsilon_1, epsilon_2)
        for epsilon_1, epsilon_2 in itertools.product((1, -1), repeat=2)
    }
    require(sum(map(len, rows.values())) == 16, "sixteen-point atlas")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_AB_FINITE_PASS "
        "cells=3,6 sign_rows=4 packets=16 equations=4"
    )


if __name__ == "__main__":
    main()
