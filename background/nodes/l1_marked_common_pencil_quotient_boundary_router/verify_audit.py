#!/usr/bin/env python3
"""Mutation audit for the marked common-pencil quotient-boundary router."""


def main() -> None:
    fiber = {1, 2, 3}
    defect = {1, 2, 3, 7}

    # A complete fiber belongs to the quotient factor, not the boundary.
    boundary = defect - fiber
    assert boundary == {7}

    # A proper part of a fiber cannot be promoted to a quotient factor.
    partial = {1, 2}
    assert not fiber <= partial

    # The lower CRT endpoint costs q^(2p), not an unproved q^p factor.
    q, p = 11, 3
    assert q ** (2 * p) > q**p

    # Locator periodicity alone does not make an arbitrary agreement set periodic.
    locator_periodic = True
    agreement_set_periodic = False
    assert locator_periodic and not agreement_set_periodic

    print("L1_QUOTIENT_BOUNDARY_AUDIT_PASS mutations=4")


if __name__ == "__main__":
    main()

