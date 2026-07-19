#!/usr/bin/env python3
"""Audit bounded A=1 core/degree/slack profiles and chamber widths."""

from __future__ import annotations


def main() -> None:
    profiles = 0
    positive_saturation = 0
    chambers = 0
    for m in range(6, 72):
        rho = 4 * m
        domain = 4 * rho
        for core in range(3):
            residual_degree = rho - core
            for degree in range(m + 1, residual_degree // (core + 1) + 1):
                regular = residual_degree - (core + 1) * degree
                total = (domain - core) * degree + regular
                cap, remainder = divmod(total, residual_degree)
                beta = cap - 4 * degree
                defect = 4 * degree - residual_degree
                coefficient = 4 * defect + 4 * beta - 3 * core
                assert regular + remainder < 2 * cap
                if core in (1, 2):
                    assert regular + remainder < cap
                for component_degree in range(1, degree + 1):
                    lower_num = coefficient * component_degree - regular
                    upper_num = coefficient * component_degree + remainder
                    lower = -((-lower_num) // cap)
                    upper = upper_num // cap
                    assert max(0, upper - lower + 1) <= 2
                    chambers += 1
                for supported in range(rho + 2, cap + 1):
                    slack = cap - supported
                    for omission in {0, regular // 2, regular}:
                        capacity = (domain - core) * degree - (
                            supported * residual_degree - omission
                        )
                        assert capacity == slack * residual_degree + remainder - regular + omission
                        if capacity < 0:
                            continue
                        assert capacity <= slack * residual_degree + remainder
                        guaranteed = max(
                            0, (domain - core) - slack * residual_degree - remainder
                        )
                        assert guaranteed <= max(0, (domain - core) - capacity)
                        profiles += 1
                        positive_saturation += guaranteed > 0

    assert profiles > 100_000
    assert positive_saturation > 0
    print(
        "AUDIT_RATE_HALF_CA_HANKEL_HALF_DISTANCE_A1_CORE_SLOPE_SLACK_PASS "
        f"profiles={profiles} chambers={chambers} "
        f"positive_saturation_profiles={positive_saturation}"
    )


if __name__ == "__main__":
    main()
