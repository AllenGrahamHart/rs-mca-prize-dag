#!/usr/bin/env python3
"""Verify the branchwise exclusion of cells [4,5,7,8]."""

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
    "nonloop_singleton_mixed_pair_exclusion"
)
ROUTER_PATH = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_one_loop_442_cell4578_sparse_router.py"
)
SPEC = importlib.util.spec_from_file_location("router", ROUTER_PATH)
ROUTER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ROUTER)
P = ROUTER.P
IOTA = ROUTER.ATLAS.ZETA


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def monic(expression, variables):
    return sp.Poly(expression, *variables, modulus=P).monic()


def exact_quotient(expression, divisor, variables):
    quotient, remainder = sp.div(
        sp.Poly(expression, *variables, modulus=P),
        sp.Poly(divisor, *variables, modulus=P),
    )
    require(remainder.is_zero, "nonexact guard quotient")
    return quotient.as_expr()


def linear_roots(polynomial, variable):
    factors = sp.factor_list(polynomial, modulus=P)[1]
    roots = []
    for factor, multiplicity in factors:
        value = sp.Poly(factor, variable, modulus=P)
        require(value.degree() == 1 and multiplicity == 1,
                "candidate does not split simply")
        coefficient, constant = value.all_coeffs()
        roots.append(int(-constant*coefficient**-1) % P)
    require(len(roots) == 2, "candidate root count")
    return roots


def compile_row(epsilon_1, epsilon_2):
    (
        (b, c, r, t), original, compatibility, c_value,
        q_right_numerator, branches, _, _,
    ) = ROUTER.routed_data(epsilon_1, epsilon_2)
    p_left, _, _, _ = original
    a_value = r**2*t**2-1
    b_value = r**2-t**2
    expected_c = -b*(b*a_value+b_value)/(b*b_value+a_value)
    numerator = sp.together(c_value-expected_c).as_numer_denom()[0]
    require(sp.Poly(numerator, b, r, t, modulus=P).is_zero,
            "c reconstruction")
    require(sp.expand(
        b*(b*b_value+a_value)-(b*a_value+b_value)
        -(b**2-1)*b_value
    ) == 0, "c denominator identity")
    expected_branches = (
        r*t+1,
        r*t-epsilon_1*IOTA*(r+t)-1,
    )
    require(all(
        monic(left, (b, r, t)) == monic(right, (b, r, t))
        for left, right in zip(branches, expected_branches)
    ), "q branch split")

    reduced_rows = []
    for index, branch in enumerate(branches):
        t_coefficient = sp.diff(branch, t)
        t_value = -branch.subs(t, 0)/t_coefficient
        product_routed = ROUTER.primitive(
            compatibility.subs(t, t_value), (b, r)
        )
        q_routed = ROUTER.primitive(
            q_right_numerator.subs(t, t_value), (b, r)
        )
        common = sp.gcd(
            sp.Poly(product_routed, b, r, modulus=P),
            sp.Poly(q_routed, b, r, modulus=P),
        ).monic()
        if index == 0:
            expected_common = b**2*(r**2-1)**2*(r**2+1)
        else:
            expected_common = (
                b**2*(b-1)**2*r
                *(r-epsilon_1*IOTA)**5*(r+epsilon_1*IOTA)
            )
        require(common == monic(expected_common, (b, r)),
                f"common guard branch {index}")
        product_reduced = exact_quotient(
            product_routed, common.as_expr(), (b, r)
        )
        q_reduced = exact_quotient(
            q_routed, common.as_expr(), (b, r)
        )
        resultant = sp.Poly(
            sp.resultant(product_reduced, q_reduced, b),
            r, modulus=P,
        ).monic()
        if index == 0:
            expected_resultant = (
                r**2*(r**2+1)**2*(r**2-1)**3
                *(r**2+epsilon_2*IOTA)
                *(r**2-epsilon_2*IOTA)**3
            )
        else:
            expected_resultant = (
                r**2*(r+epsilon_1*IOTA)
                *(r+epsilon_1*epsilon_2)
            )
        require(resultant == monic(expected_resultant, (r,)),
                f"branch resultant {index}")
        reduced_rows.append((product_reduced, q_reduced))

    product_reduced, q_reduced = reduced_rows[0]
    expected_b = (
        (r**2+epsilon_2*IOTA, sp.Poly(b-1, b, modulus=P).monic()),
        (r**2-epsilon_2*IOTA, sp.Poly((b-1)**2, b, modulus=P).monic()),
    )
    for candidate, b_expected in expected_b:
        for r_root in linear_roots(candidate, r):
            b_gcd = sp.gcd(
                sp.Poly(product_reduced.subs(r, r_root), b, modulus=P),
                sp.Poly(q_reduced.subs(r, r_root), b, modulus=P),
            ).monic()
            require(b_gcd == b_expected, "nonlabel root forces b=1")


def main():
    warnings.filterwarnings("ignore", category=SymPyDeprecationWarning)
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("KB41M-4" in statement and "entire common" in statement, "claim")
    require("does not close" in statement and "nonclaim" in contract, "scope")

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

    for epsilon_1, epsilon_2 in itertools.product((1, -1), repeat=2):
        compile_row(epsilon_1, epsilon_2)
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_MIXED_PASS "
        "cells=4,5,7,8 sign_rows=4 branches=8 status=empty"
    )


if __name__ == "__main__":
    main()
