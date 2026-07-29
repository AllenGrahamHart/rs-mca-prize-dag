#!/usr/bin/env python3
"""Audit identities for the singular-J-nonzero chart compiler."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_singular_jnonzero_chart_compiler"
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
    determinant = g2 * j + x * (q - d) * delta0
    q6 = (y - a) * v - s
    e6 = delta0 * q6 - k6
    e4w0 = delta0 * g2 * h - x * k6
    n = g2**2 + x * delta0
    z = n + 6 * delta0 * g2
    p = 3 * x * (6 * g2 + a * x * u - 20 - delta0) - 8 * q * x - 3 * g2 * h
    return locals()


def main() -> None:
    for values in (
        (F(2), F(3), F(5), F(7)),
        (F(-1), F(4), F(9), F(2)),
        (F(5, 2), F(-3, 2), F(11), F(-4)),
    ):
        z = packet(*values)
        assert z["q6"] == 6 * z["g2"] + z["a"] * z["x"] * z["u"] - z["l3"] - z["delta0"]
        assert z["p"] - z["q"] * z["x"] * z["d"] == 3 * (
            z["x"] * z["q6"] - z["g2"] * z["h"]
        )
        assert z["determinant"] == z["q"] * z["n"] - z["d"] * z["z"]
        assert z["x"] * z["e6"] == z["delta0"] * (
            z["x"] * z["q6"] - z["g2"] * z["h"]
        ) + z["e4w0"]

    for q, d in ((F(5), F(7)), (F(11), F(-4))):
        y = (q + 30) / 12
        z = packet(F(0), y, q, d)
        pw = q**3 + 126 * q**2 + (4356 + 504 * d + 72 * d**2) * q + 31320
        pf = (
            576 * q * d**2
            + (q**3 + 90 * q**2 + 7164 * q + 57240) * d
            + 144 * q**2
            + 4320 * q
        )
        pl = (q**3 + 90 * q**2 + 3132 * q + 57240) * d - (
            8 * q**3 + 864 * q**2 + 30528 * q + 250560
        )
        f0 = (q - d) * y + d * y**3 + d * z["l3"]
        assert z["g2"] == 0
        assert pw == 288 * z["w"]
        assert pf == 1728 * f0
        assert pf == 8 * pw + pl
        assert z["e6"] == -(z["k6"] + y**6 + z["l3"] * y**3)

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
    for anchor in ("(SJC1)", "(SJC4)", "(SJC6)", "(SJC8)"):
        assert anchor in statement
    for anchor in ("P_F^+=8P_W^++P_L^+", "Delta=qN-dZ", "J=-x(q-d)D/G_2"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_TWO_ONE_SINGULAR_JNONZERO_CHART_COMPILER_PASS")


if __name__ == "__main__":
    main()
