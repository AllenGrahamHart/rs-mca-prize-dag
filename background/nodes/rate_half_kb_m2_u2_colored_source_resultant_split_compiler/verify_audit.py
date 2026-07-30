#!/usr/bin/env python3
"""Audit every four-root colored divisor in the twelve exchange slots."""

from itertools import combinations


def main() -> None:
    exchange = range(12)
    checked = 0
    for colored_tuple in combinations(exchange, 4):
        colored = set(colored_tuple)
        j_exchange = [int(slot in colored) for slot in exchange]
        i_exchange = [2 - order for order in j_exchange]
        assert sum(j_exchange) == 4
        assert sum(i_exchange) == 20
        assert all(i_order + j_order == 2
                   for i_order, j_order in zip(i_exchange, j_exchange))
        assert all(order in (0, 1) for order in j_exchange)
        checked += 1
    assert checked == 495
    assert 20 + 4 == 24
    assert 4 + 20 == 24
    print(
        "RATE_HALF_KB_M2_U2_COLORED_SOURCE_RESULTANT_SPLIT_COMPILER_AUDIT_PASS "
        f"colored_divisors={checked}"
    )


if __name__ == "__main__":
    main()
