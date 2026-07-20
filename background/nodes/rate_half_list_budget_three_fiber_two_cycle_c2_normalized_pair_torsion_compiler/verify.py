#!/usr/bin/env python3
"""Exact checks for the c=2 normalized pair-torsion compiler."""

from __future__ import annotations

import importlib.util
import json
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NODE_ID = "rate_half_list_budget_three_fiber_two_cycle_c2_normalized_pair_torsion_compiler"
DEPENDENCIES = {
    "rate_half_list_budget_three_antipodal_generic_canonical_span_criterion",
    "rate_half_list_budget_three_fiber_two_cycle_c2_joint_pair_torsion_selector",
}
CONSUMER = "rate_half_list_adjacent_crossing"
DEPENDENCY = (
    HERE.parent
    / "rate_half_list_budget_three_fiber_two_cycle_mismatch_trace_resolvent_elimination"
    / "verify.py"
)
SPEC = importlib.util.spec_from_file_location("mismatch_trace_algebra", DEPENDENCY)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load mismatch trace algebra")
algebra = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(algebra)

PRIME = algebra.PRIME


def primitive_root() -> int:
    for candidate in range(2, PRIME):
        if all(
            pow(candidate, (PRIME - 1) // factor, PRIME) != 1
            for factor in (2, 3, 7)
        ):
            return candidate
    raise AssertionError("primitive root not found")


def torsion_recurrence(
    t: int,
    total: int,
    product: int,
    levels: int,
    recurrence_constant: int = 2,
) -> tuple[int, int, int]:
    for _ in range(levels):
        t = t * t % PRIME
        total = (total * total - recurrence_constant * product) % PRIME
        product = product * product % PRIME
    return t, total, product


def normalized_coordinates(
    a: int, b: int, c: int, d: int
) -> tuple[int, int, int]:
    inverse = pow(a, -1, PRIME)
    t = b * inverse % PRIME
    c_normalized = c * inverse % PRIME
    d_normalized = d * inverse % PRIME
    return (
        t,
        (c_normalized + d_normalized) % PRIME,
        c_normalized * d_normalized % PRIME,
    )


def orientation_reverse(t: int, total: int, product: int) -> tuple[int, int, int]:
    inverse = pow(t, -1, PRIME)
    return (
        inverse,
        total * inverse % PRIME,
        product * inverse * inverse % PRIME,
    )


def distinctness_product(t: int, total: int, product: int) -> int:
    factors = (
        t,
        product,
        t - 1,
        1 - total + product,
        t * t - total * t + product,
        total * total - 4 * product,
    )
    value = 1
    for factor in factors:
        value = value * factor % PRIME
    return value


def normalized_denominator(t: int, total: int, product: int) -> list[int]:
    return algebra.poly_mul(
        algebra.poly_mul([-1, 1], [-t % PRIME, 1]),
        [product, -total % PRIME, 1],
    )


def scaled_outer(
    alpha: int, beta: int, gamma: int, scale: int, h: int
) -> tuple[int, int, int]:
    return (
        pow(scale, 2 * h, PRIME) * alpha % PRIME,
        pow(scale, 3 * h, PRIME) * beta % PRIME,
        pow(scale, 4 * h, PRIME) * gamma % PRIME,
    )


def centered_invariants(alpha: int, beta: int, gamma: int) -> tuple[int, int]:
    return (
        (alpha * alpha + 12 * gamma) % PRIME,
        (72 * alpha * gamma - 27 * beta * beta - 2 * alpha**3) % PRIME,
    )


def check_wiring() -> None:
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
    assert incoming == DEPENDENCIES
    assert CONSUMER in outgoing


def main() -> None:
    check_wiring()
    generator = primitive_root()
    subgroup = [pow(generator, (PRIME - 1) // 8 * index, PRIME) for index in range(8)]
    levels = 3
    packets = 0

    for roots in combinations(subgroup, 4):
        for a, b in combinations(roots, 2):
            c, d = tuple(root for root in roots if root not in (a, b))
            t, total, product = normalized_coordinates(a, b, c, d)
            assert torsion_recurrence(t, total, product, levels) == (1, 2, 1)
            assert distinctness_product(t, total, product) != 0

            normalized_roots = (
                1,
                t,
                c * pow(a, -1, PRIME) % PRIME,
                d * pow(a, -1, PRIME) % PRIME,
            )
            direct = [1]
            for root in normalized_roots:
                direct = algebra.poly_mul(direct, [-root % PRIME, 1])
            assert normalized_denominator(t, total, product) == direct

            reverse = orientation_reverse(t, total, product)
            assert reverse == normalized_coordinates(b, a, c, d)
            assert orientation_reverse(*reverse) == (t, total, product)
            packets += 1

    alpha, beta, gamma = 17, 29, 43
    h = 11
    for scale in subgroup:
        invariant_i, invariant_j = centered_invariants(alpha, beta, gamma)
        scaled = scaled_outer(alpha, beta, gamma, scale, h)
        scaled_i, scaled_j = centered_invariants(*scaled)
        assert scaled_i == pow(scale, 4 * h, PRIME) * invariant_i % PRIME
        assert scaled_j == pow(scale, 6 * h, PRIME) * invariant_j % PRIME
        original_cubic = algebra.outer_cubic(invariant_i, invariant_j)
        scaled_cubic = algebra.outer_cubic(scaled_i, scaled_j)
        weight = pow(scale, 12 * h, PRIME)
        assert scaled_cubic == [weight * value % PRIME for value in original_cubic]

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_NORMALIZED_PAIR_TORSION_PASS "
        f"packets={packets} covariance_checks={len(subgroup)} "
        f"levels={levels} official_levels=40 wiring=3"
    )


if __name__ == "__main__":
    main()
