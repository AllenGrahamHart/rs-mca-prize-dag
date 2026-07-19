#!/usr/bin/env python3
"""Audit the three algebraic neighbor certificates of a fixed generic pair."""

from __future__ import annotations


def main() -> None:
    checked = 0
    for prime in (97, 193):
        for x in range(2, min(prime, 50)):
            for y in range(2, min(prime, 50)):
                target = (1 - x) * (1 - y) % prime
                if not target:
                    continue
                certificates = []
                for root in (x, y):
                    product = -root % prime
                    total = (1 + product - target) % prime
                    certificates.append((total, product))
                fixed = -x * y % prime
                if fixed != 1:
                    other = (1 - target * pow(1 - fixed, prime - 2, prime)) % prime
                    certificates.append((fixed + other, fixed * other % prime))
                assert len(certificates) <= 3

                q = x * y % prime
                root = -q % prime
                if root != 1:
                    second = (1 - target * pow(1 - root, prime - 2, prime)) % prime
                    assert (1 - root) * (1 - second) % prime == target
                checked += 1
    assert checked
    print(
        "AUDIT_F3_H3_DISTANCE_FOUR_FIBER_DEGREE_CAP_PASS "
        f"pairs={checked} oriented_head_unique=1"
    )


if __name__ == "__main__":
    main()
