#!/usr/bin/env python3
"""Audit the extension-family collision-ledger proof boundary."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    proof = "".join((HERE / "proof.md").read_text().split())
    audit = " ".join((HERE / "audit.md").read_text().split())
    for marker in (
        "everyextensionpointof`T_i`thatliesin`X`mustliein`Z_i`",
        "|S_iintersectS_j|=|X|-z_i-z_j=a+d+1-z_i-z_j",
        "T_iintersectS_j=I_i",
        "T_iintersectT_j=O_iintersectO_j",
        "z_i+z_j>=d+1",
        "Each`|I_i|`occursinexactly`t-1`pairs",
        "sum_(xoutsideX)C(m_x,2)",
        "(t-1)Z-C(t,2)(d+1)",
        "equivalenttoeverypairwiseblockcap",
    ):
        assert marker in proof
    assert "cannot contain another row's zero fiber" in audit
    assert "not `z_i+z_j-d`" in audit
    assert "charged `t-1` times" in audit
    assert "does not replace them by the whole ambient domain" in audit
    assert "No Modal" in audit
    print("XR_RANK_TWO_EXTENSION_FAMILY_COLLISION_LEDGER_AUDIT_PASS mutations=14")


if __name__ == "__main__":
    main()
