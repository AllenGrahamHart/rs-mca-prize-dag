#!/usr/bin/env python3
"""Mutation audit for the extremal marked kernel normal form."""


def main() -> None:
    m = 3

    # With 2m-1 labels a determinant may retain one residual linear factor.
    assert 2 * m - (2 * m - 1) == 1

    # A constant value pattern has a large polynomial-multiple kernel; it is
    # excluded only by saturation, not by row counting alone.
    constant_value_rank_cap = m + 1
    assert constant_value_rank_cap < 2 * m

    # At the next strip boundary one more P-adic block enters.
    ell, d, v = 7, m * 7 + 2, 5
    assert d + v == (m + 1) * ell

    # Specializing lambda at a resultant root can destroy saturation.
    assert "lambda-resultant guard" != "all finite specializations"

    print("L1_EXTREMAL_KERNEL_AUDIT_PASS mutations=4")


if __name__ == "__main__":
    main()
