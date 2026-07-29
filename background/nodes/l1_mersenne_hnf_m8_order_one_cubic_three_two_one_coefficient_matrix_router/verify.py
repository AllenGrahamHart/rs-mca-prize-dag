#!/usr/bin/env python3
"""Check the 3+2+1 coefficient-matrix routing identities."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_coefficient_matrix_router"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_scaled_quadratic_core_compiler"
CONSUMER = "l1_mixed_petal_amplification"


def packet(x: F, y: F, q: F, d: F) -> dict[str, F]:
    a = 6 - 2 * x
    u = x + y
    l2 = 15 + q / 2
    l3 = 20 + q * (d + 8) / 3
    l4 = 15 + q * (d**2 + 7 * d + 23) / 4 + q**2 / 8
    k6 = (
        1
        + q * (10 * d**4 + 62 * d**3 + 163 * d**2 + 237 * d + 213) / 60
        + q**2 * (13 * d**2 + 55 * d + 76) / 72
        + q**3 / 48
    )
    g2 = (l2 - x**2 - a * (2 * x + y)) / 2
    v = g2 + x * y + y**2
    s = l3 + 2 * y * v - 2 * x * g2 - a * (v + x * u + g2)
    delta0 = y * v
    h = g2 + a * u
    w = y * (a + x) * v + l4
    j = (q - d) * g2 - 6 * d * delta0
    determinant = g2 * j + x * (q - d) * delta0
    e4 = delta0 * g2 * h - delta0 * w - x * k6
    e5 = (q - d) * delta0**2 * h + j * k6
    e6 = delta0 * ((y - a) * v - s) - k6
    return locals()


def main() -> None:
    for values in (
        (F(2), F(3), F(5), F(7)),
        (F(-1), F(4), F(9), F(2)),
        (F(5, 2), F(-3, 2), F(11), F(-4)),
    ):
        z = packet(*values)
        assert z["j"] * z["e4"] + z["x"] * z["e5"] == z["delta0"] * (
            z["determinant"] * z["h"] - z["w"] * z["j"]
        )

    for y, q, d in ((F(3), F(5), F(7)), (F(-2), F(11), F(4))):
        z = packet(F(0), y, q, d)
        c0 = (
            96 * y**3
            - 144 * y**2
            + (720 + 24 * q) * y
            + q**2
            + 4 * q * (d**2 + 7 * d + 8)
            - 660
        )
        assert c0 == -16 * (z["e4"] / z["delta0"])
        m = 6 * z["g2"] - z["l3"] - z["delta0"]
        f5 = (q - d) * z["delta0"] * z["h"] + z["j"] * m
        assert z["delta0"] * f5 == z["e5"] + z["j"] * z["e6"]

    for q, d in ((F(5), F(7)), (F(11), F(-4))):
        ell = 15 + q / 2
        y = -ell / 6
        v = ell * (ell + 36) / 36
        l4 = 15 + q * (d**2 + 7 * d + 23) / 4 + q**2 / 8
        fj = d * (q**2 + 132 * q + 2916) + 144 * q
        fw = q**3 + 126 * q**2 + (5364 - 504 * d - 72 * d**2) * q + 87480
        assert fj == 144 * (q - d + d * v)
        assert fw == -288 * (l4 - ell * v)
        assert y == -ell / 6

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
    for anchor in ("(CMR1)", "(CMR2)", "(CMR3)", "(CMR4)", "(CMR7)"):
        assert anchor in statement
    for anchor in ("Cramer's rule", "WJ=0", "F_J", "F_W"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_TWO_ONE_COEFFICIENT_MATRIX_ROUTER_PASS")


if __name__ == "__main__":
    main()
