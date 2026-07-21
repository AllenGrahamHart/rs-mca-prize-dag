#!/usr/bin/env python3
"""Checks for the c2 minimum-support collision branch compiler."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NODE_ID = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_minimum_support_barycentric_collision_branch_compiler"
COLLISION_DEP = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_minimum_support_barycentric_collision_router"
FIELD_DEP = "rate_half_list_budget_three_fiber_two_cycle_c2_torsion_field_router"
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 97


def is_square(value: int) -> bool:
    return value % PRIME != 0 and pow(value % PRIME, (PRIME - 1) // 2, PRIME) == 1


def curve(y: int, z: int) -> int:
    return (
        32 * z * (z - 36) ** 2
        - (3 * y - 4) ** 2 * (3 * y + 2) * (z + 12) ** 3
    ) % PRIME


def factors(y: int, z: int) -> tuple[int, int]:
    linear = (y * (z + 12) - 2 * z + 8) % PRIME
    square = ((y * (z + 12) - 16) ** 2 - 64 * z) % PRIME
    return linear, square


def roots_of_quadratic(linear: int, constant: int) -> list[int]:
    return [
        value
        for value in range(PRIME)
        if (value * value + linear * value + constant) % PRIME == 0
    ]


def barycentric_weights(roots: list[int]) -> list[int]:
    out = []
    for i, root in enumerate(roots):
        derivative = 1
        for j, other in enumerate(roots):
            if i != j:
                derivative = derivative * (root - other) % PRIME
        out.append(pow(derivative, -1, PRIME))
    return out


def check_fixture(branch: str, y: int, pair_sum: int) -> None:
    p = PRIME
    alpha = 3
    rho = 2
    t = rho * rho % p
    x = (rho + pow(rho, -1, p)) % p
    z = x * x % p
    denominator = (z + 12) % p
    kappa = -2 * alpha * pow(denominator, -1, p) % p
    assert kappa == 1
    assert pair_sum * pair_sum % p == alpha * y % p

    linear_factor, square_factor = factors(y, z)
    if branch == "L":
        assert linear_factor == 0
        assert y * (t * t + 14 * t + 1) % p == 2 * (t - 1) ** 2 % p
    else:
        assert square_factor == 0
        left = (y * (t * t + 14 * t + 1) - 16 * t) ** 2
        assert left % p == 64 * t * (1 + t) ** 2 % p
    assert curve(y, z) == 0

    inv2 = pow(2, -1, p)
    pair_constant = (pair_sum * pair_sum + alpha * inv2) % p
    comp_constant = alpha * inv2 % p
    pair_roots = roots_of_quadratic(-pair_sum % p, pair_constant)
    comp_roots = roots_of_quadratic(pair_sum, comp_constant)
    roots = pair_roots + comp_roots
    assert len(roots) == 4 and len(set(roots)) == 4
    weights = barycentric_weights(roots)
    assert weights[0] == weights[1]
    assert weights[2] != weights[3]

    delta_pair = -alpha * (3 * y + 2) % p
    delta_comp = alpha * (y - 2) % p
    assert is_square(delta_pair) and is_square(delta_comp) and is_square(kappa)


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
    assert incoming == {COLLISION_DEP, FIELD_DEP}
    assert CONSUMER in outgoing

    for y in (0, 1, 7, 29, 96):
        for z in (0, 2, 17, 36, 85):
            linear, square = factors(y, z)
            assert curve(y, z) == -27 * linear * square % PRIME

    linear, square = factors(1, -12 % PRIME)
    assert linear == 32 and square == 1024 % PRIME

    inv3 = pow(3, -1, PRIME)
    intersections = {(0, 4), (4 * inv3 % PRIME, 36)}
    assert all(factors(y, z) == (0, 0) for y, z in intersections)
    observed = {
        (y, z)
        for y in range(PRIME)
        for z in range(PRIME)
        if factors(y, z) == (0, 0)
    }
    assert observed == intersections

    check_fixture("L", y=72, pair_sum=33)
    check_fixture("Q", y=91, pair_sum=46)

    y_antipodal = 4 * inv3 % PRIME
    assert factors(y_antipodal, 0)[1] == 0
    assert (3 * y_antipodal - 4) % PRIME == 0
    alpha = -6 % PRIME
    pair_sum = 34
    beta = -pow(pair_sum, 3, PRIME) % PRIME
    gamma = 11 * alpha * alpha * pow(12, -1, PRIME) % PRIME
    assert pair_sum * pair_sum % PRIME == 4 * alpha * inv3 % PRIME
    assert 12 * gamma % PRIME == 11 * alpha * alpha % PRIME
    assert 27 * beta * beta % PRIME == 64 * pow(alpha, 3, PRIME) % PRIME
    assert is_square(-alpha * pow(6, -1, PRIME))
    assert is_square(-2)

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_BARYCENTRIC_COLLISION_BRANCH_PASS "
        "factorization=1 branches=2 intersections=2 ratio_lift=1 square_class=1 antipodal_scalars=1 wiring=3"
    )


if __name__ == "__main__":
    main()
