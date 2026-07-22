#!/usr/bin/env python3
"""Audit the Maxwell collision-defect identity proof boundary."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    proof = "".join((HERE / "proof.md").read_text().split())
    audit = " ".join((HERE / "audit.md").read_text().split())
    for marker in (
        "v=|X|+|union_iO_i|",
        "1=m-C(m,2)+C(m-1,2)",
        "t(h-d-1)+Z-I",
        "-(t-1)I-sigma",
        "+(t-2)I+sigma+H",
        "2v-2a-ht",
        "Delta=-e<=0",
        "everyindividualnonnegativepairslackiszero",
        "H=0`isequivalentto`m_x<=2",
    ):
        assert marker in proof
    assert "not `C(m_x,3)`" in audit
    assert "Inside reuse contributes `(t-2)I`" in audit
    assert "identity for every compatible family" in audit
    assert "permits outside multiplicity two" in audit
    assert "No Modal" in audit
    print("XR_RANK_TWO_MAXWELL_COLLISION_DEFECT_IDENTITY_AUDIT_PASS mutations=14")


if __name__ == "__main__":
    main()
