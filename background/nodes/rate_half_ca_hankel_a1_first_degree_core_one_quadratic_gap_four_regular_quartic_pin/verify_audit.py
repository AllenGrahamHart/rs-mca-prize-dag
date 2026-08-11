#!/usr/bin/env python3
"""Guard rank-loss multiplicities and quartic nonclaims."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
text = "\n".join(
    (ROOT / name).read_text()
    for name in ("statement.md", "proof.md", "audit.md", "claim_contract.md")
)

for token in (
    "D_1=a g_*E_4",
    "D_1=a G_1G_2E_4",
    "E_4 g_*^3S_B^6",
    "E_4 G_1^5G_2S_1^6",
    "E_4 G_1G_2^5S_2^6",
    "including exponent two at every common root",
    "No identification with `S_B^2` or `S_1S_2`",
):
    assert token in text, token

print("QUADRATIC_GAP_FOUR_REGULAR_QUARTIC_PIN_AUDIT_PASS")
