#!/usr/bin/env python3
"""Exact first-subresultant certificate for the final quadratic chamber."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m16_order_zero_even_quadratic_exclusion"
DEPENDENCIES = (
    "l1_mersenne_next_to_maximal_hypergeometric_normal_form",
    "l1_mersenne_hnf_order_zero_quadratic_collision_router",
    "l1_mersenne_hnf_m8_order_zero_quadratic_exclusion",
    "l1_mersenne_hnf_m16_order_zero_single_collision_exclusion",
)
CONSUMER = "l1_mixed_petal_amplification"
PRIME = 8191


def expected_factor(s: sp.Symbol) -> sp.Expr:
    return (
        s**6
        * (s - 3)
        * (s - 2)
        * (s - 1) ** 6
        * (s + 1) ** 6
        * (s + 2) ** 5
        * (s + 3) ** 5
        * (s + 4) ** 4
        * (s + 5) ** 4
        * (s + 6) ** 3
        * (s + 7) ** 3
        * (s + 8) ** 2
        * (s + 9) ** 2
        * (s + 10)
        * (s + 11)
    )


def reduce_mod(poly: sp.Poly, variable: sp.Symbol) -> sp.Poly:
    expression = 0
    for (exponent,), coefficient in poly.terms():
        numerator, denominator = map(int, coefficient.as_numer_denom())
        assert denominator % PRIME
        residue = (numerator % PRIME) * pow(denominator % PRIME, -1, PRIME) % PRIME
        expression += residue * variable**exponent
    return sp.Poly(expression, variable, modulus=PRIME)


def main() -> None:
    s, y = sp.symbols("s y")
    b = [sp.prod(s + j for j in range(r)) / sp.factorial(r) for r in range(16)]
    odd = sum(b[r] * y ** ((14 - r) // 2) for r in range(0, 15, 2))
    even = sum(b[r] * y ** ((15 - r) // 2) for r in range(1, 16, 2))
    reduced_even = sp.cancel(even - s * odd)

    assert sp.degree(odd, y) == 7
    assert sp.degree(reduced_even, y) == 6
    assert sp.factor(sp.Poly(reduced_even, y).LC()) == -s * (s - 1) * (s + 1) / 3

    subresultants = sp.subresultants(odd, reduced_even, y)
    assert [sp.degree(value, y) for value in subresultants] == list(range(7, -1, -1))
    first = sp.Poly(subresultants[-2], y)
    assert first.degree() == 1
    c0 = sp.Poly(first.nth(0), s, domain=sp.QQ)
    c1 = sp.Poly(first.nth(1), s, domain=sp.QQ)
    assert (c0.degree(), c1.degree()) == (80, 78)

    expected_qq = sp.Poly(expected_factor(s), s, domain=sp.QQ).monic()
    gcd_qq = sp.gcd(c0, c1).monic()
    assert gcd_qq == expected_qq
    assert gcd_qq.degree() == 50

    c0_mod = reduce_mod(c0, s)
    c1_mod = reduce_mod(c1, s)
    assert int(c0_mod.eval(123)) % PRIME == 8032
    assert int(c1_mod.eval(123)) % PRIME == 2546
    expected_mod = sp.Poly(expected_factor(s), s, modulus=PRIME).monic()
    gcd_mod = sp.gcd(c0_mod, c1_mod).monic()
    assert gcd_mod == expected_mod
    assert gcd_mod.degree() == 50

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    for dependency in DEPENDENCIES:
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = Path(__file__).with_name("statement.md").read_text()
    proof = Path(__file__).with_name("proof.md").read_text()
    assert "deg E_s != 2" in statement
    assert "Sres_1" in proof and "degree 50" in proof

    wrong = sp.Poly(expected_factor(s) / (s - 2), s, modulus=PRIME).monic()
    assert gcd_mod != wrong

    print(
        "L1_MERSENNE_HNF_M16_ORDER_ZERO_EVEN_QUADRATIC_EXCLUSION_PASS "
        "row=1 subresultants=8 coefficient_degrees=80,78 gcd_degree=50 mutations=1"
    )


if __name__ == "__main__":
    main()
