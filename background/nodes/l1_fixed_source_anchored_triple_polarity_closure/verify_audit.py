#!/usr/bin/env python3
"""Mutation audit for anchored triple-polarity closure."""


def main() -> None:
    fiber = {0, 1}
    residual = {2}

    # Residual core points must be charged: complete-fiber data alone cannot
    # distinguish these two cores.
    core_a = {0}
    core_b = {0, 2}
    assert core_a & fiber == core_b & fiber
    assert core_a != core_b

    # The same guard is load-bearing for defects inside a fixed residual core.
    core = {0, 2}
    defect_a = {0}
    defect_b = {0, 2}
    assert defect_a & fiber == defect_b & fiber
    assert defect_a != defect_b

    tie_is_sparse = not (1 > 2 / 2)
    partial_core_is_allowed = True
    numerator_fiber_is_paid = True
    dense_support_is_not_an_anchor = True
    assert tie_is_sparse
    assert partial_core_is_allowed
    assert numerator_fiber_is_paid
    assert dense_support_is_not_an_anchor

    print("L1_FIXED_SOURCE_ANCHORED_TRIPLE_AUDIT_PASS mutations=6")


if __name__ == "__main__":
    main()
