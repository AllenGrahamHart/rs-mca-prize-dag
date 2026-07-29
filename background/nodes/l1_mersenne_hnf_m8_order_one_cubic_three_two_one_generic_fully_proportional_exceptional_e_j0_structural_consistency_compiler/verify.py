#!/usr/bin/env python3
"""Check the exceptional-E J-zero structural compiler."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_j0_structural_consistency_compiler"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_j0_affine_router"
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
    assert actual_total <= total
    assert actual_q_degree <= q_degree


def polynomial_check() -> None:
    one: Poly = {(0, 0): Fraction(1)}
    b: Poly = {(1, 0): Fraction(1)}
    q: Poly = {(0, 1): Fraction(1)}
    b2, q2 = power(b, 2), power(q, 2)
    x = scale(add(b, scale(one, 15)), Fraction(1, 4))
    a = scale(add(b, scale(one, 3)), Fraction(-1, 2))
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
    h_num = add(multiply(ell, g_den), scale(g_num, -1))
    y_den = multiply(a, g_den)
    y_num = add(multiply(ell, g_den), scale(g_num, -2), scale(multiply(x, y_den), -1))
    v_den = power(y_den, 2)
    v_num = add(
        multiply(g_num, power(a, 2), g_den),
        multiply(x, y_num, y_den),
        power(y_num, 2),
    )

    z_d = add(
        multiply(d_star, power(a, 6), power(d_den, 2)),
        scale(multiply(y_num, v_num), -1),
    )
    r_num = scale(multiply(q, p), -1)
    r_factor = scale(multiply(power(a, 2), b), 4500)
    d_factor = multiply(power(a, 2), d_den)
    constants = add(scale(q, Fraction(23, 4)), scale(q2, Fraction(1, 8)), scale(one, 15))
    z_r = add(
        multiply(r_num, r_factor),
        scale(multiply(g_num, h_num), -1),
        multiply(add(multiply(x, q0), constants), power(g_den, 2)),
        multiply(add(a, x), d_star, d_factor),
    )

    assert_bounds(g_num, 4, 2)
    assert_bounds(y_num, 4, 2)
    assert_bounds(v_num, 8, 4)
    assert_bounds(z_d, 12, 6)
    assert_bounds(z_r, 8, 4)
    assert add(scale(x, -2), scale(one, 6)) == a


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
    for marker in ("Q_j=q^2/3", "(FJS3)", "deg_q(Z_D^j)<=6", "deg Zhat_R^j<=16"):
        assert marker in packet


def main() -> None:
    polynomial_check()
    packet_check()
    print(
        "L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_321_EXCEPTIONAL_E_J0_STRUCTURAL_COMPILER_PASS "
        "filters=2 degrees=24,16"
    )


if __name__ == "__main__":
    main()
