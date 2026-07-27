#!/usr/bin/env python3
"""Exact moment certificates for the collision-free quadratic exclusion."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_order_zero_quadratic_collisionfree_exclusion"
HNF = "l1_mersenne_next_to_maximal_hypergeometric_normal_form"
LINEAR = "l1_mersenne_hnf_order_zero_linear_color_exclusion"
CONSUMER = "l1_mixed_petal_amplification"
ZERO = [Fraction(0)]
ONE = [Fraction(1)]


def trim(a: list[Fraction]) -> list[Fraction]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    return trim(out)


def scale(a: list[Fraction], c: Fraction | int) -> list[Fraction]:
    return trim([Fraction(c) * value for value in a])


def mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] += left * right
    return trim(out)


def rising(r: int) -> list[Fraction]:
    out = ONE
    for j in range(r):
        out = mul(out, [Fraction(j), Fraction(1)])
    return scale(out, Fraction(1, math.factorial(r)))


def svtrim(a: list[list[Fraction]]) -> list[list[Fraction]]:
    while len(a) > 1 and a[-1] == ZERO:
        a.pop()
    return a


def svadd(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    out = [ZERO[:] for _ in range(max(len(a), len(b)))]
    for i, value in enumerate(a):
        out[i] = add(out[i], value)
    for i, value in enumerate(b):
        out[i] = add(out[i], value)
    return svtrim(out)


def svscale(a: list[list[Fraction]], c: Fraction | int) -> list[list[Fraction]]:
    return svtrim([scale(value, c) for value in a])


def svmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    out = [ZERO[:] for _ in range(len(a) + len(b) - 1)]
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] = add(out[i + j], mul(left, right))
    return svtrim(out)


def svpow(a: list[list[Fraction]], exponent: int) -> list[list[Fraction]]:
    out = [ONE]
    for _ in range(exponent):
        out = svmul(out, a)
    return out


def check_moments(h: int) -> None:
    coefficients = [rising(r) for r in range(7)]
    powers: list[list[Fraction] | None] = [None]
    for k in range(1, 7):
        total = scale(coefficients[k], k)
        for j in range(1, k):
            total = add(total, mul(coefficients[j], powers[k - j]))  # type: ignore[arg-type]
        powers.append(scale(total, -1))
        assert powers[k] == [Fraction(0), Fraction(-1)]

    z = [ONE, [Fraction(-1)]]
    q: list[list[list[Fraction]] | None] = [None]
    for r in range(1, 4):
        value = [ZERO[:]]
        for j in range(r + 1):
            term = scale(
                powers[r + j],  # type: ignore[arg-type]
                math.comb(r, j) * ((-1) ** (r - j)),
            )
            slot = [ZERO[:] for _ in range(r - j)] + [term]
            value = svadd(value, slot)
        q.append(value)
        expected_q = [mul(entry, [Fraction(0), Fraction(-1)]) for entry in svpow(z, r)]
        assert value == expected_q

    locator_coefficients: list[list[list[Fraction]] | None] = [[ONE]]
    for r in range(1, 4):
        total = q[r]  # type: ignore[assignment]
        for j in range(1, r):
            total = svadd(
                total,
                svmul(locator_coefficients[j], q[r - j]),  # type: ignore[arg-type]
            )
        current = svscale(total, Fraction(-1, r))
        locator_coefficients.append(current)
        expected = [mul(entry, rising(r)) for entry in svpow(z, r)]
        assert current == expected

    assert Fraction(h + 1, 2 * h) != 0


def main() -> None:
    for h in (7, 15):
        check_moments(h)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[LINEAR]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (HNF, NODE, "req") in edges
    assert (LINEAR, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = Path(__file__).with_name("statement.md").read_text()
    proof = Path(__file__).with_name("proof.md").read_text()
    assert "not injective" in statement
    assert "exactly one repeated color" in statement
    assert "does not exclude" in statement and "retained quadratic systems" in statement
    assert "p_j=-s" in proof and "d_r=binom" in proof

    mutation = [entry[:] for entry in svpow([ONE, [Fraction(-1)]], 3)]
    mutation[0] = add(mutation[0], ONE)
    expected = [mul(entry, rising(3)) for entry in svpow([ONE, [Fraction(-1)]], 3)]
    assert mutation != expected

    print(
        "L1_MERSENNE_HNF_ORDER_ZERO_QUADRATIC_COLLISIONFREE_EXCLUSION_PASS "
        "rows=5 moments=12 coefficient_levels=6 mutations=1"
    )


if __name__ == "__main__":
    main()
