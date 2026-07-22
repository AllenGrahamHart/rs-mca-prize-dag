#!/usr/bin/env python3
"""Mutation audit for the embedded-family arithmetic."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    caught = 0
    for p, m in ((7, 4), (31, 8), (127, 16)):
        nbase = p + 1
        n = m * nbase
        correct = (m // 2) * nbase
        assert correct == n // 2
        assert m * nbase != n // 2
        assert (m // 2) * (nbase // 2) != n // 2
        caught += 2
    statement = (HERE / "statement.md").read_text()
    assert "d=p, p+1" in statement
    assert "does not classify all" in statement
    assert "zero is not a split value" in statement
    assert "m=4:       h=2" in statement
    caught += 4
    print(f"L1_MERSENNE_CHECKPOINT_EMBEDDED_M2_FAMILY_AUDIT_PASS checks={caught}")


if __name__ == "__main__":
    main()
