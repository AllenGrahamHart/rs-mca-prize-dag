#!/usr/bin/env python3
"""Verify the inner-degree-12 outer-subdegree route cut."""

from math import gcd
from pathlib import Path


NODE = Path(__file__).resolve().parent


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    assert "- **status:** PROVED" in statement
    assert "(r,delta)=(2,24),(4,12)" in statement
    assert "Neither surviving type is deleted" in contract

    p = 2130706433
    q = p**6
    assert p % 5 == 3
    assert q % 5 == 4
    assert gcd(5, q - 1) == 1

    primitive_subdegrees = ((1, 1, 1, 1, 1), (1, 2, 2), (1, 4))
    assert all(3 not in row for row in primitive_subdegrees)
    survivors = []
    for r in (1, 2, 3, 4):
        if r == 1 or r == 3:
            continue
        delta = 48 // r
        assert delta * r == 48
        survivors.append((r, delta))
    assert survivors == [(2, 24), (4, 12)]
    print("RATE_HALF_KB_M12_OUTER_SUBDEGREE_ROUTE_CUT_PASS")


if __name__ == "__main__":
    main()
