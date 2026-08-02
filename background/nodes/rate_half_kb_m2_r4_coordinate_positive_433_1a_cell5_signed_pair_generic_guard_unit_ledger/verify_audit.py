#!/usr/bin/env python3
"""Scope and mutation audit for the generic guard-unit ledger."""

import runpy
from pathlib import Path


HERE = Path(__file__).parent
ROOT = HERE.parents[2]
statement = (HERE / "statement.md").read_text()
contract = (HERE / "claim_contract.md").read_text()
assert "does not calculate" in statement
assert "No finite-fiber guard theorem" in contract
runpy.run_path(
    str(
        ROOT
        / "experiments/prize_resolution"
        / "audit_rate_half_kb_positive_433_1a_cell5_pair_generic_guard_units.py"
    ),
    run_name="__main__",
)
print("positive 433-1a cell-5 signed-pair generic-guard-unit audit verified")
