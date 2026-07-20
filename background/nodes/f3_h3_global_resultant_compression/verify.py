#!/usr/bin/env python3
"""Verify the H3 global resultant compression on exact small orders."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path

from sympy import Poly, expand, resultant, symbols


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_global_resultant_compression"
DEPENDENCY = "f3_h3_global_derivative_ideal_valuation"
CONSUMER = "f3_h3_mobius_excess_half"


def shifted_polynomial(n: int, x):
    return sum((-1) ** j * comb(n, j) * x ** (j - 1) for j in range(1, n + 1))


def exact_specialization(n: int, prime: int, generator: int) -> None:
    x, t, u = symbols("x t u")
    d = n - 1
    f = expand(shifted_polynomial(n, x))
    roots = [(1 - pow(generator, exponent, prime)) % prime for exponent in range(1, n)]
    assert len(set(roots)) == d

    product_direct = Poly(1, t, modulus=prime)
    for left in roots:
        for right in roots:
            product_direct *= Poly(t - left * right, t, modulus=prime)
    product_resultant = Poly(
        resultant(f, expand(x**d * f.subs(x, t / x)), x),
        t,
        modulus=prime,
    )
    assert product_resultant == product_direct

    quotient_direct = Poly(1, t, modulus=prime)
    for i, left in enumerate(roots):
        for j, right in enumerate(roots):
            if i != j:
                quotient_direct *= Poly(left * t - right, t, modulus=prime)
    quotient_all = Poly(resultant(f, f.subs(x, t * x), x), t, modulus=prime)
    diagonal = Poly(n * (t - 1) ** d, t, modulus=prime)
    assert quotient_all == diagonal * quotient_direct

    c, e = roots[0], roots[1]
    derivative_direct = Poly(1, u, modulus=prime)
    for left in roots:
        for right in roots:
            derivative_direct *= Poly(e + c * u - c * left * right, u, modulus=prime)

    f_poly = Poly(f, x)
    y = e + c * u
    h = sum(
        int(coefficient) * y**degree * (c * x) ** (d - degree)
        for (degree,), coefficient in f_poly.terms()
    )
    derivative_resultant = Poly(resultant(f, expand(h), x), u, modulus=prime)
    assert derivative_resultant == derivative_direct


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md",
        "proof.md",
        "claim_contract.md",
        "dependency_subdag.md",
        "audit.md",
        "result.md",
        "verify.py",
        "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join((base / name).read_text() for name in required if name.endswith(".md"))
    for marker in (
        "((1-X)^n-1)/X",
        "n(T-1)^d",
        "C^N Pcal_n(D/C+U)",
        "modulo `U^19`",
        "official-scale resultant algorithm",
    ):
        assert marker in text


def main() -> None:
    exact_specialization(4, 17, 4)
    exact_specialization(8, 17, 2)
    packet_check()
    print("F3_H3_GLOBAL_RESULTANT_COMPRESSION_PASS orders=4,8 identities=6")


if __name__ == "__main__":
    main()
