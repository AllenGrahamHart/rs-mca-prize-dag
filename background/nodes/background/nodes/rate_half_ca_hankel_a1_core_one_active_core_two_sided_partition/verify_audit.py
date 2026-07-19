#!/usr/bin/env python3
"""Audit two-sided partition and active-incidence degree arithmetic."""

from __future__ import annotations


def main() -> None:
    profiles = 0
    for e in range(8, 512, 5):
        d0 = 8 * e + 7
        t = 4 * e + 1
        for b in range((e - 2) // 5 + 1):
            e_star = e - b
            r = 2 * e_star + 1
            for slope_deficit in (0, 1):
                capacity = e - 5 * b - 1 + slope_deficit
                if capacity < 1:
                    continue
                for z in (0, 1):
                    assert r + (d0 - z - r) == d0 - z
                    assert e_star + (t - e_star) == t
                for c in (1, capacity):
                    for exceptional_bad in range(c + 1 if slope_deficit else 1):
                        direct = c * e_star - capacity - exceptional_bad
                        if not slope_deficit:
                            explicit = (c - 1) * e + (5 - c) * b + 1
                        else:
                            explicit = (c - 1) * e + (5 - c) * b - exceptional_bad
                        assert direct == explicit
                        profiles += 1

    # Mutation fences: a degree-(r-1) clean fiber misses one unit, and
    # omitting E_bad overcounts clean incidences when D_*=1.
    d0, r, z = 100, 21, 1
    assert (r - 1) + (d0 - z - r) == d0 - z - 1
    e, b, c, exceptional_bad = 18, 1, 2, 1
    capacity = e - 5 * b
    direct = c * (e - b) - capacity - exceptional_bad
    assert direct != (c - 1) * e + (5 - c) * b

    print(
        "AUDIT_RATE_HALF_CA_HANKEL_A1_CORE_ONE_ACTIVE_TWO_SIDED_PARTITION_PASS "
        f"profiles={profiles} mutations=2"
    )


if __name__ == "__main__":
    main()
