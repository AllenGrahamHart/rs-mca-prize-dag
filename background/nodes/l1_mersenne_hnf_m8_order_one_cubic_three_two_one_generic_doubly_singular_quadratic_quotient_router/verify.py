#!/usr/bin/env python3
"""Audit identities for the doubly-singular quadratic-quotient router."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_doubly_singular_quadratic_quotient_router"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_double_linear_d_router"
CONSUMER = "l1_mixed_petal_amplification"


def packet(x: F, y: F, q: F, d: F, c2: F, c1: F, c0: F) -> dict[str, F]:
    a = 6 - 2 * x
    u = x + y
    l2 = 15 + q / 2
    l3 = 20 + q * (d + 8) / 3
    g2 = (l2 - x**2 - a * (2 * x + y)) / 2
    v = g2 + x * y + y**2
    delta0 = y * v
    h = g2 + a * u
    q0 = 6 * g2 + a * x * u - 20 - 8 * q / 3 - delta0
    w0 = y * (a + x) * v + 15 + 23 * q / 4 + q**2 / 8
    r0 = g2 * h - x * q0 - w0
    role_r = a * (3 * y**2 + 2 * x * y + g2)
    role_s0 = (y - a) * v - q0
    ad = 4 * x - 21
    alpha = ad / 3
    beta = 4 * r0 / q
    p4 = -3 * q * d**2 + q * ad * d + 12 * r0
    conic = (
        35 * q**2
        + 14 * q * (11 * d**2 + 27 * d + 27)
        + 120 * (d**4 + 4 * d**3 + 7 * d**2 + 6 * d + 3)
    )
    n1 = q**2 * (
        40 * ad**3 + 480 * ad**2 + (2520 + 462 * q) * ad + 6480 + 3402 * q
    ) + 2880 * q * r0 * (ad + 6)
    n0 = (
        q * r0 * (480 * ad**2 + 5760 * ad + 30240 + 5544 * q)
        + 17280 * r0**2
        + q**2 * (3240 + 3402 * q + 315 * q**2)
    )
    qc = 120 * (d**2 + alpha * d + alpha**2 + beta) + 480 * (d + alpha) + 840 + 154 * q
    phi = c2 * role_r**2 + c1 * role_r * (role_s0 + q * d / 3) + c0 * (
        role_s0 + q * d / 3
    ) ** 2
    u1 = 9 * q * (c1 * role_r + 2 * c0 * role_s0) + c0 * q**2 * ad
    u0 = 27 * (c2 * role_r**2 + c1 * role_r * role_s0 + c0 * role_s0**2) + 12 * c0 * q * r0
    return locals()


def main() -> None:
    for values in (
        (F(2), F(3), F(5), F(7), F(1), F(2), F(3)),
        (F(-1), F(4), F(9), F(2), F(2), F(-1), F(5)),
        (F(5, 2), F(-3, 2), F(11), F(-4), F(3), F(4), F(2)),
    ):
        z = packet(*values)
        assert 9 * z["q"] ** 2 * z["conic"] == (
            z["n1"] * z["d"] + z["n0"] - 3 * z["q"] * z["qc"] * z["p4"]
        )
        assert 27 * z["phi"] + z["c0"] * z["q"] * z["p4"] == (
            z["u1"] * z["d"] + z["u0"]
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
    for anchor in ("(DQR1)", "(DQR4)", "(DQR7)", "(DQR9)"):
        assert anchor in statement
    for anchor in ("d^2=alpha d+beta", "N_1d+N_0", "U_1d+U_0"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_TWO_ONE_GENERIC_DOUBLY_SINGULAR_QUADRATIC_QUOTIENT_ROUTER_PASS")


if __name__ == "__main__":
    main()
