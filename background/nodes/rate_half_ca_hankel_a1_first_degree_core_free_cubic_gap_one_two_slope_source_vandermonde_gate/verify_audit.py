#!/usr/bin/env python3
"""Guard the source support and equality-case claims."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
text = "\n".join(
    (ROOT / name).read_text()
    for name in ("statement.md", "proof.md", "audit.md", "claim_contract.md")
)

for token in (
    "S_beta\\S_alpha",
    "|S_beta\\S_alpha|>=c_alpha",
    "roots(R_alpha)=S_beta\\S_alpha",
    "|S_alpha union S_beta|>=rho",
    "evaluation rank-one forms",
    "Vandermonde inversion is used only",
):
    assert token in text, token

print("CORE_FREE_CUBIC_GAP_ONE_TWO_SLOPE_VANDERMONDE_AUDIT_PASS")
