#!/usr/bin/env python3
"""Guard the norm gate's exact factors and one-way scope."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
text = "\n".join(
    (ROOT / name).read_text()
    for name in ("statement.md", "proof.md", "audit.md", "claim_contract.md")
)

for token in (
    "q_d(z)^deg(P) H(z)^d",
    "Xi_P=Norm_(K_C/F(z))(W)^3",
    "d Xi_P/dz=0",
    "remaining constant lying in",
    "finite base field is perfect",
    "norm test is one-way",
    "not sufficient",
    "No irreducibility assumption",
):
    assert token in text, token

print("DOUBLE_ROOT_RESULTANT_CUBE_GATE_AUDIT_PASS")
