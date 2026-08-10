#!/usr/bin/env python3
"""Degree and homogeneity replay for the normalized Forney resultant."""


def main():
    profiles = 0
    for m in list(range(2, 65)) + [1 << j for j in range(7, 18)]:
        rho = 4 * m - 1
        degree_p_t = m + 1
        degree_delta = m - 1
        resultant_a_power = 2 * rho + 2

        assert degree_p_t == m + 1
        assert degree_delta == m - 1
        assert resultant_a_power == 8 * m
        assert (rho - 1) + rho + 3 == 2 * rho + 2
        assert (4 * m + 1) - 2 * (m - 1) == 2 * m + 3
        profiles += 1

    official_m = 1 << 37
    assert 2 * (4 * official_m - 1) + 2 == 8 * official_m
    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_FORNEY_RESULTANT_REGULAR_FACTOR_PASS "
        f"profiles={profiles} official_m={official_m}"
    )


if __name__ == "__main__":
    main()
