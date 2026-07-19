#!/usr/bin/env python3
"""Audit the low/high excess split on deterministic exact profiles."""

from __future__ import annotations

import random


def main() -> None:
    rng = random.Random(0xEBD2)
    checked = 0
    for n in (16, 32, 64):
        mass = (n - 1) * (n - 2)
        for cutoff in range(18):
            for _ in range(100):
                remaining = mass
                profile = []
                for excess in range(1, 30):
                    value = rng.randrange(remaining + 1)
                    profile.append((excess, value))
                    remaining -= value
                low = sum(excess * value for excess, value in profile if excess <= cutoff)
                high = sum(excess * value for excess, value in profile if excess > cutoff)
                assert low <= cutoff * mass
                budget = 300 * n * n - 17 * cutoff * mass
                if 17 * high <= budget:
                    assert 17 * (low + high) <= 300 * n * n
                checked += 1
    print(f"AUDIT_F3_H3_EXCESS_BUDGET_DEGREE_TRADEOFF_PASS profiles={checked}")


if __name__ == "__main__":
    main()
