#!/usr/bin/env python3
"""Verify the degree-60 decomposition divisor ledger."""

from pathlib import Path


NODE = Path(__file__).resolve().parent
ROWS = (
    (2, 30, 6, 0),
    (3, 20, 4, 0),
    (4, 15, 3, 0),
    (5, 12, 2, 2),
    (6, 10, 2, 0),
    (10, 6, 1, 1),
    (12, 5, 1, 0),
    (30, 2, 0, 2),
)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    assert "- **status:** PROVED" in statement
    assert "does not descend `h` to `K`" in statement
    assert "No model of `h` over the deployed field" in contract

    for inner, outer, order_five, simple in ROWS:
        assert inner * outer == 60
        assert 5 * order_five + simple == outer
        assert simple == 0 or inner % 5 == 0
        source_points = order_five * inner + simple * (inner // 5)
        assert source_points == 12
        assert outer * inner == 60
    print("RATE_HALF_KB_DEGREE60_DECOMPOSITION_DIVISOR_ADAPTER_PASS")


if __name__ == "__main__":
    main()
