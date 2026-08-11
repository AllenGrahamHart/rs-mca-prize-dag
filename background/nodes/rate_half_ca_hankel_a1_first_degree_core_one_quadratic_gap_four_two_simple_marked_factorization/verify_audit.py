#!/usr/bin/env python3
"""Guard square/cube exponents and shared-root scope."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
text = "\n".join(
    (ROOT / name).read_text()
    for name in ("statement.md", "proof.md", "audit.md", "claim_contract.md")
)

for token in (
    "Q(U,V;x_1)=c_1 G_1^2 S_1^3",
    "Q(U,V;x_2)=c_2 G_2^2 S_2^3",
    "D_1G_i^4S_i^6",
    "d/dz (Q(z;x_i)/G_i(z)^2)=0",
    "Shared roots are permitted",
    "need not be sixth powers",
):
    assert token in text, token

print("QUADRATIC_GAP_FOUR_TWO_SIMPLE_MARKED_FACTORIZATION_AUDIT_PASS")
