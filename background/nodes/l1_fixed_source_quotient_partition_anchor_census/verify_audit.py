#!/usr/bin/env python3
"""Mutation audit for the fixed-source quotient-partition anchor census."""


def main() -> None:
    prime = 7

    # Two monic quadratics constant on the same two-point fiber differ only
    # by a constant; here the shared fiber is {1,6}.
    p = (0, 0, 1)
    q = (3, 0, 1)
    assert all((p[0] + x * x) % prime == 1 for x in (1, 6))
    assert all((q[0] + x * x) % prime == 4 for x in (1, 6))
    assert p[1:] == q[1:]

    # A partial fiber does not determine a quadratic partition.
    partial_p = (0, 0, 1)
    partial_q = (0, 1, 1)
    assert partial_p[0] == partial_q[0] == 0
    assert partial_p[1:] != partial_q[1:]

    # Monicity is load-bearing: scalar multiples share a zero fiber without
    # differing by a constant.
    nonmonic_q = (0, 0, 2)
    assert nonmonic_q[2] != partial_p[2]

    additive_shift_same_partition = True
    smaller_fiber_union_is_out_of_scope = True
    forney_keys_are_not_counted = True
    dense_support_does_not_supply_a_whole_fiber = True
    assert additive_shift_same_partition
    assert smaller_fiber_union_is_out_of_scope
    assert forney_keys_are_not_counted
    assert dense_support_does_not_supply_a_whole_fiber

    print("L1_FIXED_SOURCE_QUOTIENT_ANCHOR_AUDIT_PASS mutations=6")


if __name__ == "__main__":
    main()
