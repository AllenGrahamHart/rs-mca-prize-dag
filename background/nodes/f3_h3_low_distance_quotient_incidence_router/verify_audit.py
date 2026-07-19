#!/usr/bin/env python3
"""Audit the rational formulas in both distance-four covers."""

from __future__ import annotations


def main() -> None:
    checked_generic = 0
    checked_antipodal = 0
    for prime in (97, 193, 257):
        for u in range(2, min(prime, 40)):
            for y in range(2, min(prime, 40)):
                if y == 1 or u == 1:
                    continue
                x = (u * u - y) * pow(u * (1 - y) % prime, prime - 2, prime) % prime
                v = -y * pow(u, prime - 2, prime) % prime
                assert (1 - x) * (1 - y) % prime == (1 - u) * (1 - v) % prime
                checked_generic += 1
            for x in range(2, min(prime, 40)):
                v = (x * x - u) * pow(1 - u, prime - 2, prime) % prime
                assert (1 - u) * (1 - v) % prime == (1 - x * x) % prime
                checked_antipodal += 1
    assert checked_generic and checked_antipodal
    print(
        "AUDIT_F3_H3_LOW_DISTANCE_QUOTIENT_INCIDENCE_ROUTER_PASS "
        f"generic={checked_generic} antipodal={checked_antipodal}"
    )


if __name__ == "__main__":
    main()
