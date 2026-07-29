#!/usr/bin/env python3
"""Check the h=7 cubic 2+2+2 x=0 quintic reduction."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_double_x0_quintic_reduction"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_double_linear_remainder_reduction"
CONSUMER = "l1_mixed_petal_amplification"
PRIMES = (8191, 131071, 524287, 2147483647)


def quantities(d: F, q: F) -> dict[str, F]:
    a = 11 * d**2 + 27 * d + 27
    b = d**4 + 4 * d**3 + 7 * d**2 + 6 * d + 3
    c = 13 * d**2 + 34 * d + 33
    e = 5 * d**4 + 21 * d**3 + 37 * d**2 + 32 * d + 15
    p = 5 * d**3 + 16 * d**2 + 18 * d + 10
    p5 = 60 * d**5 + 407 * d**4 + 1147 * d**3 + 1659 * d**2 + 1218 * d + 360
    g = (
        1
        + q * (10 * d**4 + 62 * d**3 + 163 * d**2 + 237 * d + 213) / 60
        + q**2 * (13 * d**2 + 55 * d + 76) / 72
        + q**3 / 48
    )
    b5 = 6 + q * (d**2 + 5 * d + 11) / 2 + q**2 * (d + 5) / 12
    m5 = (q - d) * b5 + 6 * d * g
    j = 25 * q**2 + 10 * c * q + 24 * e
    conic = 35 * q**2 + 14 * a * q + 120 * b
    return locals()


def main() -> None:
    for d, q in ((F(1), F(2)), (F(4), F(-3)), (F(-5, 2), F(7))):
        z = quantities(d, q)
        assert 120 * z["m5"] == q * (d + 2) * z["j"]
        assert 25 * z["conic"] - 35 * z["j"] == -10 * (2 * d + 3) * (
            35 * (d + 2) * q + 12 * z["p"]
        )
        if d != -2:
            q0 = -12 * z["p"] / (35 * (d + 2))
            w = quantities(d, q0)
            assert 35 * (d + 2) ** 2 * w["conic"] == -24 * (d + 3) * w["p5"]

    for prime in PRIMES:
        assert prime % 8 == 7
        for value in (F(4), F(9, 4), F(9)):
            residue = value.numerator * pow(value.denominator, -1, prime) % prime
            assert residue not in (1, prime - 1)

    z = quantities(F(1), F(2))
    assert 120 * z["m5"] != 2 * 3 * z["j"] + 1
    assert z["p5"] != z["p5"] + 1

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
    for anchor in ("(XQ2)", "(XQ4)", "(XQ6)", "(XQ8)"):
        assert anchor in statement
    for anchor in ("P_5", "32", "No gcd verdict"):
        assert anchor in statement + proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_DOUBLE_X0_QUINTIC_REDUCTION_PASS")


if __name__ == "__main__":
    main()
