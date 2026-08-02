#!/usr/bin/env python3
"""Scope and mutation audit for the primitive residue ledger."""

import runpy
from pathlib import Path


HERE = Path(__file__).parent
ROOT = HERE.parents[2]
statement = (HERE / "statement.md").read_text()
contract = (HERE / "claim_contract.md").read_text()
assert "generic squared signed-pair algebra" in statement
assert "does not lift" in statement
assert "No source-configuration count" in contract
for script in (
    "audit_rate_half_kb_positive_433_1a_cell5_pair_primitive_polynomial.py",
    "audit_rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization.py",
):
    runpy.run_path(
        str(ROOT / "experiments/prize_resolution" / script),
        run_name="__main__",
    )
print("positive 433-1a cell-5 signed-pair primitive-ledger audit verified")
