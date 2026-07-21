#!/usr/bin/env python3
"""Checks for the c2 minimum-support barycentric collision router."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NODE_ID = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_minimum_support_barycentric_collision_router"
SUPPORT_DEP = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_barycentric_support_polynomial_compiler"
GAP_DEP = "rate_half_list_budget_three_fiber_two_cycle_c2_normalized_gap_span_compiler"
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 97


def outer_coefficients(roots: list[int]) -> tuple[int, int, int]:
    alpha = sum(roots[i] * roots[j] for i, j in combinations(range(4), 2))
    beta = sum(
        roots[i] * roots[j] * roots[k]
        for i, j, k in combinations(range(4), 3)
    )
    gamma = 1
    for root in roots:
        gamma *= root
    return alpha % PRIME, beta % PRIME, gamma % PRIME


def barycentric_weights(roots: list[int]) -> list[int]:
    weights = []
    for i, root in enumerate(roots):
        derivative = 1
        for j, other in enumerate(roots):
            if i != j:
                derivative = derivative * (root - other) % PRIME
        weights.append(pow(derivative, -1, PRIME))
    return weights


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
    assert incoming == {SUPPORT_DEP, GAP_DEP}
    assert CONSUMER in outgoing

    h = 5
    r = 2 * h - 3
    assert r % 2 == 1
    assert 5 * h - 11 > 2 * r - 1

    # A centered, separable fixture with exactly one repeated weight.
    roots = [1, 2, 33, 61]
    assert sum(roots) % PRIME == 0
    weights = barycentric_weights(roots)
    assert sorted(weights.count(value) for value in set(weights)) == [1, 1, 2]
    i, j = 1, 3
    assert weights[i] == weights[j]
    alpha, beta, gamma = outer_coefficients(roots)
    pair_sum = (roots[i] + roots[j]) % PRIME
    assert alpha != 0 and pair_sum != 0
    delta = (4 * gamma - alpha * alpha) % PRIME
    assert pow(pair_sum, 3, PRIME) == -beta % PRIME
    assert delta == 2 * alpha * pair_sum * pair_sum % PRIME
    assert pow(delta, 3, PRIME) == 8 * pow(alpha, 3, PRIME) * beta * beta % PRIME

    y = pair_sum * pair_sum * pow(alpha, -1, PRIME) % PRIME
    invariant_i = (alpha * alpha + 12 * gamma) % PRIME
    invariant_j = (72 * alpha * gamma - 27 * beta * beta - 2 * alpha**3) % PRIME
    assert invariant_i == 2 * alpha * alpha * (3 * y + 2) % PRIME
    assert invariant_j == -pow(alpha, 3, PRIME) * (3 * y - 4) * (3 * y + 2) ** 2 % PRIME
    assert (3 * y + 2) % PRIME != 0
    for trace_z in (0, 7, 85):
        original = (
            4 * invariant_i**3 * trace_z * (trace_z - 36) ** 2
            - invariant_j**2 * (trace_z + 12) ** 3
        ) % PRIME
        reduced = (
            32 * trace_z * (trace_z - 36) ** 2
            - (3 * y - 4) ** 2 * (3 * y + 2) * (trace_z + 12) ** 3
        ) % PRIME
        multiplier = pow(alpha, 6, PRIME) * pow(3 * y + 2, 3, PRIME) % PRIME
        assert original == multiplier * reduced % PRIME

    # A triple collision forces alpha=0 and is incompatible with alpha=4c!=0.
    cube_root = 35
    triple_roots = [1, cube_root, cube_root * cube_root % PRIME, 0]
    triple_weights = barycentric_weights(triple_roots)
    assert triple_weights[0] == triple_weights[1] == triple_weights[2]
    assert triple_weights[3] != triple_weights[0]
    alpha, beta, gamma = outer_coefficients(triple_roots)
    assert alpha == gamma == 0 and beta != 0

    # Two antipodal root pairs have opposite, not equal, derivative weights.
    two_pair_roots = [1, -1 % PRIME, 2, -2 % PRIME]
    two_pair_weights = barycentric_weights(two_pair_roots)
    assert two_pair_weights[0] == -two_pair_weights[1] % PRIME
    assert two_pair_weights[2] == -two_pair_weights[3] % PRIME

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_BARYCENTRIC_COLLISION_ROUTER_PASS "
        "degree_router=1 one_pair_normal_form=1 normalized_curve=1 larger_collisions=0 wiring=3"
    )


if __name__ == "__main__":
    main()
