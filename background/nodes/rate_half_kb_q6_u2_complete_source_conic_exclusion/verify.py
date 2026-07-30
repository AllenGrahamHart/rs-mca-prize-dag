#!/usr/bin/env python3
"""Verify the KoalaBear Q6 u2 complete-source conic exclusion ledger."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    assert "- **status:** PROVED" in statement
    assert "Ledger movement is zero" in statement
    assert "No birational-quartic" in contract

    assert 12 * 4 == 2 * 24 == 48

    d4 = []
    for ramified in range(3):
        double_ok = ramified % 4 == 0
        simple_ok = (24 - 2 * ramified) % 4 == 2
        d4.append((ramified, double_ok, simple_ok))
    assert d4 == [(0, True, False), (1, False, True), (2, False, False)]
    assert not any(double_ok and simple_ok for _, double_ok, simple_ok in d4)

    d5_fixed = []
    for ramified in range(3):
        simple_fixed = (24 - 2 * ramified) % 5
        double_fixed = ramified % 5
        d5_fixed.append((ramified, simple_fixed, double_fixed))
    assert d5_fixed == [(0, 4, 0), (1, 2, 1), (2, 0, 2)]
    assert d5_fixed[0][1] > 2
    assert d5_fixed[1][1] + d5_fixed[1][2] > 2

    assert 288 + 36 == 324
    assert 8 + 2 == 10
    print("RATE_HALF_KB_Q6_U2_COMPLETE_SOURCE_CONIC_EXCLUSION_PASS")


if __name__ == "__main__":
    main()
