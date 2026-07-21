#!/usr/bin/env python3
"""Independent audit for the quarter-width norm exclusion."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "background" / "nodes" / "f3_hge4_cyclotomic_norm_quarter_width_exclusion"


def delicate_endpoint_audit() -> None:
    for order in (16, 32, 64, 128, 256, 512):
        quarter = order // 4
        width = quarter + 1
        rank = width // 2
        unsharpened = (4 * width) ** quarter
        threshold = order ** (2 * rank)
        sharpened = order ** quarter
        assert unsharpened > threshold
        assert sharpened == threshold
        assert (order * order + 1) ** rank > sharpened


def parity_audit() -> None:
    for order in (16, 32, 64, 128, 256, 512, 1024):
        quarter = order // 4
        for width in range(quarter + 2, (order - 1) // 3 + 1):
            difference = width - quarter
            rank = width // 2
            assert (difference % 2 == 0) == (width % 2 == 0)
            if width % 2 == 0:
                assert 2 * rank == quarter + difference
            else:
                assert difference >= 3
                assert 2 * rank == quarter + difference - 1
                assert order ** (difference - 1) > 3 ** difference


def packet_language_audit() -> None:
    statement = (BASE / "statement.md").read_text()
    proof = (BASE / "proof.md").read_text()
    result = (BASE / "result.md").read_text()
    assert "E_h^prim(m,p)=0" in statement
    assert "m/4<=h<m/3" in statement
    assert "lower-quarter" in statement
    assert "contrary to primitivity" in proof
    assert "L=2" in proof and "alpha^2=beta^2" in proof
    assert "lower-quarter" in result.lower() and "aggregate remains open" in result.lower()
    assert "HGE4 is proved" not in statement + proof + result


def main() -> None:
    delicate_endpoint_audit()
    parity_audit()
    packet_language_audit()
    print("F3_HGE4_CYCLOTOMIC_NORM_QUARTER_WIDTH_EXCLUSION_AUDIT_PASS")


if __name__ == "__main__":
    main()
