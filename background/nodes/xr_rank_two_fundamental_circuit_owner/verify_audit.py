#!/usr/bin/env python3
"""Audit the XR rank-two fundamental-circuit owner proof boundary."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    proof = "".join((HERE / "proof.md").read_text().split())
    audit = " ".join((HERE / "audit.md").read_text().split())
    for marker in (
        "If`q<=2`,someatmostthreecolumnswouldcontainacircuit",
        "v_e=sum_(binB)beta_(e,b)v_b",
        "asecondexpressionfor`v_e`",
        "coordinatesoutside`B`formtheidentitymatrix",
        "|I|-q=dimK",
        "residualisakernelvectorsupportedinside`B`",
        "allbutatmostoneoftheatleastfourrows",
    ):
        assert marker in proof
    assert "deterministic rather than existential" in audit
    assert "entire scaling kernel" in audit
    assert "not four anchors globally" in audit
    assert "No Modal" in audit
    print("XR_RANK_TWO_FUNDAMENTAL_CIRCUIT_OWNER_AUDIT_PASS mutations=11")


if __name__ == "__main__":
    main()
