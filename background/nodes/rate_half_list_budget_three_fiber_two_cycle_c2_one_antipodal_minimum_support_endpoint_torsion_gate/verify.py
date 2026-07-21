#!/usr/bin/env python3
"""Checks for the c2 minimum-support endpoint torsion gate."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NODE_ID = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_minimum_support_endpoint_torsion_gate"
SUPPORT_DEP = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_barycentric_support_polynomial_compiler"
EULER_DEP = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_minimum_support_euler_divisor_gate"
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


def polynomial_from_roots(roots: list[int]) -> list[int]:
    out = [1]
    for root in roots:
        out = mul(out, [-root % PRIME, 1])
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
    assert incoming == {SUPPORT_DEP, EULER_DEP}
    assert CONSUMER in outgoing

    h = 5
    r = 2 * h - 3
    m = h - 3
    b = [1, 2, 3, 4, 5, 6, 7, 8]
    c = [1, 9, 11]
    q_minus = [1, -13 % PRIME, 17]
    q_plus = negate_argument(q_minus)
    theta = add(
        scale(mul(b, c), h),
        shift(add(mul(b, derivative(c)), scale(mul(derivative(b), c), -1)), 1),
    )
    delta_inf = (b[r - 1] * c[m] - b[r] * c[m - 1]) % PRIME
    assert theta[3 * h - 7] == delta_inf and delta_inf != 0
    j_supp = add(
        mul(mul(q_minus, mul(c, c)), theta),
        mul(
            mul(q_plus, mul(negate_argument(c), negate_argument(c))),
            negate_argument(theta),
        ),
    )
    assert len(j_supp) - 1 == 5 * h - 11
    assert j_supp[0] == 2 * h % PRIME
    expected_lead = 2 * q_minus[-1] * c[m] * c[m] * delta_inf % PRIME
    assert j_supp[-1] == expected_lead

    n = 8 * h - 8
    generator = subgroup_generator(n)
    exponents = [1, 2, 3, 4, 5, 6, 8]
    roots = []
    for exponent in exponents:
        root = pow(generator, exponent, PRIME)
        roots.extend((root, -root % PRIME))
    split_poly = polynomial_from_roots(roots)
    xi = 1
    for root in roots:
        xi = xi * root % PRIME
    assert split_poly[0] * pow(split_poly[-1], -1, PRIME) % PRIME == xi
    assert pow(xi, n // 2, PRIME) == 1
    assert pow(xi, n // 4, PRIME) != 1

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_MIN_SUPPORT_ENDPOINT_TORSION_PASS "
        "theta_endpoint=1 support_endpoints=2 negation_pairs=7 half_order=1 wiring=3"
    )


if __name__ == "__main__":
    main()
