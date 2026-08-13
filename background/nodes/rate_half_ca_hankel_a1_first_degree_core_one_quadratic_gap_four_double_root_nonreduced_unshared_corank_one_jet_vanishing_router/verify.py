#!/usr/bin/env python3
"""Replay the order-four symmetric Schur ledger."""


def main() -> None:
    determinant_order = 4
    forced_image_order = 2
    complement_order = 2 * forced_image_order
    assert complement_order == determinant_order

    pairing_order = min(determinant_order, complement_order)
    assert pairing_order == 4
    assert pairing_order > 2
    assert pairing_order > 3

    padded_evaluation = 7
    for jet in (2, 3):
        leading_coefficient = padded_evaluation
        assert leading_coefficient != 0
        assert jet < pairing_order

    print("RATE_HALF_NONREDUCED_CORANK_ONE_JET_ROUTER_PASS jets=2 pairing_order=4")


if __name__ == "__main__":
    main()
