#!/usr/bin/env python3
"""Audit all small strict A=3 slope-slack arithmetic profiles."""

from __future__ import annotations


def main() -> None:
    profiles = 0
    saturated_profiles = 0
    for m in range(2, 97):
        rho = 4 * m - 1
        domain = 16 * m
        for e in range(m, rho // 3 + 1):
            regular = rho - 3 * e
            defect = 4 * e - rho
            sharp_cap = 4 * e + 1
            for component_e in range(1, e + 1):
                lower_numerator = 4 * defect * component_e - (e - defect)
                upper_numerator = 4 * defect * component_e + e
                lower = -((-lower_numerator) // sharp_cap)
                upper = upper_numerator // sharp_cap
                assert upper < lower or upper == lower
            for supported in range(rho + 2, 4 * e + 2):
                h = 4 * e + 1 - supported
                assert 0 <= h <= 4 * (e - m)
                for omission in {0, regular // 2, regular}:
                    capacity = domain * e - (supported * rho - omission)
                    assert capacity == 4 * e - rho + h * rho + omission
                    assert 0 <= capacity <= e + h * rho
                    guaranteed = max(0, domain - e - h * rho)
                    assert guaranteed <= max(0, domain - capacity)
                    profiles += 1
                    saturated_profiles += guaranteed > 0

    assert profiles > 100_000
    assert saturated_profiles > 0
    print(
        "AUDIT_RATE_HALF_CA_HANKEL_STRICT_A3_SLOPE_SLACK_PASS "
        f"profiles={profiles} positive_saturation_profiles={saturated_profiles}"
    )


if __name__ == "__main__":
    main()
