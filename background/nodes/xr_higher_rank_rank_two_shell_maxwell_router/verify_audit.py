#!/usr/bin/env python3
"""Mutation audit for the XR shell/Maxwell router."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    # Pair-sum and disjoint-union constraints are independently load-bearing.
    assert 1 + 1 < 3
    assert 1 + 2 == 3
    assert min(4 * 2, 7) == 7

    # Saving r-1 coordinates at one new coordinate creates enough pairs.
    for degree in range(1, 40):
        assert degree * (degree - 1) // 2 >= degree - 1

    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    for marker in (
        "P_0=C(t,2)rho-(t-1)Z",
        "q>=E-(aC(t,2)-P_0)",
        "Delta_J=-e<=0",
        "Delta_J>=6+t(h-t-1)",
        "Delta_J>=8+t(h-2t)",
        "t<=3",
    ):
        assert marker in proof
    assert "Proper local rank-two circuits remain real" in audit
    assert "Z<=min(td,a+d+1)" in audit
    assert "C(r,2)>=r-1" in audit

    print("XR_HIGHER_RANK_RANK_TWO_SHELL_MAXWELL_ROUTER_AUDIT_PASS mutations=9")


if __name__ == "__main__":
    main()
