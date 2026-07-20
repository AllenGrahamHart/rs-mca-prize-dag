#!/usr/bin/env python3
"""Mutation guards for the HGE4 boundary-defect trace pin."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_boundary_defect_trace_pin"


def main() -> None:
    # Scaling covariance in the e=1 identity uses m=3h+1 exactly.
    for width in (5, 21, 85, 341):
        order = 3 * width + 1
        assert 4 * width + 1 - width == order

    # The normalized one-ratio gate is an exact rearrangement.
    for x_value in (Fraction(2), Fraction(3, 2), Fraction(-2)):
        a_value = (1 + x_value) / (x_value * (x_value - 1) ** 2)
        assert 1 + x_value == (x_value - 1) ** 2 * a_value * x_value

    # Omitting d^2 or replacing m-1 by m breaks generic fixtures.
    d_value, a_value = Fraction(3, 2), Fraction(5, 7)
    order, width = 32, 10
    correct = d_value * d_value * Fraction(order - 1, order) * a_value
    assert correct != d_value * Fraction(order - 1, order) * a_value
    assert correct != d_value * d_value * a_value
    assert width > 2

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes["f3_hge4_norm_gate_count"]["status"] == "TARGET"
    statement = (ROOT / "critical/nodes/f3_hge4_norm_gate_count/statement.md").read_text()
    for marker in (
        NODE, "G=d^2(a-(h/m)X)", "b-2a^2",
        "a=(1+x)/(x(x-1)^2)", "does not exclude",
    ):
        assert marker in statement
    print(
        "F3_HGE4_BOUNDARY_DEFECT_TRACE_PIN_AUDIT_PASS "
        "scaling_rows=4 ratio_guards=3 coefficient_mutations=2"
    )


if __name__ == "__main__":
    main()
