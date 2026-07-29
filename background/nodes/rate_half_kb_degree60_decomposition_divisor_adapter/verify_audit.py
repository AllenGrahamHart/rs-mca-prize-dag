#!/usr/bin/env python3
"""Independently reconstruct the divisor and ramification profiles."""


EXPECTED = {2, 3, 4, 5, 6, 10, 12, 30}


def main() -> None:
    rows = []
    for inner in range(2, 60):
        if 60 % inner:
            continue
        outer = 60 // inner
        for simple in range(outer + 1):
            if (outer - simple) % 5:
                continue
            order_five = (outer - simple) // 5
            if simple and inner % 5:
                continue
            forced = simple * 4 * inner // 5
            if forced > 2 * inner - 2:
                continue
            if order_five * inner + simple * (inner // 5) != 12:
                continue
            rows.append((inner, outer, order_five, simple))
    assert {row[0] for row in rows} == EXPECTED
    assert len(rows) == 8
    assert all((60 // inner) * inner == 60 for inner in EXPECTED)
    print("RATE_HALF_KB_DEGREE60_DECOMPOSITION_DIVISOR_ADAPTER_AUDIT_PASS")


if __name__ == "__main__":
    main()
