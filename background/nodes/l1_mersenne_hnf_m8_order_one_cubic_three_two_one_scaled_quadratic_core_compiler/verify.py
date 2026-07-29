#!/usr/bin/env python3
"""Check the scaled triangular identities for the official 3+2+1 core."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_scaled_quadratic_core_compiler"
DEPENDENCIES = {
    "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_common_quadratic_compiler",
    "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_official_frobenius_role_split",
}
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
    r = a * (3 * y**2 + 2 * x * y + g2)
    delta = y * v
    l5 = -6 * d * k6 / (q - d)

    c4 = g2**2 + a * u * g2 + v * (a * (x - y) - 2 * x * y) + s * x - l4
    c5 = v * (g2 * (a - 2 * y) - a * y * u) + s * g2 - l5
    e6 = delta * ((y - a) * v - s) - k6
    e4 = delta * (g2**2 + a * u * g2 - y * (a + x) * v - l4) - x * k6
    e5 = (q - d) * (y**2 * v**2 * (g2 + a * u) + g2 * k6) - 6 * d * k6 * delta
    rd = delta * r
    sd = y * (y - a) * v**2 - k6
    return locals()


def main() -> None:
    for values in (
        (F(2), F(3), F(5), F(7)),
        (F(-1), F(4), F(9), F(2)),
        (F(5, 2), F(-3, 2), F(11), F(-4)),
    ):
        z = packet(*values)
        assert z["e6"] == z["delta"] * ((z["y"] - z["a"]) * z["v"] - z["s"]) - z["k6"]
        assert z["e4"] == z["delta"] * z["c4"] + z["x"] * z["e6"]
        assert z["e5"] == -(z["q"] - z["d"]) * (
            z["delta"] * z["c5"] + z["g2"] * z["e6"]
        )
        assert z["sd"] == z["delta"] * z["s"] + z["e6"]
        for alpha, beta, gamma in ((F(1), F(2), F(3)), (F(2), F(-1), F(5))):
            transported = alpha * z["rd"] ** 2 + beta * z["rd"] * z["sd"] + gamma * z["sd"] ** 2
            original = z["delta"] ** 2 * (
                alpha * z["r"] ** 2 + beta * z["r"] * z["s"] + gamma * z["s"] ** 2
            )
            correction = z["e6"] * (
                beta * z["rd"] + gamma * (2 * z["delta"] * z["s"] + z["e6"])
            )
            assert transported == original + correction

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
    for anchor in ("(SQC1)", "(SQC2)", "(SQC3)", "(SQC5)", "(SQC7)"):
        assert anchor in statement
    for anchor in ("E_4=D C_4+xE_6", "E_5=-(q-d)(D C_5+G_2E_6)", "D^2 Phi(R,S)"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_TWO_ONE_SCALED_QUADRATIC_CORE_COMPILER_PASS")


if __name__ == "__main__":
    main()
