#!/usr/bin/env python3
"""Verify the nonharmonic trace/fourth-power router and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_generic_deleted_pair_nonharmonic_fourth_power_router"
DEPENDENCY = "rate_half_list_budget_three_antipodal_generic_deleted_pair_nonharmonic_scalar_router"
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 97
ORDER = 8


def inverse(value: int) -> int:
    return pow(value % PRIME, -1, PRIME)


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, value in enumerate(left):
        for j, other in enumerate(right):
            answer[i + j] = (answer[i + j] + value * other) % PRIME
    return answer


def scale(poly: list[int], scalar: int) -> list[int]:
    return [scalar * value % PRIME for value in poly]


def branch_data(branch: int, chi: int) -> tuple[int, int]:
    if branch == 0:
        h_value = inverse(2 * (chi - 1))
        y_value = 4 * (chi - 1) ** 2 - 2
    elif branch == 1:
        h_value = (chi - 2) * inverse(2 * (chi + 2))
        y_value = 4 * (chi + 2) ** 2 * inverse((chi - 2) ** 2) - 2
    else:
        h_value = chi * inverse(2 * (chi - 4))
        y_value = 4 * (chi - 4) ** 2 * inverse(chi * chi) - 2
    return h_value % PRIME, y_value % PRIME


def mobius_gate(branch: int, r_value: int, q_value: int) -> bool:
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
    return (
        a_values[branch] * pow(1 + q_value, 2, PRIME)
        - 4 * q_value * b_values[branch]
    ) % PRIME == 0


def trace_power(value: int, steps: int) -> int:
    for _ in range(steps):
        value = (value * value - 2) % PRIME
    return value


def algebra_check() -> None:
    generator = 5
    zeta = pow(generator, (PRIME - 1) // ORDER, PRIME)
    q_roots = {pow(zeta, exponent, PRIME) for exponent in range(ORDER)}
    q_roots -= {1, PRIME - 1}
    fourth_roots = {
        value: next(eta for eta in range(1, PRIME) if pow(eta, 4, PRIME) == value)
        for value in q_roots
    }

    positives = 0
    square_poly = multiply([3, 1], [3, 1])
    fourth_poly = multiply(square_poly, square_poly)
    for r_value in range(1, PRIME):
        if pow(r_value, 4, PRIME) == 1:
            continue
        chi = (r_value + inverse(r_value)) % PRIME
        for branch in range(3):
            for q_value in q_roots:
                if not mobius_gate(branch, r_value, q_value):
                    continue
                h_value, y_value = branch_data(branch, chi)
                assert y_value == (q_value + inverse(q_value)) % PRIME
                assert trace_power(y_value, 3) == 2
                scalar = q_value * inverse(pow(1 + q_value, 2, PRIME)) % PRIME
                assert h_value * h_value % PRIME == scalar

                z_poly = square_poly
                s_poly = scale(z_poly, 1 + q_value)
                t_poly = scale(multiply(z_poly, z_poly), q_value)
                assert t_poly == multiply(
                    scale(s_poly, h_value), scale(s_poly, h_value)
                )
                eta = fourth_roots[q_value]
                assert t_poly == scale(fourth_poly, pow(eta, 4, PRIME))

                # Conversely, a fourth power satisfying the scalar identity
                # makes S/(1+q) a square; the remaining scalar has square class 1.
                converse_s = scale(square_poly, inverse(h_value))
                converse_z = scale(converse_s, inverse(1 + q_value))
                z_scalar = inverse(h_value * (1 + q_value)) % PRIME
                assert pow(z_scalar, (PRIME - 1) // 2, PRIME) == 1
                assert converse_z == scale(square_poly, z_scalar)
                positives += 1

    assert positives > 0


def wiring_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "chi=r+r^(-1)",
        "h_0=1/(2(chi-1))",
        "y_(j,38)=2",
        "T=W^4",
        "4(chi-1)^2T=S^2",
        "root-dependent polynomial-square test remains",
        "does not prove",
    ):
        assert marker in statement


def main() -> None:
    algebra_check()
    wiring_check()
    print(
        "RATE_HALF_ANTIPODAL_DELETED_PAIR_NONHARMONIC_FOURTH_POWER_PASS "
        "branches=3 outer_roots=0 final_square_tests=0 fourth_power_tests=1"
    )


if __name__ == "__main__":
    main()
