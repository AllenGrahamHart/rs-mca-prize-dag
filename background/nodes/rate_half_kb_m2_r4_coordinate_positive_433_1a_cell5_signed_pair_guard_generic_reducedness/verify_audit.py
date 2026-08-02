#!/usr/bin/env python3
"""Scope and mutation audit for localized signed-pair reducedness."""

import runpy
from pathlib import Path


HERE = Path(__file__).parent
ROOT = HERE.parents[2]
statement = (HERE / "statement.md").read_text()
contract = (HERE / "claim_contract.md").read_text()
assert "generic-function-field reducedness" in statement
assert "does not factor" in statement
assert "No residue-factor count" in contract
runpy.run_path(
    str(
        ROOT
        / "experiments/prize_resolution/"
        "audit_rate_half_kb_positive_433_1a_cell5_pair_localized_operator.py"
    ),
    run_name="__main__",
)
print("positive 433-1a cell-5 signed-pair generic-reducedness audit verified")
