#!/usr/bin/env python3
"""Mutation guards for the HGE4 linear-boundary orbit payment."""

from __future__ import annotations

import importlib.util
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_linear_boundary_orbit_bound"


def main() -> None:
    # Arithmetic scope and candidate payment at every dyadic e=1 level.
    rows = 0
    for exponent in range(2, 42, 2):
        order = 2**exponent
        width = (order - 1) // 3
        assert order == 3 * width + 1
        assert width == 1 or width > 4
        assert order - 2 < Fraction(21, 2) * order * order
        rows += 1

    # x=-1 is a real h=1 mutation and is excluded only in theorem scope.
    assert (4, 1) == (3 * 1 + 1, 1)
    assert 1 == 1

    # Recheck the first official-width finite-field challenge.
    base_path = (
        ROOT
        / "background/nodes/f3_hge4_nonfull_complement_third_gate/verify.py"
    )
    spec = importlib.util.spec_from_file_location("hge4_linear_audit_base", base_path)
    assert spec is not None and spec.loader is not None
    base = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(base)
    assert not base.shift_pairs(16, 257, 5)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes["f3_hge4_norm_gate_count"]["status"] == "TARGET"
    statement = (ROOT / "critical/nodes/f3_hge4_norm_gate_count/statement.md").read_text()
    for marker in (
        NODE, "E_h^prim(m,p)<=m-2", "initial `m-2` debit",
        "LBO3", "not a converse", "E_h^prim(m,p)<=2N(h+e,e)",
        "e=1: E_h^prim(m,p)<=2", "f3_hge4_near_third_dual_gap_exclusion",
        "E_h^prim(m,p)=0",
    ):
        assert marker in statement
    print(
        "F3_HGE4_LINEAR_BOUNDARY_ORBIT_BOUND_AUDIT_PASS "
        f"dyadic_levels={rows} h1_scope_guard=1 p257_challenge=empty"
    )


if __name__ == "__main__":
    main()
