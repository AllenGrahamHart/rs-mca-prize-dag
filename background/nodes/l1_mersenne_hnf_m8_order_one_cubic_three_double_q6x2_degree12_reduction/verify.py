#!/usr/bin/env python3
"""Check the h=7 cubic 2+2+2 q=-6x^2 degree-12 reduction."""

from __future__ import annotations

import json
from fractions import Fraction as FQ
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_double_q6x2_degree12_reduction"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_double_linear_remainder_reduction"
CONSUMER = "l1_mixed_petal_amplification"


def add(a: list[FQ], b: list[FQ]) -> list[FQ]:
    out = [FQ(0)] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def mul(a: list[FQ], b: list[FQ]) -> list[FQ]:
    out = [FQ(0)] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] += left * right
    return out


def remainder(poly: list[FQ], divisor: list[FQ]) -> list[FQ]:
    out = poly[:]
    while len(out) >= len(divisor):
        scale = out[-1] / divisor[-1]
        shift = len(out) - len(divisor)
        for i, value in enumerate(divisor):
            out[i + shift] -= scale * value
        while len(out) > 1 and out[-1] == 0:
            out.pop()
    return out


def quantities(d: FQ, x: FQ) -> dict[str, FQ]:
    y = x**2
    q = -6 * y
    a = 11 * d**2 + 27 * d + 27
    b = d**4 + 4 * d**3 + 7 * d**2 + 6 * d + 3
    s = d**2 + 3 * d + 3
    u = d**2 + 2 * d + 2
    quartic = 5 * d**4 + 21 * d**3 + 37 * d**2 + 32 * d + 15
    conic = 105 * y**2 - 7 * a * y + 10 * b
    e0 = -2 * quartic / 5 + (13 * d**2 + 33 * d + 33) * y - 21 * y**2
    branch = (d + 2) * e0 - x * (d + 6 * y) * (s - y)

    g = (
        1
        + q * (10 * d**4 + 62 * d**3 + 163 * d**2 + 237 * d + 213) / 60
        + q**2 * (13 * d**2 + 55 * d + 76) / 72
        + q**3 / 48
    )
    b5 = (
        12 * x**3
        + 6
        + q * (d**2 + 5 * d + 11 + (1 - d**2 - 3 * d) * x - (d + 2) * x**2) / 2
        + q**2 * (d + 5 - x) / 12
    )
    m5 = (q - d) * b5 + 6 * d * g
    e = 14 * (2 * d**2 + 9 * d + 9) ** 2 - 75 * b
    f = 5 * b * (19 * d**2 + 63 * d + 63) - 126 * (d + 2) ** 2 * u**2
    return locals()


def main() -> None:
    for d, x in ((FQ(1), FQ(2)), (FQ(-3), FQ(1)), (FQ(5, 2), FQ(-2))):
        z = quantities(d, x)
        assert z["m5"] == 3 * x**2 * z["branch"]
        assert z["e0"] + 2 * z["u"] * (d + 6 * z["y"]) / 5 == -z["conic"] / 5

        cy = [10 * z["b"], -7 * z["a"], FQ(105)]
        sy = [z["s"], FQ(-1)]
        qy = add(
            [FQ(-4) * (d + 2) ** 2 * z["u"] ** 2],
            [25 * value for value in mul([FQ(0), FQ(1)], mul(sy, sy))],
        )
        rem = remainder(qy, cy)
        assert rem == [2 * z["f"] / 63, 2 * z["e"] / 63]

    # Leading coefficients of F, E, A, and B determine degree and leader.
    leader = 105 * 31**2 + 7 * 11 * 31 * 19 + 10 * 19**2
    assert leader == 149868
    assert leader != 149867

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
    for anchor in ("(QDR3)", "(QDR6)", "(QDR7)", "(QDR8)"):
        assert anchor in statement
    for anchor in ("149868", "32", "No gcd verdict"):
        assert anchor in statement + proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_DOUBLE_Q6X2_DEGREE12_REDUCTION_PASS")


if __name__ == "__main__":
    main()
