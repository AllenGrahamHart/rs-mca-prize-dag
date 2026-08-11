#!/usr/bin/env python3
"""Guard the global-cube bridge against overinterpretation."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
text = "\n".join(
    (ROOT / name).read_text()
    for name in ("statement.md", "proof.md", "audit.md", "claim_contract.md")
)

for token in (
    "W^3=(J^3/R_a)(G_L/H)",
    "=(X-x_s)^2(X-x_d) G_L/H",
    "=(X-x_d) G_L/H",
    "total quotient ring",
    "pole at `R_0`",
    "does not make the biform equation a separated",
    "Characteristic three",
    "no cube is excluded",
):
    assert token in text, token

print("DOUBLE_ROOT_RADICAL_CUBE_BRIDGE_AUDIT_PASS")
