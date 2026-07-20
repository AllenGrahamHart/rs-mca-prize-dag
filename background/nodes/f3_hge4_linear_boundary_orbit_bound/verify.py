#!/usr/bin/env python3
"""Verify the HGE4 linear-boundary recurrence and orbit payment."""

from __future__ import annotations

import json
from fractions import Fraction
from math import factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_linear_boundary_orbit_bound"
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


def recurrence_check(width: int, x_value: Fraction) -> None:
    order = 3 * width + 1
    d_value = x_value - 1
    a_value = (1 + x_value) / (x_value * (x_value - 1) ** 2)
    reciprocal = [c_value(index) * a_value**index for index in range(width)]

    fourth = power(reciprocal, 4, width)
    left = [
        (width - index) * reciprocal[index] for index in range(width)
    ]
    right = [Fraction(0)] * width
    for index in range(width):
        right[index] += width * fourth[index]
        if index:
            right[index] -= order * a_value * fourth[index - 1]
    assert left == right

    inverse_cube = power(reciprocal, 3, width)
    target = [Fraction(1), -3 * a_value] + [Fraction(0)] * (width - 2)
    assert multiply(inverse_cube, target, width) == [Fraction(1)] + [
        Fraction(0)
    ] * (width - 1)

    endpoint = 1 + x_value - 2 * c_value(width) * a_value**width
    numerator_product = 1
    for step in range(width):
        numerator_product *= 3 * step + 1
    integer_screen = (
        factorial(width) * x_value**width * (x_value - 1) ** (2 * width)
        - 2 * numerator_product * (1 + x_value) ** (width - 1)
    )
    scale = (
        factorial(width)
        * x_value**width
        * (x_value - 1) ** (2 * width)
        / (1 + x_value)
    )
    assert integer_screen == endpoint * scale
    assert d_value != 0


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
        "U=(1-3ay)^(-1/3) mod y^h", "E_h^prim(m,p)<=m-2",
        "h! x^h(x-1)^(2h)", "mu_m\\{1,-1}", "not sufficient",
    ):
        assert marker in text


def main() -> None:
    recurrence_check(5, Fraction(2))
    recurrence_check(21, Fraction(3, 2))
    packet_check()
    print(
        "F3_HGE4_LINEAR_BOUNDARY_ORBIT_BOUND_PASS "
        "recurrence_widths=5,21 endpoint_screens=2"
    )


if __name__ == "__main__":
    main()
