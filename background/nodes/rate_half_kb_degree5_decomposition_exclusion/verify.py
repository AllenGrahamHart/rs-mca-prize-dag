#!/usr/bin/env python3
"""Verify the deployed-field degree-five exclusion arithmetic."""

from math import gcd
from pathlib import Path


NODE = Path(__file__).resolve().parent
P = 2130706433
EXTENSION_DEGREE = 6


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    assert "- **status:** PROVED" in statement
    assert "{2,3,4,6,10,12,30}" in statement
    assert "No claim is made for inner degree" in contract

    q = P**EXTENSION_DEGREE
    assert P % 5 == 3
    assert q % 5 == 4
    assert gcd(5, q - 1) == 1
    assert 2 * (5 - 1) == 2 * 5 - 2
    assert 12 * 5 == 60
    print("RATE_HALF_KB_DEGREE5_DECOMPOSITION_EXCLUSION_PASS")


if __name__ == "__main__":
    main()
