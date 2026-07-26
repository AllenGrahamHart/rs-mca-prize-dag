#!/usr/bin/env python3
"""Exhaust the small set-system core of fixed-union Johnson."""

from itertools import combinations


def main() -> None:
    checks = 0
    for n in range(2, 6):
        universe = range(n)
        for nu in range(1, n):
            for h in range(1, n + 1):
                denom = h * h - n * (nu - 1)
                if denom <= 0:
                    continue
                blocks = list(combinations(universe, h))
                for mask in range(1 << len(blocks)):
                    family = [set(blocks[i]) for i in range(len(blocks))
                              if mask & (1 << i)]
                    if any(len(a & b) > nu - 1
                           for a, b in combinations(family, 2)):
                        continue
                    bound = n * (h - nu + 1) // denom
                    assert len(family) <= bound
                    checks += 1
    print(f"AUDIT_UPSTREAM_GFV4_FIXED_UNION_JOHNSON_PASS checks={checks}")


if __name__ == "__main__":
    main()
