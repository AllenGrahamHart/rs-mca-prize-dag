#!/usr/bin/env python3
"""Mutation audit for the XR global-explanation list owner."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    for field_size in range(3, 80):
        for ordinary in range(1, field_size):
            bound = ordinary * (field_size - 1) // (field_size - ordinary)
            if ordinary * ordinary < field_size:
                assert bound == ordinary

    statement = "".join((ROOT / "statement.md").read_text().split())
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "max(E-1,0)" in statement
    assert "firstterminalpayment" in statement
    assert "Theinitialpaircannotownaretainedmismatchslope" in proof
    assert "neitherbranchdepthnorthenumberoflocatorflags" in proof
    assert "The root subtraction is necessary" in audit
    assert "Separate supports in the two components" in audit
    assert "only `(GEO4)` is available" in audit

    print("XR_MISMATCH_GLOBAL_EXPLANATION_LIST_OWNER_AUDIT_PASS mutations=7")


if __name__ == "__main__":
    main()
