#!/usr/bin/env python3
"""Verify exact clean boundary and resultant degree saturation."""


def main() -> None:
    scales = (2, 3, 4, 8, 64, 2**37)
    checked = 0
    for m in scales:
        rho = 4 * m - 1
        domain_size = 16 * m
        slopes = 4 * m + 1
        for b_degree in (1, max(1, m // 2), m - 1):
            resultant_degree = (slopes + b_degree) * rho + 1
            degree_without_b = resultant_degree - b_degree * rho
            assert degree_without_b == slopes * rho + 1
            assert degree_without_b == m * domain_size
            forced_x_degree = (degree_without_b + m - 1) // m
            assert forced_x_degree == domain_size

            # An off-by-one exponent would no longer force saturation.
            weakened = (slopes - 1) * rho + 1
            assert weakened < m * domain_size
            checked += 1

    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_RESULTANT_BOUNDARY_SATURATION_PASS "
        f"profiles={checked} official_m={2**37}"
    )


if __name__ == "__main__":
    main()
