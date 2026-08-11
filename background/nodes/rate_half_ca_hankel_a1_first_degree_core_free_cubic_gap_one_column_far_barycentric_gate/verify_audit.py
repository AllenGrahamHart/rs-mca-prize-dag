#!/usr/bin/env python3
"""Guard the strictness correction and boundary-only identity."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
text = "\n".join(
    (ROOT / name).read_text()
    for name in ("statement.md", "proof.md", "audit.md", "claim_contract.md")
)

for token in (
    "|S_alpha union S_beta|>=rho+1",
    "|S_beta\\S_alpha|>=c_alpha+1",
    "equality branch `(TSV7)` never occurs",
    "mu_x R_alpha(x)",
    "kappa_(alpha,beta)/P_(alpha,beta)'(x)",
    "Barycentric uniqueness is asserted only",
):
    assert token in text, token

print("CORE_FREE_CUBIC_GAP_ONE_COLUMN_FAR_BARYCENTRIC_AUDIT_PASS")
