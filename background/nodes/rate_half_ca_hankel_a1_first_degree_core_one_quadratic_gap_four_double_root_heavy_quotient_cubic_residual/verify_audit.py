#!/usr/bin/env python3
"""Guard the D1 divisibility, cubic recurrence, and one-chain conclusion."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
text = "\n".join(
    (ROOT / name).read_text()
    for name in ("statement.md", "proof.md", "audit.md", "claim_contract.md")
)

for token in (
    "P_F(t,x_*)=D_1(t)C_0(t)",
    "M(t)u(t)=D_1(t)C(t)",
    "deg_t C<=3",
    "C_(i+1)=x_* C_i-kappa S_B h_i",
    "S_B is squarefree",
    "gcd(g_*,S_B)=1",
    "Smith type `[2]`, not `[1,1]`",
    "no `D_1`-divisibility or Smith",
    "does not exclude",
):
    assert token in text, token

print("QUADRATIC_DOUBLE_ROOT_HEAVY_QUOTIENT_CUBIC_AUDIT_PASS")
