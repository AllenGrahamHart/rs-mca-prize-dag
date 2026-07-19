#!/usr/bin/env python3
"""Verify the deleted-pair Legendre coefficient collapse and DAG wiring."""

from __future__ import annotations

from math import comb
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_coefficient_legendre_collapse"
GAP = "rate_half_list_budget_three_antipodal_fourth_root_gap_reduction"
CONSTANT = "rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_coefficient_gate"
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 257


def inverse(value: int) -> int:
    return pow(value % PRIME, -1, PRIME)


def multiply(left: list[int], right: list[int], length: int) -> list[int]:
    answer = [0] * length
    for i, value in enumerate(left):
        for j, other in enumerate(right):
            if i + j >= length:
                break
            answer[i + j] = (answer[i + j] + value * other) % PRIME
    return answer


def power(poly: list[int], exponent: int, length: int) -> list[int]:
    answer = [1] + [0] * (length - 1)
    base = poly[:length] + [0] * max(0, length - len(poly))
    while exponent:
        if exponent & 1:
            answer = multiply(answer, base, length)
        base = multiply(base, base, length)
        exponent //= 2
    return answer


def divide(numerator: list[int], denominator: list[int], length: int) -> list[int]:
    assert denominator[0] % PRIME == 1
    answer: list[int] = []
    for n in range(length):
        value = numerator[n] if n < len(numerator) else 0
        value -= sum(
            denominator[j] * answer[n - j]
            for j in range(1, min(n, len(denominator) - 1) + 1)
        )
        answer.append(value % PRIME)
    return answer


def fourth_root_coefficients(t_value: int, limit: int) -> list[int]:
    eta_1 = -(1 + t_value) % PRIME
    eta_2 = t_value % PRIME
    answer = [1]
    for n in range(1, limit + 1):
        numerator = (4 * n - 3) * eta_1 * answer[n - 1]
        if n >= 2:
            numerator += (4 * n - 6) * eta_2 * answer[n - 2]
        answer.append(-numerator * inverse(4 * n) % PRIME)
    return answer


def half_root_coefficients(t_value: int, limit: int) -> list[int]:
    answer = [1, (1 + t_value) * inverse(2) % PRIME]
    for n in range(1, limit):
        next_value = (
            (2 * n + 1) * (1 + t_value) * answer[n]
            - 2 * n * t_value * answer[n - 1]
        ) * inverse(2 * (n + 1))
        answer.append(next_value % PRIME)
    return answer[: limit + 1]


def algebra_check() -> None:
    # M=2 and t=156 give a formal primary-gap fixture: [z^4]E^(-1/4)=0.
    m_value = 3
    a_value = 7
    s_value = 2
    h_value = 5
    t_value = 156
    length = a_value + 1

    f_coefficients = fourth_root_coefficients(t_value, a_value)
    assert f_coefficients[m_value + 1] == 0
    b_poly = f_coefficients[: m_value + 1]
    b_squared = multiply(b_poly, b_poly, length)
    b_fourth = multiply(b_squared, b_squared, length)
    e_inverse = power(f_coefficients, 4, length)

    difference = [
        (e_inverse[index] - b_fourth[index]) % PRIME
        for index in range(length)
    ]
    assert difference[:h_value] == [0] * h_value
    r_reversed = difference[h_value : h_value + s_value + 1]
    s_reversed = divide(r_reversed, b_squared, s_value + 1)
    sigma = s_reversed[s_value]

    quotient = divide(e_inverse, b_squared, length)
    direct_sigma = (quotient[a_value] - b_squared[a_value]) % PRIME
    h_coefficients = half_root_coefficients(t_value, a_value)
    assert multiply(f_coefficients, f_coefficients, length) == h_coefficients
    assert sigma == direct_sigma == 2 * h_coefficients[a_value] % PRIME

    explicit = sum(
        comb(2 * j, j)
        * inverse(pow(4, j, PRIME))
        * comb(2 * (a_value - j), a_value - j)
        * inverse(pow(4, a_value - j, PRIME))
        * pow(t_value, j, PRIME)
        for j in range(a_value + 1)
    ) % PRIME
    assert explicit == h_coefficients[a_value]

    # Substitution sigma=2H turns each CCG3 equation into four times LCC6.
    for r_value in range(1, PRIME):
        t_branch = pow(r_value, 4, PRIME)
        chi = (r_value + inverse(r_value)) % PRIME
        h_terminal = half_root_coefficients(t_branch, a_value)[a_value]
        old_gates = (
            t_branch * (2 * h_terminal) ** 2 + 4 * (chi - 1) ** 2,
            t_branch * (chi - 2) ** 2 * (2 * h_terminal) ** 2 + 4 * (chi + 2) ** 2,
            t_branch * chi**2 * (2 * h_terminal) ** 2 + 4 * (chi - 4) ** 2,
        )
        new_gates = (
            t_branch * h_terminal**2 + (chi - 1) ** 2,
            t_branch * (chi - 2) ** 2 * h_terminal**2 + (chi + 2) ** 2,
            t_branch * chi**2 * h_terminal**2 + (chi - 4) ** 2,
        )
        assert all(old % PRIME == 4 * new % PRIME for old, new in zip(old_gates, new_gates))

        k_terminal = pow(4, a_value, PRIME) * h_terminal % PRIME
        denominator_scale = pow(4, 2 * a_value, PRIME)
        cleared_gates = (
            r_value**6 * k_terminal**2
            + denominator_scale * (r_value**2 - r_value + 1) ** 2,
            r_value**4 * (r_value - 1) ** 4 * k_terminal**2
            + denominator_scale * (r_value + 1) ** 4,
            r_value**4 * (r_value**2 + 1) ** 2 * k_terminal**2
            + denominator_scale * (r_value**2 - 4 * r_value + 1) ** 2,
        )
        assert all(
            cleared % PRIME == denominator_scale * r_value**2 * new % PRIME
            for cleared, new in zip(cleared_gates, new_gates)
        )


def wiring_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[GAP]["status"] == "PROVED"
    assert nodes[CONSTANT]["status"] == "PROVED"
    assert (GAP, NODE, "req") in edges
    assert (CONSTANT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "sigma=2H_a(t)",
        "H_n(t)=sum_(j=0)^n",
        "2(n+1)H_(n+1)",
        "H_n(r^4)=r^(2n)P_n",
        "t H^2+(chi-1)^2=0",
        "t(chi-2)^2H^2+(chi+2)^2=0",
        "t chi^2H^2+(chi-4)^2=0",
        "does not prove",
    ):
        assert marker in statement

    requests = (ROOT / "notes" / "PRIZE_COMPUTE_REQUESTS.md").read_text()
    for marker in (
        "B_0(r)=r^6K_n(r^4)^2",
        "B_1(r)=r^4(r-1)^4K_n(r^4)^2",
        "B_2(r)=r^4(r^2+1)^2K_n(r^4)^2",
        "root-by-characteristic",
    ):
        assert marker in requests


def main() -> None:
    algebra_check()
    wiring_check()
    print(
        "RATE_HALF_ANTIPODAL_DELETED_PAIR_LEGENDRE_COLLAPSE_PASS "
        "quotient_divisions=0 recurrence_width=2 branch_gates=3"
    )


if __name__ == "__main__":
    main()
