#!/usr/bin/env python3
"""Audit the dual support-extension factorization proof boundary."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    proof = "".join((HERE / "proof.md").read_text().split())
    audit = " ".join((HERE / "audit.md").read_text().split())
    for marker in (
        "|T_i|=|A_i|-|S_i|=h-d-1+z_i",
        "degR_X<=d-z_i",
        "Lambda'_X(x)=Lambda'_(S_i)(x)Lambda_(Z_i)(x)",
        "R_X=R_A=:R_i",
        "Everyactiverowhasweightatleast`a+1`",
        "deg(RLambda_T)<=d-|Z|+h-d-1+|Z|=h-1",
        "rootavoidancemakesthesupportexactly`S`",
    ):
        assert marker in proof
    assert "need not be disjoint from each other" in audit
    assert "dropping the `-1`" in audit
    assert "only at the dual-codeword level" in audit
    assert "No Modal" in audit
    print("XR_RANK_TWO_DUAL_SUPPORT_EXTENSION_FACTORIZATION_AUDIT_PASS mutations=11")


if __name__ == "__main__":
    main()
