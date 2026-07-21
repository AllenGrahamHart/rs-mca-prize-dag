#!/usr/bin/env python3
"""Checks for the c2 one-antipodal degree-defect global gate router."""

from __future__ import annotations

import json
from math import isqrt
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NODE_ID = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_degree_defect_global_gate_router"
SUPPORT_DEP = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_barycentric_support_polynomial_compiler"
COLLISION_DEP = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_collision_or_high_support_router"
DIFFERENTIAL_DEP = "rate_half_list_budget_three_fiber_two_cycle_c2_secondary_differential_certifier"
FIELD_DEP = "rate_half_list_budget_three_maximal_field_degree_collapse"
STEPANOV_DEP = "f3_h2_stepanov_inhouse"
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 97


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % PRIME == 0:
        poly.pop()
    return [value % PRIME for value in poly]


def add(left: list[int], right: list[int]) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
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
    return trim([index * value for index, value in enumerate(poly)][1:] or [0])


def shift(poly: list[int]) -> list[int]:
    return [0] + poly


def negate_argument(poly: list[int]) -> list[int]:
    return trim([value if index % 2 == 0 else -value for index, value in enumerate(poly)])


def polynomial_from_roots(roots: list[int]) -> list[int]:
    out = [1]
    for root in roots:
        out = mul(out, [-root, 1])
    return out


def derivative_values(roots: list[int]) -> list[int]:
    return [
        product_mod(root - other for j, other in enumerate(roots) if i != j)
        for i, root in enumerate(roots)
    ]


def product_mod(values) -> int:
    out = 1
    for value in values:
        out = out * value % PRIME
    return out


def floor_rational_cuberoot(numerator: int, denominator: int) -> int:
    low, high = 0, 1
    while denominator * high**3 <= numerator:
        high *= 2
    while low + 1 < high:
        middle = (low + high) // 2
        if denominator * middle**3 <= numerator:
            low = middle
        else:
            high = middle
    return low


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
    assert incoming == {SUPPORT_DEP, COLLISION_DEP, DIFFERENTIAL_DEP, FIELD_DEP, STEPANOV_DEP}
    assert CONSUMER in outgoing

    h = 5
    n = 8 * h - 8
    expected_floors = {0: 3 * h + 1, 1: 3 * h + 3, 2: 3 * h + 7}
    b = [1, 3, 4, 8, 2, 9, 7, 5]
    q_minus = [1, -3, 5]
    for defect, c in ((0, [1, 6, 11]), (1, [1, 6]), (2, [1])):
        epsilon = int(defect % 2 == 0)
        degree_ceiling = 5 * h - 10 - 3 * defect - epsilon
        theta = add(
            scale(mul(b, c), h),
            shift(add(mul(b, derivative(c)), scale(mul(derivative(b), c), -1))),
        )
        first = mul(mul(q_minus, mul(c, c)), theta)
        j_poly = add(first, negate_argument(first))
        assert all(value == 0 for index, value in enumerate(j_poly) if index % 2)
        assert len(j_poly) - 1 <= degree_ceiling
        if defect == 1:
            assert len(j_poly) - 1 == degree_ceiling
        floor = n - 2 - degree_ceiling
        assert floor == expected_floors[defect]
        assert degree_ceiling % 2 == 0 and floor % 2 == 0

    official_h = (1 << 37) + 1
    assert (official_h - 3) % 3 == 0

    # Exact order-32 infinity control: distinct roots and one derivative pair.
    ell = [12, 67, 42, 28]
    assert all(pow(value, 32, PRIME) == 1 for value in ell)
    direct = polynomial_from_roots(ell)
    derivatives = derivative_values(ell)
    multiplicities = sorted(
        (derivatives.count(value) for value in set(derivatives)), reverse=True
    )
    assert multiplicities == [2, 1, 1]
    p_src = pow(direct[0], -1, PRIME)
    assert product_mod(ell) == pow(p_src, -1, PRIME)

    inverse_six = pow(6, -1, PRIME)
    d = (ell[0] - ell[1]) * inverse_six % PRIME
    a = (ell[0] + ell[1] - ell[2] - ell[3]) * pow(4 * d, -1, PRIME) % PRIME
    tau = ell[3]
    y = ell[2] * pow(tau, -1, PRIME) % PRIME
    affine_a = ((a + 2) * y - (a + 1)) % PRIME
    affine_b = ((a - 1) * y + (2 - a)) % PRIME
    assert a * a % PRIME == -2 % PRIME
    assert [tau * affine_a % PRIME, tau * affine_b % PRIME, tau * y % PRIME, tau] == ell
    assert pow(p_src * y * affine_a * affine_b % PRIME, 8, PRIME) == 1

    order = 1 << 40
    a_0 = floor_rational_cuberoot(27 * order * order, 64)
    b_0 = floor_rational_cuberoot(125 * order, 64) + 1
    d_0 = a_0
    p_min = isqrt(3 * (1 << 128) - 1) + 1
    assert (a_0, b_0, d_0) == (79_896_510, 12_902, 79_896_510)
    assert a_0 + order * b_0 < p_min
    assert (a_0 + 2 * order * b_0) // d_0 == 355_106_851

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_DEGREE_DEFECT_GLOBAL_GATE_PASS "
        "defects=3 parity=1 euler=1 infinity=1 affine=1 cap=355106851 wiring=6"
    )


if __name__ == "__main__":
    main()
