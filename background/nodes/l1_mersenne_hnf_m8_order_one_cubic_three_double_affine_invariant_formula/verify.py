#!/usr/bin/env python3
"""Check the quadratic-map invariant formulas and rational color factors."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_double_affine_invariant_formula"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_double_affine_color_compiler"
CONSUMER = "l1_mixed_petal_amplification"


def poly_mul(left: list[F], right: list[F]) -> list[F]:
    out = [F(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def invariants(values: tuple[F, F, F]) -> tuple[F, F]:
    e1 = sum(values)
    e2 = values[0] * values[1] + values[0] * values[2] + values[1] * values[2]
    e3 = values[0] * values[1] * values[2]
    return e2 - e1**2 / 3, e3 - e1 * e2 / 3 + 2 * e1**3 / 27


def main() -> None:
    roots = (F(-2), F(-1), F(3))
    p = roots[0] * roots[1] + roots[0] * roots[2] + roots[1] * roots[2]
    eta = roots[0] * roots[1] * roots[2]
    a, ell = F(2), F(3)
    values = tuple(a * value**2 + ell * value for value in roots)
    p_direct, q_direct = invariants(values)
    p_formula = ell**2 * p - 3 * a * ell * eta - a**2 * p**2 / 3
    q_formula = (
        a**3 * (eta**2 + 2 * p**3 / 27)
        - a**2 * ell * p * eta
        + 2 * a * ell**2 * p**2 / 3
        + ell**3 * eta
    )
    assert (p_direct, q_direct) == (p_formula, q_formula)

    theta = [F(1)]
    for factor in (
        [F(50), F(1)],
        [F(-578), F(-224), F(1)],
        [F(54), F(-4), F(1)],
        [F(13448), F(-2404), F(125)],
    ):
        theta = poly_mul(theta, factor)
    assert len(theta) - 1 == 7
    assert 224**2 + 4 * 578 == 4 * 81**2 * 2
    assert (-4) ** 2 - 4 * 54 == -200
    assert 2404**2 - 4 * 125 * 13448 == -(2 * 486) ** 2

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[DEPENDENCY] == "PROVED"
    assert statuses[CONSUMER] == "TARGET"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    for anchor in ("(AIF3)", "(AIF5)", "(AIF6)", "(AIF7)"):
        assert anchor in statement
    for anchor in ("sum w_i^2", "A=-2x", "including the `P=0` locus"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_DOUBLE_AFFINE_INVARIANT_FORMULA_PASS")


if __name__ == "__main__":
    main()
