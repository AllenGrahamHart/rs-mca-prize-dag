#!/usr/bin/env python3
"""Verify clean Picard cohomology and relative-bundle arithmetic."""


def main() -> None:
    scales = (2, 3, 4, 8, 64, 2**37)
    for m in scales:
        rho = 4 * m - 1
        domain_size = 16 * m
        slopes = 4 * m + 1

        source = (domain_size - rho + 1) * (slopes + m - 1)
        target = (domain_size + 1) * (slopes - 1)
        assert source == 60 * m * m + 10 * m
        assert target == 64 * m * m + 4 * m
        assert source < target
        assert target - source == 4 * m * m - 6 * m

        kernel_rank = (slopes + m - 1) - (slopes - 1)
        kernel_degree = (
            (slopes + m - 1) * (domain_size - rho)
            - (slopes - 1) * domain_size
        )
        assert kernel_rank == m
        assert kernel_degree == m * (5 - 4 * m)
        assert kernel_degree < 0

    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_PICARD_MULTIPLICATION_"
        f"INJECTIVITY_REDUCTION_PASS scales={len(scales)} official_m={2**37}"
    )


if __name__ == "__main__":
    main()
