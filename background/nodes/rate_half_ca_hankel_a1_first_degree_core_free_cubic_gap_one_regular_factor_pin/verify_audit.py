#!/usr/bin/env python3
"""Guard exact-supported cases and the linear-factor nonclaims."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
text = "\n".join(
    (ROOT / name).read_text()
    for name in ("statement.md", "proof.md", "audit.md", "claim_contract.md")
)

for token in (
    "P_C=product_gamma L_gamma^c_gamma",
    "D_0=a P_C E_w",
    "`1,0,0,0`",
    "det M_0[x]=a P_C E_w Q(U,V;x)",
    "`E_1` may repeat a factor already present in `P_C`",
    "No equality between `E_1` and the degree-one Picard correction",
):
    assert token in text, token

print("CORE_FREE_CUBIC_GAP_ONE_REGULAR_FACTOR_PIN_AUDIT_PASS")
