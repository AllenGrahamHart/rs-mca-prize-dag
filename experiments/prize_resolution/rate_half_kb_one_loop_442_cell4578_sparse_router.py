#!/usr/bin/env python3
"""Branchwise common-K router for one-loop 442 cells [4,5,7,8]."""

import argparse
import importlib.util
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
ATLAS_PATH = ROOT / (
    "critical/nodes/rate_half_band_closure/notes/"
    "kb_one_loop_442_common_atlas.py"
)
SPEC = importlib.util.spec_from_file_location("atlas", ATLAS_PATH)
ATLAS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ATLAS)
P = ATLAS.PRIME


def primitive(expression, variables):
    numerator = sp.cancel(expression).as_numer_denom()[0]
    return sp.Poly(numerator, *variables, modulus=P).monic().as_expr()


def exact_quotient(expression, divisor, variables):
    quotient, remainder = sp.div(
        sp.Poly(expression, *variables, modulus=P),
        sp.Poly(divisor, *variables, modulus=P),
    )
    if not remainder.is_zero:
        raise RuntimeError("nonexact quotient")
    return quotient.as_expr()


def routed_data(epsilon_1, epsilon_2):
    variables, equations, _, metadata = ATLAS.compile_cell(
        4, epsilon_1, epsilon_2
    )
    t, r, c, b = variables
    p_left, p_right, q_left, q_right = equations
    a_left = sp.diff(p_left, c)
    b_left = p_left.subs(c, 0)
    a_right = sp.diff(p_right, c)
    b_right = p_right.subs(c, 0)
    compatibility = primitive(
        a_left*b_right-a_right*b_left, (b, r, t)
    )
    c_value = -b_left/a_left
    q_left_numerator = primitive(q_left.subs(c, c_value), (b, r, t))
    q_right_numerator = primitive(q_right.subs(c, c_value), (b, r, t))

    guard = b*(b-1)*(b+1)*(r-t)*(r+t)
    residual = sp.Poly(q_left_numerator, b, r, t, modulus=P)
    for factor in (b, b-1, b+1, r-t, r+t):
        divisor = sp.Poly(factor, b, r, t, modulus=P)
        while True:
            quotient, remainder = sp.div(residual, divisor)
            if not remainder.is_zero:
                break
            residual = quotient
    branches = (
        r*t+1,
        r*t-epsilon_1*ATLAS.ZETA*(r+t)-1,
    )
    expected = sp.Poly(branches[0]*branches[1], b, r, t,
                       modulus=P).monic()
    if residual.monic() != expected:
        raise RuntimeError("first q weld branch identity")
    return (
        (b, c, r, t), (p_left, p_right, q_left, q_right),
        compatibility, c_value, q_right_numerator, branches, metadata, guard,
    )


def route(epsilon_1, epsilon_2, branch_index):
    (
        (b, c, r, t), original, compatibility, c_value,
        q_right_numerator, branches, metadata, _,
    ) = routed_data(epsilon_1, epsilon_2)
    print(
        f"CELL4578_BRANCHES eps={epsilon_1},{epsilon_2} branches={branches}",
        flush=True,
    )
    branch = branches[branch_index]
    branch_polynomial = sp.Poly(branch, b, r, t, modulus=P)
    if branch_polynomial.degree(t) != 1 or branch_polynomial.degree(b) != 0:
        raise RuntimeError("branch is not linear in t over F_p(r)")
    t_coefficient = sp.diff(branch, t)
    t_constant = branch.subs(t, 0)
    t_value = -t_constant/t_coefficient
    print(
        f"CELL4578_ROUTE branch={branch_index} equation={branch} "
        f"t={sp.cancel(t_value)}",
        flush=True,
    )

    product_routed = primitive(compatibility.subs(t, t_value), (b, r))
    q_routed = primitive(q_right_numerator.subs(t, t_value), (b, r))
    common = sp.gcd(
        sp.Poly(product_routed, b, r, modulus=P),
        sp.Poly(q_routed, b, r, modulus=P),
    ).monic()
    product_reduced = exact_quotient(
        product_routed, common.as_expr(), (b, r)
    )
    q_reduced = exact_quotient(q_routed, common.as_expr(), (b, r))
    resultant = sp.Poly(
        sp.resultant(product_reduced, q_reduced, b), r, modulus=P
    ).monic()
    print(f"common_gcd={common.as_expr()}", flush=True)
    print(
        f"routed_terms={len(sp.Poly(product_reduced,b,r,modulus=P).terms())},"
        f"{len(sp.Poly(q_reduced,b,r,modulus=P).terms())}",
        flush=True,
    )
    print(
        f"resultant_factors={sp.factor_list(resultant.as_expr(),modulus=P)[1]}",
        flush=True,
    )

    # Preserve exact candidate witnesses for later guard routing.
    _, _, labels, products, _ = metadata
    for factor, _ in sp.factor_list(resultant.as_expr(), modulus=P)[1]:
        polynomial = sp.Poly(factor, r, modulus=P)
        if polynomial.degree() != 1:
            continue
        coefficient, constant = polynomial.all_coeffs()
        r_root = int(-constant*coefficient**-1) % P
        product_at_root = sp.Poly(
            product_reduced.subs(r, r_root), b, modulus=P
        )
        q_at_root = sp.Poly(q_reduced.subs(r, r_root), b, modulus=P)
        b_gcd = sp.gcd(product_at_root, q_at_root).monic()
        print(f"linear_root={r_root} b_gcd={b_gcd.as_expr()}", flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--epsilon-1", type=int, choices=(-1, 1), required=True)
    parser.add_argument("--epsilon-2", type=int, choices=(-1, 1), required=True)
    parser.add_argument("--branch", type=int, choices=(0, 1), required=True)
    arguments = parser.parse_args()
    route(arguments.epsilon_1, arguments.epsilon_2, arguments.branch)


if __name__ == "__main__":
    main()
