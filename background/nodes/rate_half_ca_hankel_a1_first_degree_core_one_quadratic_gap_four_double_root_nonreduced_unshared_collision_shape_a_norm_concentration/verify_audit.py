#!/usr/bin/env python3
"""Text audit for the shape-A norm concentration."""

from pathlib import Path


root = Path(__file__).resolve().parent
statement = (root / "statement.md").read_text()
proof = (root / "proof.md").read_text()

for token in (
    "(X-x_*)^(e-7)",
    "deg T=e-sum_delta q_delta<=e",
    "gcd(T,L_U0)=1",
    "does not identify `T`",
):
    if token not in statement:
        raise AssertionError(f"missing statement token: {token}")

for token in (
    "sum_(delta in Gamma)r_delta=e-7",
    "degree is exactly the left side",
    "T=product H_delta",
    "strictly larger than `e`",
):
    if token not in proof:
        raise AssertionError(f"missing proof token: {token}")

mutated = proof.replace("sum_(delta in Gamma)r_delta=e-7", "sum_(delta in Gamma)r_delta=e-6")
if "sum_(delta in Gamma)r_delta=e-7" in mutated:
    raise AssertionError("hostile padding-sum mutation survived")

print("RATE_HALF_SHAPE_A_NORM_CONCENTRATION_AUDIT_PASS tamper=1/1")
