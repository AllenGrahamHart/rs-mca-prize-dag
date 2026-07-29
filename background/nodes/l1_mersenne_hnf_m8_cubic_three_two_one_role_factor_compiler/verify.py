#!/usr/bin/env python3
"""Check the four-factor role-polynomial homogenization."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_cubic_three_two_one_role_factor_compiler"
DEPENDENCIES = {
    "l1_mersenne_hnf_m8_cubic_three_two_one_role_polynomial_compiler",
    "l1_mersenne_hnf_m8_order_one_cubic_three_double_affine_color_compiler",
}
CONSUMER = "l1_mixed_petal_amplification"


def mul(left: list[F], right: list[F]) -> list[F]:
    out = [F(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def add(left: list[F], right: list[F], scale: F = F(1)) -> list[F]:
    out = [F(0)] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += scale * value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def power(poly: list[F], exponent: int) -> list[F]:
    out = [F(1)]
    for _ in range(exponent):
        out = mul(out, poly)
    return out


def main() -> None:
    a = [F(1), F(-1), F(1)]
    b = [F(2), F(-3), F(-3), F(2)]
    a3 = power(a, 3)
    a6 = power(a, 6)
    b2 = power(b, 2)
    b4 = power(b, 4)
    factors = (
        add(b2, a3, F(50)),
        add(add(b4, mul(b2, a3), F(-224)), a6, F(-578)),
        add(add(b4, mul(b2, a3), F(-4)), a6, F(54)),
        add(add([125 * value for value in b4], mul(b2, a3), F(-2404)), a6, F(13448)),
    )
    assert tuple(len(factor) - 1 for factor in factors) == (6, 12, 12, 12)
    product = [F(1)]
    for factor in factors:
        product = mul(product, factor)
    assert len(product) - 1 == 42

    identity = add(power(a, 3), power(b, 2), F(-1, 4))
    rhs = mul(power([F(0), F(1)], 2), power([F(-1), F(1)], 2))
    assert [4 * value for value in identity] == [27 * value for value in rhs]

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[CONSUMER] == "TARGET"
    for dependency in DEPENDENCIES:
        assert statuses[dependency] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    for anchor in ("(RFC1)", "(RFC2)", "(RFC3)", "(RFC4)"):
        assert anchor in statement
    for anchor in ("six ordered", "same root multiset", "factors may merge"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_CUBIC_THREE_TWO_ONE_ROLE_FACTOR_COMPILER_PASS")


if __name__ == "__main__":
    main()
