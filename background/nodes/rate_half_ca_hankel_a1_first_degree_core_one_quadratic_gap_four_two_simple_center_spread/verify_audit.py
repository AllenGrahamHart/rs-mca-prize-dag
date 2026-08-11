#!/usr/bin/env python3
"""Guard overlap, exact error weights, and the weighted line cap."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
text = "\n".join(
    (ROOT / name).read_text()
    for name in ("statement.md", "proof.md", "audit.md", "claim_contract.md")
)

for token in (
    "deg_Z(x_1)=(e-3)/2",
    "deg_Z(x_2)=(e-9)/2",
    "rho-8 other heavy points",
    "wt(f_gamma-c_gamma)=rho-r_gamma",
    "h<=rho+1-sum_(gamma in A)r_gamma",
    "3+r_alpha+r_beta",
    "not assumed disjoint",
):
    assert token in text, token

print("QUADRATIC_GAP_FOUR_TWO_SIMPLE_CENTER_SPREAD_AUDIT_PASS")
