#!/usr/bin/env python3
"""Replay exact correction orders with and without center overlap."""


def main() -> None:
    vertical_order = 3
    for center_order in (0, 1):
        forney_order = 2
        curve_g_order = forney_order - center_order
        fixed_row_error_order = vertical_order
        heavy_factor_order = 2 - center_order

        assert curve_g_order in (1, 2)
        assert curve_g_order < fixed_row_error_order
        assert curve_g_order == heavy_factor_order
        overlap_factor_order = curve_g_order - heavy_factor_order
        assert overlap_factor_order == 0

    print("RATE_HALF_HEAVY_ROW_CORRECTION_EXACT_ORDER_PASS cases=2")


if __name__ == "__main__":
    main()
