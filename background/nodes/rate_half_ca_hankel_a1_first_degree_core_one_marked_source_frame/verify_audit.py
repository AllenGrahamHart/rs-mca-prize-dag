#!/usr/bin/env python3
"""Guard the source formula, isotropy, and cancellation fences."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
text = "\n".join(
    (ROOT / name).read_text()
    for name in ("statement.md", "proof.md", "audit.md", "claim_contract.md")
)

for token in (
    "q_i^T M_s q_j=0",
    "sum_(x in D_res) omega_x^(s) v_xv_x^T=0",
    "Vand(x_*,J)^2",
    "C_*=D_1Q(U,V;x_*)^2",
    "c^2D_1g_*^2S_B^6",
    "termwise",
    "does not promote the critical target",
):
    assert token in text, token

print("CORE_ONE_MARKED_SOURCE_FRAME_AUDIT_PASS")
