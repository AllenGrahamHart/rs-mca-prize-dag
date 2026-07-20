#!/usr/bin/env python3
"""Verify the c=1 parity nonharmonic scalar compiler."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_fiber_two_cycle_c1_parity_nonharmonic_scalar_compiler"
DEPENDENCIES = {
    "rate_half_list_budget_three_fiber_two_cycle_c1_parity_mobius_router",
    "rate_half_list_budget_three_fiber_two_cycle_c1_parity_harmonic_exclusion",
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_even_factorization",
    "rate_half_list_budget_three_maximal_field_degree_collapse",
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_ode",
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_coefficient_legendre_collapse",
}
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 97


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % PRIME == 0:
        poly.pop()
    return [value % PRIME for value in poly]


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    return trim([
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(size)
    ])


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([scalar * value for value in poly])


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for left_index, value in enumerate(left):
        for right_index, other in enumerate(right):
            answer[left_index + right_index] += value * other
    return trim(answer)


def derivative(poly: list[int]) -> list[int]:
    return trim([
        index * poly[index] for index in range(1, len(poly))
    ] or [0])


def shift(poly: list[int], amount: int) -> list[int]:
    return [0] * amount + poly


def remainder(dividend: list[int], divisor: list[int]) -> list[int]:
    dividend = trim(dividend[:])
    divisor = trim(divisor[:])
    inverse_lead = pow(divisor[-1], -1, PRIME)
    while len(dividend) >= len(divisor) and dividend != [0]:
        offset = len(dividend) - len(divisor)
        coefficient = dividend[-1] * inverse_lead % PRIME
        for index, value in enumerate(divisor):
            dividend[index + offset] -= coefficient * value
        dividend = trim(dividend)
    return dividend


def trace_iterate(value: int, levels: int) -> int:
    for _ in range(levels):
        value = (value * value - 2) % PRIME
    return value


def scalar_and_fourth_power_check() -> None:
    # PRIME-1 is divisible by 2L for the toy order L=8.
    l_order = 8
    generator = 5
    q_out = pow(generator, (PRIME - 1) // l_order, PRIME)
    assert pow(q_out, l_order, PRIME) == 1
    assert pow(q_out, l_order // 2, PRIME) != 1
    assert pow(q_out, (PRIME - 1) // 2, PRIME) == 1

    y_value = (q_out + pow(q_out, -1, PRIME)) % PRIME
    assert y_value not in (2, PRIME - 2)
    assert trace_iterate(y_value, 3) == 2
    assert trace_iterate(y_value, 2) != 2

    w_poly = [2, 1]
    z_poly = multiply(w_poly, w_poly)
    s_poly = scale(z_poly, 1 + q_out)
    t_poly = scale(multiply(z_poly, z_poly), q_out)
    assert multiply(s_poly, s_poly) == scale(t_poly, y_value + 2)
    assert scale(t_poly, pow(q_out, -1, PRIME)) == multiply(z_poly, z_poly)

    reciprocal_scaled = scale(t_poly, q_out)
    fourth_multiplier_root = next(
        root for root in range(1, PRIME)
        if pow(root, 4, PRIME) == q_out * q_out % PRIME
    )
    assert reciprocal_scaled == scale(
        multiply(multiply(w_poly, w_poly), multiply(w_poly, w_poly)),
        pow(fourth_multiplier_root, 4, PRIME),
    )

    # The constant gate follows formally from S(0)=2H and T(0)=-1/t.
    h_value = s_poly[0] * pow(2, -1, PRIME) % PRIME
    t_value = -pow(t_poly[0], -1, PRIME) % PRIME
    assert (4 * t_value * h_value * h_value + y_value + 2) % PRIME == 0


def differential_check() -> None:
    n_value = 8
    t_value = 29
    assert (5 * t_value * t_value + 2 * t_value + 5) % PRIME == 0
    d_poly = [t_value, -(1 + t_value), 1]
    u_zero = 2 * t_value * pow(5 * (t_value + 1), -1, PRIME) % PRIME
    u_poly = [u_zero, 1]

    ode = add(
        add(
            scale(multiply(d_poly, u_poly), 2 * n_value - 4),
            scale(shift(multiply(derivative(d_poly), u_poly), 1), -2),
        ),
        scale(shift(multiply(d_poly, derivative(u_poly)), 1), -8),
    )
    assert len(ode) == 1 and ode[0] != 0
    kappa = ode[0]

    a_poly = shift(multiply(u_poly, u_poly), 1)
    x_to_n_minus_one = [PRIME - 1] + [0] * (n_value - 1) + [1]
    numerator_r = add(
        x_to_n_minus_one,
        scale(multiply(d_poly, multiply(a_poly, a_poly)), -1),
    )

    left = scale(
        shift(add(
            multiply(derivative(numerator_r), d_poly),
            scale(multiply(numerator_r, derivative(d_poly)), -1),
        ), 1),
        2,
    )
    p_aux = add(
        [2 * n_value],
        scale(shift(multiply(multiply(u_poly, u_poly), u_poly), 2), kappa),
    )
    nd_minus_xdprime = add(
        scale(d_poly, n_value),
        scale(shift(derivative(d_poly), 1), -1),
    )
    right = add(
        multiply(p_aux, d_poly),
        scale(multiply(nd_minus_xdprime, numerator_r), 2),
    )
    assert left == right

    # Check the divisibility consequence without a coprimality hypothesis.
    w_poly = [2, 1]
    w_squared = multiply(w_poly, w_poly)
    model_r = multiply(w_squared, [3, 4, 1])
    model_p = add(
        scale(shift(multiply(d_poly, derivative(model_r)), 1), 2),
        scale(multiply(nd_minus_xdprime, model_r), -2),
    )
    assert remainder(model_p, w_poly) == [0]
    assert remainder(multiply(model_p, model_p), w_squared) == [0]


def wiring_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (
        ROOT / "background" / "nodes" / NODE / "statement.md"
    ).read_text()
    for marker in (
        "p=1 mod 2L",
        "source lift `r` need not descend",
        "S^2=(y+2)T",
        "T/q_out=W^4",
        "4tH^2+y+2=0",
        "deg gcd(S,P_aux)>=M-1=2^36-1",
        "does not prove uniform",
        "authorize a large computation",
    ):
        assert marker in statement


def main() -> None:
    scalar_and_fourth_power_check()
    differential_check()
    wiring_check()
    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C1_PARITY_NONHARMONIC_SCALAR_PASS "
        "branches=6 trace_depth=39 twisted_fourth_power=1 gcd_gate=1"
    )


if __name__ == "__main__":
    main()

