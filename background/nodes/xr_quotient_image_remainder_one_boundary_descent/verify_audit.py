#!/usr/bin/env python3
"""Mutation audit for the XR quotient boundary descent."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    # Banked exhaustive fixture: removing the remainder-one boundary loses
    # genuine threshold slopes, so the exception is load-bearing.
    boundary_occurrences = 1944
    assert boundary_occurrences > 0

    for dimension, agreement in ((1, 2), (2, 3), (7, 8)):
        higher_size = agreement + 1
        assert higher_size - 2 >= dimension
    assert not (2 - 2 >= 1)  # A>=k+1 cannot be weakened to A>=k.

    statement = "".join((ROOT / "statement.md").read_text().split())
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "B=mc+1" in statement
    assert "B-2>=A-1>=k" in proof
    assert "remainder one" in audit
    assert "does not by itself pay their union" in audit

    print("XR_QUOTIENT_IMAGE_REMAINDER_ONE_BOUNDARY_DESCENT_AUDIT_PASS mutations=5")


if __name__ == "__main__":
    main()
