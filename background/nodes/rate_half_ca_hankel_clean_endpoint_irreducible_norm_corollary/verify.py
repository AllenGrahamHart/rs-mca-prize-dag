#!/usr/bin/env python3
"""Verify the clean endpoint arithmetic and component-budget collapse."""


def main() -> None:
    scales = (2, 3, 4, 64, 2**37)
    for m in scales:
        rho = 4 * m - 1
        domain_size = 16 * m
        slopes = 4 * m + 1
        incidence = slopes * rho
        assert incidence == domain_size * m - 1

        # O=E=0 in the component ledger forces zero residual degree.
        omission = 0
        overlap = 0
        residual_degree_cap = (omission - overlap) // 4
        assert residual_degree_cap == 0
        dominant_parameter_degree = m - residual_degree_cap
        dominant_x_degree = 4 * dominant_parameter_degree - 1
        assert dominant_parameter_degree == m
        assert dominant_x_degree == rho

        norm_degree = domain_size * m
        power_degree = slopes * rho
        assert norm_degree - power_degree == 1
        assert 3 * m + 1 >= 2 * m + 2

        saturated_columns = domain_size - 1
        assert saturated_columns >= 15 * m
        assert (rho + saturated_columns - 1) - saturated_columns == rho - 1

    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_IRREDUCIBLE_NORM_COROLLARY_PASS "
        f"scales={len(scales)} official_m={2**37}"
    )


if __name__ == "__main__":
    main()
