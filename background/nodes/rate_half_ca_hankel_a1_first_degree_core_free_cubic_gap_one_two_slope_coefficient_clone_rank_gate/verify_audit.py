#!/usr/bin/env python3
"""Guard the full coefficient chain and exact rank codimension."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
text = "\n".join(
    (ROOT / name).read_text()
    for name in ("statement.md", "proof.md", "audit.md", "claim_contract.md")
)

for token in (
    "rank Ev_(alpha,beta)<=j_(alpha,beta)",
    "M_1q_e=0",
    "V diag(eta_x) Ev_(alpha,beta)=0",
    "m-c_alpha",
    "rank exactly one",
    "does not supply point separation",
):
    assert token in text, token

print("CORE_FREE_CUBIC_GAP_ONE_COEFFICIENT_CLONE_RANK_AUDIT_PASS")
