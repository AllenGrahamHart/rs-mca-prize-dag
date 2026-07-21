#!/usr/bin/env python3
"""Checks for the c2 minimum-support infinity-cell torsion gate."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NODE_ID = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_minimum_support_infinity_cell_torsion_gate"
CELL_DEP = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_canonical_cell_fourier_ladder"
BRANCH_DEP = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_minimum_support_barycentric_collision_branch_compiler"
EULER_DEP = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_minimum_support_euler_divisor_gate"
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 97


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % PRIME == 0:
        poly.pop()
    return [value % PRIME for value in poly]


def add(left: list[int], right: list[int]) -> list[int]:
    out = [0] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    return trim(out)


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([scalar * value for value in poly])


def mul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def divmod_poly(dividend: list[int], divisor: list[int]) -> tuple[list[int], list[int]]:
    work = trim(dividend[:])
    quotient = [0] * max(1, len(work) - len(divisor) + 1)
    inverse = pow(divisor[-1], -1, PRIME)
    while len(work) >= len(divisor) and work != [0]:
        shift = len(work) - len(divisor)
        coefficient = work[-1] * inverse % PRIME
        quotient[shift] = coefficient
        for i, value in enumerate(divisor):
            work[i + shift] -= coefficient * value
        work = trim(work)
    return trim(quotient), trim(work)


def polynomial_from_roots(roots: list[int]) -> list[int]:
    out = [1]
    for root in roots:
        out = mul(out, [-root % PRIME, 1])
    return out


def derivative_values(roots: list[int]) -> list[int]:
    out = []
    for i, root in enumerate(roots):
        value = 1
        for j, other in enumerate(roots):
            if i != j:
                value = value * (root - other) % PRIME
        out.append(value)
    return out


def centered_coefficients(roots: list[int]) -> tuple[int, int, int, int]:
    inverse_four = pow(4, -1, PRIME)
    center = sum(roots) * inverse_four % PRIME
    shifted = [(root - center) % PRIME for root in roots]
    phi = polynomial_from_roots(shifted)
    assert phi[3] == 0 and phi[4] == 1
    return center, phi[2], phi[1], phi[0]


def square_remainder(value: list[int], modulus: list[int]) -> list[int]:
    return divmod_poly(mul(value, value), modulus)[1]


def main() -> None:
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
    assert incoming == {CELL_DEP, BRANCH_DEP, EULER_DEP}
    assert CONSUMER in outgoing

    # This order-32 quartet has exactly one derivative collision and J=0.
    ell = [1, 28, 27, 33]
    assert all(pow(value, 32, PRIME) == 1 for value in ell)
    assert all(-value % PRIME not in ell for value in ell)
    b, alpha_inf, beta_inf, gamma_inf = centered_coefficients(ell)
    c = 7
    alpha = alpha_inf * pow(c, -2, PRIME) % PRIME
    beta = beta_inf * pow(c, -3, PRIME) % PRIME
    gamma = gamma_inf * pow(c, -4, PRIME) % PRIME

    x_minus_b = [-b % PRIME, 1]
    compiled = add(
        add(mul(mul(x_minus_b, x_minus_b), mul(x_minus_b, x_minus_b)),
            scale(mul(x_minus_b, x_minus_b), alpha * c * c)),
        add(scale(x_minus_b, beta * pow(c, 3, PRIME)), [gamma * pow(c, 4, PRIME)]),
    )
    direct = polynomial_from_roots(ell)
    assert compiled == direct

    p_src = pow(direct[0], -1, PRIME)
    assert direct[0] == pow(p_src, -1, PRIME)
    remainder = [0, 1]
    for _ in range(5):
        remainder = square_remainder(remainder, direct)
    assert remainder == [1]

    w = [(value - b) * pow(c, -1, PRIME) % PRIME for value in ell]
    outer_derivatives = derivative_values(w)
    infinity_derivatives = derivative_values(ell)
    assert infinity_derivatives == [pow(c, 3, PRIME) * value % PRIME for value in outer_derivatives]
    classes = sorted(sorted(i for i, value in enumerate(infinity_derivatives) if value == target)
                     for target in set(infinity_derivatives))
    assert sorted(map(len, classes), reverse=True) == [2, 1, 1]
    j_inf = (72 * alpha_inf * gamma_inf - 27 * beta_inf * beta_inf - 2 * alpha_inf**3) % PRIME
    assert j_inf == 0

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_MIN_SUPPORT_INFINITY_TORSION_PASS "
        "quartic=1 torsion_squarings=5 product=1 collision=1 "
        "nonantipodal_J_zero=1 wiring=4"
    )


if __name__ == "__main__":
    main()
