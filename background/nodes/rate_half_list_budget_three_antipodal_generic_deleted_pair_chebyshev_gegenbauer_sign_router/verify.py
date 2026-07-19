#!/usr/bin/env python3
"""Verify the deleted-pair Chebyshev/Gegenbauer sign router."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_generic_deleted_pair_chebyshev_gegenbauer_sign_router"
PARITY = "rate_half_list_budget_three_antipodal_generic_deleted_pair_parity_reduction"
LEGENDRE = "rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_coefficient_legendre_collapse"
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 257


def inverse(value: int) -> int:
    return pow(value % PRIME, -1, PRIME)


def gegenbauer(degree: int, parameter_numerator: int, parameter_denominator: int, x_value: int) -> int:
    parameter = parameter_numerator * inverse(parameter_denominator) % PRIME
    values = [1]
    if degree == 0:
        return 1
    values.append(2 * parameter * x_value % PRIME)
    for n in range(1, degree):
        values.append(
            (
                2 * (n + parameter) * x_value * values[n]
                - (n + 2 * parameter - 1) * values[n - 1]
            )
            * inverse(n + 1)
            % PRIME
        )
    return values[degree]


def legendre(degree: int, x_value: int) -> int:
    return gegenbauer(degree, 1, 2, x_value)


def chebyshev(degree: int, y_value: int) -> int:
    values = [1, y_value]
    for _ in range(1, degree):
        values.append((2 * y_value * values[-1] - values[-2]) % PRIME)
    return values[degree]


def coefficient_values(t_value: int, limit: int, exponent_denominator: int) -> list[int]:
    # Coefficients of ((1-z)(1-tz))^(-1/exponent_denominator).
    if exponent_denominator == 4:
        answer = [1]
        for n in range(1, limit + 1):
            previous_two = answer[n - 2] if n >= 2 else 0
            answer.append(
                (
                    (4 * n - 3) * (1 + t_value) * answer[n - 1]
                    - (4 * n - 6) * t_value * previous_two
                )
                * inverse(4 * n)
                % PRIME
            )
        return answer
    answer = [1, (1 + t_value) * inverse(2) % PRIME]
    for n in range(1, limit):
        answer.append(
            (
                (2 * n + 1) * (1 + t_value) * answer[n]
                - 2 * n * t_value * answer[n - 1]
            )
            * inverse(2 * (n + 1))
            % PRIME
        )
    return answer[: limit + 1]


def algebra_check() -> None:
    m_value = 1
    l_value = 2 * m_value
    n_value = 2 * l_value - 1
    torsion_roots = [value for value in range(1, PRIME) if pow(value, 16 * l_value, PRIME) == 1]
    assert len(torsion_roots) == 16 * l_value

    for r_value in torsion_roots:
        u_value = r_value * r_value % PRIME
        t_value = u_value * u_value % PRIME
        y_value = (r_value + inverse(r_value)) * inverse(2) % PRIME
        x_value = (2 * y_value * y_value - 1) % PRIME
        epsilon = pow(r_value, 8 * l_value, PRIME)
        assert epsilon in (1, PRIME - 1)
        assert chebyshev(8 * l_value, y_value) == epsilon

        fourth = coefficient_values(t_value, l_value, 4)
        half = coefficient_values(t_value, n_value, 2)
        c_primary = gegenbauer(l_value, 1, 4, x_value)
        p_value = legendre(n_value, x_value)
        assert fourth[l_value] == pow(u_value, l_value, PRIME) * c_primary % PRIME
        assert half[n_value] == pow(u_value, n_value, PRIME) * p_value % PRIME
        assert t_value * half[n_value] ** 2 % PRIME == epsilon * p_value**2 % PRIME

        chi = 2 * y_value % PRIME
        old_gates = (
            t_value * half[n_value] ** 2 + (chi - 1) ** 2,
            t_value * (chi - 2) ** 2 * half[n_value] ** 2 + (chi + 2) ** 2,
            t_value * chi**2 * half[n_value] ** 2 + (chi - 4) ** 2,
        )
        trace_gates = (
            epsilon * p_value**2 + (2 * y_value - 1) ** 2,
            epsilon * p_value**2 * (y_value - 1) ** 2 + (y_value + 1) ** 2,
            epsilon * p_value**2 * y_value**2 + (y_value - 2) ** 2,
        )
        assert old_gates[0] % PRIME == trace_gates[0] % PRIME
        assert old_gates[1] % PRIME == 4 * trace_gates[1] % PRIME
        assert old_gates[2] % PRIME == 4 * trace_gates[2] % PRIME

        sign_roots = [value for value in range(PRIME) if value * value % PRIME == -epsilon % PRIME]
        assert len(sign_roots) == 2
        linear = (
            [p_value - sign * (2 * y_value - 1) for sign in sign_roots],
            [p_value * (y_value - 1) - sign * (y_value + 1) for sign in sign_roots],
            [p_value * y_value - sign * (y_value - 2) for sign in sign_roots],
        )
        for gate, factors in zip(trace_gates, linear):
            assert (gate % PRIME == 0) == any(factor % PRIME == 0 for factor in factors)


def wiring_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[PARITY]["status"] == "PROVED"
    assert nodes[LEGENDRE]["status"] == "PROVED"
    assert (PARITY, NODE, "req") in edges
    assert (LEGENDRE, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "T_(8L)(y)=epsilon",
        "C_L^(1/4)(x)=0",
        "t H_(2L-1)(t)^2=epsilon P^2",
        "epsilon P^2+(2y-1)^2=0",
        "P=s(2y-1)",
        "P(y-1)=s(y+1)",
        "Py=s(y-2)",
        "six linear-sign branches",
        "does not prove",
    ):
        assert marker in statement


def main() -> None:
    algebra_check()
    wiring_check()
    print(
        "RATE_HALF_DELETED_PAIR_CHEBYSHEV_GEGENBAUER_SIGN_PASS "
        "trace_variables=1 torsion_signs=2 linear_branches=6"
    )


if __name__ == "__main__":
    main()
