#!/usr/bin/env python3
"""Verify the deleted-pair constant-coefficient gate and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_coefficient_gate"
DEPENDENCY = "rate_half_list_budget_three_antipodal_generic_deleted_pair_nonharmonic_fourth_power_router"
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 97


def inverse(value: int) -> int:
    return pow(value % PRIME, -1, PRIME)


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % PRIME == 0:
        poly.pop()
    return [value % PRIME for value in poly]


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    return trim([
        (left[i] if i < len(left) else 0)
        + (right[i] if i < len(right) else 0)
        for i in range(size)
    ])


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([scalar * value for value in poly])


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, value in enumerate(left):
        for j, other in enumerate(right):
            answer[i + j] += value * other
    return trim(answer)


def reverse(poly: list[int], degree: int) -> list[int]:
    return [poly[degree - index] if degree - index < len(poly) else 0 for index in range(degree + 1)]


def truncated_divide(numerator: list[int], denominator: list[int], length: int) -> list[int]:
    assert denominator[0] % PRIME == 1
    quotient: list[int] = []
    for index in range(length):
        value = numerator[index] if index < len(numerator) else 0
        value -= sum(
            denominator[j] * quotient[index - j]
            for j in range(1, min(index, len(denominator) - 1) + 1)
        )
        quotient.append(value % PRIME)
    return quotient


def algebra_check() -> None:
    # Audit the reversed quotient at a=7, s=2.
    a_degree = 7
    s_degree = 2
    a_poly = [0, 3, 4, 1, 2, 5, 7, 1]
    s_poly = [11, 13, 1]
    t_poly = [9, 8, 7, 6, 5, 4, 3]
    r_poly = add(multiply(a_poly, s_poly), t_poly)
    a_rev = reverse(a_poly, a_degree)
    r_rev = reverse(r_poly, a_degree + s_degree)
    s_rev = truncated_divide(r_rev, a_rev, s_degree + 1)
    assert s_rev == reverse(s_poly, s_degree)
    assert s_rev[s_degree] == s_poly[0]

    # Each printed gate is exactly the constant scalar identity plus T(0)=-1/t.
    sigma = 17
    for r_value in range(1, PRIME):
        if pow(r_value, 4, PRIME) == 1:
            continue
        t_value = pow(r_value, 4, PRIME)
        chi = (r_value + inverse(r_value)) % PRIME
        branch_data = (
            (1, 2 * (chi - 1), 4 * (chi - 1) ** 2),
            (chi - 2, 2 * (chi + 2), 4 * (chi + 2) ** 2),
            (chi, 2 * (chi - 4), 4 * (chi - 4) ** 2),
        )
        for numerator, denominator, left_factor in branch_data:
            if denominator % PRIME == 0:
                continue
            h_value = numerator * inverse(denominator) % PRIME
            t_zero = h_value * h_value * sigma * sigma % PRIME
            gate = (
                t_value * numerator * numerator * sigma * sigma
                + left_factor
            ) % PRIME
            scaled_constant_identity = (
                t_value * left_factor * (t_zero + inverse(t_value))
            ) % PRIME
            assert gate == scaled_constant_identity


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
        "D_0=(x-1)(x-t)",
        "sigma=[z^s](R_rev/A_rev mod z^(s+1))",
        "sigma=S(0)",
        "t sigma^2+4(chi-1)^2=0",
        "t(chi-2)^2 sigma^2+4(chi+2)^2=0",
        "t chi^2 sigma^2+4(chi-4)^2=0",
        "rejection gate",
        "does not prove",
    ):
        assert marker in statement


def main() -> None:
    algebra_check()
    wiring_check()
    print(
        "RATE_HALF_ANTIPODAL_DELETED_PAIR_CONSTANT_COEFFICIENT_PASS "
        "branches=3 quotient_coefficients=1 full_remainders=0"
    )


if __name__ == "__main__":
    main()
