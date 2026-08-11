#!/usr/bin/env python3
"""Guard the derivative radical and the w=1 exception."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
text = "\n".join(
    (ROOT / name).read_text()
    for name in ("statement.md", "proof.md", "audit.md", "claim_contract.md")
)

for token in (
    "rank B_gamma=c",
    "rad_right(B_gamma)=span{R_gamma}",
    "dot Phi(Q_min^2(X-r_gamma))=0",
    "dot Phi(Q_min^2)!=0",
    "positive Smith exponent is",
    "except possibly the single projective slope cut out by",
):
    assert token in text, token

print("CORE_FREE_CUBIC_GAP_ONE_FIRST_JET_PAIRING_AUDIT_PASS")
