#!/usr/bin/env python3
"""Checks for the official c=2 pure fourth-root primary exclusion."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NODE_ID = "rate_half_list_budget_three_fiber_two_cycle_c2_pure_fourth_root_primary_exclusion"
DEPENDENCIES = {
    "rate_half_list_budget_three_maximal_field_degree_collapse",
    "rate_half_list_budget_three_fiber_two_cycle_c2_normalized_gap_span_compiler",
}
CONSUMER = "rate_half_list_adjacent_crossing"


def pure_coefficient(index: int) -> Fraction:
    if index % 4:
        return Fraction(0)
    degree = index // 4
    out = Fraction(1)
    for value in range(degree):
        out *= Fraction(4 * value + 1, 4 * (value + 1))
    return out


def coefficient_mod_prime(index: int, prime: int) -> int:
    if index % 4:
        return 0
    degree = index // 4
    out = 1
    for value in range(degree):
        out = out * (4 * value + 1) % prime
        out = out * pow(4 * (value + 1), -1, prime) % prime
    return out


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
    official_height = (1 << 37) + 1
    official_index = 2 * official_height - 2
    official_degree = official_index // 4
    assert official_index == 1 << 38
    assert official_degree == 1 << 36
    assert official_height % 2 == 1

    checks = 0
    for height in range(3, 17):
        index = 2 * height - 2
        coefficient = pure_coefficient(index)
        assert (coefficient != 0) == (height % 2 == 1)
        checks += 1

    for prime in (97, 193, 257):
        for height in range(3, 13):
            index = 2 * height - 2
            if index >= prime:
                continue
            coefficient = coefficient_mod_prime(index, prime)
            assert (coefficient != 0) == (height % 2 == 1)
            checks += 1

    # The proof uses inequalities, not an impossible official-size loop.
    official_prime_floor = (1 << 40) + 1
    assert 4 * official_degree < official_prime_floor
    assert official_degree < official_prime_floor

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_PURE_FOURTH_ROOT_EXCLUSION_PASS "
        f"small_checks={checks} official_degree={official_degree} wiring=3"
    )


if __name__ == "__main__":
    main()
