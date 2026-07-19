#!/usr/bin/env python3
"""Audit all small half-distance A=3 slope-slack profiles."""

from __future__ import annotations


def main() -> None:
    profiles = 0
    positive_saturation = 0
    for m in range(4, 113):
        rho = 4 * m - 1
        domain = 16 * m
        for e in range(m + 1, rho // 3 + 1):
            regular = rho - 3 * e
            defect = 4 * e - rho
            sharp_cap = 4 * e + 1
            for component_e in range(1, e + 1):
                lower_numerator = 4 * defect * component_e - (e - defect)
                upper_numerator = 4 * defect * component_e + e
                lower = -((-lower_numerator) // sharp_cap)
                upper = upper_numerator // sharp_cap
                assert upper < lower or upper == lower
            for supported in range(rho + 3, 4 * e + 2):
                h = 4 * e + 1 - supported
                assert 0 <= h <= 4 * (e - m) - 1
                for omission in {0, regular // 2, regular}:
                    capacity = domain * e - (supported * rho - omission)
                    assert capacity == 4 * e - rho + h * rho + omission
                    assert 0 <= capacity <= e + h * rho
                    guaranteed = max(0, domain - e - h * rho)
                    assert guaranteed <= max(0, domain - capacity)
                    profiles += 1
                    positive_saturation += guaranteed > 0

    assert profiles > 100_000
    assert positive_saturation > 0
    print(
        "AUDIT_RATE_HALF_CA_HANKEL_HALF_DISTANCE_A3_SLOPE_SLACK_PASS "
        f"profiles={profiles} positive_saturation_profiles={positive_saturation}"
    )


if __name__ == "__main__":
    main()
