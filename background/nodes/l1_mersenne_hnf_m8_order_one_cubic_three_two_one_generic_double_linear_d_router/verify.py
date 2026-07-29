#!/usr/bin/env python3
"""Audit identities for the generic double-linear-d router."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_double_linear_d_router"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_linear_d_router"
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
    q6 = (y - a) * v - s
    e6 = delta0 * q6 - k6
    conic = (
        35 * q**2
        + 14 * q * (11 * d**2 + 27 * d + 27)
        + 120 * (d**4 + 4 * d**3 + 7 * d**2 + 6 * d + 3)
    )
    q0 = 6 * g2 + a * x * u - 20 - 8 * q / 3 - delta0
    w0 = y * (a + x) * v + 15 + 23 * q / 4 + q**2 / 8
    r0 = g2 * h - x * q0 - w0
    p4 = -3 * q * d**2 + q * (4 * x - 21) * d + 12 * r0
    kappa = 12 * q + 366 - 176 * x
    b1 = -q * (120 * delta0 + 1062 + 86 * q) - 528 * r0
    b0 = 360 * delta0 * q0 - 360 - 1098 * q - 191 * q**2 + 10 * q**3
    m1 = 3 * b1 + q * kappa * (4 * x - 21)
    m0 = 3 * b0 + 12 * kappa * r0
    r3 = (
        -132 * q * d**3
        + (12 * q**2 - 558 * q) * d**2
        - (120 * delta0 * q + 1062 * q + 86 * q**2) * d
        + b0
    )
    r2 = q * kappa * d**2 + b1 * d + b0
    return locals()


def main() -> None:
    for values in (
        (F(2), F(3), F(5), F(7)),
        (F(-1), F(4), F(9), F(2)),
        (F(5, 2), F(-3, 2), F(11), F(-4)),
    ):
        z = packet(*values)
        assert z["r3"] == (720 * z["e6"] + z["q"] * z["conic"]) / 2
        assert z["r2"] == z["r3"] - 44 * z["d"] * z["p4"]
        assert 3 * z["r2"] + z["kappa"] * z["p4"] == z["m1"] * z["d"] + z["m0"]
        assert 2 * (z["m1"] * z["d"] + z["m0"]) == (
            2160 * z["e6"]
            + 3 * z["q"] * z["conic"]
            + 2 * (z["kappa"] - 132 * z["d"]) * z["p4"]
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
    for anchor in ("(GDL1)", "(GDL2)", "(GDL4)", "(GDL5)"):
        assert anchor in statement
    for anchor in ("R_3=(720E_6+qC)/2", "R_2=R_3-44dP_4", "3R_2+kappa P_4"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_TWO_ONE_GENERIC_DOUBLE_LINEAR_D_ROUTER_PASS")


if __name__ == "__main__":
    main()
