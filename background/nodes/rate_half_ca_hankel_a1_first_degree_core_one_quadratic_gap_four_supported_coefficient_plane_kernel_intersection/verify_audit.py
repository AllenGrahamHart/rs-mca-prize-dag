#!/usr/bin/env python3
"""Guard the exact rank-one statement and scoped rank-two alternative."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
text = "\n".join(
    (ROOT / name).read_text()
    for name in ("statement.md", "proof.md", "audit.md", "claim_contract.md")
)

for token in (
    "dim(H_gamma/span{Q_gamma})<=floor(c/2)",
    "e-floor(c/2)<=rank E_gamma<=e",
    "H_gamma=span{Q_gamma}",
    "rank E_gamma=e",
    "rank E_gamma in {e-1,e}",
    "totally isotropic",
    "away from the correction divisor",
):
    assert token in text, token

print("QUADRATIC_SUPPORTED_COEFFICIENT_KERNEL_INTERSECTION_AUDIT_PASS")
