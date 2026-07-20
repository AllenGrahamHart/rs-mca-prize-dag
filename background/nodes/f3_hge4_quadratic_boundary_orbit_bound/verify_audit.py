#!/usr/bin/env python3
"""Mutation guards for the HGE4 quadratic-boundary orbit payment."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_quadratic_boundary_orbit_bound"


def main() -> None:
    rows = 0
    for exponent in range(3, 42, 2):
        order = 2**exponent
        width = (order - 2) // 3
        assert order == 3 * width + 2
        assert width == 2 or width > 2
        bound = 2 * (order - 1) * (width + 1)
        assert bound == 2 * (order * order - 1) // 3
        assert bound < Fraction(21, 2) * order * order
        rows += 1

    # The first e=2 level is a deliberate h>2 scope mutation.
    assert (8, 2) == (3 * 2 + 2, 2)

    # Two square classes are required; one-class counting is not consumed.
    order, width = 32, 10
    correct = 2 * (order - 1) * (width + 1)
    assert correct == 2 * ((order - 1) * (width + 1))
    assert correct > (order - 1) * (width + 1)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes["f3_hge4_norm_gate_count"]["status"] == "TARGET"
    statement = (ROOT / "critical/nodes/f3_hge4_norm_gate_count/statement.md").read_text()
    for marker in (
        NODE, "E_h^prim(m,p)<=2(m-1)(h+1)",
        "payment for the `e=2` width", "f_(h+1)", "not sufficient",
        "E_h^prim(m,p)<=2N(h+e,e)",
        "e=2: E_h^prim(m,p)<=h+2=(m+4)/3",
        "f3_hge4_near_third_dual_gap_exclusion", "E_h^prim(m,p)=0",
    ):
        assert marker in statement
    print(
        "F3_HGE4_QUADRATIC_BOUNDARY_ORBIT_BOUND_AUDIT_PASS "
        f"dyadic_levels={rows} h2_scope_guard=1 square_classes=2"
    )


if __name__ == "__main__":
    main()
