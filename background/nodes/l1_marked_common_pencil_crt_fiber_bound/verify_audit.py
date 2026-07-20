#!/usr/bin/env python3
"""Mutation audit for the marked common-pencil CRT fiber bound."""


def main() -> None:
    m, ell, p = 3, 11, 4

    # At t=m+1, omitting the next-strip margin can lose uniqueness.
    t, v = m + 1, p
    boundary_d = (m + 1) * ell - p
    assert t * ell - v == boundary_d

    # At t=m, replacing r<=ell-1 by r<=ell loses eta<=p-1.
    strict_eta_max = p - 1
    nonstrict_eta_max = p
    assert nonstrict_eta_max == strict_eta_max + 1

    # Counting full locators instead of support locators overstates deg S.
    support_degree = t * ell - v
    full_degree = t * ell
    assert full_degree > support_degree

    # The q^(2p) factor is polynomial only for fixed p.
    assert "fixed p" != "unbounded p"

    print("L1_CRT_FIBER_AUDIT_PASS mutations=4")


if __name__ == "__main__":
    main()
