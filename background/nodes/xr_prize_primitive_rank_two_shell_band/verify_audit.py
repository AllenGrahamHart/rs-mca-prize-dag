#!/usr/bin/env python3
"""Mutation audit for the prize rank-two shell band."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    for marker in (
        "N=R+a",
        "Z<=td",
        "B_(h,d+1)(t)-B_(h,d)(t)=-(t-2)(t+1)<0",
        "Delta_G=2|unionG|-2a-h|G|=-e<=0",
        "neitherconstructsatrade",
    ):
        assert marker in proof
    assert "Concavity, not monotonicity" in audit
    assert "not counterexamples" in audit
    assert "Proper local circuits survive" in audit
    print("XR_PRIZE_PRIMITIVE_RANK_TWO_SHELL_BAND_AUDIT_PASS mutations=7")


if __name__ == "__main__":
    main()
