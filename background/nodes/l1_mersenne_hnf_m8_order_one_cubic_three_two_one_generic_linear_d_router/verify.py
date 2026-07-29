#!/usr/bin/env python3
"""Audit identities for the generic linear-d router."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_linear_d_router"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_coefficient_matrix_router"
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
    q6 = (y - a) * v - s
    e6 = delta0 * q6 - k6
    e4 = delta0 * g2 * h - delta0 * w - x * k6
    e5 = (q - d) * delta0**2 * h + j * k6
    f4 = g2 * h - x * q6 - w
    f5 = (q - d) * delta0 * h + j * q6
    t = g2 + 6 * delta0
    q0 = 6 * g2 + a * x * u - 20 - 8 * q / 3 - delta0
    w0 = y * (a + x) * v + 15 + 23 * q / 4 + q**2 / 8
    r0 = g2 * h - x * q0 - w0
    p4 = -3 * q * d**2 + q * (4 * x - 21) * d + 12 * r0
    p5 = q * t * d**2 - (3 * delta0 * h + q**2 * g2 + 3 * t * q0) * d + 3 * q * (
        delta0 * h + g2 * q0
    )
    c1 = q * t * (4 * x - 21) - 9 * delta0 * h - 3 * q**2 * g2 - 9 * t * q0
    c0 = 9 * q * (delta0 * h + g2 * q0) + 12 * t * r0
    return locals()


def main() -> None:
    for values in (
        (F(2), F(3), F(5), F(7)),
        (F(-1), F(4), F(9), F(2)),
        (F(5, 2), F(-3, 2), F(11), F(-4)),
    ):
        z = packet(*values)
        assert z["q6"] == z["q0"] - z["q"] * z["d"] / 3
        assert z["w"] == z["w0"] + z["q"] * (z["d"] ** 2 + 7 * z["d"]) / 4
        assert z["j"] == z["q"] * z["g2"] - z["d"] * z["t"]
        assert z["e4"] == z["delta0"] * z["f4"] + z["x"] * z["e6"]
        assert z["e5"] == z["delta0"] * z["f5"] - z["j"] * z["e6"]
        assert z["p4"] == 12 * z["f4"]
        assert z["p5"] == 3 * z["f5"]
        assert 3 * z["p5"] + z["t"] * z["p4"] == z["c1"] * z["d"] + z["c0"]

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
    for anchor in ("(GLD1)", "(GLD5)", "(GLD7)", "(GLD10)"):
        assert anchor in statement
    for anchor in ("E_4=DF_4+xE_6", "E_5=DF_5-JE_6", "3P_5+TP_4"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_TWO_ONE_GENERIC_LINEAR_D_ROUTER_PASS")


if __name__ == "__main__":
    main()
