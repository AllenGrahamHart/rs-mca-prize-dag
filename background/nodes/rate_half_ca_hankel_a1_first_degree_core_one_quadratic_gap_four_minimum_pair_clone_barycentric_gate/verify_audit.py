#!/usr/bin/env python3
"""Audit semantic pins for the minimum-pair clone-barycentric gate."""

from pathlib import Path


root = Path(__file__).resolve().parent
statement = (root / "statement.md").read_text()
proof = (root / "proof.md").read_text()
audit = (root / "audit.md").read_text()

for token in ["r_alpha+2", "lambda_x", "L_X'(x)", "reverse orientation"]:
    assert token in statement
for token in ["rank", "squarefree", "Vandermonde", "x-s_0"]:
    assert token in proof
for token in ["actual error supports", "dual multiplier", "sharp pair union"]:
    assert token in audit

print("QUADRATIC_GAP_FOUR_MINIMUM_PAIR_CLONE_BARYCENTRIC_GATE_AUDIT_PASS")
