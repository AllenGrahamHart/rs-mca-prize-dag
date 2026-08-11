#!/usr/bin/env python3
"""Guard the construction and its strict support-only scope."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
text = "\n".join(
    (ROOT / name).read_text()
    for name in (
        "statement.md",
        "proof.md",
        "audit.md",
        "claim_contract.md",
        "falsification.md",
    )
)

for token in (
    "sigma_j=floor(7(j+1)/b)-floor(7j/b)",
    "3b-7=9e+2=3rho+5",
    "z=e-6",
    "1+(3rho+5)+1+(rho-7)=4rho=N",
    "support-degree arguments alone",
    "numerical evidence only",
    "no codeword-center assignment",
):
    assert token in text, token

print("QUADRATIC_GAP_FOUR_ABSTRACT_INCIDENCE_DESIGN_AUDIT_PASS")
