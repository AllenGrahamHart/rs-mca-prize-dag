#!/usr/bin/env python3
"""Guard the extra symmetric row and stronger spread claims."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
text = "\n".join(
    (ROOT / name).read_text()
    for name in ("statement.md", "proof.md", "audit.md", "claim_contract.md")
)

for token in (
    "j_(alpha,beta)>=2",
    "<=j_(alpha,beta)-1",
    "|S_alpha union S_beta|>=rho+2",
    "2h<=rho+2-sum_(gamma in A)r_gamma",
    "ceil((rho+6+r_alpha+r_beta)/2)",
    "old cyclic abstract design",
):
    assert token in text, token

print("QUADRATIC_GAP_FOUR_TWO_SLOPE_COEFFICIENT_RANK_SPREAD_AUDIT_PASS")
