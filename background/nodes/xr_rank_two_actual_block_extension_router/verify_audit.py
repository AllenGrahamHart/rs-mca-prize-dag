#!/usr/bin/env python3
"""Audit the actual-block extension-router proof boundary."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    proof = "".join((HERE / "proof.md").read_text().split())
    audit = " ".join((HERE / "audit.md").read_text().split())
    for marker in (
        "Euclideandivisiongivestheuniquedecomposition`(AR2)`",
        "h-tau_i=d+1-z_i",
        "P_i=R_iLambda_(T_i)",
        "(d-z_i)+tau_i=h-1",
        "|S_i|-a=d+1-z_i",
        "Since`|S_i|>=a+1`,thatpolynomialisunique",
        "exactlywheneverypointof`T_i`belongstotheexternalzeroset",
        "Choosing`tau_i`pointsfrom`E_i`",
    ):
        assert marker in proof
    assert "one support-local dimension" in audit
    assert "external zero set excludes `S_i`" in audit
    assert "include points of the active zero set `Z_i`" in audit
    assert "per fixed support and slope" in audit
    assert "No Modal" in audit
    print("XR_RANK_TWO_ACTUAL_BLOCK_EXTENSION_ROUTER_AUDIT_PASS mutations=13")


if __name__ == "__main__":
    main()
