#!/usr/bin/env python3
"""Verify the HGE4 quadratic-boundary recurrence and orbit payment."""

from __future__ import annotations

import json
from fractions import Fraction
from math import factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_quadratic_boundary_orbit_bound"
DEPENDENCY = "f3_hge4_boundary_defect_trace_pin"
CONSUMER = "f3_hge4_norm_gate_count"


def multiply(left: list[Fraction], right: list[Fraction], cutoff: int) -> list[Fraction]:
    output = [Fraction(0)] * cutoff
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            if i + j < cutoff:
                output[i + j] += first * second
    return output


def power(poly: list[Fraction], exponent: int, cutoff: int) -> list[Fraction]:
    output = [Fraction(1)] + [Fraction(0)] * (cutoff - 1)
    for _ in range(exponent):
        output = multiply(output, poly, cutoff)
    return output


def c_value(index: int) -> Fraction:
    numerator = 1
    for step in range(index):
        numerator *= 3 * step + 1
    return Fraction(numerator, factorial(index))


def series_f(a_value: Fraction, c_two: Fraction, cutoff: int) -> list[Fraction]:
    atom = [Fraction(0), a_value, c_two] + [Fraction(0)] * max(0, cutoff - 3)
    output = [Fraction(1)] + [Fraction(0)] * (cutoff - 1)
    atom_power = [Fraction(1)] + [Fraction(0)] * (cutoff - 1)
    for exponent in range(1, cutoff):
        atom_power = multiply(atom_power, atom, cutoff)
        coefficient = c_value(exponent)
        for index in range(cutoff):
            output[index] += coefficient * atom_power[index]
    return output


def recurrence_and_endpoint_check(width: int) -> None:
    order = 3 * width + 2
    epsilon = Fraction(1)
    x_value = Fraction(2)
    d_value = epsilon * (x_value - 1)
    c_two = (1 + x_value) / (
        epsilon**3 * x_value * (x_value - 1) ** 2
    )
    a_value = Fraction(5, 7)
    cutoff = width + 2
    formal = series_f(a_value, c_two, cutoff)

    # Verify the reciprocal ODE below the endpoint.
    fourth = power(formal, 4, width)
    left = [(width - index) * formal[index] for index in range(width)]
    right = [Fraction(0)] * width
    for index in range(width):
        right[index] += width * fourth[index]
        if index >= 1:
            right[index] -= (order - 1) * a_value * fourth[index - 1]
        if index >= 2:
            right[index] -= order * c_two * fourth[index - 2]
    assert left == right

    # Recompute the exact equation through degree h+1.  The y^m factor and
    # the second summand of (1), which starts at y^(h+2), do not enter yet.
    actual_u = formal.copy()
    actual_u[width] = epsilon
    actual_u[width + 1] = Fraction(0)
    actual_v = actual_u.copy()
    actual_v[width] += d_value
    coefficient = [Fraction(width), -(order - 1) * a_value, -order * c_two]
    lhs = [
        (width - index) * actual_u[index] for index in range(cutoff)
    ]
    rhs = multiply(
        coefficient,
        multiply(power(actual_u, 2, cutoff), power(actual_v, 2, cutoff), cutoff),
        cutoff,
    )
    residual = [lhs[index] - rhs[index] for index in range(cutoff)]

    # Directly replay both endpoint residual formulas.
    delta = epsilon - formal[width]
    first_residual = -2 * width * (
        2 * delta + d_value
    )
    assert residual[width] == first_residual
    assert first_residual == -2 * width * (
        epsilon + epsilon * x_value - 2 * formal[width]
    )
    second_residual = (
        (4 * width + 1) * formal[width + 1]
        + 4 * a_value * delta
        + 2 * d_value * a_value
    )
    assert residual[width + 1] == second_residual
    assert 4 * a_value * (-d_value / 2) + 2 * d_value * a_value == 0

    leading = c_value(width + 1)
    assert leading != 0
    assert 2 * (order - 1) * (width + 1) == 2 * (order * order - 1) // 3
    assert 2 * (order * order - 1) // 3 < Fraction(2, 3) * order * order


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    base = ROOT / "background/nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md", "dependency_subdag.md",
        "audit.md", "result.md", "verify.py", "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join((base / name).read_text() for name in required if name.endswith(".md"))
    for marker in (
        "F_(a,c_2)(y)=(1-3ay-3c_2y^2)^(-1/3)",
        "f_(h+1)(a,c_2)=0", "E_h^prim(m,p)<=2(m-1)(h+1)",
        "2(m^2-1)/3", "necessary, not sufficient",
    ):
        assert marker in text


def main() -> None:
    recurrence_and_endpoint_check(10)
    recurrence_and_endpoint_check(42)
    packet_check()
    print(
        "F3_HGE4_QUADRATIC_BOUNDARY_ORBIT_BOUND_PASS "
        "recurrence_widths=10,42 endpoint_ledgers=2"
    )


if __name__ == "__main__":
    main()
