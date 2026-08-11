#!/usr/bin/env python3
"""Guard the symmetric radical and exact correction exclusions."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
text = "\n".join(
    (ROOT / name).read_text()
    for name in ("statement.md", "proof.md", "audit.md", "claim_contract.md")
)

for token in (
    "rank B_gamma=c",
    "rad B_gamma=span{R_gamma}",
    "dot Phi(Q_min^2 X(X-r_gamma))=0",
    "dot Phi(Q_min^2)!=0",
    "ord_gamma(D_1)=c",
    "every positive Smith exponent is one",
    "except at most two projective slopes",
    "at most four",
):
    assert token in text, token

print("QUADRATIC_GAP_FOUR_SUPPORTED_FIRST_JET_PAIRING_AUDIT_PASS")
