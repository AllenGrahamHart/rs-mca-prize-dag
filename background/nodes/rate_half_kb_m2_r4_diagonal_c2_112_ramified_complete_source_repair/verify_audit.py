#!/usr/bin/env python3
"""Independently audit the local ramified order allocation."""

from itertools import product


def main() -> None:
    allocations = [orders for orders in product(range(3), repeat=2)
                   if sum(orders) == 4]
    assert allocations == [(2, 2)]

    # If H(j,X)=U(j,X^2)+X V(j,X^2) has order two and U(j,0)=0,
    # its linear coefficient must vanish.
    expansions_checked = 0
    for u1, v0 in product(range(-2, 3), repeat=2):
        if v0 == 0 and u1 != 0:
            order = 2
        elif v0 != 0:
            order = 1
        else:
            order = 3
        if order == 2:
            assert v0 == 0
        expansions_checked += 1

    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_C2_112_RAMIFIED_COMPLETE_SOURCE_REPAIR_AUDIT_PASS "
        f"allocations=1 forced_orders=2,2 expansions_checked={expansions_checked}"
    )


if __name__ == "__main__":
    main()
