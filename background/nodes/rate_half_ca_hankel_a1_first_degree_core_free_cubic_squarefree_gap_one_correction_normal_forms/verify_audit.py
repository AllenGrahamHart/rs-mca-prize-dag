#!/usr/bin/env python3
"""Guard the scope and route fences in the squarefree gap-one proof."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
text = "\n".join(
    (ROOT / name).read_text()
    for name in ("statement.md", "proof.md", "audit.md", "claim_contract.md")
)

for token in (
    "q_h=3",
    "V_i=R_i+N_i+3P_i",
    "V_i=R_i+N_i-J+3P_i",
    "V_i=R_i+N_i+2J",
    "degree `e+1`",
    "not an independent ambient section",
    "no positive deficit partition or packet is excluded",
):
    assert token in text, token

print("CUBIC_SQUAREFREE_GAP_ONE_NORMAL_FORMS_AUDIT_PASS")
