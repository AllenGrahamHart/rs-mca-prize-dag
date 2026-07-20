#!/usr/bin/env python3
"""Mutation audit for the next-strip boundary fiber bound."""


def main() -> None:
    polarity_cap = 4
    ell = 2 * polarity_cap
    p = gap = polarity_cap

    # At ell=2P_0 the t=m contradiction can become equality.
    assert ell == p + gap

    # Losing the strict background cap loses one unit in the threshold.
    strict_remainder = ell - 1
    nonstrict_remainder = ell
    assert nonstrict_remainder == strict_remainder + 1

    # Marks can make deg S<=d even with t=m+1.
    m = 3
    d = (m + 1) * ell - 1
    v = p
    support_degree = (m + 1) * ell - v
    assert support_degree <= d

    # The affine coefficient count includes the constant coefficient.
    freedom_degree = v - 1
    assert freedom_degree + 1 == v

    print("L1_NEXT_STRIP_BOUNDARY_AUDIT_PASS mutations=4")


if __name__ == "__main__":
    main()

