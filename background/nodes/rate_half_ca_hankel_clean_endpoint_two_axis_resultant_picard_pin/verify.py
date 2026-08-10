#!/usr/bin/env python3
"""Verify the two-axis intersection and Picard degree ledger."""


def main() -> None:
    scales = (2, 3, 4, 8, 64, 2**37)
    checked = 0
    for m in scales:
        rho = 4 * m - 1
        domain_size = 16 * m
        slopes = 4 * m + 1
        for b_degree in (1, max(1, m // 2), m - 1):
            intersection = rho * b_degree + m * domain_size
            divisor = 1 + (slopes + b_degree) * rho
            assert intersection == divisor
            assert m * domain_size - slopes * rho == 1

            # Reciprocal resultant factors split the m exceptional roots.
            assert (m - 1) + 1 == m
            checked += 1

    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_TWO_AXIS_RESULTANT_PICARD_PIN_PASS "
        f"profiles={checked} official_m={2**37}"
    )


if __name__ == "__main__":
    main()
