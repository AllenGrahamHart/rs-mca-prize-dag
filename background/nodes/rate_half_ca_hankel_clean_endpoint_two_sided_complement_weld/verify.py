#!/usr/bin/env python3
"""Verify the clean two-sided-complement degree ledger."""


def main() -> None:
    scales = (2, 3, 4, 8, 64, 2**37)
    for m in scales:
        rho = 4 * m - 1
        domain_size = 16 * m
        slopes = 4 * m + 1

        degree_x_a = domain_size - rho
        degree_z_a = slopes - 1
        degree_z_b = m + degree_z_a - slopes
        degree_x_b = max(domain_size, rho + degree_x_a)

        assert degree_x_a == 12 * m + 1
        assert degree_z_b == m - 1
        assert degree_x_b == domain_size

        degree_z_w = slopes
        degree_x_w = rho - 1
        degree_z_k = degree_z_w + degree_z_b - m
        degree_x_k = degree_x_w + degree_x_b - rho

        assert degree_z_k == slopes - 1 == 4 * m
        assert degree_x_k == domain_size - 1

    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_TWO_SIDED_COMPLEMENT_WELD_PASS "
        f"scales={len(scales)} official_m={2**37}"
    )


if __name__ == "__main__":
    main()
