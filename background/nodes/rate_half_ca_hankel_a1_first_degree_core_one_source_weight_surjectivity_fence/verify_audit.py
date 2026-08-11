#!/usr/bin/env python3
"""Guard the diagonal formula and the limits of source universality."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
text = "\n".join(
    (ROOT / name).read_text()
    for name in ("statement.md", "proof.md", "audit.md", "claim_contract.md")
)

for token in (
    "omega_x=(x-s_0)v_xa_x",
    "diagonal linear isomorphism",
    "2d+1=2rho-1",
    "is surjective",
    "column-farness",
    "do not seek a source-only positivity",
    "additional column-farness",
):
    assert token in text, token

print("CORE_ONE_SOURCE_WEIGHT_SURJECTIVITY_FENCE_AUDIT_PASS")
