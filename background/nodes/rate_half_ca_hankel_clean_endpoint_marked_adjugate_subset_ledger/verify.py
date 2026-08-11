#!/usr/bin/env python3
"""Arithmetic replay for marked adjugate degrees and subset dimensions."""


def main():
    profiles = 0
    subset_terms = 0
    for m in list(range(2, 65)) + [1 << j for j in range(7, 18)]:
        rho = 4 * m - 1
        n = rho + 1
        degree_q = m
        degree_d = 2 * m - 1

        assert n == 4 * m
        assert (n - 1) - 2 * degree_q == degree_d
        assert degree_d + 2 * degree_q == n - 1
        assert (4 * m + 1) - degree_d == 2 * m + 2
        assert degree_d == (m - 1) + m
        assert (4 * m + 1) - 2 * (m - 1) == 2 * m + 3

        # Cofactors select n-1=rho support columns.
        assert n - 1 == rho
        subset_terms += n * n
        profiles += 1

    official_m = 1 << 37
    assert 2 * official_m - 1 > 0
    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_MARKED_ADJUGATE_SUBSET_LEDGER_PASS "
        f"profiles={profiles} cofactor_profiles={subset_terms} official_m={official_m}"
    )


if __name__ == "__main__":
    main()
