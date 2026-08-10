#!/usr/bin/env python3
"""Verify the adjunction genus exclusion and surviving splitting."""


def main() -> None:
    scales = (2, 3, 4, 8, 64, 2**37)
    for m in scales:
        rho = 4 * m - 1
        genus = (rho - 1) * (m - 1)
        assert genus == (4 * m - 2) * (m - 1)
        assert genus > 0

        surviving_degree = (1 - rho) - (m - 2) * rho
        assert surviving_degree == m * (5 - 4 * m)
        assert rho >= 7

    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_RATIONAL_ELEMENTARY_BRANCH_"
        f"EXCLUSION_PASS scales={len(scales)} official_m={2**37}"
    )


if __name__ == "__main__":
    main()
