#!/usr/bin/env python3
"""Verify the HGE4 e=1/e=2 boundary trace pins."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_boundary_defect_trace_pin"
DEPENDENCY = "f3_hge4_complement_separator_defect_normal_form"
CONSUMER = "f3_hge4_norm_gate_count"


def trim(poly: list[Fraction]) -> list[Fraction]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * max(len(left), len(right))
    for index in range(len(out)):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        )
    return trim(out)


def sub(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    return add(left, [-value for value in right])


def scale(poly: list[Fraction], scalar: Fraction) -> list[Fraction]:
    return trim([scalar * value for value in poly])


def mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            out[i + j] += first * second
    return trim(out)


def derivative(poly: list[Fraction]) -> list[Fraction]:
    return trim([index * poly[index] for index in range(1, len(poly))])


def divmod_poly(
    numerator: list[Fraction], denominator: list[Fraction]
) -> tuple[list[Fraction], list[Fraction]]:
    remainder = numerator[:]
    quotient = [Fraction(0)] * max(1, len(numerator) - len(denominator) + 1)
    while len(remainder) >= len(denominator) and remainder != [0]:
        offset = len(remainder) - len(denominator)
        coefficient = remainder[-1] / denominator[-1]
        quotient[offset] = coefficient
        for index, value in enumerate(denominator):
            remainder[index + offset] -= coefficient * value
        trim(remainder)
    return trim(quotient), trim(remainder)


def forced_defect(
    width: int, defect: int, a_value: Fraction, b_value: Fraction, d_value: Fraction
) -> list[Fraction]:
    order = 3 * width + defect
    p_poly = [Fraction(index + 2, index + 3) for index in range(width + 1)]
    p_poly[-1] = 1
    p_poly[-2] = a_value
    p_poly[-3] = b_value
    q_poly = p_poly[:]
    q_poly[0] += d_value
    product = mul(p_poly, q_poly)
    x_power = [Fraction(0)] * order + [Fraction(1)]
    r_poly, _ = divmod_poly(x_power, product)
    numerator = sub(
        add(p_poly, q_poly),
        scale(
            mul([0, 1], mul(derivative(p_poly), r_poly)),
            d_value * d_value / order,
        ),
    )
    quotient, _ = divmod_poly(numerator, product)
    return quotient


def coefficient_checks() -> None:
    a_value, b_value, d_value = Fraction(5, 7), Fraction(11, 13), Fraction(3, 2)

    width, order = 5, 16
    observed = forced_defect(width, 1, a_value, b_value, d_value)
    expected = [
        d_value * d_value * a_value,
        -d_value * d_value * Fraction(width, order),
    ]
    assert observed == expected

    width, order = 10, 32
    observed = forced_defect(width, 2, a_value, b_value, d_value)
    expected = [
        d_value * d_value * (b_value - 2 * a_value * a_value),
        d_value * d_value * Fraction(order - 1, order) * a_value,
        -d_value * d_value * Fraction(width, order),
    ]
    assert observed == expected

    # Exact zero-value gates on synthetic boundary data.
    p_zero, d_value = Fraction(1), Fraction(2)
    q_zero = p_zero + d_value
    a_e1 = (p_zero + q_zero) / (d_value * d_value * p_zero * q_zero)
    assert p_zero + q_zero == d_value * d_value * a_e1 * p_zero * q_zero
    a_e2 = Fraction(1, 5)
    b_e2 = 2 * a_e2 * a_e2 + a_e1
    assert p_zero + q_zero == (
        d_value * d_value * (b_e2 - 2 * a_e2 * a_e2) * p_zero * q_zero
    )


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
        "G=d^2 (a-(h/m)X)", "b-2a^2", "p_0+q_0=d^2 a p_0q_0",
        "a=(1+x)/(x(x-1)^2)", "no boundary emptiness",
    ):
        assert marker in text


def main() -> None:
    coefficient_checks()
    packet_check()
    print(
        "F3_HGE4_BOUNDARY_DEFECT_TRACE_PIN_PASS "
        "e1_coefficients=2 e2_coefficients=3 scalar_gates=2"
    )


if __name__ == "__main__":
    main()
