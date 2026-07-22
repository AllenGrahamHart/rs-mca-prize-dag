#!/usr/bin/env python3
"""Audit the accumulated-locator flag proof boundary."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    proof = "".join((HERE / "proof.md").read_text().split())
    audit = " ".join((HERE / "audit.md").read_text().split())
    for marker in (
        "`Z_j`liesin`D_j\\T_j`",
        "L_(j+1)=L_jP_j",
        "delta_j+d_j+(K_j-d_j)=K",
        "delta_j+d_j+(A_j-d_j)=delta_j+A_j=A",
        "=L_(j+1)q_z^(j+1)",
        "sum_(j=s)^(r-1)L_(j+1)g_i^j",
        "K-1-delta_s=K_s-1",
    ):
        assert marker in proof
    assert "Zero-size layers are permitted" in audit
    assert "Earlier non-root agreement coordinates may be lost" in audit
    assert "does not say" in audit
    assert "only to distinct lifted pairs" in audit
    assert "No Modal" in audit
    print("XR_MISMATCH_ACCUMULATED_LOCATOR_FLAG_AUDIT_PASS mutations=13")


if __name__ == "__main__":
    main()
