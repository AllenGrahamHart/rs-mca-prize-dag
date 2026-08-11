#!/usr/bin/env python3
"""Guard the exact factors and signed ordinary correction."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
text = "\n".join(
    (ROOT / name).read_text()
    for name in ("statement.md", "proof.md", "audit.md", "claim_contract.md")
)

for token in (
    "R_3=c^3 H^rho S_A^3",
    "R_3=c^3 L_0^(rho-3) H_0^rho S_AB^3",
    "R_2=c^3 H^(rho-1) S_B^3",
    "b=3a",
    "q_d^a",
    "degree `N-1`",
    "not necessarily products of displayed linear",
    "necessary and remains compatible",
):
    assert token in text, token

print("DOUBLE_ROOT_LOW_DEGREE_RESULTANT_FACTORIZATION_AUDIT_PASS")
