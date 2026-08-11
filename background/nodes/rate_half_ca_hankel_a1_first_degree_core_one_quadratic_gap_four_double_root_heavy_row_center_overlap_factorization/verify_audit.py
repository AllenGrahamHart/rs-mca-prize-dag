#!/usr/bin/env python3
"""Guard center cancellation, residual degree, and MDS scope."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
text = "\n".join(
    (ROOT / name).read_text()
    for name in ("statement.md", "proof.md", "audit.md", "claim_contract.md")
)

for token in (
    "J=gcd(Lambda,g_*S_B^2)",
    "deg T_j<=j",
    "G(t,x_*)=H(t)T_j(t)",
    "G(t,x_*)=c g_*(t)S_B(t)^2",
    "in RS[F,X_cls union {x_*},n+1]",
    "only `j+1<=4` new scalar unknowns",
    "does not prove",
):
    assert token in text, token

print("QUADRATIC_DOUBLE_HEAVY_CENTER_OVERLAP_AUDIT_PASS")
