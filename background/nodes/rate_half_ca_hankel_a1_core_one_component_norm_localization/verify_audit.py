#!/usr/bin/env python3
"""Audit component norm-degree and saturation identities."""

from __future__ import annotations


def main() -> None:
    dominant_profiles = 0
    residual_profiles = 0
    for m in range(3, 256):
        e = 2 * m - 1
        residual_domain = 16 * m - 1
        supported = 4 * e + 1
        for residual_e in range(e // 5 + 1):
            dominant_e = e - residual_e
            difference = residual_domain * dominant_e - supported * (2 * dominant_e + 1)
            assert difference == e - 5 * residual_e - 1
            for omission in (0, 1):
                capacity = difference + omission
                if capacity >= 0:
                    assert residual_domain - capacity >= 14 * m + 5 * residual_e
                dominant_profiles += 1
        for component_e in range(1, e + 1):
            assert residual_domain * component_e - supported * 2 * component_e == 5 * component_e
            residual_profiles += 1
    print(
        "AUDIT_RATE_HALF_CA_HANKEL_A1_CORE_ONE_COMPONENT_NORM_PASS "
        f"dominant_profiles={dominant_profiles} residual_profiles={residual_profiles}"
    )


if __name__ == "__main__":
    main()
