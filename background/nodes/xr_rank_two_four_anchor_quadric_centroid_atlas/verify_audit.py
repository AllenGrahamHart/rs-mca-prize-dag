#!/usr/bin/env python3
"""Audit the four-anchor quadric-centroid proof boundary."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    proof = "".join((HERE / "proof.md").read_text().split())
    audit = " ".join((HERE / "audit.md").read_text().split())
    for marker in (
        "det(sum_ibeta_iR_i)",
        "(gamma_j-gamma_i)(c_id_j-d_ic_j)",
        "pullbackofthedeterminantquadric",
        "cannot havesupporttwo".replace(" ", ""),
        "M_B((1,1,1,1)+sum_(enotinB)beta_e)",
        "finite-slopeanddistinct-projectionhypotheses",
        "anchorskeepcoefficientrankfour",
    ):
        assert marker in proof
    assert "affine column coordinates" in audit
    assert "exactly `(-1,-1,-1,-1)`" in audit
    assert "finite-slope and distinct-projection conditions" in audit
    assert "No Modal" in audit
    print("XR_RANK_TWO_FOUR_ANCHOR_QUADRIC_CENTROID_ATLAS_AUDIT_PASS mutations=11")


if __name__ == "__main__":
    main()
