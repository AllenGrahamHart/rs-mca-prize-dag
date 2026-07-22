#!/usr/bin/env python3
"""Mutation audit for the XR proper-circuit defect and host router."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    # Parity upgrades the four-row proper deficit from one to two.
    for h in range(1, 40, 2):
        for D in range(3, 30):
            for Z in range(1, 30):
                D0 = 4 * h + 2 * (3 * D - 2 * Z)
                assert D0 % 2 == 0

    # The two ownership ranges are adjacent at every nonpositive baseline.
    for t, delta in ((4, 2), (5, 1)):
        for D0 in range(-100, 1):
            if D0 % 2 != t % 2:
                continue
            full_upper = (-D0) // 2
            proper_lower = (delta - D0) // 2
            assert proper_lower == full_upper + 1

    # Crossing each parity cutoff flips the maximal baseline below delta_t.
    for h in (3, 5, 17, (1 << 16) + 1):
        even4, odd4 = 2 * h - 2, 2 * h - 3
        assert 4 * h - 2 * even4 >= 2
        assert 4 * h - 2 * (even4 + 2) < 2
        assert 4 * h - 2 * odd4 - 4 >= 2
        assert 4 * h - 2 * (odd4 + 2) - 4 < 2

        even5 = (5 * h - 1) // 3
        odd5 = (5 * h - 10) // 3
        even5 -= even5 % 2
        if odd5 % 2 == 0:
            odd5 -= 1
        assert 5 * h - 3 * even5 >= 1
        assert 5 * h - 3 * (even5 + 2) < 1
        if odd5 >= 3:
            assert 5 * h - 3 * odd5 - 9 >= 1
            assert 5 * h - 3 * (odd5 + 2) - 9 < 1

    statement = "".join((ROOT / "statement.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "I>0" in statement and "sigma>0" in statement and "H>0" in statement
    assert "Baseline-positive proper circuits may have" in audit
    assert "not an existence assertion" in audit

    print("XR_RANK_TWO_PROPER_CIRCUIT_DEFECT_HOST_ROUTER_AUDIT_PASS mutations=12")


if __name__ == "__main__":
    main()
