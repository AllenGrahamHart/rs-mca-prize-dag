#!/usr/bin/env python3
"""Scope audit for the deployed cell-5 rational lift atlas."""

from pathlib import Path


HERE = Path(__file__).parent
statement = (HERE / "statement.md").read_text()
contract = (HERE / "claim_contract.md").read_text()
assert "is injective" in statement
assert "does not assert that every" in statement
assert "Surjectivity" in contract
assert "signed-family/colored-edge emptiness" in contract
print("positive 433-1a cell-5 rational lift atlas scope audit verified")
