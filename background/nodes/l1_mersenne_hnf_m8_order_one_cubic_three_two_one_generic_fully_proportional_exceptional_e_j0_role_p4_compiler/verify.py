#!/usr/bin/env python3
"""Check the exceptional-E J-zero role/P4 compiler."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_j0_role_p4_compiler"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_j0_structural_consistency_compiler"
CONSUMER = "l1_mixed_petal_amplification"
Poly = dict[tuple[int, int], Fraction]


def clean(poly: Poly) -> Poly:
    return {monomial: coefficient for monomial, coefficient in poly.items() if coefficient}


def add(*polys: Poly) -> Poly:
    out: Poly = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            out[monomial] = out.get(monomial, Fraction(0)) + coefficient
    return clean(out)


def scale(poly: Poly, scalar: int | Fraction) -> Poly:
    value = Fraction(scalar)
    return clean({monomial: value * coefficient for monomial, coefficient in poly.items()})


def multiply(*polys: Poly) -> Poly:
    out: Poly = {(0, 0): Fraction(1)}
    for poly in polys:
        product: Poly = {}
        for (left_b, left_q), left_value in out.items():
            for (right_b, right_q), right_value in poly.items():
                monomial = (left_b + right_b, left_q + right_q)
                product[monomial] = product.get(monomial, Fraction(0)) + left_value * right_value
        out = clean(product)
    return out


def power(poly: Poly, exponent: int) -> Poly:
    return multiply(*(poly for _ in range(exponent))) if exponent else {(0, 0): Fraction(1)}


def degrees(poly: Poly) -> tuple[int, int]:
    return max(sum(monomial) for monomial in poly), max(q_degree for _, q_degree in poly)


def assert_bounds(poly: Poly, total: int, q_degree: int) -> None:
    actual_total, actual_q_degree = degrees(poly)
    assert actual_total <= total and actual_q_degree <= q_degree


def polynomial_check() -> None:
    one: Poly = {(0, 0): Fraction(1)}
    b: Poly = {(1, 0): Fraction(1)}
    q: Poly = {(0, 1): Fraction(1)}
    b2, q2 = power(b, 2), power(q, 2)
    x = scale(add(b, scale(one, 15)), Fraction(1, 4))
    a = scale(add(b, scale(one, 3)), Fraction(-1, 2))
    ad = add(b, scale(one, -6))
    ell = scale(add(b2, scale(b, 6), scale(one, 105), scale(q, 8)), Fraction(1, 16))
    p = add(
        scale(multiply(b, add(b2, scale(b, -6), scale(one, 27))), 40),
        scale(multiply(q, add(scale(b, 11), scale(one, 15))), 42),
    )
    d_star = add(
        scale(multiply(q, add(scale(b2, 40), scale(b, -253), scale(one, 1155))), 3),
        scale(multiply(b, add(scale(b2, 11), scale(b, 81), scale(one, 414))), -20),
    )
    d_den = scale(b, 3600)
    q0 = scale(q2, Fraction(1, 3))
    g_den = multiply(a, d_den)
    g_num = add(
        multiply(d_den, add(q0, scale(multiply(x, ell), -1), scale(one, 20), scale(q, Fraction(8, 3)))),
        d_star,
    )
    y_den = multiply(a, g_den)
    y_num = add(multiply(ell, g_den), scale(g_num, -2), scale(multiply(x, y_den), -1))
    v_den = power(y_den, 2)
    v_num = add(
        multiply(g_num, power(a, 2), g_den),
        multiply(x, y_num, y_den),
        power(y_num, 2),
    )

    role_den = power(y_den, 2)
    role_num = multiply(
        a,
        add(
            scale(power(y_num, 2), 3),
            scale(multiply(x, y_num, y_den), 2),
            multiply(g_num, power(a, 2), g_den),
        ),
    )
    s_den = power(y_den, 3)
    s_num = add(
        multiply(add(y_num, scale(multiply(a, y_den), -1)), v_num),
        scale(multiply(q0, s_den), -1),
    )

    c2, c1, c0 = 1, 2, 3
    delta = c1**2 - 4 * c2 * c0
    l_num = add(
        scale(s_num, 18 * c0),
        scale(multiply(role_num, y_den), 9 * c1),
        scale(multiply(q, ad, s_den), c0),
    )
    role_square_den = power(role_den, 2)
    r0_num = scale(multiply(q, p), -1)
    r0_factor = scale(multiply(power(a, 8), power(b, 3)), Fraction(3600**4, 2880))
    discriminant_num = add(
        multiply(q2, power(ad, 2), role_square_den),
        scale(multiply(q, r0_num, r0_factor), 144),
    )
    w_num = add(
        scale(discriminant_num, c0**2),
        scale(power(role_num, 2), -81 * delta),
    )

    assert_bounds(role_num, 9, 4)
    assert_bounds(s_num, 12, 6)
    assert_bounds(l_num, 12, 6)
    assert_bounds(w_num, 18, 8)


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    base = ROOT / "background" / "nodes" / NODE
    refs = set(nodes[NODE]["refs"])
    for name in (
        "statement.md",
        "proof.md",
        "claim_contract.md",
        "dependency_subdag.md",
        "audit.md",
        "result.md",
        "lineage.md",
        "upstream_crosswalk.md",
        "verify.py",
        "verify_audit.py",
    ):
        assert str((base / name).relative_to(ROOT)) in refs
    packet = (base / "statement.md").read_text() + (base / "proof.md").read_text()
    for marker in ("(FJR2)", "deg What_Phi<=34", "d=3(eta R_j-S_j)/q", "27Phi(R_j,S_j+qd/3)"):
        assert marker in packet


def main() -> None:
    polynomial_check()
    packet_check()
    print(
        "L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_321_EXCEPTIONAL_E_J0_ROLE_P4_COMPILER_PASS "
        "role_filters=2 max_degree=34"
    )


if __name__ == "__main__":
    main()
