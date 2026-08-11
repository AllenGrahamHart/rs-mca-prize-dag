#!/usr/bin/env python3
"""Guard the scope distinctions in the quadratic root router."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
text = "\n".join(
    (ROOT / name).read_text()
    for name in ("statement.md", "proof.md", "audit.md", "claim_contract.md")
)

for token in (
    "O=u-4",
    "t_E>=e+2-2u-I_0+epsilon_E",
    "t_x<=c_x+epsilon_x",
    "(2-r)e<=3u+2I_0<=5u",
    "one double heavy root",
    "two distinct heavy roots",
    "estimate is imported into the double-root branch",
    "neither retained pattern is excluded",
):
    assert token in text, token

print("CORE_ONE_QUADRATIC_ROOT_MULTIPLICITY_ROUTER_AUDIT_PASS")
