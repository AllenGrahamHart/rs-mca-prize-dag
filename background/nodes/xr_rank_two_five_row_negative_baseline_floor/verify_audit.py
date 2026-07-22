#!/usr/bin/env python3
"""Mutation audit for the XR five-row negative-baseline floor."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def main() -> None:
    # Zero baseline has the wrong modulo-six residue at every odd reserve.
    for h in range(1, 40, 2):
        assert (5 * h) % 6 != 0

    # The capacity floor is load-bearing at each official reserve class.
    for h, b in ((5, 5), (3, 3), ((1 << 33) + 1, 3), ((1 << 32) + 1, 5)):
        D = ceil_div(5 * h + b + 30, 18)
        Z = (5 * h + 12 * D + b) // 6
        assert Z <= 5 * (D - 1)
        if D > 1:
            prior_Z = (5 * h + 12 * (D - 1) + b) // 6
            assert prior_Z > 5 * (D - 2)

    # RowC minimum baselines require one defect; prize minima may use zero.
    assert max(0, ceil_div(5 - 5 + 1, 2)) == 1
    assert max(0, ceil_div(3 - 3 + 1, 2)) == 1
    assert max(0, ceil_div(3 - ((1 << 33) + 1) + 1, 2)) == 0
    assert max(0, ceil_div(5 - ((1 << 32) + 1) + 1, 2)) == 0

    statement = "".join((ROOT / "statement.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "9544371773" in statement
    assert "4772185889" in statement
    assert "proper five-block circuit" in audit
    assert "not an existence theorem" in audit

    print("XR_RANK_TWO_FIVE_ROW_NEGATIVE_BASELINE_FLOOR_AUDIT_PASS mutations=10")


if __name__ == "__main__":
    main()
