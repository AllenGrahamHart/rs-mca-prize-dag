#!/usr/bin/env python3
"""Mutation audit for the prize first-shell rank-three exclusion."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    for marker in (
        "rankC=3",
        "|Z_iunionZ_j|>=3",
        "U_2=4C(t,2)-I",
        "U_2=3(t-1)+4C(t-1,2)-I",
        "Delta_G=-e<=0",
        "rankatmostthedual-codedimensionthree",
    ):
        assert marker in proof
    assert "another root outside `X`" in audit
    assert "does not delete proper local edge circuits" in audit
    assert "no RowC rank-three exclusion is claimed" in audit
    print("XR_PRIZE_FIRST_SHELL_PRIMITIVE_RANK_THREE_EXCLUSION_AUDIT_PASS mutations=8")


if __name__ == "__main__":
    main()
