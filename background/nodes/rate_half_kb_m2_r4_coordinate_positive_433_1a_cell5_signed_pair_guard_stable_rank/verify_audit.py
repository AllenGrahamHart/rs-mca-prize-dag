#!/usr/bin/env python3
"""Scope and hostile-mutation audit for the cell-5 stable-rank theorem."""

import runpy
from pathlib import Path


HERE = Path(__file__).parent
ROOT = HERE.parents[2]
statement = (HERE / "statement.md").read_text()
contract = (HERE / "claim_contract.md").read_text()
assert "does not assert that" in statement
assert "generic-function-field length" in statement
assert "No reducedness" in contract
runpy.run_path(
    str(
        ROOT
        / "experiments/prize_resolution/"
        "audit_rate_half_kb_positive_433_1a_cell5_pair_guard_stable_rank.py"
    ),
    run_name="__main__",
)
print("positive 433-1a cell-5 signed-pair stable-rank scope audit verified")
