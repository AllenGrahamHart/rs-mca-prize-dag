#!/usr/bin/env python3
"""Checks for the c2 barycentric support-polynomial compiler."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NODE_ID = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_barycentric_support_polynomial_compiler"
DEPENDENCY = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_barycentric_negation_syndrome"
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 97


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % PRIME == 0:
        poly.pop()
    return [value % PRIME for value in poly]


def add(left: list[int], right: list[int]) -> list[int]:
    out = [0] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    return trim(out)


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([scalar * value for value in poly])


def mul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def derivative(poly: list[int]) -> list[int]:
    return trim([i * poly[i] for i in range(1, len(poly))] or [0])


def shift(poly: list[int], amount: int) -> list[int]:
    return [0] * amount + poly


def negate_argument(poly: list[int]) -> list[int]:
    return [value if i % 2 == 0 else -value % PRIME for i, value in enumerate(poly)]


def evaluate(poly: list[int], value: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * value + coefficient) % PRIME
    return out


def subgroup_generator(order: int) -> int:
    return next(
        value
        for value in range(2, PRIME)
        if pow(value, order, PRIME) == 1 and pow(value, order // 2, PRIME) != 1
    )


def main() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    incoming = {
        edge["from"]
        for edge in dag["edges"]
        if edge["to"] == NODE_ID and edge.get("kind") == "req"
    }
    outgoing = {
        edge["to"]
        for edge in dag["edges"]
        if edge["from"] == NODE_ID and edge.get("kind") == "ev"
    }
    assert nodes[NODE_ID]["status"] == "PROVED"
    assert incoming == {DEPENDENCY}
    assert CONSUMER in outgoing

    h = 3
    n = 8 * h - 8
    r = 2 * h - 3
    b = [1, 2, 3, 4]
    c = [1]
    v = shift(c, h)
    s, p = 5, 7
    q_minus = [1, -s % PRIME, p]
    q_plus = negate_argument(q_minus)
    e = mul([1, 0, -1 % PRIME], q_minus)

    theta = add(
        scale(mul(b, c), h),
        shift(add(mul(b, derivative(c)), scale(mul(derivative(b), c), -1)), 1),
    )
    assert len(theta) - 1 <= 3 * h - 7
    j_poly = add(
        mul(mul(q_minus, mul(c, c)), theta),
        mul(mul(q_plus, mul(negate_argument(c), negate_argument(c))), negate_argument(theta)),
    )
    assert all(coefficient == 0 for coefficient in j_poly[1::2])
    assert len(j_poly) - 1 <= 5 * h - 11

    wronskian = add(mul(b, derivative(v)), scale(mul(derivative(b), v), -1))
    assert len(wronskian) - 1 <= 2 * r - 2
    k_poly = scale(mul(mul(e, mul(v, v)), wronskian), -1)
    projected = add(k_poly, negate_argument(k_poly))
    compiled = scale(shift(mul([1, 0, -1 % PRIME], j_poly), 3 * h - 1), -1)
    assert trim(projected) == trim(compiled)
    assert len(projected) - 1 <= n - 2

    omega = subgroup_generator(n)
    subgroup = [pow(omega, exponent, PRIME) for exponent in range(n)]
    n_inv = pow(n, -1, PRIME)
    values = {}
    for x in subgroup:
        values[x] = evaluate(projected, pow(x, -1, PRIME)) * n_inv * pow(x, -1, PRIME) % PRIME
    assert values[1] == values[-1 % PRIME] == 0
    assert sum(value != 0 for value in values.values()) >= 3 * h + 1

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_BARYCENTRIC_SUPPORT_POLY_PASS "
        "toy_H=3 order=16 theta_degree=2 J_degree=4 projection=1 support_bound=10 wiring=2"
    )


if __name__ == "__main__":
    main()
