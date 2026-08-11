#!/usr/bin/env python3
"""Guard the determinant interfaces and their nonclaims."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
text = "\n".join(
    (ROOT / name).read_text()
    for name in ("statement.md", "proof.md", "audit.md", "claim_contract.md")
)

for token in (
    "det M_0[x]=D_0 Q(U,V;x)",
    "signed maximal-minor vector",
    "det(M_1+tau nu(x)nu(x)^T)=tau D_1 Q(U,V;x)^2",
    "Q(U,V;x_*)=c g_* S_B^3",
    "D_1 g_*^2 S_B^6",
    "scalar `c^2` need not be a sixth power",
    "no target promotion",
):
    assert token in text, token

print("DOUBLE_ROOT_MARKED_HANKEL_DETERMINANT_GATE_AUDIT_PASS")
