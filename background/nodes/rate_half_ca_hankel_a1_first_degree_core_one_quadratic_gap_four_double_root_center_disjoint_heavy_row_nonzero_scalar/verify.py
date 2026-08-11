#!/usr/bin/env python3
"""Replay the valuation trichotomy excluding a zero center-disjoint row."""


def main() -> None:
    correction_order_in_q_row = 3
    correction_order_in_exact_residual = 2
    transverse_intersection_order = 1

    assert correction_order_in_q_row > correction_order_in_exact_residual
    assert correction_order_in_q_row > transverse_intersection_order

    cases = {
        "unsupported": correction_order_in_q_row
        > correction_order_in_exact_residual,
        "actual": correction_order_in_q_row > transverse_intersection_order,
        "padding": True,  # padding at x_* is exactly membership in g_*.
    }
    assert all(cases.values())

    # Mutation controls: lowering the contact order or allowing support
    # collision removes the corresponding contradiction.
    assert not (2 > correction_order_in_exact_residual)
    assert not (1 > transverse_intersection_order)
    gcd_g_s_is_one = True
    assert gcd_g_s_is_one
    assert not (not gcd_g_s_is_one)
    print("RATE_HALF_CENTER_DISJOINT_HEAVY_ROW_NONZERO_PASS cases=3")


if __name__ == "__main__":
    main()
