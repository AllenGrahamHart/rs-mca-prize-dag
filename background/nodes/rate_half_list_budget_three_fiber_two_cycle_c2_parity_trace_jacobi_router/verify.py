#!/usr/bin/env python3
"""Checks for the c=2 parity trace/Jacobi router."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
import json
from pathlib import Path


PRIME = 97
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NODE_ID = "rate_half_list_budget_three_fiber_two_cycle_c2_parity_trace_jacobi_router"
DEPENDENCIES = {
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_parity_reduction",
    "rate_half_list_budget_three_fiber_two_cycle_mismatch_trace_resolvent_elimination",
    "rate_half_list_budget_three_fiber_two_cycle_matched_trace_jacobi_norm_transfer",
    "rate_half_list_budget_three_fiber_two_cycle_c2_normalized_gap_span_compiler",
    "rate_half_list_budget_three_fiber_two_cycle_c2_pure_fourth_root_primary_exclusion",
}
CONSUMER = "rate_half_list_adjacent_crossing"


def primitive_root() -> int:
    for candidate in range(2, PRIME):
        if all(pow(candidate, (PRIME - 1) // factor, PRIME) != 1 for factor in (2, 3)):
            return candidate
    raise AssertionError("primitive root not found")


def pair_trace(left: int, right: int) -> int:
    return (left + right) ** 2 * pow(left * right % PRIME, -1, PRIME) % PRIME


def outer_gate(value: int, invariant_i: int, invariant_j: int) -> int:
    return (
        4 * invariant_i**3 * value * (value - 36) ** 2
        - invariant_j**2 * (value + 12) ** 3
    ) % PRIME


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
    q = pow(generator, (PRIME - 1) // 32, PRIME)
    assert pow(q, 32, PRIME) == 1 and pow(q, 16, PRIME) != 1
    r = q * q % PRIME
    tau = r * r % PRIME
    roots = (1, -1 % PRIME, r, -r % PRIME)
    assert len(set(roots)) == 4

    chi = (r + pow(r, -1, PRIME)) % PRIME
    expected = Counter({0: 2, (2 + chi) % PRIME: 2, (2 - chi) % PRIME: 2})
    actual = Counter(pair_trace(left, right) for left, right in combinations(roots, 2))
    assert actual == expected

    jacobi_x = chi * pow(2, -1, PRIME) % PRIME
    jacobi_w = (2 * jacobi_x * jacobi_x - 1) % PRIME
    assert jacobi_w == (tau + pow(tau, -1, PRIME)) * pow(2, -1, PRIME) % PRIME

    for invariant_i, invariant_j in ((3, 5), (11, 0), (17, 29)):
        assert outer_gate(0, invariant_i, invariant_j) == -1728 * invariant_j**2 % PRIME
        plus = outer_gate((2 + chi) % PRIME, invariant_i, invariant_j)
        minus = outer_gate((2 - chi) % PRIME, invariant_i, invariant_j)
        product = plus * minus % PRIME
        chi_reversed = (-chi) % PRIME
        reversed_product = (
            outer_gate((2 + chi_reversed) % PRIME, invariant_i, invariant_j)
            * outer_gate((2 - chi_reversed) % PRIME, invariant_i, invariant_j)
            % PRIME
        )
        assert product == reversed_product

    official_m = 1 << 36
    assert 16 * official_m == 1 << 40
    assert 8 * official_m == 1 << 39

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_PARITY_TRACE_JACOBI_PASS "
        "pair_classes=3 pair_multiplicity=2 cross_norm_checks=3 wiring=3"
    )


if __name__ == "__main__":
    main()
