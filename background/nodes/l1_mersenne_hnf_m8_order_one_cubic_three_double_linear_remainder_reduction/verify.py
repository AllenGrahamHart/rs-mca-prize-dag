#!/usr/bin/env python3
"""Check the h=7 cubic 2+2+2 linear polynomial-remainder reduction."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_double_linear_remainder_reduction"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_double_symmetric_compiler"
CONSUMER = "l1_mixed_petal_amplification"


def data(x: F, b: F, q: F, d: F) -> dict[str, F]:
    a = x + 3
    k = 6 * x - 3 + q / 2
    c = (b + k) / 3
    t0 = 12 * x - 16 - q * (d + 2) / 6
    t1 = 2 - x
    t = t1 * b + t0
    g = (
        1
        + q * (10 * d**4 + 62 * d**3 + 163 * d**2 + 237 * d + 213) / 60
        + q**2 * (13 * d**2 + 55 * d + 76) / 72
        + q**3 / 48
    )
    h = x**2 - 8 - q / 6
    k0 = 48 - 12 * x**2 + q * (-d**2 - 3 * d + 5) / 4 - q**2 / 24
    divisor = b**2 + 3 * h * b + 3 * k0

    p2 = 36 - 2 * b
    p3 = 216 - 18 * b + 3 * t
    p4 = 1296 - 144 * b + 2 * b**2 + 24 * t
    sum_v = p2 - 6 * a + 3 * c
    sum_v2 = p4 - 2 * a * p3 + (a**2 + 2 * c) * p2 - 12 * a * c + 3 * c**2
    l4 = (sum_v**2 - sum_v2) / 2 + (6 - 3 * a) * t + c * b
    l5 = t * (3 * a**2 - 12 * a + b - 3 * c) + 2 * c * b * (3 - a) + 6 * c**2
    l6 = (
        t**2
        + t * (-a * b - 12 * c + 6 * a**2 + 3 * a * c - a**3)
        + c * b * (b + a**2 - 6 * a)
        + c**2 * (36 - 6 * a - 2 * b)
        + c**3
    )
    hnf4 = 15 + q * (d**2 + 7 * d + 23) / 4 + q**2 / 8

    a5 = -x * (x**2 + q / 6)
    b5 = (
        12 * x**3
        + 6
        + q * (d**2 + 5 * d + 11 + (1 - d**2 - 3 * d) * x - (d + 2) * x**2) / 2
        + q**2 * (d + 5 - x) / 12
    )
    c3 = F(4, 27)
    c2 = (4 * x**2 - 2 * x - 15) / 3
    p0 = -x**3 + 3 * x**2 + 30 + (x - 1) * q / 2
    m = x**2 - 9
    n = 18 - 6 * x
    c1 = -2 * x * t0 + t1 * p0 + k * m / 3 + (2 * k * n - k**2) / 9
    c0 = t0**2 + t0 * p0 + k**2 * n / 9 + k**3 / 27
    a6 = c1 + 4 * h**2 / 3 - 4 * k0 / 9 - 3 * h * c2
    b6 = c0 + 4 * h * k0 / 3 - 3 * k0 * c2 - g
    return locals()


def main() -> None:
    samples = ((F(2), F(7), F(5), F(3)), (F(-1), F(4), F(7), F(2)))
    for x, b, q, d in samples:
        z = data(x, b, q, d)
        assert 3 * (z["l4"] - z["hnf4"]) == z["divisor"]
        c5 = 2 * (1 - x) / 3
        assert z["l5"] - (z["a5"] * b + z["b5"]) == c5 * z["divisor"]
        assert z["a5"] == -x * (x**2 + q / 6)
        assert z["l6"] == z["c3"] * b**3 + z["c2"] * b**2 + z["c1"] * b + z["c0"]
        assert (
            z["l6"] - z["g"] - (z["a6"] * b + z["b6"])
            == (z["c3"] * (b - 3 * z["h"]) + z["c2"]) * z["divisor"]
        )

    z = data(F(2), F(7), F(5), F(3))
    assert 3 * (z["l4"] - z["hnf4"]) != z["divisor"] + 1
    assert z["a5"] != -2 * (F(4) - F(5, 6))

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
    for anchor in ("(TLR3)", "(TLR5)", "(TLR7)", "(TLR9)"):
        assert anchor in statement
    for anchor in ("b^2=-3Hb-3K", "q-d!=0", "No branch"):
        assert anchor in statement + proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_DOUBLE_LINEAR_REMAINDER_REDUCTION_PASS")


if __name__ == "__main__":
    main()
