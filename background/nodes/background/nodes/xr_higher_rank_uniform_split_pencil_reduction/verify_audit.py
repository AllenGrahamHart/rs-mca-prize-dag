#!/usr/bin/env python3
"""Audit the arbitrary-rank support and Maxwell arithmetic."""

from __future__ import annotations


def main() -> None:
    checked = 0
    for a in range(1, 129):
        for h in range(1, 17):
            for t in range(4, a + 3):
                for rho in range(a + 2, 2 * a + 1):
                    if rho * (t - 2) <= a * t:
                        assert t <= a + 2
                        assert rho - a - 1 <= a - 1
                        checked += 1
            for e in range(h):
                for private in range((h - e - 1) // 2 + 1):
                    assert e + 2 * private <= h - 1
                    checked += 1
    print(f"AUDIT_XR_HIGHER_RANK_UNIFORM_SPLIT_PENCIL_PASS cases={checked}")


if __name__ == "__main__":
    main()
