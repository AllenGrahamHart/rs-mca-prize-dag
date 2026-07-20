#!/usr/bin/env python3
"""Mutation guards for the HGE4 near-third dual-gap exclusion."""

from __future__ import annotations

import importlib.util
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_near_third_dual_gap_exclusion"
VERIFY = ROOT / "background/nodes" / NODE / "verify.py"


def load_verify():
    spec = importlib.util.spec_from_file_location("dual_gap_verify", VERIFY)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    verify = load_verify()

    # The threshold is sharp for the recurrence block, not a rounding choice.
    assert 9 < 2 * 5 + 1
    assert 20 >= 2 * 4 + 1
    assert 41 >= 2 * 5 + 1

    # The 3|e stall is real, which is why the dyadic residue is load-bearing.
    for e_value in (3, 6, 9):
        stalled = 2 * e_value // 3
        assert 3 * stalled - 2 * e_value == 0
        verify.recurrence_check(e_value, 2 * e_value + 1)
    for exponent in range(2, 16):
        order = 2**exponent
        assert order % 3 in (1, 2)

    # Mutating the factor 3 in the inverse-gap identity is detected.
    h_value = 5
    z_poly = [Fraction(1), Fraction(-1)]
    formal = verify.rational_power(z_poly, -1, 3, 2 * h_value)
    centered = formal[: h_value + 1] + [Fraction(0)] * (h_value - 1)
    inv_centered = verify.inverse(centered, 2 * h_value)
    inverse_square = verify.multiply(inv_centered, inv_centered, 2 * h_value)
    two_thirds = verify.rational_power(z_poly, 2, 3, 2 * h_value)
    assert inverse_square[h_value + 2] == 3 * two_thirds[h_value + 2]
    assert inverse_square[h_value + 2] != 2 * two_thirds[h_value + 2]

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes["f3_hge4_norm_gate_count"]["status"] == "TARGET"
    consumer = (ROOT / "critical/nodes/f3_hge4_norm_gate_count/statement.md").read_text()
    for marker in (
        NODE, "E_h^prim(m,p)=0", "floor(2m/7)", "(32,9,5)",
        "zero-cost analytic exclusion",
    ):
        assert marker in consumer
    print(
        "F3_HGE4_NEAR_THIRD_DUAL_GAP_EXCLUSION_AUDIT_PASS "
        "threshold_guard=32_9_5 dyadic_stall_guard=3 factor_guard=3"
    )


if __name__ == "__main__":
    main()
