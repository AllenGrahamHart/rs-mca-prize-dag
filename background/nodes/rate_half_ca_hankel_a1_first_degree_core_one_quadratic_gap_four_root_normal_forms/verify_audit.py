#!/usr/bin/env python3
"""Guard the scope and divisor distinctions in the gap-four theorem."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
text = "\n".join(
    (ROOT / name).read_text()
    for name in ("statement.md", "proof.md", "audit.md", "claim_contract.md")
)

for token in (
    "u>=4",
    "O=0",
    "I_0=0",
    "V_*=R_*+3B",
    "div(s_F)=R_*+2B",
    "(q_1,q_2)=(3,9)",
    "V_i=2R_i+3P_i",
    "only its canonical reduced-root quotient section",
    "neither pattern is excluded",
):
    assert token in text, token

print("CORE_ONE_QUADRATIC_GAP_FOUR_NORMAL_FORMS_AUDIT_PASS")
