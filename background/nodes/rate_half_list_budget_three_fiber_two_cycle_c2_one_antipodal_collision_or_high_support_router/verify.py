#!/usr/bin/env python3
"""Checks for the c2 one-antipodal collision-or-high-support router."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NODE_ID = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_collision_or_high_support_router"
CELL_DEP = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_canonical_cell_fourier_ladder"
SUPPORT_DEP = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_barycentric_support_polynomial_compiler"
GAP_DEP = "rate_half_list_budget_three_fiber_two_cycle_c2_normalized_gap_span_compiler"
FIELD_DEP = "rate_half_list_budget_three_fiber_two_cycle_c2_torsion_field_router"
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


def branch_factors(y: int, z: int) -> tuple[int, int, int]:
    curve = 32 * z * (z - 36) ** 2 - (3 * y - 4) ** 2 * (3 * y + 2) * (z + 12) ** 3
    linear = y * (z + 12) - 2 * z + 8
    square = (y * (z + 12) - 16) ** 2 - 64 * z
    return curve % PRIME, linear % PRIME, square % PRIME


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
    assert incoming == {CELL_DEP, SUPPORT_DEP, GAP_DEP, FIELD_DEP}
    assert CONSUMER in outgoing

    h = 5
    n = 8 * h - 8
    r = 2 * h - 3
    assert n - 2 - (4 * h - 8) == 4 * h - 2
    assert (4 * h - 8) % 2 == 0 and 2 * r - 1 == 4 * h - 7

    b = [1, 3, 4, 8, 2, 9, 7, 5]
    c = [1, 6, 11]
    v = [0] * h + c
    d_poly = add(mul(b, negate_argument(v)), scale(mul(negate_argument(b), v), -1))
    assert d_poly != [0] and len(d_poly) - 1 <= 2 * r - 1
    assert all(value == 0 for i, value in enumerate(d_poly) if i % 2 == 0)
    generator = subgroup_generator(n)
    roots = [pow(generator, exponent, PRIME) for exponent in range(n)]
    zero_count = sum(evaluate(d_poly, root) == 0 for root in roots)
    assert zero_count % 2 == 0 and zero_count <= 4 * h - 8

    for y in (0, 1, 7, 29, 96):
        for z in (0, 2, 17, 36, 85):
            curve, linear, square = branch_factors(y, z)
            assert curve == -27 * linear * square % PRIME

    inv3 = pow(3, -1, PRIME)
    y_antipodal = 4 * inv3 % PRIME
    curve, linear, square = branch_factors(y_antipodal, 0)
    assert curve == 0 and linear != 0 and square == 0

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_COLLISION_OR_HIGH_SUPPORT_PASS "
        "support_floor=18 parity=1 wronskian=1 branches=2 antipodal=1 wiring=5"
    )


if __name__ == "__main__":
    main()
