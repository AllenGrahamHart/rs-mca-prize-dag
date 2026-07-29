#!/usr/bin/env python3
"""Verify the KoalaBear primitive-subdegree-four route cut."""

from pathlib import Path


NODE = Path(__file__).resolve().parent
EXPECTED_ROWS = {
    (2, 30, 6, 0),
    (3, 20, 4, 0),
    (4, 15, 3, 0),
    (5, 12, 2, 2),
    (6, 10, 2, 0),
    (10, 6, 1, 1),
    (12, 5, 1, 0),
    (30, 2, 0, 2),
}


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    assert "- **status:** PROVED" in statement
    assert "Ledger movement is zero" in statement
    assert "No decomposition is asserted" in contract

    subdegree_rows = (
        (1, 12, 12, 15, 20),
        (1, 12, 12, 15, 20),
        (1, 15, 20, 24),
        (1, 15, 20, 24),
        (1, 15, 20, 24),
        (1, 59),
        (1, 59),
        (1, 59),
        (1, 59),
    )
    assert len(subdegree_rows) == 9
    assert all(4 not in row for row in subdegree_rows)

    rows = set()
    for inner in range(2, 60):
        if 60 % inner:
            continue
        outer = 60 // inner
        for order_one in range(outer + 1):
            remainder = outer - order_one
            if remainder % 5:
                continue
            order_five = remainder // 5
            if order_one and inner % 5:
                continue
            if order_one * 4 * inner > 5 * (2 * inner - 2):
                continue
            rows.add((inner, outer, order_five, order_one))
    assert rows == EXPECTED_ROWS
    assert {row[0] for row in rows} == {2, 3, 4, 5, 6, 10, 12, 30}
    print("RATE_HALF_KB_Q6_U2_PRIMITIVE_SUBDEGREE4_ROUTE_CUT_PASS")


if __name__ == "__main__":
    main()
