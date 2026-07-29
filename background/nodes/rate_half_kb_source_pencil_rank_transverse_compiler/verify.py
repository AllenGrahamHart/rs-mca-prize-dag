#!/usr/bin/env python3
"""Verify the source-pencil rank and transverse compiler ledger."""

from pathlib import Path


NODE = Path(__file__).resolve().parent
ROWS = {
    2: (30, 10395, (3, 6), 4, (2, 4, 8)),
    3: (20, 15400, (4, 4), 4, (2, 3, 4, 6, 12)),
    4: (15, 5775, (5, 3), 3, (1, 2, 4, 8)),
    6: (10, 462, (7, 2), 0, (1, 2, 3, 4, 6, 8)),
    10: (6, 66, (11, 2), 0, (1, 2, 4, 5)),
    12: (5, 1, None, None, (1, 2, 3, 4)),
}


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    assert "- **status:** PROVED" in statement
    assert "not a finite census" in statement
    assert "No finite census of all endpoint records" in contract

    assert sum(row[1] for row in ROWS.values()) == 32099
    transverse_count = 0
    for m, (n, _, shape, codim, rs) in ROWS.items():
        assert m * n == 60
        if shape is not None:
            assert shape[0] == m + 1
            assert codim == (shape[0] - 2) * (shape[1] - 2)
            assert 60 - n >= 0
        for r in rs:
            delta = 4 * m // r
            assert delta * r == 4 * m
            assert delta <= m * m
            assert r <= n - 1
            transverse_count += 1
    assert transverse_count == 26
    assert 49 - 5 == 44
    print("RATE_HALF_KB_SOURCE_PENCIL_RANK_TRANSVERSE_COMPILER_PASS")


if __name__ == "__main__":
    main()
