#!/usr/bin/env python3
"""Verify the nu=0, b=0 value-coset table and DAG wiring."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_m4_h3_nu0_zero_b_value_coset_certificate"
SUPPLIER = "l1_m4_h3_mason_defect_budget"
CONSUMER = "l1_mixed_petal_amplification"
SCRIPT = ROOT / "experiments" / "prize_resolution" / \
    "l1_m4_h3_nu0_zero_b_value_coset_check.py"


def load_script():
    spec = importlib.util.spec_from_file_location("zero_b_value_coset", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def signed(value: tuple[int, int], p: int) -> int | str:
    if value == (1, 0):
        return 1
    if value == (-1 % p, 0):
        return -1
    return "imaginary"


def main() -> None:
    module = load_script()
    expected = {
        8191: set(),
        131071: set(),
        524287: {(1, -1), (-1, 1)},
        2147483647: {(1, -1), (-1, 1)},
    }
    checks = 0
    for p, expected_valid in expected.items():
        rows = module.table(p)
        degenerate = [row for row in rows if row[2].startswith("DEGENERATE")]
        assert len(degenerate) == 1
        assert signed(degenerate[0][0], p) == signed(degenerate[0][1], p) == 1
        valid = {
            (signed(epsilon, p), signed(eta, p))
            for epsilon, eta, outcome in rows
            if outcome == "ALL_QUADRATIC_ROOTS"
        }
        assert valid == expected_valid
        checks += 4

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[SUPPLIER]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (SUPPLIER, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    checks += 5

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in ("(ZVC2)", "(ZVC3)", "(ZVC4)", "(ZVC5)",
                   "a^2+3aR(0)^2+R(0)^4", "does not"):
        assert anchor in statement
        checks += 1

    print(f"L1_M4_H3_NU0_ZERO_B_VALUE_COSET_CERTIFICATE_PASS checks={checks}")


if __name__ == "__main__":
    main()
