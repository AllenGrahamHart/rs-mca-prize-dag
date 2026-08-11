#!/usr/bin/env python3
"""Guard the exact design and the coding hypotheses in the spread proof."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
text = "\n".join(
    (ROOT / name).read_text()
    for name in ("statement.md", "proof.md", "audit.md", "claim_contract.md")
)

for token in (
    "|L|=3rho+5",
    "deg_Z(x_*)=e-6",
    "|H_0|=rho-7",
    "minimum distance `2rho+1`",
    "wt(f_gamma-c_gamma)=rho-1",
    "Column-farness",
    "h<=rho+1-r",
    "3+|{alpha,beta} intersect Z_*|",
    "strict subsets of the padded locator blocks",
):
    assert token in text, token

print("QUADRATIC_GAP_FOUR_INCIDENCE_CENTER_SPREAD_AUDIT_PASS")
