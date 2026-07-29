#!/usr/bin/env python3
"""Audit the q-quotient recurrence for the fully-proportional endpoint."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_q_quotient_router"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_coefficient_bivariate_compiler"
CONSUMER = "l1_mixed_petal_amplification"


def trim(poly: list[F]) -> list[F]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left: list[F], right: list[F]) -> list[F]:
    out = [F(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
    return trim(out)


def scale(poly: list[F], scalar: F) -> list[F]:
    return trim([scalar * value for value in poly])


def mul(left: list[F], right: list[F]) -> list[F]:
    out = [F(0)] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            out[i + j] += left_value * right_value
    return trim(out)


def divmod_poly(numerator: list[F], denominator: list[F]) -> tuple[list[F], list[F]]:
    remainder = trim(numerator[:])
    quotient = [F(0)] * max(1, len(remainder) - len(denominator) + 1)
    while len(remainder) >= len(denominator) and remainder != [F(0)]:
        shift = len(remainder) - len(denominator)
        factor = remainder[-1] / denominator[-1]
        quotient[shift] += factor
        subtract = [F(0)] * shift + scale(denominator, factor)
        remainder = add(remainder, scale(subtract, F(-1)))
    return trim(quotient), trim(remainder)


def check_sample(b: F) -> None:
    q_poly = [F(0), F(1)]
    p = [40 * b * (b**2 - 6 * b + 27), 42 * (11 * b + 15)]
    d_star = [
        -20 * b * (11 * b**2 + 81 * b + 414),
        3 * (40 * b**2 - 253 * b + 1155),
    ]
    kappa = [-44 * b - 294, F(12)]
    q_star = add(
        [720 * b * 360, 720 * b * 1098, 720 * b * 191, -720 * b * 10],
        mul(mul(kappa, q_poly), p),
    )
    k_star = add([F(0), 240 * b * (b - 6)], scale(p, F(-1)))
    e_g = add(k_star, [F(0), F(0), -720 * b])
    l_star = add(
        [135 * b * (b**2 + 6 * b + 105), 1080 * b],
        scale(p, F(-6)),
    )
    f_star = add(mul(d_star, k_star), scale(q_star, -30 * b))
    j_star = add(
        add(scale(q_star, 150 * b), scale(mul(d_star, d_star), F(-3))),
        scale(mul(p, d_star), F(-5)),
    )
    theta = add(
        scale(mul(mul(mul(e_g, d_star), d_star), l_star), F(5)),
        scale(mul(j_star, f_star), F(-6)),
    )
    theta += [F(0)] * (7 - len(theta))

    a2 = 63 * (1575 - 247 * b**2)
    a1 = 9240 * b**2 * (9 - b**2)
    a0 = 400 * b**2 * (9 - b**2) * (b**2 + 27)
    assert a2 != 0
    fb = [a0, a1, a2]

    u = {1: F(1), 2: -a1}
    v = {1: F(0), 2: -a0}
    for j in range(3, 7):
        u[j] = -a1 * u[j - 1] - a2 * a0 * u[j - 2]
        v[j] = -a1 * v[j - 1] - a2 * a0 * v[j - 2]
        power = [F(0)] * j + [a2 ** (j - 1)]
        _, remainder = divmod_poly(add(power, [-v[j], -u[j]]), fb)
        assert remainder == [F(0)]

    r1 = a2**5 * theta[1]
    r0 = a2**5 * theta[0]
    for j in range(2, 7):
        r1 += a2 ** (6 - j) * theta[j] * u[j]
        r0 += a2 ** (6 - j) * theta[j] * v[j]
    left = scale(theta, a2**5)
    _, remainder = divmod_poly(add(left, [-r0, -r1]), fb)
    assert remainder == [F(0)]


def main() -> None:
    for b in (F(2), F(-1), F(5, 2)):
        check_sample(b)

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
    for anchor in ("(FQR1)", "(FQR6)", "(FQR7)", "(FQR10)"):
        assert anchor in statement
    for anchor in ("a_2q^2", "R_1q+R_0", "degree at most 58"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_TWO_ONE_GENERIC_FULLY_PROPORTIONAL_Q_QUOTIENT_ROUTER_PASS")


if __name__ == "__main__":
    main()
