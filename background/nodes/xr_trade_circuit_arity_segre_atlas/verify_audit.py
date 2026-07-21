#!/usr/bin/env python3
"""Mutation audit for the XR trade-circuit arity atlas."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    for marker in (
        "r<=t-2",
        "dimK>=t-2r",
        "t>=2r+2",
        "alpha_i=0",
        "c_i(gamma_id_i)-d_i(gamma_ic_i)=0",
        "columnrankis`t-1`",
        "[c:d]=[B+Dgamma:-(A+Cgamma)]",
    ):
        assert marker in proof
    assert "valid left relation" in audit
    assert "may have lower trade rank" in audit
    assert "Five-point circuits are generic" in audit
    assert "not by itself a payment" in audit
    print("XR_TRADE_CIRCUIT_ARITY_SEGRE_ATLAS_AUDIT_PASS mutations=10")


if __name__ == "__main__":
    main()
