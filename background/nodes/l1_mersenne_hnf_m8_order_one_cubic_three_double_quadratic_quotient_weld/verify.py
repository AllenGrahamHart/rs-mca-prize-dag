#!/usr/bin/env python3
"""Check the quadratic quotient and generic coefficient weld."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_double_quadratic_quotient_weld"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_double_affine_invariant_formula"
CONSUMER = "l1_mixed_petal_amplification"


def add(left: list[F], right: list[F]) -> list[F]:
    out = [F(0)] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    return out


def mul(left: list[F], right: list[F]) -> list[F]:
    out = [F(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def scale(poly: list[F], value: F) -> list[F]:
    return [value * coefficient for coefficient in poly]


def reduce_quadratic(poly: list[F], a: F, h: F) -> tuple[F, F]:
    u = [F(0), F(1)]
    v = [F(1), F(0)]
    coefficient = F(0)
    constant = F(0)
    for degree, value in enumerate(poly):
        while len(u) <= degree:
            u.append(v[-1] - a * u[-1])
            v.append(h * u[-2])
        coefficient += value * u[degree]
        constant += value * v[degree]
    return coefficient, constant


def main() -> None:
    x, q, d = F(2), F(5), F(3)
    c = d**2 + 3 * d + 3
    a = 3 * x**2 - q / 2
    h = 3 * q * c / 4 + q**2 / 8
    p = [F(0), F(1)]
    z = x**2 + q / 6
    ell = add([z], scale(p, F(-2, 3)))
    eta = add([-q * (d + 2) / 6], scale(p, -x))
    p_image = add(
        add(mul(mul(ell, ell), p), scale(mul(ell, eta), 6 * x)),
        scale(mul(p, p), -4 * x**2 / 3),
    )
    coefficient, constant = reduce_quadratic(p_image, a, h)
    r_p = -60 * x**4 - 8 * q * x**2 + 8 * q * (d + 2) * x + 4 * q * c + q**2
    s_p = -12 * x * q * (d + 2) * z
    assert (12 * coefficient, 12 * constant) == (r_p, s_p)

    alpha, delta, a6, gamma = F(7), F(11), F(13), F(17)
    reconstructed = -delta / alpha
    assert alpha * reconstructed + delta == 0
    assert alpha * gamma - a6 * delta == alpha * (a6 * reconstructed + gamma)
    assert delta**2 - a * alpha * delta - h * alpha**2 == alpha**2 * (
        reconstructed**2 + a * reconstructed - h
    )

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
    for anchor in ("(QQW2)", "(QQW5)", "(QQW6)", "(QQW7)"):
        assert anchor in statement
    for anchor in ("unique affine-linear remainder", "Conversely", "equivalent"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_DOUBLE_QUADRATIC_QUOTIENT_WELD_PASS")


if __name__ == "__main__":
    main()
