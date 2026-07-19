#!/usr/bin/env python3
"""Verify the deleted-pair trace gcd router."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_generic_deleted_pair_trace_gcd_router"
SIGN = "rate_half_list_budget_three_antipodal_generic_deleted_pair_chebyshev_gegenbauer_sign_router"
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 257


def inv(value: int) -> int:
    return pow(value % PRIME, -1, PRIME)


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % PRIME == 0:
        poly.pop()
    return [value % PRIME for value in poly]


def add(left: list[int], right: list[int]) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
    return trim(out)


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([scalar * value % PRIME for value in poly])


def shift(poly: list[int]) -> list[int]:
    return [0] + poly


def multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            out[i + j] += left_value * right_value
    return trim(out)


def divide(dividend: list[int], divisor: list[int]) -> tuple[list[int], list[int]]:
    remainder = trim(dividend[:])
    divisor = trim(divisor[:])
    quotient = [0] * max(1, len(remainder) - len(divisor) + 1)
    lead_inverse = inv(divisor[-1])
    while len(remainder) >= len(divisor) and remainder != [0]:
        degree = len(remainder) - len(divisor)
        coefficient = remainder[-1] * lead_inverse % PRIME
        quotient[degree] = coefficient
        for index, value in enumerate(divisor):
            remainder[index + degree] -= coefficient * value
        remainder = trim(remainder)
    return trim(quotient), remainder


def gcd(*polys: list[int]) -> list[int]:
    answer = trim(polys[0][:])
    for poly in polys[1:]:
        other = trim(poly[:])
        while other != [0]:
            _, remainder = divide(answer, other)
            answer, other = other, remainder
    return scale(answer, inv(answer[-1]))


def evaluate(poly: list[int], value: int) -> int:
    answer = 0
    for coefficient in reversed(poly):
        answer = (answer * value + coefficient) % PRIME
    return answer


def gegenbauer(degree: int, numerator: int, denominator: int) -> list[int]:
    parameter = numerator * inv(denominator) % PRIME
    values = [[1]]
    if degree == 0:
        return values[0]
    values.append([0, 2 * parameter % PRIME])
    for n in range(1, degree):
        top = add(
            scale(shift(values[n]), 2 * (n + parameter)),
            scale(values[n - 1], -(n + 2 * parameter - 1)),
        )
        values.append(scale(top, inv(n + 1)))
    return values[degree]


def chebyshev_t(degree: int) -> list[int]:
    values = [[1], [0, 1]]
    for _ in range(1, degree):
        values.append(add(scale(shift(values[-1]), 2), scale(values[-2], -1)))
    return values[degree]


def chebyshev_u(degree: int) -> list[int]:
    values = [[1], [0, 2]]
    for _ in range(1, degree):
        values.append(add(scale(shift(values[-1]), 2), scale(values[-2], -1)))
    return values[degree]


def branch_polynomials(remainder: list[int], x_value: int, scalar: int) -> tuple[int, int, int]:
    p_value = evaluate(remainder, x_value)
    return (
        (p_value + scalar) ** 2 - 2 * scalar**2 * (x_value + 1),
        2 * (p_value + scalar) ** 2 - (x_value + 1) * (p_value - scalar) ** 2,
        (x_value + 1) * (p_value - scalar) ** 2 - 8 * scalar**2,
    )


def algebra_check() -> None:
    inverse_two = inv(2)
    for l_value in (2, 4, 8):
        primary = gegenbauer(l_value, 1, 4)
        legendre = gegenbauer(2 * l_value - 1, 1, 2)
        quotient, remainder = divide(legendre, primary)
        assert add(multiply(quotient, primary), remainder) == legendre
        assert len(remainder) - 1 < l_value

        torsion = {
            PRIME - 1: chebyshev_t(2 * l_value),
            1: chebyshev_u(2 * l_value - 1),
        }
        t_four_l = chebyshev_t(4 * l_value)

        for x_value in range(PRIME):
            if x_value not in (1, PRIME - 1):
                for epsilon, gate in torsion.items():
                    assert (
                        (evaluate(t_four_l, x_value) - epsilon) % PRIME == 0
                    ) == (evaluate(gate, x_value) == 0)

            p_value = evaluate(legendre, x_value)
            r_value = evaluate(remainder, x_value)
            if evaluate(primary, x_value) == 0:
                assert p_value == r_value

            for epsilon in (1, PRIME - 1):
                signs = [value for value in range(PRIME) if value * value % PRIME == -epsilon % PRIME]
                assert len(signs) == 2
                for scalar in signs:
                    equations = branch_polynomials(remainder, x_value, scalar)
                    for branch, equation in enumerate(equations):
                        if equation % PRIME != 0:
                            continue
                        if branch == 0:
                            y_value = (r_value + scalar) * inv(2 * scalar) % PRIME
                            signed = r_value - scalar * (2 * y_value - 1)
                        elif branch == 1:
                            assert r_value != scalar
                            y_value = (r_value + scalar) * inv(r_value - scalar) % PRIME
                            signed = r_value * (y_value - 1) - scalar * (y_value + 1)
                        else:
                            assert r_value != scalar
                            y_value = -2 * scalar * inv(r_value - scalar) % PRIME
                            signed = r_value * y_value - scalar * (y_value - 2)
                        assert (2 * y_value * y_value - 1) % PRIME == x_value
                        assert signed % PRIME == 0

        # The gcd interface and direct common-root census agree.
        for epsilon, gate in torsion.items():
            gate_remainder = divide(gate, primary)[1]
            for scalar in [value for value in range(PRIME) if value * value % PRIME == -epsilon % PRIME]:
                r_plus = add(remainder, [scalar])
                r_minus = add(remainder, [-scalar])
                x_plus_one = [1, 1]
                equations = (
                    add(multiply(r_plus, r_plus), scale(x_plus_one, -2 * scalar * scalar)),
                    add(scale(multiply(r_plus, r_plus), 2), scale(multiply(x_plus_one, multiply(r_minus, r_minus)), -1)),
                    add(multiply(x_plus_one, multiply(r_minus, r_minus)), [-8 * scalar * scalar]),
                )
                for equation in equations:
                    equation_remainder = divide(equation, primary)[1]
                    common = gcd(primary, gate_remainder, equation_remainder)
                    roots = [
                        value
                        for value in range(PRIME)
                        if evaluate(primary, value) == 0
                        and evaluate(gate, value) == 0
                        and evaluate(equation, value) == 0
                    ]
                    assert roots == [value for value in range(PRIME) if evaluate(common, value) == 0]


def wiring_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[SIGN]["status"] == "PROVED"
    assert (SIGN, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "T_(2L)(x)",
        "U_(2L-1)(x)",
        "E_(0,s)",
        "E_(1,s)",
        "E_(2,s)",
        "gcd(C, G_epsilon mod C, E_(j,s) mod C)=1",
        "does not prove",
    ):
        assert marker in statement


def main() -> None:
    algebra_check()
    wiring_check()
    print(
        "RATE_HALF_DELETED_PAIR_TRACE_GCD_ROUTER_PASS "
        "torsion_degrees=2L signed_branches=6 quotient_polynomials=3"
    )


if __name__ == "__main__":
    main()
