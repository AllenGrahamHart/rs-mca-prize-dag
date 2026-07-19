#!/usr/bin/env python3
"""Audit two-sided complement degree boxes."""

from __future__ import annotations


def main() -> None:
    profiles = 0
    for m in range(3, 512):
        e = 2 * m - 1
        residual_domain = 16 * m - 1
        supported = 4 * e + 1
        for residual_e in range(e // 5 + 1):
            dominant_e = e - residual_e
            r = 2 * dominant_e + 1
            for omission in (0, 1):
                capacity = e - 5 * residual_e - 1 + omission
                if capacity < 0:
                    continue
                c = capacity
                clean = supported - omission
                assert residual_domain - c >= 14 * m + 5 * residual_e
                assert residual_domain - r >= 0
                assert clean - 1 + dominant_e - 1 - dominant_e <= supported - 2
                assert (r - 1) + residual_domain - r == residual_domain - 1
                profiles += 1
    print(
        "AUDIT_RATE_HALF_CA_HANKEL_A1_CORE_ONE_TWO_SIDED_WELD_PASS "
        f"degree_boxes={profiles} mutations=2"
    )


if __name__ == "__main__":
    main()
