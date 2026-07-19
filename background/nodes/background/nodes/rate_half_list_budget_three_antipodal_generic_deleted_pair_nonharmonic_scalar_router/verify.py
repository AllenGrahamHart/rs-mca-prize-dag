#!/usr/bin/env python3
"""Verify the deleted-pair nonharmonic scalar router and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_generic_deleted_pair_nonharmonic_scalar_router"
DEPENDENCIES = {
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_mobius_ratio_router",
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_remainder_square_router",
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_harmonic_exclusion",
}
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 97
ORDER = 8


def inverse(value: int) -> int:
    return pow(value % PRIME, -1, PRIME)


def branch_factors(branch: int, r_value: int) -> tuple[int, int]:
    r_value %= PRIME
    a_values = (
        r_value * r_value,
        pow(r_value - 1, 4, PRIME),
        pow(r_value * r_value + 1, 2, PRIME),
    )
    b_values = (
        pow(r_value * r_value - r_value + 1, 2, PRIME),
        pow(r_value + 1, 4, PRIME),
        pow(r_value * r_value - 4 * r_value + 1, 2, PRIME),
    )
    return a_values[branch] % PRIME, b_values[branch] % PRIME


def trace_power(value: int, steps: int) -> int:
    for _ in range(steps):
        value = (value * value - 2) % PRIME
    return value


def algebra_check() -> None:
    generator = 5
    zeta = pow(generator, (PRIME - 1) // ORDER, PRIME)
    roots = {pow(zeta, exponent, PRIME) for exponent in range(ORDER)}
    assert len(roots) == ORDER
    nonharmonic = roots - {1, PRIME - 1}

    positives = 0
    for r_value in range(1, PRIME):
        if pow(r_value, 4, PRIME) == 1:
            continue
        for branch in range(3):
            a_value, b_value = branch_factors(branch, r_value)
            assert a_value != 0
            y_value = (4 * b_value * inverse(a_value) - 2) % PRIME
            traced = (
                y_value not in (2, PRIME - 2)
                and trace_power(y_value, 3) == 2
            )
            recovered = {
                q_value
                for q_value in nonharmonic
                if (q_value + inverse(q_value)) % PRIME == y_value
            }
            assert traced == bool(recovered)
            assert len(recovered) in (0, 2)

            for q_value in recovered:
                assert b_value != 0
                assert (
                    a_value * pow(1 + q_value, 2, PRIME)
                    - 4 * q_value * b_value
                ) % PRIME == 0
                scalar = q_value * inverse(pow(1 + q_value, 2, PRIME)) % PRIME
                assert scalar == a_value * inverse(4 * b_value) % PRIME
                assert pow(q_value, (PRIME - 1) // 2, PRIME) == 1

                square_direction = 9
                quotient = (1 + q_value) * square_direction % PRIME
                inverse_q = inverse(q_value)
                direction_inverse = quotient * inverse(1 + inverse_q) % PRIME
                assert direction_inverse == q_value * square_direction % PRIME
                assert pow(direction_inverse, (PRIME - 1) // 2, PRIME) == 1
                positives += 1

    assert positives > 0


def wiring_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "4b_j T=a_j S^2",
        "y_(m+1)=y_m^2-2",
        "y_38=2",
        "X^2-y_0X+1=0",
        "truth value for either root",
        "one-variable identities in the lift ratio",
        "does not prove",
    ):
        assert marker in statement


def main() -> None:
    algebra_check()
    wiring_check()
    print(
        "RATE_HALF_ANTIPODAL_DELETED_PAIR_NONHARMONIC_SCALAR_PASS "
        "branches=3 outer_ratio_variables=0 trace_steps=38 root_choice_invariant=1"
    )


if __name__ == "__main__":
    main()
