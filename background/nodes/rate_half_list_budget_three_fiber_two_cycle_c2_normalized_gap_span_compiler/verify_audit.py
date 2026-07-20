#!/usr/bin/env python3
"""Mutation audit for the normalized c=2 gap-span compiler."""

from __future__ import annotations

import verify


def main() -> None:
    height = 3
    denominator = [1, 71, 13, 70, 39]
    correct = verify.fourth_root_coefficients(denominator, 3 * height)
    product = verify.poly_mul(
        denominator, verify.fourth_power(correct, 3 * height), 3 * height
    )
    assert product == [1] + [0] * (3 * height - 1)

    wrong_weight = verify.fourth_root_coefficients(
        denominator, 3 * height, weight_shift=1
    )
    wrong_product = verify.poly_mul(
        denominator,
        verify.fourth_power(wrong_weight, 3 * height),
        3 * height,
    )
    assert wrong_product != product

    wrong_sign = denominator[:]
    wrong_sign[3] = -wrong_sign[3] % verify.PRIME
    assert wrong_sign != verify.denominator_from_roots((1, 84, 67, 68))

    _, _, residual_bar, leading, canonical, windows = (
        verify.primary_two_window_packet(denominator, height)
    )
    assert residual_bar[0] == 4 * leading % verify.PRIME
    assert residual_bar[0] != leading
    assert canonical == windows

    shifted_high = correct[2 * height - 1 : 3 * height - 1]
    low = correct[:height]
    wrong_windows = [
        value * pow(leading, -1, verify.PRIME) % verify.PRIME
        for value in verify.poly_mul(low, shifted_high, height)
    ]
    assert wrong_windows != windows

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_NORMALIZED_GAP_SPAN_AUDIT_PASS "
        "mutations=4"
    )


if __name__ == "__main__":
    main()
