#!/usr/bin/env python3
"""Check the exceptional-E J-zero affine polynomial compiler."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_j0_affine_router"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_coefficient_bivariate_compiler"
CONSUMER = "l1_mixed_petal_amplification"
PRIMES = (8191, 131071, 524287, 2147483647)
Poly = dict[tuple[int, int], int]


def clean(poly: Poly) -> Poly:
    return {monomial: coefficient for monomial, coefficient in poly.items() if coefficient}


def add(*polys: Poly) -> Poly:
    out: Poly = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            out[monomial] = out.get(monomial, 0) + coefficient
    return clean(out)


def scale(poly: Poly, scalar: int) -> Poly:
    return clean({monomial: scalar * coefficient for monomial, coefficient in poly.items()})


def multiply(*polys: Poly) -> Poly:
    out: Poly = {(0, 0): 1}
    for poly in polys:
        product: Poly = {}
        for (left_b, left_q), left_value in out.items():
            for (right_b, right_q), right_value in poly.items():
                monomial = (left_b + right_b, left_q + right_q)
                product[monomial] = product.get(monomial, 0) + left_value * right_value
        out = clean(product)
    return out


def power(poly: Poly, exponent: int) -> Poly:
    out: Poly = {(0, 0): 1}
    for _ in range(exponent):
        out = multiply(out, poly)
    return out


def total_degree(poly: Poly) -> int:
    return max(sum(monomial) for monomial in poly)


def clear_q(poly: Poly, q_numerator: Poly, q_denominator: Poly, degree: int) -> Poly:
    assert all(q_degree <= degree for _, q_degree in poly)
    out: Poly = {}
    for (b_degree, q_degree), coefficient in poly.items():
        term = {(b_degree, 0): coefficient}
        term = multiply(term, power(q_numerator, q_degree))
        term = multiply(term, power(q_denominator, degree - q_degree))
        out = add(out, term)
    return out


def polynomial_check() -> None:
    one: Poly = {(0, 0): 1}
    b: Poly = {(1, 0): 1}
    q: Poly = {(0, 1): 1}
    b2 = power(b, 2)
    q2 = power(q, 2)
    p = add(
        scale(multiply(b, add(b2, scale(b, -6), scale(one, 27))), 40),
        scale(multiply(q, add(scale(b, 11), scale(one, 15))), 42),
    )
    d_star = add(
        scale(multiply(q, add(scale(b2, 40), scale(b, -253), scale(one, 1155))), 3),
        scale(multiply(b, add(scale(b2, 11), scale(b, 81), scale(one, 414))), -20),
    )
    q_star = add(
        scale(
            multiply(
                b,
                add(
                    scale(one, 360),
                    scale(q, 1098),
                    scale(q2, 191),
                    scale(power(q, 3), -10),
                ),
            ),
            720,
        ),
        multiply(add(scale(q, 12), scale(b, -44), scale(one, -294)), q, p),
    )
    k_star = add(scale(multiply(b, q, add(b, scale(one, -6))), 240), scale(p, -1))
    e_g = add(k_star, scale(multiply(b, q2), -720))
    l_star = add(
        scale(multiply(b, add(b2, scale(b, 6), scale(one, 105), scale(q, 8))), 135),
        scale(p, -6),
    )
    x_star = add(q_star, scale(multiply(d_star, q2), -24))
    j_star = add(
        scale(multiply(b, q_star), 150),
        scale(power(d_star, 2), -3),
        scale(multiply(p, d_star), -5),
    )

    b_poly = add(
        scale(q2, 96),
        multiply(add(scale(one, 216), scale(b, -32)), q),
        scale(b2, 3),
        scale(b, 18),
        scale(one, 315),
    )
    t = add(scale(b2, -280), scale(b, 2241), scale(one, 3465))
    m = add(scale(b2, 29), scale(b, 234), scale(one, 81))
    r = scale(multiply(b, m), 5)
    r_j = add(scale(d_star, 3), scale(p, 5), scale(multiply(b, q2), -3600))

    assert l_star == add(scale(multiply(b, b_poly), 45), scale(e_g, 6))
    assert add(r_j, scale(e_g, 5)) == add(
        scale(multiply(b, b_poly), -75),
        scale(add(multiply(t, q), scale(r, -1)), 3),
    )
    assert j_star == add(scale(multiply(d_star, r_j), -1), scale(multiply(b, x_star), 150))
    assert add(scale(t, 29), scale(m, 280)) == add(scale(b, 130509), scale(one, 123165))

    numerator = 29 * 13685**2 - 234 * 13685 * 14501 + 81 * 14501**2
    assert numerator == -23972710684
    assert tuple(numerator % prime for prime in PRIMES) == (
        3690,
        44145,
        312391,
        1797093080,
    )
    assert all(9 % prime and 14501 % prime and 5 % prime for prime in PRIMES)

    f_b = add(
        scale(multiply(add(scale(one, 1575), scale(b2, -247)), q2), 63),
        scale(multiply(b2, add(scale(one, 9), scale(b2, -1)), q), 9240),
        scale(
            multiply(b2, add(scale(one, 9), scale(b2, -1)), add(b2, scale(one, 27))),
            400,
        ),
    )
    hats = {
        "Bhat": clear_q(b_poly, r, t, 2),
        "Ehat": clear_q(e_g, r, t, 2),
        "Fhat": clear_q(f_b, r, t, 2),
        "Xhat": clear_q(x_star, r, t, 3),
    }
    bounds = {
        "Bhat": 6,
        "Ehat": 7,
        "Fhat": 10,
        "Xhat": 11,
    }
    assert all(total_degree(poly) <= bounds[label] for label, poly in hats.items())


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
    for marker in ("(FJ02)", "T(b)=-280b^2+2241b+3465", "-23972710684", "deg Xhat<=11"):
        assert marker in packet


def main() -> None:
    polynomial_check()
    packet_check()
    print(
        "L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_321_EXCEPTIONAL_E_J0_AFFINE_ROUTER_PASS "
        "filters=4 max_degree=11"
    )


if __name__ == "__main__":
    main()
