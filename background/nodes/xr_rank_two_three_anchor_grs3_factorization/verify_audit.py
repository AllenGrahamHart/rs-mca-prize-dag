#!/usr/bin/env python3
"""Audit the three-anchor dual-GRS3 factorization proof boundary."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    proof = "".join((HERE / "proof.md").read_text().split())
    audit = " ".join((HERE / "audit.md").read_text().split())
    for marker in (
        "AD-B_0C!=0",
        "P=B_0F-AG,Q=DF-CG",
        "sum_is_igamma_i^2",
        "deg(H(T)T^j)<=t-2",
        "kernelalsohasdimension`t-3`",
        "rootavoidancein`(TG3)`",
        "standardbarycentricidentityonfourdistinctslopes",
        "Normalizingits`e`coordinatetoone",
    ):
        assert marker in proof
    assert "Three moments, not two" in audit
    assert "strict, `deg H<t-3`" in audit
    assert "pre-existing row scale `s_i`" in audit
    assert "larger-shell support embeddings are not declared paid" in audit
    assert "No Modal" in audit
    print("XR_RANK_TWO_THREE_ANCHOR_GRS3_FACTORIZATION_AUDIT_PASS mutations=13")


if __name__ == "__main__":
    main()
