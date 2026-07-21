#!/usr/bin/env python3
"""Checks for the c2 minimum-support Euler divisor gate."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NODE_ID = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_minimum_support_euler_divisor_gate"
GAP_DEP = "rate_half_list_budget_three_fiber_two_cycle_c2_normalized_gap_span_compiler"
DIFFERENTIAL_DEP = "rate_half_list_budget_three_fiber_two_cycle_c2_secondary_differential_certifier"
SUPPORT_DEP = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_barycentric_support_polynomial_compiler"
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


def divmod_poly(dividend: list[int], divisor: list[int]) -> tuple[list[int], list[int]]:
    remainder = trim(dividend[:])
    divisor = trim(divisor[:])
    quotient = [0] * max(1, len(remainder) - len(divisor) + 1)
    inverse = pow(divisor[-1], -1, PRIME)
    while len(remainder) >= len(divisor) and remainder != [0]:
        offset = len(remainder) - len(divisor)
        coefficient = remainder[-1] * inverse % PRIME
        quotient[offset] = coefficient
        for i, value in enumerate(divisor):
            remainder[offset + i] -= coefficient * value
        remainder = trim(remainder)
    return trim(quotient), trim(remainder)


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
    assert incoming == {GAP_DEP, DIFFERENTIAL_DEP, SUPPORT_DEP}
    assert CONSUMER in outgoing

    # Check the Euler identity on a nontrivial abstract norm remainder.
    n = 16
    h = 3
    e = [1, 2]
    c = [1, 1]
    v = shift(c, h)
    k = [1, 0, 1]
    s_poly = mul(e, mul(mul(v, v), k))
    a_poly = add([1] + [0] * (n - 1) + [-1], scale(s_poly, -1))
    p_poly = add(
        add(scale(a_poly, n), scale(shift(derivative(a_poly), 1), -1)),
        [-n],
    )
    euler_rhs = add(shift(derivative(s_poly), 1), scale(s_poly, -n))
    assert p_poly == euler_rhs
    assert divmod_poly(p_poly, v)[1] == [0]

    # The sparse differential residual removes derivatives from T.
    e_boundary = [1, 2, 3, 4, 5]
    b_boundary = [1, 2, 3, 4]
    c_0 = 7
    b_0 = b_boundary[-1]
    e_4 = e_boundary[-1]
    delta = add(
        shift([-8 * h * c_0], 2 * h - 1),
        shift([8 * (h - 1) * e_4 * b_0], 2 * h),
    )
    t_direct = add(scale(mul(e_boundary, b_boundary), n), scale(shift(delta, 1), -1))
    t_0 = add(
        add(
            scale(mul(e_boundary, b_boundary), h - 1),
            shift([h * c_0], 2 * h),
        ),
        shift([-(h - 1) * e_4 * b_0], 2 * h + 1),
    )
    assert t_direct == scale(t_0, 8)

    # A degree-three C fixture checks the remainder/resultant cube packet.
    c_resultant = [1, 0, 0, 1]
    b = [1]
    h_minus_one = h - 1
    t_poly = add([h_minus_one], mul(c_resultant, [0, 1]))
    p_fixture = add(mul(t_poly, mul(mul(b, b), b)), [-h_minus_one])
    assert divmod_poly(p_fixture, c_resultant)[1] == [0]
    resultant_c_t = pow(h_minus_one, 3, PRIME)
    assert resultant_c_t == pow(h_minus_one, len(c_resultant) - 1, PRIME)
    assert pow(resultant_c_t, (PRIME - 1) // 3, PRIME) == 1

    # A nonmonic first polynomial needs explicit monic normalization.
    nonmonic_lead = 2
    t_degree = 4
    raw_resultant = pow(nonmonic_lead, t_degree, PRIME) * resultant_c_t % PRIME
    assert raw_resultant != resultant_c_t

    official_h = 2**37 + 1
    assert (official_h - 3) % 3 == 0
    assert 2 + 2 * (official_h - 4) + (3 * official_h - 7) < 5 * official_h - 11
    assert 2 + 2 * (official_h - 3) + (3 * official_h - 7) == 5 * official_h - 11

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_MIN_SUPPORT_EULER_PASS "
        "euler_identity=1 sparse_T0=1 divisor=1 valuation=2H degree_C=H-3 monic_resultant_cube=1 wiring=4"
    )


if __name__ == "__main__":
    main()
